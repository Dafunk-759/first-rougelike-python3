import tcod

from input_handlers import EventHandler
from entity import Entity
from game_map import GameMap
from engine import Engine

class Main:
    def __init__(self) -> None:
        self.screen_width = 80
        self.screen_height = 50
        self.tileset = tcod.tileset.load_tilesheet(
            "asset/tileset.png", 
            columns=32, 
            rows=8,
            charmap=tcod.tileset.CHARMAP_TCOD
        )
        self.root_console = None
        self.engine = self.create_engine()

    
    def create_engine(self) -> Engine:
        player = Entity(
            int(self.screen_width / 2),
            int(self.screen_height / 2),
            "@",
            (255, 255, 255)
        )

        npc = Entity(
            int(self.screen_width / 2) - 5,
            int(self.screen_height / 2),
            "@",
            (255, 255, 0)
        )

        entities = {
            player,
            npc
        }

        map_width = 80
        map_height = 50

        game_map = GameMap(map_width, map_height)

        return Engine(
            entities=entities, 
            event_handler=EventHandler(), 
            player=player,
            game_map=game_map
        )


    def main_loop(self, context: tcod.context.Context):
        self.engine.render(self.root_console, context)

        events = tcod.event.wait()
        self.engine.handle_event(events)


    def main(self):
        with tcod.context.new_terminal(
            self.screen_width,
            self.screen_height,
            tileset=self.tileset,
            title="First Rougelike game",
        ) as context:
            self.root_console = tcod.Console(
                height=self.screen_height,
                width=self.screen_width,
                order="F"
            )
            while True:
                self.main_loop(context)



if __name__ == "__main__":
    Main().main()