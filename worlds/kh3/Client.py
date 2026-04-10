


import asyncio

from pymem import pymem

from CommonClient import gui_enabled, logger, get_base_parser, CommonContext, server_loop
from NetUtils import ClientStatus
from worlds.kh3.Checks import finished_game

class KingdomHeartsIIIContext(CommonContext):
    # command_processor = KingdomHeartsIIICommandProcessor
    game = "Kingdom Hearts III"
    items_handling = 0b111  # Indicates you get items sent from other worlds.

    def __init__(self, server_address, password):
        super(KingdomHeartsIIIContext, self).__init__(server_address, password)


async def kh3_watcher(ctx: KingdomHeartsIIIContext):
    while not ctx.exit_event.is_set():
        try:
            if ctx.kh3connected and ctx.serverconnected:
                ctx.sending = []
                await asyncio.create_task(ctx.checkWorldLocations())
                await asyncio.create_task(ctx.checkLevels())
                await asyncio.create_task(ctx.checkSlots())
                await asyncio.create_task(ctx.verifyChests())
                await asyncio.create_task(ctx.verifyItems())
                await asyncio.create_task(ctx.verifyLevel())
                await asyncio.create_task(ctx.is_dead())

                if (ctx.deathlink_toggle and "DeathLink" not in ctx.tags) or (not ctx.deathlink_toggle and "DeathLink" in ctx.tags):
                    await ctx.update_death_link(ctx.deathlink_toggle)

                if finished_game(ctx) and not ctx.kh3_finished_game:
                    await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                    ctx.kh3_finished_game = True

                if ctx.sending:
                    message = [{"cmd": 'LocationChecks', "locations": ctx.sending}]
                    await ctx.send_msgs(message)

                if ctx.queued_puzzle_popup:
                    await asyncio.create_task(ctx.displayPuzzlePieceTextinGame(ctx.queued_puzzle_popup[0]))  # send the num 1 index of whats in the queue
                if ctx.queued_info_popup:
                    await asyncio.create_task(ctx.displayInfoTextinGame(ctx.queued_info_popup[0]))
                if ctx.queued_chest_popup:
                    await asyncio.create_task(ctx.displayChestTextInGame(ctx.queued_chest_popup[0]))

            elif not ctx.kh3connected and ctx.serverconnected:
                logger.info("Game Connection lost. trying to reconnect.")
                ctx.kh3 = None
                #todo: change this to be an option for the client to auto reconnect with the default being yes
                # reason is because the await sleep causes the client to hang if you close the game then the client without disconnecting.
                while not ctx.kh3connected and ctx.serverconnected:
                    try:
                        ctx.kh3 = pymem.Pymem(process_name="KINGDOM HEARTS III")
                        ctx.get_addresses()
                        logger.info("Game Connection Established.")
                    except Exception as e:
                        await asyncio.sleep(5)
            if ctx.disconnect_from_server:
                ctx.disconnect_from_server = False
                await ctx.disconnect()
        except Exception as e:
            if ctx.kh3connected:
                ctx.kh3connected = False
            logger.info(e)
        await asyncio.sleep(0.5)

def launch():
    async def main(args):
        ctx = KingdomHeartsIIIContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        progression_watcher = asyncio.create_task(
                kh3_watcher(ctx), name="KingdomHeartsIIIProgressionWatcher")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await progression_watcher

        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description="KH3 Client, for text interfacing.")

    args, rest = parser.parse_known_args()
    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()