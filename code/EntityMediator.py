from code import EnemyShot
from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.Entity import Entity
from code.PlayerShot import PlayerShot
from code.EnemyShot import EnemyShot


class EntityMediator:
    @staticmethod
    # method private
    def __verify_collision_window(ent:Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity = entity_list[i]
            EntityMediator.__verify_collision_window(entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)