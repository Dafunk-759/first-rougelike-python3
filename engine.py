from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

class Engine:
    def __init__(
        self,
        entities: Set[Entity],
        event_handler: EventHandler,
        player: Entity,
        game_map: GameMap
    ) -> None:
        self.entities = entities
        self.event_handler = event_handler
        self.player = player
        self.game_map = game_map
    

    def handle_event(self, events: Iterable[Any]):
        for event in events:
            action = self.event_handler.dispatch(event)
            if action is None:
                continue

            action.perform(self, self.player)
    

    def render(self, console: Console, context: Context):
        self.game_map.render(console)

        for entity in self.entities:
            console.print(
                x=entity.x,
                y=entity.y,
                string=entity.char,
                fg=entity.color
            )        

        context.present(console)
        console.clear()