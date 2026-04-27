from dataclasses import dataclass
from typing import TypeAlias

from .items import ItemId

RecipeMaterialId: TypeAlias = ItemId | str

@dataclass(frozen=True)
class Recipe:
    product: ItemId
    materials: dict[RecipeMaterialId, int]

_ITEM_RECIPES: dict[ItemId, Recipe] = {
    ItemId.PalSphere: Recipe(
        product=ItemId.PalSphere,
        materials={
            ItemId.PaldiumFragment: 1,
            ItemId.Wood: 3,
            ItemId.Stone: 3,
        },
    ),
    ItemId.MegaSphere: Recipe(
        product=ItemId.MegaSphere,
        materials={
            ItemId.PaldiumFragment: 1,
            ItemId.Ingot: 1,
            ItemId.Wood: 5,
            ItemId.Stone: 5,
        },
    ),
    ItemId.GigaSphere: Recipe(
        product=ItemId.GigaSphere,
        materials={
            ItemId.PaldiumFragment: 2,
            ItemId.Ingot: 2,
            ItemId.Wood: 7,
            ItemId.Stone: 7,
        },
    ),
    ItemId.HyperSphere: Recipe(
        product=ItemId.HyperSphere,
        materials={
            ItemId.PaldiumFragment: 3,
            ItemId.Ingot: 3,
            ItemId.Wood: 10,
            ItemId.Cement: 2,
        },
    ),
    ItemId.UltraSphere: Recipe(
        product=ItemId.UltraSphere,
        materials={
            ItemId.PaldiumFragment: 5,
            ItemId.RefinedIngot: 5,
            ItemId.CarbonFiber: 2,
            ItemId.Cement: 3,
        },
    ),
    ItemId.LegendarySphere: Recipe(
        product=ItemId.LegendarySphere,
        materials={
            ItemId.PaldiumFragment: 10,
            ItemId.PalMetalIngot: 5,
            ItemId.CarbonFiber: 3,
            ItemId.Cement: 5,
        },
    ),
    ItemId.UltimateSphere: Recipe(
        product=ItemId.UltimateSphere,
        materials={
            ItemId.PaldiumFragment: 20,
            ItemId.PalMetalIngot: 10,
            ItemId.CarbonFiber: 5,
            ItemId.Plasteel: 1,
        },
    ),
    ItemId.ExoticSphere: Recipe(
        product=ItemId.ExoticSphere,
        materials={
            ItemId.PaldiumFragment: 30,
            ItemId.Plasteel: 2,
            ItemId.CarbonFiber: 7,
            ItemId.Hexolite: 1,
        },
    ),
    ItemId.HeavyWeightModule: Recipe(
        product=ItemId.HeavyWeightModule,
        materials={
            ItemId.PaldiumFragment: 10,
            ItemId.Ingot: 10,
            ItemId.Stone: 20,
        },
    ),
    ItemId.CurveModule: Recipe(
        product=ItemId.CurveModule,
        materials={
            ItemId.PaldiumFragment: 30,
            ItemId.Ingot: 30,
            ItemId.Stone: 50,
            ItemId.AncientCivilizationParts: 5,
        },
    ),
    ItemId.SniperModule: Recipe(
        product=ItemId.SniperModule,
        materials={
            ItemId.PaldiumFragment: 50,
            ItemId.Ingot: 50,
            ItemId.Cement: 30,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.SliderModule: Recipe(
        product=ItemId.SliderModule,
        materials={
            ItemId.PaldiumFragment: 100,
            ItemId.RefinedIngot: 50,
            ItemId.CarbonFiber: 50,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.SniperModuleSphereModuleSniper2: Recipe(
        product=ItemId.SniperModuleSphereModuleSniper2,
        materials={
            ItemId.PaldiumFragment: 200,
            ItemId.PalMetalIngot: 50,
            ItemId.CarbonFiber: 30,
            ItemId.AncientCivilizationParts: 30,
            ItemId.AncientCivilizationCore: 5,
        },
    ),
    ItemId.HomingModule: Recipe(
        product=ItemId.HomingModule,
        materials={
            ItemId.Plasteel: 50,
            ItemId.CarbonFiber: 100,
            ItemId.AncientCivilizationParts: 50,
            ItemId.DarkFragment: 50,
            ItemId.AncientCivilizationCore: 10,
        },
    ),
    ItemId.WoodenClub: Recipe(
        product=ItemId.WoodenClub,
        materials={
            ItemId.Wood: 5,
        },
    ),
    ItemId.Bat: Recipe(
        product=ItemId.Bat,
        materials={
            ItemId.Wood: 30,
            ItemId.Stone: 10,
        },
    ),
    ItemId.HandHeldTorch: Recipe(
        product=ItemId.HandHeldTorch,
        materials={
            ItemId.Wood: 2,
            ItemId.Stone: 2,
        },
    ),
    ItemId.MeatCleaver: Recipe(
        product=ItemId.MeatCleaver,
        materials={
            ItemId.Ingot: 5,
            ItemId.Wood: 20,
            ItemId.Stone: 5,
        },
    ),
    ItemId.StonePickaxe: Recipe(
        product=ItemId.StonePickaxe,
        materials={
            ItemId.Stone: 5,
            ItemId.Wood: 5,
        },
    ),
    ItemId.MetalPickaxe: Recipe(
        product=ItemId.MetalPickaxe,
        materials={
            ItemId.Stone: 15,
            ItemId.Wood: 20,
            ItemId.Ingot: 5,
        },
    ),
    ItemId.RefinedMetalPickaxe: Recipe(
        product=ItemId.RefinedMetalPickaxe,
        materials={
            ItemId.Stone: 30,
            ItemId.Wood: 40,
            ItemId.RefinedIngot: 10,
        },
    ),
    ItemId.PalMetalPickaxe: Recipe(
        product=ItemId.PalMetalPickaxe,
        materials={
            ItemId.Stone: 50,
            ItemId.Wood: 100,
            ItemId.PalMetalIngot: 10,
        },
    ),
    ItemId.StoneAxe: Recipe(
        product=ItemId.StoneAxe,
        materials={
            ItemId.Stone: 5,
            ItemId.Wood: 5,
        },
    ),
    ItemId.MetalAxe: Recipe(
        product=ItemId.MetalAxe,
        materials={
            ItemId.Stone: 15,
            ItemId.Wood: 20,
            ItemId.Ingot: 5,
        },
    ),
    ItemId.RefinedMetalAxe: Recipe(
        product=ItemId.RefinedMetalAxe,
        materials={
            ItemId.Stone: 30,
            ItemId.Wood: 40,
            ItemId.RefinedIngot: 10,
        },
    ),
    ItemId.PalMetalAxe: Recipe(
        product=ItemId.PalMetalAxe,
        materials={
            ItemId.Stone: 50,
            ItemId.Wood: 100,
            ItemId.PalMetalIngot: 10,
        },
    ),
    ItemId.StoneSpear: Recipe(
        product=ItemId.StoneSpear,
        materials={
            ItemId.Wood: 18,
            ItemId.Stone: 6,
        },
    ),
    ItemId.MetalSpear: Recipe(
        product=ItemId.MetalSpear,
        materials={
            ItemId.Wood: 27,
            ItemId.Stone: 12,
            ItemId.Ingot: 10,
        },
    ),
    ItemId.RefinedMetalSpear: Recipe(
        product=ItemId.RefinedMetalSpear,
        materials={
            ItemId.Wood: 36,
            ItemId.Stone: 18,
            ItemId.RefinedIngot: 10,
        },
    ),
    ItemId.LilySSpear: Recipe(
        product=ItemId.LilySSpear,
        materials={
            ItemId.PaldiumFragment: 20,
            ItemId.RefinedIngot: 30,
            ItemId.HighQualityCloth: 20,
            ItemId.Wood: 50,
            ItemId.AncientCivilizationParts: 20,
        },
    ),
    ItemId.LilySSpear4: Recipe(
        product=ItemId.LilySSpear4,
        materials={
            ItemId.PaldiumFragment: 45,
            ItemId.RefinedIngot: 67,
            ItemId.HighQualityCloth: 45,
            ItemId.Wood: 112,
            ItemId.AncientCivilizationParts: 40,
        },
    ),
    ItemId.StunBaton: Recipe(
        product=ItemId.StunBaton,
        materials={
            ItemId.Ingot: 20,
            ItemId.ElectricOrgan: 20,
        },
    ),
    ItemId.Katana: Recipe(
        product=ItemId.Katana,
        materials={
            ItemId.PalMetalIngot: 20,
            ItemId.Wood: 20,
        },
    ),
    ItemId.Katana1: Recipe(
        product=ItemId.Katana1,
        materials={
            ItemId.PalMetalIngot: 40,
            ItemId.Wood: 40,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.Katana2: Recipe(
        product=ItemId.Katana2,
        materials={
            ItemId.PalMetalIngot: 60,
            ItemId.Wood: 60,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.Katana3: Recipe(
        product=ItemId.Katana3,
        materials={
            ItemId.PalMetalIngot: 90,
            ItemId.Wood: 90,
            ItemId.AncientCivilizationParts: 16,
        },
    ),
    ItemId.Katana4: Recipe(
        product=ItemId.Katana4,
        materials={
            ItemId.PalMetalIngot: 135,
            ItemId.Wood: 135,
            ItemId.AncientCivilizationParts: 32,
        },
    ),
    ItemId.Sword: Recipe(
        product=ItemId.Sword,
        materials={
            ItemId.Ingot: 30,
            ItemId.Wood: 20,
            ItemId.Stone: 20,
        },
    ),
    ItemId.Sword1: Recipe(
        product=ItemId.Sword1,
        materials={
            ItemId.Ingot: 60,
            ItemId.Wood: 40,
            ItemId.Stone: 40,
            ItemId.AncientCivilizationParts: 3,
        },
    ),
    ItemId.Sword2: Recipe(
        product=ItemId.Sword2,
        materials={
            ItemId.Ingot: 90,
            ItemId.Wood: 60,
            ItemId.Stone: 60,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.Sword3: Recipe(
        product=ItemId.Sword3,
        materials={
            ItemId.Ingot: 135,
            ItemId.Wood: 90,
            ItemId.Stone: 90,
            ItemId.AncientCivilizationParts: 12,
        },
    ),
    ItemId.Sword4: Recipe(
        product=ItemId.Sword4,
        materials={
            ItemId.Ingot: 202,
            ItemId.Wood: 135,
            ItemId.Stone: 135,
            ItemId.AncientCivilizationParts: 24,
        },
    ),
    ItemId.MetalDetector: Recipe(
        product=ItemId.MetalDetector,
        materials={
            ItemId.Plasteel: 30,
            ItemId.PaldiumFragment: 100,
            ItemId.CircuitBoard: 30,
            ItemId.NightstarSand: 20,
        },
    ),
    ItemId.BeamSword: Recipe(
        product=ItemId.BeamSword,
        materials={
            ItemId.Hexolite: 30,
            ItemId.PaldiumFragment: 100,
            ItemId.NightstarSand: 20,
            ItemId.AncientCivilizationParts: 5,
        },
    ),
    ItemId.BeamSword1: Recipe(
        product=ItemId.BeamSword1,
        materials={
            ItemId.Hexolite: 60,
            ItemId.PaldiumFragment: 200,
            ItemId.NightstarSand: 40,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.BeamSword2: Recipe(
        product=ItemId.BeamSword2,
        materials={
            ItemId.Hexolite: 90,
            ItemId.PaldiumFragment: 300,
            ItemId.NightstarSand: 60,
            ItemId.AncientCivilizationParts: 20,
        },
    ),
    ItemId.BeamSword3: Recipe(
        product=ItemId.BeamSword3,
        materials={
            ItemId.Hexolite: 135,
            ItemId.PaldiumFragment: 450,
            ItemId.NightstarSand: 90,
            ItemId.AncientCivilizationParts: 30,
        },
    ),
    ItemId.BeamSword4: Recipe(
        product=ItemId.BeamSword4,
        materials={
            ItemId.Hexolite: 202,
            ItemId.PaldiumFragment: 675,
            ItemId.NightstarSand: 135,
            ItemId.AncientCivilizationParts: 40,
        },
    ),
    ItemId.OldBow: Recipe(
        product=ItemId.OldBow,
        materials={
            ItemId.Wood: 30,
            ItemId.Stone: 5,
            ItemId.Fiber: 15,
        },
    ),
    ItemId.OldBow1: Recipe(
        product=ItemId.OldBow1,
        materials={
            ItemId.Wood: 60,
            ItemId.Stone: 10,
            ItemId.Fiber: 30,
            ItemId.AncientCivilizationParts: 1,
        },
    ),
    ItemId.OldBow2: Recipe(
        product=ItemId.OldBow2,
        materials={
            ItemId.Wood: 90,
            ItemId.Stone: 15,
            ItemId.Fiber: 45,
            ItemId.AncientCivilizationParts: 2,
        },
    ),
    ItemId.OldBow3: Recipe(
        product=ItemId.OldBow3,
        materials={
            ItemId.Wood: 135,
            ItemId.Stone: 22,
            ItemId.Fiber: 67,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.OldBow4: Recipe(
        product=ItemId.OldBow4,
        materials={
            ItemId.Wood: 202,
            ItemId.Stone: 33,
            ItemId.Fiber: 100,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.FireBow: Recipe(
        product=ItemId.FireBow,
        materials={
            ItemId.Wood: 40,
            ItemId.Stone: 8,
            ItemId.Fiber: 20,
            ItemId.FlameOrgan: 2,
        },
    ),
    ItemId.PoisonBow: Recipe(
        product=ItemId.PoisonBow,
        materials={
            ItemId.Wood: 40,
            ItemId.Stone: 8,
            ItemId.Fiber: 20,
            ItemId.VenomGland: 2,
        },
    ),
    ItemId.ThreeShotBow: Recipe(
        product=ItemId.ThreeShotBow,
        materials={
            ItemId.Wood: 50,
            ItemId.Stone: 12,
            ItemId.Fiber: 30,
        },
    ),
    ItemId.Crossbow: Recipe(
        product=ItemId.Crossbow,
        materials={
            ItemId.Wood: 50,
            ItemId.Stone: 40,
            ItemId.Ingot: 10,
            ItemId.Nail: 5,
        },
    ),
    ItemId.Crossbow1: Recipe(
        product=ItemId.Crossbow1,
        materials={
            ItemId.Wood: 100,
            ItemId.Stone: 80,
            ItemId.Ingot: 20,
            ItemId.Nail: 10,
            ItemId.AncientCivilizationParts: 2,
        },
    ),
    ItemId.Crossbow2: Recipe(
        product=ItemId.Crossbow2,
        materials={
            ItemId.Wood: 150,
            ItemId.Stone: 120,
            ItemId.Ingot: 30,
            ItemId.Nail: 15,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.Crossbow3: Recipe(
        product=ItemId.Crossbow3,
        materials={
            ItemId.Wood: 225,
            ItemId.Stone: 180,
            ItemId.Ingot: 45,
            ItemId.Nail: 22,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.Crossbow4: Recipe(
        product=ItemId.Crossbow4,
        materials={
            ItemId.Wood: 337,
            ItemId.Stone: 270,
            ItemId.Ingot: 67,
            ItemId.Nail: 33,
            ItemId.AncientCivilizationParts: 12,
        },
    ),
    ItemId.FireArrowCrossbow: Recipe(
        product=ItemId.FireArrowCrossbow,
        materials={
            ItemId.Wood: 50,
            ItemId.Stone: 50,
            ItemId.Ingot: 15,
            ItemId.Nail: 5,
            ItemId.FlameOrgan: 5,
        },
    ),
    ItemId.FireArrowCrossbow1: Recipe(
        product=ItemId.FireArrowCrossbow1,
        materials={
            ItemId.Wood: 100,
            ItemId.Stone: 100,
            ItemId.Ingot: 30,
            ItemId.Nail: 10,
            ItemId.AncientCivilizationParts: 2,
        },
    ),
    ItemId.FireArrowCrossbow2: Recipe(
        product=ItemId.FireArrowCrossbow2,
        materials={
            ItemId.Wood: 150,
            ItemId.Stone: 150,
            ItemId.Ingot: 45,
            ItemId.Nail: 15,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.FireArrowCrossbow3: Recipe(
        product=ItemId.FireArrowCrossbow3,
        materials={
            ItemId.Wood: 225,
            ItemId.Stone: 225,
            ItemId.Ingot: 67,
            ItemId.Nail: 22,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.FireArrowCrossbow4: Recipe(
        product=ItemId.FireArrowCrossbow4,
        materials={
            ItemId.Wood: 337,
            ItemId.Stone: 337,
            ItemId.Ingot: 100,
            ItemId.Nail: 33,
            ItemId.AncientCivilizationParts: 12,
        },
    ),
    ItemId.PoisonArrowCrossbow: Recipe(
        product=ItemId.PoisonArrowCrossbow,
        materials={
            ItemId.Wood: 50,
            ItemId.Stone: 50,
            ItemId.Ingot: 15,
            ItemId.Nail: 5,
            ItemId.VenomGland: 5,
        },
    ),
    ItemId.PoisonArrowCrossbow1: Recipe(
        product=ItemId.PoisonArrowCrossbow1,
        materials={
            ItemId.Wood: 100,
            ItemId.Stone: 100,
            ItemId.Ingot: 30,
            ItemId.Nail: 10,
            ItemId.AncientCivilizationParts: 2,
        },
    ),
    ItemId.PoisonArrowCrossbow2: Recipe(
        product=ItemId.PoisonArrowCrossbow2,
        materials={
            ItemId.Wood: 150,
            ItemId.Stone: 150,
            ItemId.Ingot: 45,
            ItemId.Nail: 15,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.PoisonArrowCrossbow3: Recipe(
        product=ItemId.PoisonArrowCrossbow3,
        materials={
            ItemId.Wood: 225,
            ItemId.Stone: 225,
            ItemId.Ingot: 67,
            ItemId.Nail: 22,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.PoisonArrowCrossbow4: Recipe(
        product=ItemId.PoisonArrowCrossbow4,
        materials={
            ItemId.Wood: 337,
            ItemId.Stone: 337,
            ItemId.Ingot: 100,
            ItemId.Nail: 33,
            ItemId.AncientCivilizationParts: 12,
        },
    ),
    ItemId.CompoundBow: Recipe(
        product=ItemId.CompoundBow,
        materials={
            ItemId.Ingot: 50,
            ItemId.Fiber: 40,
            ItemId.Nail: 20,
        },
    ),
    ItemId.CompoundBow1: Recipe(
        product=ItemId.CompoundBow1,
        materials={
            ItemId.Ingot: 100,
            ItemId.Fiber: 80,
            ItemId.Nail: 40,
        },
    ),
    ItemId.CompoundBow2: Recipe(
        product=ItemId.CompoundBow2,
        materials={
            ItemId.Ingot: 200,
            ItemId.Fiber: 160,
            ItemId.Nail: 80,
        },
    ),
    ItemId.CompoundBow3: Recipe(
        product=ItemId.CompoundBow3,
        materials={
            ItemId.Ingot: 400,
            ItemId.Fiber: 320,
            ItemId.Nail: 160,
        },
    ),
    ItemId.CompoundBow4: Recipe(
        product=ItemId.CompoundBow4,
        materials={
            ItemId.Ingot: 800,
            ItemId.Fiber: 640,
            ItemId.Nail: 320,
        },
    ),
    ItemId.AdvancedBow: Recipe(
        product=ItemId.AdvancedBow,
        materials={
            ItemId.Hexolite: 40,
            ItemId.CarbonFiber: 100,
            ItemId.NightstarSand: 20,
        },
    ),
    ItemId.AdvancedBow1: Recipe(
        product=ItemId.AdvancedBow1,
        materials={
            ItemId.Hexolite: 80,
            ItemId.CarbonFiber: 200,
            ItemId.NightstarSand: 40,
        },
    ),
    ItemId.AdvancedBow2: Recipe(
        product=ItemId.AdvancedBow2,
        materials={
            ItemId.Hexolite: 120,
            ItemId.CarbonFiber: 300,
            ItemId.NightstarSand: 60,
        },
    ),
    ItemId.AdvancedBow3: Recipe(
        product=ItemId.AdvancedBow3,
        materials={
            ItemId.Hexolite: 180,
            ItemId.CarbonFiber: 450,
            ItemId.NightstarSand: 90,
        },
    ),
    ItemId.AdvancedBow4: Recipe(
        product=ItemId.AdvancedBow4,
        materials={
            ItemId.Hexolite: 270,
            ItemId.CarbonFiber: 675,
            ItemId.NightstarSand: 135,
        },
    ),
    ItemId.Musket: Recipe(
        product=ItemId.Musket,
        materials={
            ItemId.Ingot: 25,
            ItemId.HighQualityPalOil: 5,
            ItemId.Wood: 30,
        },
    ),
    ItemId.Musket1: Recipe(
        product=ItemId.Musket1,
        materials={
            ItemId.Ingot: 50,
            ItemId.HighQualityPalOil: 10,
            ItemId.Wood: 60,
            ItemId.AncientCivilizationParts: 3,
        },
    ),
    ItemId.Musket2: Recipe(
        product=ItemId.Musket2,
        materials={
            ItemId.Ingot: 75,
            ItemId.HighQualityPalOil: 15,
            ItemId.Wood: 90,
            ItemId.AncientCivilizationParts: 5,
        },
    ),
    ItemId.Musket3: Recipe(
        product=ItemId.Musket3,
        materials={
            ItemId.Ingot: 112,
            ItemId.HighQualityPalOil: 22,
            ItemId.Wood: 135,
            ItemId.AncientCivilizationParts: 7,
        },
    ),
    ItemId.Musket4: Recipe(
        product=ItemId.Musket4,
        materials={
            ItemId.Ingot: 168,
            ItemId.HighQualityPalOil: 33,
            ItemId.Wood: 202,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.MakeshiftHandgun: Recipe(
        product=ItemId.MakeshiftHandgun,
        materials={
            ItemId.Ingot: 35,
            ItemId.HighQualityPalOil: 10,
            ItemId.Fiber: 30,
        },
    ),
    ItemId.MakeshiftHandgun1: Recipe(
        product=ItemId.MakeshiftHandgun1,
        materials={
            ItemId.Ingot: 70,
            ItemId.HighQualityPalOil: 20,
            ItemId.Fiber: 60,
            ItemId.AncientCivilizationParts: 2,
        },
    ),
    ItemId.MakeshiftHandgun2: Recipe(
        product=ItemId.MakeshiftHandgun2,
        materials={
            ItemId.Ingot: 105,
            ItemId.HighQualityPalOil: 30,
            ItemId.Fiber: 90,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.MakeshiftHandgun3: Recipe(
        product=ItemId.MakeshiftHandgun3,
        materials={
            ItemId.Ingot: 157,
            ItemId.HighQualityPalOil: 45,
            ItemId.Fiber: 135,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.MakeshiftHandgun4: Recipe(
        product=ItemId.MakeshiftHandgun4,
        materials={
            ItemId.Ingot: 235,
            ItemId.HighQualityPalOil: 67,
            ItemId.Fiber: 202,
            ItemId.AncientCivilizationParts: 16,
        },
    ),
    ItemId.MakeshiftSMG: Recipe(
        product=ItemId.MakeshiftSMG,
        materials={
            ItemId.Ingot: 40,
            ItemId.HighQualityPalOil: 10,
            ItemId.Fiber: 30,
        },
    ),
    ItemId.MakeshiftSMG1: Recipe(
        product=ItemId.MakeshiftSMG1,
        materials={
            ItemId.Ingot: 80,
            ItemId.HighQualityPalOil: 20,
            ItemId.Fiber: 60,
            ItemId.AncientCivilizationParts: 3,
        },
    ),
    ItemId.MakeshiftSMG2: Recipe(
        product=ItemId.MakeshiftSMG2,
        materials={
            ItemId.Ingot: 120,
            ItemId.HighQualityPalOil: 30,
            ItemId.Fiber: 90,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.MakeshiftSMG3: Recipe(
        product=ItemId.MakeshiftSMG3,
        materials={
            ItemId.Ingot: 180,
            ItemId.HighQualityPalOil: 45,
            ItemId.Fiber: 135,
            ItemId.AncientCivilizationParts: 12,
        },
    ),
    ItemId.MakeshiftSMG4: Recipe(
        product=ItemId.MakeshiftSMG4,
        materials={
            ItemId.Ingot: 270,
            ItemId.HighQualityPalOil: 67,
            ItemId.Fiber: 202,
            ItemId.AncientCivilizationParts: 24,
        },
    ),
    ItemId.MakeshiftShotgun: Recipe(
        product=ItemId.MakeshiftShotgun,
        materials={
            ItemId.Ingot: 60,
            ItemId.HighQualityPalOil: 15,
            ItemId.Fiber: 50,
        },
    ),
    ItemId.MakeshiftShotgun1: Recipe(
        product=ItemId.MakeshiftShotgun1,
        materials={
            ItemId.Ingot: 120,
            ItemId.HighQualityPalOil: 30,
            ItemId.Fiber: 100,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.MakeshiftShotgun2: Recipe(
        product=ItemId.MakeshiftShotgun2,
        materials={
            ItemId.Ingot: 180,
            ItemId.HighQualityPalOil: 45,
            ItemId.Fiber: 150,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.MakeshiftShotgun3: Recipe(
        product=ItemId.MakeshiftShotgun3,
        materials={
            ItemId.Ingot: 270,
            ItemId.HighQualityPalOil: 67,
            ItemId.Fiber: 225,
            ItemId.AncientCivilizationParts: 16,
        },
    ),
    ItemId.MakeshiftShotgun4: Recipe(
        product=ItemId.MakeshiftShotgun4,
        materials={
            ItemId.Ingot: 405,
            ItemId.HighQualityPalOil: 100,
            ItemId.Fiber: 337,
            ItemId.AncientCivilizationParts: 32,
        },
    ),
    ItemId.MakeshiftAssaultRifle: Recipe(
        product=ItemId.MakeshiftAssaultRifle,
        materials={
            ItemId.Ingot: 70,
            ItemId.HighQualityPalOil: 20,
            ItemId.Fiber: 60,
        },
    ),
    ItemId.MakeshiftAssaultRifle1: Recipe(
        product=ItemId.MakeshiftAssaultRifle1,
        materials={
            ItemId.Ingot: 140,
            ItemId.HighQualityPalOil: 40,
            ItemId.Fiber: 120,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.MakeshiftAssaultRifle2: Recipe(
        product=ItemId.MakeshiftAssaultRifle2,
        materials={
            ItemId.Ingot: 210,
            ItemId.HighQualityPalOil: 60,
            ItemId.Fiber: 180,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.MakeshiftAssaultRifle3: Recipe(
        product=ItemId.MakeshiftAssaultRifle3,
        materials={
            ItemId.Ingot: 315,
            ItemId.HighQualityPalOil: 90,
            ItemId.Fiber: 270,
            ItemId.AncientCivilizationParts: 16,
        },
    ),
    ItemId.MakeshiftAssaultRifle4: Recipe(
        product=ItemId.MakeshiftAssaultRifle4,
        materials={
            ItemId.Ingot: 472,
            ItemId.HighQualityPalOil: 135,
            ItemId.Fiber: 405,
            ItemId.AncientCivilizationParts: 32,
        },
    ),
    ItemId.BoostGun: Recipe(
        product=ItemId.BoostGun,
        materials={
            ItemId.Ingot: 45,
            ItemId.HighQualityPalOil: 10,
            ItemId.Fiber: 30,
        },
    ),
    ItemId.MegaboostGun: Recipe(
        product=ItemId.MegaboostGun,
        materials={
            ItemId.CoralumIngot: 150,
            ItemId.Hexolite: 120,
            ItemId.CarbonFiber: 200,
            ItemId.CircuitBoard: 100,
        },
    ),
    ItemId.Handgun: Recipe(
        product=ItemId.Handgun,
        materials={
            ItemId.Ingot: 50,
            ItemId.HighQualityPalOil: 15,
        },
    ),
    ItemId.Handgun1: Recipe(
        product=ItemId.Handgun1,
        materials={
            ItemId.Ingot: 100,
            ItemId.HighQualityPalOil: 30,
            ItemId.AncientCivilizationParts: 3,
        },
    ),
    ItemId.Handgun2: Recipe(
        product=ItemId.Handgun2,
        materials={
            ItemId.Ingot: 150,
            ItemId.HighQualityPalOil: 45,
            ItemId.AncientCivilizationParts: 5,
        },
    ),
    ItemId.Handgun3: Recipe(
        product=ItemId.Handgun3,
        materials={
            ItemId.Ingot: 225,
            ItemId.HighQualityPalOil: 67,
            ItemId.AncientCivilizationParts: 7,
        },
    ),
    ItemId.Handgun4: Recipe(
        product=ItemId.Handgun4,
        materials={
            ItemId.Ingot: 337,
            ItemId.HighQualityPalOil: 100,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.OldRevolver: Recipe(
        product=ItemId.OldRevolver,
        materials={
            ItemId.Ingot: 60,
            ItemId.HighQualityPalOil: 20,
        },
    ),
    ItemId.OldRevolver1: Recipe(
        product=ItemId.OldRevolver1,
        materials={
            ItemId.Ingot: 120,
            ItemId.HighQualityPalOil: 40,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.OldRevolver2: Recipe(
        product=ItemId.OldRevolver2,
        materials={
            ItemId.Ingot: 240,
            ItemId.HighQualityPalOil: 80,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.OldRevolver3: Recipe(
        product=ItemId.OldRevolver3,
        materials={
            ItemId.Ingot: 480,
            ItemId.HighQualityPalOil: 160,
            ItemId.AncientCivilizationParts: 16,
        },
    ),
    ItemId.OldRevolver4: Recipe(
        product=ItemId.OldRevolver4,
        materials={
            ItemId.Ingot: 960,
            ItemId.HighQualityPalOil: 320,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.SingleShotRifle: Recipe(
        product=ItemId.SingleShotRifle,
        materials={
            ItemId.RefinedIngot: 20,
            ItemId.Polymer: 5,
        },
    ),
    ItemId.SingleShotRifle1: Recipe(
        product=ItemId.SingleShotRifle1,
        materials={
            ItemId.RefinedIngot: 40,
            ItemId.Polymer: 10,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.SingleShotRifle2: Recipe(
        product=ItemId.SingleShotRifle2,
        materials={
            ItemId.RefinedIngot: 60,
            ItemId.Polymer: 15,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.SingleShotRifle3: Recipe(
        product=ItemId.SingleShotRifle3,
        materials={
            ItemId.RefinedIngot: 90,
            ItemId.Polymer: 22,
            ItemId.AncientCivilizationParts: 16,
        },
    ),
    ItemId.SingleShotRifle4: Recipe(
        product=ItemId.SingleShotRifle4,
        materials={
            ItemId.RefinedIngot: 135,
            ItemId.Polymer: 33,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.SMG: Recipe(
        product=ItemId.SMG,
        materials={
            ItemId.RefinedIngot: 25,
            ItemId.Polymer: 6,
        },
    ),
    ItemId.SMG1: Recipe(
        product=ItemId.SMG1,
        materials={
            ItemId.RefinedIngot: 50,
            ItemId.Polymer: 12,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.SMG2: Recipe(
        product=ItemId.SMG2,
        materials={
            ItemId.RefinedIngot: 75,
            ItemId.Polymer: 18,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.SMG3: Recipe(
        product=ItemId.SMG3,
        materials={
            ItemId.RefinedIngot: 112,
            ItemId.Polymer: 27,
            ItemId.AncientCivilizationParts: 16,
        },
    ),
    ItemId.SMG4: Recipe(
        product=ItemId.SMG4,
        materials={
            ItemId.RefinedIngot: 168,
            ItemId.Polymer: 40,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.DoubleBarreledShotgun: Recipe(
        product=ItemId.DoubleBarreledShotgun,
        materials={
            ItemId.RefinedIngot: 30,
            ItemId.Polymer: 7,
        },
    ),
    ItemId.DoubleBarreledShotgun1: Recipe(
        product=ItemId.DoubleBarreledShotgun1,
        materials={
            ItemId.RefinedIngot: 60,
            ItemId.Polymer: 14,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.DoubleBarreledShotgun2: Recipe(
        product=ItemId.DoubleBarreledShotgun2,
        materials={
            ItemId.RefinedIngot: 90,
            ItemId.Polymer: 21,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.DoubleBarreledShotgun3: Recipe(
        product=ItemId.DoubleBarreledShotgun3,
        materials={
            ItemId.RefinedIngot: 135,
            ItemId.Polymer: 31,
            ItemId.AncientCivilizationParts: 16,
        },
    ),
    ItemId.DoubleBarreledShotgun4: Recipe(
        product=ItemId.DoubleBarreledShotgun4,
        materials={
            ItemId.RefinedIngot: 202,
            ItemId.Polymer: 46,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.SemiAutoRifle: Recipe(
        product=ItemId.SemiAutoRifle,
        materials={
            ItemId.RefinedIngot: 35,
            ItemId.Polymer: 10,
        },
    ),
    ItemId.SemiAutoRifle1: Recipe(
        product=ItemId.SemiAutoRifle1,
        materials={
            ItemId.RefinedIngot: 70,
            ItemId.Polymer: 20,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.SemiAutoRifle2: Recipe(
        product=ItemId.SemiAutoRifle2,
        materials={
            ItemId.RefinedIngot: 105,
            ItemId.Polymer: 30,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.SemiAutoRifle3: Recipe(
        product=ItemId.SemiAutoRifle3,
        materials={
            ItemId.RefinedIngot: 157,
            ItemId.Polymer: 45,
            ItemId.AncientCivilizationParts: 16,
        },
    ),
    ItemId.SemiAutoRifle4: Recipe(
        product=ItemId.SemiAutoRifle4,
        materials={
            ItemId.RefinedIngot: 235,
            ItemId.Polymer: 67,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.AssaultRifle: Recipe(
        product=ItemId.AssaultRifle,
        materials={
            ItemId.RefinedIngot: 40,
            ItemId.Polymer: 10,
            ItemId.CarbonFiber: 30,
        },
    ),
    ItemId.AssaultRifle1: Recipe(
        product=ItemId.AssaultRifle1,
        materials={
            ItemId.RefinedIngot: 80,
            ItemId.Polymer: 20,
            ItemId.CarbonFiber: 60,
            ItemId.AncientCivilizationParts: 5,
        },
    ),
    ItemId.AssaultRifle2: Recipe(
        product=ItemId.AssaultRifle2,
        materials={
            ItemId.RefinedIngot: 120,
            ItemId.Polymer: 30,
            ItemId.CarbonFiber: 90,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.AssaultRifle3: Recipe(
        product=ItemId.AssaultRifle3,
        materials={
            ItemId.RefinedIngot: 180,
            ItemId.Polymer: 45,
            ItemId.CarbonFiber: 135,
            ItemId.AncientCivilizationParts: 20,
        },
    ),
    ItemId.AssaultRifle4: Recipe(
        product=ItemId.AssaultRifle4,
        materials={
            ItemId.RefinedIngot: 270,
            ItemId.Polymer: 67,
            ItemId.CarbonFiber: 202,
            ItemId.AncientCivilizationParts: 30,
        },
    ),
    ItemId.PumpActionShotgun: Recipe(
        product=ItemId.PumpActionShotgun,
        materials={
            ItemId.RefinedIngot: 30,
            ItemId.Polymer: 20,
            ItemId.CarbonFiber: 40,
        },
    ),
    ItemId.PumpActionShotgun1: Recipe(
        product=ItemId.PumpActionShotgun1,
        materials={
            ItemId.RefinedIngot: 60,
            ItemId.Polymer: 40,
            ItemId.CarbonFiber: 80,
            ItemId.AncientCivilizationParts: 5,
        },
    ),
    ItemId.PumpActionShotgun2: Recipe(
        product=ItemId.PumpActionShotgun2,
        materials={
            ItemId.RefinedIngot: 90,
            ItemId.Polymer: 60,
            ItemId.CarbonFiber: 120,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.PumpActionShotgun3: Recipe(
        product=ItemId.PumpActionShotgun3,
        materials={
            ItemId.RefinedIngot: 135,
            ItemId.Polymer: 90,
            ItemId.CarbonFiber: 180,
            ItemId.AncientCivilizationParts: 20,
        },
    ),
    ItemId.PumpActionShotgun4: Recipe(
        product=ItemId.PumpActionShotgun4,
        materials={
            ItemId.RefinedIngot: 202,
            ItemId.Polymer: 135,
            ItemId.CarbonFiber: 270,
            ItemId.AncientCivilizationParts: 30,
        },
    ),
    ItemId.SemiAutoShotgun: Recipe(
        product=ItemId.SemiAutoShotgun,
        materials={
            ItemId.RefinedIngot: 50,
            ItemId.Polymer: 20,
            ItemId.CarbonFiber: 40,
        },
    ),
    ItemId.SemiAutoShotgun1: Recipe(
        product=ItemId.SemiAutoShotgun1,
        materials={
            ItemId.RefinedIngot: 100,
            ItemId.Polymer: 40,
            ItemId.CarbonFiber: 80,
            ItemId.AncientCivilizationParts: 5,
        },
    ),
    ItemId.SemiAutoShotgun2: Recipe(
        product=ItemId.SemiAutoShotgun2,
        materials={
            ItemId.RefinedIngot: 150,
            ItemId.Polymer: 60,
            ItemId.CarbonFiber: 120,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.SemiAutoShotgun3: Recipe(
        product=ItemId.SemiAutoShotgun3,
        materials={
            ItemId.RefinedIngot: 225,
            ItemId.Polymer: 90,
            ItemId.CarbonFiber: 180,
            ItemId.AncientCivilizationParts: 20,
        },
    ),
    ItemId.SemiAutoShotgun4: Recipe(
        product=ItemId.SemiAutoShotgun4,
        materials={
            ItemId.RefinedIngot: 337,
            ItemId.Polymer: 135,
            ItemId.CarbonFiber: 270,
            ItemId.AncientCivilizationParts: 30,
        },
    ),
    ItemId.RocketLauncher: Recipe(
        product=ItemId.RocketLauncher,
        materials={
            ItemId.PalMetalIngot: 75,
            ItemId.Polymer: 30,
            ItemId.CarbonFiber: 50,
        },
    ),
    ItemId.RocketLauncher1: Recipe(
        product=ItemId.RocketLauncher1,
        materials={
            ItemId.PalMetalIngot: 150,
            ItemId.Polymer: 60,
            ItemId.CarbonFiber: 100,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.RocketLauncher2: Recipe(
        product=ItemId.RocketLauncher2,
        materials={
            ItemId.PalMetalIngot: 225,
            ItemId.Polymer: 90,
            ItemId.CarbonFiber: 150,
            ItemId.AncientCivilizationParts: 20,
        },
    ),
    ItemId.RocketLauncher3: Recipe(
        product=ItemId.RocketLauncher3,
        materials={
            ItemId.PalMetalIngot: 337,
            ItemId.Polymer: 135,
            ItemId.CarbonFiber: 225,
            ItemId.AncientCivilizationParts: 30,
        },
    ),
    ItemId.RocketLauncher4: Recipe(
        product=ItemId.RocketLauncher4,
        materials={
            ItemId.PalMetalIngot: 505,
            ItemId.Polymer: 202,
            ItemId.CarbonFiber: 337,
            ItemId.AncientCivilizationParts: 40,
        },
    ),
    ItemId.LaserRifle: Recipe(
        product=ItemId.LaserRifle,
        materials={
            ItemId.PalMetalIngot: 50,
            ItemId.Plasteel: 40,
            ItemId.CarbonFiber: 40,
        },
    ),
    ItemId.LaserRifle1: Recipe(
        product=ItemId.LaserRifle1,
        materials={
            ItemId.PalMetalIngot: 100,
            ItemId.Plasteel: 80,
            ItemId.CarbonFiber: 80,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.LaserRifle2: Recipe(
        product=ItemId.LaserRifle2,
        materials={
            ItemId.PalMetalIngot: 150,
            ItemId.Plasteel: 120,
            ItemId.CarbonFiber: 120,
            ItemId.AncientCivilizationParts: 20,
        },
    ),
    ItemId.LaserRifle3: Recipe(
        product=ItemId.LaserRifle3,
        materials={
            ItemId.PalMetalIngot: 225,
            ItemId.Plasteel: 180,
            ItemId.CarbonFiber: 180,
            ItemId.AncientCivilizationParts: 30,
        },
    ),
    ItemId.LaserRifle4: Recipe(
        product=ItemId.LaserRifle4,
        materials={
            ItemId.PalMetalIngot: 337,
            ItemId.Plasteel: 270,
            ItemId.CarbonFiber: 270,
            ItemId.AncientCivilizationParts: 40,
        },
    ),
    ItemId.Flamethrower: Recipe(
        product=ItemId.Flamethrower,
        materials={
            ItemId.PalMetalIngot: 40,
            ItemId.Plasteel: 30,
            ItemId.CarbonFiber: 35,
            ItemId.FlameOrgan: 30,
        },
    ),
    ItemId.Flamethrower1: Recipe(
        product=ItemId.Flamethrower1,
        materials={
            ItemId.PalMetalIngot: 80,
            ItemId.Plasteel: 60,
            ItemId.CarbonFiber: 70,
            ItemId.FlameOrgan: 60,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.Flamethrower2: Recipe(
        product=ItemId.Flamethrower2,
        materials={
            ItemId.PalMetalIngot: 120,
            ItemId.Plasteel: 90,
            ItemId.CarbonFiber: 105,
            ItemId.FlameOrgan: 90,
            ItemId.AncientCivilizationParts: 20,
        },
    ),
    ItemId.Flamethrower3: Recipe(
        product=ItemId.Flamethrower3,
        materials={
            ItemId.PalMetalIngot: 180,
            ItemId.Plasteel: 135,
            ItemId.CarbonFiber: 157,
            ItemId.FlameOrgan: 135,
            ItemId.AncientCivilizationParts: 30,
        },
    ),
    ItemId.Flamethrower4: Recipe(
        product=ItemId.Flamethrower4,
        materials={
            ItemId.PalMetalIngot: 270,
            ItemId.Plasteel: 202,
            ItemId.CarbonFiber: 235,
            ItemId.FlameOrgan: 202,
            ItemId.AncientCivilizationParts: 40,
        },
    ),
    ItemId.GrenadeLauncher: Recipe(
        product=ItemId.GrenadeLauncher,
        materials={
            ItemId.PalMetalIngot: 75,
            ItemId.Plasteel: 60,
            ItemId.CarbonFiber: 60,
        },
    ),
    ItemId.GrenadeLauncher1: Recipe(
        product=ItemId.GrenadeLauncher1,
        materials={
            ItemId.PalMetalIngot: 150,
            ItemId.Plasteel: 120,
            ItemId.CarbonFiber: 120,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.GrenadeLauncher2: Recipe(
        product=ItemId.GrenadeLauncher2,
        materials={
            ItemId.PalMetalIngot: 225,
            ItemId.Plasteel: 180,
            ItemId.CarbonFiber: 180,
            ItemId.AncientCivilizationParts: 20,
        },
    ),
    ItemId.GrenadeLauncher3: Recipe(
        product=ItemId.GrenadeLauncher3,
        materials={
            ItemId.PalMetalIngot: 337,
            ItemId.Plasteel: 270,
            ItemId.CarbonFiber: 270,
            ItemId.AncientCivilizationParts: 30,
        },
    ),
    ItemId.GrenadeLauncher4: Recipe(
        product=ItemId.GrenadeLauncher4,
        materials={
            ItemId.PalMetalIngot: 505,
            ItemId.Plasteel: 405,
            ItemId.CarbonFiber: 405,
            ItemId.AncientCivilizationParts: 40,
        },
    ),
    ItemId.GuidedMissileLauncher: Recipe(
        product=ItemId.GuidedMissileLauncher,
        materials={
            ItemId.PalMetalIngot: 100,
            ItemId.Plasteel: 50,
            ItemId.CarbonFiber: 100,
            ItemId.CircuitBoard: 20,
        },
    ),
    ItemId.GuidedMissileLauncher1: Recipe(
        product=ItemId.GuidedMissileLauncher1,
        materials={
            ItemId.PalMetalIngot: 200,
            ItemId.Plasteel: 100,
            ItemId.CarbonFiber: 200,
            ItemId.CircuitBoard: 40,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.GuidedMissileLauncher2: Recipe(
        product=ItemId.GuidedMissileLauncher2,
        materials={
            ItemId.PalMetalIngot: 300,
            ItemId.Plasteel: 150,
            ItemId.CarbonFiber: 300,
            ItemId.CircuitBoard: 60,
            ItemId.AncientCivilizationParts: 20,
        },
    ),
    ItemId.GuidedMissileLauncher3: Recipe(
        product=ItemId.GuidedMissileLauncher3,
        materials={
            ItemId.PalMetalIngot: 450,
            ItemId.Plasteel: 225,
            ItemId.CarbonFiber: 450,
            ItemId.CircuitBoard: 90,
            ItemId.AncientCivilizationParts: 30,
        },
    ),
    ItemId.GuidedMissileLauncher4: Recipe(
        product=ItemId.GuidedMissileLauncher4,
        materials={
            ItemId.PalMetalIngot: 675,
            ItemId.Plasteel: 337,
            ItemId.CarbonFiber: 675,
            ItemId.CircuitBoard: 135,
            ItemId.AncientCivilizationParts: 40,
        },
    ),
    ItemId.MultiGuidedMissileLauncher: Recipe(
        product=ItemId.MultiGuidedMissileLauncher,
        materials={
            ItemId.PalMetalIngot: 150,
            ItemId.Plasteel: 80,
            ItemId.CarbonFiber: 120,
            ItemId.CircuitBoard: 30,
        },
    ),
    ItemId.MultiGuidedMissileLauncher1: Recipe(
        product=ItemId.MultiGuidedMissileLauncher1,
        materials={
            ItemId.PalMetalIngot: 300,
            ItemId.Plasteel: 160,
            ItemId.CarbonFiber: 240,
            ItemId.CircuitBoard: 60,
            ItemId.AncientCivilizationParts: 20,
        },
    ),
    ItemId.MultiGuidedMissileLauncher2: Recipe(
        product=ItemId.MultiGuidedMissileLauncher2,
        materials={
            ItemId.PalMetalIngot: 450,
            ItemId.Plasteel: 240,
            ItemId.CarbonFiber: 360,
            ItemId.CircuitBoard: 90,
            ItemId.AncientCivilizationParts: 30,
        },
    ),
    ItemId.MultiGuidedMissileLauncher3: Recipe(
        product=ItemId.MultiGuidedMissileLauncher3,
        materials={
            ItemId.PalMetalIngot: 675,
            ItemId.Plasteel: 360,
            ItemId.CarbonFiber: 540,
            ItemId.CircuitBoard: 135,
            ItemId.AncientCivilizationParts: 40,
        },
    ),
    ItemId.MultiGuidedMissileLauncher4: Recipe(
        product=ItemId.MultiGuidedMissileLauncher4,
        materials={
            ItemId.PalMetalIngot: 1012,
            ItemId.Plasteel: 540,
            ItemId.CarbonFiber: 810,
            ItemId.CircuitBoard: 202,
            ItemId.AncientCivilizationParts: 50,
        },
    ),
    ItemId.GatlingGun: Recipe(
        product=ItemId.GatlingGun,
        materials={
            ItemId.PalMetalIngot: 150,
            ItemId.Plasteel: 70,
            ItemId.CarbonFiber: 140,
        },
    ),
    ItemId.GatlingGun1: Recipe(
        product=ItemId.GatlingGun1,
        materials={
            ItemId.PalMetalIngot: 300,
            ItemId.Plasteel: 140,
            ItemId.CarbonFiber: 280,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.GatlingGun2: Recipe(
        product=ItemId.GatlingGun2,
        materials={
            ItemId.PalMetalIngot: 450,
            ItemId.Plasteel: 210,
            ItemId.CarbonFiber: 420,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.GatlingGun3: Recipe(
        product=ItemId.GatlingGun3,
        materials={
            ItemId.PalMetalIngot: 675,
            ItemId.Plasteel: 315,
            ItemId.CarbonFiber: 630,
            ItemId.AncientCivilizationParts: 35,
        },
    ),
    ItemId.GatlingGun4: Recipe(
        product=ItemId.GatlingGun4,
        materials={
            ItemId.PalMetalIngot: 1012,
            ItemId.Plasteel: 472,
            ItemId.CarbonFiber: 945,
            ItemId.AncientCivilizationParts: 45,
        },
    ),
    ItemId.MeteorLauncher: Recipe(
        product=ItemId.MeteorLauncher,
        materials={
            ItemId.MeteoriteFragment: 100,
            ItemId.RefinedIngot: 30,
            ItemId.PaldiumFragment: 20,
        },
    ),
    ItemId.MeteorLauncher4: Recipe(
        product=ItemId.MeteorLauncher4,
        materials={
            ItemId.MeteoriteFragment: 675,
            ItemId.RefinedIngot: 200,
            ItemId.PaldiumFragment: 135,
        },
    ),
    ItemId.LaserGatlingGun: Recipe(
        product=ItemId.LaserGatlingGun,
        materials={
            ItemId.Plasteel: 110,
            ItemId.Hexolite: 100,
            ItemId.CarbonFiber: 200,
        },
    ),
    ItemId.LaserGatlingGun1: Recipe(
        product=ItemId.LaserGatlingGun1,
        materials={
            ItemId.Plasteel: 220,
            ItemId.Hexolite: 200,
            ItemId.CarbonFiber: 400,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.LaserGatlingGun2: Recipe(
        product=ItemId.LaserGatlingGun2,
        materials={
            ItemId.Plasteel: 330,
            ItemId.Hexolite: 300,
            ItemId.CarbonFiber: 600,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.LaserGatlingGun3: Recipe(
        product=ItemId.LaserGatlingGun3,
        materials={
            ItemId.Plasteel: 495,
            ItemId.Hexolite: 450,
            ItemId.CarbonFiber: 900,
            ItemId.AncientCivilizationParts: 35,
        },
    ),
    ItemId.LaserGatlingGun4: Recipe(
        product=ItemId.LaserGatlingGun4,
        materials={
            ItemId.Plasteel: 742,
            ItemId.Hexolite: 675,
            ItemId.CarbonFiber: 1350,
            ItemId.AncientCivilizationParts: 45,
        },
    ),
    ItemId.PlasmaCannon: Recipe(
        product=ItemId.PlasmaCannon,
        materials={
            ItemId.Plasteel: 150,
            ItemId.Hexolite: 130,
            ItemId.CarbonFiber: 200,
            ItemId.CircuitBoard: 100,
        },
    ),
    ItemId.PlasmaCannon1: Recipe(
        product=ItemId.PlasmaCannon1,
        materials={
            ItemId.Plasteel: 300,
            ItemId.Hexolite: 260,
            ItemId.CarbonFiber: 400,
            ItemId.CircuitBoard: 200,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.PlasmaCannon2: Recipe(
        product=ItemId.PlasmaCannon2,
        materials={
            ItemId.Plasteel: 450,
            ItemId.Hexolite: 390,
            ItemId.CarbonFiber: 600,
            ItemId.CircuitBoard: 300,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.PlasmaCannon3: Recipe(
        product=ItemId.PlasmaCannon3,
        materials={
            ItemId.Plasteel: 675,
            ItemId.Hexolite: 585,
            ItemId.CarbonFiber: 900,
            ItemId.CircuitBoard: 450,
            ItemId.AncientCivilizationParts: 35,
        },
    ),
    ItemId.PlasmaCannon4: Recipe(
        product=ItemId.PlasmaCannon4,
        materials={
            ItemId.Plasteel: 1012,
            ItemId.Hexolite: 877,
            ItemId.CarbonFiber: 1350,
            ItemId.CircuitBoard: 675,
            ItemId.AncientCivilizationParts: 45,
        },
    ),
    ItemId.EnergyShotgun: Recipe(
        product=ItemId.EnergyShotgun,
        materials={
            ItemId.CoralumIngot: 155,
            ItemId.Hexolite: 130,
            ItemId.CarbonFiber: 220,
            ItemId.CircuitBoard: 120,
        },
    ),
    ItemId.EnergyShotgun1: Recipe(
        product=ItemId.EnergyShotgun1,
        materials={
            ItemId.CoralumIngot: 310,
            ItemId.Hexolite: 260,
            ItemId.CarbonFiber: 440,
            ItemId.CircuitBoard: 240,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.EnergyShotgun2: Recipe(
        product=ItemId.EnergyShotgun2,
        materials={
            ItemId.CoralumIngot: 465,
            ItemId.Hexolite: 390,
            ItemId.CarbonFiber: 660,
            ItemId.CircuitBoard: 360,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.EnergyShotgun3: Recipe(
        product=ItemId.EnergyShotgun3,
        materials={
            ItemId.CoralumIngot: 697,
            ItemId.Hexolite: 585,
            ItemId.CarbonFiber: 990,
            ItemId.CircuitBoard: 540,
            ItemId.AncientCivilizationParts: 35,
        },
    ),
    ItemId.EnergyShotgun4: Recipe(
        product=ItemId.EnergyShotgun4,
        materials={
            ItemId.CoralumIngot: 1045,
            ItemId.Hexolite: 877,
            ItemId.CarbonFiber: 1485,
            ItemId.CircuitBoard: 810,
            ItemId.AncientCivilizationParts: 45,
        },
    ),
    ItemId.OverheatRifle: Recipe(
        product=ItemId.OverheatRifle,
        materials={
            ItemId.CoralumIngot: 160,
            ItemId.Hexolite: 135,
            ItemId.CarbonFiber: 250,
            ItemId.CircuitBoard: 130,
        },
    ),
    ItemId.OverheatRifle1: Recipe(
        product=ItemId.OverheatRifle1,
        materials={
            ItemId.CoralumIngot: 320,
            ItemId.Hexolite: 270,
            ItemId.CarbonFiber: 500,
            ItemId.CircuitBoard: 260,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.OverheatRifle2: Recipe(
        product=ItemId.OverheatRifle2,
        materials={
            ItemId.CoralumIngot: 480,
            ItemId.Hexolite: 405,
            ItemId.CarbonFiber: 750,
            ItemId.CircuitBoard: 390,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.OverheatRifle3: Recipe(
        product=ItemId.OverheatRifle3,
        materials={
            ItemId.CoralumIngot: 720,
            ItemId.Hexolite: 607,
            ItemId.CarbonFiber: 1125,
            ItemId.CircuitBoard: 585,
            ItemId.AncientCivilizationParts: 35,
        },
    ),
    ItemId.OverheatRifle4: Recipe(
        product=ItemId.OverheatRifle4,
        materials={
            ItemId.CoralumIngot: 1080,
            ItemId.Hexolite: 910,
            ItemId.CarbonFiber: 1687,
            ItemId.CircuitBoard: 877,
            ItemId.AncientCivilizationParts: 45,
        },
    ),
    ItemId.ChargeRifle: Recipe(
        product=ItemId.ChargeRifle,
        materials={
            ItemId.CoralumIngot: 200,
            ItemId.Hexolite: 150,
            ItemId.CarbonFiber: 300,
            ItemId.CircuitBoard: 150,
        },
    ),
    ItemId.ChargeRifle1: Recipe(
        product=ItemId.ChargeRifle1,
        materials={
            ItemId.CoralumIngot: 400,
            ItemId.Hexolite: 300,
            ItemId.CarbonFiber: 600,
            ItemId.CircuitBoard: 300,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.ChargeRifle2: Recipe(
        product=ItemId.ChargeRifle2,
        materials={
            ItemId.CoralumIngot: 600,
            ItemId.Hexolite: 450,
            ItemId.CarbonFiber: 900,
            ItemId.CircuitBoard: 450,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.ChargeRifle3: Recipe(
        product=ItemId.ChargeRifle3,
        materials={
            ItemId.CoralumIngot: 900,
            ItemId.Hexolite: 675,
            ItemId.CarbonFiber: 1350,
            ItemId.CircuitBoard: 675,
            ItemId.AncientCivilizationParts: 35,
        },
    ),
    ItemId.ChargeRifle4: Recipe(
        product=ItemId.ChargeRifle4,
        materials={
            ItemId.CoralumIngot: 1350,
            ItemId.Hexolite: 1012,
            ItemId.CarbonFiber: 2025,
            ItemId.CircuitBoard: 1012,
            ItemId.AncientCivilizationParts: 45,
        },
    ),
    ItemId.HomingSphereLauncher: Recipe(
        product=ItemId.HomingSphereLauncher,
        materials={
            ItemId.PalMetalIngot: 100,
            ItemId.Polymer: 50,
            ItemId.PaldiumFragment: 200,
            ItemId.CarbonFiber: 50,
            ItemId.AncientCivilizationParts: 20,
        },
    ),
    ItemId.ScatterSphereLauncher: Recipe(
        product=ItemId.ScatterSphereLauncher,
        materials={
            ItemId.RefinedIngot: 50,
            ItemId.Polymer: 15,
            ItemId.PaldiumFragment: 50,
            ItemId.CarbonFiber: 30,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.SingleShotSphereLauncher: Recipe(
        product=ItemId.SingleShotSphereLauncher,
        materials={
            ItemId.Ingot: 50,
            ItemId.Stone: 100,
            ItemId.PaldiumFragment: 50,
            ItemId.AncientCivilizationParts: 5,
        },
    ),
    ItemId.DecalGun1: Recipe(
        product=ItemId.DecalGun1,
        materials={
            ItemId.Ingot: 30,
            ItemId.Polymer: 10,
            ItemId.PaldiumFragment: 15,
            ItemId.AncientCivilizationParts: 3,
        },
    ),
    ItemId.DecalGun2: Recipe(
        product=ItemId.DecalGun2,
        materials={
            ItemId.Ingot: 30,
            ItemId.Polymer: 10,
            ItemId.PaldiumFragment: 15,
            ItemId.AncientCivilizationParts: 3,
        },
    ),
    ItemId.DecalGun3: Recipe(
        product=ItemId.DecalGun3,
        materials={
            ItemId.Ingot: 30,
            ItemId.Polymer: 10,
            ItemId.PaldiumFragment: 15,
            ItemId.AncientCivilizationParts: 3,
        },
    ),
    ItemId.DecalGun4: Recipe(
        product=ItemId.DecalGun4,
        materials={
            ItemId.Ingot: 30,
            ItemId.Polymer: 10,
            ItemId.PaldiumFragment: 15,
            ItemId.AncientCivilizationParts: 3,
        },
    ),
    ItemId.DecalGun5: Recipe(
        product=ItemId.DecalGun5,
        materials={
            ItemId.Ingot: 30,
            ItemId.Polymer: 10,
            ItemId.PaldiumFragment: 15,
            ItemId.AncientCivilizationParts: 3,
        },
    ),
    ItemId.GrapplingGun: Recipe(
        product=ItemId.GrapplingGun,
        materials={
            ItemId.PaldiumFragment: 10,
            ItemId.Ingot: 10,
            ItemId.Fiber: 30,
            ItemId.AncientCivilizationParts: 1,
        },
    ),
    ItemId.MegaGrapplingGun: Recipe(
        product=ItemId.MegaGrapplingGun,
        materials={
            ItemId.PaldiumFragment: 20,
            ItemId.Ingot: 20,
            ItemId.Fiber: 50,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.GigaGrapplingGun: Recipe(
        product=ItemId.GigaGrapplingGun,
        materials={
            ItemId.PaldiumFragment: 30,
            ItemId.Ingot: 30,
            ItemId.Fiber: 80,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.HyperGrapplingGun: Recipe(
        product=ItemId.HyperGrapplingGun,
        materials={
            ItemId.PaldiumFragment: 40,
            ItemId.RefinedIngot: 30,
            ItemId.CarbonFiber: 20,
            ItemId.Polymer: 20,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.UltraGrapplingGun: Recipe(
        product=ItemId.UltraGrapplingGun,
        materials={
            ItemId.PaldiumFragment: 100,
            ItemId.CoralumIngot: 30,
            ItemId.CarbonFiber: 50,
            ItemId.Polymer: 50,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.MarksmanRevolver: Recipe(
        product=ItemId.MarksmanRevolver,
        materials={
            ItemId.Ingot: 60,
            ItemId.HighQualityPalOil: 15,
            ItemId.GoldCoin: 1,
            ItemId.ElectricOrgan: 30,
        },
    ),
    ItemId.MarksmanRevolver1: Recipe(
        product=ItemId.MarksmanRevolver1,
        materials={
            ItemId.Ingot: 120,
            ItemId.HighQualityPalOil: 30,
            ItemId.GoldCoin: 1,
            ItemId.ElectricOrgan: 50,
            ItemId.AncientCivilizationParts: 3,
        },
    ),
    ItemId.MarksmanRevolver2: Recipe(
        product=ItemId.MarksmanRevolver2,
        materials={
            ItemId.Ingot: 180,
            ItemId.HighQualityPalOil: 45,
            ItemId.GoldCoin: 1,
            ItemId.ElectricOrgan: 70,
            ItemId.AncientCivilizationParts: 5,
        },
    ),
    ItemId.MarksmanRevolver3: Recipe(
        product=ItemId.MarksmanRevolver3,
        materials={
            ItemId.Ingot: 270,
            ItemId.HighQualityPalOil: 67,
            ItemId.GoldCoin: 1,
            ItemId.ElectricOrgan: 90,
            ItemId.AncientCivilizationParts: 7,
        },
    ),
    ItemId.MarksmanRevolver4: Recipe(
        product=ItemId.MarksmanRevolver4,
        materials={
            ItemId.Ingot: 405,
            ItemId.HighQualityPalOil: 100,
            ItemId.GoldCoin: 1,
            ItemId.ElectricOrgan: 110,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.CoreEjectShotgun: Recipe(
        product=ItemId.CoreEjectShotgun,
        materials={
            ItemId.PalMetalIngot: 80,
            ItemId.Plasteel: 65,
            ItemId.CarbonFiber: 65,
            ItemId.FlameOrgan: 40,
        },
    ),
    ItemId.CoreEjectShotgun1: Recipe(
        product=ItemId.CoreEjectShotgun1,
        materials={
            ItemId.PalMetalIngot: 160,
            ItemId.Plasteel: 130,
            ItemId.CarbonFiber: 130,
            ItemId.FlameOrgan: 60,
            ItemId.AncientCivilizationParts: 5,
        },
    ),
    ItemId.CoreEjectShotgun2: Recipe(
        product=ItemId.CoreEjectShotgun2,
        materials={
            ItemId.PalMetalIngot: 240,
            ItemId.Plasteel: 195,
            ItemId.CarbonFiber: 195,
            ItemId.FlameOrgan: 80,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.CoreEjectShotgun3: Recipe(
        product=ItemId.CoreEjectShotgun3,
        materials={
            ItemId.PalMetalIngot: 360,
            ItemId.Plasteel: 292,
            ItemId.CarbonFiber: 292,
            ItemId.FlameOrgan: 100,
            ItemId.AncientCivilizationParts: 20,
        },
    ),
    ItemId.CoreEjectShotgun4: Recipe(
        product=ItemId.CoreEjectShotgun4,
        materials={
            ItemId.PalMetalIngot: 540,
            ItemId.Plasteel: 438,
            ItemId.CarbonFiber: 438,
            ItemId.FlameOrgan: 130,
            ItemId.AncientCivilizationParts: 30,
        },
    ),
    ItemId.FragGrenade: Recipe(
        product=ItemId.FragGrenade,
        materials={
            ItemId.Fiber: 10,
            ItemId.Stone: 10,
            ItemId.Gunpowder1: 1,
        },
    ),
    ItemId.IncendiaryGrenade: Recipe(
        product=ItemId.IncendiaryGrenade,
        materials={
            ItemId.Fiber: 10,
            ItemId.Stone: 10,
            ItemId.FlameOrgan: 1,
        },
    ),
    ItemId.ShockGrenade: Recipe(
        product=ItemId.ShockGrenade,
        materials={
            ItemId.Fiber: 10,
            ItemId.Stone: 10,
            ItemId.ElectricOrgan: 1,
        },
    ),
    ItemId.IceGrenade: Recipe(
        product=ItemId.IceGrenade,
        materials={
            ItemId.Fiber: 10,
            ItemId.Stone: 10,
            ItemId.IceOrgan: 1,
        },
    ),
    ItemId.WaterGrenade: Recipe(
        product=ItemId.WaterGrenade,
        materials={
            ItemId.Fiber: 10,
            ItemId.Stone: 10,
            ItemId.PalFluids: 1,
        },
    ),
    ItemId.GrassGrenade: Recipe(
        product=ItemId.GrassGrenade,
        materials={
            ItemId.Fiber: 10,
            ItemId.Stone: 10,
            ItemId.Wood: 10,
        },
    ),
    ItemId.GroundGrenade: Recipe(
        product=ItemId.GroundGrenade,
        materials={
            ItemId.Fiber: 10,
            ItemId.Stone: 10,
            ItemId.Ore: 1,
        },
    ),
    ItemId.DarkGrenade: Recipe(
        product=ItemId.DarkGrenade,
        materials={
            ItemId.Fiber: 10,
            ItemId.Stone: 10,
            ItemId.VenomGland: 1,
        },
    ),
    ItemId.DragonGrenade: Recipe(
        product=ItemId.DragonGrenade,
        materials={
            ItemId.Fiber: 10,
            ItemId.Stone: 10,
            ItemId.Horn: 1,
        },
    ),
    ItemId.FragGrenadeMk2: Recipe(
        product=ItemId.FragGrenadeMk2,
        materials={
            ItemId.Fiber: 20,
            ItemId.PalMetalIngot: 3,
            ItemId.Gunpowder1: 3,
            ItemId.CrudeOil: 3,
        },
    ),
    ItemId.PalRecoveryGrenade: Recipe(
        product=ItemId.PalRecoveryGrenade,
        materials={
            ItemId.Fiber: 10,
            ItemId.Stone: 10,
            ItemId.CavernMushroom: 5,
        },
    ),
    ItemId.ClothOutfit: Recipe(
        product=ItemId.ClothOutfit,
        materials={
            ItemId.Cloth: 2,
        },
    ),
    ItemId.ClothOutfit1: Recipe(
        product=ItemId.ClothOutfit1,
        materials={
            ItemId.Cloth: 4,
            ItemId.AncientCivilizationParts: 1,
        },
    ),
    ItemId.ClothOutfit2: Recipe(
        product=ItemId.ClothOutfit2,
        materials={
            ItemId.Cloth: 6,
            ItemId.AncientCivilizationParts: 2,
        },
    ),
    ItemId.ClothOutfit3: Recipe(
        product=ItemId.ClothOutfit3,
        materials={
            ItemId.Cloth: 9,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.ClothOutfit4: Recipe(
        product=ItemId.ClothOutfit4,
        materials={
            ItemId.Cloth: 13,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.TropicalOutfit: Recipe(
        product=ItemId.TropicalOutfit,
        materials={
            ItemId.Cloth: 3,
            ItemId.FlameOrgan: 2,
        },
    ),
    ItemId.TropicalOutfit1: Recipe(
        product=ItemId.TropicalOutfit1,
        materials={
            ItemId.Cloth: 6,
            ItemId.FlameOrgan: 4,
            ItemId.AncientCivilizationParts: 2,
        },
    ),
    ItemId.TropicalOutfit2: Recipe(
        product=ItemId.TropicalOutfit2,
        materials={
            ItemId.Cloth: 9,
            ItemId.FlameOrgan: 6,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.TropicalOutfit3: Recipe(
        product=ItemId.TropicalOutfit3,
        materials={
            ItemId.Cloth: 13,
            ItemId.FlameOrgan: 9,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.TropicalOutfit4: Recipe(
        product=ItemId.TropicalOutfit4,
        materials={
            ItemId.Cloth: 19,
            ItemId.FlameOrgan: 13,
            ItemId.AncientCivilizationParts: 12,
        },
    ),
    ItemId.TundraOutfit: Recipe(
        product=ItemId.TundraOutfit,
        materials={
            ItemId.Cloth: 3,
            ItemId.IceOrgan: 2,
        },
    ),
    ItemId.TundraOutfit1: Recipe(
        product=ItemId.TundraOutfit1,
        materials={
            ItemId.Cloth: 6,
            ItemId.IceOrgan: 4,
            ItemId.AncientCivilizationParts: 2,
        },
    ),
    ItemId.TundraOutfit2: Recipe(
        product=ItemId.TundraOutfit2,
        materials={
            ItemId.Cloth: 9,
            ItemId.IceOrgan: 6,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.TundraOutfit3: Recipe(
        product=ItemId.TundraOutfit3,
        materials={
            ItemId.Cloth: 13,
            ItemId.IceOrgan: 9,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.TundraOutfit4: Recipe(
        product=ItemId.TundraOutfit4,
        materials={
            ItemId.Cloth: 19,
            ItemId.IceOrgan: 13,
            ItemId.AncientCivilizationParts: 12,
        },
    ),
    ItemId.PeltArmor: Recipe(
        product=ItemId.PeltArmor,
        materials={
            ItemId.Leather: 10,
        },
    ),
    ItemId.PeltArmor1: Recipe(
        product=ItemId.PeltArmor1,
        materials={
            ItemId.Leather: 20,
            ItemId.AncientCivilizationParts: 3,
        },
    ),
    ItemId.PeltArmor2: Recipe(
        product=ItemId.PeltArmor2,
        materials={
            ItemId.Leather: 30,
            ItemId.AncientCivilizationParts: 5,
        },
    ),
    ItemId.PeltArmor3: Recipe(
        product=ItemId.PeltArmor3,
        materials={
            ItemId.Leather: 45,
            ItemId.AncientCivilizationParts: 7,
        },
    ),
    ItemId.PeltArmor4: Recipe(
        product=ItemId.PeltArmor4,
        materials={
            ItemId.Leather: 67,
            ItemId.AncientCivilizationParts: 13,
        },
    ),
    ItemId.HeatResistantPeltArmor: Recipe(
        product=ItemId.HeatResistantPeltArmor,
        materials={
            ItemId.Leather: 15,
            ItemId.FlameOrgan: 4,
        },
    ),
    ItemId.HeatResistantPeltArmor1: Recipe(
        product=ItemId.HeatResistantPeltArmor1,
        materials={
            ItemId.Leather: 30,
            ItemId.FlameOrgan: 8,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.HeatResistantPeltArmor2: Recipe(
        product=ItemId.HeatResistantPeltArmor2,
        materials={
            ItemId.Leather: 45,
            ItemId.FlameOrgan: 12,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.HeatResistantPeltArmor3: Recipe(
        product=ItemId.HeatResistantPeltArmor3,
        materials={
            ItemId.Leather: 67,
            ItemId.FlameOrgan: 18,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.HeatResistantPeltArmor4: Recipe(
        product=ItemId.HeatResistantPeltArmor4,
        materials={
            ItemId.Leather: 100,
            ItemId.FlameOrgan: 27,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.ColdResistantPeltArmor: Recipe(
        product=ItemId.ColdResistantPeltArmor,
        materials={
            ItemId.Leather: 15,
            ItemId.IceOrgan: 4,
        },
    ),
    ItemId.ColdResistantPeltArmor1: Recipe(
        product=ItemId.ColdResistantPeltArmor1,
        materials={
            ItemId.Leather: 30,
            ItemId.IceOrgan: 8,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.ColdResistantPeltArmor2: Recipe(
        product=ItemId.ColdResistantPeltArmor2,
        materials={
            ItemId.Leather: 45,
            ItemId.IceOrgan: 12,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.ColdResistantPeltArmor3: Recipe(
        product=ItemId.ColdResistantPeltArmor3,
        materials={
            ItemId.Leather: 67,
            ItemId.IceOrgan: 18,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.ColdResistantPeltArmor4: Recipe(
        product=ItemId.ColdResistantPeltArmor4,
        materials={
            ItemId.Leather: 100,
            ItemId.IceOrgan: 27,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.MetalArmor: Recipe(
        product=ItemId.MetalArmor,
        materials={
            ItemId.Ingot: 30,
            ItemId.Leather: 10,
            ItemId.Cloth: 5,
        },
    ),
    ItemId.MetalArmor1: Recipe(
        product=ItemId.MetalArmor1,
        materials={
            ItemId.Ingot: 60,
            ItemId.Leather: 20,
            ItemId.Cloth: 10,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.MetalArmor2: Recipe(
        product=ItemId.MetalArmor2,
        materials={
            ItemId.Ingot: 90,
            ItemId.Leather: 30,
            ItemId.Cloth: 15,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.MetalArmor3: Recipe(
        product=ItemId.MetalArmor3,
        materials={
            ItemId.Ingot: 135,
            ItemId.Leather: 45,
            ItemId.Cloth: 22,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.MetalArmor4: Recipe(
        product=ItemId.MetalArmor4,
        materials={
            ItemId.Ingot: 202,
            ItemId.Leather: 67,
            ItemId.Cloth: 33,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.HeatResistantMetalArmor: Recipe(
        product=ItemId.HeatResistantMetalArmor,
        materials={
            ItemId.Ingot: 40,
            ItemId.Leather: 13,
            ItemId.Cloth: 8,
            ItemId.FlameOrgan: 8,
        },
    ),
    ItemId.HeatResistantMetalArmor1: Recipe(
        product=ItemId.HeatResistantMetalArmor1,
        materials={
            ItemId.Ingot: 80,
            ItemId.Leather: 26,
            ItemId.Cloth: 16,
            ItemId.FlameOrgan: 16,
            ItemId.AncientCivilizationParts: 5,
        },
    ),
    ItemId.HeatResistantMetalArmor2: Recipe(
        product=ItemId.HeatResistantMetalArmor2,
        materials={
            ItemId.Ingot: 120,
            ItemId.Leather: 39,
            ItemId.Cloth: 24,
            ItemId.FlameOrgan: 24,
            ItemId.AncientCivilizationParts: 7,
        },
    ),
    ItemId.HeatResistantMetalArmor3: Recipe(
        product=ItemId.HeatResistantMetalArmor3,
        materials={
            ItemId.Ingot: 180,
            ItemId.Leather: 58,
            ItemId.Cloth: 36,
            ItemId.FlameOrgan: 36,
            ItemId.AncientCivilizationParts: 9,
        },
    ),
    ItemId.HeatResistantMetalArmor4: Recipe(
        product=ItemId.HeatResistantMetalArmor4,
        materials={
            ItemId.Ingot: 270,
            ItemId.Leather: 87,
            ItemId.Cloth: 54,
            ItemId.FlameOrgan: 54,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.ColdResistantMetalArmor: Recipe(
        product=ItemId.ColdResistantMetalArmor,
        materials={
            ItemId.Ingot: 40,
            ItemId.Leather: 13,
            ItemId.Cloth: 8,
            ItemId.IceOrgan: 8,
        },
    ),
    ItemId.ColdResistantMetalArmor1: Recipe(
        product=ItemId.ColdResistantMetalArmor1,
        materials={
            ItemId.Ingot: 80,
            ItemId.Leather: 26,
            ItemId.Cloth: 16,
            ItemId.IceOrgan: 16,
            ItemId.AncientCivilizationParts: 5,
        },
    ),
    ItemId.ColdResistantMetalArmor2: Recipe(
        product=ItemId.ColdResistantMetalArmor2,
        materials={
            ItemId.Ingot: 120,
            ItemId.Leather: 39,
            ItemId.Cloth: 24,
            ItemId.IceOrgan: 24,
            ItemId.AncientCivilizationParts: 7,
        },
    ),
    ItemId.ColdResistantMetalArmor3: Recipe(
        product=ItemId.ColdResistantMetalArmor3,
        materials={
            ItemId.Ingot: 180,
            ItemId.Leather: 58,
            ItemId.Cloth: 36,
            ItemId.IceOrgan: 36,
            ItemId.AncientCivilizationParts: 9,
        },
    ),
    ItemId.ColdResistantMetalArmor4: Recipe(
        product=ItemId.ColdResistantMetalArmor4,
        materials={
            ItemId.Ingot: 270,
            ItemId.Leather: 87,
            ItemId.Cloth: 54,
            ItemId.IceOrgan: 54,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.RefinedMetalArmor: Recipe(
        product=ItemId.RefinedMetalArmor,
        materials={
            ItemId.RefinedIngot: 30,
            ItemId.Leather: 15,
            ItemId.HighQualityCloth: 2,
        },
    ),
    ItemId.RefinedMetalArmor1: Recipe(
        product=ItemId.RefinedMetalArmor1,
        materials={
            ItemId.RefinedIngot: 60,
            ItemId.Leather: 30,
            ItemId.HighQualityCloth: 4,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.RefinedMetalArmor2: Recipe(
        product=ItemId.RefinedMetalArmor2,
        materials={
            ItemId.RefinedIngot: 90,
            ItemId.Leather: 45,
            ItemId.HighQualityCloth: 6,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.RefinedMetalArmor3: Recipe(
        product=ItemId.RefinedMetalArmor3,
        materials={
            ItemId.RefinedIngot: 135,
            ItemId.Leather: 67,
            ItemId.HighQualityCloth: 9,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.RefinedMetalArmor4: Recipe(
        product=ItemId.RefinedMetalArmor4,
        materials={
            ItemId.RefinedIngot: 202,
            ItemId.Leather: 100,
            ItemId.HighQualityCloth: 13,
            ItemId.AncientCivilizationParts: 16,
        },
    ),
    ItemId.HeatResistantRefinedMetalArmor: Recipe(
        product=ItemId.HeatResistantRefinedMetalArmor,
        materials={
            ItemId.RefinedIngot: 40,
            ItemId.Leather: 20,
            ItemId.HighQualityCloth: 3,
            ItemId.FlameOrgan: 12,
        },
    ),
    ItemId.HeatResistantRefinedMetalArmor1: Recipe(
        product=ItemId.HeatResistantRefinedMetalArmor1,
        materials={
            ItemId.RefinedIngot: 80,
            ItemId.Leather: 40,
            ItemId.HighQualityCloth: 6,
            ItemId.FlameOrgan: 24,
            ItemId.AncientCivilizationParts: 7,
        },
    ),
    ItemId.HeatResistantRefinedMetalArmor2: Recipe(
        product=ItemId.HeatResistantRefinedMetalArmor2,
        materials={
            ItemId.RefinedIngot: 120,
            ItemId.Leather: 60,
            ItemId.HighQualityCloth: 9,
            ItemId.FlameOrgan: 36,
            ItemId.AncientCivilizationParts: 9,
        },
    ),
    ItemId.HeatResistantRefinedMetalArmor3: Recipe(
        product=ItemId.HeatResistantRefinedMetalArmor3,
        materials={
            ItemId.RefinedIngot: 180,
            ItemId.Leather: 90,
            ItemId.HighQualityCloth: 13,
            ItemId.FlameOrgan: 54,
            ItemId.AncientCivilizationParts: 11,
        },
    ),
    ItemId.HeatResistantRefinedMetalArmor4: Recipe(
        product=ItemId.HeatResistantRefinedMetalArmor4,
        materials={
            ItemId.RefinedIngot: 270,
            ItemId.Leather: 135,
            ItemId.HighQualityCloth: 19,
            ItemId.FlameOrgan: 81,
            ItemId.AncientCivilizationParts: 17,
        },
    ),
    ItemId.ColdResistantRefinedMetalArmor: Recipe(
        product=ItemId.ColdResistantRefinedMetalArmor,
        materials={
            ItemId.RefinedIngot: 40,
            ItemId.Leather: 20,
            ItemId.HighQualityCloth: 3,
            ItemId.IceOrgan: 12,
        },
    ),
    ItemId.ColdResistantRefinedMetalArmor1: Recipe(
        product=ItemId.ColdResistantRefinedMetalArmor1,
        materials={
            ItemId.RefinedIngot: 80,
            ItemId.Leather: 40,
            ItemId.HighQualityCloth: 6,
            ItemId.IceOrgan: 24,
            ItemId.AncientCivilizationParts: 7,
        },
    ),
    ItemId.ColdResistantRefinedMetalArmor2: Recipe(
        product=ItemId.ColdResistantRefinedMetalArmor2,
        materials={
            ItemId.RefinedIngot: 120,
            ItemId.Leather: 60,
            ItemId.HighQualityCloth: 9,
            ItemId.IceOrgan: 36,
            ItemId.AncientCivilizationParts: 9,
        },
    ),
    ItemId.ColdResistantRefinedMetalArmor3: Recipe(
        product=ItemId.ColdResistantRefinedMetalArmor3,
        materials={
            ItemId.RefinedIngot: 180,
            ItemId.Leather: 90,
            ItemId.HighQualityCloth: 13,
            ItemId.IceOrgan: 54,
            ItemId.AncientCivilizationParts: 11,
        },
    ),
    ItemId.ColdResistantRefinedMetalArmor4: Recipe(
        product=ItemId.ColdResistantRefinedMetalArmor4,
        materials={
            ItemId.RefinedIngot: 270,
            ItemId.Leather: 135,
            ItemId.HighQualityCloth: 19,
            ItemId.IceOrgan: 81,
            ItemId.AncientCivilizationParts: 17,
        },
    ),
    ItemId.PalMetalArmor: Recipe(
        product=ItemId.PalMetalArmor,
        materials={
            ItemId.PalMetalIngot: 20,
            ItemId.Leather: 20,
            ItemId.HighQualityCloth: 4,
        },
    ),
    ItemId.PalMetalArmor1: Recipe(
        product=ItemId.PalMetalArmor1,
        materials={
            ItemId.PalMetalIngot: 40,
            ItemId.Leather: 40,
            ItemId.HighQualityCloth: 8,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.PalMetalArmor2: Recipe(
        product=ItemId.PalMetalArmor2,
        materials={
            ItemId.PalMetalIngot: 60,
            ItemId.Leather: 60,
            ItemId.HighQualityCloth: 12,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.PalMetalArmor3: Recipe(
        product=ItemId.PalMetalArmor3,
        materials={
            ItemId.PalMetalIngot: 90,
            ItemId.Leather: 90,
            ItemId.HighQualityCloth: 18,
            ItemId.AncientCivilizationParts: 12,
        },
    ),
    ItemId.PalMetalArmor4: Recipe(
        product=ItemId.PalMetalArmor4,
        materials={
            ItemId.PalMetalIngot: 135,
            ItemId.Leather: 135,
            ItemId.HighQualityCloth: 27,
            ItemId.AncientCivilizationParts: 18,
        },
    ),
    ItemId.HeatResistantPalMetalArmor: Recipe(
        product=ItemId.HeatResistantPalMetalArmor,
        materials={
            ItemId.PalMetalIngot: 30,
            ItemId.Leather: 30,
            ItemId.HighQualityCloth: 6,
            ItemId.FlameOrgan: 16,
        },
    ),
    ItemId.HeatResistantPalMetalArmor1: Recipe(
        product=ItemId.HeatResistantPalMetalArmor1,
        materials={
            ItemId.PalMetalIngot: 60,
            ItemId.Leather: 60,
            ItemId.HighQualityCloth: 12,
            ItemId.FlameOrgan: 32,
            ItemId.AncientCivilizationParts: 9,
        },
    ),
    ItemId.HeatResistantPalMetalArmor2: Recipe(
        product=ItemId.HeatResistantPalMetalArmor2,
        materials={
            ItemId.PalMetalIngot: 90,
            ItemId.Leather: 90,
            ItemId.HighQualityCloth: 18,
            ItemId.FlameOrgan: 48,
            ItemId.AncientCivilizationParts: 11,
        },
    ),
    ItemId.HeatResistantPalMetalArmor3: Recipe(
        product=ItemId.HeatResistantPalMetalArmor3,
        materials={
            ItemId.PalMetalIngot: 135,
            ItemId.Leather: 135,
            ItemId.HighQualityCloth: 27,
            ItemId.FlameOrgan: 72,
            ItemId.AncientCivilizationParts: 13,
        },
    ),
    ItemId.HeatResistantPalMetalArmor4: Recipe(
        product=ItemId.HeatResistantPalMetalArmor4,
        materials={
            ItemId.PalMetalIngot: 202,
            ItemId.Leather: 202,
            ItemId.HighQualityCloth: 40,
            ItemId.FlameOrgan: 108,
            ItemId.AncientCivilizationParts: 19,
        },
    ),
    ItemId.ColdResistantPalMetalArmor: Recipe(
        product=ItemId.ColdResistantPalMetalArmor,
        materials={
            ItemId.PalMetalIngot: 30,
            ItemId.Leather: 30,
            ItemId.HighQualityCloth: 6,
            ItemId.IceOrgan: 16,
        },
    ),
    ItemId.ColdResistantPalMetalArmor1: Recipe(
        product=ItemId.ColdResistantPalMetalArmor1,
        materials={
            ItemId.PalMetalIngot: 60,
            ItemId.Leather: 60,
            ItemId.HighQualityCloth: 12,
            ItemId.IceOrgan: 32,
            ItemId.AncientCivilizationParts: 9,
        },
    ),
    ItemId.ColdResistantPalMetalArmor2: Recipe(
        product=ItemId.ColdResistantPalMetalArmor2,
        materials={
            ItemId.PalMetalIngot: 90,
            ItemId.Leather: 90,
            ItemId.HighQualityCloth: 18,
            ItemId.IceOrgan: 48,
            ItemId.AncientCivilizationParts: 11,
        },
    ),
    ItemId.ColdResistantPalMetalArmor3: Recipe(
        product=ItemId.ColdResistantPalMetalArmor3,
        materials={
            ItemId.PalMetalIngot: 135,
            ItemId.Leather: 135,
            ItemId.HighQualityCloth: 27,
            ItemId.IceOrgan: 72,
            ItemId.AncientCivilizationParts: 13,
        },
    ),
    ItemId.ColdResistantPalMetalArmor4: Recipe(
        product=ItemId.ColdResistantPalMetalArmor4,
        materials={
            ItemId.PalMetalIngot: 202,
            ItemId.Leather: 202,
            ItemId.HighQualityCloth: 40,
            ItemId.IceOrgan: 108,
            ItemId.AncientCivilizationParts: 19,
        },
    ),
    ItemId.PlasteelArmor: Recipe(
        product=ItemId.PlasteelArmor,
        materials={
            ItemId.Plasteel: 30,
            ItemId.PalMetalIngot: 30,
            ItemId.HighQualityCloth: 10,
        },
    ),
    ItemId.PlasteelArmor1: Recipe(
        product=ItemId.PlasteelArmor1,
        materials={
            ItemId.Plasteel: 60,
            ItemId.PalMetalIngot: 60,
            ItemId.HighQualityCloth: 20,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.PlasteelArmor2: Recipe(
        product=ItemId.PlasteelArmor2,
        materials={
            ItemId.Plasteel: 90,
            ItemId.PalMetalIngot: 90,
            ItemId.HighQualityCloth: 30,
            ItemId.AncientCivilizationParts: 17,
        },
    ),
    ItemId.PlasteelArmor3: Recipe(
        product=ItemId.PlasteelArmor3,
        materials={
            ItemId.Plasteel: 135,
            ItemId.PalMetalIngot: 135,
            ItemId.HighQualityCloth: 45,
            ItemId.AncientCivilizationParts: 19,
        },
    ),
    ItemId.PlasteelArmor4: Recipe(
        product=ItemId.PlasteelArmor4,
        materials={
            ItemId.Plasteel: 202,
            ItemId.PalMetalIngot: 202,
            ItemId.HighQualityCloth: 67,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.HeatResistantPlasteelArmor: Recipe(
        product=ItemId.HeatResistantPlasteelArmor,
        materials={
            ItemId.Plasteel: 30,
            ItemId.PalMetalIngot: 30,
            ItemId.HighQualityCloth: 10,
            ItemId.FlameOrgan: 20,
        },
    ),
    ItemId.HeatResistantPlasteelArmor1: Recipe(
        product=ItemId.HeatResistantPlasteelArmor1,
        materials={
            ItemId.Plasteel: 60,
            ItemId.PalMetalIngot: 60,
            ItemId.HighQualityCloth: 20,
            ItemId.FlameOrgan: 40,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.HeatResistantPlasteelArmor2: Recipe(
        product=ItemId.HeatResistantPlasteelArmor2,
        materials={
            ItemId.Plasteel: 90,
            ItemId.PalMetalIngot: 90,
            ItemId.HighQualityCloth: 30,
            ItemId.FlameOrgan: 60,
            ItemId.AncientCivilizationParts: 17,
        },
    ),
    ItemId.HeatResistantPlasteelArmor3: Recipe(
        product=ItemId.HeatResistantPlasteelArmor3,
        materials={
            ItemId.Plasteel: 135,
            ItemId.PalMetalIngot: 135,
            ItemId.HighQualityCloth: 45,
            ItemId.FlameOrgan: 90,
            ItemId.AncientCivilizationParts: 19,
        },
    ),
    ItemId.HeatResistantPlasteelArmor4: Recipe(
        product=ItemId.HeatResistantPlasteelArmor4,
        materials={
            ItemId.Plasteel: 202,
            ItemId.PalMetalIngot: 202,
            ItemId.HighQualityCloth: 67,
            ItemId.FlameOrgan: 135,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.ColdResistantPlasteelArmor: Recipe(
        product=ItemId.ColdResistantPlasteelArmor,
        materials={
            ItemId.Plasteel: 30,
            ItemId.PalMetalIngot: 30,
            ItemId.HighQualityCloth: 10,
            ItemId.IceOrgan: 20,
        },
    ),
    ItemId.ColdResistantPlasteelArmor1: Recipe(
        product=ItemId.ColdResistantPlasteelArmor1,
        materials={
            ItemId.Plasteel: 60,
            ItemId.PalMetalIngot: 60,
            ItemId.HighQualityCloth: 20,
            ItemId.IceOrgan: 40,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.ColdResistantPlasteelArmor2: Recipe(
        product=ItemId.ColdResistantPlasteelArmor2,
        materials={
            ItemId.Plasteel: 90,
            ItemId.PalMetalIngot: 90,
            ItemId.HighQualityCloth: 30,
            ItemId.IceOrgan: 60,
            ItemId.AncientCivilizationParts: 17,
        },
    ),
    ItemId.ColdResistantPlasteelArmor3: Recipe(
        product=ItemId.ColdResistantPlasteelArmor3,
        materials={
            ItemId.Plasteel: 135,
            ItemId.PalMetalIngot: 135,
            ItemId.HighQualityCloth: 45,
            ItemId.IceOrgan: 90,
            ItemId.AncientCivilizationParts: 19,
        },
    ),
    ItemId.ColdResistantPlasteelArmor4: Recipe(
        product=ItemId.ColdResistantPlasteelArmor4,
        materials={
            ItemId.Plasteel: 202,
            ItemId.PalMetalIngot: 202,
            ItemId.HighQualityCloth: 67,
            ItemId.IceOrgan: 135,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.LightweightPlasteelArmor: Recipe(
        product=ItemId.LightweightPlasteelArmor,
        materials={
            ItemId.Plasteel: 30,
            ItemId.PalMetalIngot: 30,
            ItemId.HighQualityCloth: 10,
        },
    ),
    ItemId.LightweightPlasteelArmor1: Recipe(
        product=ItemId.LightweightPlasteelArmor1,
        materials={
            ItemId.Plasteel: 60,
            ItemId.PalMetalIngot: 60,
            ItemId.HighQualityCloth: 20,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.LightweightPlasteelArmor2: Recipe(
        product=ItemId.LightweightPlasteelArmor2,
        materials={
            ItemId.Plasteel: 90,
            ItemId.PalMetalIngot: 90,
            ItemId.HighQualityCloth: 30,
            ItemId.AncientCivilizationParts: 17,
        },
    ),
    ItemId.LightweightPlasteelArmor3: Recipe(
        product=ItemId.LightweightPlasteelArmor3,
        materials={
            ItemId.Plasteel: 135,
            ItemId.PalMetalIngot: 135,
            ItemId.HighQualityCloth: 45,
            ItemId.AncientCivilizationParts: 19,
        },
    ),
    ItemId.LightweightPlasteelArmor4: Recipe(
        product=ItemId.LightweightPlasteelArmor4,
        materials={
            ItemId.Plasteel: 202,
            ItemId.PalMetalIngot: 202,
            ItemId.HighQualityCloth: 67,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.HexoliteArmor: Recipe(
        product=ItemId.HexoliteArmor,
        materials={
            ItemId.Hexolite: 50,
            ItemId.Plasteel: 20,
            ItemId.HighQualityCloth: 20,
        },
    ),
    ItemId.HexoliteArmor1: Recipe(
        product=ItemId.HexoliteArmor1,
        materials={
            ItemId.Hexolite: 100,
            ItemId.Plasteel: 40,
            ItemId.HighQualityCloth: 40,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.HexoliteArmor2: Recipe(
        product=ItemId.HexoliteArmor2,
        materials={
            ItemId.Hexolite: 150,
            ItemId.Plasteel: 60,
            ItemId.HighQualityCloth: 60,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.HexoliteArmor3: Recipe(
        product=ItemId.HexoliteArmor3,
        materials={
            ItemId.Hexolite: 225,
            ItemId.Plasteel: 90,
            ItemId.HighQualityCloth: 90,
            ItemId.AncientCivilizationParts: 35,
        },
    ),
    ItemId.HexoliteArmor4: Recipe(
        product=ItemId.HexoliteArmor4,
        materials={
            ItemId.Hexolite: 337,
            ItemId.Plasteel: 135,
            ItemId.HighQualityCloth: 135,
            ItemId.AncientCivilizationParts: 45,
        },
    ),
    ItemId.HeatResistantHexoliteArmor: Recipe(
        product=ItemId.HeatResistantHexoliteArmor,
        materials={
            ItemId.Hexolite: 50,
            ItemId.Plasteel: 20,
            ItemId.HighQualityCloth: 20,
            ItemId.FlameOrgan: 30,
        },
    ),
    ItemId.HeatResistantHexoliteArmor1: Recipe(
        product=ItemId.HeatResistantHexoliteArmor1,
        materials={
            ItemId.Hexolite: 100,
            ItemId.Plasteel: 40,
            ItemId.HighQualityCloth: 40,
            ItemId.FlameOrgan: 60,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.HeatResistantHexoliteArmor2: Recipe(
        product=ItemId.HeatResistantHexoliteArmor2,
        materials={
            ItemId.Hexolite: 150,
            ItemId.Plasteel: 60,
            ItemId.HighQualityCloth: 60,
            ItemId.FlameOrgan: 90,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.HeatResistantHexoliteArmor3: Recipe(
        product=ItemId.HeatResistantHexoliteArmor3,
        materials={
            ItemId.Hexolite: 225,
            ItemId.Plasteel: 90,
            ItemId.HighQualityCloth: 90,
            ItemId.FlameOrgan: 135,
            ItemId.AncientCivilizationParts: 35,
        },
    ),
    ItemId.HeatResistantHexoliteArmor4: Recipe(
        product=ItemId.HeatResistantHexoliteArmor4,
        materials={
            ItemId.Hexolite: 337,
            ItemId.Plasteel: 135,
            ItemId.HighQualityCloth: 135,
            ItemId.FlameOrgan: 202,
            ItemId.AncientCivilizationParts: 45,
        },
    ),
    ItemId.ColdResistantHexoliteArmor: Recipe(
        product=ItemId.ColdResistantHexoliteArmor,
        materials={
            ItemId.Hexolite: 50,
            ItemId.Plasteel: 20,
            ItemId.HighQualityCloth: 20,
            ItemId.IceOrgan: 30,
        },
    ),
    ItemId.ColdResistantHexoliteArmor1: Recipe(
        product=ItemId.ColdResistantHexoliteArmor1,
        materials={
            ItemId.Hexolite: 100,
            ItemId.Plasteel: 40,
            ItemId.HighQualityCloth: 40,
            ItemId.IceOrgan: 60,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.ColdResistantHexoliteArmor2: Recipe(
        product=ItemId.ColdResistantHexoliteArmor2,
        materials={
            ItemId.Hexolite: 150,
            ItemId.Plasteel: 60,
            ItemId.HighQualityCloth: 60,
            ItemId.IceOrgan: 90,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.ColdResistantHexoliteArmor3: Recipe(
        product=ItemId.ColdResistantHexoliteArmor3,
        materials={
            ItemId.Hexolite: 225,
            ItemId.Plasteel: 90,
            ItemId.HighQualityCloth: 90,
            ItemId.IceOrgan: 135,
            ItemId.AncientCivilizationParts: 35,
        },
    ),
    ItemId.ColdResistantHexoliteArmor4: Recipe(
        product=ItemId.ColdResistantHexoliteArmor4,
        materials={
            ItemId.Hexolite: 337,
            ItemId.Plasteel: 135,
            ItemId.HighQualityCloth: 135,
            ItemId.IceOrgan: 202,
            ItemId.AncientCivilizationParts: 45,
        },
    ),
    ItemId.LightweightHexoliteArmor: Recipe(
        product=ItemId.LightweightHexoliteArmor,
        materials={
            ItemId.Hexolite: 100,
            ItemId.Plasteel: 20,
            ItemId.HighQualityCloth: 20,
        },
    ),
    ItemId.LightweightHexoliteArmor1: Recipe(
        product=ItemId.LightweightHexoliteArmor1,
        materials={
            ItemId.Hexolite: 200,
            ItemId.Plasteel: 40,
            ItemId.HighQualityCloth: 40,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.LightweightHexoliteArmor2: Recipe(
        product=ItemId.LightweightHexoliteArmor2,
        materials={
            ItemId.Hexolite: 300,
            ItemId.Plasteel: 60,
            ItemId.HighQualityCloth: 60,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.LightweightHexoliteArmor3: Recipe(
        product=ItemId.LightweightHexoliteArmor3,
        materials={
            ItemId.Hexolite: 450,
            ItemId.Plasteel: 90,
            ItemId.HighQualityCloth: 90,
            ItemId.AncientCivilizationParts: 35,
        },
    ),
    ItemId.LightweightHexoliteArmor4: Recipe(
        product=ItemId.LightweightHexoliteArmor4,
        materials={
            ItemId.Hexolite: 675,
            ItemId.Plasteel: 135,
            ItemId.HighQualityCloth: 135,
            ItemId.AncientCivilizationParts: 45,
        },
    ),
    ItemId.FeatheredHairBand: Recipe(
        product=ItemId.FeatheredHairBand,
        materials={
            ItemId.Fiber: 10,
            ItemId.PaldiumFragment: 5,
        },
    ),
    ItemId.FeatheredHairBand1: Recipe(
        product=ItemId.FeatheredHairBand1,
        materials={
            ItemId.Fiber: 20,
            ItemId.PaldiumFragment: 10,
            ItemId.AncientCivilizationParts: 3,
        },
    ),
    ItemId.FeatheredHairBand2: Recipe(
        product=ItemId.FeatheredHairBand2,
        materials={
            ItemId.Fiber: 30,
            ItemId.PaldiumFragment: 15,
            ItemId.AncientCivilizationParts: 5,
        },
    ),
    ItemId.FeatheredHairBand3: Recipe(
        product=ItemId.FeatheredHairBand3,
        materials={
            ItemId.Fiber: 45,
            ItemId.PaldiumFragment: 22,
            ItemId.AncientCivilizationParts: 7,
        },
    ),
    ItemId.FeatheredHairBand4: Recipe(
        product=ItemId.FeatheredHairBand4,
        materials={
            ItemId.Fiber: 67,
            ItemId.PaldiumFragment: 33,
            ItemId.AncientCivilizationParts: 13,
        },
    ),
    ItemId.MetalHelm: Recipe(
        product=ItemId.MetalHelm,
        materials={
            ItemId.Ingot: 20,
            ItemId.PaldiumFragment: 10,
        },
    ),
    ItemId.MetalHelm1: Recipe(
        product=ItemId.MetalHelm1,
        materials={
            ItemId.Ingot: 40,
            ItemId.PaldiumFragment: 20,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.MetalHelm2: Recipe(
        product=ItemId.MetalHelm2,
        materials={
            ItemId.Ingot: 60,
            ItemId.PaldiumFragment: 30,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.MetalHelm3: Recipe(
        product=ItemId.MetalHelm3,
        materials={
            ItemId.Ingot: 90,
            ItemId.PaldiumFragment: 45,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.MetalHelm4: Recipe(
        product=ItemId.MetalHelm4,
        materials={
            ItemId.Ingot: 135,
            ItemId.PaldiumFragment: 67,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.RefinedMetalHelm: Recipe(
        product=ItemId.RefinedMetalHelm,
        materials={
            ItemId.RefinedIngot: 20,
            ItemId.PaldiumFragment: 15,
        },
    ),
    ItemId.RefinedMetalHelm1: Recipe(
        product=ItemId.RefinedMetalHelm1,
        materials={
            ItemId.RefinedIngot: 40,
            ItemId.PaldiumFragment: 30,
            ItemId.AncientCivilizationParts: 7,
        },
    ),
    ItemId.RefinedMetalHelm2: Recipe(
        product=ItemId.RefinedMetalHelm2,
        materials={
            ItemId.RefinedIngot: 60,
            ItemId.PaldiumFragment: 45,
            ItemId.AncientCivilizationParts: 9,
        },
    ),
    ItemId.RefinedMetalHelm3: Recipe(
        product=ItemId.RefinedMetalHelm3,
        materials={
            ItemId.RefinedIngot: 90,
            ItemId.PaldiumFragment: 67,
            ItemId.AncientCivilizationParts: 11,
        },
    ),
    ItemId.RefinedMetalHelm4: Recipe(
        product=ItemId.RefinedMetalHelm4,
        materials={
            ItemId.RefinedIngot: 135,
            ItemId.PaldiumFragment: 100,
            ItemId.AncientCivilizationParts: 17,
        },
    ),
    ItemId.PalMetalHelm: Recipe(
        product=ItemId.PalMetalHelm,
        materials={
            ItemId.PalMetalIngot: 20,
            ItemId.PaldiumFragment: 20,
        },
    ),
    ItemId.PalMetalHelm1: Recipe(
        product=ItemId.PalMetalHelm1,
        materials={
            ItemId.PalMetalIngot: 40,
            ItemId.PaldiumFragment: 40,
            ItemId.AncientCivilizationParts: 9,
        },
    ),
    ItemId.PalMetalHelm2: Recipe(
        product=ItemId.PalMetalHelm2,
        materials={
            ItemId.PalMetalIngot: 60,
            ItemId.PaldiumFragment: 60,
            ItemId.AncientCivilizationParts: 11,
        },
    ),
    ItemId.PalMetalHelm3: Recipe(
        product=ItemId.PalMetalHelm3,
        materials={
            ItemId.PalMetalIngot: 90,
            ItemId.PaldiumFragment: 90,
            ItemId.AncientCivilizationParts: 13,
        },
    ),
    ItemId.PalMetalHelm4: Recipe(
        product=ItemId.PalMetalHelm4,
        materials={
            ItemId.PalMetalIngot: 135,
            ItemId.PaldiumFragment: 135,
            ItemId.AncientCivilizationParts: 19,
        },
    ),
    ItemId.PlasteelHelmet: Recipe(
        product=ItemId.PlasteelHelmet,
        materials={
            ItemId.Plasteel: 20,
            ItemId.PalMetalIngot: 25,
        },
    ),
    ItemId.PlasteelHelmet1: Recipe(
        product=ItemId.PlasteelHelmet1,
        materials={
            ItemId.Plasteel: 40,
            ItemId.PalMetalIngot: 50,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.PlasteelHelmet2: Recipe(
        product=ItemId.PlasteelHelmet2,
        materials={
            ItemId.Plasteel: 60,
            ItemId.PalMetalIngot: 75,
            ItemId.AncientCivilizationParts: 17,
        },
    ),
    ItemId.PlasteelHelmet3: Recipe(
        product=ItemId.PlasteelHelmet3,
        materials={
            ItemId.Plasteel: 90,
            ItemId.PalMetalIngot: 112,
            ItemId.AncientCivilizationParts: 19,
        },
    ),
    ItemId.PlasteelHelmet4: Recipe(
        product=ItemId.PlasteelHelmet4,
        materials={
            ItemId.Plasteel: 135,
            ItemId.PalMetalIngot: 168,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.HexoliteHelmet: Recipe(
        product=ItemId.HexoliteHelmet,
        materials={
            ItemId.Hexolite: 40,
            ItemId.Plasteel: 15,
        },
    ),
    ItemId.HexoliteHelmet1: Recipe(
        product=ItemId.HexoliteHelmet1,
        materials={
            ItemId.Hexolite: 80,
            ItemId.Plasteel: 30,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.HexoliteHelmet2: Recipe(
        product=ItemId.HexoliteHelmet2,
        materials={
            ItemId.Hexolite: 120,
            ItemId.Plasteel: 45,
            ItemId.AncientCivilizationParts: 25,
        },
    ),
    ItemId.HexoliteHelmet3: Recipe(
        product=ItemId.HexoliteHelmet3,
        materials={
            ItemId.Hexolite: 180,
            ItemId.Plasteel: 67,
            ItemId.AncientCivilizationParts: 35,
        },
    ),
    ItemId.HexoliteHelmet4: Recipe(
        product=ItemId.HexoliteHelmet4,
        materials={
            ItemId.Hexolite: 270,
            ItemId.Plasteel: 100,
            ItemId.AncientCivilizationParts: 45,
        },
    ),
    ItemId.V1Armor: Recipe(
        product=ItemId.V1Armor,
        materials={
            ItemId.Ingot: 30,
            ItemId.HighQualityPalOil: 15,
        },
    ),
    ItemId.V1Armor4: Recipe(
        product=ItemId.V1Armor4,
        materials={
            ItemId.Ingot: 270,
            ItemId.HighQualityPalOil: 85,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.V2Armor: Recipe(
        product=ItemId.V2Armor,
        materials={
            ItemId.Plasteel: 40,
            ItemId.PalMetalIngot: 40,
            ItemId.HighQualityCloth: 20,
        },
    ),
    ItemId.V2Armor4: Recipe(
        product=ItemId.V2Armor4,
        materials={
            ItemId.Plasteel: 270,
            ItemId.PalMetalIngot: 202,
            ItemId.HighQualityCloth: 80,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.MonarchSCrown: Recipe(
        product=ItemId.MonarchSCrown,
        materials={
            ItemId.Ingot: 20,
            ItemId.Cloth: 3,
        },
    ),
    ItemId.MonarchSCrown1: Recipe(
        product=ItemId.MonarchSCrown1,
        materials={
            ItemId.Ingot: 30,
            ItemId.Cloth: 4,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.MonarchSCrown2: Recipe(
        product=ItemId.MonarchSCrown2,
        materials={
            ItemId.Ingot: 45,
            ItemId.Cloth: 6,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.MonarchSCrown3: Recipe(
        product=ItemId.MonarchSCrown3,
        materials={
            ItemId.Ingot: 67,
            ItemId.Cloth: 9,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.MonarchSCrown4: Recipe(
        product=ItemId.MonarchSCrown4,
        materials={
            ItemId.Ingot: 100,
            ItemId.Cloth: 13,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.GoldenCrown: Recipe(
        product=ItemId.GoldenCrown,
        materials={
            ItemId.Ingot: 25,
        },
    ),
    ItemId.GoldenCrown1: Recipe(
        product=ItemId.GoldenCrown1,
        materials={
            ItemId.Ingot: 37,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.GoldenCrown2: Recipe(
        product=ItemId.GoldenCrown2,
        materials={
            ItemId.Ingot: 55,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.GoldenCrown3: Recipe(
        product=ItemId.GoldenCrown3,
        materials={
            ItemId.Ingot: 82,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.GoldenCrown4: Recipe(
        product=ItemId.GoldenCrown4,
        materials={
            ItemId.Ingot: 123,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.LongEaredHeadband: Recipe(
        product=ItemId.LongEaredHeadband,
        materials={
            ItemId.Cloth: 12,
            ItemId.Ingot: 2,
        },
    ),
    ItemId.LongEaredHeadband1: Recipe(
        product=ItemId.LongEaredHeadband1,
        materials={
            ItemId.Cloth: 18,
            ItemId.Ingot: 3,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.LongEaredHeadband2: Recipe(
        product=ItemId.LongEaredHeadband2,
        materials={
            ItemId.Cloth: 27,
            ItemId.Ingot: 4,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.LongEaredHeadband3: Recipe(
        product=ItemId.LongEaredHeadband3,
        materials={
            ItemId.Cloth: 40,
            ItemId.Ingot: 6,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.LongEaredHeadband4: Recipe(
        product=ItemId.LongEaredHeadband4,
        materials={
            ItemId.Cloth: 60,
            ItemId.Ingot: 9,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.WitchHat: Recipe(
        product=ItemId.WitchHat,
        materials={
            ItemId.Cloth: 10,
            ItemId.Ingot: 3,
        },
    ),
    ItemId.WitchHat1: Recipe(
        product=ItemId.WitchHat1,
        materials={
            ItemId.Cloth: 15,
            ItemId.Ingot: 4,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.WitchHat2: Recipe(
        product=ItemId.WitchHat2,
        materials={
            ItemId.Cloth: 22,
            ItemId.Ingot: 6,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.WitchHat3: Recipe(
        product=ItemId.WitchHat3,
        materials={
            ItemId.Cloth: 33,
            ItemId.Ingot: 9,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.WitchHat4: Recipe(
        product=ItemId.WitchHat4,
        materials={
            ItemId.Cloth: 49,
            ItemId.Ingot: 13,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.SoftHat: Recipe(
        product=ItemId.SoftHat,
        materials={
            ItemId.Cloth: 10,
            ItemId.Fiber: 10,
        },
    ),
    ItemId.SoftHat1: Recipe(
        product=ItemId.SoftHat1,
        materials={
            ItemId.Cloth: 15,
            ItemId.Fiber: 15,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.SoftHat2: Recipe(
        product=ItemId.SoftHat2,
        materials={
            ItemId.Cloth: 22,
            ItemId.Fiber: 22,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.SoftHat3: Recipe(
        product=ItemId.SoftHat3,
        materials={
            ItemId.Cloth: 33,
            ItemId.Fiber: 33,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.SoftHat4: Recipe(
        product=ItemId.SoftHat4,
        materials={
            ItemId.Cloth: 49,
            ItemId.Fiber: 49,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.Helmet: Recipe(
        product=ItemId.Helmet,
        materials={
            ItemId.Ingot: 20,
            ItemId.Wool: 5,
        },
    ),
    ItemId.Helmet1: Recipe(
        product=ItemId.Helmet1,
        materials={
            ItemId.Ingot: 30,
            ItemId.Wool: 7,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.Helmet2: Recipe(
        product=ItemId.Helmet2,
        materials={
            ItemId.Ingot: 45,
            ItemId.Wool: 10,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.Helmet3: Recipe(
        product=ItemId.Helmet3,
        materials={
            ItemId.Ingot: 67,
            ItemId.Wool: 15,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.Helmet4: Recipe(
        product=ItemId.Helmet4,
        materials={
            ItemId.Ingot: 100,
            ItemId.Wool: 22,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.SilkHat: Recipe(
        product=ItemId.SilkHat,
        materials={
            ItemId.Cloth: 15,
        },
    ),
    ItemId.SilkHat1: Recipe(
        product=ItemId.SilkHat1,
        materials={
            ItemId.Cloth: 22,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.SilkHat2: Recipe(
        product=ItemId.SilkHat2,
        materials={
            ItemId.Cloth: 33,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.SilkHat3: Recipe(
        product=ItemId.SilkHat3,
        materials={
            ItemId.Cloth: 49,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.SilkHat4: Recipe(
        product=ItemId.SilkHat4,
        materials={
            ItemId.Cloth: 73,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.Tricorne: Recipe(
        product=ItemId.Tricorne,
        materials={
            ItemId.Leather: 10,
        },
    ),
    ItemId.Tricorne1: Recipe(
        product=ItemId.Tricorne1,
        materials={
            ItemId.Leather: 15,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.Tricorne2: Recipe(
        product=ItemId.Tricorne2,
        materials={
            ItemId.Leather: 22,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.Tricorne3: Recipe(
        product=ItemId.Tricorne3,
        materials={
            ItemId.Leather: 33,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.Tricorne4: Recipe(
        product=ItemId.Tricorne4,
        materials={
            ItemId.Leather: 49,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.ExplorerCap: Recipe(
        product=ItemId.ExplorerCap,
        materials={
            ItemId.Cloth: 10,
            ItemId.Leather: 3,
            ItemId.Ingot: 2,
        },
    ),
    ItemId.ExplorerCap1: Recipe(
        product=ItemId.ExplorerCap1,
        materials={
            ItemId.Cloth: 15,
            ItemId.Leather: 4,
            ItemId.Ingot: 3,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.ExplorerCap2: Recipe(
        product=ItemId.ExplorerCap2,
        materials={
            ItemId.Cloth: 22,
            ItemId.Leather: 6,
            ItemId.Ingot: 4,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.ExplorerCap3: Recipe(
        product=ItemId.ExplorerCap3,
        materials={
            ItemId.Cloth: 33,
            ItemId.Leather: 9,
            ItemId.Ingot: 6,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.ExplorerCap4: Recipe(
        product=ItemId.ExplorerCap4,
        materials={
            ItemId.Cloth: 49,
            ItemId.Leather: 13,
            ItemId.Ingot: 9,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.GraduationCap: Recipe(
        product=ItemId.GraduationCap,
        materials={
            ItemId.Cloth: 20,
            ItemId.Fiber: 10,
        },
    ),
    ItemId.GraduationCap1: Recipe(
        product=ItemId.GraduationCap1,
        materials={
            ItemId.Cloth: 30,
            ItemId.Fiber: 15,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.GraduationCap2: Recipe(
        product=ItemId.GraduationCap2,
        materials={
            ItemId.Cloth: 45,
            ItemId.Fiber: 22,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.GraduationCap3: Recipe(
        product=ItemId.GraduationCap3,
        materials={
            ItemId.Cloth: 67,
            ItemId.Fiber: 33,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.GraduationCap4: Recipe(
        product=ItemId.GraduationCap4,
        materials={
            ItemId.Cloth: 100,
            ItemId.Fiber: 49,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.FarmingHat: Recipe(
        product=ItemId.FarmingHat,
        materials={
            ItemId.Fiber: 30,
            ItemId.Wood: 10,
        },
    ),
    ItemId.FarmingHat1: Recipe(
        product=ItemId.FarmingHat1,
        materials={
            ItemId.Fiber: 45,
            ItemId.Wood: 15,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.FarmingHat2: Recipe(
        product=ItemId.FarmingHat2,
        materials={
            ItemId.Fiber: 67,
            ItemId.Wood: 22,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.FarmingHat3: Recipe(
        product=ItemId.FarmingHat3,
        materials={
            ItemId.Fiber: 100,
            ItemId.Wood: 33,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.FarmingHat4: Recipe(
        product=ItemId.FarmingHat4,
        materials={
            ItemId.Fiber: 150,
            ItemId.Wood: 49,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.BowlerHat: Recipe(
        product=ItemId.BowlerHat,
        materials={
            ItemId.Cloth: 15,
        },
    ),
    ItemId.BowlerHat1: Recipe(
        product=ItemId.BowlerHat1,
        materials={
            ItemId.Cloth: 22,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.BowlerHat2: Recipe(
        product=ItemId.BowlerHat2,
        materials={
            ItemId.Cloth: 33,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.BowlerHat3: Recipe(
        product=ItemId.BowlerHat3,
        materials={
            ItemId.Cloth: 49,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.BowlerHat4: Recipe(
        product=ItemId.BowlerHat4,
        materials={
            ItemId.Cloth: 73,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.TocotocoCap: Recipe(
        product=ItemId.TocotocoCap,
        materials={
            ItemId.TocotocoFeather: 5,
        },
    ),
    ItemId.TocotocoCap1: Recipe(
        product=ItemId.TocotocoCap1,
        materials={
            ItemId.TocotocoFeather: 7,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.TocotocoCap2: Recipe(
        product=ItemId.TocotocoCap2,
        materials={
            ItemId.TocotocoFeather: 10,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.TocotocoCap3: Recipe(
        product=ItemId.TocotocoCap3,
        materials={
            ItemId.TocotocoFeather: 15,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.TocotocoCap4: Recipe(
        product=ItemId.TocotocoCap4,
        materials={
            ItemId.TocotocoFeather: 22,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.GrinningTocotocoCap: Recipe(
        product=ItemId.GrinningTocotocoCap,
        materials={
            ItemId.TocotocoFeather: 5,
        },
    ),
    ItemId.GrinningTocotocoCap1: Recipe(
        product=ItemId.GrinningTocotocoCap1,
        materials={
            ItemId.TocotocoFeather: 7,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.GrinningTocotocoCap2: Recipe(
        product=ItemId.GrinningTocotocoCap2,
        materials={
            ItemId.TocotocoFeather: 10,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.GrinningTocotocoCap3: Recipe(
        product=ItemId.GrinningTocotocoCap3,
        materials={
            ItemId.TocotocoFeather: 15,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.GrinningTocotocoCap4: Recipe(
        product=ItemId.GrinningTocotocoCap4,
        materials={
            ItemId.TocotocoFeather: 22,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.GumossCap: Recipe(
        product=ItemId.GumossCap,
        materials={
            ItemId.GumossLeaf: 5,
        },
    ),
    ItemId.GumossCap1: Recipe(
        product=ItemId.GumossCap1,
        materials={
            ItemId.GumossLeaf: 7,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.GumossCap2: Recipe(
        product=ItemId.GumossCap2,
        materials={
            ItemId.GumossLeaf: 10,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.GumossCap3: Recipe(
        product=ItemId.GumossCap3,
        materials={
            ItemId.GumossLeaf: 15,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.GumossCap4: Recipe(
        product=ItemId.GumossCap4,
        materials={
            ItemId.GumossLeaf: 22,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.PenkingCap: Recipe(
        product=ItemId.PenkingCap,
        materials={
            ItemId.PenkingPlume: 5,
        },
    ),
    ItemId.PenkingCap1: Recipe(
        product=ItemId.PenkingCap1,
        materials={
            ItemId.PenkingPlume: 7,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.PenkingCap2: Recipe(
        product=ItemId.PenkingCap2,
        materials={
            ItemId.PenkingPlume: 10,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.PenkingCap3: Recipe(
        product=ItemId.PenkingCap3,
        materials={
            ItemId.PenkingPlume: 15,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.PenkingCap4: Recipe(
        product=ItemId.PenkingCap4,
        materials={
            ItemId.PenkingPlume: 22,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.KatressCap: Recipe(
        product=ItemId.KatressCap,
        materials={
            ItemId.KatressHair: 5,
        },
    ),
    ItemId.KatressCap1: Recipe(
        product=ItemId.KatressCap1,
        materials={
            ItemId.KatressHair: 7,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.KatressCap2: Recipe(
        product=ItemId.KatressCap2,
        materials={
            ItemId.KatressHair: 10,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.KatressCap3: Recipe(
        product=ItemId.KatressCap3,
        materials={
            ItemId.KatressHair: 15,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.KatressCap4: Recipe(
        product=ItemId.KatressCap4,
        materials={
            ItemId.KatressHair: 22,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.RibbunyHeadband: Recipe(
        product=ItemId.RibbunyHeadband,
        materials={
            ItemId.RibbunyRibbon: 5,
        },
    ),
    ItemId.RibbunyHeadband1: Recipe(
        product=ItemId.RibbunyHeadband1,
        materials={
            ItemId.RibbunyRibbon: 7,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.RibbunyHeadband2: Recipe(
        product=ItemId.RibbunyHeadband2,
        materials={
            ItemId.RibbunyRibbon: 10,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.RibbunyHeadband3: Recipe(
        product=ItemId.RibbunyHeadband3,
        materials={
            ItemId.RibbunyRibbon: 15,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.RibbunyHeadband4: Recipe(
        product=ItemId.RibbunyHeadband4,
        materials={
            ItemId.RibbunyRibbon: 22,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.LeezpunkHood: Recipe(
        product=ItemId.LeezpunkHood,
        materials={
            ItemId.LeezpunkCrest: 5,
        },
    ),
    ItemId.LeezpunkHood1: Recipe(
        product=ItemId.LeezpunkHood1,
        materials={
            ItemId.LeezpunkCrest: 7,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.LeezpunkHood2: Recipe(
        product=ItemId.LeezpunkHood2,
        materials={
            ItemId.LeezpunkCrest: 10,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.LeezpunkHood3: Recipe(
        product=ItemId.LeezpunkHood3,
        materials={
            ItemId.LeezpunkCrest: 15,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.LeezpunkHood4: Recipe(
        product=ItemId.LeezpunkHood4,
        materials={
            ItemId.LeezpunkCrest: 22,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.KillamariCap: Recipe(
        product=ItemId.KillamariCap,
        materials={
            ItemId.KillamariTentacle: 5,
        },
    ),
    ItemId.KillamariCap1: Recipe(
        product=ItemId.KillamariCap1,
        materials={
            ItemId.KillamariTentacle: 7,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.KillamariCap2: Recipe(
        product=ItemId.KillamariCap2,
        materials={
            ItemId.KillamariTentacle: 10,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.KillamariCap3: Recipe(
        product=ItemId.KillamariCap3,
        materials={
            ItemId.KillamariTentacle: 15,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.KillamariCap4: Recipe(
        product=ItemId.KillamariCap4,
        materials={
            ItemId.KillamariTentacle: 22,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.SweeCap: Recipe(
        product=ItemId.SweeCap,
        materials={
            ItemId.SweeHair: 5,
        },
    ),
    ItemId.SweeCap1: Recipe(
        product=ItemId.SweeCap1,
        materials={
            ItemId.SweeHair: 7,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.SweeCap2: Recipe(
        product=ItemId.SweeCap2,
        materials={
            ItemId.SweeHair: 10,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.SweeCap3: Recipe(
        product=ItemId.SweeCap3,
        materials={
            ItemId.SweeHair: 15,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.SweeCap4: Recipe(
        product=ItemId.SweeCap4,
        materials={
            ItemId.SweeHair: 22,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.DazziHat: Recipe(
        product=ItemId.DazziHat,
        materials={
            ItemId.DazziCloud: 5,
        },
    ),
    ItemId.DazziHat1: Recipe(
        product=ItemId.DazziHat1,
        materials={
            ItemId.DazziCloud: 7,
            ItemId.AncientCivilizationParts: 4,
        },
    ),
    ItemId.DazziHat2: Recipe(
        product=ItemId.DazziHat2,
        materials={
            ItemId.DazziCloud: 10,
            ItemId.AncientCivilizationParts: 6,
        },
    ),
    ItemId.DazziHat3: Recipe(
        product=ItemId.DazziHat3,
        materials={
            ItemId.DazziCloud: 15,
            ItemId.AncientCivilizationParts: 8,
        },
    ),
    ItemId.DazziHat4: Recipe(
        product=ItemId.DazziHat4,
        materials={
            ItemId.DazziCloud: 22,
            ItemId.AncientCivilizationParts: 14,
        },
    ),
    ItemId.RingOfMercy: Recipe(
        product=ItemId.RingOfMercy,
        materials={
            ItemId.Ingot: 30,
            ItemId.PaldiumFragment: 20,
            ItemId.AncientCivilizationParts: 5,
        },
    ),
    ItemId.AbilityGlasses: Recipe(
        product=ItemId.AbilityGlasses,
        materials={
            ItemId.RefinedIngot: 30,
            ItemId.PaldiumFragment: 20,
            ItemId.AncientCivilizationParts: 10,
            ItemId.AncientCivilizationCore: 5,
        },
    ),
    ItemId.AntiGravityBelt: Recipe(
        product=ItemId.AntiGravityBelt,
        materials={
            ItemId.Ingot: 30,
            ItemId.PaldiumFragment: 30,
            ItemId.NightstarSand: 10,
        },
    ),
    ItemId.DoubleJumpBoots: Recipe(
        product=ItemId.DoubleJumpBoots,
        materials={
            ItemId.RefinedIngot: 30,
            ItemId.PaldiumFragment: 50,
            ItemId.NightstarSand: 20,
        },
    ),
    ItemId.TripleJumpBoots: Recipe(
        product=ItemId.TripleJumpBoots,
        materials={
            ItemId.Hexolite: 30,
            ItemId.PaldiumFragment: 150,
            ItemId.NightstarSand: 50,
            ItemId.DarkFragment: 50,
        },
    ),
    ItemId.AirDashBoots: Recipe(
        product=ItemId.AirDashBoots,
        materials={
            ItemId.RefinedIngot: 30,
            ItemId.PaldiumFragment: 50,
            ItemId.NightstarSand: 20,
        },
    ),
    ItemId.DoubleAirDashBoots: Recipe(
        product=ItemId.DoubleAirDashBoots,
        materials={
            ItemId.Plasteel: 30,
            ItemId.PaldiumFragment: 100,
            ItemId.NightstarSand: 30,
            ItemId.DarkFragment: 30,
        },
    ),
    ItemId.TripleAirDashBoots: Recipe(
        product=ItemId.TripleAirDashBoots,
        materials={
            ItemId.CoralumIngot: 30,
            ItemId.PaldiumFragment: 150,
            ItemId.NightstarSand: 40,
            ItemId.DarkFragment: 50,
        },
    ),
    ItemId.Arrow: Recipe(
        product=ItemId.Arrow,
        materials={
            ItemId.Wood: 1,
            ItemId.Stone: 1,
        },
    ),
    ItemId.FireArrow: Recipe(
        product=ItemId.FireArrow,
        materials={
            ItemId.Wood: 3,
            ItemId.Stone: 3,
            ItemId.FlameOrgan: 1,
        },
    ),
    ItemId.PoisonArrow: Recipe(
        product=ItemId.PoisonArrow,
        materials={
            ItemId.Wood: 3,
            ItemId.Stone: 3,
            ItemId.VenomGland: 1,
        },
    ),
    ItemId.ReinforcedArrow: Recipe(
        product=ItemId.ReinforcedArrow,
        materials={
            ItemId.Ingot: 1,
            ItemId.Stone: 2,
        },
    ),
    ItemId.AdvancedArrow: Recipe(
        product=ItemId.AdvancedArrow,
        materials={
            ItemId.Hexolite: 1,
            ItemId.Stone: 10,
        },
    ),
    ItemId.CoarseAmmo: Recipe(
        product=ItemId.CoarseAmmo,
        materials={
            ItemId.Ingot: 2,
            ItemId.Gunpowder1: 1,
        },
    ),
    ItemId.BoostGunAmmo: Recipe(
        product=ItemId.BoostGunAmmo,
        materials={
            ItemId.Ingot: 2,
            ItemId.ElectricOrgan: 1,
        },
    ),
    ItemId.HandgunAmmo: Recipe(
        product=ItemId.HandgunAmmo,
        materials={
            ItemId.Ingot: 2,
            ItemId.Gunpowder1: 1,
        },
    ),
    ItemId.RifleAmmo: Recipe(
        product=ItemId.RifleAmmo,
        materials={
            ItemId.RefinedIngot: 1,
            ItemId.Gunpowder1: 2,
        },
    ),
    ItemId.ShotgunShell: Recipe(
        product=ItemId.ShotgunShell,
        materials={
            ItemId.RefinedIngot: 1,
            ItemId.Gunpowder1: 3,
        },
    ),
    ItemId.AssaultRifleAmmo: Recipe(
        product=ItemId.AssaultRifleAmmo,
        materials={
            ItemId.RefinedIngot: 1,
            ItemId.Gunpowder1: 2,
        },
    ),
    ItemId.RocketAmmo: Recipe(
        product=ItemId.RocketAmmo,
        materials={
            ItemId.PalMetalIngot: 1,
            ItemId.Gunpowder1: 5,
        },
    ),
    ItemId.FlamethrowerFuel: Recipe(
        product=ItemId.FlamethrowerFuel,
        materials={
            ItemId.CrudeOil: 1,
        },
    ),
    ItemId.EnergyCartridge: Recipe(
        product=ItemId.EnergyCartridge,
        materials={
            ItemId.ElectricOrgan: 5,
            ItemId.PalMetalIngot: 1,
        },
    ),
    ItemId.GrenadeAmmo: Recipe(
        product=ItemId.GrenadeAmmo,
        materials={
            ItemId.PalMetalIngot: 1,
            ItemId.Fiber: 20,
            ItemId.Gunpowder1: 3,
        },
    ),
    ItemId.MissileAmmo: Recipe(
        product=ItemId.MissileAmmo,
        materials={
            ItemId.PalMetalIngot: 1,
            ItemId.CrudeOil: 1,
            ItemId.CircuitBoard: 1,
            ItemId.PalFluids: 1,
        },
    ),
    ItemId.GatlingGunAmmo: Recipe(
        product=ItemId.GatlingGunAmmo,
        materials={
            ItemId.PalMetalIngot: 1,
            ItemId.Gunpowder1: 3,
        },
    ),
    ItemId.LaserGatlingCartridge: Recipe(
        product=ItemId.LaserGatlingCartridge,
        materials={
            ItemId.ElectricOrgan: 5,
            ItemId.Plasteel: 1,
        },
    ),
    ItemId.PlasmaCartridge: Recipe(
        product=ItemId.PlasmaCartridge,
        materials={
            ItemId.ElectricOrgan: 10,
            ItemId.Hexolite: 1,
        },
    ),
    ItemId.MeteoriteAmmo: Recipe(
        product=ItemId.MeteoriteAmmo,
        materials={
            ItemId.MeteoriteFragment: 2,
        },
    ),
    ItemId.EnergyShotgunAmmo: Recipe(
        product=ItemId.EnergyShotgunAmmo,
        materials={
            ItemId.ElectricOrgan: 10,
            ItemId.Hexolite: 1,
            ItemId.CoralumIngot: 1,
        },
    ),
    ItemId.OverheatRifleAmmo: Recipe(
        product=ItemId.OverheatRifleAmmo,
        materials={
            ItemId.ElectricOrgan: 10,
            ItemId.Hexolite: 1,
            ItemId.CoralumIngot: 1,
        },
    ),
    ItemId.ChargeRifleAmmo: Recipe(
        product=ItemId.ChargeRifleAmmo,
        materials={
            ItemId.ElectricOrgan: 10,
            ItemId.Hexolite: 1,
            ItemId.CoralumIngot: 1,
        },
    ),
    ItemId.DecalInk: Recipe(
        product=ItemId.DecalInk,
        materials={
            ItemId.PalFluids: 1,
            ItemId.HighQualityPalOil: 1,
        },
    ),
    ItemId.CommonShield: Recipe(
        product=ItemId.CommonShield,
        materials={
            ItemId.PaldiumFragment: 10,
            ItemId.Wood: 20,
            "stone": 20,
            ItemId.Fiber: 10,
        },
    ),
    ItemId.MegaShield: Recipe(
        product=ItemId.MegaShield,
        materials={
            ItemId.AncientCivilizationParts: 5,
            ItemId.PaldiumFragment: 30,
        },
    ),
    ItemId.GigaShield: Recipe(
        product=ItemId.GigaShield,
        materials={
            ItemId.AncientCivilizationParts: 15,
            ItemId.PaldiumFragment: 50,
        },
    ),
    ItemId.HyperShield: Recipe(
        product=ItemId.HyperShield,
        materials={
            ItemId.AncientCivilizationParts: 30,
            ItemId.PaldiumFragment: 100,
        },
    ),
    ItemId.UltraShield: Recipe(
        product=ItemId.UltraShield,
        materials={
            ItemId.AncientCivilizationParts: 50,
            ItemId.PaldiumFragment: 150,
            ItemId.Plasteel: 50,
            ItemId.AncientCivilizationCore: 30,
        },
    ),
    ItemId.AdvancedShield: Recipe(
        product=ItemId.AdvancedShield,
        materials={
            ItemId.AncientCivilizationParts: 80,
            ItemId.PaldiumFragment: 200,
            ItemId.Hexolite: 50,
            ItemId.AncientCivilizationCore: 30,
        },
    ),
    ItemId.NormalParachute: Recipe(
        product=ItemId.NormalParachute,
        materials={
            ItemId.Wood: 10,
            ItemId.Cloth: 2,
        },
    ),
    ItemId.MegaGlider: Recipe(
        product=ItemId.MegaGlider,
        materials={
            ItemId.Wood: 50,
            ItemId.Bone: 10,
            "cloth": 20,
        },
    ),
    ItemId.GigaGlider: Recipe(
        product=ItemId.GigaGlider,
        materials={
            ItemId.RefinedIngot: 20,
            ItemId.Wood: 100,
            ItemId.CarbonFiber: 20,
            "cloth2": 10,
        },
    ),
    ItemId.HyperGlider1: Recipe(
        product=ItemId.HyperGlider1,
        materials={
            ItemId.PalMetalIngot: 40,
            ItemId.Wood: 200,
            ItemId.CarbonFiber: 50,
            "cloth2": 20,
        },
    ),
    ItemId.HipLantern: Recipe(
        product=ItemId.HipLantern,
        materials={
            ItemId.Ingot: 20,
            ItemId.Wood: 10,
            ItemId.FlameOrgan: 10,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.EnhancedHipLantern: Recipe(
        product=ItemId.EnhancedHipLantern,
        materials={
            ItemId.RefinedIngot: 30,
            ItemId.Wood: 30,
            ItemId.FlameOrgan: 30,
            ItemId.AncientCivilizationParts: 20,
        },
    ),
    ItemId.SmallFeedBag: Recipe(
        product=ItemId.SmallFeedBag,
        materials={
            ItemId.Wood: 5,
            ItemId.Fiber: 10,
            ItemId.Leather: 3,
        },
    ),
    ItemId.AverageFeedBag: Recipe(
        product=ItemId.AverageFeedBag,
        materials={
            ItemId.Wood: 10,
            ItemId.Fiber: 30,
            ItemId.Leather: 10,
        },
    ),
    ItemId.LargeFeedBag: Recipe(
        product=ItemId.LargeFeedBag,
        materials={
            ItemId.Wood: 20,
            ItemId.Fiber: 50,
            ItemId.Leather: 20,
        },
    ),
    ItemId.HugeFeedBag: Recipe(
        product=ItemId.HugeFeedBag,
        materials={
            ItemId.Wood: 30,
            ItemId.Fiber: 90,
            ItemId.Leather: 35,
            ItemId.CarbonFiber: 10,
        },
    ),
    ItemId.GiantFeedBag: Recipe(
        product=ItemId.GiantFeedBag,
        materials={
            ItemId.Wood: 50,
            ItemId.Fiber: 200,
            ItemId.Leather: 50,
            ItemId.CarbonFiber: 20,
        },
    ),
    ItemId.SmallPouch: Recipe(
        product=ItemId.SmallPouch,
        materials={
            ItemId.PredatorCore: 1,
            ItemId.Fiber: 20,
            ItemId.Leather: 10,
        },
    ),
    ItemId.MediumPouch: Recipe(
        product=ItemId.MediumPouch,
        materials={
            ItemId.PredatorCore: 5,
            ItemId.Fiber: 50,
            ItemId.Leather: 20,
        },
    ),
    ItemId.LargePouch: Recipe(
        product=ItemId.LargePouch,
        materials={
            ItemId.PredatorCore: 10,
            ItemId.Fiber: 80,
            ItemId.Leather: 30,
            ItemId.CarbonFiber: 10,
        },
    ),
    ItemId.GiantPouch: Recipe(
        product=ItemId.GiantPouch,
        materials={
            ItemId.PredatorCore: 20,
            ItemId.Fiber: 120,
            ItemId.Leather: 40,
            ItemId.CarbonFiber: 20,
        },
    ),
    ItemId.Cloth: Recipe(
        product=ItemId.Cloth,
        materials={
            ItemId.Wool: 2,
        },
    ),
    ItemId.HighQualityCloth: Recipe(
        product=ItemId.HighQualityCloth,
        materials={
            ItemId.Wool: 10,
        },
    ),
    ItemId.Gunpowder1: Recipe(
        product=ItemId.Gunpowder1,
        materials={
            ItemId.Charcoal: 2,
            ItemId.Sulfur: 1,
        },
    ),
    ItemId.Charcoal: Recipe(
        product=ItemId.Charcoal,
        materials={
            ItemId.Wood: 2,
        },
    ),
    ItemId.Nail: Recipe(
        product=ItemId.Nail,
        materials={
            ItemId.Ingot: 1,
        },
    ),
    ItemId.CircuitBoard: Recipe(
        product=ItemId.CircuitBoard,
        materials={
            ItemId.PureQuartz: 4,
            ItemId.Polymer: 2,
        },
    ),
    ItemId.Polymer: Recipe(
        product=ItemId.Polymer,
        materials={
            ItemId.HighQualityPalOil: 2,
        },
    ),
    ItemId.Cement: Recipe(
        product=ItemId.Cement,
        materials={
            ItemId.Stone: 50,
            ItemId.Bone: 1,
            ItemId.PalFluids: 1,
        },
    ),
    ItemId.CarbonFiber: Recipe(
        product=ItemId.CarbonFiber,
        materials={
            ItemId.Charcoal: 5,
        },
    ),
    ItemId.HomewardThundercloud: Recipe(
        product=ItemId.HomewardThundercloud,
        materials={
            ItemId.DazziCloud: 1,
            ItemId.ElectricOrgan: 5,
            ItemId.AncientCivilizationParts: 2,
        },
    ),
    ItemId.RepairKit: Recipe(
        product=ItemId.RepairKit,
        materials={
            ItemId.Fiber: 5,
            ItemId.Stone: 5,
        },
    ),
    ItemId.Ingot: Recipe(
        product=ItemId.Ingot,
        materials={
            ItemId.Ore: 2,
        },
    ),
    ItemId.RefinedIngot: Recipe(
        product=ItemId.RefinedIngot,
        materials={
            ItemId.Ore: 2,
            ItemId.Coal: 2,
        },
    ),
    ItemId.PalMetalIngot: Recipe(
        product=ItemId.PalMetalIngot,
        materials={
            ItemId.Ore: 4,
            ItemId.PaldiumFragment: 2,
        },
    ),
    ItemId.Plasteel: Recipe(
        product=ItemId.Plasteel,
        materials={
            ItemId.CrudeOil: 5,
            ItemId.PaldiumFragment: 5,
            ItemId.Ore: 10,
        },
    ),
    ItemId.Hexolite: Recipe(
        product=ItemId.Hexolite,
        materials={
            ItemId.Chromite: 5,
            ItemId.HexoliteQuartz: 12,
            ItemId.Ore: 20,
        },
    ),
    ItemId.CoralumIngot: Recipe(
        product=ItemId.CoralumIngot,
        materials={
            ItemId.CoralumOre: 5,
            ItemId.Ore: 30,
            ItemId.Coal: 20,
        },
    ),
    ItemId.LowQualityRecoveryMeds: Recipe(
        product=ItemId.LowQualityRecoveryMeds,
        materials={
            ItemId.CavernMushroom: 3,
            ItemId.RedBerries: 5,
            ItemId.PalFluids: 2,
        },
    ),
    ItemId.RecoveryMeds: Recipe(
        product=ItemId.RecoveryMeds,
        materials={
            ItemId.CavernMushroom: 5,
            ItemId.RedBerries: 5,
            ItemId.PalFluids: 5,
            ItemId.CottonCandy: 3,
        },
    ),
    ItemId.HighQualityRecoveryMeds: Recipe(
        product=ItemId.HighQualityRecoveryMeds,
        materials={
            ItemId.CavernMushroom: 10,
            ItemId.RedBerries: 20,
            ItemId.HighQualityPalOil: 5,
            ItemId.CottonCandy: 5,
            ItemId.Sulfur: 5,
        },
    ),
    ItemId.AdvancedRecoveryMeds: Recipe(
        product=ItemId.AdvancedRecoveryMeds,
        materials={
            ItemId.CavernMushroom: 15,
            ItemId.RedBerries: 30,
            ItemId.HighQualityPalOil: 10,
            ItemId.CottonCandy: 7,
            ItemId.Sulfur: 10,
        },
    ),
    ItemId.RevivalPotion: Recipe(
        product=ItemId.RevivalPotion,
        materials={
            ItemId.CavernMushroom: 30,
            ItemId.RedBerries: 50,
            ItemId.HighQualityPalOil: 20,
            ItemId.CottonCandy: 10,
            ItemId.Sulfur: 20,
        },
    ),
    ItemId.LowGradeMedicalSupplies: Recipe(
        product=ItemId.LowGradeMedicalSupplies,
        materials={
            ItemId.RedBerries: 5,
            ItemId.Horn: 2,
        },
    ),
    ItemId.MedicalSupplies: Recipe(
        product=ItemId.MedicalSupplies,
        materials={
            ItemId.Ingot: 3,
            ItemId.Horn: 3,
            ItemId.Bone: 1,
        },
    ),
    ItemId.HighGradeMedicalSupplies: Recipe(
        product=ItemId.HighGradeMedicalSupplies,
        materials={
            ItemId.Ingot: 5,
            ItemId.Horn: 5,
            ItemId.Bone: 2,
        },
    ),
    ItemId.MindControlMeds: Recipe(
        product=ItemId.MindControlMeds,
        materials={
            ItemId.RefinedIngot: 10,
            ItemId.Horn: 10,
            ItemId.Bone: 5,
            ItemId.PalFluids: 3,
        },
    ),
    ItemId.SuspiciousJuice: Recipe(
        product=ItemId.SuspiciousJuice,
        materials={
            ItemId.BeautifulFlower: 3,
            ItemId.Horn: 3,
            ItemId.Bone: 1,
            ItemId.PalFluids: 1,
        },
    ),
    ItemId.StrangeJuice: Recipe(
        product=ItemId.StrangeJuice,
        materials={
            ItemId.BeautifulFlower: 5,
            ItemId.Horn: 5,
            ItemId.Bone: 2,
            ItemId.PalFluids: 2,
        },
    ),
    ItemId.MysteriousMushroomJuice: Recipe(
        product=ItemId.MysteriousMushroomJuice,
        materials={
            ItemId.MysteriousMushroom: 20,
            ItemId.BeautifulFlower: 10,
            ItemId.Horn: 10,
            ItemId.Bone: 5,
            ItemId.PalFluids: 5,
        },
    ),
    ItemId.MemoryWipingMedicine: Recipe(
        product=ItemId.MemoryWipingMedicine,
        materials={
            ItemId.BeautifulFlower: 99,
            ItemId.Horn: 50,
            ItemId.Bone: 50,
            ItemId.PalFluids: 50,
        },
    ),
    ItemId.Fiber: Recipe(
        product=ItemId.Fiber,
        materials={
            ItemId.Wood: 1,
        },
    ),
    ItemId.PaldiumFragment: Recipe(
        product=ItemId.PaldiumFragment,
        materials={
            ItemId.ExoticSphere: 1,
        },
    ),
    ItemId.Flour: Recipe(
        product=ItemId.Flour,
        materials={
            ItemId.Wheat: 3,
        },
    ),
    ItemId.BakedBerries: Recipe(
        product=ItemId.BakedBerries,
        materials={
            ItemId.RedBerries: 1,
        },
    ),
    ItemId.BakedMushroom: Recipe(
        product=ItemId.BakedMushroom,
        materials={
            ItemId.Mushroom: 1,
        },
    ),
    ItemId.Bread: Recipe(
        product=ItemId.Bread,
        materials={
            ItemId.Flour: 1,
        },
    ),
    ItemId.FriedEgg: Recipe(
        product=ItemId.FriedEgg,
        materials={
            ItemId.Egg: 1,
        },
    ),
    "Hotmilk": Recipe(
        product="Hotmilk",
        materials={
            ItemId.Milk: 1,
        },
    ),
    ItemId.JamFilledBun: Recipe(
        product=ItemId.JamFilledBun,
        materials={
            ItemId.Flour: 1,
            ItemId.RedBerries: 2,
        },
    ),
    ItemId.Pancake: Recipe(
        product=ItemId.Pancake,
        materials={
            ItemId.Flour: 1,
            ItemId.Milk: 1,
        },
    ),
    ItemId.Salad: Recipe(
        product=ItemId.Salad,
        materials={
            ItemId.Lettuce: 2,
            ItemId.Tomato: 2,
        },
    ),
    ItemId.Omelet: Recipe(
        product=ItemId.Omelet,
        materials={
            ItemId.Tomato: 1,
            ItemId.Egg: 2,
        },
    ),
    ItemId.MarinatedMushrooms: Recipe(
        product=ItemId.MarinatedMushrooms,
        materials={
            ItemId.Mushroom: 1,
            ItemId.RedBerries: 2,
        },
    ),
    ItemId.MushroomSoup: Recipe(
        product=ItemId.MushroomSoup,
        materials={
            ItemId.Mushroom: 1,
            ItemId.Milk: 2,
        },
    ),
    ItemId.Pizza: Recipe(
        product=ItemId.Pizza,
        materials={
            ItemId.Flour: 1,
            ItemId.RedBerries: 2,
            ItemId.Tomato: 2,
            ItemId.Milk: 2,
        },
    ),
    ItemId.Carbonara: Recipe(
        product=ItemId.Carbonara,
        materials={
            ItemId.Flour: 1,
            ItemId.Egg: 2,
            ItemId.Milk: 2,
        },
    ),
    ItemId.Cake: Recipe(
        product=ItemId.Cake,
        materials={
            ItemId.Flour: 5,
            ItemId.RedBerries: 8,
            ItemId.Milk: 7,
            ItemId.Egg: 8,
            ItemId.Honey: 2,
        },
    ),
    ItemId.JolthogSGloves: Recipe(
        product=ItemId.JolthogSGloves,
        materials={
            ItemId.Cloth: 5,
            ItemId.ElectricOrgan: 5,
            ItemId.PaldiumFragment: 5,
        },
    ),
    ItemId.JolthogCrystSGloves: Recipe(
        product=ItemId.JolthogCrystSGloves,
        materials={
            ItemId.Cloth: 6,
            ItemId.IceOrgan: 6,
            ItemId.PaldiumFragment: 6,
        },
    ),
    ItemId.FoxparksHarness: Recipe(
        product=ItemId.FoxparksHarness,
        materials={
            ItemId.Leather: 3,
            ItemId.FlameOrgan: 5,
            ItemId.PaldiumFragment: 5,
        },
    ),
    ItemId.FoxparksCrystSHarness: Recipe(
        product=ItemId.FoxparksCrystSHarness,
        materials={
            ItemId.Leather: 10,
            ItemId.IceOrgan: 10,
            ItemId.PaldiumFragment: 20,
        },
    ),
    ItemId.MelpacaSaddle: Recipe(
        product=ItemId.MelpacaSaddle,
        materials={
            ItemId.Leather: 3,
            ItemId.Wool: 5,
            ItemId.PaldiumFragment: 5,
        },
    ),
    ItemId.SweepaSaddle: Recipe(
        product=ItemId.SweepaSaddle,
        materials={
            ItemId.Leather: 3,
            ItemId.Cloth: 8,
            ItemId.PaldiumFragment: 10,
        },
    ),
    ItemId.RushoarSaddle: Recipe(
        product=ItemId.RushoarSaddle,
        materials={
            ItemId.Leather: 3,
            ItemId.Stone: 10,
            ItemId.PaldiumFragment: 5,
        },
    ),
    ItemId.CelaraySGloves: Recipe(
        product=ItemId.CelaraySGloves,
        materials={
            ItemId.Cloth: 5,
            ItemId.PalFluids: 3,
            ItemId.PaldiumFragment: 5,
        },
    ),
    ItemId.CelarayLuxSGloves: Recipe(
        product=ItemId.CelarayLuxSGloves,
        materials={
            ItemId.Cloth: 10,
            ItemId.ElectricOrgan: 5,
            ItemId.PaldiumFragment: 6,
        },
    ),
    ItemId.LifmunkSSubmachineGun: Recipe(
        product=ItemId.LifmunkSSubmachineGun,
        materials={
            ItemId.Ingot: 5,
            ItemId.Stone: 10,
            ItemId.Wood: 20,
            ItemId.PaldiumFragment: 10,
        },
    ),
    ItemId.DirehowlSSaddledHarness: Recipe(
        product=ItemId.DirehowlSSaddledHarness,
        materials={
            ItemId.Leather: 10,
            "wood": 20,
            ItemId.Fiber: 15,
            ItemId.PaldiumFragment: 10,
        },
    ),
    ItemId.TanzeeSAssaultRifle: Recipe(
        product=ItemId.TanzeeSAssaultRifle,
        materials={
            ItemId.Ingot: 5,
            ItemId.Stone: 15,
            ItemId.Wood: 15,
            ItemId.PaldiumFragment: 10,
        },
    ),
    ItemId.SurfentSaddle: Recipe(
        product=ItemId.SurfentSaddle,
        materials={
            ItemId.Leather: 5,
            ItemId.PalFluids: 5,
            ItemId.PaldiumFragment: 10,
        },
    ),
    ItemId.SurfentTerraSaddle: Recipe(
        product=ItemId.SurfentTerraSaddle,
        materials={
            ItemId.Leather: 6,
            ItemId.Ingot: 6,
            ItemId.PaldiumFragment: 12,
        },
    ),
    ItemId.EikthyrdeerSaddle: Recipe(
        product=ItemId.EikthyrdeerSaddle,
        materials={
            ItemId.Leather: 5,
            ItemId.Fiber: 20,
            ItemId.Ingot: 10,
            ItemId.Horn: 3,
            ItemId.PaldiumFragment: 15,
        },
    ),
    ItemId.EikthyrdeerTerraSaddle: Recipe(
        product=ItemId.EikthyrdeerTerraSaddle,
        materials={
            ItemId.Leather: 6,
            ItemId.Fiber: 24,
            ItemId.Ingot: 12,
            ItemId.Horn: 3,
            ItemId.PaldiumFragment: 18,
        },
    ),
    ItemId.GrintaleSaddle: Recipe(
        product=ItemId.GrintaleSaddle,
        materials={
            ItemId.Leather: 10,
            ItemId.PaldiumFragment: 10,
        },
    ),
    ItemId.HerbilSHarness: Recipe(
        product=ItemId.HerbilSHarness,
        materials={
            ItemId.Leather: 20,
            ItemId.Fiber: 40,
            ItemId.Ingot: 20,
            ItemId.PaldiumFragment: 25,
        },
    ),
    ItemId.PolapupSaddle: Recipe(
        product=ItemId.PolapupSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.Fiber: 60,
            ItemId.RefinedIngot: 30,
            ItemId.IceOrgan: 6,
            ItemId.PaldiumFragment: 30,
        },
    ),
    ItemId.UnivoltSaddle: Recipe(
        product=ItemId.UnivoltSaddle,
        materials={
            ItemId.Leather: 10,
            ItemId.Ingot: 5,
            ItemId.ElectricOrgan: 10,
            ItemId.PaldiumFragment: 15,
        },
    ),
    ItemId.KillamariSGloves: Recipe(
        product=ItemId.KillamariSGloves,
        materials={
            ItemId.Cloth: 5,
            ItemId.VenomGland: 5,
            ItemId.PaldiumFragment: 10,
        },
    ),
    ItemId.KillamariPrimoSGloves: Recipe(
        product=ItemId.KillamariPrimoSGloves,
        materials={
            ItemId.Cloth: 6,
            ItemId.PalFluids: 4,
            ItemId.PaldiumFragment: 12,
        },
    ),
    ItemId.TocotocoSGloves: Recipe(
        product=ItemId.TocotocoSGloves,
        materials={
            ItemId.Cloth: 10,
            ItemId.Leather: 10,
            ItemId.Fiber: 15,
            ItemId.FlameOrgan: 10,
            ItemId.PaldiumFragment: 15,
        },
    ),
    ItemId.NitewingSaddle: Recipe(
        product=ItemId.NitewingSaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.Cloth: 10,
            ItemId.Ingot: 15,
            ItemId.Fiber: 20,
            ItemId.PaldiumFragment: 20,
        },
    ),
    ItemId.ArsoxSaddle: Recipe(
        product=ItemId.ArsoxSaddle,
        materials={
            ItemId.Leather: 15,
            ItemId.Fiber: 25,
            ItemId.FlameOrgan: 10,
            ItemId.PaldiumFragment: 15,
        },
    ),
    ItemId.FlopieSNecklace: Recipe(
        product=ItemId.FlopieSNecklace,
        materials={
            ItemId.Leather: 10,
            ItemId.Fiber: 20,
            ItemId.Ingot: 5,
            ItemId.PaldiumFragment: 15,
        },
    ),
    ItemId.DigtoiseSHeadband: Recipe(
        product=ItemId.DigtoiseSHeadband,
        materials={
            ItemId.Leather: 20,
            ItemId.Fiber: 30,
            ItemId.Ingot: 10,
            ItemId.Stone: 50,
            ItemId.PaldiumFragment: 20,
        },
    ),
    ItemId.PengulletRocketLauncher: Recipe(
        product=ItemId.PengulletRocketLauncher,
        materials={
            ItemId.Ingot: 20,
            ItemId.Stone: 20,
            ItemId.Wood: 30,
            ItemId.PaldiumFragment: 20,
        },
    ),
    ItemId.PengulletLuxSRocketLauncher: Recipe(
        product=ItemId.PengulletLuxSRocketLauncher,
        materials={
            ItemId.Ingot: 24,
            ItemId.Stone: 24,
            ItemId.Wood: 36,
            ItemId.ElectricOrgan: 20,
            ItemId.PaldiumFragment: 24,
        },
    ),
    ItemId.DinossomSaddle: Recipe(
        product=ItemId.DinossomSaddle,
        materials={
            ItemId.Leather: 15,
            ItemId.Fiber: 30,
            ItemId.Ingot: 10,
            ItemId.PaldiumFragment: 20,
        },
    ),
    ItemId.DinossomLuxSaddle: Recipe(
        product=ItemId.DinossomLuxSaddle,
        materials={
            ItemId.Leather: 18,
            ItemId.Fiber: 36,
            ItemId.Ingot: 12,
            ItemId.PaldiumFragment: 24,
        },
    ),
    ItemId.DaedreamSNecklace: Recipe(
        product=ItemId.DaedreamSNecklace,
        materials={
            ItemId.Leather: 5,
            ItemId.Fiber: 10,
            ItemId.PaldiumFragment: 10,
        },
    ),
    ItemId.BroncherrySaddle: Recipe(
        product=ItemId.BroncherrySaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.Fiber: 30,
            ItemId.Ingot: 15,
            ItemId.PaldiumFragment: 20,
        },
    ),
    ItemId.BroncherryAquaSaddle: Recipe(
        product=ItemId.BroncherryAquaSaddle,
        materials={
            ItemId.Leather: 24,
            ItemId.Fiber: 36,
            ItemId.Ingot: 18,
            ItemId.PaldiumFragment: 24,
        },
    ),
    ItemId.VanwyrmSaddle: Recipe(
        product=ItemId.VanwyrmSaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.FlameOrgan: 10,
            ItemId.Ingot: 15,
            ItemId.Fiber: 30,
            ItemId.PaldiumFragment: 20,
        },
    ),
    ItemId.VanwyrmCrystSaddle: Recipe(
        product=ItemId.VanwyrmCrystSaddle,
        materials={
            ItemId.Leather: 24,
            ItemId.IceOrgan: 12,
            ItemId.Ingot: 18,
            ItemId.Fiber: 36,
            ItemId.PaldiumFragment: 24,
        },
    ),
    ItemId.ChilletSaddle: Recipe(
        product=ItemId.ChilletSaddle,
        materials={
            ItemId.Leather: 10,
            ItemId.Fiber: 20,
            ItemId.Cloth: 5,
            ItemId.PaldiumFragment: 20,
        },
    ),
    ItemId.ChilletIgnisSaddle: Recipe(
        product=ItemId.ChilletIgnisSaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.Fiber: 30,
            ItemId.Cloth: 10,
            ItemId.FlameOrgan: 10,
            ItemId.PaldiumFragment: 30,
        },
    ),
    ItemId.HangyuSGloves: Recipe(
        product=ItemId.HangyuSGloves,
        materials={
            ItemId.Cloth: 5,
            ItemId.Leather: 3,
            ItemId.Fiber: 10,
            ItemId.Ingot: 3,
            ItemId.PaldiumFragment: 10,
        },
    ),
    ItemId.HangyuCrystSGlove: Recipe(
        product=ItemId.HangyuCrystSGlove,
        materials={
            ItemId.Cloth: 6,
            ItemId.Leather: 3,
            ItemId.Fiber: 12,
            ItemId.Ingot: 3,
            ItemId.PaldiumFragment: 12,
        },
    ),
    ItemId.KingpacaSaddle: Recipe(
        product=ItemId.KingpacaSaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.Fiber: 20,
            ItemId.Ingot: 15,
            ItemId.Wool: 30,
            ItemId.PaldiumFragment: 20,
        },
    ),
    ItemId.KingpacaCrystSaddle: Recipe(
        product=ItemId.KingpacaCrystSaddle,
        materials={
            ItemId.Leather: 24,
            ItemId.Fiber: 24,
            ItemId.Ingot: 18,
            ItemId.Wool: 36,
            ItemId.PaldiumFragment: 24,
        },
    ),
    ItemId.ElphidranSaddle: Recipe(
        product=ItemId.ElphidranSaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.Fiber: 20,
            ItemId.Ingot: 15,
            ItemId.PaldiumFragment: 20,
        },
    ),
    ItemId.ElphidranAquaSaddle: Recipe(
        product=ItemId.ElphidranAquaSaddle,
        materials={
            ItemId.Leather: 24,
            ItemId.Fiber: 24,
            ItemId.Ingot: 18,
            ItemId.PaldiumFragment: 24,
        },
    ),
    ItemId.DazziSNecklace: Recipe(
        product=ItemId.DazziSNecklace,
        materials={
            ItemId.Leather: 15,
            ItemId.Fiber: 15,
            ItemId.Ingot: 10,
            ItemId.PaldiumFragment: 20,
        },
    ),
    ItemId.DazziNoctSNecklace: Recipe(
        product=ItemId.DazziNoctSNecklace,
        materials={
            ItemId.Leather: 10,
            ItemId.Fiber: 30,
            ItemId.DarkFragment: 10,
            ItemId.PaldiumFragment: 40,
        },
    ),
    ItemId.DazemuSaddle: Recipe(
        product=ItemId.DazemuSaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.Fiber: 30,
            ItemId.Ingot: 15,
            ItemId.PaldiumFragment: 20,
        },
    ),
    ItemId.GaleclawSGloves: Recipe(
        product=ItemId.GaleclawSGloves,
        materials={
            ItemId.Cloth: 20,
            ItemId.Leather: 20,
            ItemId.Fiber: 30,
            ItemId.PaldiumFragment: 30,
        },
    ),
    ItemId.MaraithSaddle: Recipe(
        product=ItemId.MaraithSaddle,
        materials={
            ItemId.Leather: 15,
            ItemId.Fiber: 25,
            ItemId.Ingot: 10,
            ItemId.PaldiumFragment: 20,
        },
    ),
    ItemId.GhanglerSaddle: Recipe(
        product=ItemId.GhanglerSaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.Cloth: 10,
            ItemId.Ingot: 20,
            ItemId.PalFluids: 20,
            ItemId.PaldiumFragment: 25,
        },
    ),
    ItemId.GhanglerIgnisSaddle: Recipe(
        product=ItemId.GhanglerIgnisSaddle,
        materials={
            ItemId.Leather: 24,
            ItemId.Cloth: 12,
            ItemId.Ingot: 24,
            ItemId.FlameOrgan: 24,
            ItemId.PaldiumFragment: 30,
        },
    ),
    ItemId.BralohaSaddle: Recipe(
        product=ItemId.BralohaSaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.Cloth: 20,
            ItemId.Fiber: 30,
            ItemId.RefinedIngot: 10,
            ItemId.PaldiumFragment: 30,
        },
    ),
    ItemId.PalumbaSaddle: Recipe(
        product=ItemId.PalumbaSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.Cloth: 30,
            ItemId.Ingot: 30,
            ItemId.PaldiumFragment: 40,
        },
    ),
    ItemId.MossandaSGrenadeLauncher: Recipe(
        product=ItemId.MossandaSGrenadeLauncher,
        materials={
            ItemId.Ingot: 50,
            ItemId.HighQualityPalOil: 20,
            ItemId.PaldiumFragment: 40,
        },
    ),
    ItemId.MossandaLuxSGrenadeLauncher: Recipe(
        product=ItemId.MossandaLuxSGrenadeLauncher,
        materials={
            ItemId.Ingot: 60,
            ItemId.HighQualityPalOil: 24,
            ItemId.PaldiumFragment: 48,
        },
    ),
    ItemId.TarantrissSaddle: Recipe(
        product=ItemId.TarantrissSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.Fiber: 50,
            ItemId.VenomGland: 30,
            ItemId.PaldiumFragment: 40,
        },
    ),
    ItemId.ReptyroSaddle: Recipe(
        product=ItemId.ReptyroSaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.Ingot: 20,
            ItemId.FlameOrgan: 20,
            ItemId.PaldiumFragment: 20,
        },
    ),
    ItemId.ReptyroCrystSaddle: Recipe(
        product=ItemId.ReptyroCrystSaddle,
        materials={
            ItemId.Leather: 24,
            ItemId.Ingot: 24,
            ItemId.IceOrgan: 24,
            ItemId.PaldiumFragment: 24,
        },
    ),
    ItemId.PyrinSaddle: Recipe(
        product=ItemId.PyrinSaddle,
        materials={
            ItemId.Leather: 25,
            ItemId.Fiber: 30,
            ItemId.FlameOrgan: 20,
            ItemId.Ingot: 15,
            ItemId.PaldiumFragment: 25,
        },
    ),
    ItemId.PyrinNoctSaddle: Recipe(
        product=ItemId.PyrinNoctSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.Fiber: 36,
            ItemId.FlameOrgan: 24,
            ItemId.Ingot: 18,
            ItemId.PaldiumFragment: 30,
        },
    ),
    ItemId.MammorestSaddle: Recipe(
        product=ItemId.MammorestSaddle,
        materials={
            ItemId.Leather: 50,
            ItemId.Fiber: 70,
            ItemId.HighQualityPalOil: 10,
            ItemId.Wood: 100,
            ItemId.PaldiumFragment: 60,
        },
    ),
    ItemId.MammorestCrystSaddle: Recipe(
        product=ItemId.MammorestCrystSaddle,
        materials={
            ItemId.Leather: 60,
            ItemId.Fiber: 84,
            ItemId.HighQualityPalOil: 12,
            ItemId.Wood: 120,
            ItemId.PaldiumFragment: 72,
        },
    ),
    ItemId.AzurobeSaddle: Recipe(
        product=ItemId.AzurobeSaddle,
        materials={
            ItemId.Leather: 25,
            ItemId.Fiber: 30,
            ItemId.Cloth: 10,
            ItemId.PalFluids: 10,
            ItemId.PaldiumFragment: 25,
        },
    ),
    ItemId.AzurobeCrystSaddle: Recipe(
        product=ItemId.AzurobeCrystSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.Fiber: 36,
            ItemId.Cloth: 12,
            ItemId.IceOrgan: 12,
            ItemId.PaldiumFragment: 30,
        },
    ),
    ItemId.JormuntideSaddle: Recipe(
        product=ItemId.JormuntideSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.Fiber: 50,
            ItemId.Ingot: 50,
            ItemId.PalFluids: 20,
            ItemId.PaldiumFragment: 40,
        },
    ),
    ItemId.JormuntideIgnisSaddle: Recipe(
        product=ItemId.JormuntideIgnisSaddle,
        materials={
            ItemId.Leather: 36,
            ItemId.Fiber: 60,
            ItemId.Ingot: 60,
            ItemId.FlameOrgan: 24,
            ItemId.PaldiumFragment: 48,
        },
    ),
    ItemId.KitsunSaddle: Recipe(
        product=ItemId.KitsunSaddle,
        materials={
            ItemId.Leather: 25,
            ItemId.Cloth: 10,
            ItemId.FlameOrgan: 15,
            ItemId.PaldiumFragment: 20,
        },
    ),
    ItemId.KitsunNoctSaddle: Recipe(
        product=ItemId.KitsunNoctSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.HighQualityCloth: 10,
            ItemId.FlameOrgan: 30,
            ItemId.PaldiumFragment: 40,
        },
    ),
    ItemId.RayhoundSaddle: Recipe(
        product=ItemId.RayhoundSaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.Fiber: 40,
            ItemId.Ingot: 20,
            ItemId.ElectricOrgan: 15,
            ItemId.PaldiumFragment: 25,
        },
    ),
    ItemId.BlazehowlSaddle: Recipe(
        product=ItemId.BlazehowlSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.Ingot: 30,
            ItemId.Fiber: 50,
            ItemId.FlameOrgan: 20,
            ItemId.PaldiumFragment: 30,
        },
    ),
    ItemId.BlazehowlNoctSaddle: Recipe(
        product=ItemId.BlazehowlNoctSaddle,
        materials={
            ItemId.Leather: 36,
            ItemId.Ingot: 36,
            ItemId.Fiber: 60,
            ItemId.FlameOrgan: 24,
            ItemId.PaldiumFragment: 36,
        },
    ),
    ItemId.ReindrixSaddle: Recipe(
        product=ItemId.ReindrixSaddle,
        materials={
            ItemId.Leather: 25,
            ItemId.IceOrgan: 10,
            ItemId.Ingot: 20,
            ItemId.Horn: 20,
            ItemId.PaldiumFragment: 25,
        },
    ),
    ItemId.BeakonSaddle: Recipe(
        product=ItemId.BeakonSaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.Cloth: 10,
            ItemId.Ingot: 20,
            ItemId.ElectricOrgan: 20,
            ItemId.PaldiumFragment: 25,
        },
    ),
    ItemId.RagnahawkSaddle: Recipe(
        product=ItemId.RagnahawkSaddle,
        materials={
            ItemId.Leather: 25,
            ItemId.Cloth: 15,
            ItemId.Ingot: 20,
            ItemId.FlameOrgan: 20,
            ItemId.PaldiumFragment: 25,
        },
    ),
    ItemId.FalerisSaddle: Recipe(
        product=ItemId.FalerisSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.Cloth: 10,
            ItemId.RefinedIngot: 30,
            ItemId.FlameOrgan: 25,
            ItemId.PaldiumFragment: 30,
        },
    ),
    ItemId.FalerisAquaSaddle: Recipe(
        product=ItemId.FalerisAquaSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.HighQualityCloth: 20,
            ItemId.Plasteel: 5,
            ItemId.PalFluids: 30,
            ItemId.PaldiumFragment: 75,
        },
    ),
    ItemId.QuivernSaddle: Recipe(
        product=ItemId.QuivernSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.Ingot: 30,
            ItemId.Cloth: 10,
            ItemId.PaldiumFragment: 30,
        },
    ),
    ItemId.QuivernBotanSaddle: Recipe(
        product=ItemId.QuivernBotanSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.Ingot: 30,
            ItemId.Cloth: 20,
            ItemId.PaldiumFragment: 40,
        },
    ),
    ItemId.HelzephyrSaddle: Recipe(
        product=ItemId.HelzephyrSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.Cloth: 10,
            ItemId.RefinedIngot: 30,
            ItemId.ElectricOrgan: 20,
            ItemId.PaldiumFragment: 30,
        },
    ),
    ItemId.HelzephyrLuxSaddle: Recipe(
        product=ItemId.HelzephyrLuxSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.Plasteel: 10,
            ItemId.ElectricOrgan: 30,
            ItemId.PaldiumFragment: 60,
        },
    ),
    ItemId.FenglopeSaddle: Recipe(
        product=ItemId.FenglopeSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.Fiber: 30,
            ItemId.Ingot: 20,
            ItemId.Cloth: 20,
            ItemId.PaldiumFragment: 40,
        },
    ),
    ItemId.FenglopeLuxSaddle: Recipe(
        product=ItemId.FenglopeLuxSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.Fiber: 30,
            ItemId.ElectricOrgan: 20,
            ItemId.HighQualityCloth: 10,
            ItemId.PaldiumFragment: 45,
        },
    ),
    ItemId.SuzakuSaddle: Recipe(
        product=ItemId.SuzakuSaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.RefinedIngot: 25,
            ItemId.FlameOrgan: 20,
            ItemId.PaldiumFragment: 40,
        },
    ),
    ItemId.SuzakuAquaSaddle: Recipe(
        product=ItemId.SuzakuAquaSaddle,
        materials={
            ItemId.Leather: 24,
            ItemId.RefinedIngot: 30,
            ItemId.PalFluids: 24,
            ItemId.PaldiumFragment: 48,
        },
    ),
    ItemId.YakumoSaddle: Recipe(
        product=ItemId.YakumoSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.Fiber: 50,
            ItemId.Ingot: 30,
            ItemId.PaldiumFragment: 40,
        },
    ),
    ItemId.BlazamutSaddle: Recipe(
        product=ItemId.BlazamutSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.RefinedIngot: 30,
            ItemId.Ingot: 20,
            ItemId.PaldiumFragment: 40,
        },
    ),
    ItemId.BlazamutRyuSaddle: Recipe(
        product=ItemId.BlazamutRyuSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.Plasteel: 30,
            ItemId.FlameOrgan: 50,
            ItemId.PaldiumFragment: 60,
        },
    ),
    ItemId.WumpoSaddle: Recipe(
        product=ItemId.WumpoSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.IceOrgan: 20,
            ItemId.Fiber: 50,
            ItemId.RefinedIngot: 10,
            ItemId.PaldiumFragment: 40,
        },
    ),
    ItemId.WumpoBotanSaddle: Recipe(
        product=ItemId.WumpoBotanSaddle,
        materials={
            ItemId.Leather: 36,
            ItemId.BeautifulFlower: 24,
            ItemId.Fiber: 60,
            ItemId.RefinedIngot: 12,
            ItemId.PaldiumFragment: 48,
        },
    ),
    ItemId.WhalaskaSaddle: Recipe(
        product=ItemId.WhalaskaSaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.Cloth: 10,
            ItemId.Ingot: 20,
            ItemId.IceOrgan: 20,
            ItemId.PaldiumFragment: 25,
        },
    ),
    ItemId.WhalaskaIgnisSaddle: Recipe(
        product=ItemId.WhalaskaIgnisSaddle,
        materials={
            ItemId.Leather: 24,
            ItemId.Cloth: 12,
            ItemId.Ingot: 24,
            ItemId.FlameOrgan: 24,
            ItemId.PaldiumFragment: 30,
        },
    ),
    ItemId.GrizzboltSMinigun: Recipe(
        product=ItemId.GrizzboltSMinigun,
        materials={
            ItemId.RefinedIngot: 50,
            ItemId.Polymer: 20,
            ItemId.HighQualityPalOil: 10,
            ItemId.PaldiumFragment: 75,
        },
    ),
    ItemId.ShadowbeakSaddle: Recipe(
        product=ItemId.ShadowbeakSaddle,
        materials={
            ItemId.Leather: 50,
            ItemId.RefinedIngot: 40,
            ItemId.VenomGland: 25,
            ItemId.PaldiumFragment: 45,
        },
    ),
    ItemId.AstegonSaddle: Recipe(
        product=ItemId.AstegonSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.RefinedIngot: 50,
            ItemId.Ingot: 50,
            ItemId.PaldiumFragment: 55,
        },
    ),
    ItemId.RelaxaurusMissileLauncher: Recipe(
        product=ItemId.RelaxaurusMissileLauncher,
        materials={
            ItemId.RefinedIngot: 100,
            ItemId.Polymer: 35,
            ItemId.Ingot: 100,
            ItemId.PaldiumFragment: 85,
        },
    ),
    ItemId.RelaxaurusLuxSMissileLauncher: Recipe(
        product=ItemId.RelaxaurusLuxSMissileLauncher,
        materials={
            ItemId.RefinedIngot: 120,
            ItemId.Polymer: 42,
            ItemId.Ingot: 120,
            ItemId.PaldiumFragment: 102,
        },
    ),
    ItemId.ShroomerSaddle: Recipe(
        product=ItemId.ShroomerSaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.Mushroom: 20,
            ItemId.Fiber: 30,
            ItemId.RefinedIngot: 10,
            ItemId.PaldiumFragment: 30,
        },
    ),
    ItemId.ShroomerNoctSaddle: Recipe(
        product=ItemId.ShroomerNoctSaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.MysteriousMushroom: 20,
            ItemId.Fiber: 30,
            ItemId.RefinedIngot: 10,
            ItemId.PaldiumFragment: 30,
        },
    ),
    ItemId.FrostallionSaddle: Recipe(
        product=ItemId.FrostallionSaddle,
        materials={
            ItemId.Leather: 100,
            ItemId.RefinedIngot: 200,
            ItemId.IceOrgan: 50,
            ItemId.PaldiumFragment: 75,
        },
    ),
    ItemId.FrostallionNoctSaddle: Recipe(
        product=ItemId.FrostallionNoctSaddle,
        materials={
            ItemId.Leather: 120,
            ItemId.RefinedIngot: 240,
            ItemId.VenomGland: 60,
            ItemId.PaldiumFragment: 90,
        },
    ),
    ItemId.PaladiusSaddle: Recipe(
        product=ItemId.PaladiusSaddle,
        materials={
            ItemId.Leather: 100,
            ItemId.RefinedIngot: 200,
            ItemId.Ingot: 300,
            ItemId.PaldiumFragment: 85,
        },
    ),
    ItemId.NecromusSaddle: Recipe(
        product=ItemId.NecromusSaddle,
        materials={
            ItemId.Leather: 100,
            ItemId.RefinedIngot: 200,
            ItemId.Ingot: 300,
            ItemId.PaldiumFragment: 85,
        },
    ),
    ItemId.JetragonSMissileLauncher: Recipe(
        product=ItemId.JetragonSMissileLauncher,
        materials={
            ItemId.Leather: 100,
            ItemId.RefinedIngot: 200,
            ItemId.CircuitBoard: 50,
            ItemId.PaldiumFragment: 140,
        },
    ),
    ItemId.XenogardSaddle: Recipe(
        product=ItemId.XenogardSaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.MeteoriteFragment: 30,
            ItemId.PaldiumFragment: 50,
        },
    ),
    ItemId.SelyneSaddle: Recipe(
        product=ItemId.SelyneSaddle,
        materials={
            ItemId.Leather: 20,
            ItemId.Plasteel: 30,
            ItemId.MeteoriteFragment: 10,
            ItemId.PaldiumFragment: 60,
        },
    ),
    ItemId.SmokieSHarness: Recipe(
        product=ItemId.SmokieSHarness,
        materials={
            ItemId.Leather: 20,
            ItemId.Fiber: 50,
            ItemId.DarkFragment: 10,
            ItemId.PaldiumFragment: 40,
        },
    ),
    ItemId.StarryonSaddle: Recipe(
        product=ItemId.StarryonSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.HighQualityCloth: 15,
            ItemId.DarkFragment: 20,
            ItemId.PaldiumFragment: 60,
        },
    ),
    ItemId.AzurmaneSaddle: Recipe(
        product=ItemId.AzurmaneSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.HighQualityCloth: 15,
            ItemId.ElectricOrgan: 50,
            ItemId.PaldiumFragment: 60,
        },
    ),
    ItemId.GildaneSaddle: Recipe(
        product=ItemId.GildaneSaddle,
        materials={
            ItemId.Leather: 40,
            ItemId.HighQualityCloth: 20,
            ItemId.PaldiumFragment: 60,
        },
    ),
    ItemId.NyafiaSShotgun: Recipe(
        product=ItemId.NyafiaSShotgun,
        materials={
            ItemId.RefinedIngot: 50,
            ItemId.DarkFragment: 30,
            ItemId.Polymer: 30,
            ItemId.PaldiumFragment: 85,
        },
    ),
    ItemId.CelesdirSaddle: Recipe(
        product=ItemId.CelesdirSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.HighQualityCloth: 20,
            ItemId.HighQualityRecoveryMeds: 10,
            ItemId.PaldiumFragment: 75,
        },
    ),
    ItemId.SilvegisSaddle: Recipe(
        product=ItemId.SilvegisSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.Hexolite: 15,
            ItemId.PaldiumFragment: 75,
        },
    ),
    ItemId.BastigorSHammer: Recipe(
        product=ItemId.BastigorSHammer,
        materials={
            ItemId.Hexolite: 30,
            ItemId.IceOrgan: 50,
            ItemId.PaldiumFragment: 140,
        },
    ),
    ItemId.XenolordSaddle: Recipe(
        product=ItemId.XenolordSaddle,
        materials={
            ItemId.Leather: 30,
            ItemId.DarkFragment: 50,
            ItemId.MeteoriteFragment: 30,
            ItemId.PaldiumFragment: 200,
        },
    ),
    ItemId.NeptiliusSaddle: Recipe(
        product=ItemId.NeptiliusSaddle,
        materials={
            ItemId.Leather: 100,
            ItemId.CoralumIngot: 40,
            ItemId.PalFluids: 68,
            ItemId.PaldiumFragment: 200,
        },
    ),
    ItemId.GrilledChikipi: Recipe(
        product=ItemId.GrilledChikipi,
        materials={
            ItemId.ChikipiPoultry: 1,
        },
    ),
    ItemId.LamballKebab: Recipe(
        product=ItemId.LamballKebab,
        materials={
            ItemId.LamballMutton: 1,
        },
    ),
    ItemId.GrilledKelpsea: Recipe(
        product=ItemId.GrilledKelpsea,
        materials={
            ItemId.RawKelpsea: 1,
        },
    ),
    ItemId.GrilledGaleclaw: Recipe(
        product=ItemId.GrilledGaleclaw,
        materials={
            ItemId.GaleclawPoultry: 1,
        },
    ),
    ItemId.RoastRushoar: Recipe(
        product=ItemId.RoastRushoar,
        materials={
            ItemId.RushoarPork: 1,
        },
    ),
    ItemId.BroiledDumud: Recipe(
        product=ItemId.BroiledDumud,
        materials={
            ItemId.RawDumud: 1,
        },
    ),
    ItemId.RoastEikthyrdeer: Recipe(
        product=ItemId.RoastEikthyrdeer,
        materials={
            ItemId.EikthyrdeerVenison: 1,
        },
    ),
    ItemId.RoastReindrix: Recipe(
        product=ItemId.RoastReindrix,
        materials={
            ItemId.ReindrixVenison: 1,
        },
    ),
    ItemId.HerbRoastedCaprity: Recipe(
        product=ItemId.HerbRoastedCaprity,
        materials={
            ItemId.CaprityMeat: 1,
        },
    ),
    ItemId.MozzarinaSteak: Recipe(
        product=ItemId.MozzarinaSteak,
        materials={
            ItemId.MozzarinaMeat: 1,
        },
    ),
    ItemId.BroncherryRibRoast: Recipe(
        product=ItemId.BroncherryRibRoast,
        materials={
            ItemId.BroncherryMeat: 1,
        },
    ),
    ItemId.MammorestSteak: Recipe(
        product=ItemId.MammorestSteak,
        materials={
            ItemId.MammorestMeat: 1,
        },
    ),
    ItemId.MunchillSteak: Recipe(
        product=ItemId.MunchillSteak,
        materials={
            ItemId.MunchillMeat: 1,
        },
    ),
    ItemId.ChikipiSaut: Recipe(
        product=ItemId.ChikipiSaut,
        materials={
            ItemId.ChikipiPoultry: 1,
            ItemId.RedBerries: 2,
        },
    ),
    ItemId.HerbRoastedLamball: Recipe(
        product=ItemId.HerbRoastedLamball,
        materials={
            ItemId.LamballMutton: 1,
            ItemId.RedBerries: 2,
        },
    ),
    ItemId.GrilledLamball: Recipe(
        product=ItemId.GrilledLamball,
        materials={
            ItemId.LamballMutton: 1,
            ItemId.Lettuce: 2,
        },
    ),
    ItemId.StewedGaleclaw: Recipe(
        product=ItemId.StewedGaleclaw,
        materials={
            ItemId.GaleclawPoultry: 1,
            ItemId.RedBerries: 2,
        },
    ),
    ItemId.RushoarBaconNEggs: Recipe(
        product=ItemId.RushoarBaconNEggs,
        materials={
            ItemId.RushoarPork: 2,
            ItemId.Egg: 2,
        },
    ),
    ItemId.ReindrixStew: Recipe(
        product=ItemId.ReindrixStew,
        materials={
            ItemId.ReindrixVenison: 1,
            ItemId.Tomato: 2,
        },
    ),
    ItemId.RushoarGyoza: Recipe(
        product=ItemId.RushoarGyoza,
        materials={
            ItemId.RushoarPork: 1,
            ItemId.Mushroom: 1,
            ItemId.Flour: 1,
        },
    ),
    ItemId.StirFriedVegetables: Recipe(
        product=ItemId.StirFriedVegetables,
        materials={
            ItemId.Onion: 2,
            ItemId.Carrot: 2,
        },
    ),
    ItemId.FrenchFries: Recipe(
        product=ItemId.FrenchFries,
        materials={
            ItemId.Potato: 2,
            ItemId.HighQualityPalOil: 1,
        },
    ),
    ItemId.FriedGloopieBalls: Recipe(
        product=ItemId.FriedGloopieBalls,
        materials={
            ItemId.GloopieTentacle: 2,
            ItemId.Flour: 3,
        },
    ),
    ItemId.JellietteSJigglyJelly: Recipe(
        product=ItemId.JellietteSJigglyJelly,
        materials={
            ItemId.JellietteBellFlesh: 2,
            ItemId.PalFluids: 2,
        },
    ),
    ItemId.JellroySJollyJelly: Recipe(
        product=ItemId.JellroySJollyJelly,
        materials={
            ItemId.JellroyBellFlesh: 2,
            ItemId.RedBerries: 2,
        },
    ),
    ItemId.FriedChikipi: Recipe(
        product=ItemId.FriedChikipi,
        materials={
            ItemId.ChikipiPoultry: 1,
            ItemId.Flour: 1,
            ItemId.Egg: 1,
            ItemId.HighQualityPalOil: 1,
        },
    ),
    ItemId.RushoarHotDog: Recipe(
        product=ItemId.RushoarHotDog,
        materials={
            ItemId.RushoarPork: 1,
            ItemId.Flour: 1,
            ItemId.Lettuce: 2,
        },
    ),
    ItemId.EikthyrdeerLocoMoco: Recipe(
        product=ItemId.EikthyrdeerLocoMoco,
        materials={
            ItemId.EikthyrdeerVenison: 1,
            ItemId.RedBerries: 2,
            ItemId.Egg: 2,
        },
    ),
    ItemId.EikthyrdeerStew: Recipe(
        product=ItemId.EikthyrdeerStew,
        materials={
            ItemId.EikthyrdeerVenison: 2,
            ItemId.Mushroom: 1,
            ItemId.Milk: 2,
        },
    ),
    ItemId.MozzarinaHamburger: Recipe(
        product=ItemId.MozzarinaHamburger,
        materials={
            ItemId.MozzarinaMeat: 1,
            ItemId.Flour: 1,
            ItemId.Lettuce: 2,
        },
    ),
    ItemId.MozzarinaCheeseburger: Recipe(
        product=ItemId.MozzarinaCheeseburger,
        materials={
            ItemId.MozzarinaMeat: 2,
            ItemId.Flour: 1,
            ItemId.Tomato: 2,
            ItemId.Milk: 2,
        },
    ),
    ItemId.FriedKelpsea: Recipe(
        product=ItemId.FriedKelpsea,
        materials={
            ItemId.RawKelpsea: 1,
            ItemId.Flour: 1,
            ItemId.Egg: 1,
            ItemId.HighQualityPalOil: 1,
        },
    ),
    ItemId.DumudChowder: Recipe(
        product=ItemId.DumudChowder,
        materials={
            ItemId.RawDumud: 1,
            ItemId.Lettuce: 2,
            ItemId.Tomato: 2,
        },
    ),
    ItemId.BroncherryFriedNoodles: Recipe(
        product=ItemId.BroncherryFriedNoodles,
        materials={
            ItemId.BroncherryMeat: 1,
            ItemId.Onion: 1,
            ItemId.Carrot: 1,
            ItemId.Flour: 1,
        },
    ),
    ItemId.SpringRolls: Recipe(
        product=ItemId.SpringRolls,
        materials={
            ItemId.Onion: 2,
            ItemId.Mushroom: 2,
            ItemId.Flour: 1,
        },
    ),
    ItemId.Gratin: Recipe(
        product=ItemId.Gratin,
        materials={
            ItemId.Milk: 2,
            ItemId.Potato: 2,
            ItemId.Flour: 1,
        },
    ),
    ItemId.Minestrone: Recipe(
        product=ItemId.Minestrone,
        materials={
            ItemId.Tomato: 3,
            ItemId.Carrot: 2,
            ItemId.Onion: 2,
            ItemId.Potato: 1,
        },
    ),
    ItemId.SeafoodSalad: Recipe(
        product=ItemId.SeafoodSalad,
        materials={
            ItemId.GloopieTentacle: 3,
            ItemId.Lettuce: 4,
        },
    ),
    ItemId.MammorestCurry: Recipe(
        product=ItemId.MammorestCurry,
        materials={
            ItemId.MammorestMeat: 1,
            ItemId.Onion: 2,
            ItemId.Carrot: 2,
            ItemId.Potato: 2,
            ItemId.RedBerries: 2,
        },
    ),
    ItemId.GaleclawNikujaga: Recipe(
        product=ItemId.GaleclawNikujaga,
        materials={
            ItemId.GaleclawPoultry: 1,
            ItemId.Onion: 2,
            ItemId.Carrot: 2,
            ItemId.Potato: 2,
        },
    ),
    ItemId.MushroomQuiche: Recipe(
        product=ItemId.MushroomQuiche,
        materials={
            ItemId.Flour: 1,
            ItemId.Mushroom: 2,
            ItemId.Onion: 2,
            ItemId.Egg: 2,
            ItemId.Milk: 2,
        },
    ),
    ItemId.VitalRemedy: Recipe(
        product=ItemId.VitalRemedy,
        materials={
            ItemId.LifeLotusS: 4,
            ItemId.RawKelpsea: 3,
            ItemId.GumossLeaf: 2,
            ItemId.PalFluids: 2,
        },
    ),
    ItemId.StaminaRemedy: Recipe(
        product=ItemId.StaminaRemedy,
        materials={
            ItemId.StaminaLotusS: 4,
            ItemId.EikthyrdeerVenison: 3,
            ItemId.Honey: 2,
            ItemId.PalFluids: 2,
        },
    ),
    ItemId.MightRemedy: Recipe(
        product=ItemId.MightRemedy,
        materials={
            ItemId.PowerLotusS: 4,
            ItemId.RushoarPork: 3,
            ItemId.MozzarinaMeat: 2,
            ItemId.PalFluids: 2,
        },
    ),
    ItemId.SpeedRemedy: Recipe(
        product=ItemId.SpeedRemedy,
        materials={
            ItemId.SpeedLotusS: 4,
            ItemId.RibbunyRibbon: 3,
            ItemId.KatressHair: 2,
            ItemId.PalFluids: 2,
        },
    ),
    ItemId.BurdenRemedy: Recipe(
        product=ItemId.BurdenRemedy,
        materials={
            ItemId.CarryingLotusS: 4,
            ItemId.SweeHair: 3,
            ItemId.CottonCandy: 2,
            ItemId.PalFluids: 2,
        },
    ),
    ItemId.VitalElixir: Recipe(
        product=ItemId.VitalElixir,
        materials={
            ItemId.LifeLotusL: 6,
            ItemId.GaleclawPoultry: 3,
            ItemId.KillamariTentacle: 2,
            ItemId.HighQualityPalOil: 2,
        },
    ),
    ItemId.StaminaElixir: Recipe(
        product=ItemId.StaminaElixir,
        materials={
            ItemId.StaminaLotusL: 6,
            ItemId.ReindrixVenison: 3,
            ItemId.CaprityMeat: 2,
            ItemId.HighQualityPalOil: 2,
        },
    ),
    ItemId.MightElixir: Recipe(
        product=ItemId.MightElixir,
        materials={
            ItemId.PowerLotusL: 6,
            ItemId.MammorestMeat: 3,
            ItemId.BroncherryMeat: 2,
            ItemId.HighQualityPalOil: 2,
        },
    ),
    ItemId.SpeedElixir: Recipe(
        product=ItemId.SpeedElixir,
        materials={
            ItemId.SpeedLotusL: 6,
            ItemId.DazziCloud: 3,
            ItemId.TocotocoFeather: 2,
            ItemId.HighQualityPalOil: 2,
        },
    ),
    ItemId.BurdenElixir: Recipe(
        product=ItemId.BurdenElixir,
        materials={
            ItemId.CarryingLotusL: 6,
            ItemId.LeezpunkCrest: 3,
            ItemId.RawDumud: 2,
            ItemId.HighQualityPalOil: 2,
        },
    ),
    ItemId.BellanoirSSlab: Recipe(
        product=ItemId.BellanoirSSlab,
        materials={
            ItemId.BellanoirSSlabFragment: 4,
        },
    ),
    ItemId.BellanoirLiberoSSlab: Recipe(
        product=ItemId.BellanoirLiberoSSlab,
        materials={
            ItemId.BellanoirLiberoSSlabFragment: 4,
        },
    ),
    ItemId.BellanoirLiberoUltraSlab: Recipe(
        product=ItemId.BellanoirLiberoUltraSlab,
        materials={
            ItemId.BellanoirLiberoUltraSlabFragment: 4,
        },
    ),
    ItemId.BlazamutRyuSlab: Recipe(
        product=ItemId.BlazamutRyuSlab,
        materials={
            ItemId.BlazamutRyuSlabFragment: 4,
        },
    ),
    ItemId.BlazamutRyuUltraSlab: Recipe(
        product=ItemId.BlazamutRyuUltraSlab,
        materials={
            ItemId.BlazamutRyuUltraSlabFragment: 4,
        },
    ),
    ItemId.XenolordSlab: Recipe(
        product=ItemId.XenolordSlab,
        materials={
            ItemId.XenolordSlabFragment: 4,
        },
    ),
    ItemId.XenolordUltraSlab: Recipe(
        product=ItemId.XenolordUltraSlab,
        materials={
            ItemId.XenolordUltraSlabFragment: 4,
        },
    ),
    ItemId.SmallPalSoul: Recipe(
        product=ItemId.SmallPalSoul,
        materials={
            ItemId.MediumPalSoul: 1,
        },
    ),
    ItemId.MediumPalSoul: Recipe(
        product=ItemId.MediumPalSoul,
        materials={
            ItemId.LargePalSoul: 1,
        },
    ),
    ItemId.LargePalSoul: Recipe(
        product=ItemId.LargePalSoul,
        materials={
            ItemId.GiantPalSoul: 1,
        },
    ),
    ItemId.GiantPalSoul: Recipe(
        product=ItemId.GiantPalSoul,
        materials={
            ItemId.LargePalSoul: 2,
        },
    ),
    ItemId.WitchSCrown: Recipe(
        product=ItemId.WitchSCrown,
        materials={
            ItemId.Ingot: 1,
        },
    ),
    ItemId.HornsOfSupremacy: Recipe(
        product=ItemId.HornsOfSupremacy,
        materials={
            ItemId.Ingot: 1,
        },
    ),
    ItemId.ZoeHat: Recipe(
        product=ItemId.ZoeHat,
        materials={
            ItemId.Cloth: 1,
        },
    ),
    ItemId.AxelHat: Recipe(
        product=ItemId.AxelHat,
        materials={
            ItemId.Cloth: 1,
        },
    ),
    ItemId.LilyHat: Recipe(
        product=ItemId.LilyHat,
        materials={
            ItemId.Cloth: 1,
        },
    ),
    ItemId.VictorHat: Recipe(
        product=ItemId.VictorHat,
        materials={
            ItemId.Cloth: 1,
        },
    ),
    ItemId.MarcusHat: Recipe(
        product=ItemId.MarcusHat,
        materials={
            ItemId.Cloth: 1,
        },
    ),
    ItemId.SayaHat: Recipe(
        product=ItemId.SayaHat,
        materials={
            ItemId.Cloth: 1,
        },
    ),
    ItemId.BjornHat: Recipe(
        product=ItemId.BjornHat,
        materials={
            ItemId.Cloth: 1,
        },
    ),
    ItemId.LockpickingToolV1: Recipe(
        product=ItemId.LockpickingToolV1,
        materials={
            ItemId.Ingot: 10,
            ItemId.PaldiumFragment: 10,
            ItemId.Nail: 5,
        },
    ),
    ItemId.LockpickingToolV2: Recipe(
        product=ItemId.LockpickingToolV2,
        materials={
            ItemId.Ingot: 20,
            ItemId.PaldiumFragment: 20,
            ItemId.Nail: 10,
        },
    ),
    ItemId.LockpickingToolV3: Recipe(
        product=ItemId.LockpickingToolV3,
        materials={
            ItemId.PalMetalIngot: 30,
            ItemId.PaldiumFragment: 30,
            ItemId.Nail: 20,
        },
    ),
    ItemId.CattivaHat: Recipe(
        product=ItemId.CattivaHat,
        materials={
            ItemId.Cloth: 1,
        },
    ),
    ItemId.LamballHelm: Recipe(
        product=ItemId.LamballHelm,
        materials={
            ItemId.Cloth: 1,
        },
    ),
    ItemId.CawgnitoHat: Recipe(
        product=ItemId.CawgnitoHat,
        materials={
            ItemId.Cloth: 1,
        },
    ),
    ItemId.DumudHelm: Recipe(
        product=ItemId.DumudHelm,
        materials={
            ItemId.Cloth: 1,
        },
    ),
    ItemId.SibelyxHat: Recipe(
        product=ItemId.SibelyxHat,
        materials={
            ItemId.Cloth: 1,
        },
    ),
    ItemId.LyleenFloralCap: Recipe(
        product=ItemId.LyleenFloralCap,
        materials={
            ItemId.Cloth: 1,
        },
    ),
    ItemId.GoldCoin: Recipe(
        product=ItemId.GoldCoin,
        materials={
            ItemId.Ingot: 1,
        },
    ),
    ItemId.SwordSchematic2: Recipe(
        product=ItemId.SwordSchematic2,
        materials={
            ItemId.SwordSchematic1: 5,
        },
    ),
    ItemId.SwordSchematic3: Recipe(
        product=ItemId.SwordSchematic3,
        materials={
            ItemId.SwordSchematic2: 5,
        },
    ),
    ItemId.SwordSchematic4: Recipe(
        product=ItemId.SwordSchematic4,
        materials={
            ItemId.SwordSchematic3: 5,
        },
    ),
    ItemId.KatanaSchematic2: Recipe(
        product=ItemId.KatanaSchematic2,
        materials={
            ItemId.KatanaSchematic1: 5,
        },
    ),
    ItemId.KatanaSchematic3: Recipe(
        product=ItemId.KatanaSchematic3,
        materials={
            ItemId.KatanaSchematic2: 5,
        },
    ),
    ItemId.KatanaSchematic4: Recipe(
        product=ItemId.KatanaSchematic4,
        materials={
            ItemId.KatanaSchematic3: 5,
        },
    ),
    ItemId.BeamSwordSchematic2: Recipe(
        product=ItemId.BeamSwordSchematic2,
        materials={
            ItemId.BeamSwordSchematic1: 5,
        },
    ),
    ItemId.BeamSwordSchematic3: Recipe(
        product=ItemId.BeamSwordSchematic3,
        materials={
            ItemId.BeamSwordSchematic2: 5,
        },
    ),
    ItemId.BeamSwordSchematic4: Recipe(
        product=ItemId.BeamSwordSchematic4,
        materials={
            ItemId.BeamSwordSchematic3: 5,
        },
    ),
    ItemId.OldBowSchematic2: Recipe(
        product=ItemId.OldBowSchematic2,
        materials={
            ItemId.OldBowSchematic1: 5,
        },
    ),
    ItemId.OldBowSchematic3: Recipe(
        product=ItemId.OldBowSchematic3,
        materials={
            ItemId.OldBowSchematic2: 5,
        },
    ),
    ItemId.OldBowSchematic4: Recipe(
        product=ItemId.OldBowSchematic4,
        materials={
            ItemId.OldBowSchematic3: 5,
        },
    ),
    ItemId.CrossbowSchematic2: Recipe(
        product=ItemId.CrossbowSchematic2,
        materials={
            ItemId.CrossbowSchematic1: 5,
        },
    ),
    ItemId.CrossbowSchematic3: Recipe(
        product=ItemId.CrossbowSchematic3,
        materials={
            ItemId.CrossbowSchematic2: 5,
        },
    ),
    ItemId.CrossbowSchematic4: Recipe(
        product=ItemId.CrossbowSchematic4,
        materials={
            ItemId.CrossbowSchematic3: 5,
        },
    ),
    ItemId.FireArrowCrossbowSchematic2: Recipe(
        product=ItemId.FireArrowCrossbowSchematic2,
        materials={
            ItemId.FireArrowCrossbowSchematic1: 5,
        },
    ),
    ItemId.FireArrowCrossbowSchematic3: Recipe(
        product=ItemId.FireArrowCrossbowSchematic3,
        materials={
            ItemId.FireArrowCrossbowSchematic2: 5,
        },
    ),
    ItemId.FireArrowCrossbowSchematic4: Recipe(
        product=ItemId.FireArrowCrossbowSchematic4,
        materials={
            ItemId.FireArrowCrossbowSchematic3: 5,
        },
    ),
    ItemId.PoisonArrowCrossbowSchematic2: Recipe(
        product=ItemId.PoisonArrowCrossbowSchematic2,
        materials={
            ItemId.PoisonArrowCrossbowSchematic1: 5,
        },
    ),
    ItemId.PoisonArrowCrossbowSchematic3: Recipe(
        product=ItemId.PoisonArrowCrossbowSchematic3,
        materials={
            ItemId.PoisonArrowCrossbowSchematic2: 5,
        },
    ),
    ItemId.PoisonArrowCrossbowSchematic4: Recipe(
        product=ItemId.PoisonArrowCrossbowSchematic4,
        materials={
            ItemId.PoisonArrowCrossbowSchematic3: 5,
        },
    ),
    ItemId.MakeshiftHandgunSchematic2: Recipe(
        product=ItemId.MakeshiftHandgunSchematic2,
        materials={
            ItemId.MakeshiftHandgunSchematic1: 5,
        },
    ),
    ItemId.MakeshiftHandgunSchematic3: Recipe(
        product=ItemId.MakeshiftHandgunSchematic3,
        materials={
            ItemId.MakeshiftHandgunSchematic2: 5,
        },
    ),
    ItemId.MakeshiftHandgunSchematic4: Recipe(
        product=ItemId.MakeshiftHandgunSchematic4,
        materials={
            ItemId.MakeshiftHandgunSchematic3: 5,
        },
    ),
    ItemId.MusketSchematic2: Recipe(
        product=ItemId.MusketSchematic2,
        materials={
            ItemId.MusketSchematic1: 5,
        },
    ),
    ItemId.MusketSchematic3: Recipe(
        product=ItemId.MusketSchematic3,
        materials={
            ItemId.MusketSchematic2: 5,
        },
    ),
    ItemId.MusketSchematic4: Recipe(
        product=ItemId.MusketSchematic4,
        materials={
            ItemId.MusketSchematic3: 5,
        },
    ),
    ItemId.HandgunSchematic2: Recipe(
        product=ItemId.HandgunSchematic2,
        materials={
            ItemId.HandgunSchematic1: 5,
        },
    ),
    ItemId.HandgunSchematic3: Recipe(
        product=ItemId.HandgunSchematic3,
        materials={
            ItemId.HandgunSchematic2: 5,
        },
    ),
    ItemId.HandgunSchematic4: Recipe(
        product=ItemId.HandgunSchematic4,
        materials={
            ItemId.HandgunSchematic3: 5,
        },
    ),
    ItemId.OldRevolverSchematic2: Recipe(
        product=ItemId.OldRevolverSchematic2,
        materials={
            ItemId.OldRevolverSchematic1: 5,
        },
    ),
    ItemId.OldRevolverSchematic3: Recipe(
        product=ItemId.OldRevolverSchematic3,
        materials={
            ItemId.OldRevolverSchematic2: 5,
        },
    ),
    ItemId.OldRevolverSchematic4: Recipe(
        product=ItemId.OldRevolverSchematic4,
        materials={
            ItemId.OldRevolverSchematic3: 5,
        },
    ),
    ItemId.SingleShotRifleSchematic2: Recipe(
        product=ItemId.SingleShotRifleSchematic2,
        materials={
            ItemId.SingleShotRifleSchematic1: 5,
        },
    ),
    ItemId.SingleShotRifleSchematic3: Recipe(
        product=ItemId.SingleShotRifleSchematic3,
        materials={
            ItemId.SingleShotRifleSchematic2: 5,
        },
    ),
    ItemId.SingleShotRifleSchematic4: Recipe(
        product=ItemId.SingleShotRifleSchematic4,
        materials={
            ItemId.SingleShotRifleSchematic3: 5,
        },
    ),
    ItemId.SemiAutoRifleSchematic2: Recipe(
        product=ItemId.SemiAutoRifleSchematic2,
        materials={
            ItemId.SemiAutoRifleSchematic1: 5,
        },
    ),
    ItemId.SemiAutoRifleSchematic3: Recipe(
        product=ItemId.SemiAutoRifleSchematic3,
        materials={
            ItemId.SemiAutoRifleSchematic2: 5,
        },
    ),
    ItemId.SemiAutoRifleSchematic4: Recipe(
        product=ItemId.SemiAutoRifleSchematic4,
        materials={
            ItemId.SemiAutoRifleSchematic3: 5,
        },
    ),
    ItemId.MakeshiftAssaultRifleSchematic2: Recipe(
        product=ItemId.MakeshiftAssaultRifleSchematic2,
        materials={
            ItemId.MakeshiftAssaultRifleSchematic1: 5,
        },
    ),
    ItemId.MakeshiftAssaultRifleSchematic3: Recipe(
        product=ItemId.MakeshiftAssaultRifleSchematic3,
        materials={
            ItemId.MakeshiftAssaultRifleSchematic2: 5,
        },
    ),
    ItemId.MakeshiftAssaultRifleSchematic4: Recipe(
        product=ItemId.MakeshiftAssaultRifleSchematic4,
        materials={
            ItemId.MakeshiftAssaultRifleSchematic3: 5,
        },
    ),
    ItemId.AssaultRifleSchematic2: Recipe(
        product=ItemId.AssaultRifleSchematic2,
        materials={
            ItemId.AssaultRifleSchematic1: 5,
        },
    ),
    ItemId.AssaultRifleSchematic3: Recipe(
        product=ItemId.AssaultRifleSchematic3,
        materials={
            ItemId.AssaultRifleSchematic2: 5,
        },
    ),
    ItemId.AssaultRifleSchematic4: Recipe(
        product=ItemId.AssaultRifleSchematic4,
        materials={
            ItemId.AssaultRifleSchematic3: 5,
        },
    ),
    ItemId.MakeshiftShotgunSchematic2: Recipe(
        product=ItemId.MakeshiftShotgunSchematic2,
        materials={
            ItemId.MakeshiftShotgunSchematic1: 5,
        },
    ),
    ItemId.MakeshiftShotgunSchematic3: Recipe(
        product=ItemId.MakeshiftShotgunSchematic3,
        materials={
            ItemId.MakeshiftShotgunSchematic2: 5,
        },
    ),
    ItemId.MakeshiftShotgunSchematic4: Recipe(
        product=ItemId.MakeshiftShotgunSchematic4,
        materials={
            ItemId.MakeshiftShotgunSchematic3: 5,
        },
    ),
    ItemId.DoubleBarreledShotgunSchematic2: Recipe(
        product=ItemId.DoubleBarreledShotgunSchematic2,
        materials={
            ItemId.DoubleBarreledShotgunSchematic1: 5,
        },
    ),
    ItemId.DoubleBarreledShotgunSchematic3: Recipe(
        product=ItemId.DoubleBarreledShotgunSchematic3,
        materials={
            ItemId.DoubleBarreledShotgunSchematic2: 5,
        },
    ),
    ItemId.DoubleBarreledShotgunSchematic4: Recipe(
        product=ItemId.DoubleBarreledShotgunSchematic4,
        materials={
            ItemId.DoubleBarreledShotgunSchematic3: 5,
        },
    ),
    ItemId.PumpActionShotgunSchematic2: Recipe(
        product=ItemId.PumpActionShotgunSchematic2,
        materials={
            ItemId.PumpActionShotgunSchematic1: 5,
        },
    ),
    ItemId.PumpActionShotgunSchematic3: Recipe(
        product=ItemId.PumpActionShotgunSchematic3,
        materials={
            ItemId.PumpActionShotgunSchematic2: 5,
        },
    ),
    ItemId.PumpActionShotgunSchematic4: Recipe(
        product=ItemId.PumpActionShotgunSchematic4,
        materials={
            ItemId.PumpActionShotgunSchematic3: 5,
        },
    ),
    ItemId.SemiAutoShotgunSchematic2: Recipe(
        product=ItemId.SemiAutoShotgunSchematic2,
        materials={
            ItemId.SemiAutoShotgunSchematic1: 5,
        },
    ),
    ItemId.SemiAutoShotgunSchematic3: Recipe(
        product=ItemId.SemiAutoShotgunSchematic3,
        materials={
            ItemId.SemiAutoShotgunSchematic2: 5,
        },
    ),
    ItemId.SemiAutoShotgunSchematic4: Recipe(
        product=ItemId.SemiAutoShotgunSchematic4,
        materials={
            ItemId.SemiAutoShotgunSchematic3: 5,
        },
    ),
    ItemId.MakeshiftSMGSchematic2: Recipe(
        product=ItemId.MakeshiftSMGSchematic2,
        materials={
            ItemId.MakeshiftSMGSchematic1: 5,
        },
    ),
    ItemId.MakeshiftSMGSchematic3: Recipe(
        product=ItemId.MakeshiftSMGSchematic3,
        materials={
            ItemId.MakeshiftSMGSchematic2: 5,
        },
    ),
    ItemId.MakeshiftSMGSchematic4: Recipe(
        product=ItemId.MakeshiftSMGSchematic4,
        materials={
            ItemId.MakeshiftSMGSchematic3: 5,
        },
    ),
    ItemId.SMGSchematic2: Recipe(
        product=ItemId.SMGSchematic2,
        materials={
            ItemId.SMGSchematic1: 5,
        },
    ),
    ItemId.SMGSchematic3: Recipe(
        product=ItemId.SMGSchematic3,
        materials={
            ItemId.SMGSchematic2: 5,
        },
    ),
    ItemId.SMGSchematic4: Recipe(
        product=ItemId.SMGSchematic4,
        materials={
            ItemId.SMGSchematic3: 5,
        },
    ),
    ItemId.RocketLauncherSchematic2: Recipe(
        product=ItemId.RocketLauncherSchematic2,
        materials={
            ItemId.RocketLauncherSchematic1: 5,
        },
    ),
    ItemId.RocketLauncherSchematic3: Recipe(
        product=ItemId.RocketLauncherSchematic3,
        materials={
            ItemId.RocketLauncherSchematic2: 5,
        },
    ),
    ItemId.RocketLauncherSchematic4: Recipe(
        product=ItemId.RocketLauncherSchematic4,
        materials={
            ItemId.RocketLauncherSchematic3: 5,
        },
    ),
    ItemId.LaserRifleSchematic2: Recipe(
        product=ItemId.LaserRifleSchematic2,
        materials={
            ItemId.LaserRifleSchematic1: 5,
        },
    ),
    ItemId.LaserRifleSchematic3: Recipe(
        product=ItemId.LaserRifleSchematic3,
        materials={
            ItemId.LaserRifleSchematic2: 5,
        },
    ),
    ItemId.LaserRifleSchematic4: Recipe(
        product=ItemId.LaserRifleSchematic4,
        materials={
            ItemId.LaserRifleSchematic3: 5,
        },
    ),
    ItemId.FlamethrowerSchematic2: Recipe(
        product=ItemId.FlamethrowerSchematic2,
        materials={
            ItemId.FlamethrowerSchematic1: 5,
        },
    ),
    ItemId.FlamethrowerSchematic3: Recipe(
        product=ItemId.FlamethrowerSchematic3,
        materials={
            ItemId.FlamethrowerSchematic2: 5,
        },
    ),
    ItemId.FlamethrowerSchematic4: Recipe(
        product=ItemId.FlamethrowerSchematic4,
        materials={
            ItemId.FlamethrowerSchematic3: 5,
        },
    ),
    ItemId.GrenadeLauncherSchematic2: Recipe(
        product=ItemId.GrenadeLauncherSchematic2,
        materials={
            ItemId.GrenadeLauncherSchematic1: 5,
        },
    ),
    ItemId.GrenadeLauncherSchematic3: Recipe(
        product=ItemId.GrenadeLauncherSchematic3,
        materials={
            ItemId.GrenadeLauncherSchematic2: 5,
        },
    ),
    ItemId.GrenadeLauncherSchematic4: Recipe(
        product=ItemId.GrenadeLauncherSchematic4,
        materials={
            ItemId.GrenadeLauncherSchematic3: 5,
        },
    ),
    ItemId.GuidedMissileLauncherSchematic2: Recipe(
        product=ItemId.GuidedMissileLauncherSchematic2,
        materials={
            ItemId.GuidedMissileLauncherSchematic1: 5,
        },
    ),
    ItemId.GuidedMissileLauncherSchematic3: Recipe(
        product=ItemId.GuidedMissileLauncherSchematic3,
        materials={
            ItemId.GuidedMissileLauncherSchematic2: 5,
        },
    ),
    ItemId.GuidedMissileLauncherSchematic4: Recipe(
        product=ItemId.GuidedMissileLauncherSchematic4,
        materials={
            ItemId.GuidedMissileLauncherSchematic3: 5,
        },
    ),
    ItemId.MultiGuidedMissileLauncherSchematic1: Recipe(
        product=ItemId.MultiGuidedMissileLauncherSchematic1,
        materials={
            ItemId.MultiGuidedMissileLauncherSchematic: 5,
        },
    ),
    ItemId.MultiGuidedMissileLauncherSchematic2: Recipe(
        product=ItemId.MultiGuidedMissileLauncherSchematic2,
        materials={
            ItemId.MultiGuidedMissileLauncherSchematic1: 5,
        },
    ),
    ItemId.MultiGuidedMissileLauncherSchematic3: Recipe(
        product=ItemId.MultiGuidedMissileLauncherSchematic3,
        materials={
            ItemId.MultiGuidedMissileLauncherSchematic2: 5,
        },
    ),
    ItemId.MultiGuidedMissileLauncherSchematic4: Recipe(
        product=ItemId.MultiGuidedMissileLauncherSchematic4,
        materials={
            ItemId.MultiGuidedMissileLauncherSchematic3: 5,
        },
    ),
    ItemId.GatlingGunSchematic2: Recipe(
        product=ItemId.GatlingGunSchematic2,
        materials={
            ItemId.GatlingGunSchematic1: 5,
        },
    ),
    ItemId.GatlingGunSchematic3: Recipe(
        product=ItemId.GatlingGunSchematic3,
        materials={
            ItemId.GatlingGunSchematic2: 5,
        },
    ),
    ItemId.GatlingGunSchematic4: Recipe(
        product=ItemId.GatlingGunSchematic4,
        materials={
            ItemId.GatlingGunSchematic3: 5,
        },
    ),
    ItemId.LaserGatlingGunSchematic2: Recipe(
        product=ItemId.LaserGatlingGunSchematic2,
        materials={
            ItemId.LaserGatlingGunSchematic1: 5,
        },
    ),
    ItemId.LaserGatlingGunSchematic3: Recipe(
        product=ItemId.LaserGatlingGunSchematic3,
        materials={
            ItemId.LaserGatlingGunSchematic2: 5,
        },
    ),
    ItemId.LaserGatlingGunSchematic4: Recipe(
        product=ItemId.LaserGatlingGunSchematic4,
        materials={
            ItemId.LaserGatlingGunSchematic3: 5,
        },
    ),
    ItemId.PlasmaCannonSchematic2: Recipe(
        product=ItemId.PlasmaCannonSchematic2,
        materials={
            ItemId.PlasmaCannonSchematic1: 5,
        },
    ),
    ItemId.PlasmaCannonSchematic3: Recipe(
        product=ItemId.PlasmaCannonSchematic3,
        materials={
            ItemId.PlasmaCannonSchematic2: 5,
        },
    ),
    ItemId.PlasmaCannonSchematic4: Recipe(
        product=ItemId.PlasmaCannonSchematic4,
        materials={
            ItemId.PlasmaCannonSchematic3: 5,
        },
    ),
    ItemId.CompoundBowSchematic2: Recipe(
        product=ItemId.CompoundBowSchematic2,
        materials={
            ItemId.CompoundBowSchematic1: 5,
        },
    ),
    ItemId.CompoundBowSchematic3: Recipe(
        product=ItemId.CompoundBowSchematic3,
        materials={
            ItemId.CompoundBowSchematic2: 5,
        },
    ),
    ItemId.CompoundBowSchematic4: Recipe(
        product=ItemId.CompoundBowSchematic4,
        materials={
            ItemId.CompoundBowSchematic3: 5,
        },
    ),
    ItemId.AdvancedBowSchematic2: Recipe(
        product=ItemId.AdvancedBowSchematic2,
        materials={
            ItemId.AdvancedBowSchematic1: 5,
        },
    ),
    ItemId.AdvancedBowSchematic3: Recipe(
        product=ItemId.AdvancedBowSchematic3,
        materials={
            ItemId.AdvancedBowSchematic2: 5,
        },
    ),
    ItemId.AdvancedBowSchematic4: Recipe(
        product=ItemId.AdvancedBowSchematic4,
        materials={
            ItemId.AdvancedBowSchematic3: 5,
        },
    ),
    ItemId.EnergyShotgunSchematic2: Recipe(
        product=ItemId.EnergyShotgunSchematic2,
        materials={
            ItemId.EnergyShotgunSchematic1: 5,
        },
    ),
    ItemId.EnergyShotgunSchematic3: Recipe(
        product=ItemId.EnergyShotgunSchematic3,
        materials={
            ItemId.EnergyShotgunSchematic2: 5,
        },
    ),
    ItemId.EnergyShotgunSchematic4: Recipe(
        product=ItemId.EnergyShotgunSchematic4,
        materials={
            ItemId.EnergyShotgunSchematic3: 5,
        },
    ),
    ItemId.OverheatRifleSchematic2: Recipe(
        product=ItemId.OverheatRifleSchematic2,
        materials={
            ItemId.OverheatRifleSchematic1: 5,
        },
    ),
    ItemId.OverheatRifleSchematic3: Recipe(
        product=ItemId.OverheatRifleSchematic3,
        materials={
            ItemId.OverheatRifleSchematic2: 5,
        },
    ),
    ItemId.OverheatRifleSchematic4: Recipe(
        product=ItemId.OverheatRifleSchematic4,
        materials={
            ItemId.OverheatRifleSchematic3: 5,
        },
    ),
    ItemId.ChargeRifleSchematic2: Recipe(
        product=ItemId.ChargeRifleSchematic2,
        materials={
            ItemId.ChargeRifleSchematic1: 5,
        },
    ),
    ItemId.ChargeRifleSchematic3: Recipe(
        product=ItemId.ChargeRifleSchematic3,
        materials={
            ItemId.ChargeRifleSchematic2: 5,
        },
    ),
    ItemId.ChargeRifleSchematic4: Recipe(
        product=ItemId.ChargeRifleSchematic4,
        materials={
            ItemId.ChargeRifleSchematic3: 5,
        },
    ),
    ItemId.ExcaliburSchematic1: Recipe(
        product=ItemId.ExcaliburSchematic1,
        materials={
            ItemId.ExcaliburSchematic: 5,
        },
    ),
    ItemId.ExcaliburSchematic2: Recipe(
        product=ItemId.ExcaliburSchematic2,
        materials={
            ItemId.ExcaliburSchematic1: 5,
        },
    ),
    ItemId.ExcaliburSchematic3: Recipe(
        product=ItemId.ExcaliburSchematic3,
        materials={
            ItemId.ExcaliburSchematic2: 5,
        },
    ),
    ItemId.ExcaliburSchematic4: Recipe(
        product=ItemId.ExcaliburSchematic4,
        materials={
            ItemId.ExcaliburSchematic3: 5,
        },
    ),
    ItemId.TerraprismaSchematic1: Recipe(
        product=ItemId.TerraprismaSchematic1,
        materials={
            ItemId.TerraprismaSchematic: 5,
        },
    ),
    ItemId.TerraprismaSchematic2: Recipe(
        product=ItemId.TerraprismaSchematic2,
        materials={
            ItemId.TerraprismaSchematic1: 5,
        },
    ),
    ItemId.TerraprismaSchematic3: Recipe(
        product=ItemId.TerraprismaSchematic3,
        materials={
            ItemId.TerraprismaSchematic2: 5,
        },
    ),
    ItemId.TerraprismaSchematic4: Recipe(
        product=ItemId.TerraprismaSchematic4,
        materials={
            ItemId.TerraprismaSchematic3: 5,
        },
    ),
    ItemId.VortexBeaterSchematic1: Recipe(
        product=ItemId.VortexBeaterSchematic1,
        materials={
            ItemId.VortexBeaterSchematic: 5,
        },
    ),
    ItemId.VortexBeaterSchematic2: Recipe(
        product=ItemId.VortexBeaterSchematic2,
        materials={
            ItemId.VortexBeaterSchematic1: 5,
        },
    ),
    ItemId.VortexBeaterSchematic3: Recipe(
        product=ItemId.VortexBeaterSchematic3,
        materials={
            ItemId.VortexBeaterSchematic2: 5,
        },
    ),
    ItemId.VortexBeaterSchematic4: Recipe(
        product=ItemId.VortexBeaterSchematic4,
        materials={
            ItemId.VortexBeaterSchematic3: 5,
        },
    ),
    ItemId.NightglowSchematic1: Recipe(
        product=ItemId.NightglowSchematic1,
        materials={
            ItemId.NightglowSchematic: 5,
        },
    ),
    ItemId.NightglowSchematic2: Recipe(
        product=ItemId.NightglowSchematic2,
        materials={
            ItemId.NightglowSchematic1: 5,
        },
    ),
    ItemId.NightglowSchematic3: Recipe(
        product=ItemId.NightglowSchematic3,
        materials={
            ItemId.NightglowSchematic2: 5,
        },
    ),
    ItemId.NightglowSchematic4: Recipe(
        product=ItemId.NightglowSchematic4,
        materials={
            ItemId.NightglowSchematic3: 5,
        },
    ),
    ItemId.TerraBladeSchematic1: Recipe(
        product=ItemId.TerraBladeSchematic1,
        materials={
            ItemId.TerraBladeSchematic: 5,
        },
    ),
    ItemId.TerraBladeSchematic2: Recipe(
        product=ItemId.TerraBladeSchematic2,
        materials={
            ItemId.TerraBladeSchematic1: 5,
        },
    ),
    ItemId.TerraBladeSchematic3: Recipe(
        product=ItemId.TerraBladeSchematic3,
        materials={
            ItemId.TerraBladeSchematic2: 5,
        },
    ),
    ItemId.TerraBladeSchematic4: Recipe(
        product=ItemId.TerraBladeSchematic4,
        materials={
            ItemId.TerraBladeSchematic3: 5,
        },
    ),
    ItemId.ClothOutfitSchematic2: Recipe(
        product=ItemId.ClothOutfitSchematic2,
        materials={
            ItemId.ClothOutfitSchematic1: 5,
        },
    ),
    ItemId.ClothOutfitSchematic3: Recipe(
        product=ItemId.ClothOutfitSchematic3,
        materials={
            ItemId.ClothOutfitSchematic2: 5,
        },
    ),
    ItemId.ClothOutfitSchematic4: Recipe(
        product=ItemId.ClothOutfitSchematic4,
        materials={
            ItemId.ClothOutfitSchematic3: 5,
        },
    ),
    ItemId.TropicalOutfitSchematic2: Recipe(
        product=ItemId.TropicalOutfitSchematic2,
        materials={
            ItemId.TropicalOutfitSchematic1: 5,
        },
    ),
    ItemId.TropicalOutfitSchematic3: Recipe(
        product=ItemId.TropicalOutfitSchematic3,
        materials={
            ItemId.TropicalOutfitSchematic2: 5,
        },
    ),
    ItemId.TropicalOutfitSchematic4: Recipe(
        product=ItemId.TropicalOutfitSchematic4,
        materials={
            ItemId.TropicalOutfitSchematic3: 5,
        },
    ),
    ItemId.TundraOutfitSchematic2: Recipe(
        product=ItemId.TundraOutfitSchematic2,
        materials={
            ItemId.TundraOutfitSchematic1: 5,
        },
    ),
    ItemId.TundraOutfitSchematic3: Recipe(
        product=ItemId.TundraOutfitSchematic3,
        materials={
            ItemId.TundraOutfitSchematic2: 5,
        },
    ),
    ItemId.TundraOutfitSchematic4: Recipe(
        product=ItemId.TundraOutfitSchematic4,
        materials={
            ItemId.TundraOutfitSchematic3: 5,
        },
    ),
    ItemId.PeltArmorSchematic2: Recipe(
        product=ItemId.PeltArmorSchematic2,
        materials={
            ItemId.PeltArmorSchematic1: 5,
        },
    ),
    ItemId.PeltArmorSchematic3: Recipe(
        product=ItemId.PeltArmorSchematic3,
        materials={
            ItemId.PeltArmorSchematic2: 5,
        },
    ),
    ItemId.PeltArmorSchematic4: Recipe(
        product=ItemId.PeltArmorSchematic4,
        materials={
            ItemId.PeltArmorSchematic3: 5,
        },
    ),
    ItemId.HeatResistantPeltArmorSchematic2: Recipe(
        product=ItemId.HeatResistantPeltArmorSchematic2,
        materials={
            ItemId.HeatResistantPeltArmorSchematic1: 5,
        },
    ),
    ItemId.HeatResistantPeltArmorSchematic3: Recipe(
        product=ItemId.HeatResistantPeltArmorSchematic3,
        materials={
            ItemId.HeatResistantPeltArmorSchematic2: 5,
        },
    ),
    ItemId.HeatResistantPeltArmorSchematic4: Recipe(
        product=ItemId.HeatResistantPeltArmorSchematic4,
        materials={
            ItemId.HeatResistantPeltArmorSchematic3: 5,
        },
    ),
    ItemId.ColdResistantPeltArmorSchematic2: Recipe(
        product=ItemId.ColdResistantPeltArmorSchematic2,
        materials={
            ItemId.ColdResistantPeltArmorSchematic1: 5,
        },
    ),
    ItemId.ColdResistantPeltArmorSchematic3: Recipe(
        product=ItemId.ColdResistantPeltArmorSchematic3,
        materials={
            ItemId.ColdResistantPeltArmorSchematic2: 5,
        },
    ),
    ItemId.ColdResistantPeltArmorSchematic4: Recipe(
        product=ItemId.ColdResistantPeltArmorSchematic4,
        materials={
            ItemId.ColdResistantPeltArmorSchematic3: 5,
        },
    ),
    ItemId.MetalArmorSchematic2: Recipe(
        product=ItemId.MetalArmorSchematic2,
        materials={
            ItemId.MetalArmorSchematic1: 5,
        },
    ),
    ItemId.MetalArmorSchematic3: Recipe(
        product=ItemId.MetalArmorSchematic3,
        materials={
            ItemId.MetalArmorSchematic2: 5,
        },
    ),
    ItemId.MetalArmorSchematic4: Recipe(
        product=ItemId.MetalArmorSchematic4,
        materials={
            ItemId.MetalArmorSchematic3: 5,
        },
    ),
    ItemId.HeatResistantMetalArmorSchematic2: Recipe(
        product=ItemId.HeatResistantMetalArmorSchematic2,
        materials={
            ItemId.HeatResistantMetalArmorSchematic1: 5,
        },
    ),
    ItemId.HeatResistantMetalArmorSchematic3: Recipe(
        product=ItemId.HeatResistantMetalArmorSchematic3,
        materials={
            ItemId.HeatResistantMetalArmorSchematic2: 5,
        },
    ),
    ItemId.HeatResistantMetalArmorSchematic4: Recipe(
        product=ItemId.HeatResistantMetalArmorSchematic4,
        materials={
            ItemId.HeatResistantMetalArmorSchematic3: 5,
        },
    ),
    ItemId.ColdResistantMetalArmorSchematic2: Recipe(
        product=ItemId.ColdResistantMetalArmorSchematic2,
        materials={
            ItemId.ColdResistantMetalArmorSchematic1: 5,
        },
    ),
    ItemId.ColdResistantMetalArmorSchematic3: Recipe(
        product=ItemId.ColdResistantMetalArmorSchematic3,
        materials={
            ItemId.ColdResistantMetalArmorSchematic2: 5,
        },
    ),
    ItemId.ColdResistantMetalArmorSchematic4: Recipe(
        product=ItemId.ColdResistantMetalArmorSchematic4,
        materials={
            ItemId.ColdResistantMetalArmorSchematic3: 5,
        },
    ),
    ItemId.RefinedMetalArmorSchematic2: Recipe(
        product=ItemId.RefinedMetalArmorSchematic2,
        materials={
            ItemId.RefinedMetalArmorSchematic1: 5,
        },
    ),
    ItemId.RefinedMetalArmorSchematic3: Recipe(
        product=ItemId.RefinedMetalArmorSchematic3,
        materials={
            ItemId.RefinedMetalArmorSchematic2: 5,
        },
    ),
    ItemId.RefinedMetalArmorSchematic4: Recipe(
        product=ItemId.RefinedMetalArmorSchematic4,
        materials={
            ItemId.RefinedMetalArmorSchematic3: 5,
        },
    ),
    ItemId.HeatResistantRefinedMetalArmorSchematic2: Recipe(
        product=ItemId.HeatResistantRefinedMetalArmorSchematic2,
        materials={
            ItemId.HeatResistantRefinedMetalArmorSchematic1: 5,
        },
    ),
    ItemId.HeatResistantRefinedMetalArmorSchematic3: Recipe(
        product=ItemId.HeatResistantRefinedMetalArmorSchematic3,
        materials={
            ItemId.HeatResistantRefinedMetalArmorSchematic2: 5,
        },
    ),
    ItemId.HeatResistantRefinedMetalArmorSchematic4: Recipe(
        product=ItemId.HeatResistantRefinedMetalArmorSchematic4,
        materials={
            ItemId.HeatResistantRefinedMetalArmorSchematic3: 5,
        },
    ),
    ItemId.ColdResistantRefinedMetalArmorSchematic2: Recipe(
        product=ItemId.ColdResistantRefinedMetalArmorSchematic2,
        materials={
            ItemId.ColdResistantRefinedMetalArmorSchematic1: 5,
        },
    ),
    ItemId.ColdResistantRefinedMetalArmorSchematic3: Recipe(
        product=ItemId.ColdResistantRefinedMetalArmorSchematic3,
        materials={
            ItemId.ColdResistantRefinedMetalArmorSchematic2: 5,
        },
    ),
    ItemId.ColdResistantRefinedMetalArmorSchematic4: Recipe(
        product=ItemId.ColdResistantRefinedMetalArmorSchematic4,
        materials={
            ItemId.ColdResistantRefinedMetalArmorSchematic3: 5,
        },
    ),
    ItemId.PalMetalArmorSchematic2: Recipe(
        product=ItemId.PalMetalArmorSchematic2,
        materials={
            ItemId.PalMetalArmorSchematic1: 5,
        },
    ),
    ItemId.PalMetalArmorSchematic3: Recipe(
        product=ItemId.PalMetalArmorSchematic3,
        materials={
            ItemId.PalMetalArmorSchematic2: 5,
        },
    ),
    ItemId.PalMetalArmorSchematic4: Recipe(
        product=ItemId.PalMetalArmorSchematic4,
        materials={
            ItemId.PalMetalArmorSchematic3: 5,
        },
    ),
    ItemId.HeatResistantPalMetalArmorSchematic2: Recipe(
        product=ItemId.HeatResistantPalMetalArmorSchematic2,
        materials={
            ItemId.HeatResistantPalMetalArmorSchematic1: 5,
        },
    ),
    ItemId.HeatResistantPalMetalArmorSchematic3: Recipe(
        product=ItemId.HeatResistantPalMetalArmorSchematic3,
        materials={
            ItemId.HeatResistantPalMetalArmorSchematic2: 5,
        },
    ),
    ItemId.HeatResistantPalMetalArmorSchematic4: Recipe(
        product=ItemId.HeatResistantPalMetalArmorSchematic4,
        materials={
            ItemId.HeatResistantPalMetalArmorSchematic3: 5,
        },
    ),
    ItemId.ColdResistantPalMetalArmorSchematic2: Recipe(
        product=ItemId.ColdResistantPalMetalArmorSchematic2,
        materials={
            ItemId.ColdResistantPalMetalArmorSchematic1: 5,
        },
    ),
    ItemId.ColdResistantPalMetalArmorSchematic3: Recipe(
        product=ItemId.ColdResistantPalMetalArmorSchematic3,
        materials={
            ItemId.ColdResistantPalMetalArmorSchematic2: 5,
        },
    ),
    ItemId.ColdResistantPalMetalArmorSchematic4: Recipe(
        product=ItemId.ColdResistantPalMetalArmorSchematic4,
        materials={
            ItemId.ColdResistantPalMetalArmorSchematic3: 5,
        },
    ),
    ItemId.PlasteelArmorSchematic2: Recipe(
        product=ItemId.PlasteelArmorSchematic2,
        materials={
            ItemId.PlasteelArmorSchematic1: 5,
        },
    ),
    ItemId.PlasteelArmorSchematic3: Recipe(
        product=ItemId.PlasteelArmorSchematic3,
        materials={
            ItemId.PlasteelArmorSchematic2: 5,
        },
    ),
    ItemId.PlasteelArmorSchematic4: Recipe(
        product=ItemId.PlasteelArmorSchematic4,
        materials={
            ItemId.PlasteelArmorSchematic3: 5,
        },
    ),
    ItemId.HeatResistantPlasteelArmorSchematic2: Recipe(
        product=ItemId.HeatResistantPlasteelArmorSchematic2,
        materials={
            ItemId.HeatResistantPlasteelArmorSchematic1: 5,
        },
    ),
    ItemId.HeatResistantPlasteelArmorSchematic3: Recipe(
        product=ItemId.HeatResistantPlasteelArmorSchematic3,
        materials={
            ItemId.HeatResistantPlasteelArmorSchematic2: 5,
        },
    ),
    ItemId.HeatResistantPlasteelArmorSchematic4: Recipe(
        product=ItemId.HeatResistantPlasteelArmorSchematic4,
        materials={
            ItemId.HeatResistantPlasteelArmorSchematic3: 5,
        },
    ),
    ItemId.ColdResistantPlasteelArmorSchematic2: Recipe(
        product=ItemId.ColdResistantPlasteelArmorSchematic2,
        materials={
            ItemId.ColdResistantPlasteelArmorSchematic1: 5,
        },
    ),
    ItemId.ColdResistantPlasteelArmorSchematic3: Recipe(
        product=ItemId.ColdResistantPlasteelArmorSchematic3,
        materials={
            ItemId.ColdResistantPlasteelArmorSchematic2: 5,
        },
    ),
    ItemId.ColdResistantPlasteelArmorSchematic4: Recipe(
        product=ItemId.ColdResistantPlasteelArmorSchematic4,
        materials={
            ItemId.ColdResistantPlasteelArmorSchematic3: 5,
        },
    ),
    ItemId.LightweightPlasteelArmorSchematic2: Recipe(
        product=ItemId.LightweightPlasteelArmorSchematic2,
        materials={
            ItemId.LightweightPlasteelArmorSchematic1: 5,
        },
    ),
    ItemId.LightweightPlasteelArmorSchematic3: Recipe(
        product=ItemId.LightweightPlasteelArmorSchematic3,
        materials={
            ItemId.LightweightPlasteelArmorSchematic2: 5,
        },
    ),
    ItemId.LightweightPlasteelArmorSchematic4: Recipe(
        product=ItemId.LightweightPlasteelArmorSchematic4,
        materials={
            ItemId.LightweightPlasteelArmorSchematic3: 5,
        },
    ),
    ItemId.HexoliteArmorSchematic2: Recipe(
        product=ItemId.HexoliteArmorSchematic2,
        materials={
            ItemId.HexoliteArmorSchematic1: 5,
        },
    ),
    ItemId.HexoliteArmorSchematic3: Recipe(
        product=ItemId.HexoliteArmorSchematic3,
        materials={
            ItemId.HexoliteArmorSchematic2: 5,
        },
    ),
    ItemId.HexoliteArmorSchematic4: Recipe(
        product=ItemId.HexoliteArmorSchematic4,
        materials={
            ItemId.HexoliteArmorSchematic3: 5,
        },
    ),
    ItemId.HeatResistantHexoliteArmorSchematic2: Recipe(
        product=ItemId.HeatResistantHexoliteArmorSchematic2,
        materials={
            ItemId.HeatResistantHexoliteArmorSchematic1: 5,
        },
    ),
    ItemId.HeatResistantHexoliteArmorSchematic3: Recipe(
        product=ItemId.HeatResistantHexoliteArmorSchematic3,
        materials={
            ItemId.HeatResistantHexoliteArmorSchematic2: 5,
        },
    ),
    ItemId.HeatResistantHexoliteArmorSchematic4: Recipe(
        product=ItemId.HeatResistantHexoliteArmorSchematic4,
        materials={
            ItemId.HeatResistantHexoliteArmorSchematic3: 5,
        },
    ),
    ItemId.ColdResistantHexoliteArmorSchematic2: Recipe(
        product=ItemId.ColdResistantHexoliteArmorSchematic2,
        materials={
            ItemId.ColdResistantHexoliteArmorSchematic1: 5,
        },
    ),
    ItemId.ColdResistantHexoliteArmorSchematic3: Recipe(
        product=ItemId.ColdResistantHexoliteArmorSchematic3,
        materials={
            ItemId.ColdResistantHexoliteArmorSchematic2: 5,
        },
    ),
    ItemId.ColdResistantHexoliteArmorSchematic4: Recipe(
        product=ItemId.ColdResistantHexoliteArmorSchematic4,
        materials={
            ItemId.ColdResistantHexoliteArmorSchematic3: 5,
        },
    ),
    ItemId.LightweightHexoliteArmorSchematic2: Recipe(
        product=ItemId.LightweightHexoliteArmorSchematic2,
        materials={
            ItemId.LightweightHexoliteArmorSchematic1: 5,
        },
    ),
    ItemId.LightweightHexoliteArmorSchematic3: Recipe(
        product=ItemId.LightweightHexoliteArmorSchematic3,
        materials={
            ItemId.LightweightHexoliteArmorSchematic2: 5,
        },
    ),
    ItemId.LightweightHexoliteArmorSchematic4: Recipe(
        product=ItemId.LightweightHexoliteArmorSchematic4,
        materials={
            ItemId.LightweightHexoliteArmorSchematic3: 5,
        },
    ),
    ItemId.FeatheredHairBandSchematic2: Recipe(
        product=ItemId.FeatheredHairBandSchematic2,
        materials={
            ItemId.FeatheredHairBandSchematic1: 5,
        },
    ),
    ItemId.FeatheredHairBandSchematic3: Recipe(
        product=ItemId.FeatheredHairBandSchematic3,
        materials={
            ItemId.FeatheredHairBandSchematic2: 5,
        },
    ),
    ItemId.FeatheredHairBandSchematic4: Recipe(
        product=ItemId.FeatheredHairBandSchematic4,
        materials={
            ItemId.FeatheredHairBandSchematic3: 5,
        },
    ),
    ItemId.MetalHelmSchematic2: Recipe(
        product=ItemId.MetalHelmSchematic2,
        materials={
            ItemId.MetalHelmSchematic1: 5,
        },
    ),
    ItemId.MetalHelmSchematic3: Recipe(
        product=ItemId.MetalHelmSchematic3,
        materials={
            ItemId.MetalHelmSchematic2: 5,
        },
    ),
    ItemId.MetalHelmSchematic4: Recipe(
        product=ItemId.MetalHelmSchematic4,
        materials={
            ItemId.MetalHelmSchematic3: 5,
        },
    ),
    ItemId.RefinedMetalHelmSchematic2: Recipe(
        product=ItemId.RefinedMetalHelmSchematic2,
        materials={
            ItemId.RefinedMetalHelmSchematic1: 5,
        },
    ),
    ItemId.RefinedMetalHelmSchematic3: Recipe(
        product=ItemId.RefinedMetalHelmSchematic3,
        materials={
            ItemId.RefinedMetalHelmSchematic2: 5,
        },
    ),
    ItemId.RefinedMetalHelmSchematic4: Recipe(
        product=ItemId.RefinedMetalHelmSchematic4,
        materials={
            ItemId.RefinedMetalHelmSchematic3: 5,
        },
    ),
    ItemId.PalMetalHelmSchematic2: Recipe(
        product=ItemId.PalMetalHelmSchematic2,
        materials={
            ItemId.PalMetalHelmSchematic1: 5,
        },
    ),
    ItemId.PalMetalHelmSchematic3: Recipe(
        product=ItemId.PalMetalHelmSchematic3,
        materials={
            ItemId.PalMetalHelmSchematic2: 5,
        },
    ),
    ItemId.PalMetalHelmSchematic4: Recipe(
        product=ItemId.PalMetalHelmSchematic4,
        materials={
            ItemId.PalMetalHelmSchematic3: 5,
        },
    ),
    ItemId.PlasteelHelmetSchematic2: Recipe(
        product=ItemId.PlasteelHelmetSchematic2,
        materials={
            ItemId.PlasteelHelmetSchematic1: 5,
        },
    ),
    ItemId.PlasteelHelmetSchematic3: Recipe(
        product=ItemId.PlasteelHelmetSchematic3,
        materials={
            ItemId.PlasteelHelmetSchematic2: 5,
        },
    ),
    ItemId.PlasteelHelmetSchematic4: Recipe(
        product=ItemId.PlasteelHelmetSchematic4,
        materials={
            ItemId.PlasteelHelmetSchematic3: 5,
        },
    ),
    ItemId.HexoliteHelmetSchematic2: Recipe(
        product=ItemId.HexoliteHelmetSchematic2,
        materials={
            ItemId.HexoliteHelmetSchematic1: 5,
        },
    ),
    ItemId.HexoliteHelmetSchematic3: Recipe(
        product=ItemId.HexoliteHelmetSchematic3,
        materials={
            ItemId.HexoliteHelmetSchematic2: 5,
        },
    ),
    ItemId.HexoliteHelmetSchematic4: Recipe(
        product=ItemId.HexoliteHelmetSchematic4,
        materials={
            ItemId.HexoliteHelmetSchematic3: 5,
        },
    ),
    ItemId.HallowedMaskSchematic1: Recipe(
        product=ItemId.HallowedMaskSchematic1,
        materials={
            ItemId.HallowedMaskSchematic: 5,
        },
    ),
    ItemId.HallowedMaskSchematic2: Recipe(
        product=ItemId.HallowedMaskSchematic2,
        materials={
            ItemId.HallowedMaskSchematic1: 5,
        },
    ),
    ItemId.HallowedMaskSchematic3: Recipe(
        product=ItemId.HallowedMaskSchematic3,
        materials={
            ItemId.HallowedMaskSchematic2: 5,
        },
    ),
    ItemId.HallowedMaskSchematic4: Recipe(
        product=ItemId.HallowedMaskSchematic4,
        materials={
            ItemId.HallowedMaskSchematic3: 5,
        },
    ),
    ItemId.HallowedHeadgearSchematic1: Recipe(
        product=ItemId.HallowedHeadgearSchematic1,
        materials={
            ItemId.HallowedHeadgearSchematic: 5,
        },
    ),
    ItemId.HallowedHeadgearSchematic2: Recipe(
        product=ItemId.HallowedHeadgearSchematic2,
        materials={
            ItemId.HallowedHeadgearSchematic1: 5,
        },
    ),
    ItemId.HallowedHeadgearSchematic3: Recipe(
        product=ItemId.HallowedHeadgearSchematic3,
        materials={
            ItemId.HallowedHeadgearSchematic2: 5,
        },
    ),
    ItemId.HallowedHeadgearSchematic4: Recipe(
        product=ItemId.HallowedHeadgearSchematic4,
        materials={
            ItemId.HallowedHeadgearSchematic3: 5,
        },
    ),
    ItemId.HallowedHelmetSchematic1: Recipe(
        product=ItemId.HallowedHelmetSchematic1,
        materials={
            ItemId.HallowedHelmetSchematic: 5,
        },
    ),
    ItemId.HallowedHelmetSchematic2: Recipe(
        product=ItemId.HallowedHelmetSchematic2,
        materials={
            ItemId.HallowedHelmetSchematic1: 5,
        },
    ),
    ItemId.HallowedHelmetSchematic3: Recipe(
        product=ItemId.HallowedHelmetSchematic3,
        materials={
            ItemId.HallowedHelmetSchematic2: 5,
        },
    ),
    ItemId.HallowedHelmetSchematic4: Recipe(
        product=ItemId.HallowedHelmetSchematic4,
        materials={
            ItemId.HallowedHelmetSchematic3: 5,
        },
    ),
    ItemId.HallowedHoodSchematic1: Recipe(
        product=ItemId.HallowedHoodSchematic1,
        materials={
            ItemId.HallowedHoodSchematic: 5,
        },
    ),
    ItemId.HallowedHoodSchematic2: Recipe(
        product=ItemId.HallowedHoodSchematic2,
        materials={
            ItemId.HallowedHoodSchematic1: 5,
        },
    ),
    ItemId.HallowedHoodSchematic3: Recipe(
        product=ItemId.HallowedHoodSchematic3,
        materials={
            ItemId.HallowedHoodSchematic2: 5,
        },
    ),
    ItemId.HallowedHoodSchematic4: Recipe(
        product=ItemId.HallowedHoodSchematic4,
        materials={
            ItemId.HallowedHoodSchematic3: 5,
        },
    ),
    ItemId.HallowedPlateMailSchematic1: Recipe(
        product=ItemId.HallowedPlateMailSchematic1,
        materials={
            ItemId.HallowedPlateMailSchematic: 5,
        },
    ),
    ItemId.HallowedPlateMailSchematic2: Recipe(
        product=ItemId.HallowedPlateMailSchematic2,
        materials={
            ItemId.HallowedPlateMailSchematic1: 5,
        },
    ),
    ItemId.HallowedPlateMailSchematic3: Recipe(
        product=ItemId.HallowedPlateMailSchematic3,
        materials={
            ItemId.HallowedPlateMailSchematic2: 5,
        },
    ),
    ItemId.HallowedPlateMailSchematic4: Recipe(
        product=ItemId.HallowedPlateMailSchematic4,
        materials={
            ItemId.HallowedPlateMailSchematic3: 5,
        },
    ),
    ItemId.ElizabeeSStaff: Recipe(
        product=ItemId.ElizabeeSStaff,
        materials={
            ItemId.Wood: 1,
            ItemId.Honey: 1,
        },
    ),
    ItemId.BeegardeSSpear: Recipe(
        product=ItemId.BeegardeSSpear,
        materials={
            ItemId.Wood: 1,
            ItemId.Honey: 1,
        },
    ),
    ItemId.XenolordSHead: Recipe(
        product=ItemId.XenolordSHead,
        materials={
            ItemId.Ingot: 1,
        },
    ),
    ItemId.BeginnerFishingRodChillet: Recipe(
        product=ItemId.BeginnerFishingRodChillet,
        materials={
            ItemId.PaldiumFragment: 10,
            ItemId.PalFluids: 3,
            ItemId.Ingot: 8,
            ItemId.Fiber: 8,
        },
    ),
    ItemId.BeginnerFishingRodGumoss: Recipe(
        product=ItemId.BeginnerFishingRodGumoss,
        materials={
            ItemId.PaldiumFragment: 20,
            ItemId.PalFluids: 6,
            ItemId.Ingot: 16,
            ItemId.Fiber: 16,
            ItemId.CoralumOre: 3,
        },
    ),
    ItemId.IntermediateFishingRodCattiva: Recipe(
        product=ItemId.IntermediateFishingRodCattiva,
        materials={
            ItemId.PaldiumFragment: 30,
            ItemId.HighQualityPalOil: 10,
            ItemId.Cement: 10,
            ItemId.Fiber: 30,
        },
    ),
    ItemId.IntermediateFishingRodCroajiro: Recipe(
        product=ItemId.IntermediateFishingRodCroajiro,
        materials={
            ItemId.PaldiumFragment: 60,
            ItemId.HighQualityPalOil: 20,
            ItemId.Cement: 20,
            ItemId.Fiber: 60,
            ItemId.CoralumOre: 10,
        },
    ),
    ItemId.AdvancedFishingRodPengullet: Recipe(
        product=ItemId.AdvancedFishingRodPengullet,
        materials={
            ItemId.PaldiumFragment: 70,
            ItemId.HighQualityPalOil: 20,
            ItemId.PalMetalIngot: 15,
            ItemId.CarbonFiber: 30,
        },
    ),
    ItemId.AdvancedFishingRodDepresso: Recipe(
        product=ItemId.AdvancedFishingRodDepresso,
        materials={
            ItemId.PaldiumFragment: 140,
            ItemId.HighQualityPalOil: 40,
            ItemId.PalMetalIngot: 30,
            ItemId.CarbonFiber: 60,
            ItemId.CoralumIngot: 5,
        },
    ),
    ItemId.SimpleBait: Recipe(
        product=ItemId.SimpleBait,
        materials={
            ItemId.PalFluids: 2,
            ItemId.RedBerries: 4,
            ItemId.Flour: 2,
        },
    ),
    ItemId.HighQualityBait: Recipe(
        product=ItemId.HighQualityBait,
        materials={
            ItemId.PalFluids: 3,
            ItemId.Tomato: 4,
            ItemId.Flour: 3,
        },
    ),
    ItemId.DeluxeBait: Recipe(
        product=ItemId.DeluxeBait,
        materials={
            ItemId.HighQualityPalOil: 4,
            ItemId.Onion: 4,
            ItemId.Carrot: 3,
            ItemId.Flour: 4,
        },
    ),
    ItemId.BeginnerBait: Recipe(
        product=ItemId.BeginnerBait,
        materials={
            ItemId.PalFluids: 4,
            ItemId.RedBerries: 2,
            ItemId.Flour: 1,
        },
    ),
    ItemId.SweetBait: Recipe(
        product=ItemId.SweetBait,
        materials={
            ItemId.PalFluids: 4,
            ItemId.RedBerries: 2,
            ItemId.Flour: 1,
        },
    ),
    ItemId.LuckyBait: Recipe(
        product=ItemId.LuckyBait,
        materials={
            ItemId.PalFluids: 6,
            ItemId.Tomato: 5,
            ItemId.Flour: 3,
        },
    ),
    ItemId.QuickBait: Recipe(
        product=ItemId.QuickBait,
        materials={
            ItemId.PalFluids: 6,
            ItemId.Tomato: 5,
            ItemId.Flour: 3,
        },
    ),
    ItemId.AlluringBait: Recipe(
        product=ItemId.AlluringBait,
        materials={
            ItemId.HighQualityPalOil: 10,
            ItemId.CavernMushroom: 1,
            ItemId.Carrot: 3,
            ItemId.Flour: 5,
        },
    ),
    ItemId.RiskyBait: Recipe(
        product=ItemId.RiskyBait,
        materials={
            ItemId.HighQualityPalOil: 8,
            ItemId.CavernMushroom: 3,
            ItemId.Carrot: 3,
            ItemId.Flour: 5,
        },
    ),
    ItemId.FishingMagnet: Recipe(
        product=ItemId.FishingMagnet,
        materials={
            ItemId.Ingot: 1,
        },
    ),
    ItemId.PowerfulFishingMagnet: Recipe(
        product=ItemId.PowerfulFishingMagnet,
        materials={
            ItemId.Hexolite: 1,
        },
    ),
    ItemId.Excalibur: Recipe(
        product=ItemId.Excalibur,
        materials={
            ItemId.HallowedBar: 30,
        },
    ),
    ItemId.Excalibur1: Recipe(
        product=ItemId.Excalibur1,
        materials={
            ItemId.HallowedBar: 45,
        },
    ),
    ItemId.Excalibur2: Recipe(
        product=ItemId.Excalibur2,
        materials={
            ItemId.HallowedBar: 90,
        },
    ),
    ItemId.Excalibur3: Recipe(
        product=ItemId.Excalibur3,
        materials={
            ItemId.HallowedBar: 180,
        },
    ),
    ItemId.Excalibur4: Recipe(
        product=ItemId.Excalibur4,
        materials={
            ItemId.HallowedBar: 360,
        },
    ),
    ItemId.Terraprisma: Recipe(
        product=ItemId.Terraprisma,
        materials={
            ItemId.HallowedBar: 40,
            ItemId.PalMetalIngot: 20,
            ItemId.AncientCivilizationParts: 3,
        },
    ),
    ItemId.Terraprisma1: Recipe(
        product=ItemId.Terraprisma1,
        materials={
            ItemId.HallowedBar: 60,
            ItemId.PalMetalIngot: 30,
            ItemId.AncientCivilizationParts: 5,
        },
    ),
    ItemId.Terraprisma2: Recipe(
        product=ItemId.Terraprisma2,
        materials={
            ItemId.HallowedBar: 120,
            ItemId.PalMetalIngot: 60,
            ItemId.AncientCivilizationParts: 7,
        },
    ),
    ItemId.Terraprisma3: Recipe(
        product=ItemId.Terraprisma3,
        materials={
            ItemId.HallowedBar: 240,
            ItemId.PalMetalIngot: 120,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.Terraprisma4: Recipe(
        product=ItemId.Terraprisma4,
        materials={
            ItemId.HallowedBar: 480,
            ItemId.PalMetalIngot: 240,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.VortexBeater: Recipe(
        product=ItemId.VortexBeater,
        materials={
            ItemId.HallowedBar: 40,
            ItemId.PalMetalIngot: 20,
            ItemId.ElectricOrgan: 5,
        },
    ),
    ItemId.VortexBeater1: Recipe(
        product=ItemId.VortexBeater1,
        materials={
            ItemId.HallowedBar: 60,
            ItemId.PalMetalIngot: 30,
            ItemId.ElectricOrgan: 10,
        },
    ),
    ItemId.VortexBeater2: Recipe(
        product=ItemId.VortexBeater2,
        materials={
            ItemId.HallowedBar: 120,
            ItemId.PalMetalIngot: 60,
            ItemId.ElectricOrgan: 15,
        },
    ),
    ItemId.VortexBeater3: Recipe(
        product=ItemId.VortexBeater3,
        materials={
            ItemId.HallowedBar: 240,
            ItemId.PalMetalIngot: 120,
            ItemId.ElectricOrgan: 20,
        },
    ),
    ItemId.VortexBeater4: Recipe(
        product=ItemId.VortexBeater4,
        materials={
            ItemId.HallowedBar: 480,
            ItemId.PalMetalIngot: 240,
            ItemId.ElectricOrgan: 25,
        },
    ),
    ItemId.Nightglow: Recipe(
        product=ItemId.Nightglow,
        materials={
            ItemId.HallowedBar: 40,
            ItemId.PalMetalIngot: 20,
            ItemId.AncientCivilizationParts: 3,
        },
    ),
    ItemId.Nightglow1: Recipe(
        product=ItemId.Nightglow1,
        materials={
            ItemId.HallowedBar: 60,
            ItemId.PalMetalIngot: 30,
            ItemId.AncientCivilizationParts: 5,
        },
    ),
    ItemId.Nightglow2: Recipe(
        product=ItemId.Nightglow2,
        materials={
            ItemId.HallowedBar: 120,
            ItemId.PalMetalIngot: 60,
            ItemId.AncientCivilizationParts: 7,
        },
    ),
    ItemId.Nightglow3: Recipe(
        product=ItemId.Nightglow3,
        materials={
            ItemId.HallowedBar: 240,
            ItemId.PalMetalIngot: 120,
            ItemId.AncientCivilizationParts: 10,
        },
    ),
    ItemId.Nightglow4: Recipe(
        product=ItemId.Nightglow4,
        materials={
            ItemId.HallowedBar: 480,
            ItemId.PalMetalIngot: 240,
            ItemId.AncientCivilizationParts: 15,
        },
    ),
    ItemId.TerraBlade: Recipe(
        product=ItemId.TerraBlade,
        materials={
            ItemId.HallowedBar: 40,
            ItemId.PalMetalIngot: 20,
            ItemId.PredatorCore: 1,
        },
    ),
    ItemId.TerraBlade1: Recipe(
        product=ItemId.TerraBlade1,
        materials={
            ItemId.HallowedBar: 60,
            ItemId.PalMetalIngot: 30,
            ItemId.PredatorCore: 3,
        },
    ),
    ItemId.TerraBlade2: Recipe(
        product=ItemId.TerraBlade2,
        materials={
            ItemId.HallowedBar: 120,
            ItemId.PalMetalIngot: 60,
            ItemId.PredatorCore: 5,
        },
    ),
    ItemId.TerraBlade3: Recipe(
        product=ItemId.TerraBlade3,
        materials={
            ItemId.HallowedBar: 240,
            ItemId.PalMetalIngot: 120,
            ItemId.PredatorCore: 10,
        },
    ),
    ItemId.TerraBlade4: Recipe(
        product=ItemId.TerraBlade4,
        materials={
            ItemId.HallowedBar: 480,
            ItemId.PalMetalIngot: 240,
            ItemId.PredatorCore: 15,
        },
    ),
    ItemId.HallowedMask: Recipe(
        product=ItemId.HallowedMask,
        materials={
            ItemId.HallowedBar: 20,
        },
    ),
    ItemId.HallowedMask1: Recipe(
        product=ItemId.HallowedMask1,
        materials={
            ItemId.HallowedBar: 30,
        },
    ),
    ItemId.HallowedMask2: Recipe(
        product=ItemId.HallowedMask2,
        materials={
            ItemId.HallowedBar: 60,
        },
    ),
    ItemId.HallowedMask3: Recipe(
        product=ItemId.HallowedMask3,
        materials={
            ItemId.HallowedBar: 120,
        },
    ),
    ItemId.HallowedMask4: Recipe(
        product=ItemId.HallowedMask4,
        materials={
            ItemId.HallowedBar: 240,
        },
    ),
    ItemId.HallowedHeadgear: Recipe(
        product=ItemId.HallowedHeadgear,
        materials={
            ItemId.HallowedBar: 20,
        },
    ),
    ItemId.HallowedHeadgear1: Recipe(
        product=ItemId.HallowedHeadgear1,
        materials={
            ItemId.HallowedBar: 30,
        },
    ),
    ItemId.HallowedHeadgear2: Recipe(
        product=ItemId.HallowedHeadgear2,
        materials={
            ItemId.HallowedBar: 60,
        },
    ),
    ItemId.HallowedHeadgear3: Recipe(
        product=ItemId.HallowedHeadgear3,
        materials={
            ItemId.HallowedBar: 120,
        },
    ),
    ItemId.HallowedHeadgear4: Recipe(
        product=ItemId.HallowedHeadgear4,
        materials={
            ItemId.HallowedBar: 240,
        },
    ),
    ItemId.HallowedPlateMail: Recipe(
        product=ItemId.HallowedPlateMail,
        materials={
            ItemId.HallowedBar: 20,
        },
    ),
    ItemId.HallowedPlateMail1: Recipe(
        product=ItemId.HallowedPlateMail1,
        materials={
            ItemId.HallowedBar: 30,
        },
    ),
    ItemId.HallowedPlateMail2: Recipe(
        product=ItemId.HallowedPlateMail2,
        materials={
            ItemId.HallowedBar: 60,
        },
    ),
    ItemId.HallowedPlateMail3: Recipe(
        product=ItemId.HallowedPlateMail3,
        materials={
            ItemId.HallowedBar: 120,
        },
    ),
    ItemId.HallowedPlateMail4: Recipe(
        product=ItemId.HallowedPlateMail4,
        materials={
            ItemId.HallowedBar: 240,
        },
    ),
    ItemId.HallowedHelmet: Recipe(
        product=ItemId.HallowedHelmet,
        materials={
            ItemId.HallowedBar: 20,
        },
    ),
    ItemId.HallowedHelmet1: Recipe(
        product=ItemId.HallowedHelmet1,
        materials={
            ItemId.HallowedBar: 30,
        },
    ),
    ItemId.HallowedHelmet2: Recipe(
        product=ItemId.HallowedHelmet2,
        materials={
            ItemId.HallowedBar: 60,
        },
    ),
    ItemId.HallowedHelmet3: Recipe(
        product=ItemId.HallowedHelmet3,
        materials={
            ItemId.HallowedBar: 120,
        },
    ),
    ItemId.HallowedHelmet4: Recipe(
        product=ItemId.HallowedHelmet4,
        materials={
            ItemId.HallowedBar: 240,
        },
    ),
    ItemId.HallowedHood: Recipe(
        product=ItemId.HallowedHood,
        materials={
            ItemId.HallowedBar: 20,
        },
    ),
    ItemId.HallowedHood1: Recipe(
        product=ItemId.HallowedHood1,
        materials={
            ItemId.HallowedBar: 30,
        },
    ),
    ItemId.HallowedHood2: Recipe(
        product=ItemId.HallowedHood2,
        materials={
            ItemId.HallowedBar: 60,
        },
    ),
    ItemId.HallowedHood3: Recipe(
        product=ItemId.HallowedHood3,
        materials={
            ItemId.HallowedBar: 120,
        },
    ),
    ItemId.HallowedHood4: Recipe(
        product=ItemId.HallowedHood4,
        materials={
            ItemId.HallowedBar: 240,
        },
    ),
    ItemId.Meowmere: Recipe(
        product=ItemId.Meowmere,
        materials={
            ItemId.Ingot: 22,
            ItemId.PaldiumFragment: 22,
            ItemId.Coal: 22,
            ItemId.PredatorCore: 3,
        },
    ),
    ItemId.CelestialSigil: Recipe(
        product=ItemId.CelestialSigil,
        materials={
            ItemId.HallowedBar: 100,
        },
    ),
    ItemId.MoonLordMask: Recipe(
        product=ItemId.MoonLordMask,
        materials={
            ItemId.HallowedBar: 1,
        },
    ),
    ItemId.EyeOfCthulhuMask: Recipe(
        product=ItemId.EyeOfCthulhuMask,
        materials={
            ItemId.HallowedBar: 1,
        },
    ),
    ItemId.LegendaryMeowmere: Recipe(
        product=ItemId.LegendaryMeowmere,
        materials={
            ItemId.HallowedBar: 22,
            ItemId.PaldiumFragment: 22,
            ItemId.Coal: 22,
            ItemId.PredatorCore: 5,
        },
    ),
    ItemId.NutrientTonic: Recipe(
        product=ItemId.NutrientTonic,
        materials={
            ItemId.CottonCandy: 10,
            ItemId.Onion: 10,
            "None": 5,
        },
    ),
    ItemId.HartalisSaddle: Recipe(
        product=ItemId.HartalisSaddle,
        materials={
            ItemId.Leather: 100,
            ItemId.HighQualityCloth: 40,
            ItemId.CoralumIngot: 40,
            ItemId.PaldiumFragment: 200,
        },
    ),
    ItemId.ZoeSHalloweenCostume: Recipe(
        product=ItemId.ZoeSHalloweenCostume,
        materials={
            ItemId.Cloth: 5,
            ItemId.Leather: 5,
        },
    ),
    ItemId.DepressoHelmet: Recipe(
        product=ItemId.DepressoHelmet,
        materials={
            ItemId.HighQualityCloth: 5,
            ItemId.VenomGland: 25,
        },
    ),
    ItemId.DepressoArmor: Recipe(
        product=ItemId.DepressoArmor,
        materials={
            ItemId.HighQualityCloth: 15,
            ItemId.VenomGland: 75,
        },
    ),
    ItemId.HartalisSlab: Recipe(
        product=ItemId.HartalisSlab,
        materials={
            ItemId.HartalisSlabFragment: 4,
        },
    ),
    ItemId.HartalisUltraSlab: Recipe(
        product=ItemId.HartalisUltraSlab,
        materials={
            ItemId.HartalisUltraSlabFragment: 4,
        },
    ),
    ItemId.CrownOfSalvation: Recipe(
        product=ItemId.CrownOfSalvation,
        materials={
            ItemId.Ingot: 1,
        },
    ),
}

def has_recipe(product: ItemId | str) -> bool:
    return product in _ITEM_RECIPES

def get_recipe(product: ItemId) -> Recipe | None:
    recipe = _ITEM_RECIPES.get(product)
    if recipe is None:
        return None
    return Recipe(product=recipe.product, materials=dict(recipe.materials))

def get_recipes() -> dict[ItemId, Recipe]:
    return {
        product: Recipe(product=recipe.product, materials=dict(recipe.materials))
        for product, recipe in _ITEM_RECIPES.items()
    }

def get_recipe_materials(product: ItemId) -> dict[RecipeMaterialId, int] | None:
    recipe = get_recipe(product)
    if recipe is None:
        return None
    return dict(recipe.materials)
