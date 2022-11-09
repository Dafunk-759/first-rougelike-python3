import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

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
        self.event_handler = EventHandler()

        self.player_x = int(self.screen_width / 2)
        self.player_y = int(self.screen_height / 2)

    
    def print_player(self):
        if type(self.root_console) == tcod.Console:
            self.root_console.print(
                self.player_x,
                self.player_y,
                string="@"
            )
    

    def dispatch_event(self, event):
        action = self.event_handler.dispatch(event)

        match action:
            case MovementAction(dx=dx, dy=dy):
                # print(f"dx:{dx}, dy:{dy}")
                self.player_x += dx
                self.player_y += dy
            
            case EscapeAction():
                raise SystemExit()
            
            case None:
                return
    

    def main_loop(self, context: tcod.context.Context):
        self.root_console.clear()

        self.print_player()
        context.present(self.root_console)

        for event in tcod.event.wait():
            self.dispatch_event(event)


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