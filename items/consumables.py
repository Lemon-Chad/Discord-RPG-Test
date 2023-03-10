from objects.items import Consumable, ItemUseResponse
import objects.context as rpgctx

class HealthPotion(Consumable):
    def __init__(self) -> None:
        super().__init__("Health Potion I", "Heals 2 HP", "🧪")
    
    async def on_use(self, context) -> ItemUseResponse:
        player = context.player
        if player.hp >= player.max_hp:
            return ItemUseResponse.fail("Player is already at Max HP")
        player.hp = min(player.hp + 2, player.max_hp)
        return ItemUseResponse.ok("Healed 2 HP")


class HealthPotionII(Consumable):
    def __init__(self) -> None:
        super().__init__("Health Potion II", "Heals 5 HP", "🧪")
    
    async def on_use(self, context) -> ItemUseResponse:
        player = context.player
        if player.hp >= player.max_hp:
            return ItemUseResponse.fail("Player is already at Max HP")
        player.hp = min(player.hp + 5, player.max_hp)
        return ItemUseResponse.ok("Healed 5 HP")


class HealthPotionIII(Consumable):
    def __init__(self) -> None:
        super().__init__("Health Potion III", "Heals 15 HP", "🧪")
    
    async def on_use(self, context) -> ItemUseResponse:
        player = context.player
        if player.hp >= player.max_hp:
            return ItemUseResponse.fail("Player is already at Max HP")
        player.hp = min(player.hp + 15, player.max_hp)
        return ItemUseResponse.ok("Healed 15 HP")


class Grenade(Consumable):
    def __init__(self) -> None:
        super().__init__("Grenade I", "Deals 5 DMG", "🧨")
    
    async def on_use(self, context: rpgctx.BattleContext) -> ItemUseResponse:
        if type(context) != rpgctx.BattleContext:
            return ItemUseResponse.fail("Must be used in battle")
        enemy = context.enemy
        return ItemUseResponse.ok(f"Dealt {enemy.damage(5)} DMG")


class GrenadeII(Consumable):
    def __init__(self) -> None:
        super().__init__("Grenade II", "Deals 10 DMG", "🧨")
    
    async def on_use(self, context: rpgctx.BattleContext) -> ItemUseResponse:
        if type(context) != rpgctx.BattleContext:
            return ItemUseResponse.fail("Must be used in battle")
        enemy = context.enemy
        return ItemUseResponse.ok(f"Dealt {enemy.damage(10)} DMG")


class GrenadeIII(Consumable):
    def __init__(self) -> None:
        super().__init__("Grenade III", "Deals 15 DMG", "🧨")
    
    async def on_use(self, context: rpgctx.BattleContext) -> ItemUseResponse:
        if type(context) != rpgctx.BattleContext:
            return ItemUseResponse.fail("Must be used in battle")
        enemy = context.enemy
        return ItemUseResponse.ok(f"Dealt {enemy.damage(15)} DMG")
