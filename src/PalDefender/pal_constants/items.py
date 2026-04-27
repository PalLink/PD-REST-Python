from enum import Enum

class ItemId(str, Enum):
    GoldCoin = "Money"
    PalSphere = "PalSphere"
    MegaSphere = "PalSphere_Mega"
    GigaSphere = "PalSphere_Giga"
    HyperSphere = "PalSphere_Tera"
    UltraSphere = "PalSphere_Master"
    LegendarySphere = "PalSphere_Legend"
    UltimateSphere = "PalSphere_Ultimate"
    ExoticSphere = "PalSphere_Exotic"
    Arrow = "Arrow"
    PoisonArrow = "Arrow_Poison"
    FireArrow = "Arrow_Fire"
    ReinforcedArrow = "ReinforcedArrow"
    AdvancedArrow = "SFArrow"
    CoarseAmmo = "RoughBullet"
    HandgunAmmo = "HandgunBullet"
    MagnumAmmo = "MagnumBullet"
    RifleAmmo = "RifleBullet"
    ShotgunShell = "ShotgunBullet"
    MachineGunAmmo = "MachingunBullet"
    AssaultRifleAmmo = "AssaultRifleBullet"
    RocketAmmo = "ExplosiveBullet"
    DecalInk = "InkBullet"
    FlamethrowerFuel = "FlamethrowerBullet"
    MissileAmmo = "MissileBullet"
    GrenadeAmmo = "GrenadeBullet"
    GatlingGunAmmo = "GatlingBullet"
    MeteoriteAmmo = "MeteorBullet"
    EnergyCartridge = "LaserBullet"
    PlasmaCartridge = "EnergyLauncherBullet"
    LaserGatlingCartridge = "LaserGatlingBullet"
    ChargeRifleAmmo = "ChargeLaserRifleBullet"
    OverheatRifleAmmo = "OverheatRifleBullet"
    EnergyShotgunAmmo = "EnergyShotgunBullet"
    BoostGunAmmo = "PalDopingShotBullet"
    SimpleBait = "FishingBait_1"
    HighQualityBait = "FishingBait_2"
    DeluxeBait = "FishingBait_3"
    BeginnerBait = "FishingBait_1_A"
    SweetBait = "FishingBait_1_B"
    LuckyBait = "FishingBait_2_A"
    QuickBait = "FishingBait_2_B"
    AlluringBait = "FishingBait_3_A"
    RiskyBait = "FishingBait_3_B"
    WoodenClub = "Bat"
    HandHeldTorch = "Torch"
    Bat = "Bat2"
    StoneAxe = "Axe_Tier_00"
    MetalAxe = "Axe_Tier_01"
    RefinedMetalAxe = "Axe_Tier_02"
    Axe4 = "Axe_Tier_03"
    PalMetalAxe = "Axe_Steal"
    StonePickaxe = "Pickaxe_Tier_00"
    MetalPickaxe = "Pickaxe_Tier_01"
    RefinedMetalPickaxe = "Pickaxe_Tier_02"
    EnText2 = "Pickaxe_Tier_03"
    PalMetalPickaxe = "Pickaxe_Steal"
    StoneSpear = "Spear"
    MetalSpear = "Spear_2"
    RefinedMetalSpear = "Spear_3"
    ElizabeeSStaff = "Spear_QueenBee"
    BeegardeSSpear = "Spear_SoldierBee"
    LilySSpear = "Spear_ForestBoss"
    LilySSpear4 = "Spear_ForestBoss_5"
    Sword = "Sword"
    Sword1 = "Sword_2"
    Sword2 = "Sword_3"
    Sword3 = "Sword_4"
    Sword4 = "Sword_5"
    Katana = "Katana"
    Katana1 = "Katana_2"
    Katana2 = "Katana_3"
    Katana3 = "Katana_4"
    Katana4 = "Katana_5"
    BeamSword = "BeamSword"
    BeamSword1 = "BeamSword_2"
    BeamSword2 = "BeamSword_3"
    BeamSword3 = "BeamSword_4"
    BeamSword4 = "BeamSword_5"
    Meowmere = "YakushimaBlade"
    MeatCleaver = "MeatCutterKnife"
    StunBaton = "ElecBaton"
    MetalDetector = "MetalDetector"
    OldBow = "WeakerBow"
    OldBow1 = "WeakerBow_2"
    OldBow2 = "WeakerBow_3"
    OldBow3 = "WeakerBow_4"
    OldBow4 = "WeakerBow_5"
    PoisonBow = "Bow_Poison"
    FireBow = "Bow_Fire"
    ThreeShotBow = "Bow_Triple"
    FiveShotBow = "Bow_Fifth"
    Crossbow = "BowGun"
    Crossbow1 = "BowGun_2"
    Crossbow2 = "BowGun_3"
    Crossbow3 = "BowGun_4"
    Crossbow4 = "BowGun_5"
    PoisonArrowCrossbow = "BowGun_Poison"
    FireArrowCrossbow = "BowGun_Fire"
    PoisonArrowCrossbow1 = "BowGun_Poison_2"
    PoisonArrowCrossbow2 = "BowGun_Poison_3"
    PoisonArrowCrossbow3 = "BowGun_Poison_4"
    PoisonArrowCrossbow4 = "BowGun_Poison_5"
    FireArrowCrossbow1 = "BowGun_Fire_2"
    FireArrowCrossbow2 = "BowGun_Fire_3"
    FireArrowCrossbow3 = "BowGun_Fire_4"
    FireArrowCrossbow4 = "BowGun_Fire_5"
    CompoundBow = "CompoundBow"
    CompoundBow1 = "CompoundBow_2"
    CompoundBow2 = "CompoundBow_3"
    CompoundBow3 = "CompoundBow_4"
    CompoundBow4 = "CompoundBow_5"
    AdvancedBow = "SFBow"
    AdvancedBow1 = "SFBow_2"
    AdvancedBow2 = "SFBow_3"
    AdvancedBow3 = "SFBow_4"
    AdvancedBow4 = "SFBow_5"
    MakeshiftHandgun = "MakeshiftHandgun"
    MakeshiftHandgun1 = "MakeshiftHandgun_2"
    MakeshiftHandgun2 = "MakeshiftHandgun_3"
    MakeshiftHandgun3 = "MakeshiftHandgun_4"
    MakeshiftHandgun4 = "MakeshiftHandgun_5"
    Handgun = "HandGun_Default"
    Handgun1 = "HandGun_Default_2"
    Handgun2 = "HandGun_Default_3"
    Handgun3 = "HandGun_Default_4"
    Handgun4 = "HandGun_Default_5"
    DecalGun1 = "DecalGun_1"
    DecalGun2 = "DecalGun_2"
    DecalGun3 = "DecalGun_3"
    DecalGun4 = "DecalGun_4"
    DecalGun5 = "DecalGun_5"
    OldRevolver = "OldRevolver"
    OldRevolver1 = "OldRevolver_2"
    OldRevolver2 = "OldRevolver_3"
    OldRevolver3 = "OldRevolver_4"
    OldRevolver4 = "OldRevolver_5"
    BoostGun = "PalDopingShot"
    MegaboostGun = "PalDopingShot_2"
    BoostGun2 = "PalDopingShot_3"
    GrapplingGun = "GrapplingGun"
    MegaGrapplingGun = "GrapplingGun2"
    GigaGrapplingGun = "GrapplingGun3"
    HyperGrapplingGun = "GrapplingGun4"
    UltraGrapplingGun = "GrapplingGun5"
    UnknownItemHandgunShield = "HandgunShield"
    MakeshiftShotgun = "MakeshiftShotgun"
    MakeshiftShotgun1 = "MakeshiftShotgun_2"
    MakeshiftShotgun2 = "MakeshiftShotgun_3"
    MakeshiftShotgun3 = "MakeshiftShotgun_4"
    MakeshiftShotgun4 = "MakeshiftShotgun_5"
    DoubleBarreledShotgun = "DoubleBarrelShotgun"
    DoubleBarreledShotgun1 = "DoubleBarrelShotgun_2"
    DoubleBarreledShotgun2 = "DoubleBarrelShotgun_3"
    DoubleBarreledShotgun3 = "DoubleBarrelShotgun_4"
    DoubleBarreledShotgun4 = "DoubleBarrelShotgun_5"
    PumpActionShotgun = "PumpActionShotgun"
    PumpActionShotgun1 = "PumpActionShotgun_2"
    PumpActionShotgun2 = "PumpActionShotgun_3"
    PumpActionShotgun3 = "PumpActionShotgun_4"
    PumpActionShotgun4 = "PumpActionShotgun_5"
    SemiAutoShotgun = "SemiAutoShotgun"
    SemiAutoShotgun1 = "SemiAutoShotgun_2"
    SemiAutoShotgun2 = "SemiAutoShotgun_3"
    SemiAutoShotgun3 = "SemiAutoShotgun_4"
    SemiAutoShotgun4 = "SemiAutoShotgun_5"
    EnergyShotgun = "EnergyShotgun"
    EnergyShotgun1 = "EnergyShotgun_2"
    EnergyShotgun2 = "EnergyShotgun_3"
    EnergyShotgun3 = "EnergyShotgun_4"
    EnergyShotgun4 = "EnergyShotgun_5"
    Musket = "Musket"
    Musket1 = "Musket_2"
    Musket2 = "Musket_3"
    Musket3 = "Musket_4"
    Musket4 = "Musket_5"
    SingleShotRifle = "SingleShotRifle"
    SingleShotRifle1 = "SingleShotRifle_2"
    SingleShotRifle2 = "SingleShotRifle_3"
    SingleShotRifle3 = "SingleShotRifle_4"
    SingleShotRifle4 = "SingleShotRifle_5"
    SemiAutoRifle = "SemiAutoRifle"
    SemiAutoRifle1 = "SemiAutoRifle_2"
    SemiAutoRifle2 = "SemiAutoRifle_3"
    SemiAutoRifle3 = "SemiAutoRifle_4"
    SemiAutoRifle4 = "SemiAutoRifle_5"
    MakeshiftAssaultRifle = "MakeshiftAssaultRifle"
    MakeshiftAssaultRifle1 = "MakeshiftAssaultRifle_2"
    MakeshiftAssaultRifle2 = "MakeshiftAssaultRifle_3"
    MakeshiftAssaultRifle3 = "MakeshiftAssaultRifle_4"
    MakeshiftAssaultRifle4 = "MakeshiftAssaultRifle_5"
    AssaultRifle = "AssaultRifle_Default1"
    AssaultRifle1 = "AssaultRifle_Default2"
    AssaultRifle2 = "AssaultRifle_Default3"
    AssaultRifle3 = "AssaultRifle_Default4"
    AssaultRifle4 = "AssaultRifle_Default5"
    MakeshiftSMG = "MakeshiftSubmachineGun"
    MakeshiftSMG1 = "MakeshiftSubmachineGun_2"
    MakeshiftSMG2 = "MakeshiftSubmachineGun_3"
    MakeshiftSMG3 = "MakeshiftSubmachineGun_4"
    MakeshiftSMG4 = "MakeshiftSubmachineGun_5"
    SMG = "SubmachineGun"
    SMG1 = "SubmachineGun_2"
    SMG2 = "SubmachineGun_3"
    SMG3 = "SubmachineGun_4"
    SMG4 = "SubmachineGun_5"
    MeteorLauncher = "Launcher_Meteor"
    MeteorLauncher4 = "Launcher_Meteor_5"
    RocketLauncher = "Launcher_Default"
    EnText46 = "Launcher_Meat"
    RocketLauncher1 = "Launcher_Default_2"
    RocketLauncher2 = "Launcher_Default_3"
    RocketLauncher3 = "Launcher_Default_4"
    RocketLauncher4 = "Launcher_Default_5"
    SingleShotSphereLauncher = "SphereLauncher_Once"
    ScatterSphereLauncher = "SphereLauncher"
    HomingSphereLauncher = "HomingSphereLauncher"
    LaserRifle = "LaserRifle"
    LaserRifle1 = "LaserRifle_2"
    LaserRifle2 = "LaserRifle_3"
    LaserRifle3 = "LaserRifle_4"
    LaserRifle4 = "LaserRifle_5"
    ChargeRifle = "ChargeLaserRifle"
    OverheatRifle = "OverheatRifle"
    ChargeRifle1 = "ChargeLaserRifle_2"
    ChargeRifle2 = "ChargeLaserRifle_3"
    ChargeRifle3 = "ChargeLaserRifle_4"
    ChargeRifle4 = "ChargeLaserRifle_5"
    OverheatRifle1 = "OverheatRifle_2"
    OverheatRifle2 = "OverheatRifle_3"
    OverheatRifle3 = "OverheatRifle_4"
    OverheatRifle4 = "OverheatRifle_5"
    Flamethrower = "FlameThrower"
    Flamethrower1 = "FlameThrower_2"
    Flamethrower2 = "FlameThrower_3"
    Flamethrower3 = "FlameThrower_4"
    Flamethrower4 = "FlameThrower_5"
    GatlingGun = "GatlingGun"
    GatlingGun1 = "GatlingGun_2"
    GatlingGun2 = "GatlingGun_3"
    GatlingGun3 = "GatlingGun_4"
    GatlingGun4 = "GatlingGun_5"
    LaserGatlingGun = "LaserGatlingGun"
    LaserGatlingGun1 = "LaserGatlingGun_2"
    LaserGatlingGun2 = "LaserGatlingGun_3"
    LaserGatlingGun3 = "LaserGatlingGun_4"
    LaserGatlingGun4 = "LaserGatlingGun_5"
    GrenadeLauncher = "GrenadeLauncher"
    GrenadeLauncher1 = "GrenadeLauncher_2"
    GrenadeLauncher2 = "GrenadeLauncher_3"
    GrenadeLauncher3 = "GrenadeLauncher_4"
    GrenadeLauncher4 = "GrenadeLauncher_5"
    GuidedMissileLauncher = "GuidedMissileLauncher"
    GuidedMissileLauncher1 = "GuidedMissileLauncher_2"
    GuidedMissileLauncher2 = "GuidedMissileLauncher_3"
    GuidedMissileLauncher3 = "GuidedMissileLauncher_4"
    GuidedMissileLauncher4 = "GuidedMissileLauncher_5"
    MultiGuidedMissileLauncher = "MultiGuidedMissileLauncher"
    MultiGuidedMissileLauncher1 = "MultiGuidedMissileLauncher_2"
    MultiGuidedMissileLauncher2 = "MultiGuidedMissileLauncher_3"
    MultiGuidedMissileLauncher3 = "MultiGuidedMissileLauncher_4"
    MultiGuidedMissileLauncher4 = "MultiGuidedMissileLauncher_5"
    PlasmaCannon = "EnergyRocketLauncher"
    PlasmaCannon1 = "EnergyRocketLauncher_2"
    PlasmaCannon2 = "EnergyRocketLauncher_3"
    PlasmaCannon3 = "EnergyRocketLauncher_4"
    PlasmaCannon4 = "EnergyRocketLauncher_5"
    Excalibur = "YakushimaBlade004"
    Excalibur1 = "YakushimaBlade004_2"
    Excalibur2 = "YakushimaBlade004_3"
    Excalibur3 = "YakushimaBlade004_4"
    Excalibur4 = "YakushimaBlade004_5"
    TerraBlade = "YakushimaBlade002"
    TerraBlade1 = "YakushimaBlade002_2"
    TerraBlade2 = "YakushimaBlade002_3"
    TerraBlade3 = "YakushimaBlade002_4"
    TerraBlade4 = "YakushimaBlade002_5"
    VortexBeater = "YakushimaGun001"
    VortexBeater1 = "YakushimaGun001_2"
    VortexBeater2 = "YakushimaGun001_3"
    VortexBeater3 = "YakushimaGun001_4"
    VortexBeater4 = "YakushimaGun001_5"
    Nightglow = "YakushimaLantern001"
    Nightglow1 = "YakushimaLantern001_2"
    Nightglow2 = "YakushimaLantern001_3"
    Nightglow3 = "YakushimaLantern001_4"
    Nightglow4 = "YakushimaLantern001_5"
    Terraprisma = "YakushimaBlade003"
    Terraprisma1 = "YakushimaBlade003_2"
    Terraprisma2 = "YakushimaBlade003_3"
    Terraprisma3 = "YakushimaBlade003_4"
    Terraprisma4 = "YakushimaBlade003_5"
    LegendaryMeowmere = "YakushimaBlade005"
    MarksmanRevolver = "OctaviaRevolver"
    MarksmanRevolver1 = "OctaviaRevolver_2"
    MarksmanRevolver2 = "OctaviaRevolver_3"
    MarksmanRevolver3 = "OctaviaRevolver_4"
    MarksmanRevolver4 = "OctaviaRevolver_5"
    CoreEjectShotgun = "OctaviaShotgun"
    CoreEjectShotgun1 = "OctaviaShotgun_2"
    CoreEjectShotgun2 = "OctaviaShotgun_3"
    CoreEjectShotgun3 = "OctaviaShotgun_4"
    CoreEjectShotgun4 = "OctaviaShotgun_5"
    BeginnerFishingRodChillet = "FishingRod_01_1"
    BeginnerFishingRodGumoss = "FishingRod_01_2"
    IntermediateFishingRodCattiva = "FishingRod_02_1"
    IntermediateFishingRodCroajiro = "FishingRod_02_2"
    AdvancedFishingRodPengullet = "FishingRod_03_1"
    AdvancedFishingRodDepresso = "FishingRod_03_2"
    FragGrenade = "FragGrenade"
    ShockGrenade = "FragGrenade_Elec"
    IceGrenade = "FragGrenade_Ice"
    IncendiaryGrenade = "FragGrenade_Fire"
    WaterGrenade = "FragGrenade_Water"
    GrassGrenade = "FragGrenade_Leaf"
    GroundGrenade = "FragGrenade_Ground"
    DarkGrenade = "FragGrenade_Dark"
    DragonGrenade = "FragGrenade_Dragon"
    FragGrenadeMk2 = "FragGrenade_Super"
    PalRecoveryGrenade = "PalHealingGrenade"
    CommonShield = "Shield_01"
    MegaShield = "Shield_02"
    GigaShield = "Shield_03"
    HyperShield = "Shield_04"
    EnText4 = "Shield_05"
    UltraShield = "Shield_Ultra"
    AdvancedShield = "Shield_SF"
    ClothOutfit = "ClothArmor"
    ClothOutfit1 = "ClothArmor_2"
    ClothOutfit2 = "ClothArmor_3"
    ClothOutfit3 = "ClothArmor_4"
    ClothOutfit4 = "ClothArmor_5"
    TropicalOutfit = "ClothArmorHeat"
    TropicalOutfit1 = "ClothArmorHeat_2"
    TropicalOutfit2 = "ClothArmorHeat_3"
    TropicalOutfit3 = "ClothArmorHeat_4"
    TropicalOutfit4 = "ClothArmorHeat_5"
    TundraOutfit = "ClothArmorCold"
    TundraOutfit1 = "ClothArmorCold_2"
    TundraOutfit2 = "ClothArmorCold_3"
    TundraOutfit3 = "ClothArmorCold_4"
    TundraOutfit4 = "ClothArmorCold_5"
    PeltArmor = "FurArmor"
    PeltArmor1 = "FurArmor_2"
    PeltArmor2 = "FurArmor_3"
    PeltArmor3 = "FurArmor_4"
    PeltArmor4 = "FurArmor_5"
    HeatResistantPeltArmor = "FurArmorHeat"
    HeatResistantPeltArmor1 = "FurArmorHeat_2"
    HeatResistantPeltArmor2 = "FurArmorHeat_3"
    HeatResistantPeltArmor3 = "FurArmorHeat_4"
    HeatResistantPeltArmor4 = "FurArmorHeat_5"
    ColdResistantPeltArmor = "FurArmorCold"
    ColdResistantPeltArmor1 = "FurArmorCold_2"
    ColdResistantPeltArmor2 = "FurArmorCold_3"
    ColdResistantPeltArmor3 = "FurArmorCold_4"
    ColdResistantPeltArmor4 = "FurArmorCold_5"
    MetalArmor = "CopperArmor"
    MetalArmor1 = "CopperArmor_2"
    MetalArmor2 = "CopperArmor_3"
    MetalArmor3 = "CopperArmor_4"
    MetalArmor4 = "CopperArmor_5"
    HeatResistantMetalArmor = "CopperArmorHeat"
    HeatResistantMetalArmor1 = "CopperArmorHeat_2"
    HeatResistantMetalArmor2 = "CopperArmorHeat_3"
    HeatResistantMetalArmor3 = "CopperArmorHeat_4"
    HeatResistantMetalArmor4 = "CopperArmorHeat_5"
    ColdResistantMetalArmor = "CopperArmorCold"
    ColdResistantMetalArmor1 = "CopperArmorCold_2"
    ColdResistantMetalArmor2 = "CopperArmorCold_3"
    ColdResistantMetalArmor3 = "CopperArmorCold_4"
    ColdResistantMetalArmor4 = "CopperArmorCold_5"
    RefinedMetalArmor = "IronArmor"
    RefinedMetalArmor1 = "IronArmor_2"
    RefinedMetalArmor2 = "IronArmor_3"
    RefinedMetalArmor3 = "IronArmor_4"
    RefinedMetalArmor4 = "IronArmor_5"
    HeatResistantRefinedMetalArmor = "IronArmorHeat"
    HeatResistantRefinedMetalArmor1 = "IronArmorHeat_2"
    HeatResistantRefinedMetalArmor2 = "IronArmorHeat_3"
    HeatResistantRefinedMetalArmor3 = "IronArmorHeat_4"
    HeatResistantRefinedMetalArmor4 = "IronArmorHeat_5"
    ColdResistantRefinedMetalArmor = "IronArmorCold"
    ColdResistantRefinedMetalArmor1 = "IronArmorCold_2"
    ColdResistantRefinedMetalArmor2 = "IronArmorCold_3"
    ColdResistantRefinedMetalArmor3 = "IronArmorCold_4"
    ColdResistantRefinedMetalArmor4 = "IronArmorCold_5"
    PalMetalArmor = "StealArmor"
    PalMetalArmor1 = "StealArmor_2"
    PalMetalArmor2 = "StealArmor_3"
    PalMetalArmor3 = "StealArmor_4"
    PalMetalArmor4 = "StealArmor_5"
    HeatResistantPalMetalArmor = "StealArmorHeat"
    HeatResistantPalMetalArmor1 = "StealArmorHeat_2"
    HeatResistantPalMetalArmor2 = "StealArmorHeat_3"
    HeatResistantPalMetalArmor3 = "StealArmorHeat_4"
    HeatResistantPalMetalArmor4 = "StealArmorHeat_5"
    ColdResistantPalMetalArmor = "StealArmorCold"
    ColdResistantPalMetalArmor1 = "StealArmorCold_2"
    ColdResistantPalMetalArmor2 = "StealArmorCold_3"
    ColdResistantPalMetalArmor3 = "StealArmorCold_4"
    ColdResistantPalMetalArmor4 = "StealArmorCold_5"
    PlasteelArmor = "PlasticArmor"
    HeatResistantPlasteelArmor = "PlasticArmorHeat"
    ColdResistantPlasteelArmor = "PlasticArmorCold"
    LightweightPlasteelArmor = "PlasticArmorWeight"
    PlasteelArmor1 = "PlasticArmor_2"
    PlasteelArmor2 = "PlasticArmor_3"
    PlasteelArmor3 = "PlasticArmor_4"
    PlasteelArmor4 = "PlasticArmor_5"
    HeatResistantPlasteelArmor1 = "PlasticArmorHeat_2"
    HeatResistantPlasteelArmor2 = "PlasticArmorHeat_3"
    HeatResistantPlasteelArmor3 = "PlasticArmorHeat_4"
    HeatResistantPlasteelArmor4 = "PlasticArmorHeat_5"
    ColdResistantPlasteelArmor1 = "PlasticArmorCold_2"
    ColdResistantPlasteelArmor2 = "PlasticArmorCold_3"
    ColdResistantPlasteelArmor3 = "PlasticArmorCold_4"
    ColdResistantPlasteelArmor4 = "PlasticArmorCold_5"
    LightweightPlasteelArmor1 = "PlasticArmorWeight_2"
    LightweightPlasteelArmor2 = "PlasticArmorWeight_3"
    LightweightPlasteelArmor3 = "PlasticArmorWeight_4"
    LightweightPlasteelArmor4 = "PlasticArmorWeight_5"
    HexoliteArmor = "SFArmor"
    HexoliteArmor1 = "SFArmor_2"
    HexoliteArmor2 = "SFArmor_3"
    HexoliteArmor3 = "SFArmor_4"
    HexoliteArmor4 = "SFArmor_5"
    HeatResistantHexoliteArmor = "SFArmorHeat"
    HeatResistantHexoliteArmor1 = "SFArmorHeat_2"
    HeatResistantHexoliteArmor2 = "SFArmorHeat_3"
    HeatResistantHexoliteArmor3 = "SFArmorHeat_4"
    HeatResistantHexoliteArmor4 = "SFArmorHeat_5"
    ColdResistantHexoliteArmor = "SFArmorCold"
    ColdResistantHexoliteArmor1 = "SFArmorCold_2"
    ColdResistantHexoliteArmor2 = "SFArmorCold_3"
    ColdResistantHexoliteArmor3 = "SFArmorCold_4"
    ColdResistantHexoliteArmor4 = "SFArmorCold_5"
    LightweightHexoliteArmor = "SFArmorWeight"
    LightweightHexoliteArmor1 = "SFArmorWeight_2"
    LightweightHexoliteArmor2 = "SFArmorWeight_3"
    LightweightHexoliteArmor3 = "SFArmorWeight_4"
    LightweightHexoliteArmor4 = "SFArmorWeight_5"
    HallowedPlateMail = "YakushimaArmor001"
    HallowedPlateMail1 = "YakushimaArmor001_2"
    HallowedPlateMail2 = "YakushimaArmor001_3"
    HallowedPlateMail3 = "YakushimaArmor001_4"
    HallowedPlateMail4 = "YakushimaArmor001_5"
    DepressoArmor = "Player_Outfit_Kigurumi001"
    V1Armor = "Octavia001_Armor"
    V1Armor4 = "Octavia001_Armor_5"
    V2Armor = "Octavia002_Armor"
    V2Armor4 = "Octavia002_Armor_5"
    FeatheredHairBand = "FurHelmet"
    FeatheredHairBand1 = "FurHelmet_2"
    FeatheredHairBand2 = "FurHelmet_3"
    FeatheredHairBand3 = "FurHelmet_4"
    FeatheredHairBand4 = "FurHelmet_5"
    MetalHelm = "CopperHelmet"
    MetalHelm1 = "CopperHelmet_2"
    MetalHelm2 = "CopperHelmet_3"
    MetalHelm3 = "CopperHelmet_4"
    MetalHelm4 = "CopperHelmet_5"
    RefinedMetalHelm = "IronHelmet"
    RefinedMetalHelm1 = "IronHelmet_2"
    RefinedMetalHelm2 = "IronHelmet_3"
    RefinedMetalHelm3 = "IronHelmet_4"
    RefinedMetalHelm4 = "IronHelmet_5"
    PalMetalHelm = "StealHelmet"
    PalMetalHelm1 = "StealHelmet_2"
    PalMetalHelm2 = "StealHelmet_3"
    PalMetalHelm3 = "StealHelmet_4"
    PalMetalHelm4 = "StealHelmet_5"
    PlasteelHelmet = "PlasticHelmet"
    PlasteelHelmet1 = "PlasticHelmet_2"
    PlasteelHelmet2 = "PlasticHelmet_3"
    PlasteelHelmet3 = "PlasticHelmet_4"
    HexoliteHelmet = "SFHelmet"
    PlasteelHelmet4 = "PlasticHelmet_5"
    HexoliteHelmet1 = "SFHelmet_2"
    HexoliteHelmet2 = "SFHelmet_3"
    HexoliteHelmet3 = "SFHelmet_4"
    HexoliteHelmet4 = "SFHelmet_5"
    HallowedMask = "YakushimaHeadEquip001"
    HallowedMask1 = "YakushimaHeadEquip001_2"
    HallowedMask2 = "YakushimaHeadEquip001_3"
    HallowedMask3 = "YakushimaHeadEquip001_4"
    HallowedMask4 = "YakushimaHeadEquip001_5"
    HallowedHelmet = "YakushimaHeadEquip003"
    HallowedHelmet1 = "YakushimaHeadEquip003_2"
    HallowedHelmet2 = "YakushimaHeadEquip003_3"
    HallowedHelmet3 = "YakushimaHeadEquip003_4"
    HallowedHelmet4 = "YakushimaHeadEquip003_5"
    HallowedHeadgear = "YakushimaHeadEquip002"
    HallowedHeadgear1 = "YakushimaHeadEquip002_2"
    HallowedHeadgear2 = "YakushimaHeadEquip002_3"
    HallowedHeadgear3 = "YakushimaHeadEquip002_4"
    HallowedHeadgear4 = "YakushimaHeadEquip002_5"
    HallowedHood = "YakushimaHeadEquip004"
    HallowedHood1 = "YakushimaHeadEquip004_2"
    HallowedHood2 = "YakushimaHeadEquip004_3"
    HallowedHood3 = "YakushimaHeadEquip004_4"
    HallowedHood4 = "YakushimaHeadEquip004_5"
    MonarchSCrown = "Head001"
    MonarchSCrown1 = "Head001_2"
    MonarchSCrown2 = "Head001_3"
    MonarchSCrown3 = "Head001_4"
    MonarchSCrown4 = "Head001_5"
    GoldenCrown = "Head002"
    GoldenCrown1 = "Head002_2"
    GoldenCrown2 = "Head002_3"
    GoldenCrown3 = "Head002_4"
    GoldenCrown4 = "Head002_5"
    LongEaredHeadband = "Head003"
    LongEaredHeadband1 = "Head003_2"
    LongEaredHeadband2 = "Head003_3"
    LongEaredHeadband3 = "Head003_4"
    LongEaredHeadband4 = "Head003_5"
    WitchHat = "Head004"
    WitchHat1 = "Head004_2"
    WitchHat2 = "Head004_3"
    WitchHat3 = "Head004_4"
    WitchHat4 = "Head004_5"
    SoftHat = "Head005"
    SoftHat1 = "Head005_2"
    SoftHat2 = "Head005_3"
    SoftHat3 = "Head005_4"
    SoftHat4 = "Head005_5"
    Helmet = "Head006"
    Helmet1 = "Head006_2"
    Helmet2 = "Head006_3"
    Helmet3 = "Head006_4"
    Helmet4 = "Head006_5"
    SilkHat = "Head007"
    SilkHat1 = "Head007_2"
    SilkHat2 = "Head007_3"
    SilkHat3 = "Head007_4"
    SilkHat4 = "Head007_5"
    Tricorne = "Head008"
    Tricorne1 = "Head008_2"
    Tricorne2 = "Head008_3"
    Tricorne3 = "Head008_4"
    Tricorne4 = "Head008_5"
    ExplorerCap = "Head009"
    ExplorerCap1 = "Head009_2"
    ExplorerCap2 = "Head009_3"
    ExplorerCap3 = "Head009_4"
    ExplorerCap4 = "Head009_5"
    GraduationCap = "Head010"
    GraduationCap1 = "Head010_2"
    GraduationCap2 = "Head010_3"
    GraduationCap3 = "Head010_4"
    GraduationCap4 = "Head010_5"
    FarmingHat = "Head011"
    FarmingHat1 = "Head011_2"
    FarmingHat2 = "Head011_3"
    FarmingHat3 = "Head011_4"
    FarmingHat4 = "Head011_5"
    BowlerHat = "Head012"
    BowlerHat1 = "Head012_2"
    BowlerHat2 = "Head012_3"
    BowlerHat3 = "Head012_4"
    BowlerHat4 = "Head012_5"
    TocotocoCap = "Head013"
    TocotocoCap1 = "Head013_2"
    TocotocoCap2 = "Head013_3"
    TocotocoCap3 = "Head013_4"
    TocotocoCap4 = "Head013_5"
    GrinningTocotocoCap = "Head014"
    GrinningTocotocoCap1 = "Head014_2"
    GrinningTocotocoCap2 = "Head014_3"
    GrinningTocotocoCap3 = "Head014_4"
    GrinningTocotocoCap4 = "Head014_5"
    GumossCap = "Head015"
    GumossCap1 = "Head015_2"
    GumossCap2 = "Head015_3"
    GumossCap3 = "Head015_4"
    GumossCap4 = "Head015_5"
    PenkingCap = "Head016"
    PenkingCap1 = "Head016_2"
    PenkingCap2 = "Head016_3"
    PenkingCap3 = "Head016_4"
    PenkingCap4 = "Head016_5"
    KatressCap = "Head017"
    KatressCap1 = "Head017_2"
    KatressCap2 = "Head017_3"
    KatressCap3 = "Head017_4"
    KatressCap4 = "Head017_5"
    LyleenFloralCap = "HeadEquip023"
    SibelyxHat = "HeadEquip024"
    LeezpunkHood = "HeadEquip025"
    LeezpunkHood1 = "HeadEquip025_2"
    LeezpunkHood2 = "HeadEquip025_3"
    LeezpunkHood3 = "HeadEquip025_4"
    LeezpunkHood4 = "HeadEquip025_5"
    KillamariCap = "HeadEquip026"
    KillamariCap1 = "HeadEquip026_2"
    KillamariCap2 = "HeadEquip026_3"
    KillamariCap3 = "HeadEquip026_4"
    KillamariCap4 = "HeadEquip026_5"
    CawgnitoHat = "HeadEquip027"
    RibbunyHeadband = "HeadEquip028"
    RibbunyHeadband1 = "HeadEquip028_2"
    RibbunyHeadband2 = "HeadEquip028_3"
    RibbunyHeadband3 = "HeadEquip028_4"
    RibbunyHeadband4 = "HeadEquip028_5"
    LamballHelm = "HeadEquip029"
    DumudHelm = "HeadEquip030"
    SweeCap = "HeadEquip031"
    SweeCap1 = "HeadEquip031_2"
    SweeCap2 = "HeadEquip031_3"
    SweeCap3 = "HeadEquip031_4"
    SweeCap4 = "HeadEquip031_5"
    DazziHat = "HeadEquip032"
    DazziHat1 = "HeadEquip032_2"
    DazziHat2 = "HeadEquip032_3"
    DazziHat3 = "HeadEquip032_4"
    DazziHat4 = "HeadEquip032_5"
    CattivaHat = "HeadEquip033"
    WitchSCrown = "HeadEquip001_purple"
    HornsOfSupremacy = "HeadEquip041"
    XenolordSHead = "HeadEquip044"
    MoonLordMask = "YakushimaHeadEquip005"
    CrownOfSalvation = "HeadEquip046"
    ZoeHat = "GYM_Head_Grass"
    LilyHat = "GYM_Head_Forest"
    AxelHat = "GYM_Head_Electric"
    MarcusHat = "GYM_Head_Desert"
    VictorHat = "GYM_Head_Snow"
    SayaHat = "GYM_Head_Sakurajima"
    BjornHat = "GYM_Head_Viking"
    EyeOfCthulhuMask = "YakushimaHeadEquip006"
    DepressoHelmet = "HeadEquip045"
    LifePendant = "Accessory_HP_1"
    LifePendant1 = "Accessory_HP_2"
    LifePendant2 = "Accessory_HP_3"
    AttackPendant = "Accessory_AT_1"
    AttackPendant1 = "Accessory_AT_2"
    AttackPendant2 = "Accessory_AT_3"
    DefensePendant = "Accessory_defense_1"
    DefensePendant1 = "Accessory_defense_2"
    DefensePendant2 = "Accessory_defense_3"
    PendantOfDiligence = "Accessory_WorkSpeed_1"
    PendantOfDiligence1 = "Accessory_WorkSpeed_2"
    PendantOfDiligence2 = "Accessory_WorkSpeed_3"
    HeatResistantUndershirt = "Accessory_HeatResist_1"
    HeatResistantUndershirt1 = "Accessory_HeatResist_2"
    HeatResistantUndershirt2 = "Accessory_HeatResist_3"
    MulticlimateUndershirt = "Accessory_HeatColdResist_1"
    MulticlimateUndershirt1 = "Accessory_HeatColdResist_2"
    MulticlimateUndershirt2 = "Accessory_HeatColdResist_3"
    ThermalUndershirt = "Accessory_CoolResist_1"
    ThermalUndershirt1 = "Accessory_CoolResist_2"
    ThermalUndershirt2 = "Accessory_CoolResist_3"
    RingOfNeutralResistance = "Accessory_NormalResist_1"
    RingOfNeutralResistance1 = "Accessory_NormalResist_2"
    RingOfNeutralResistance2 = "Accessory_NormalResist_3"
    RingOfFireResistance = "Accessory_FireResist_1"
    RingOfFireResistance1 = "Accessory_FireResist_2"
    RingOfFireResistance2 = "Accessory_FireResist_3"
    RingOfWaterResistance = "Accessory_AquaResist_1"
    RingOfWaterResistance1 = "Accessory_AquaResist_2"
    RingOfWaterResistance2 = "Accessory_AquaResist_3"
    RingOfLightningResistance = "Accessory_ThunderResist_1"
    RingOfLightningResistance1 = "Accessory_ThunderResist_2"
    RingOfLightningResistance2 = "Accessory_ThunderResist_3"
    RingOfGrassResistance = "Accessory_LeafResist_1"
    RingOfGrassResistance1 = "Accessory_LeafResist_2"
    RingOfGrassResistance2 = "Accessory_LeafResist_3"
    RingOfIceResistance = "Accessory_IceResist_1"
    RingOfIceResistance1 = "Accessory_IceResist_2"
    RingOfIceResistance2 = "Accessory_IceResist_3"
    RingOfEarthResistance = "Accessory_EarthResist_1"
    RingOfEarthResistance1 = "Accessory_EarthResist_2"
    RingOfEarthResistance2 = "Accessory_EarthResist_3"
    RingOfDarkResistance = "Accessory_DarkResist_1"
    RingOfDarkResistance1 = "Accessory_DarkResist_2"
    RingOfDarkResistance2 = "Accessory_DarkResist_3"
    RingOfDragonResistance = "Accessory_DragonResist_1"
    RingOfDragonResistance1 = "Accessory_DragonResist_2"
    RingOfDragonResistance2 = "Accessory_DragonResist_3"
    RingOfMercy = "Accessory_Nonkilling"
    AbilityGlasses = "Accessory_TalentChecker"
    RingOfFreight = "Accessory_MaxWeightUp_01"
    RingOfFreight1 = "Accessory_MaxWeightUp_02"
    RingOfFreight2 = "Accessory_MaxWeightUp_03"
    AntiGravityBelt = "Accessory_JumpPower_Increase"
    DoubleJumpBoots = "Accessory_JumpCount_Increase1"
    TripleJumpBoots = "Accessory_JumpCount_Increase2"
    QuadrupleJumpBoots = "Accessory_JumpCount_Increase3"
    AirDashBoots = "Accessory_AirDash1"
    DoubleAirDashBoots = "Accessory_AirDash2"
    TripleAirDashBoots = "Accessory_AirDash3"
    QuadrupleAirDashBoots = "Accessory_AirDash4"
    NeutralSupportWhistle = "Otomo_ElementBoost_Normal_1"
    NeutralSupportWhistle1 = "Otomo_ElementBoost_Normal_2"
    NeutralSupportWhistle2 = "Otomo_ElementBoost_Normal_3"
    FireSupportWhistle = "Otomo_ElementBoost_Fire_1"
    FireSupportWhistle1 = "Otomo_ElementBoost_Fire_2"
    FireSupportWhistle2 = "Otomo_ElementBoost_Fire_3"
    WaterSupportWhistle = "Otomo_ElementBoost_Water_1"
    WaterSupportWhistle1 = "Otomo_ElementBoost_Water_2"
    WaterSupportWhistle2 = "Otomo_ElementBoost_Water_3"
    ElectricSupportWhistle = "Otomo_ElementBoost_Electricity_1"
    ElectricSupportWhistle1 = "Otomo_ElementBoost_Electricity_2"
    ElectricSupportWhistle2 = "Otomo_ElementBoost_Electricity_3"
    GrassSupportWhistle = "Otomo_ElementBoost_Leaf_1"
    GrassSupportWhistle1 = "Otomo_ElementBoost_Leaf_2"
    GrassSupportWhistle2 = "Otomo_ElementBoost_Leaf_3"
    IceSupportWhistle = "Otomo_ElementBoost_Ice_1"
    IceSupportWhistle1 = "Otomo_ElementBoost_Ice_2"
    IceSupportWhistle2 = "Otomo_ElementBoost_Ice_3"
    GroundSupportWhistle = "Otomo_ElementBoost_Earth_1"
    GroundSupportWhistle1 = "Otomo_ElementBoost_Earth_2"
    GroundSupportWhistle2 = "Otomo_ElementBoost_Earth_3"
    DarkSupportWhistle = "Otomo_ElementBoost_Dark_1"
    DarkSupportWhistle1 = "Otomo_ElementBoost_Dark_2"
    DarkSupportWhistle2 = "Otomo_ElementBoost_Dark_3"
    DragonSupportWhistle = "Otomo_ElementBoost_Dragon_1"
    DragonSupportWhistle1 = "Otomo_ElementBoost_Dragon_2"
    DragonSupportWhistle2 = "Otomo_ElementBoost_Dragon_3"
    AttackSupportWhistle = "Otomo_Attack_up1"
    AttackSupportWhistle1 = "Otomo_Attack_up2"
    AttackSupportWhistle2 = "Otomo_Attack_up3"
    DefenseSupportWhistle = "Otomo_Defense_up1"
    DefenseSupportWhistle1 = "Otomo_Defense_up2"
    DefenseSupportWhistle2 = "Otomo_Defense_up3"
    GrowthAccelerationBell = "Otomo_PalExp_Increase_1"
    GrowthAccelerationBell1 = "Otomo_PalExp_Increase_2"
    GrowthAccelerationBell2 = "Otomo_PalExp_Increase_3"
    UnknownItemOtomoMoveSpeedUp1 = "Otomo_MoveSpeed_up_1"
    NormalParachute = "Glider_Old"
    MegaGlider = "Glider_Good"
    GigaGlider = "Glider_Super"
    HyperGlider1 = "Glider_Tera"
    Cake = "Cake"
    MammorestCurry = "Curry"
    BroncherryFriedNoodles = "Yakisoba"
    BLT = "BLT"
    Hamburger = "Hamburger"
    MozzarinaCheeseburger = "Cheeseburger_2"
    RoastReindrix = "BakedMeat_IceDeer"
    BroncherryRibRoast = "BakedMeat_SakuraSaurus"
    MammorestSteak = "BakedMeat_GrassMammoth"
    MushroomStew = "MushroomStew"
    EikthyrdeerStew = "DeerStew"
    BologneseSauce = "MeatSauce"
    Pizza = "Pizza"
    MushroomQuiche = "Quiche"
    BroncherryMeat = "Meat_SakuraSaurus"
    MammorestMeat = "Meat_GrassMammoth"
    EikthyrdeerLocoMoco = "DeerLocoMoco"
    DumudChowder = "Chowder"
    RushoarBaconNEggs = "BaconEggs"
    MozzarinaHamburger = "Hamburger_2"
    GaleclawNikujaga = "MeatAndPotatoes"
    GrilledLamball = "GenghisKhan"
    Minestrone = "Minestrone"
    RushoarHotDog = "HotDog_2"
    ReindrixStew = "StewedIceDeer"
    Carbonara = "Carbonara"
    RushoarGyoza = "Gyoza"
    SpringRolls = "SpringRolls"
    Gratin = "Gratin"
    FriedChikipi = "FriedChicken"
    FriedKelpsea = "FriedKelpie"
    HotDog = "HotDog"
    SeafoodSalad = "Seafood_Salada"
    HerbRoastedLamball = "GrilledSheepHerbs"
    ChikipiSaut = "ChickenSaute"
    StewedGaleclaw = "Eaglestew"
    StirFriedVeggies = "FriedVegetables"
    MunchillSteak = "BakedMeat_IceCrocodile"
    Salad = "Salad"
    HerbRoastedCaprity = "BakedMeat_BerryGoat"
    MozzarinaSteak = "BakedMeat_CowPal"
    FriedGloopieBalls = "OctopusGirl_Takoyaki"
    BroiledDumud = "BakedMeat_LazyCatfish"
    RoastEikthyrdeer = "BakedMeat_Deer"
    Omelet = "Omelet"
    ReindrixVenison = "Meat_IceDeer"
    MarinatedMushrooms = "MarinatedMushrooms"
    RoastRushoar = "BakedMeat_Boar"
    JellroySJollyJelly = "JellyfishGhost_jelly"
    JellietteSJigglyJelly = "JellyfishFairy_jelly"
    CaprityMeat = "Meat_BerryGoat"
    MozzarinaMeat = "Meat_CowPal"
    StirFriedVegetables = "StirFriedVegetables"
    MushroomSoup = "MushroomSoup"
    LamballKebab = "BakedMeat_SheepBall"
    JamFilledBun = "JamBun"
    RawDumud = "Meat_LazyCatfish"
    EikthyrdeerVenison = "Meat_Deer"
    GrilledChikipi = "BakedMeat_ChickenPal"
    GrilledKelpsea = "BakedMeat_Kelpie"
    GrilledGaleclaw = "BakedMeat_Eagle"
    RushoarPork = "Meat_Boar"
    Pancake = "Pancake"
    MunchillMeat = "Meat_IceCrocodile"
    GloopieTentacle = "Meat_OctopusGirl"
    LamballMutton = "Meat_SheepBall"
    JellroyBellFlesh = "Meat_JellyfishGhost"
    ChikipiPoultry = "Meat_ChickenPal"
    RawKelpsea = "Meat_Kelpie"
    GaleclawPoultry = "Meat_Eagle"
    FrenchFries = "PotatoChips"
    JellietteBellFlesh = "Meat_JellyfishFairy"
    Bread = "Pan"
    FriedEgg = "FriedEggs"
    BakedBerries = "Baked_Berries"
    BakedMushroom = "BakedMushroom"
    Egg = "Egg"
    HotMilk = "HotMilk"
    RedBerries = "Berries"
    Tomato = "Tomato"
    Lettuce = "Lettuce"
    CavernMushroom = "CaveMushroom"
    Mushroom = "Mushroom"
    Milk = "Milk"
    Potato = "Potato"
    Honey = "Honey"
    Carrot = "Carrot"
    Onion = "Onion"
    Wheat = "Wheat"
    CottonCandy = "Sweet"
    Flour = "Flour"
    MysteriousMushroom = "PoisonMushroom"
    LowGradeMedicalSupplies = "Herbs"
    MedicalSupplies = "Medicines"
    HighGradeMedicalSupplies = "LuxuryMedicines"
    MindControlMeds = "MindControlDrug"
    LowQualityRecoveryMeds = "Potion_Low"
    RecoveryMeds = "Potion"
    HighQualityRecoveryMeds = "Potion_High"
    AdvancedRecoveryMeds = "Potion_Extreme"
    BeautifulFlower = "Poppy"
    SuspiciousJuice = "Opium"
    StrangeJuice = "Narcotic"
    MysteriousMushroomJuice = "MushroomJuice"
    MemoryWipingMedicine = "StatusPointResetSan"
    RevivalPotion = "PalRevive"
    NutrientTonic = "Supplement"
    VitalRemedy = "Elixir_hp_01"
    StaminaRemedy = "Elixir_stamina_01"
    MightRemedy = "Elixir_attack_01"
    SpeedRemedy = "Elixir_workspeed_01"
    BurdenRemedy = "Elixir_weight_01"
    VitalElixir = "Elixir_hp_02"
    StaminaElixir = "Elixir_stamina_02"
    MightElixir = "Elixir_attack_02"
    SpeedElixir = "Elixir_workspeed_02"
    BurdenElixir = "Elixir_weight_02"
    LifeCrystal = "Elixir_hp_Yakushima"
    KinshipPeach = "AffectionFruit_01"
    LittleKinshipPeach = "AffectionFruit_02"
    ScrappedTissueSample = "MeaninglessItem_ButcheringImportPal"
    LifeLotusS = "Lotus_hp_01"
    StaminaLotusS = "Lotus_stamina_01"
    PowerLotusS = "Lotus_attack_01"
    SpeedLotusS = "Lotus_workspeed_01"
    CarryingLotusS = "Lotus_weight_01"
    LifeLotusL = "Lotus_hp_02"
    StaminaLotusL = "Lotus_stamina_02"
    PowerLotusL = "Lotus_attack_02"
    SpeedLotusL = "Lotus_workspeed_02"
    CarryingLotusL = "Lotus_weight_02"
    LifeFruit = "Fruit_hp_01"
    PowerFruit = "Fruit_attack_01"
    StoutFruit = "Fruit__defense_01"
    HomewardThundercloud = "Homeward"
    AwakeningStarfruit1 = "Rankup_1"
    AwakeningStarfruit2 = "Rankup_2"
    AwakeningStarfruit3 = "Rankup_3"
    AwakeningStarfruit4 = "Rankup_4"
    RipeAwakeningStarfruit = "Rankup_Arbitrary"
    AppliedKindlingTechnique = "WorkSuitability_AddTicket_EmitFlame"
    AppliedWateringTechnique = "WorkSuitability_AddTicket_Watering"
    AppliedPlantingTechnique = "WorkSuitability_AddTicket_Seeding"
    AppliedGeneratingElectricityTechnique = "WorkSuitability_AddTicket_GenerateElectricity"
    AppliedHandiworkTechnique = "WorkSuitability_AddTicket_Handcraft"
    AppliedGatheringTechnique = "WorkSuitability_AddTicket_Collection"
    AppliedLumberingTechnique = "WorkSuitability_AddTicket_Deforest"
    AppliedMiningTechnique = "WorkSuitability_AddTicket_Mining"
    AppliedMedicineProductionTechnique = "WorkSuitability_AddTicket_ProductMedicine"
    AppliedCoolingTechnique = "WorkSuitability_AddTicket_Cool"
    AppliedTransportingTechnique = "WorkSuitability_AddTicket_Transport"
    TrainingManualS = "ExpBoost_01"
    TrainingManualM = "ExpBoost_02"
    TrainingManualL = "ExpBoost_03"
    TrainingManualXL = "ExpBoost_04"
    TrainingCrystal = "LvUP_01"
    Wood = "Wood"
    Fiber = "Fiber"
    Stone = "Stone"
    PaldiumFragment = "Pal_crystal_S"
    Ore = "CopperOre"
    Coal = "Coal"
    Sulfur = "Sulfur"
    PureQuartz = "Quartz"
    CrudeOil = "CrudeOil"
    Chromite = "Chromium"
    NightstarSand = "NightStone"
    HexoliteQuartz = "RainbowCrystal"
    CoralumOre = "ManganeseOre"
    MeteoriteFragment = "MeteorDrop"
    Wool = "Wool"
    Leather = "Leather"
    Bone = "Bone"
    Horn = "Horn"
    ElectricOrgan = "ElectricOrgan"
    VenomGland = "Venom"
    FlameOrgan = "FireOrgan"
    IceOrgan = "IceOrgan"
    PalFluids = "PalFluid"
    HighQualityPalOil = "PalOil"
    DarkFragment = "PalDarkParts"
    TocotocoFeather = "PalItem_ColorfulBird"
    GumossLeaf = "PalItem_PlantSlime"
    PenkingPlume = "PalItem_CaptainPenguin"
    KatressHair = "PalItem_CatMage"
    RibbunyRibbon = "PalItem_PinkRabbit"
    SweeHair = "PalItem_MopBaby"
    KillamariTentacle = "PalItem_NegativeOctopus"
    DazziCloud = "PalItem_RaijinDaughter"
    LeezpunkCrest = "PalItem_LizardMan"
    AncientPalManuscript = "AncientParts3"
    AncientCivilizationParts = "PalCrystal_Ex"
    AncientCivilizationCore = "AncientParts2"
    PredatorCore = "PredatorCrystal"
    SuccessfulBountyToken = "BountyProof_1"
    BattleTicket = "BattleTicket"
    BerrySeeds = "BerrySeeds"
    WheatSeeds = "WheatSeeds"
    TomatoSeeds = "TomatoSeeds"
    LettuceSeeds = "LettuceSeeds"
    PotatoSeeds = "PotatoSeeds"
    CarrotSeeds = "CarrotSeeds"
    OnionSeeds = "OnionSeeds"
    Cloth = "Cloth"
    HighQualityCloth = "Cloth2"
    Nail = "MachineParts"
    Gunpowder1 = "Gunpowder2"
    CircuitBoard = "MachineParts2"
    Polymer = "Polymer"
    Silicon = "Silicon"
    Cement = "Cement"
    CarbonFiber = "CarbonFiber"
    Charcoal = "Charcoal"
    Ingot = "CopperIngot"
    RefinedIngot = "IronIngot"
    PalMetalIngot = "StealIngot"
    Plasteel = "Plastic"
    Hexolite = "StainlessSteel"
    UnknownItemYakushimaParts003 = "YakushimaParts003"
    HallowedBar = "YakushimaIngot001"
    LuminiteBar = "YakushimaIngot002"
    CoralumIngot = "ManganeseIngot"
    CommonEgg = "PalEgg_Normal_01"
    CommonEgg1 = "PalEgg_Normal_02"
    LargeCommonEgg2 = "PalEgg_Normal_03"
    LargeCommonEgg3 = "PalEgg_Normal_04"
    HugeCommonEgg = "PalEgg_Normal_05"
    ScorchingEgg = "PalEgg_Fire_01"
    ScorchingEgg1 = "PalEgg_Fire_02"
    LargeScorchingEgg2 = "PalEgg_Fire_03"
    LargeScorchingEgg3 = "PalEgg_Fire_04"
    HugeScorchingEgg = "PalEgg_Fire_05"
    DampEgg = "PalEgg_Water_01"
    DampEgg1 = "PalEgg_Water_02"
    LargeDampEgg2 = "PalEgg_Water_03"
    LargeDampEgg3 = "PalEgg_Water_04"
    HugeDampEgg = "PalEgg_Water_05"
    VerdantEgg = "PalEgg_Leaf_01"
    VerdantEgg1 = "PalEgg_Leaf_02"
    LargeVerdantEgg2 = "PalEgg_Leaf_03"
    LargeVerdantEgg3 = "PalEgg_Leaf_04"
    HugeVerdantEgg = "PalEgg_Leaf_05"
    ElectricEgg = "PalEgg_Electricity_01"
    ElectricEgg1 = "PalEgg_Electricity_02"
    LargeElectricEgg2 = "PalEgg_Electricity_03"
    LargeElectricEgg3 = "PalEgg_Electricity_04"
    HugeElectricEgg = "PalEgg_Electricity_05"
    FrozenEgg = "PalEgg_Ice_01"
    FrozenEgg1 = "PalEgg_Ice_02"
    LargeFrozenEgg2 = "PalEgg_Ice_03"
    LargeFrozenEgg3 = "PalEgg_Ice_04"
    HugeFrozenEgg = "PalEgg_Ice_05"
    RockyEgg = "PalEgg_Earth_01"
    RockyEgg1 = "PalEgg_Earth_02"
    LargeRockyEgg2 = "PalEgg_Earth_03"
    LargeRockyEgg3 = "PalEgg_Earth_04"
    HugeRockyEgg = "PalEgg_Earth_05"
    DarkEgg = "PalEgg_Dark_01"
    DarkEgg1 = "PalEgg_Dark_02"
    LargeDarkEgg2 = "PalEgg_Dark_03"
    LargeDarkEgg3 = "PalEgg_Dark_04"
    HugeDarkEgg = "PalEgg_Dark_05"
    DragonEgg = "PalEgg_Dragon_01"
    DragonEgg1 = "PalEgg_Dragon_02"
    LargeDragonEgg2 = "PalEgg_Dragon_03"
    LargeDragonEgg3 = "PalEgg_Dragon_04"
    HugeDragonEgg = "PalEgg_Dragon_05"
    Ruby = "Ruby"
    Sapphire = "Sapphire"
    Emerald = "Eemerald"
    Diamond = "Diamond"
    PreciousDragonStone = "PalItem_ToSell_01"
    PreciousPlume = "PalItem_ToSell_02"
    PreciousEntrails = "PalItem_ToSell_03"
    PreciousClaw = "PalItem_ToSell_04"
    PreciousPelt = "PalItem_ToSell_05"
    SmallPalSoul = "PalUpgradeStone"
    MediumPalSoul = "PalUpgradeStone2"
    LargePalSoul = "PalUpgradeStone3"
    GiantPalSoul = "PalUpgradeStone4"
    UnknownItemYakushimaParts001 = "YakushimaParts001"
    UnknownItemYakushimaParts002 = "YakushimaParts002"
    SkillFruitPowerShot = "SkillCard_PowerShot"
    SkillFruitAirCannon = "SkillCard_AirCanon"
    SkillFruitAirBlade = "SkillCard_AirBlade"
    SkillFruitPowerBomb = "SkillCard_PowerBall"
    SkillFruitImplode = "SkillCard_SelfDestruct"
    SkillFruitHolyBurst = "SkillCard_HolyBlast"
    SkillFruitPalBlast = "SkillCard_HyperBeam"
    GrassSkillFruitWindCutter = "SkillCard_WindCutter"
    GrassSkillFruitSeedMachineGun = "SkillCard_SeedMachinegun"
    GrassSkillFruitSeedMine = "SkillCard_SeedMine"
    GrassSkillFruitGrassTornado = "SkillCard_GrassTornado"
    GrassSkillFruitSpineVine = "SkillCard_RootAttack"
    GrassSkillFruitMulticutter = "SkillCard_SpecialCutter"
    GrassSkillFruitCircleVine = "SkillCard_RootLance"
    GrassSkillFruitSolarBlast = "SkillCard_SolarBeam"
    GrassSkillFruitReflectLeaf = "SkillCard_ReflectiveShuriken"
    GrassSkillFruitCrosswind = "SkillCard_CrossWind"
    WaterSkillFruitAquaGun = "SkillCard_WaterGun"
    WaterSkillFruitHydroJet = "SkillCard_AquaJet"
    WaterSkillFruitAcidRain = "SkillCard_AcidRain"
    WaterSkillFruitBubbleBlast = "SkillCard_BubbleShot"
    WaterSkillFruitAquaBurst = "SkillCard_WaterBall"
    WaterSkillFruitSplash = "SkillCard_LineGeyser"
    WaterSkillFruitTorrentialBlast = "SkillCard_DiversionLaser"
    WaterSkillFruitCurtainSplash = "SkillCard_WallSplash"
    WaterSkillFruitHydroLaser = "SkillCard_HydroPump"
    WaterSkillFruitHydroSlicer = "SkillCard_HydroSlicer"
    WaterSkillFruitAquaSurge = "SkillCard_RipTide"
    FireSkillFruitIgnisBlast = "SkillCard_FireBlast"
    FireSkillFruitFlareArrow = "SkillCard_FlareArrow"
    FireSkillFruitSpiritFire = "SkillCard_FireSeed"
    FireSkillFruitIgnisBreath = "SkillCard_Flamethrower"
    FireSkillFruitFlareStorm = "SkillCard_FlareTornado"
    FireSkillFruitFlameWall = "SkillCard_FlameWall"
    FireSkillFruitFlameFunnel = "SkillCard_FlameFunnel"
    FireSkillFruitFireBall = "SkillCard_FireBall"
    FireSkillFruitIgnisRage = "SkillCard_Inferno"
    FireSkillFruitVolcanicRain = "SkillCard_Eruption"
    ElectricSkillFruitShockwave = "SkillCard_ElecWave"
    ElectricSkillFruitPlasmaFunnel = "SkillCard_ThunderFunnel"
    ElectricSkillFruitSparkBlast = "SkillCard_SpreadPulse"
    ElectricSkillFruitElectricBall = "SkillCard_ThunderBall"
    ElectricSkillFruitThunderSpear = "SkillCard_ThunderSpear"
    ElectricSkillFruitLightningStreak = "SkillCard_LineThunder"
    ElectricSkillFruitLockOnLaser = "SkillCard_LockonLaser"
    ElectricSkillFruitTriLightning = "SkillCard_ThreeThunder"
    ElectricSkillFruitTriSpark = "SkillCard_TriSpark"
    ElectricSkillFruitLightningBolt = "SkillCard_Thunderbolt"
    ElectricSkillFruitLightningStrike = "SkillCard_LightningStrike"
    ElectricSkillFruitThunderRain = "SkillCard_ThunderRain"
    ElectricSkillFruitThunderstorm = "SkillCard_ThunderStorm"
    ThunderSkillFruitAllRangeThunder = "SkillCard_RangeThunder"
    EarthSkillFruitStoneCannon = "SkillCard_ThrowRock"
    EarthSkillFruitBogBlast = "SkillCard_MudShot"
    EarthSkillFruitStoneBlast = "SkillCard_StoneShotgun"
    EarthSkillFruitSandTornado = "SkillCard_SandTornado"
    EarthSkillFruitSandTwister = "SkillCard_SandTwister"
    EarthSkillFruitRockLance = "SkillCard_RockLance"
    EarthSkillFruitRockburst = "SkillCard_Tremor"
    EarthSkillFruitStoneBeat = "SkillCard_RockBeat"
    IceSkillFruitIceMissile = "SkillCard_IceMissile"
    IceSkillFruitIcicleCutter = "SkillCard_IceBlade"
    IceSkillFruitIceberg = "SkillCard_BlizzardLance"
    IceSkillFruitCrystalBreath = "SkillCard_FrostBreath"
    IceSkillFruitFreezeWall = "SkillCard_IceWall"
    IceSkillFruitIcicleBullet = "SkillCard_IciclePierce"
    IceSkillFruitIcicleLine = "SkillCard_IcicleLine"
    IceSkillFruitBlizzardSpike = "SkillCard_IcicleThrow"
    IceSkillFruitDiamondRain = "SkillCard_DiamondFall"
    IceSkillFruitAbsoluteFrost = "SkillCard_IceAge"
    DarkSkillFruitShadowBurst = "SkillCard_DarkWave"
    DarkSkillFruitPoisonBlast = "SkillCard_PoisonShot"
    DarkSkillFruitSpiritFlame = "SkillCard_GhostFlame"
    DarkSkillFruitDarkCannon = "SkillCard_DarkCanon"
    DarkSkillFruitUmbralSurge = "SkillCard_DarkPulse"
    DarkSkillFruitDarkShot = "SkillCard_GravityShot"
    DarkSkillFruitNightmareBall = "SkillCard_ShadowBall"
    DarkSkillFruitDarkArrow = "SkillCard_DarkArrow"
    DarkSkillFruitDarkLaser = "SkillCard_DarkLaser"
    DarkSkillFruitApocalypse = "SkillCard_Apocalypse"
    DarkSkillFruitDarkWhisp = "SkillCard_DarkLegion"
    DragonSkillFruitDragonCannon = "SkillCard_DragonCanon"
    DragonSkillFruitDragonBurst = "SkillCard_DragonWave"
    DragonSkillFruitDraconicBreath = "SkillCard_DragonBreath"
    DragonSkillFruitComet = "SkillCard_Commet"
    DragonSkillFruitBlastCannon = "SkillCard_BlastCanon"
    DragonSkillFruitDragonMeteor = "SkillCard_DragonMeteor"
    DragonSkillFruitBeamSlicer = "SkillCard_BeamSlicer"
    DragonSkillFruitChargeCannon = "SkillCard_ChargeCanon"
    PalReverser = "PalGenderReverse"
    ImplantMercyHit = "PalPassiveSkillChange_NonKilling"
    ImplantNocturnal = "PalPassiveSkillChange_Nocturnal"
    ImplantPhilanthropist = "PalPassiveSkillChange_HatchingSpeed_Up"
    ImplantImpatient = "PalPassiveSkillChange_CoolTimeReduction_Up_2"
    ImplantSerenity = "PalPassiveSkillChange_CoolTimeReduction_Up_1"
    ImplantFitAsAFiddle = "PalPassiveSkillChange_Stamina_Up_2"
    ImplantInfiniteStamina = "PalPassiveSkillChange_Stamina_Up_1"
    ImplantEternalEngine = "PalPassiveSkillChange_Stamina_Up_3"
    ImplantNimble = "PalPassiveSkillChange_MoveSpeed_up_1"
    ImplantRunner = "PalPassiveSkillChange_MoveSpeed_up_2"
    ImplantSwift = "PalPassiveSkillChange_MoveSpeed_up_3"
    ImplantDaintyEater = "PalPassiveSkillChange_PAL_FullStomach_Down_1"
    ImplantDietLover = "PalPassiveSkillChange_PAL_FullStomach_Down_2"
    ImplantMasteryOfFasting = "PalPassiveSkillChange_PAL_FullStomach_Down_3"
    ImplantPositiveThinker = "PalPassiveSkillChange_PAL_Sanity_Down_1"
    ImplantWorkaholic = "PalPassiveSkillChange_PAL_Sanity_Down_2"
    ImplantHeartOfTheImmovableKing = "PalPassiveSkillChange_PAL_Sanity_Down_3"
    ImplantBrave = "PalPassiveSkillChange_PAL_ALLAttack_up1"
    ImplantFerocious = "PalPassiveSkillChange_PAL_ALLAttack_up2"
    ImplantDemonGod = "PalPassiveSkillChange_PAL_ALLAttack_up3"
    ImplantHardSkin = "PalPassiveSkillChange_Deffence_up1"
    ImplantBurlyBody = "PalPassiveSkillChange_Deffence_up2"
    ImplantDiamondBody = "PalPassiveSkillChange_Deffence_up3"
    ImplantSerious = "PalPassiveSkillChange_CraftSpeed_up1"
    ImplantArtisan = "PalPassiveSkillChange_CraftSpeed_up2"
    ImplantRemarkableCraftsmanship = "PalPassiveSkillChange_CraftSpeed_up3"
    ImplantMusclehead = "PalPassiveSkillChange_Noukin"
    ImplantVanguard = "PalPassiveSkillChange_TrainerATK_UP_1"
    ImplantStrongholdStrategist = "PalPassiveSkillChange_TrainerDEF_UP_1"
    ImplantMotivationalLeader = "PalPassiveSkillChange_TrainerWorkSpeed_UP_1"
    ImplantNoble = "PalPassiveSkillChange_SalePrice_Up_1"
    ImplantAceSwimmer = "PalPassiveSkillChange_SwimSpeed_up_2"
    ImplantMineForeman = "PalPassiveSkillChange_TrainerMining_up1"
    ImplantLoggingForeman = "PalPassiveSkillChange_TrainerLogging_up1"
    ImplantFineFurs = "PalPassiveSkillChange_SalePrice_Up_2"
    ImplantSleekStroke = "PalPassiveSkillChange_SwimSpeed_up_1"
    ImplantWorkSlave = "PalPassiveSkillChange_PAL_CorporateSlave"
    HighGradeTechnicalManual = "TechnologyBook_G1"
    InnovativeTechnicalManual = "TechnologyBook_G2"
    FutureTechnicalManual = "TechnologyBook_G3"
    AncientTechnicalManual = "AncientTechnologyBook_G1"
    CopperKey = "TreasureBoxKey01"
    SilverKey = "TreasureBoxKey02"
    GoldKey = "TreasureBoxKey03"
    FishingMagnet = "Salvage_TreasureBoxKey01"
    RepairKit = "RepairKit"
    UnknownItemWaterBuildKit = "WaterBuildKit"
    LilySSpearSchematic4 = "Blueprint_Spear_ForestBoss_5"
    SwordSchematic1 = "Blueprint_Sword_2"
    SwordSchematic2 = "Blueprint_Sword_3"
    SwordSchematic3 = "Blueprint_Sword_4"
    SwordSchematic4 = "Blueprint_Sword_5"
    KatanaSchematic1 = "Blueprint_Katana_2"
    KatanaSchematic2 = "Blueprint_Katana_3"
    KatanaSchematic3 = "Blueprint_Katana_4"
    KatanaSchematic4 = "Blueprint_Katana_5"
    BeamSwordSchematic1 = "Blueprint_BeamSword_2"
    BeamSwordSchematic2 = "Blueprint_BeamSword_3"
    BeamSwordSchematic3 = "Blueprint_BeamSword_4"
    BeamSwordSchematic4 = "Blueprint_BeamSword_5"
    OldBowSchematic1 = "Blueprint_WeakerBow_2"
    OldBowSchematic2 = "Blueprint_WeakerBow_3"
    OldBowSchematic3 = "Blueprint_WeakerBow_4"
    OldBowSchematic4 = "Blueprint_WeakerBow_5"
    CrossbowSchematic1 = "Blueprint_BowGun_2"
    CrossbowSchematic2 = "Blueprint_BowGun_3"
    CrossbowSchematic3 = "Blueprint_BowGun_4"
    CrossbowSchematic4 = "Blueprint_BowGun_5"
    FireArrowCrossbowSchematic1 = "Blueprint_BowGun_Fire_2"
    FireArrowCrossbowSchematic2 = "Blueprint_BowGun_Fire_3"
    FireArrowCrossbowSchematic3 = "Blueprint_BowGun_Fire_4"
    FireArrowCrossbowSchematic4 = "Blueprint_BowGun_Fire_5"
    PoisonArrowCrossbowSchematic1 = "Blueprint_BowGun_Poison_2"
    PoisonArrowCrossbowSchematic2 = "Blueprint_BowGun_Poison_3"
    PoisonArrowCrossbowSchematic3 = "Blueprint_BowGun_Poison_4"
    PoisonArrowCrossbowSchematic4 = "Blueprint_BowGun_Poison_5"
    MakeshiftHandgunSchematic1 = "Blueprint_MakeshiftHandgun_2"
    MakeshiftHandgunSchematic2 = "Blueprint_MakeshiftHandgun_3"
    MakeshiftHandgunSchematic3 = "Blueprint_MakeshiftHandgun_4"
    MakeshiftHandgunSchematic4 = "Blueprint_MakeshiftHandgun_5"
    MusketSchematic1 = "Blueprint_Musket_2"
    MusketSchematic2 = "Blueprint_Musket_3"
    MusketSchematic3 = "Blueprint_Musket_4"
    MusketSchematic4 = "Blueprint_Musket_5"
    HandgunSchematic1 = "Blueprint_HandGun_Default_2"
    HandgunSchematic2 = "Blueprint_HandGun_Default_3"
    HandgunSchematic3 = "Blueprint_HandGun_Default_4"
    HandgunSchematic4 = "Blueprint_HandGun_Default_5"
    OldRevolverSchematic1 = "Blueprint_OldRevolver_2"
    OldRevolverSchematic2 = "Blueprint_OldRevolver_3"
    OldRevolverSchematic3 = "Blueprint_OldRevolver_4"
    OldRevolverSchematic4 = "Blueprint_OldRevolver_5"
    SingleShotRifleSchematic1 = "Blueprint_SingleShotRifle_2"
    SingleShotRifleSchematic2 = "Blueprint_SingleShotRifle_3"
    SingleShotRifleSchematic3 = "Blueprint_SingleShotRifle_4"
    SingleShotRifleSchematic4 = "Blueprint_SingleShotRifle_5"
    SemiAutoRifleSchematic1 = "Blueprint_SemiAutoRifle_2"
    SemiAutoRifleSchematic2 = "Blueprint_SemiAutoRifle_3"
    SemiAutoRifleSchematic3 = "Blueprint_SemiAutoRifle_4"
    SemiAutoRifleSchematic4 = "Blueprint_SemiAutoRifle_5"
    MakeshiftAssaultRifleSchematic1 = "Blueprint_MakeshiftAssaultRifle_2"
    MakeshiftAssaultRifleSchematic2 = "Blueprint_MakeshiftAssaultRifle_3"
    MakeshiftAssaultRifleSchematic3 = "Blueprint_MakeshiftAssaultRifle_4"
    MakeshiftAssaultRifleSchematic4 = "Blueprint_MakeshiftAssaultRifle_5"
    AssaultRifleSchematic1 = "Blueprint_AssaultRifle_Default2"
    AssaultRifleSchematic2 = "Blueprint_AssaultRifle_Default3"
    AssaultRifleSchematic3 = "Blueprint_AssaultRifle_Default4"
    AssaultRifleSchematic4 = "Blueprint_AssaultRifle_Default5"
    MakeshiftShotgunSchematic1 = "Blueprint_MakeshiftShotgun_2"
    MakeshiftShotgunSchematic2 = "Blueprint_MakeshiftShotgun_3"
    MakeshiftShotgunSchematic3 = "Blueprint_MakeshiftShotgun_4"
    MakeshiftShotgunSchematic4 = "Blueprint_MakeshiftShotgun_5"
    DoubleBarreledShotgunSchematic1 = "Blueprint_DoubleBarrelShotgun_2"
    DoubleBarreledShotgunSchematic2 = "Blueprint_DoubleBarrelShotgun_3"
    DoubleBarreledShotgunSchematic3 = "Blueprint_DoubleBarrelShotgun_4"
    DoubleBarreledShotgunSchematic4 = "Blueprint_DoubleBarrelShotgun_5"
    PumpActionShotgunSchematic1 = "Blueprint_PumpActionShotgun_2"
    PumpActionShotgunSchematic2 = "Blueprint_PumpActionShotgun_3"
    PumpActionShotgunSchematic3 = "Blueprint_PumpActionShotgun_4"
    PumpActionShotgunSchematic4 = "Blueprint_PumpActionShotgun_5"
    SemiAutoShotgunSchematic1 = "Blueprint_SemiAutoShotgun_2"
    SemiAutoShotgunSchematic2 = "Blueprint_SemiAutoShotgun_3"
    SemiAutoShotgunSchematic3 = "Blueprint_SemiAutoShotgun_4"
    SemiAutoShotgunSchematic4 = "Blueprint_SemiAutoShotgun_5"
    MakeshiftSMGSchematic1 = "Blueprint_MakeshiftSubmachineGun_2"
    MakeshiftSMGSchematic2 = "Blueprint_MakeshiftSubmachineGun_3"
    MakeshiftSMGSchematic3 = "Blueprint_MakeshiftSubmachineGun_4"
    MakeshiftSMGSchematic4 = "Blueprint_MakeshiftSubmachineGun_5"
    SMGSchematic1 = "Blueprint_SubmachineGun_2"
    SMGSchematic2 = "Blueprint_SubmachineGun_3"
    SMGSchematic3 = "Blueprint_SubmachineGun_4"
    SMGSchematic4 = "Blueprint_SubmachineGun_5"
    RocketLauncherSchematic1 = "Blueprint_Launcher_Default_2"
    RocketLauncherSchematic2 = "Blueprint_Launcher_Default_3"
    RocketLauncherSchematic3 = "Blueprint_Launcher_Default_4"
    RocketLauncherSchematic4 = "Blueprint_Launcher_Default_5"
    LaserRifleSchematic1 = "Blueprint_LaserRifle_2"
    LaserRifleSchematic2 = "Blueprint_LaserRifle_3"
    LaserRifleSchematic3 = "Blueprint_LaserRifle_4"
    LaserRifleSchematic4 = "Blueprint_LaserRifle_5"
    FlamethrowerSchematic1 = "Blueprint_FlameThrower_2"
    FlamethrowerSchematic2 = "Blueprint_FlameThrower_3"
    FlamethrowerSchematic3 = "Blueprint_FlameThrower_4"
    FlamethrowerSchematic4 = "Blueprint_FlameThrower_5"
    GrenadeLauncherSchematic1 = "Blueprint_GrenadeLauncher_2"
    GrenadeLauncherSchematic2 = "Blueprint_GrenadeLauncher_3"
    GrenadeLauncherSchematic3 = "Blueprint_GrenadeLauncher_4"
    GrenadeLauncherSchematic4 = "Blueprint_GrenadeLauncher_5"
    GuidedMissileLauncherSchematic1 = "Blueprint_GuidedMissileLauncher_2"
    GuidedMissileLauncherSchematic2 = "Blueprint_GuidedMissileLauncher_3"
    GuidedMissileLauncherSchematic3 = "Blueprint_GuidedMissileLauncher_4"
    GuidedMissileLauncherSchematic4 = "Blueprint_GuidedMissileLauncher_5"
    MultiGuidedMissileLauncherSchematic = "Blueprint_MultiGuidedMissileLauncher"
    MultiGuidedMissileLauncherSchematic1 = "Blueprint_MultiGuidedMissileLauncher_2"
    MultiGuidedMissileLauncherSchematic2 = "Blueprint_MultiGuidedMissileLauncher_3"
    MultiGuidedMissileLauncherSchematic3 = "Blueprint_MultiGuidedMissileLauncher_4"
    MultiGuidedMissileLauncherSchematic4 = "Blueprint_MultiGuidedMissileLauncher_5"
    GatlingGunSchematic1 = "Blueprint_GatlingGun_2"
    GatlingGunSchematic2 = "Blueprint_GatlingGun_3"
    GatlingGunSchematic3 = "Blueprint_GatlingGun_4"
    GatlingGunSchematic4 = "Blueprint_GatlingGun_5"
    LaserGatlingGunSchematic1 = "Blueprint_LaserGatlingGun_2"
    LaserGatlingGunSchematic2 = "Blueprint_LaserGatlingGun_3"
    LaserGatlingGunSchematic3 = "Blueprint_LaserGatlingGun_4"
    LaserGatlingGunSchematic4 = "Blueprint_LaserGatlingGun_5"
    PlasmaCannonSchematic1 = "Blueprint_EnergyRocketLauncher_2"
    PlasmaCannonSchematic2 = "Blueprint_EnergyRocketLauncher_3"
    PlasmaCannonSchematic3 = "Blueprint_EnergyRocketLauncher_4"
    PlasmaCannonSchematic4 = "Blueprint_EnergyRocketLauncher_5"
    CompoundBowSchematic1 = "Blueprint_CompoundBow_2"
    CompoundBowSchematic2 = "Blueprint_CompoundBow_3"
    CompoundBowSchematic3 = "Blueprint_CompoundBow_4"
    CompoundBowSchematic4 = "Blueprint_CompoundBow_5"
    AdvancedBowSchematic1 = "Blueprint_SFBow_2"
    AdvancedBowSchematic2 = "Blueprint_SFBow_3"
    AdvancedBowSchematic3 = "Blueprint_SFBow_4"
    AdvancedBowSchematic4 = "Blueprint_SFBow_5"
    OverheatRifleSchematic1 = "Blueprint_OverheatRifle_2"
    OverheatRifleSchematic2 = "Blueprint_OverheatRifle_3"
    OverheatRifleSchematic3 = "Blueprint_OverheatRifle_4"
    OverheatRifleSchematic4 = "Blueprint_OverheatRifle_5"
    ChargeRifleSchematic1 = "Blueprint_ChargeLaserRifle_2"
    ChargeRifleSchematic2 = "Blueprint_ChargeLaserRifle_3"
    ChargeRifleSchematic3 = "Blueprint_ChargeLaserRifle_4"
    ChargeRifleSchematic4 = "Blueprint_ChargeLaserRifle_5"
    EnergyShotgunSchematic1 = "Blueprint_EnergyShotgun_2"
    EnergyShotgunSchematic2 = "Blueprint_EnergyShotgun_3"
    EnergyShotgunSchematic3 = "Blueprint_EnergyShotgun_4"
    EnergyShotgunSchematic4 = "Blueprint_EnergyShotgun_5"
    MeteorLauncherSchematic4 = "Blueprint_Launcher_Meteor_5"
    ExcaliburSchematic = "Blueprint_YakushimaBlade004"
    ExcaliburSchematic1 = "Blueprint_YakushimaBlade004_2"
    ExcaliburSchematic2 = "Blueprint_YakushimaBlade004_3"
    ExcaliburSchematic3 = "Blueprint_YakushimaBlade004_4"
    ExcaliburSchematic4 = "Blueprint_YakushimaBlade004_5"
    TerraBladeSchematic = "Blueprint_YakushimaBlade002"
    TerraBladeSchematic1 = "Blueprint_YakushimaBlade002_2"
    TerraBladeSchematic2 = "Blueprint_YakushimaBlade002_3"
    TerraBladeSchematic3 = "Blueprint_YakushimaBlade002_4"
    TerraBladeSchematic4 = "Blueprint_YakushimaBlade002_5"
    VortexBeaterSchematic = "Blueprint_YakushimaGun001"
    VortexBeaterSchematic1 = "Blueprint_YakushimaGun001_2"
    VortexBeaterSchematic2 = "Blueprint_YakushimaGun001_3"
    VortexBeaterSchematic3 = "Blueprint_YakushimaGun001_4"
    VortexBeaterSchematic4 = "Blueprint_YakushimaGun001_5"
    NightglowSchematic = "Blueprint_YakushimaLantern001"
    NightglowSchematic1 = "Blueprint_YakushimaLantern001_2"
    NightglowSchematic2 = "Blueprint_YakushimaLantern001_3"
    NightglowSchematic3 = "Blueprint_YakushimaLantern001_4"
    NightglowSchematic4 = "Blueprint_YakushimaLantern001_5"
    TerraprismaSchematic = "Blueprint_YakushimaBlade003"
    TerraprismaSchematic1 = "Blueprint_YakushimaBlade003_2"
    TerraprismaSchematic2 = "Blueprint_YakushimaBlade003_3"
    TerraprismaSchematic3 = "Blueprint_YakushimaBlade003_4"
    TerraprismaSchematic4 = "Blueprint_YakushimaBlade003_5"
    MarksmanRevolverSchematic1 = "Blueprint_OctaviaRevolver_2"
    MarksmanRevolverSchematic2 = "Blueprint_OctaviaRevolver_3"
    MarksmanRevolverSchematic3 = "Blueprint_OctaviaRevolver_4"
    MarksmanRevolverSchematic4 = "Blueprint_OctaviaRevolver_5"
    CoreEjectShotgunSchematic1 = "Blueprint_OctaviaShotgun_2"
    CoreEjectShotgunSchematic2 = "Blueprint_OctaviaShotgun_3"
    CoreEjectShotgunSchematic3 = "Blueprint_OctaviaShotgun_4"
    CoreEjectShotgunSchematic4 = "Blueprint_OctaviaShotgun_5"
    ClothOutfitSchematic1 = "Blueprint_ClothArmor_2"
    ClothOutfitSchematic2 = "Blueprint_ClothArmor_3"
    ClothOutfitSchematic3 = "Blueprint_ClothArmor_4"
    ClothOutfitSchematic4 = "Blueprint_ClothArmor_5"
    TropicalOutfitSchematic1 = "Blueprint_ClothArmorHeat_2"
    TropicalOutfitSchematic2 = "Blueprint_ClothArmorHeat_3"
    TropicalOutfitSchematic3 = "Blueprint_ClothArmorHeat_4"
    TropicalOutfitSchematic4 = "Blueprint_ClothArmorHeat_5"
    TundraOutfitSchematic1 = "Blueprint_ClothArmorCold_2"
    TundraOutfitSchematic2 = "Blueprint_ClothArmorCold_3"
    TundraOutfitSchematic3 = "Blueprint_ClothArmorCold_4"
    TundraOutfitSchematic4 = "Blueprint_ClothArmorCold_5"
    PeltArmorSchematic1 = "Blueprint_FurArmor_2"
    PeltArmorSchematic2 = "Blueprint_FurArmor_3"
    PeltArmorSchematic3 = "Blueprint_FurArmor_4"
    PeltArmorSchematic4 = "Blueprint_FurArmor_5"
    HeatResistantPeltArmorSchematic1 = "Blueprint_FurArmorHeat_2"
    HeatResistantPeltArmorSchematic2 = "Blueprint_FurArmorHeat_3"
    HeatResistantPeltArmorSchematic3 = "Blueprint_FurArmorHeat_4"
    HeatResistantPeltArmorSchematic4 = "Blueprint_FurArmorHeat_5"
    ColdResistantPeltArmorSchematic1 = "Blueprint_FurArmorCold_2"
    ColdResistantPeltArmorSchematic2 = "Blueprint_FurArmorCold_3"
    ColdResistantPeltArmorSchematic3 = "Blueprint_FurArmorCold_4"
    ColdResistantPeltArmorSchematic4 = "Blueprint_FurArmorCold_5"
    MetalArmorSchematic1 = "Blueprint_CopperArmor_2"
    MetalArmorSchematic2 = "Blueprint_CopperArmor_3"
    MetalArmorSchematic3 = "Blueprint_CopperArmor_4"
    MetalArmorSchematic4 = "Blueprint_CopperArmor_5"
    HeatResistantMetalArmorSchematic1 = "Blueprint_CopperArmorHeat_2"
    HeatResistantMetalArmorSchematic2 = "Blueprint_CopperArmorHeat_3"
    HeatResistantMetalArmorSchematic3 = "Blueprint_CopperArmorHeat_4"
    HeatResistantMetalArmorSchematic4 = "Blueprint_CopperArmorHeat_5"
    ColdResistantMetalArmorSchematic1 = "Blueprint_CopperArmorCold_2"
    ColdResistantMetalArmorSchematic2 = "Blueprint_CopperArmorCold_3"
    ColdResistantMetalArmorSchematic3 = "Blueprint_CopperArmorCold_4"
    ColdResistantMetalArmorSchematic4 = "Blueprint_CopperArmorCold_5"
    RefinedMetalArmorSchematic1 = "Blueprint_IronArmor_2"
    RefinedMetalArmorSchematic2 = "Blueprint_IronArmor_3"
    RefinedMetalArmorSchematic3 = "Blueprint_IronArmor_4"
    RefinedMetalArmorSchematic4 = "Blueprint_IronArmor_5"
    HeatResistantRefinedMetalArmorSchematic1 = "Blueprint_IronArmorHeat_2"
    HeatResistantRefinedMetalArmorSchematic2 = "Blueprint_IronArmorHeat_3"
    HeatResistantRefinedMetalArmorSchematic3 = "Blueprint_IronArmorHeat_4"
    HeatResistantRefinedMetalArmorSchematic4 = "Blueprint_IronArmorHeat_5"
    ColdResistantRefinedMetalArmorSchematic1 = "Blueprint_IronArmorCold_2"
    ColdResistantRefinedMetalArmorSchematic2 = "Blueprint_IronArmorCold_3"
    ColdResistantRefinedMetalArmorSchematic3 = "Blueprint_IronArmorCold_4"
    ColdResistantRefinedMetalArmorSchematic4 = "Blueprint_IronArmorCold_5"
    PalMetalArmorSchematic1 = "Blueprint_StealArmor_2"
    PalMetalArmorSchematic2 = "Blueprint_StealArmor_3"
    PalMetalArmorSchematic3 = "Blueprint_StealArmor_4"
    PalMetalArmorSchematic4 = "Blueprint_StealArmor_5"
    HeatResistantPalMetalArmorSchematic1 = "Blueprint_StealArmorHeat_2"
    HeatResistantPalMetalArmorSchematic2 = "Blueprint_StealArmorHeat_3"
    HeatResistantPalMetalArmorSchematic3 = "Blueprint_StealArmorHeat_4"
    HeatResistantPalMetalArmorSchematic4 = "Blueprint_StealArmorHeat_5"
    ColdResistantPalMetalArmorSchematic1 = "Blueprint_StealArmorCold_2"
    ColdResistantPalMetalArmorSchematic2 = "Blueprint_StealArmorCold_3"
    ColdResistantPalMetalArmorSchematic3 = "Blueprint_StealArmorCold_4"
    ColdResistantPalMetalArmorSchematic4 = "Blueprint_StealArmorCold_5"
    PlasteelArmorSchematic1 = "Blueprint_PlasticArmor_2"
    PlasteelArmorSchematic2 = "Blueprint_PlasticArmor_3"
    PlasteelArmorSchematic3 = "Blueprint_PlasticArmor_4"
    PlasteelArmorSchematic4 = "Blueprint_PlasticArmor_5"
    HeatResistantPlasteelArmorSchematic1 = "Blueprint_PlasticArmorHeat_2"
    HeatResistantPlasteelArmorSchematic2 = "Blueprint_PlasticArmorHeat_3"
    HeatResistantPlasteelArmorSchematic3 = "Blueprint_PlasticArmorHeat_4"
    HeatResistantPlasteelArmorSchematic4 = "Blueprint_PlasticArmorHeat_5"
    ColdResistantPlasteelArmorSchematic1 = "Blueprint_PlasticArmorCold_2"
    ColdResistantPlasteelArmorSchematic2 = "Blueprint_PlasticArmorCold_3"
    ColdResistantPlasteelArmorSchematic3 = "Blueprint_PlasticArmorCold_4"
    ColdResistantPlasteelArmorSchematic4 = "Blueprint_PlasticArmorCold_5"
    LightweightPlasteelArmorSchematic1 = "Blueprint_PlasticArmorWeight_2"
    LightweightPlasteelArmorSchematic2 = "Blueprint_PlasticArmorWeight_3"
    LightweightPlasteelArmorSchematic3 = "Blueprint_PlasticArmorWeight_4"
    LightweightPlasteelArmorSchematic4 = "Blueprint_PlasticArmorWeight_5"
    HexoliteArmorSchematic1 = "Blueprint_SFArmor_2"
    HexoliteArmorSchematic2 = "Blueprint_SFArmor_3"
    HexoliteArmorSchematic3 = "Blueprint_SFArmor_4"
    HexoliteArmorSchematic4 = "Blueprint_SFArmor_5"
    HeatResistantHexoliteArmorSchematic1 = "Blueprint_SFArmorHeat_2"
    HeatResistantHexoliteArmorSchematic2 = "Blueprint_SFArmorHeat_3"
    HeatResistantHexoliteArmorSchematic3 = "Blueprint_SFArmorHeat_4"
    HeatResistantHexoliteArmorSchematic4 = "Blueprint_SFArmorHeat_5"
    ColdResistantHexoliteArmorSchematic1 = "Blueprint_SFArmorCold_2"
    ColdResistantHexoliteArmorSchematic2 = "Blueprint_SFArmorCold_3"
    ColdResistantHexoliteArmorSchematic3 = "Blueprint_SFArmorCold_4"
    ColdResistantHexoliteArmorSchematic4 = "Blueprint_SFArmorCold_5"
    LightweightHexoliteArmorSchematic1 = "Blueprint_SFArmorWeight_2"
    LightweightHexoliteArmorSchematic2 = "Blueprint_SFArmorWeight_3"
    LightweightHexoliteArmorSchematic3 = "Blueprint_SFArmorWeight_4"
    LightweightHexoliteArmorSchematic4 = "Blueprint_SFArmorWeight_5"
    HallowedPlateMailSchematic = "Blueprint_YakushimaArmor001"
    HallowedPlateMailSchematic1 = "Blueprint_YakushimaArmor001_2"
    HallowedPlateMailSchematic2 = "Blueprint_YakushimaArmor001_3"
    HallowedPlateMailSchematic3 = "Blueprint_YakushimaArmor001_4"
    HallowedPlateMailSchematic4 = "Blueprint_YakushimaArmor001_5"
    V1ArmorSchematic4 = "Blueprint_Octavia001_Armor_5"
    V2ArmorSchematic4 = "Blueprint_Octavia002_Armor_5"
    FeatheredHairBandSchematic1 = "Blueprint_FurHelmet_2"
    FeatheredHairBandSchematic2 = "Blueprint_FurHelmet_3"
    FeatheredHairBandSchematic3 = "Blueprint_FurHelmet_4"
    FeatheredHairBandSchematic4 = "Blueprint_FurHelmet_5"
    MetalHelmSchematic1 = "Blueprint_CopperHelmet_2"
    MetalHelmSchematic2 = "Blueprint_CopperHelmet_3"
    MetalHelmSchematic3 = "Blueprint_CopperHelmet_4"
    MetalHelmSchematic4 = "Blueprint_CopperHelmet_5"
    RefinedMetalHelmSchematic1 = "Blueprint_IronHelmet_2"
    RefinedMetalHelmSchematic2 = "Blueprint_IronHelmet_3"
    RefinedMetalHelmSchematic3 = "Blueprint_IronHelmet_4"
    RefinedMetalHelmSchematic4 = "Blueprint_IronHelmet_5"
    PalMetalHelmSchematic1 = "Blueprint_StealHelmet_2"
    PalMetalHelmSchematic2 = "Blueprint_StealHelmet_3"
    PalMetalHelmSchematic3 = "Blueprint_StealHelmet_4"
    PalMetalHelmSchematic4 = "Blueprint_StealHelmet_5"
    PlasteelHelmetSchematic1 = "Blueprint_PlasticHelmet_2"
    PlasteelHelmetSchematic2 = "Blueprint_PlasticHelmet_3"
    PlasteelHelmetSchematic3 = "Blueprint_PlasticHelmet_4"
    PlasteelHelmetSchematic4 = "Blueprint_PlasticHelmet_5"
    HexoliteHelmetSchematic1 = "Blueprint_SFHelmet_2"
    HexoliteHelmetSchematic2 = "Blueprint_SFHelmet_3"
    HexoliteHelmetSchematic3 = "Blueprint_SFHelmet_4"
    HexoliteHelmetSchematic4 = "Blueprint_SFHelmet_5"
    HallowedMaskSchematic = "Blueprint_YakushimaHeadEquip001"
    HallowedMaskSchematic1 = "Blueprint_YakushimaHeadEquip001_2"
    HallowedMaskSchematic2 = "Blueprint_YakushimaHeadEquip001_3"
    HallowedMaskSchematic3 = "Blueprint_YakushimaHeadEquip001_4"
    HallowedMaskSchematic4 = "Blueprint_YakushimaHeadEquip001_5"
    HallowedHelmetSchematic = "Blueprint_YakushimaHeadEquip003"
    HallowedHelmetSchematic1 = "Blueprint_YakushimaHeadEquip003_2"
    HallowedHelmetSchematic2 = "Blueprint_YakushimaHeadEquip003_3"
    HallowedHelmetSchematic3 = "Blueprint_YakushimaHeadEquip003_4"
    HallowedHelmetSchematic4 = "Blueprint_YakushimaHeadEquip003_5"
    HallowedHeadgearSchematic = "Blueprint_YakushimaHeadEquip002"
    HallowedHeadgearSchematic1 = "Blueprint_YakushimaHeadEquip002_2"
    HallowedHeadgearSchematic2 = "Blueprint_YakushimaHeadEquip002_3"
    HallowedHeadgearSchematic3 = "Blueprint_YakushimaHeadEquip002_4"
    HallowedHeadgearSchematic4 = "Blueprint_YakushimaHeadEquip002_5"
    HallowedHoodSchematic = "Blueprint_YakushimaHeadEquip004"
    HallowedHoodSchematic1 = "Blueprint_YakushimaHeadEquip004_2"
    HallowedHoodSchematic2 = "Blueprint_YakushimaHeadEquip004_3"
    HallowedHoodSchematic3 = "Blueprint_YakushimaHeadEquip004_4"
    HallowedHoodSchematic4 = "Blueprint_YakushimaHeadEquip004_5"
    MonarchSCrownSchematic1 = "Blueprint_Head001_1"
    ZoeSHalloweenCostumeSchematic = "Blueprint_Zoe_Halloweenskin_1"
    MonarchSCrownSchematic2 = "Blueprint_Head001_2"
    MonarchSCrownSchematic3 = "Blueprint_Head001_3"
    MonarchSCrownSchematic4 = "Blueprint_Head001_4"
    BlueprintOfTheKingSCrown5 = "Blueprint_Head001_5"
    GoldenCrownSchematic1 = "Blueprint_Head002_1"
    GoldenCrownSchematic2 = "Blueprint_Head002_2"
    GoldenCrownSchematic3 = "Blueprint_Head002_3"
    GoldenCrownSchematic4 = "Blueprint_Head002_4"
    BlueprintForGoldenCrown5 = "Blueprint_Head002_5"
    LongEaredHeadbandSchematic1 = "Blueprint_Head003_1"
    LongEaredHeadbandSchematic2 = "Blueprint_Head003_2"
    LongEaredHeadbandSchematic3 = "Blueprint_Head003_3"
    LongEaredHeadbandSchematic4 = "Blueprint_Head003_4"
    ITEM5BlueprintsOfLongEaredHeadband = "Blueprint_Head003_5"
    WitchHatSchematic1 = "Blueprint_Head004_1"
    WitchHatSchematic2 = "Blueprint_Head004_2"
    WitchHatSchematic3 = "Blueprint_Head004_3"
    WitchHatSchematic4 = "Blueprint_Head004_4"
    DesignOfWitchHatNo5 = "Blueprint_Head004_5"
    SoftHatSchematic1 = "Blueprint_Head005_1"
    SoftHatSchematic2 = "Blueprint_Head005_2"
    SoftHatSchematic3 = "Blueprint_Head005_3"
    SoftHatSchematic4 = "Blueprint_Head005_4"
    BlueprintOfSoftHat5 = "Blueprint_Head005_5"
    HelmetSchematic1 = "Blueprint_Head006_1"
    HelmetSchematic2 = "Blueprint_Head006_2"
    HelmetSchematic3 = "Blueprint_Head006_3"
    HelmetSchematic4 = "Blueprint_Head006_4"
    BlueprintOfHelmet5 = "Blueprint_Head006_5"
    SilkHatSchematic1 = "Blueprint_Head007_1"
    SilkHatSchematic2 = "Blueprint_Head007_2"
    SilkHatSchematic3 = "Blueprint_Head007_3"
    SilkHatSchematic4 = "Blueprint_Head007_4"
    ITEM5SchematicDiagramsOfTheSilkHat = "Blueprint_Head007_5"
    TricorneSchematic1 = "Blueprint_Head008_1"
    TricorneSchematic2 = "Blueprint_Head008_2"
    TricorneSchematic3 = "Blueprint_Head008_3"
    TricorneSchematic4 = "Blueprint_Head008_4"
    BlueprintOfTheTricornHat5 = "Blueprint_Head008_5"
    ExplorationCapSchematic1 = "Blueprint_Head009_1"
    ExplorationCapSchematic2 = "Blueprint_Head009_2"
    ExplorationCapSchematic3 = "Blueprint_Head009_3"
    ExplorationCapSchematic4 = "Blueprint_Head009_4"
    BlueprintOfExplorationHat5 = "Blueprint_Head009_5"
    GraduationCapSchematic1 = "Blueprint_Head010_1"
    GraduationCapSchematic2 = "Blueprint_Head010_2"
    GraduationCapSchematic3 = "Blueprint_Head010_3"
    GraduationCapSchematic4 = "Blueprint_Head010_4"
    Blueprint5OfUniversityHat = "Blueprint_Head010_5"
    FarmingHatSchematic1 = "Blueprint_Head011_1"
    FarmingHatSchematic2 = "Blueprint_Head011_2"
    FarmingHatSchematic3 = "Blueprint_Head011_3"
    FarmingHatSchematic4 = "Blueprint_Head011_4"
    ITEM5DiagramsOfAgriculturalHat = "Blueprint_Head011_5"
    BowlerHatSchematic1 = "Blueprint_Head012_1"
    BowlerHatSchematic2 = "Blueprint_Head012_2"
    BowlerHatSchematic3 = "Blueprint_Head012_3"
    BowlerHatSchematic4 = "Blueprint_Head012_4"
    BlueprintOfBowlerHat5 = "Blueprint_Head012_5"
    TocotocoCapSchematic1 = "Blueprint_Head013_1"
    TocotocoCapSchematic2 = "Blueprint_Head013_2"
    TocotocoCapSchematic3 = "Blueprint_Head013_3"
    TocotocoCapSchematic4 = "Blueprint_Head013_4"
    DesignPlan5ForTheCrutchliHat = "Blueprint_Head013_5"
    GrinningTocotocoCapSchematic1 = "Blueprint_Head014_1"
    GrinningTocotocoCapSchematic2 = "Blueprint_Head014_2"
    GrinningTocotocoCapSchematic3 = "Blueprint_Head014_3"
    GrinningTocotocoCapSchematic4 = "Blueprint_Head014_4"
    GrinningCurlyHatBlueprint5 = "Blueprint_Head014_5"
    GumossCapSchematic1 = "Blueprint_Head015_1"
    GumossCapSchematic2 = "Blueprint_Head015_2"
    GumossCapSchematic3 = "Blueprint_Head015_3"
    GumossCapSchematic4 = "Blueprint_Head015_4"
    ITEM5BlueprintsOfNaemochiHat = "Blueprint_Head015_5"
    PenkingCapSchematic1 = "Blueprint_Head016_1"
    PenkingCapSchematic2 = "Blueprint_Head016_2"
    PenkingCapSchematic3 = "Blueprint_Head016_3"
    PenkingCapSchematic4 = "Blueprint_Head016_4"
    BlueprintOfCapppenHat5 = "Blueprint_Head016_5"
    KatressCapSchematic1 = "Blueprint_Head017_1"
    KatressCapSchematic2 = "Blueprint_Head017_2"
    KatressCapSchematic3 = "Blueprint_Head017_3"
    KatressCapSchematic4 = "Blueprint_Head017_4"
    DesignBlueprintOfClemenceHat5 = "Blueprint_Head017_5"
    LeezpunkHoodSchematic1 = "Blueprint_HeadEquip025_1"
    LeezpunkHoodSchematic2 = "Blueprint_HeadEquip025_2"
    LeezpunkHoodSchematic3 = "Blueprint_HeadEquip025_3"
    LeezpunkHoodSchematic4 = "Blueprint_HeadEquip025_4"
    UnknownItemBlueprintHeadEquip0255 = "Blueprint_HeadEquip025_5"
    KillamariCapSchematic1 = "Blueprint_HeadEquip026_1"
    KillamariCapSchematic2 = "Blueprint_HeadEquip026_2"
    KillamariCapSchematic3 = "Blueprint_HeadEquip026_3"
    KillamariCapSchematic4 = "Blueprint_HeadEquip026_4"
    UnknownItemBlueprintHeadEquip0265 = "Blueprint_HeadEquip026_5"
    RibbunyHeadbandSchematic1 = "Blueprint_HeadEquip028_1"
    RibbunyHeadbandSchematic2 = "Blueprint_HeadEquip028_2"
    RibbunyHeadbandSchematic3 = "Blueprint_HeadEquip028_3"
    RibbunyHeadbandSchematic4 = "Blueprint_HeadEquip028_4"
    UnknownItemBlueprintHeadEquip0285 = "Blueprint_HeadEquip028_5"
    SweeCapSchematic1 = "Blueprint_HeadEquip031_1"
    SweeCapSchematic2 = "Blueprint_HeadEquip031_2"
    SweeCapSchematic3 = "Blueprint_HeadEquip031_3"
    SweeCapSchematic4 = "Blueprint_HeadEquip031_4"
    UnknownItemBlueprintHeadEquip0315 = "Blueprint_HeadEquip031_5"
    DazziHatSchematic1 = "Blueprint_HeadEquip032_1"
    DazziHatSchematic2 = "Blueprint_HeadEquip032_2"
    DazziHatSchematic3 = "Blueprint_HeadEquip032_3"
    DazziHatSchematic4 = "Blueprint_HeadEquip032_4"
    UnknownItemBlueprintHeadEquip0325 = "Blueprint_HeadEquip032_5"
    BellanoirSSlabFragment = "PalSummon_NightLady_Parts"
    BellanoirLiberoSSlabFragment = "PalSummon_NightLady_Dark_Parts"
    BlazamutRyuSlabFragment = "PalSummon_KingBahamut_Dragon_Parts"
    XenolordSlabFragment = "PalSummon_DarkMechaDragon_Parts"
    HartalisSlabFragment = "PalSummon_LegendDeer_Parts"
    BellanoirLiberoUltraSlabFragment = "PalSummon_NightLady_Dark_Parts_2"
    BlazamutRyuUltraSlabFragment = "PalSummon_KingBahamut_Dragon_Parts_2"
    XenolordUltraSlabFragment = "PalSummon_DarkMechaDragon_Parts_2"
    HartalisUltraSlabFragment = "PalSummon_LegendDeer_Parts_2"
    BellanoirSSlab = "PalSummon_NightLady"
    BellanoirLiberoSSlab = "PalSummon_NightLady_Dark"
    BlazamutRyuSlab = "PalSummon_KingBahamut_Dragon"
    XenolordSlab = "PalSummon_DarkMechaDragon"
    CelestialSigil = "PalSummon_YakushimaBoss002"
    HartalisSlab = "PalSummon_LegendDeer"
    BellanoirLiberoUltraSlab = "PalSummon_NightLady_Dark_2"
    BlazamutRyuUltraSlab = "PalSummon_KingBahamut_Dragon_2"
    XenolordUltraSlab = "PalSummon_DarkMechaDragon_2"
    CelestialSigilMaster = "PalSummon_YakushimaBoss002_2"
    HartalisUltraSlab = "PalSummon_LegendDeer_2"
    PowerfulFishingMagnet = "Salvage_TreasureBoxKey02"
    RayneSyndicateFlagSchematic = "Blueprint_Hunter_GangFlag"
    LyleenStatueSchematic = "Blueprint_LilyQueenStatue"
    FreePalAllianceFlagSchematic = "Blueprint_ConservationGroupBannerA"
    FreePalAllianceBannerSchematic = "Blueprint_ConservationGroupBannerB"
    WireFenceSchematic = "Blueprint_Wire_Fence"
    WoodenBarricadeSchematic = "Blueprint_WoodenBarricade"
    MajesticWallTorchSchematic = "Blueprint_WallTorch02"
    CeremonialCandlestickSchematic = "Blueprint_FireStand"
    MajesticCandlestickSchematic = "Blueprint_CandleStand"
    PaperLanternSchematic = "Blueprint_LanternTop"
    RedWoodenLanternSchematic = "Blueprint_Shrine_Lantern"
    YakumoStatueSchematic = "Blueprint_GuardianDogStatue"
    LaboratoryDeskSchematic = "Blueprint_SF_Desk"
    LaboratoryChairSchematic = "Blueprint_SF_Chair"
    MoonLordStatueSchematic = "Blueprint_YakushimaBoss002_Relic"
    CelestialSigilSchematic = "Blueprint_PalSummon_YakushimaBoss002"
    BeginnerFishingRodGumossSchematic = "Blueprint_FishingRod_01_2"
    IntermediateFishingRodCroajiroSchematic = "Blueprint_FishingRod_02_2"
    AdvancedFishingRodDepressoSchematic = "Blueprint_FishingRod_03_2"
    UnknownItemBlueprintSalvageTreasureBoxKey01 = "Blueprint_Salvage_TreasureBoxKey01"
    UnknownItemBlueprintSalvageFishingBait1A = "Blueprint_Salvage_FishingBait_1_A"
    UnknownItemBlueprintSalvageFishingBait1B = "Blueprint_Salvage_FishingBait_1_B"
    UnknownItemBlueprintSalvageFishingBait2A = "Blueprint_Salvage_FishingBait_2_A"
    UnknownItemBlueprintSalvageFishingBait2B = "Blueprint_Salvage_FishingBait_2_B"
    UnknownItemBlueprintSalvageFishingBait3B = "Blueprint_Salvage_FishingBait_3_B"
    AnimalSkin = "AnimalSkin"
    EnText1 = "AnimalSkin2"
    EnText63 = "Scales"
    EnText64 = "Scales2"
    EnText5 = "Bat_NPC"
    EnText7 = "Berries2"
    EnText9 = "CaptureRope"
    Claw = "Claws"
    EnText12 = "Claws2"
    EnText13 = "ClawsPendant"
    EnText14 = "ClothHat"
    EnText27 = "ElectronicCircuit"
    EnText28 = "EnergyDrink"
    Fang = "Fang"
    EnText29 = "Fang2"
    EnText30 = "FangNecklace"
    EnText31 = "FarmCrop_Tmp"
    EnText32 = "FishMeat"
    EnText33 = "FishMeat2"
    EnText35 = "Flint"
    GrilledMeat = "GrilledMeat"
    Gunpowder = "Gunpowder"
    EnText40 = "Handgun_NPC"
    EnText45 = "LaserRifle_NPC"
    EnText41 = "IronOre"
    EnText43 = "Kitsunebi_Fire"
    EnText44 = "LargeBullet"
    EnText47 = "Leather2"
    RawMeat = "Meat"
    EnText49 = "Meat2"
    RadarSphere = "PalSphere_Robbery"
    PalSphereDebug = "PalSphere_Debug"
    EnText56 = "PenguinLauncher"
    EnText61 = "RocketLauncher_NPC"
    EnText70 = "SniperRifle_Default"
    EnText2AssaultRifleNPC = "AssaultRifle_NPC"
    EnText3 = "AssaultRifle_NPC_GrassBoss"
    EnText8 = "BowGun_NPC"
    EnText65 = "Seed_Tmp"
    EnText66 = "Sharkkid_Scale"
    EnText68 = "Shotgun_NPC"
    EnText34 = "FlameThrower_NPC"
    EnText37 = "GatlingGun_NPC"
    EnText36 = "FragGrenade_NPC"
    EnText69 = "SmallBullet"
    PaldiumClump = "Pal_crystal_L"
    EnText54 = "PAL_Growth_Stone_S"
    EnText53 = "PAL_Growth_Stone_M"
    EnText52 = "PAL_Growth_Stone_L"
    EnText55 = "PAL_Growth_Stone_XL"
    Dung = "Unko_S"
    HugeDung = "Unko_L"
    EnText71 = "ThrowStone"
    EnText72 = "VenisonBoiledInTomato"
    EnText73 = "WaterBucket"
    EnText60 = "RecurveBow"
    PotatoSeedPotatoes = "PotatoSeedPotatoes"
    EnText58 = "Potato_old"
    EnText15 = "Corn"
    EnText59 = "Pumpkin"
    EnText4BakedPotato = "Baked_Potato"
    Computer = "Computer"
    Grape = "Grape"
    Hop = "Hop"
    Potage = "Potage"
    Curry = "Curry_old"
    Cheeseburger = "CheeseBurger"
    Sandwich = "Sandwich"
    CornSoup = "CornSoup"
    Stew = "Stew"
    GrilledFish = "GrilledFish"
    SeafoodSoup = "SeafoodSoup"
    LuxuryOmelette = "LuxuryOmelette"
    Beer = "Beer"
    Wine = "Wine"
    AntibioticNormal = "Antibiotic_Normal"
    AntibioticGood = "Antibiotic_Good"
    AntibioticSuper = "Antibiotic_Super"
    FishingRodOld = "FishingRod_Old"
    FishingRodGood = "FishingRod_Good"
    FishingRodSuper = "FishingRod_Super"
    FishingRodLegendary = "FishingRod_Legendary"
    HyperGlider = "Glider_Legendary"
    UnknownItemPVGliderManta = "PV_Glider_Manta"
    LightzHelmet = "LightzHelmet"
    GasMask = "GasMask"
    NightVisionGoggles = "NightVisionGoggles"
    EnText10 = "CashFang"
    EnText11 = "CashScales"
    EnText24 = "Debug_Handgun_Poison"
    EnText17 = "Debug_Handgun_Burn"
    EnText26 = "Debug_Handgun_Wetness"
    EnText21 = "Debug_Handgun_Freeze"
    EnText20 = "Debug_Handgun_Electrical"
    EnText23 = "Debug_Handgun_Muddy"
    EnText22 = "Debug_Handgun_IvyCling"
    EnText18 = "Debug_Handgun_Darkness"
    EnText25 = "Debug_Handgun_Stun"
    EnText16 = "Debug_Handgun_AttackUp"
    EnText19 = "Debug_Handgun_DefenseUp"
    EnText = "AirGrapplingGun"
    DragostropheSShotgun = "SkillUnlock_BlackFurDragon"
    BoltmaneSaddle = "SkillUnlock_ElecLion"
    EnTextSPowerConverter = "SkillUnlock_DarkMutant"
    EnText62 = "Sand"
    DarkSkillFruitPsychoGravity = "SkillCard_Psychokinesis"
    EnText51 = "MonsterEquipWeapon_Dummy"
    EnText48 = "MateItem01"
    UnknownItemBlueprintTest = "BlueprintTest"
    SummoningAltar = "PalSummon"
    EnText50 = "MissileLauncher_NPC"
    EnText39 = "GrenadeLauncher_NPC"
    UNKNOWN = "Gasoline"
    ITEM1 = "Propellant"
    DogCoin = "DogCoin"
    EnText42 = "Katana_NPC"
    EnText6 = "BelieverFatCane"
    UnknownItemPalGenderReverseTest = "PalGenderReverseTest"
    UnknownItemPalPassiveSkillChangeTest = "PalPassiveSkillChangeTest"
    UnknownItemPalPassiveSkillChangeTest2 = "PalPassiveSkillChangeTest2"
    UnknownItemTESTCaptureItemModifier = "TEST_CaptureItemModifier"
    UnknownItemFishingRodTest = "FishingRod_Test"
    EnText38 = "GatlingGun_NPC_GrassBoss"
    UnknownItemSweetCaramel = "Sweet_Caramel"
    LifmunkEffigy = "Relic"
    HipLantern = "Lantern"
    EnhancedHipLantern = "Lantern_High"
    SmallFeedBag = "AutoMealPouch_Tier1"
    AverageFeedBag = "AutoMealPouch_Tier2"
    LargeFeedBag = "AutoMealPouch_Tier3"
    HugeFeedBag = "AutoMealPouch_Tier4"
    GiantFeedBag = "AutoMealPouch_Tier5"
    MysteriousAccessoryBox = "UnlockEquipmentSlot_Accessory_01"
    BoxOfMysteryAccessories = "UnlockEquipmentSlot_Accessory_02"
    LockpickingToolV1 = "Unlock_Picking_Tier1"
    LockpickingToolV2 = "Unlock_Picking_Tier2"
    LockpickingToolV3 = "Unlock_Picking_Tier3"
    JolthogSGloves = "SkillUnlock_Hedgehog"
    JolthogCrystSGloves = "SkillUnlock_Hedgehog_Ice"
    FoxparksHarness = "SkillUnlock_Kitsunebi"
    FoxparksCrystSHarness = "SkillUnlock_Kitsunebi_Ice"
    MelpacaSaddle = "SkillUnlock_Alpaca"
    SweepaSaddle = "SkillUnlock_MopKing"
    RushoarSaddle = "SkillUnlock_Boar"
    CelaraySGloves = "SkillUnlock_FlyingManta"
    CelarayLuxSGloves = "SkillUnlock_FlyingManta_Thunder"
    LifmunkSSubmachineGun = "SkillUnlock_Carbunclo"
    DirehowlSSaddledHarness = "SkillUnlock_Garm"
    TanzeeSAssaultRifle = "SkillUnlock_Monkey"
    UnknownItemSkillUnlockMonkeyIce = "SkillUnlock_Monkey_Ice"
    SurfentSaddle = "SkillUnlock_Serpent"
    SurfentTerraSaddle = "SkillUnlock_Serpent_Ground"
    EikthyrdeerSaddle = "SkillUnlock_Deer"
    EikthyrdeerTerraSaddle = "SkillUnlock_Deer_Ground"
    GrintaleSaddle = "SkillUnlock_NaughtyCat"
    HerbilSHarness = "SkillUnlock_LeafMomonga"
    PolapupSaddle = "SkillUnlock_IceSeal"
    UnivoltSaddle = "SkillUnlock_Kirin"
    UnknownItemSkillUnlockKirinIce = "SkillUnlock_Kirin_Ice"
    KillamariSGloves = "SkillUnlock_NegativeOctopus"
    KillamariPrimoSGloves = "SkillUnlock_NegativeOctopus_Neutral"
    TocotocoSGloves = "SkillUnlock_ColorfulBird"
    NitewingSaddle = "SkillUnlock_HawkBird"
    ArsoxSaddle = "SkillUnlock_FlameBuffalo"
    FlopieSNecklace = "SkillUnlock_FlowerRabbit"
    DigtoiseSHeadband = "SkillUnlock_DrillGame"
    PengulletRocketLauncher = "SkillUnlock_Penguin"
    PengulletLuxSRocketLauncher = "SkillUnlock_Penguin_Electric"
    DinossomSaddle = "SkillUnlock_FlowerDinosaur"
    DinossomLuxSaddle = "SkillUnlock_FlowerDinosaur_Electric"
    DaedreamSNecklace = "SkillUnlock_DreamDemon"
    BroncherrySaddle = "SkillUnlock_SakuraSaurus"
    BroncherryAquaSaddle = "SkillUnlock_SakuraSaurus_Water"
    VanwyrmSaddle = "SkillUnlock_BirdDragon"
    VanwyrmCrystSaddle = "SkillUnlock_BirdDragon_Ice"
    ChilletSaddle = "SkillUnlock_WeaselDragon"
    ChilletIgnisSaddle = "SkillUnlock_WeaselDragon_Fire"
    HangyuSGloves = "SkillUnlock_WindChimes"
    HangyuCrystSGlove = "SkillUnlock_WindChimes_Ice"
    KingpacaSaddle = "SkillUnlock_KingAlpaca"
    KingpacaCrystSaddle = "SkillUnlock_KingAlpaca_Ice"
    ElphidranSaddle = "SkillUnlock_FairyDragon"
    ElphidranAquaSaddle = "SkillUnlock_FairyDragon_Water"
    DazziSNecklace = "SkillUnlock_RaijinDaughter"
    DazziNoctSNecklace = "SkillUnlock_RaijinDaughter_Water"
    DazemuSaddle = "SkillUnlock_FeatherOstrich"
    GaleclawSGloves = "SkillUnlock_Eagle"
    MaraithSaddle = "SkillUnlock_GhostBeast"
    GhanglerSaddle = "SkillUnlock_GhostAnglerfish"
    GhanglerIgnisSaddle = "SkillUnlock_GhostAnglerfish_Fire"
    BralohaSaddle = "SkillUnlock_Plesiosaur"
    PalumbaSaddle = "SkillUnlock_TropicalOstrich"
    MossandaSGrenadeLauncher = "SkillUnlock_GrassPanda"
    MossandaLuxSGrenadeLauncher = "SkillUnlock_GrassPanda_Electric"
    TarantrissSaddle = "SkillUnlock_PurpleSpider"
    ReptyroSaddle = "SkillUnlock_VolcanicMonster"
    ReptyroCrystSaddle = "SkillUnlock_VolcanicMonster_Ice"
    PyrinSaddle = "SkillUnlock_FireKirin"
    PyrinNoctSaddle = "SkillUnlock_FireKirin_Dark"
    MammorestSaddle = "SkillUnlock_GrassMammoth"
    MammorestCrystSaddle = "SkillUnlock_GrassMammoth_Ice"
    AzurobeSaddle = "SkillUnlock_BlueDragon"
    AzurobeCrystSaddle = "SkillUnlock_BlueDragon_Ice"
    JormuntideSaddle = "SkillUnlock_Umihebi"
    JormuntideIgnisSaddle = "SkillUnlock_Umihebi_Fire"
    KitsunSaddle = "SkillUnlock_AmaterasuWolf"
    KitsunNoctSaddle = "SkillUnlock_AmaterasuWolf_Dark"
    RayhoundSaddle = "SkillUnlock_ThunderDog"
    UnknownItemSkillUnlockThunderDogIce = "SkillUnlock_ThunderDog_Ice"
    BlazehowlSaddle = "SkillUnlock_Manticore"
    BlazehowlNoctSaddle = "SkillUnlock_Manticore_Dark"
    ReindrixSaddle = "SkillUnlock_IceDeer"
    BeakonSaddle = "SkillUnlock_ThunderBird"
    RagnahawkSaddle = "SkillUnlock_RedArmorBird"
    FalerisSaddle = "SkillUnlock_Horus"
    FalerisAquaSaddle = "SkillUnlock_Horus_Water"
    QuivernSaddle = "SkillUnlock_SkyDragon"
    QuivernBotanSaddle = "SkillUnlock_SkyDragon_Grass"
    HelzephyrSaddle = "SkillUnlock_HadesBird"
    HelzephyrLuxSaddle = "SkillUnlock_HadesBird_Electric"
    FenglopeSaddle = "SkillUnlock_FengyunDeeper"
    FenglopeLuxSaddle = "SkillUnlock_FengyunDeeper_Electric"
    SuzakuSaddle = "SkillUnlock_Suzaku"
    SuzakuAquaSaddle = "SkillUnlock_Suzaku_Water"
    YakumoSaddle = "SkillUnlock_GuardianDog"
    BlazamutSaddle = "SkillUnlock_KingBahamut"
    BlazamutRyuSaddle = "SkillUnlock_KingBahamut_Dragon"
    WumpoSaddle = "SkillUnlock_Yeti"
    WumpoBotanSaddle = "SkillUnlock_Yeti_Grass"
    WhalaskaSaddle = "SkillUnlock_IceNarwhal"
    WhalaskaIgnisSaddle = "SkillUnlock_IceNarwhal_Fire"
    UnknownItemSkillUnlockGrassGolem = "SkillUnlock_GrassGolem"
    UnknownItemSkillUnlockGrassGolemDark = "SkillUnlock_GrassGolem_Dark"
    UnknownItemSkillUnlockPyramidTurtle = "SkillUnlock_PyramidTurtle"
    UnknownItemSkillUnlockKingSunfish = "SkillUnlock_KingSunfish"
    UnknownItemSkillUnlockSumoDog = "SkillUnlock_SumoDog"
    GrizzboltSMinigun = "SkillUnlock_ElecPanda"
    ShadowbeakSaddle = "SkillUnlock_BlackGriffon"
    AstegonSaddle = "SkillUnlock_BlackMetalDragon"
    RelaxaurusMissileLauncher = "SkillUnlock_LazyDragon"
    RelaxaurusLuxSMissileLauncher = "SkillUnlock_LazyDragon_Electric"
    ShroomerSaddle = "SkillUnlock_MushroomDragon"
    ShroomerNoctSaddle = "SkillUnlock_MushroomDragon_Dark"
    FrostallionSaddle = "SkillUnlock_IceHorse"
    FrostallionNoctSaddle = "SkillUnlock_IceHorse_Dark"
    PaladiusSaddle = "SkillUnlock_SaintCentaur"
    NecromusSaddle = "SkillUnlock_BlackCentaur"
    JetragonSMissileLauncher = "SkillUnlock_JetDragon"
    XenogardSaddle = "SkillUnlock_WhiteAlienDragon"
    SelyneSaddle = "SkillUnlock_MoonQueen"
    SmokieSHarness = "SkillUnlock_BlackPuppy"
    UnknownItemSkillUnlockBlackPuppyIce = "SkillUnlock_BlackPuppy_Ice"
    StarryonSaddle = "SkillUnlock_NightBlueHorse"
    UnknownItemSkillUnlockNightBlueHorseNeutral = "SkillUnlock_NightBlueHorse_Neutral"
    AzurmaneSaddle = "SkillUnlock_BlueThunderHorse"
    GildaneSaddle = "SkillUnlock_GoldenHorse"
    NyafiaSShotgun = "SkillUnlock_BadCatgirl"
    CelesdirSaddle = "SkillUnlock_WhiteDeer"
    SilvegisSaddle = "SkillUnlock_WhiteShieldDragon"
    BastigorSHammer = "SkillUnlock_SnowTigerBeastman"
    XenolordSaddle = "SkillUnlock_DarkMechaDragon"
    NeptiliusSaddle = "SkillUnlock_PoseidonOrca"
    UnknownItemSkillUnlockVolcanoDragon = "SkillUnlock_VolcanoDragon"
    HartalisSaddle = "SkillUnlock_LegendDeer"
    SmallPouch = "AdditionalInventory_001"
    MediumPouch = "AdditionalInventory_002"
    LargePouch = "AdditionalInventory_003"
    GiantPouch = "AdditionalInventory_004"
    HeavyWeightModule = "SphereModule_Heavy"
    CurveModule = "SphereModule_Curve"
    SniperModule = "SphereModule_Sniper"
    SliderModule = "SphereModule_Curve2"
    SniperModuleSphereModuleSniper2 = "SphereModule_Sniper2"
    HomingModule = "SphereModule_Homing"
    UnknownItemTESTBossDefeatReward = "TEST_BossDefeatReward"
    ChilletBountyToken = "BossDefeatReward_WeaselDragon"
    SweepaBountyToken = "BossDefeatReward_MopKing"
    GumossBountyToken = "BossDefeatReward_PlantSlime"
    DumudBountyToken = "BossDefeatReward_LazyCatfish"
    PenkingBountyToken = "BossDefeatReward_CaptainPenguin"
    AzurobeBountyToken = "BossDefeatReward_BlueDragon"
    GrintaleBountyToken = "BossDefeatReward_NaughtyCat"
    NitewingBountyToken = "BossDefeatReward_HawkBird"
    QuivernBountyToken = "BossDefeatReward_SkyDragon"
    FelbatBountyToken = "BossDefeatReward_CatVampire"
    KingpacaBountyToken = "BossDefeatReward_KingAlpaca"
    BroncherryBountyToken = "BossDefeatReward_SakuraSaurus"
    KatressBountyToken = "BossDefeatReward_CatMage"
    BushiBountyToken = "BossDefeatReward_Ronin"
    FenglopeBountyToken = "BossDefeatReward_FengyunDeeper"
    PetalliaBountyToken = "BossDefeatReward_FlowerDoll"
    BeakonBountyToken = "BossDefeatReward_ThunderBird"
    WarsectBountyToken = "BossDefeatReward_HerculesBeetle"
    BroncherryAquaBountyToken = "BossDefeatReward_SakuraSaurus_Water"
    ElphidranBountyToken = "BossDefeatReward_FairyDragon"
    RelaxaurusBountyToken = "BossDefeatReward_LazyDragon_Electric"
    UnivoltBountyToken = "BossDefeatReward_Kirin"
    ElizabeeBountyToken = "BossDefeatReward_QueenBee"
    MossandaLuxBountyToken = "BossDefeatReward_GrassPanda_Electric"
    LunarisBountyToken = "BossDefeatReward_Mutant"
    VerdashBountyToken = "BossDefeatReward_GrassRabbitMan"
    WumpoBotanBountyToken = "BossDefeatReward_Yeti_Grass"
    MammorestBountyToken = "BossDefeatReward_GrassMammoth"
    VaeletBountyToken = "BossDefeatReward_VioletFairy"
    SibelyxBountyToken = "BossDefeatReward_WhiteMoth"
    MenastingBountyToken = "BossDefeatReward_DarkScorpion"
    SuzakuBountyToken = "BossDefeatReward_Suzaku"
    JormuntideBountyToken = "BossDefeatReward_Umihebi"
    IceKingpacaBountyToken = "BossDefeatReward_KingAlpaca_Ice"
    DinossomLuxBountyToken = "BossDefeatReward_FlowerDinosaur_Electric"
    AnubisBountyToken = "BossDefeatReward_Anubis"
    AstegonBountyToken = "BossDefeatReward_BlackMetalDragon"
    BlazamutBountyToken = "BossDefeatReward_KingBahamut"
    LyleenNoctBountyToken = "BossDefeatReward_LilyQueen_Dark"
    MenastingTerraBountyToken = "BossDefeatReward_DarkScorpion_Ground"
    KnocklemBountyToken = "BossDefeatReward_WingGolem"
    SplatterinaBountyToken = "BossDefeatReward_GrimGirl"
    AzurmaneBountyToken = "BossDefeatReward_BlueThunderHorse"
    KitsunNoctBountyToken = "BossDefeatReward_AmaterasuWolf_Dark"
    FenglopeLuxBountyToken = "BossDefeatReward_FengyunDeeper_Electric"
    CelesdirBountyToken = "BossDefeatReward_WhiteDeer"
    SilvegisBountyToken = "BossDefeatReward_WhiteShieldDragon"
    FalerisAquaBountyToken = "BossDefeatReward_Horus_Water"
    JetragonBountyToken = "BossDefeatReward_JetDragon"
    FrostallionBountyToken = "BossDefeatReward_IceHorse"
    TwinKnightsBountyToken = "BossDefeatReward_SaintCentaur"
    SmokieBountyToken = "BossDefeatReward_BlackPuppy"
    NitemaryBountyToken = "BossDefeatReward_GhostRabbit"
    StarryonBountyToken = "BossDefeatReward_NightBlueHorse"
    PruneliaBountyToken = "BossDefeatReward_BlueberryFairy"
    NyafiaBountyToken = "BossDefeatReward_BadCatgirl"
    GildaneBountyToken = "BossDefeatReward_GoldenHorse"
    OmasculBountyToken = "BossDefeatReward_MysteryMask"
    TarantrisBountyToken = "BossDefeatReward_PurpleSpider"
    FrostallionNoctBountyToken = "BossDefeatReward_IceHorse_Dark"
    FoxparksCrystBountyToken = "BossDefeatReward_Kitsunebi_Ice"
    DazziNoctBountyToken = "BossDefeatReward_RaijinDaughter_Water"
    CryolinxTerraBountyToken = "BossDefeatReward_WhiteTiger_Ground"
    CaprityNoctBountyToken = "BossDefeatReward_BerryGoat_Dark"
    LoupmoonCrystBountyToken = "BossDefeatReward_Werewolf_Ice"
    RibbunyBotanBountyToken = "BossDefeatReward_PinkRabbit_Grass"
    WarsectTerraBountyToken = "BossDefeatReward_HerculesBeetle_Ground"
    WhalaskaBountyToken = "BossDefeatReward_IceNarwhal"
    NeptiliusBountyToken = "BossDefeatReward_PoseidonOrca"
    WhalaskaIgnisBountyToken = "BossDefeatReward_IceNarwhal_Fire"
    FarmerSSpecialDish = "QuestItem_Farmer_1"
    ZoeSTatteredMemento = "QuestItem_Zoe_1"
    ZoeSHalloweenCostume = "QuestItem_Zoe_Halloweenskin_1"
    BreederSPreciousPal = "QuestItem_Breeder_1"
    TreasureMap = "TreasureMap01"
    TreasureMap1 = "TreasureMap02"
    TreasureMap2 = "TreasureMap03"
    TreasureMap3 = "TreasureMap04"
    TreasureMap4 = "TreasureMap05"
    ChampionSEmblem = "PlayerDropItem"

ITEM_ID_TO_NAME = {
    ItemId.GoldCoin: "Gold Coin",
    ItemId.PalSphere: "Pal Sphere",
    ItemId.MegaSphere: "Mega Sphere",
    ItemId.GigaSphere: "Giga Sphere",
    ItemId.HyperSphere: "Hyper Sphere",
    ItemId.UltraSphere: "Ultra Sphere",
    ItemId.LegendarySphere: "Legendary Sphere",
    ItemId.UltimateSphere: "Ultimate Sphere",
    ItemId.ExoticSphere: "Exotic Sphere",
    ItemId.Arrow: "Arrow",
    ItemId.PoisonArrow: "Poison Arrow",
    ItemId.FireArrow: "Fire Arrow",
    ItemId.ReinforcedArrow: "Reinforced Arrow",
    ItemId.AdvancedArrow: "Advanced Arrow",
    ItemId.CoarseAmmo: "Coarse Ammo",
    ItemId.HandgunAmmo: "Handgun Ammo",
    ItemId.MagnumAmmo: "Magnum Ammo",
    ItemId.RifleAmmo: "Rifle Ammo",
    ItemId.ShotgunShell: "Shotgun Shell",
    ItemId.MachineGunAmmo: "Machine Gun Ammo",
    ItemId.AssaultRifleAmmo: "Assault Rifle Ammo",
    ItemId.RocketAmmo: "Rocket Ammo",
    ItemId.DecalInk: "Decal Ink",
    ItemId.FlamethrowerFuel: "Flamethrower Fuel",
    ItemId.MissileAmmo: "Missile Ammo",
    ItemId.GrenadeAmmo: "Grenade Ammo",
    ItemId.GatlingGunAmmo: "Gatling Gun Ammo",
    ItemId.MeteoriteAmmo: "Meteorite Ammo",
    ItemId.EnergyCartridge: "Energy Cartridge",
    ItemId.PlasmaCartridge: "Plasma Cartridge",
    ItemId.LaserGatlingCartridge: "Laser Gatling Cartridge",
    ItemId.ChargeRifleAmmo: "Charge Rifle Ammo",
    ItemId.OverheatRifleAmmo: "Overheat Rifle Ammo",
    ItemId.EnergyShotgunAmmo: "Energy Shotgun Ammo",
    ItemId.BoostGunAmmo: "Boost Gun Ammo",
    ItemId.SimpleBait: "Simple Bait",
    ItemId.HighQualityBait: "High Quality Bait",
    ItemId.DeluxeBait: "Deluxe Bait",
    ItemId.BeginnerBait: "Beginner Bait",
    ItemId.SweetBait: "Sweet Bait",
    ItemId.LuckyBait: "Lucky Bait",
    ItemId.QuickBait: "Quick Bait",
    ItemId.AlluringBait: "Alluring Bait",
    ItemId.RiskyBait: "Risky Bait",
    ItemId.WoodenClub: "Wooden Club",
    ItemId.HandHeldTorch: "Hand-Held Torch",
    ItemId.Bat: "Bat",
    ItemId.StoneAxe: "Stone Axe",
    ItemId.MetalAxe: "Metal Axe",
    ItemId.RefinedMetalAxe: "Refined Metal Axe",
    ItemId.Axe4: "Axe4",
    ItemId.PalMetalAxe: "Pal Metal Axe",
    ItemId.StonePickaxe: "Stone Pickaxe",
    ItemId.MetalPickaxe: "Metal Pickaxe",
    ItemId.RefinedMetalPickaxe: "Refined Metal Pickaxe",
    ItemId.EnText2: "en Text +2",
    ItemId.PalMetalPickaxe: "Pal Metal Pickaxe",
    ItemId.StoneSpear: "Stone Spear",
    ItemId.MetalSpear: "Metal Spear",
    ItemId.RefinedMetalSpear: "Refined Metal Spear",
    ItemId.ElizabeeSStaff: "Elizabee's Staff",
    ItemId.BeegardeSSpear: "Beegarde's Spear",
    ItemId.LilySSpear: "Lily's Spear",
    ItemId.LilySSpear4: "Lily's Spear +4",
    ItemId.Sword: "Sword",
    ItemId.Sword1: "Sword +1",
    ItemId.Sword2: "Sword +2",
    ItemId.Sword3: "Sword +3",
    ItemId.Sword4: "Sword +4",
    ItemId.Katana: "Katana",
    ItemId.Katana1: "Katana +1",
    ItemId.Katana2: "Katana +2",
    ItemId.Katana3: "Katana +3",
    ItemId.Katana4: "Katana +4",
    ItemId.BeamSword: "Beam Sword",
    ItemId.BeamSword1: "Beam Sword +1",
    ItemId.BeamSword2: "Beam Sword +2",
    ItemId.BeamSword3: "Beam Sword +3",
    ItemId.BeamSword4: "Beam Sword +4",
    ItemId.Meowmere: "Meowmere",
    ItemId.MeatCleaver: "Meat Cleaver",
    ItemId.StunBaton: "Stun Baton",
    ItemId.MetalDetector: "Metal Detector",
    ItemId.OldBow: "Old Bow",
    ItemId.OldBow1: "Old Bow +1",
    ItemId.OldBow2: "Old Bow +2",
    ItemId.OldBow3: "Old Bow +3",
    ItemId.OldBow4: "Old Bow +4",
    ItemId.PoisonBow: "Poison Bow",
    ItemId.FireBow: "Fire Bow",
    ItemId.ThreeShotBow: "Three Shot Bow",
    ItemId.FiveShotBow: "Five Shot Bow",
    ItemId.Crossbow: "Crossbow",
    ItemId.Crossbow1: "Crossbow +1",
    ItemId.Crossbow2: "Crossbow +2",
    ItemId.Crossbow3: "Crossbow +3",
    ItemId.Crossbow4: "Crossbow +4",
    ItemId.PoisonArrowCrossbow: "Poison Arrow Crossbow",
    ItemId.FireArrowCrossbow: "Fire Arrow Crossbow",
    ItemId.PoisonArrowCrossbow1: "Poison Arrow Crossbow +1",
    ItemId.PoisonArrowCrossbow2: "Poison Arrow Crossbow +2",
    ItemId.PoisonArrowCrossbow3: "Poison Arrow Crossbow +3",
    ItemId.PoisonArrowCrossbow4: "Poison Arrow Crossbow +4",
    ItemId.FireArrowCrossbow1: "Fire Arrow Crossbow +1",
    ItemId.FireArrowCrossbow2: "Fire Arrow Crossbow +2",
    ItemId.FireArrowCrossbow3: "Fire Arrow Crossbow +3",
    ItemId.FireArrowCrossbow4: "Fire Arrow Crossbow +4",
    ItemId.CompoundBow: "Compound Bow",
    ItemId.CompoundBow1: "Compound Bow +1",
    ItemId.CompoundBow2: "Compound Bow +2",
    ItemId.CompoundBow3: "Compound Bow +3",
    ItemId.CompoundBow4: "Compound Bow +4",
    ItemId.AdvancedBow: "Advanced Bow",
    ItemId.AdvancedBow1: "Advanced Bow +1",
    ItemId.AdvancedBow2: "Advanced Bow +2",
    ItemId.AdvancedBow3: "Advanced Bow +3",
    ItemId.AdvancedBow4: "Advanced Bow +4",
    ItemId.MakeshiftHandgun: "Makeshift Handgun",
    ItemId.MakeshiftHandgun1: "Makeshift Handgun +1",
    ItemId.MakeshiftHandgun2: "Makeshift Handgun +2",
    ItemId.MakeshiftHandgun3: "Makeshift Handgun +3",
    ItemId.MakeshiftHandgun4: "Makeshift Handgun +4",
    ItemId.Handgun: "Handgun",
    ItemId.Handgun1: "Handgun +1",
    ItemId.Handgun2: "Handgun +2",
    ItemId.Handgun3: "Handgun +3",
    ItemId.Handgun4: "Handgun +4",
    ItemId.DecalGun1: "Decal Gun 1",
    ItemId.DecalGun2: "Decal Gun 2",
    ItemId.DecalGun3: "Decal Gun 3",
    ItemId.DecalGun4: "Decal Gun 4",
    ItemId.DecalGun5: "Decal Gun 5",
    ItemId.OldRevolver: "Old Revolver",
    ItemId.OldRevolver1: "Old Revolver +1",
    ItemId.OldRevolver2: "Old Revolver +2",
    ItemId.OldRevolver3: "Old Revolver +3",
    ItemId.OldRevolver4: "Old Revolver +4",
    ItemId.BoostGun: "Boost Gun",
    ItemId.MegaboostGun: "Megaboost Gun",
    ItemId.BoostGun2: "Boost Gun +2",
    ItemId.GrapplingGun: "Grappling Gun",
    ItemId.MegaGrapplingGun: "Mega Grappling Gun",
    ItemId.GigaGrapplingGun: "Giga Grappling Gun",
    ItemId.HyperGrapplingGun: "Hyper Grappling Gun",
    ItemId.UltraGrapplingGun: "Ultra Grappling Gun",
    ItemId.UnknownItemHandgunShield: "Unknown Item (HandgunShield)",
    ItemId.MakeshiftShotgun: "Makeshift Shotgun",
    ItemId.MakeshiftShotgun1: "Makeshift Shotgun +1",
    ItemId.MakeshiftShotgun2: "Makeshift Shotgun +2",
    ItemId.MakeshiftShotgun3: "Makeshift Shotgun +3",
    ItemId.MakeshiftShotgun4: "Makeshift Shotgun +4",
    ItemId.DoubleBarreledShotgun: "Double-Barreled Shotgun",
    ItemId.DoubleBarreledShotgun1: "Double-Barreled Shotgun +1",
    ItemId.DoubleBarreledShotgun2: "Double-Barreled Shotgun +2",
    ItemId.DoubleBarreledShotgun3: "Double-Barreled Shotgun +3",
    ItemId.DoubleBarreledShotgun4: "Double-Barreled Shotgun +4",
    ItemId.PumpActionShotgun: "Pump-Action Shotgun",
    ItemId.PumpActionShotgun1: "Pump-Action Shotgun +1",
    ItemId.PumpActionShotgun2: "Pump-Action Shotgun +2",
    ItemId.PumpActionShotgun3: "Pump-Action Shotgun +3",
    ItemId.PumpActionShotgun4: "Pump-Action Shotgun +4",
    ItemId.SemiAutoShotgun: "Semi-Auto Shotgun",
    ItemId.SemiAutoShotgun1: "Semi-Auto Shotgun +1",
    ItemId.SemiAutoShotgun2: "Semi-Auto Shotgun +2",
    ItemId.SemiAutoShotgun3: "Semi-Auto Shotgun +3",
    ItemId.SemiAutoShotgun4: "Semi-Auto Shotgun +4",
    ItemId.EnergyShotgun: "Energy Shotgun",
    ItemId.EnergyShotgun1: "Energy Shotgun +1",
    ItemId.EnergyShotgun2: "Energy Shotgun +2",
    ItemId.EnergyShotgun3: "Energy Shotgun +3",
    ItemId.EnergyShotgun4: "Energy Shotgun +4",
    ItemId.Musket: "Musket",
    ItemId.Musket1: "Musket +1",
    ItemId.Musket2: "Musket +2",
    ItemId.Musket3: "Musket +3",
    ItemId.Musket4: "Musket +4",
    ItemId.SingleShotRifle: "Single-Shot Rifle",
    ItemId.SingleShotRifle1: "Single-Shot Rifle +1",
    ItemId.SingleShotRifle2: "Single-Shot Rifle +2",
    ItemId.SingleShotRifle3: "Single-Shot Rifle +3",
    ItemId.SingleShotRifle4: "Single-Shot Rifle +4",
    ItemId.SemiAutoRifle: "Semi-Auto Rifle",
    ItemId.SemiAutoRifle1: "Semi-Auto Rifle +1",
    ItemId.SemiAutoRifle2: "Semi-Auto Rifle +2",
    ItemId.SemiAutoRifle3: "Semi-Auto Rifle +3",
    ItemId.SemiAutoRifle4: "Semi-Auto Rifle +4",
    ItemId.MakeshiftAssaultRifle: "Makeshift Assault Rifle",
    ItemId.MakeshiftAssaultRifle1: "Makeshift Assault Rifle +1",
    ItemId.MakeshiftAssaultRifle2: "Makeshift Assault Rifle +2",
    ItemId.MakeshiftAssaultRifle3: "Makeshift Assault Rifle +3",
    ItemId.MakeshiftAssaultRifle4: "Makeshift Assault Rifle +4",
    ItemId.AssaultRifle: "Assault Rifle",
    ItemId.AssaultRifle1: "Assault Rifle +1",
    ItemId.AssaultRifle2: "Assault Rifle +2",
    ItemId.AssaultRifle3: "Assault Rifle +3",
    ItemId.AssaultRifle4: "Assault Rifle +4",
    ItemId.MakeshiftSMG: "Makeshift SMG",
    ItemId.MakeshiftSMG1: "Makeshift SMG +1",
    ItemId.MakeshiftSMG2: "Makeshift SMG +2",
    ItemId.MakeshiftSMG3: "Makeshift SMG +3",
    ItemId.MakeshiftSMG4: "Makeshift SMG +4",
    ItemId.SMG: "SMG",
    ItemId.SMG1: "SMG +1",
    ItemId.SMG2: "SMG +2",
    ItemId.SMG3: "SMG +3",
    ItemId.SMG4: "SMG +4",
    ItemId.MeteorLauncher: "Meteor Launcher",
    ItemId.MeteorLauncher4: "Meteor Launcher +4",
    ItemId.RocketLauncher: "Rocket Launcher",
    ItemId.EnText46: "en Text +46",
    ItemId.RocketLauncher1: "Rocket Launcher +1",
    ItemId.RocketLauncher2: "Rocket Launcher +2",
    ItemId.RocketLauncher3: "Rocket Launcher +3",
    ItemId.RocketLauncher4: "Rocket Launcher +4",
    ItemId.SingleShotSphereLauncher: "Single-Shot Sphere Launcher",
    ItemId.ScatterSphereLauncher: "Scatter Sphere Launcher",
    ItemId.HomingSphereLauncher: "Homing Sphere Launcher",
    ItemId.LaserRifle: "Laser Rifle",
    ItemId.LaserRifle1: "Laser Rifle +1",
    ItemId.LaserRifle2: "Laser Rifle +2",
    ItemId.LaserRifle3: "Laser Rifle +3",
    ItemId.LaserRifle4: "Laser Rifle +4",
    ItemId.ChargeRifle: "Charge Rifle",
    ItemId.OverheatRifle: "Overheat Rifle",
    ItemId.ChargeRifle1: "Charge Rifle +1",
    ItemId.ChargeRifle2: "Charge Rifle +2",
    ItemId.ChargeRifle3: "Charge Rifle +3",
    ItemId.ChargeRifle4: "Charge Rifle +4",
    ItemId.OverheatRifle1: "Overheat Rifle +1",
    ItemId.OverheatRifle2: "Overheat Rifle +2",
    ItemId.OverheatRifle3: "Overheat Rifle +3",
    ItemId.OverheatRifle4: "Overheat Rifle +4",
    ItemId.Flamethrower: "Flamethrower",
    ItemId.Flamethrower1: "Flamethrower +1",
    ItemId.Flamethrower2: "Flamethrower +2",
    ItemId.Flamethrower3: "Flamethrower +3",
    ItemId.Flamethrower4: "Flamethrower +4",
    ItemId.GatlingGun: "Gatling Gun",
    ItemId.GatlingGun1: "Gatling Gun +1",
    ItemId.GatlingGun2: "Gatling Gun +2",
    ItemId.GatlingGun3: "Gatling Gun +3",
    ItemId.GatlingGun4: "Gatling Gun +4",
    ItemId.LaserGatlingGun: "Laser Gatling Gun",
    ItemId.LaserGatlingGun1: "Laser Gatling Gun +1",
    ItemId.LaserGatlingGun2: "Laser Gatling Gun +2",
    ItemId.LaserGatlingGun3: "Laser Gatling Gun +3",
    ItemId.LaserGatlingGun4: "Laser Gatling Gun +4",
    ItemId.GrenadeLauncher: "Grenade Launcher",
    ItemId.GrenadeLauncher1: "Grenade Launcher +1",
    ItemId.GrenadeLauncher2: "Grenade Launcher +2",
    ItemId.GrenadeLauncher3: "Grenade Launcher +3",
    ItemId.GrenadeLauncher4: "Grenade Launcher +4",
    ItemId.GuidedMissileLauncher: "Guided Missile Launcher",
    ItemId.GuidedMissileLauncher1: "Guided Missile Launcher +1",
    ItemId.GuidedMissileLauncher2: "Guided Missile Launcher +2",
    ItemId.GuidedMissileLauncher3: "Guided Missile Launcher +3",
    ItemId.GuidedMissileLauncher4: "Guided Missile Launcher +4",
    ItemId.MultiGuidedMissileLauncher: "Multi Guided Missile Launcher",
    ItemId.MultiGuidedMissileLauncher1: "Multi Guided Missile Launcher +1",
    ItemId.MultiGuidedMissileLauncher2: "Multi Guided Missile Launcher +2",
    ItemId.MultiGuidedMissileLauncher3: "Multi Guided Missile Launcher +3",
    ItemId.MultiGuidedMissileLauncher4: "Multi Guided Missile Launcher +4",
    ItemId.PlasmaCannon: "Plasma Cannon",
    ItemId.PlasmaCannon1: "Plasma Cannon +1",
    ItemId.PlasmaCannon2: "Plasma Cannon +2",
    ItemId.PlasmaCannon3: "Plasma Cannon +3",
    ItemId.PlasmaCannon4: "Plasma Cannon +4",
    ItemId.Excalibur: "Excalibur",
    ItemId.Excalibur1: "Excalibur +1",
    ItemId.Excalibur2: "Excalibur +2",
    ItemId.Excalibur3: "Excalibur +3",
    ItemId.Excalibur4: "Excalibur +4",
    ItemId.TerraBlade: "Terra Blade",
    ItemId.TerraBlade1: "Terra Blade +1",
    ItemId.TerraBlade2: "Terra Blade +2",
    ItemId.TerraBlade3: "Terra Blade +3",
    ItemId.TerraBlade4: "Terra Blade +4",
    ItemId.VortexBeater: "Vortex Beater",
    ItemId.VortexBeater1: "Vortex Beater +1",
    ItemId.VortexBeater2: "Vortex Beater +2",
    ItemId.VortexBeater3: "Vortex Beater +3",
    ItemId.VortexBeater4: "Vortex Beater +4",
    ItemId.Nightglow: "Nightglow",
    ItemId.Nightglow1: "Nightglow +1",
    ItemId.Nightglow2: "Nightglow +2",
    ItemId.Nightglow3: "Nightglow +3",
    ItemId.Nightglow4: "Nightglow +4",
    ItemId.Terraprisma: "Terraprisma",
    ItemId.Terraprisma1: "Terraprisma +1",
    ItemId.Terraprisma2: "Terraprisma +2",
    ItemId.Terraprisma3: "Terraprisma +3",
    ItemId.Terraprisma4: "Terraprisma +4",
    ItemId.LegendaryMeowmere: "Legendary Meowmere",
    ItemId.MarksmanRevolver: "Marksman Revolver",
    ItemId.MarksmanRevolver1: "Marksman Revolver +1",
    ItemId.MarksmanRevolver2: "Marksman Revolver +2",
    ItemId.MarksmanRevolver3: "Marksman Revolver +3",
    ItemId.MarksmanRevolver4: "Marksman Revolver +4",
    ItemId.CoreEjectShotgun: "Core Eject Shotgun",
    ItemId.CoreEjectShotgun1: "Core Eject Shotgun +1",
    ItemId.CoreEjectShotgun2: "Core Eject Shotgun +2",
    ItemId.CoreEjectShotgun3: "Core Eject Shotgun +3",
    ItemId.CoreEjectShotgun4: "Core Eject Shotgun +4",
    ItemId.BeginnerFishingRodChillet: "Beginner Fishing Rod (Chillet)",
    ItemId.BeginnerFishingRodGumoss: "Beginner Fishing Rod (Gumoss)",
    ItemId.IntermediateFishingRodCattiva: "Intermediate Fishing Rod (Cattiva)",
    ItemId.IntermediateFishingRodCroajiro: "Intermediate Fishing Rod (Croajiro)",
    ItemId.AdvancedFishingRodPengullet: "Advanced Fishing Rod (Pengullet)",
    ItemId.AdvancedFishingRodDepresso: "Advanced Fishing Rod (Depresso)",
    ItemId.FragGrenade: "Frag Grenade",
    ItemId.ShockGrenade: "Shock Grenade",
    ItemId.IceGrenade: "Ice Grenade",
    ItemId.IncendiaryGrenade: "Incendiary Grenade",
    ItemId.WaterGrenade: "Water Grenade",
    ItemId.GrassGrenade: "Grass Grenade",
    ItemId.GroundGrenade: "Ground Grenade",
    ItemId.DarkGrenade: "Dark Grenade",
    ItemId.DragonGrenade: "Dragon Grenade",
    ItemId.FragGrenadeMk2: "Frag Grenade Mk2",
    ItemId.PalRecoveryGrenade: "Pal Recovery Grenade",
    ItemId.CommonShield: "Common Shield",
    ItemId.MegaShield: "Mega Shield",
    ItemId.GigaShield: "Giga Shield",
    ItemId.HyperShield: "Hyper Shield",
    ItemId.EnText4: "en Text +4",
    ItemId.UltraShield: "Ultra Shield",
    ItemId.AdvancedShield: "Advanced Shield",
    ItemId.ClothOutfit: "Cloth Outfit",
    ItemId.ClothOutfit1: "Cloth Outfit +1",
    ItemId.ClothOutfit2: "Cloth Outfit +2",
    ItemId.ClothOutfit3: "Cloth Outfit +3",
    ItemId.ClothOutfit4: "Cloth Outfit +4",
    ItemId.TropicalOutfit: "Tropical Outfit",
    ItemId.TropicalOutfit1: "Tropical Outfit +1",
    ItemId.TropicalOutfit2: "Tropical Outfit +2",
    ItemId.TropicalOutfit3: "Tropical Outfit +3",
    ItemId.TropicalOutfit4: "Tropical Outfit +4",
    ItemId.TundraOutfit: "Tundra Outfit",
    ItemId.TundraOutfit1: "Tundra Outfit +1",
    ItemId.TundraOutfit2: "Tundra Outfit +2",
    ItemId.TundraOutfit3: "Tundra Outfit +3",
    ItemId.TundraOutfit4: "Tundra Outfit +4",
    ItemId.PeltArmor: "Pelt Armor",
    ItemId.PeltArmor1: "Pelt Armor +1",
    ItemId.PeltArmor2: "Pelt Armor +2",
    ItemId.PeltArmor3: "Pelt Armor +3",
    ItemId.PeltArmor4: "Pelt Armor +4",
    ItemId.HeatResistantPeltArmor: "Heat Resistant Pelt Armor",
    ItemId.HeatResistantPeltArmor1: "Heat Resistant Pelt Armor +1",
    ItemId.HeatResistantPeltArmor2: "Heat Resistant Pelt Armor +2",
    ItemId.HeatResistantPeltArmor3: "Heat Resistant Pelt Armor +3",
    ItemId.HeatResistantPeltArmor4: "Heat Resistant Pelt Armor +4",
    ItemId.ColdResistantPeltArmor: "Cold Resistant Pelt Armor",
    ItemId.ColdResistantPeltArmor1: "Cold Resistant Pelt Armor +1",
    ItemId.ColdResistantPeltArmor2: "Cold Resistant Pelt Armor +2",
    ItemId.ColdResistantPeltArmor3: "Cold Resistant Pelt Armor +3",
    ItemId.ColdResistantPeltArmor4: "Cold Resistant Pelt Armor +4",
    ItemId.MetalArmor: "Metal Armor",
    ItemId.MetalArmor1: "Metal Armor +1",
    ItemId.MetalArmor2: "Metal Armor +2",
    ItemId.MetalArmor3: "Metal Armor +3",
    ItemId.MetalArmor4: "Metal Armor +4",
    ItemId.HeatResistantMetalArmor: "Heat Resistant Metal Armor",
    ItemId.HeatResistantMetalArmor1: "Heat Resistant Metal Armor +1",
    ItemId.HeatResistantMetalArmor2: "Heat Resistant Metal Armor +2",
    ItemId.HeatResistantMetalArmor3: "Heat Resistant Metal Armor +3",
    ItemId.HeatResistantMetalArmor4: "Heat Resistant Metal Armor +4",
    ItemId.ColdResistantMetalArmor: "Cold Resistant Metal Armor",
    ItemId.ColdResistantMetalArmor1: "Cold Resistant Metal Armor +1",
    ItemId.ColdResistantMetalArmor2: "Cold Resistant Metal Armor +2",
    ItemId.ColdResistantMetalArmor3: "Cold Resistant Metal Armor +3",
    ItemId.ColdResistantMetalArmor4: "Cold Resistant Metal Armor +4",
    ItemId.RefinedMetalArmor: "Refined Metal Armor",
    ItemId.RefinedMetalArmor1: "Refined Metal Armor +1",
    ItemId.RefinedMetalArmor2: "Refined Metal Armor +2",
    ItemId.RefinedMetalArmor3: "Refined Metal Armor +3",
    ItemId.RefinedMetalArmor4: "Refined Metal Armor +4",
    ItemId.HeatResistantRefinedMetalArmor: "Heat Resistant Refined Metal Armor",
    ItemId.HeatResistantRefinedMetalArmor1: "Heat Resistant Refined Metal Armor +1",
    ItemId.HeatResistantRefinedMetalArmor2: "Heat Resistant Refined Metal Armor +2",
    ItemId.HeatResistantRefinedMetalArmor3: "Heat Resistant Refined Metal Armor +3",
    ItemId.HeatResistantRefinedMetalArmor4: "Heat Resistant Refined Metal Armor +4",
    ItemId.ColdResistantRefinedMetalArmor: "Cold Resistant Refined Metal Armor",
    ItemId.ColdResistantRefinedMetalArmor1: "Cold Resistant Refined Metal Armor +1",
    ItemId.ColdResistantRefinedMetalArmor2: "Cold Resistant Refined Metal Armor +2",
    ItemId.ColdResistantRefinedMetalArmor3: "Cold Resistant Refined Metal Armor +3",
    ItemId.ColdResistantRefinedMetalArmor4: "Cold Resistant Refined Metal Armor +4",
    ItemId.PalMetalArmor: "Pal Metal Armor",
    ItemId.PalMetalArmor1: "Pal Metal Armor +1",
    ItemId.PalMetalArmor2: "Pal Metal Armor +2",
    ItemId.PalMetalArmor3: "Pal Metal Armor +3",
    ItemId.PalMetalArmor4: "Pal Metal Armor +4",
    ItemId.HeatResistantPalMetalArmor: "Heat Resistant Pal Metal Armor",
    ItemId.HeatResistantPalMetalArmor1: "Heat Resistant Pal Metal Armor +1",
    ItemId.HeatResistantPalMetalArmor2: "Heat Resistant Pal Metal Armor +2",
    ItemId.HeatResistantPalMetalArmor3: "Heat Resistant Pal Metal Armor +3",
    ItemId.HeatResistantPalMetalArmor4: "Heat Resistant Pal Metal Armor +4",
    ItemId.ColdResistantPalMetalArmor: "Cold Resistant Pal Metal Armor",
    ItemId.ColdResistantPalMetalArmor1: "Cold Resistant Pal Metal Armor +1",
    ItemId.ColdResistantPalMetalArmor2: "Cold Resistant Pal Metal Armor +2",
    ItemId.ColdResistantPalMetalArmor3: "Cold Resistant Pal Metal Armor +3",
    ItemId.ColdResistantPalMetalArmor4: "Cold Resistant Pal Metal Armor +4",
    ItemId.PlasteelArmor: "Plasteel Armor",
    ItemId.HeatResistantPlasteelArmor: "Heat Resistant Plasteel Armor",
    ItemId.ColdResistantPlasteelArmor: "Cold Resistant Plasteel Armor",
    ItemId.LightweightPlasteelArmor: "Lightweight Plasteel Armor",
    ItemId.PlasteelArmor1: "Plasteel Armor +1",
    ItemId.PlasteelArmor2: "Plasteel Armor +2",
    ItemId.PlasteelArmor3: "Plasteel Armor +3",
    ItemId.PlasteelArmor4: "Plasteel Armor +4",
    ItemId.HeatResistantPlasteelArmor1: "Heat Resistant Plasteel Armor +1",
    ItemId.HeatResistantPlasteelArmor2: "Heat Resistant Plasteel Armor +2",
    ItemId.HeatResistantPlasteelArmor3: "Heat Resistant Plasteel Armor +3",
    ItemId.HeatResistantPlasteelArmor4: "Heat Resistant Plasteel Armor +4",
    ItemId.ColdResistantPlasteelArmor1: "Cold Resistant Plasteel Armor +1",
    ItemId.ColdResistantPlasteelArmor2: "Cold Resistant Plasteel Armor +2",
    ItemId.ColdResistantPlasteelArmor3: "Cold Resistant Plasteel Armor +3",
    ItemId.ColdResistantPlasteelArmor4: "Cold Resistant Plasteel Armor +4",
    ItemId.LightweightPlasteelArmor1: "Lightweight Plasteel Armor +1",
    ItemId.LightweightPlasteelArmor2: "Lightweight Plasteel Armor +2",
    ItemId.LightweightPlasteelArmor3: "Lightweight Plasteel Armor +3",
    ItemId.LightweightPlasteelArmor4: "Lightweight Plasteel Armor +4",
    ItemId.HexoliteArmor: "Hexolite Armor",
    ItemId.HexoliteArmor1: "Hexolite Armor +1",
    ItemId.HexoliteArmor2: "Hexolite Armor +2",
    ItemId.HexoliteArmor3: "Hexolite Armor +3",
    ItemId.HexoliteArmor4: "Hexolite Armor +4",
    ItemId.HeatResistantHexoliteArmor: "Heat Resistant Hexolite Armor",
    ItemId.HeatResistantHexoliteArmor1: "Heat Resistant Hexolite Armor +1",
    ItemId.HeatResistantHexoliteArmor2: "Heat Resistant Hexolite Armor +2",
    ItemId.HeatResistantHexoliteArmor3: "Heat Resistant Hexolite Armor +3",
    ItemId.HeatResistantHexoliteArmor4: "Heat Resistant Hexolite Armor +4",
    ItemId.ColdResistantHexoliteArmor: "Cold Resistant Hexolite Armor",
    ItemId.ColdResistantHexoliteArmor1: "Cold Resistant Hexolite Armor +1",
    ItemId.ColdResistantHexoliteArmor2: "Cold Resistant Hexolite Armor +2",
    ItemId.ColdResistantHexoliteArmor3: "Cold Resistant Hexolite Armor +3",
    ItemId.ColdResistantHexoliteArmor4: "Cold Resistant Hexolite Armor +4",
    ItemId.LightweightHexoliteArmor: "Lightweight Hexolite Armor",
    ItemId.LightweightHexoliteArmor1: "Lightweight Hexolite Armor +1",
    ItemId.LightweightHexoliteArmor2: "Lightweight Hexolite Armor +2",
    ItemId.LightweightHexoliteArmor3: "Lightweight Hexolite Armor +3",
    ItemId.LightweightHexoliteArmor4: "Lightweight Hexolite Armor +4",
    ItemId.HallowedPlateMail: "Hallowed Plate Mail",
    ItemId.HallowedPlateMail1: "Hallowed Plate Mail +1",
    ItemId.HallowedPlateMail2: "Hallowed Plate Mail +2",
    ItemId.HallowedPlateMail3: "Hallowed Plate Mail +3",
    ItemId.HallowedPlateMail4: "Hallowed Plate Mail +4",
    ItemId.DepressoArmor: "Depresso Armor",
    ItemId.V1Armor: "V1 Armor",
    ItemId.V1Armor4: "V1 Armor +4",
    ItemId.V2Armor: "V2 Armor",
    ItemId.V2Armor4: "V2 Armor +4",
    ItemId.FeatheredHairBand: "Feathered Hair Band",
    ItemId.FeatheredHairBand1: "Feathered Hair Band +1",
    ItemId.FeatheredHairBand2: "Feathered Hair Band +2",
    ItemId.FeatheredHairBand3: "Feathered Hair Band +3",
    ItemId.FeatheredHairBand4: "Feathered Hair Band +4",
    ItemId.MetalHelm: "Metal Helm",
    ItemId.MetalHelm1: "Metal Helm +1",
    ItemId.MetalHelm2: "Metal Helm +2",
    ItemId.MetalHelm3: "Metal Helm +3",
    ItemId.MetalHelm4: "Metal Helm +4",
    ItemId.RefinedMetalHelm: "Refined Metal Helm",
    ItemId.RefinedMetalHelm1: "Refined Metal Helm +1",
    ItemId.RefinedMetalHelm2: "Refined Metal Helm +2",
    ItemId.RefinedMetalHelm3: "Refined Metal Helm +3",
    ItemId.RefinedMetalHelm4: "Refined Metal Helm +4",
    ItemId.PalMetalHelm: "Pal Metal Helm",
    ItemId.PalMetalHelm1: "Pal Metal Helm +1",
    ItemId.PalMetalHelm2: "Pal Metal Helm +2",
    ItemId.PalMetalHelm3: "Pal Metal Helm +3",
    ItemId.PalMetalHelm4: "Pal Metal Helm +4",
    ItemId.PlasteelHelmet: "Plasteel Helmet",
    ItemId.PlasteelHelmet1: "Plasteel Helmet +1",
    ItemId.PlasteelHelmet2: "Plasteel Helmet +2",
    ItemId.PlasteelHelmet3: "Plasteel Helmet +3",
    ItemId.HexoliteHelmet: "Hexolite Helmet",
    ItemId.PlasteelHelmet4: "Plasteel Helmet +4",
    ItemId.HexoliteHelmet1: "Hexolite Helmet +1",
    ItemId.HexoliteHelmet2: "Hexolite Helmet +2",
    ItemId.HexoliteHelmet3: "Hexolite Helmet +3",
    ItemId.HexoliteHelmet4: "Hexolite Helmet +4",
    ItemId.HallowedMask: "Hallowed Mask",
    ItemId.HallowedMask1: "Hallowed Mask +1",
    ItemId.HallowedMask2: "Hallowed Mask +2",
    ItemId.HallowedMask3: "Hallowed Mask +3",
    ItemId.HallowedMask4: "Hallowed Mask +4",
    ItemId.HallowedHelmet: "Hallowed Helmet",
    ItemId.HallowedHelmet1: "Hallowed Helmet +1",
    ItemId.HallowedHelmet2: "Hallowed Helmet +2",
    ItemId.HallowedHelmet3: "Hallowed Helmet +3",
    ItemId.HallowedHelmet4: "Hallowed Helmet +4",
    ItemId.HallowedHeadgear: "Hallowed Headgear",
    ItemId.HallowedHeadgear1: "Hallowed Headgear +1",
    ItemId.HallowedHeadgear2: "Hallowed Headgear +2",
    ItemId.HallowedHeadgear3: "Hallowed Headgear +3",
    ItemId.HallowedHeadgear4: "Hallowed Headgear +4",
    ItemId.HallowedHood: "Hallowed Hood",
    ItemId.HallowedHood1: "Hallowed Hood +1",
    ItemId.HallowedHood2: "Hallowed Hood +2",
    ItemId.HallowedHood3: "Hallowed Hood +3",
    ItemId.HallowedHood4: "Hallowed Hood +4",
    ItemId.MonarchSCrown: "Monarch's Crown",
    ItemId.MonarchSCrown1: "Monarch's Crown +1",
    ItemId.MonarchSCrown2: "Monarch's Crown +2",
    ItemId.MonarchSCrown3: "Monarch's Crown +3",
    ItemId.MonarchSCrown4: "Monarch's Crown +4",
    ItemId.GoldenCrown: "Golden Crown",
    ItemId.GoldenCrown1: "Golden Crown +1",
    ItemId.GoldenCrown2: "Golden Crown +2",
    ItemId.GoldenCrown3: "Golden Crown +3",
    ItemId.GoldenCrown4: "Golden Crown +4",
    ItemId.LongEaredHeadband: "Long-Eared Headband",
    ItemId.LongEaredHeadband1: "Long-Eared Headband +1",
    ItemId.LongEaredHeadband2: "Long-Eared Headband +2",
    ItemId.LongEaredHeadband3: "Long-Eared Headband +3",
    ItemId.LongEaredHeadband4: "Long-Eared Headband +4",
    ItemId.WitchHat: "Witch Hat",
    ItemId.WitchHat1: "Witch Hat +1",
    ItemId.WitchHat2: "Witch Hat +2",
    ItemId.WitchHat3: "Witch Hat +3",
    ItemId.WitchHat4: "Witch Hat +4",
    ItemId.SoftHat: "Soft Hat",
    ItemId.SoftHat1: "Soft Hat +1",
    ItemId.SoftHat2: "Soft Hat +2",
    ItemId.SoftHat3: "Soft Hat +3",
    ItemId.SoftHat4: "Soft Hat +4",
    ItemId.Helmet: "Helmet",
    ItemId.Helmet1: "Helmet +1",
    ItemId.Helmet2: "Helmet +2",
    ItemId.Helmet3: "Helmet +3",
    ItemId.Helmet4: "Helmet +4",
    ItemId.SilkHat: "Silk Hat",
    ItemId.SilkHat1: "Silk Hat +1",
    ItemId.SilkHat2: "Silk Hat +2",
    ItemId.SilkHat3: "Silk Hat +3",
    ItemId.SilkHat4: "Silk Hat +4",
    ItemId.Tricorne: "Tricorne",
    ItemId.Tricorne1: "Tricorne +1",
    ItemId.Tricorne2: "Tricorne +2",
    ItemId.Tricorne3: "Tricorne +3",
    ItemId.Tricorne4: "Tricorne +4",
    ItemId.ExplorerCap: "Explorer Cap",
    ItemId.ExplorerCap1: "Explorer Cap +1",
    ItemId.ExplorerCap2: "Explorer Cap +2",
    ItemId.ExplorerCap3: "Explorer Cap +3",
    ItemId.ExplorerCap4: "Explorer Cap +4",
    ItemId.GraduationCap: "Graduation Cap",
    ItemId.GraduationCap1: "Graduation Cap +1",
    ItemId.GraduationCap2: "Graduation Cap +2",
    ItemId.GraduationCap3: "Graduation Cap +3",
    ItemId.GraduationCap4: "Graduation Cap +4",
    ItemId.FarmingHat: "Farming Hat",
    ItemId.FarmingHat1: "Farming Hat +1",
    ItemId.FarmingHat2: "Farming Hat +2",
    ItemId.FarmingHat3: "Farming Hat +3",
    ItemId.FarmingHat4: "Farming Hat +4",
    ItemId.BowlerHat: "Bowler Hat",
    ItemId.BowlerHat1: "Bowler Hat +1",
    ItemId.BowlerHat2: "Bowler Hat +2",
    ItemId.BowlerHat3: "Bowler Hat +3",
    ItemId.BowlerHat4: "Bowler Hat +4",
    ItemId.TocotocoCap: "Tocotoco Cap",
    ItemId.TocotocoCap1: "Tocotoco Cap +1",
    ItemId.TocotocoCap2: "Tocotoco Cap +2",
    ItemId.TocotocoCap3: "Tocotoco Cap +3",
    ItemId.TocotocoCap4: "Tocotoco Cap +4",
    ItemId.GrinningTocotocoCap: "Grinning Tocotoco Cap",
    ItemId.GrinningTocotocoCap1: "Grinning Tocotoco Cap +1",
    ItemId.GrinningTocotocoCap2: "Grinning Tocotoco Cap +2",
    ItemId.GrinningTocotocoCap3: "Grinning Tocotoco Cap +3",
    ItemId.GrinningTocotocoCap4: "Grinning Tocotoco Cap +4",
    ItemId.GumossCap: "Gumoss Cap",
    ItemId.GumossCap1: "Gumoss Cap +1",
    ItemId.GumossCap2: "Gumoss Cap +2",
    ItemId.GumossCap3: "Gumoss Cap +3",
    ItemId.GumossCap4: "Gumoss Cap +4",
    ItemId.PenkingCap: "Penking Cap",
    ItemId.PenkingCap1: "Penking Cap +1",
    ItemId.PenkingCap2: "Penking Cap +2",
    ItemId.PenkingCap3: "Penking Cap +3",
    ItemId.PenkingCap4: "Penking Cap +4",
    ItemId.KatressCap: "Katress Cap",
    ItemId.KatressCap1: "Katress Cap +1",
    ItemId.KatressCap2: "Katress Cap +2",
    ItemId.KatressCap3: "Katress Cap +3",
    ItemId.KatressCap4: "Katress Cap +4",
    ItemId.LyleenFloralCap: "Lyleen Floral Cap",
    ItemId.SibelyxHat: "Sibelyx Hat",
    ItemId.LeezpunkHood: "Leezpunk Hood",
    ItemId.LeezpunkHood1: "Leezpunk Hood +1",
    ItemId.LeezpunkHood2: "Leezpunk Hood +2",
    ItemId.LeezpunkHood3: "Leezpunk Hood +3",
    ItemId.LeezpunkHood4: "Leezpunk Hood +4",
    ItemId.KillamariCap: "Killamari Cap",
    ItemId.KillamariCap1: "Killamari Cap +1",
    ItemId.KillamariCap2: "Killamari Cap +2",
    ItemId.KillamariCap3: "Killamari Cap +3",
    ItemId.KillamariCap4: "Killamari Cap +4",
    ItemId.CawgnitoHat: "Cawgnito Hat",
    ItemId.RibbunyHeadband: "Ribbuny Headband",
    ItemId.RibbunyHeadband1: "Ribbuny Headband +1",
    ItemId.RibbunyHeadband2: "Ribbuny Headband +2",
    ItemId.RibbunyHeadband3: "Ribbuny Headband +3",
    ItemId.RibbunyHeadband4: "Ribbuny Headband +4",
    ItemId.LamballHelm: "Lamball Helm",
    ItemId.DumudHelm: "Dumud Helm",
    ItemId.SweeCap: "Swee Cap",
    ItemId.SweeCap1: "Swee Cap +1",
    ItemId.SweeCap2: "Swee Cap +2",
    ItemId.SweeCap3: "Swee Cap +3",
    ItemId.SweeCap4: "Swee Cap +4",
    ItemId.DazziHat: "Dazzi Hat",
    ItemId.DazziHat1: "Dazzi Hat +1",
    ItemId.DazziHat2: "Dazzi Hat +2",
    ItemId.DazziHat3: "Dazzi Hat +3",
    ItemId.DazziHat4: "Dazzi Hat +4",
    ItemId.CattivaHat: "Cattiva Hat",
    ItemId.WitchSCrown: "Witch's Crown",
    ItemId.HornsOfSupremacy: "Horns of Supremacy",
    ItemId.XenolordSHead: "Xenolord's head",
    ItemId.MoonLordMask: "Moon Lord Mask",
    ItemId.CrownOfSalvation: "Crown of Salvation",
    ItemId.ZoeHat: "Zoe Hat",
    ItemId.LilyHat: "Lily Hat",
    ItemId.AxelHat: "Axel Hat",
    ItemId.MarcusHat: "Marcus Hat",
    ItemId.VictorHat: "Victor Hat",
    ItemId.SayaHat: "Saya Hat",
    ItemId.BjornHat: "Bjorn Hat",
    ItemId.EyeOfCthulhuMask: "Eye of Cthulhu Mask",
    ItemId.DepressoHelmet: "Depresso Helmet",
    ItemId.LifePendant: "Life Pendant",
    ItemId.LifePendant1: "Life Pendant +1",
    ItemId.LifePendant2: "Life Pendant +2",
    ItemId.AttackPendant: "Attack Pendant",
    ItemId.AttackPendant1: "Attack Pendant +1",
    ItemId.AttackPendant2: "Attack Pendant +2",
    ItemId.DefensePendant: "Defense Pendant",
    ItemId.DefensePendant1: "Defense Pendant +1",
    ItemId.DefensePendant2: "Defense Pendant +2",
    ItemId.PendantOfDiligence: "Pendant of Diligence",
    ItemId.PendantOfDiligence1: "Pendant of Diligence +1",
    ItemId.PendantOfDiligence2: "Pendant of Diligence +2",
    ItemId.HeatResistantUndershirt: "Heat Resistant Undershirt",
    ItemId.HeatResistantUndershirt1: "Heat Resistant Undershirt +1",
    ItemId.HeatResistantUndershirt2: "Heat Resistant Undershirt +2",
    ItemId.MulticlimateUndershirt: "Multiclimate Undershirt",
    ItemId.MulticlimateUndershirt1: "Multiclimate Undershirt +1",
    ItemId.MulticlimateUndershirt2: "Multiclimate Undershirt +2",
    ItemId.ThermalUndershirt: "Thermal Undershirt",
    ItemId.ThermalUndershirt1: "Thermal Undershirt +1",
    ItemId.ThermalUndershirt2: "Thermal Undershirt +2",
    ItemId.RingOfNeutralResistance: "Ring of Neutral Resistance",
    ItemId.RingOfNeutralResistance1: "Ring of Neutral Resistance +1",
    ItemId.RingOfNeutralResistance2: "Ring of Neutral Resistance +2",
    ItemId.RingOfFireResistance: "Ring of Fire Resistance",
    ItemId.RingOfFireResistance1: "Ring of Fire Resistance +1",
    ItemId.RingOfFireResistance2: "Ring of Fire Resistance +2",
    ItemId.RingOfWaterResistance: "Ring of Water Resistance",
    ItemId.RingOfWaterResistance1: "Ring of Water Resistance +1",
    ItemId.RingOfWaterResistance2: "Ring of Water Resistance +2",
    ItemId.RingOfLightningResistance: "Ring of Lightning Resistance",
    ItemId.RingOfLightningResistance1: "Ring of Lightning Resistance +1",
    ItemId.RingOfLightningResistance2: "Ring of Lightning Resistance +2",
    ItemId.RingOfGrassResistance: "Ring of Grass Resistance",
    ItemId.RingOfGrassResistance1: "Ring of Grass Resistance +1",
    ItemId.RingOfGrassResistance2: "Ring of Grass Resistance +2",
    ItemId.RingOfIceResistance: "Ring of Ice Resistance",
    ItemId.RingOfIceResistance1: "Ring of Ice Resistance +1",
    ItemId.RingOfIceResistance2: "Ring of Ice Resistance +2",
    ItemId.RingOfEarthResistance: "Ring of Earth Resistance",
    ItemId.RingOfEarthResistance1: "Ring of Earth Resistance +1",
    ItemId.RingOfEarthResistance2: "Ring of Earth Resistance +2",
    ItemId.RingOfDarkResistance: "Ring of Dark Resistance",
    ItemId.RingOfDarkResistance1: "Ring of Dark Resistance +1",
    ItemId.RingOfDarkResistance2: "Ring of Dark Resistance +2",
    ItemId.RingOfDragonResistance: "Ring of Dragon Resistance",
    ItemId.RingOfDragonResistance1: "Ring of Dragon Resistance +1",
    ItemId.RingOfDragonResistance2: "Ring of Dragon Resistance +2",
    ItemId.RingOfMercy: "Ring of Mercy",
    ItemId.AbilityGlasses: "Ability Glasses",
    ItemId.RingOfFreight: "Ring of Freight",
    ItemId.RingOfFreight1: "Ring of Freight +1",
    ItemId.RingOfFreight2: "Ring of Freight +2",
    ItemId.AntiGravityBelt: "Anti-Gravity Belt",
    ItemId.DoubleJumpBoots: "Double Jump Boots",
    ItemId.TripleJumpBoots: "Triple Jump Boots",
    ItemId.QuadrupleJumpBoots: "Quadruple Jump Boots",
    ItemId.AirDashBoots: "Air Dash Boots",
    ItemId.DoubleAirDashBoots: "Double Air Dash Boots",
    ItemId.TripleAirDashBoots: "Triple Air Dash Boots",
    ItemId.QuadrupleAirDashBoots: "Quadruple Air Dash Boots",
    ItemId.NeutralSupportWhistle: "Neutral Support Whistle",
    ItemId.NeutralSupportWhistle1: "Neutral Support Whistle +1",
    ItemId.NeutralSupportWhistle2: "Neutral Support Whistle +2",
    ItemId.FireSupportWhistle: "Fire Support Whistle",
    ItemId.FireSupportWhistle1: "Fire Support Whistle +1",
    ItemId.FireSupportWhistle2: "Fire Support Whistle +2",
    ItemId.WaterSupportWhistle: "Water Support Whistle",
    ItemId.WaterSupportWhistle1: "Water Support Whistle +1",
    ItemId.WaterSupportWhistle2: "Water Support Whistle +2",
    ItemId.ElectricSupportWhistle: "Electric Support Whistle",
    ItemId.ElectricSupportWhistle1: "Electric Support Whistle +1",
    ItemId.ElectricSupportWhistle2: "Electric Support Whistle +2",
    ItemId.GrassSupportWhistle: "Grass Support Whistle",
    ItemId.GrassSupportWhistle1: "Grass Support Whistle +1",
    ItemId.GrassSupportWhistle2: "Grass Support Whistle +2",
    ItemId.IceSupportWhistle: "Ice Support Whistle",
    ItemId.IceSupportWhistle1: "Ice Support Whistle +1",
    ItemId.IceSupportWhistle2: "Ice Support Whistle +2",
    ItemId.GroundSupportWhistle: "Ground Support Whistle",
    ItemId.GroundSupportWhistle1: "Ground Support Whistle +1",
    ItemId.GroundSupportWhistle2: "Ground Support Whistle +2",
    ItemId.DarkSupportWhistle: "Dark Support Whistle",
    ItemId.DarkSupportWhistle1: "Dark Support Whistle +1",
    ItemId.DarkSupportWhistle2: "Dark Support Whistle +2",
    ItemId.DragonSupportWhistle: "Dragon Support Whistle",
    ItemId.DragonSupportWhistle1: "Dragon Support Whistle +1",
    ItemId.DragonSupportWhistle2: "Dragon Support Whistle +2",
    ItemId.AttackSupportWhistle: "Attack Support Whistle",
    ItemId.AttackSupportWhistle1: "Attack Support Whistle +1",
    ItemId.AttackSupportWhistle2: "Attack Support Whistle +2",
    ItemId.DefenseSupportWhistle: "Defense Support Whistle",
    ItemId.DefenseSupportWhistle1: "Defense Support Whistle +1",
    ItemId.DefenseSupportWhistle2: "Defense Support Whistle +2",
    ItemId.GrowthAccelerationBell: "Growth Acceleration Bell",
    ItemId.GrowthAccelerationBell1: "Growth Acceleration Bell +1",
    ItemId.GrowthAccelerationBell2: "Growth Acceleration Bell +2",
    ItemId.UnknownItemOtomoMoveSpeedUp1: "Unknown Item (Otomo_MoveSpeed_up_1)",
    ItemId.NormalParachute: "Normal Parachute",
    ItemId.MegaGlider: "Mega Glider",
    ItemId.GigaGlider: "Giga Glider",
    ItemId.HyperGlider1: "Hyper Glider +1",
    ItemId.Cake: "Cake",
    ItemId.MammorestCurry: "Mammorest Curry",
    ItemId.BroncherryFriedNoodles: "Broncherry Fried Noodles",
    ItemId.BLT: "BLT",
    ItemId.Hamburger: "Hamburger",
    ItemId.MozzarinaCheeseburger: "Mozzarina Cheeseburger",
    ItemId.RoastReindrix: "Roast Reindrix",
    ItemId.BroncherryRibRoast: "Broncherry Rib Roast",
    ItemId.MammorestSteak: "Mammorest Steak",
    ItemId.MushroomStew: "Mushroom Stew",
    ItemId.EikthyrdeerStew: "Eikthyrdeer Stew",
    ItemId.BologneseSauce: "Bolognese Sauce",
    ItemId.Pizza: "Pizza",
    ItemId.MushroomQuiche: "Mushroom Quiche",
    ItemId.BroncherryMeat: "Broncherry Meat",
    ItemId.MammorestMeat: "Mammorest Meat",
    ItemId.EikthyrdeerLocoMoco: "Eikthyrdeer Loco Moco",
    ItemId.DumudChowder: "Dumud Chowder",
    ItemId.RushoarBaconNEggs: "Rushoar Bacon 'n' Eggs",
    ItemId.MozzarinaHamburger: "Mozzarina Hamburger",
    ItemId.GaleclawNikujaga: "Galeclaw Nikujaga",
    ItemId.GrilledLamball: "Grilled Lamball",
    ItemId.Minestrone: "Minestrone",
    ItemId.RushoarHotDog: "Rushoar Hot Dog",
    ItemId.ReindrixStew: "Reindrix Stew",
    ItemId.Carbonara: "Carbonara",
    ItemId.RushoarGyoza: "Rushoar Gyoza",
    ItemId.SpringRolls: "Spring Rolls",
    ItemId.Gratin: "Gratin",
    ItemId.FriedChikipi: "Fried Chikipi",
    ItemId.FriedKelpsea: "Fried Kelpsea",
    ItemId.HotDog: "Hot Dog",
    ItemId.SeafoodSalad: "Seafood Salad",
    ItemId.HerbRoastedLamball: "Herb Roasted Lamball",
    ItemId.ChikipiSaut: "Chikipi Sauté",
    ItemId.StewedGaleclaw: "Stewed Galeclaw",
    ItemId.StirFriedVeggies: "Stir-Fried Veggies",
    ItemId.MunchillSteak: "Munchill Steak",
    ItemId.Salad: "Salad",
    ItemId.HerbRoastedCaprity: "Herb Roasted Caprity",
    ItemId.MozzarinaSteak: "Mozzarina Steak",
    ItemId.FriedGloopieBalls: "Fried Gloopie Balls",
    ItemId.BroiledDumud: "Broiled Dumud",
    ItemId.RoastEikthyrdeer: "Roast Eikthyrdeer",
    ItemId.Omelet: "Omelet",
    ItemId.ReindrixVenison: "Reindrix Venison",
    ItemId.MarinatedMushrooms: "Marinated Mushrooms",
    ItemId.RoastRushoar: "Roast Rushoar",
    ItemId.JellroySJollyJelly: "Jellroy's Jolly Jelly",
    ItemId.JellietteSJigglyJelly: "Jelliette's Jiggly Jelly",
    ItemId.CaprityMeat: "Caprity Meat",
    ItemId.MozzarinaMeat: "Mozzarina Meat",
    ItemId.StirFriedVegetables: "Stir-Fried Vegetables",
    ItemId.MushroomSoup: "Mushroom Soup",
    ItemId.LamballKebab: "Lamball Kebab",
    ItemId.JamFilledBun: "Jam-Filled Bun",
    ItemId.RawDumud: "Raw Dumud",
    ItemId.EikthyrdeerVenison: "Eikthyrdeer Venison",
    ItemId.GrilledChikipi: "Grilled Chikipi",
    ItemId.GrilledKelpsea: "Grilled Kelpsea",
    ItemId.GrilledGaleclaw: "Grilled Galeclaw",
    ItemId.RushoarPork: "Rushoar Pork",
    ItemId.Pancake: "Pancake",
    ItemId.MunchillMeat: "Munchill Meat",
    ItemId.GloopieTentacle: "Gloopie Tentacle",
    ItemId.LamballMutton: "Lamball Mutton",
    ItemId.JellroyBellFlesh: "Jellroy Bell Flesh",
    ItemId.ChikipiPoultry: "Chikipi Poultry",
    ItemId.RawKelpsea: "Raw Kelpsea",
    ItemId.GaleclawPoultry: "Galeclaw Poultry",
    ItemId.FrenchFries: "French Fries",
    ItemId.JellietteBellFlesh: "Jelliette Bell Flesh",
    ItemId.Bread: "Bread",
    ItemId.FriedEgg: "Fried Egg",
    ItemId.BakedBerries: "Baked Berries",
    ItemId.BakedMushroom: "Baked Mushroom",
    ItemId.Egg: "Egg",
    ItemId.HotMilk: "Hot Milk",
    ItemId.RedBerries: "Red Berries",
    ItemId.Tomato: "Tomato",
    ItemId.Lettuce: "Lettuce",
    ItemId.CavernMushroom: "Cavern Mushroom",
    ItemId.Mushroom: "Mushroom",
    ItemId.Milk: "Milk",
    ItemId.Potato: "Potato",
    ItemId.Honey: "Honey",
    ItemId.Carrot: "Carrot",
    ItemId.Onion: "Onion",
    ItemId.Wheat: "Wheat",
    ItemId.CottonCandy: "Cotton Candy",
    ItemId.Flour: "Flour",
    ItemId.MysteriousMushroom: "Mysterious Mushroom",
    ItemId.LowGradeMedicalSupplies: "Low Grade Medical Supplies",
    ItemId.MedicalSupplies: "Medical Supplies",
    ItemId.HighGradeMedicalSupplies: "High Grade Medical Supplies",
    ItemId.MindControlMeds: "Mind Control Meds",
    ItemId.LowQualityRecoveryMeds: "Low Quality Recovery Meds",
    ItemId.RecoveryMeds: "Recovery Meds",
    ItemId.HighQualityRecoveryMeds: "High Quality Recovery Meds",
    ItemId.AdvancedRecoveryMeds: "Advanced Recovery Meds",
    ItemId.BeautifulFlower: "Beautiful Flower",
    ItemId.SuspiciousJuice: "Suspicious Juice",
    ItemId.StrangeJuice: "Strange Juice",
    ItemId.MysteriousMushroomJuice: "Mysterious Mushroom Juice",
    ItemId.MemoryWipingMedicine: "Memory Wiping Medicine",
    ItemId.RevivalPotion: "Revival Potion",
    ItemId.NutrientTonic: "Nutrient Tonic",
    ItemId.VitalRemedy: "Vital Remedy",
    ItemId.StaminaRemedy: "Stamina Remedy",
    ItemId.MightRemedy: "Might Remedy",
    ItemId.SpeedRemedy: "Speed Remedy",
    ItemId.BurdenRemedy: "Burden Remedy",
    ItemId.VitalElixir: "Vital Elixir",
    ItemId.StaminaElixir: "Stamina Elixir",
    ItemId.MightElixir: "Might Elixir",
    ItemId.SpeedElixir: "Speed Elixir",
    ItemId.BurdenElixir: "Burden Elixir",
    ItemId.LifeCrystal: "Life Crystal",
    ItemId.KinshipPeach: "Kinship Peach",
    ItemId.LittleKinshipPeach: "Little Kinship Peach",
    ItemId.ScrappedTissueSample: "Scrapped Tissue Sample",
    ItemId.LifeLotusS: "Life Lotus (S)",
    ItemId.StaminaLotusS: "Stamina Lotus (S)",
    ItemId.PowerLotusS: "Power Lotus (S)",
    ItemId.SpeedLotusS: "Speed Lotus (S)",
    ItemId.CarryingLotusS: "Carrying Lotus (S)",
    ItemId.LifeLotusL: "Life Lotus (L)",
    ItemId.StaminaLotusL: "Stamina Lotus (L)",
    ItemId.PowerLotusL: "Power Lotus (L)",
    ItemId.SpeedLotusL: "Speed Lotus (L)",
    ItemId.CarryingLotusL: "Carrying Lotus (L)",
    ItemId.LifeFruit: "Life Fruit",
    ItemId.PowerFruit: "Power Fruit",
    ItemId.StoutFruit: "Stout Fruit",
    ItemId.HomewardThundercloud: "Homeward Thundercloud",
    ItemId.AwakeningStarfruit1: "Awakening Starfruit ☆1",
    ItemId.AwakeningStarfruit2: "Awakening Starfruit ☆2",
    ItemId.AwakeningStarfruit3: "Awakening Starfruit ☆3",
    ItemId.AwakeningStarfruit4: "Awakening Starfruit ☆4",
    ItemId.RipeAwakeningStarfruit: "Ripe Awakening Starfruit",
    ItemId.AppliedKindlingTechnique: "Applied Kindling Technique Ⅰ",
    ItemId.AppliedWateringTechnique: "Applied Watering Technique Ⅰ",
    ItemId.AppliedPlantingTechnique: "Applied Planting Technique Ⅰ",
    ItemId.AppliedGeneratingElectricityTechnique: "Applied Generating Electricity Technique Ⅰ",
    ItemId.AppliedHandiworkTechnique: "Applied Handiwork Technique Ⅰ",
    ItemId.AppliedGatheringTechnique: "Applied Gathering Technique Ⅰ",
    ItemId.AppliedLumberingTechnique: "Applied Lumbering Technique Ⅰ",
    ItemId.AppliedMiningTechnique: "Applied Mining Technique Ⅰ",
    ItemId.AppliedMedicineProductionTechnique: "Applied Medicine Production Technique Ⅰ",
    ItemId.AppliedCoolingTechnique: "Applied Cooling Technique Ⅰ",
    ItemId.AppliedTransportingTechnique: "Applied Transporting Technique Ⅰ",
    ItemId.TrainingManualS: "Training Manual (S)",
    ItemId.TrainingManualM: "Training Manual (M)",
    ItemId.TrainingManualL: "Training Manual (L)",
    ItemId.TrainingManualXL: "Training Manual (XL)",
    ItemId.TrainingCrystal: "Training Crystal",
    ItemId.Wood: "Wood",
    ItemId.Fiber: "Fiber",
    ItemId.Stone: "Stone",
    ItemId.PaldiumFragment: "Paldium Fragment",
    ItemId.Ore: "Ore",
    ItemId.Coal: "Coal",
    ItemId.Sulfur: "Sulfur",
    ItemId.PureQuartz: "Pure Quartz",
    ItemId.CrudeOil: "Crude Oil",
    ItemId.Chromite: "Chromite",
    ItemId.NightstarSand: "Nightstar Sand",
    ItemId.HexoliteQuartz: "Hexolite Quartz",
    ItemId.CoralumOre: "Coralum Ore",
    ItemId.MeteoriteFragment: "Meteorite Fragment",
    ItemId.Wool: "Wool",
    ItemId.Leather: "Leather",
    ItemId.Bone: "Bone",
    ItemId.Horn: "Horn",
    ItemId.ElectricOrgan: "Electric Organ",
    ItemId.VenomGland: "Venom Gland",
    ItemId.FlameOrgan: "Flame Organ",
    ItemId.IceOrgan: "Ice Organ",
    ItemId.PalFluids: "Pal Fluids",
    ItemId.HighQualityPalOil: "High Quality Pal Oil",
    ItemId.DarkFragment: "Dark Fragment",
    ItemId.TocotocoFeather: "Tocotoco Feather",
    ItemId.GumossLeaf: "Gumoss Leaf",
    ItemId.PenkingPlume: "Penking Plume",
    ItemId.KatressHair: "Katress Hair",
    ItemId.RibbunyRibbon: "Ribbuny Ribbon",
    ItemId.SweeHair: "Swee Hair",
    ItemId.KillamariTentacle: "Killamari Tentacle",
    ItemId.DazziCloud: "Dazzi Cloud",
    ItemId.LeezpunkCrest: "Leezpunk Crest",
    ItemId.AncientPalManuscript: "Ancient Pal Manuscript",
    ItemId.AncientCivilizationParts: "Ancient Civilization Parts",
    ItemId.AncientCivilizationCore: "Ancient Civilization Core",
    ItemId.PredatorCore: "Predator Core",
    ItemId.SuccessfulBountyToken: "Successful Bounty Token",
    ItemId.BattleTicket: "Battle Ticket",
    ItemId.BerrySeeds: "Berry Seeds",
    ItemId.WheatSeeds: "Wheat Seeds",
    ItemId.TomatoSeeds: "Tomato Seeds",
    ItemId.LettuceSeeds: "Lettuce Seeds",
    ItemId.PotatoSeeds: "Potato Seeds",
    ItemId.CarrotSeeds: "Carrot Seeds",
    ItemId.OnionSeeds: "Onion Seeds",
    ItemId.Cloth: "Cloth",
    ItemId.HighQualityCloth: "High Quality Cloth",
    ItemId.Nail: "Nail",
    ItemId.Gunpowder1: "Gunpowder +1",
    ItemId.CircuitBoard: "Circuit Board",
    ItemId.Polymer: "Polymer",
    ItemId.Silicon: "Silicon",
    ItemId.Cement: "Cement",
    ItemId.CarbonFiber: "Carbon Fiber",
    ItemId.Charcoal: "Charcoal",
    ItemId.Ingot: "Ingot",
    ItemId.RefinedIngot: "Refined Ingot",
    ItemId.PalMetalIngot: "Pal Metal Ingot",
    ItemId.Plasteel: "Plasteel",
    ItemId.Hexolite: "Hexolite",
    ItemId.UnknownItemYakushimaParts003: "Unknown Item (YakushimaParts003)",
    ItemId.HallowedBar: "Hallowed Bar",
    ItemId.LuminiteBar: "Luminite Bar",
    ItemId.CoralumIngot: "Coralum Ingot",
    ItemId.CommonEgg: "Common Egg",
    ItemId.CommonEgg1: "Common Egg +1",
    ItemId.LargeCommonEgg2: "Large Common Egg +2",
    ItemId.LargeCommonEgg3: "Large Common Egg +3",
    ItemId.HugeCommonEgg: "Huge Common Egg",
    ItemId.ScorchingEgg: "Scorching Egg",
    ItemId.ScorchingEgg1: "Scorching Egg +1",
    ItemId.LargeScorchingEgg2: "Large Scorching Egg +2",
    ItemId.LargeScorchingEgg3: "Large Scorching Egg +3",
    ItemId.HugeScorchingEgg: "Huge Scorching Egg",
    ItemId.DampEgg: "Damp Egg",
    ItemId.DampEgg1: "Damp Egg +1",
    ItemId.LargeDampEgg2: "Large Damp Egg +2",
    ItemId.LargeDampEgg3: "Large Damp Egg +3",
    ItemId.HugeDampEgg: "Huge Damp Egg",
    ItemId.VerdantEgg: "Verdant Egg",
    ItemId.VerdantEgg1: "Verdant Egg +1",
    ItemId.LargeVerdantEgg2: "Large Verdant Egg +2",
    ItemId.LargeVerdantEgg3: "Large Verdant Egg +3",
    ItemId.HugeVerdantEgg: "Huge Verdant Egg",
    ItemId.ElectricEgg: "Electric Egg",
    ItemId.ElectricEgg1: "Electric Egg +1",
    ItemId.LargeElectricEgg2: "Large Electric Egg +2",
    ItemId.LargeElectricEgg3: "Large Electric Egg +3",
    ItemId.HugeElectricEgg: "Huge Electric Egg",
    ItemId.FrozenEgg: "Frozen Egg",
    ItemId.FrozenEgg1: "Frozen Egg +1",
    ItemId.LargeFrozenEgg2: "Large Frozen Egg +2",
    ItemId.LargeFrozenEgg3: "Large Frozen Egg +3",
    ItemId.HugeFrozenEgg: "Huge Frozen Egg",
    ItemId.RockyEgg: "Rocky Egg",
    ItemId.RockyEgg1: "Rocky Egg +1",
    ItemId.LargeRockyEgg2: "Large Rocky Egg +2",
    ItemId.LargeRockyEgg3: "Large Rocky Egg +3",
    ItemId.HugeRockyEgg: "Huge Rocky Egg",
    ItemId.DarkEgg: "Dark Egg",
    ItemId.DarkEgg1: "Dark Egg +1",
    ItemId.LargeDarkEgg2: "Large Dark Egg +2",
    ItemId.LargeDarkEgg3: "Large Dark Egg +3",
    ItemId.HugeDarkEgg: "Huge Dark Egg",
    ItemId.DragonEgg: "Dragon Egg",
    ItemId.DragonEgg1: "Dragon Egg +1",
    ItemId.LargeDragonEgg2: "Large Dragon Egg +2",
    ItemId.LargeDragonEgg3: "Large Dragon Egg +3",
    ItemId.HugeDragonEgg: "Huge Dragon Egg",
    ItemId.Ruby: "Ruby",
    ItemId.Sapphire: "Sapphire",
    ItemId.Emerald: "Emerald",
    ItemId.Diamond: "Diamond",
    ItemId.PreciousDragonStone: "Precious Dragon Stone",
    ItemId.PreciousPlume: "Precious Plume",
    ItemId.PreciousEntrails: "Precious Entrails",
    ItemId.PreciousClaw: "Precious Claw",
    ItemId.PreciousPelt: "Precious Pelt",
    ItemId.SmallPalSoul: "Small Pal Soul",
    ItemId.MediumPalSoul: "Medium Pal Soul",
    ItemId.LargePalSoul: "Large Pal Soul",
    ItemId.GiantPalSoul: "Giant Pal Soul",
    ItemId.UnknownItemYakushimaParts001: "Unknown Item (YakushimaParts001)",
    ItemId.UnknownItemYakushimaParts002: "Unknown Item (YakushimaParts002)",
    ItemId.SkillFruitPowerShot: "Skill Fruit: Power Shot",
    ItemId.SkillFruitAirCannon: "Skill Fruit: Air Cannon",
    ItemId.SkillFruitAirBlade: "Skill Fruit: Air Blade",
    ItemId.SkillFruitPowerBomb: "Skill Fruit: Power Bomb",
    ItemId.SkillFruitImplode: "Skill Fruit: Implode",
    ItemId.SkillFruitHolyBurst: "Skill Fruit: Holy Burst",
    ItemId.SkillFruitPalBlast: "Skill Fruit: Pal Blast",
    ItemId.GrassSkillFruitWindCutter: "Grass Skill Fruit: Wind Cutter",
    ItemId.GrassSkillFruitSeedMachineGun: "Grass Skill Fruit: Seed Machine Gun",
    ItemId.GrassSkillFruitSeedMine: "Grass Skill Fruit: Seed Mine",
    ItemId.GrassSkillFruitGrassTornado: "Grass Skill Fruit: Grass Tornado",
    ItemId.GrassSkillFruitSpineVine: "Grass Skill Fruit: Spine Vine",
    ItemId.GrassSkillFruitMulticutter: "Grass Skill Fruit: Multicutter",
    ItemId.GrassSkillFruitCircleVine: "Grass Skill Fruit: Circle Vine",
    ItemId.GrassSkillFruitSolarBlast: "Grass Skill Fruit: Solar Blast",
    ItemId.GrassSkillFruitReflectLeaf: "Grass Skill Fruit: Reflect Leaf",
    ItemId.GrassSkillFruitCrosswind: "Grass Skill Fruit: Crosswind",
    ItemId.WaterSkillFruitAquaGun: "Water Skill Fruit: Aqua Gun",
    ItemId.WaterSkillFruitHydroJet: "Water Skill Fruit: Hydro Jet",
    ItemId.WaterSkillFruitAcidRain: "Water Skill Fruit: Acid Rain",
    ItemId.WaterSkillFruitBubbleBlast: "Water Skill Fruit: Bubble Blast",
    ItemId.WaterSkillFruitAquaBurst: "Water Skill Fruit: Aqua Burst",
    ItemId.WaterSkillFruitSplash: "Water Skill Fruit: Splash",
    ItemId.WaterSkillFruitTorrentialBlast: "Water Skill Fruit: Torrential Blast",
    ItemId.WaterSkillFruitCurtainSplash: "Water Skill Fruit: Curtain Splash",
    ItemId.WaterSkillFruitHydroLaser: "Water Skill Fruit: Hydro Laser",
    ItemId.WaterSkillFruitHydroSlicer: "Water Skill Fruit: Hydro Slicer",
    ItemId.WaterSkillFruitAquaSurge: "Water Skill Fruit: Aqua Surge",
    ItemId.FireSkillFruitIgnisBlast: "Fire Skill Fruit: Ignis Blast",
    ItemId.FireSkillFruitFlareArrow: "Fire Skill Fruit: Flare Arrow",
    ItemId.FireSkillFruitSpiritFire: "Fire Skill Fruit: Spirit Fire",
    ItemId.FireSkillFruitIgnisBreath: "Fire Skill Fruit: Ignis Breath",
    ItemId.FireSkillFruitFlareStorm: "Fire Skill Fruit: Flare Storm",
    ItemId.FireSkillFruitFlameWall: "Fire Skill Fruit: Flame Wall",
    ItemId.FireSkillFruitFlameFunnel: "Fire Skill Fruit: Flame Funnel",
    ItemId.FireSkillFruitFireBall: "Fire Skill Fruit: Fire Ball",
    ItemId.FireSkillFruitIgnisRage: "Fire Skill Fruit: Ignis Rage",
    ItemId.FireSkillFruitVolcanicRain: "Fire Skill Fruit: Volcanic Rain",
    ItemId.ElectricSkillFruitShockwave: "Electric Skill Fruit: Shockwave",
    ItemId.ElectricSkillFruitPlasmaFunnel: "Electric Skill Fruit: Plasma Funnel",
    ItemId.ElectricSkillFruitSparkBlast: "Electric Skill Fruit: Spark Blast",
    ItemId.ElectricSkillFruitElectricBall: "Electric Skill Fruit: Electric Ball",
    ItemId.ElectricSkillFruitThunderSpear: "Electric Skill Fruit: Thunder Spear",
    ItemId.ElectricSkillFruitLightningStreak: "Electric Skill Fruit: Lightning Streak",
    ItemId.ElectricSkillFruitLockOnLaser: "Electric Skill Fruit: Lock-on Laser",
    ItemId.ElectricSkillFruitTriLightning: "Electric Skill Fruit: Tri-Lightning",
    ItemId.ElectricSkillFruitTriSpark: "Electric Skill Fruit: TriSpark",
    ItemId.ElectricSkillFruitLightningBolt: "Electric Skill Fruit: Lightning Bolt",
    ItemId.ElectricSkillFruitLightningStrike: "Electric Skill Fruit: Lightning Strike",
    ItemId.ElectricSkillFruitThunderRain: "Electric Skill Fruit: Thunder Rain",
    ItemId.ElectricSkillFruitThunderstorm: "Electric Skill Fruit: Thunderstorm",
    ItemId.ThunderSkillFruitAllRangeThunder: "Thunder Skill Fruit: All Range Thunder",
    ItemId.EarthSkillFruitStoneCannon: "Earth Skill Fruit: Stone Cannon",
    ItemId.EarthSkillFruitBogBlast: "Earth Skill Fruit: Bog Blast",
    ItemId.EarthSkillFruitStoneBlast: "Earth Skill Fruit: Stone Blast",
    ItemId.EarthSkillFruitSandTornado: "Earth Skill Fruit: Sand Tornado",
    ItemId.EarthSkillFruitSandTwister: "Earth Skill Fruit: Sand Twister",
    ItemId.EarthSkillFruitRockLance: "Earth Skill Fruit: Rock Lance",
    ItemId.EarthSkillFruitRockburst: "Earth Skill Fruit: Rockburst",
    ItemId.EarthSkillFruitStoneBeat: "Earth Skill Fruit: Stone Beat",
    ItemId.IceSkillFruitIceMissile: "Ice Skill Fruit: Ice Missile",
    ItemId.IceSkillFruitIcicleCutter: "Ice Skill Fruit: Icicle Cutter",
    ItemId.IceSkillFruitIceberg: "Ice Skill Fruit: Iceberg",
    ItemId.IceSkillFruitCrystalBreath: "Ice Skill Fruit: Crystal Breath",
    ItemId.IceSkillFruitFreezeWall: "Ice Skill Fruit: Freeze Wall",
    ItemId.IceSkillFruitIcicleBullet: "Ice Skill Fruit: Icicle Bullet",
    ItemId.IceSkillFruitIcicleLine: "Ice Skill Fruit: Icicle Line",
    ItemId.IceSkillFruitBlizzardSpike: "Ice Skill Fruit: Blizzard Spike",
    ItemId.IceSkillFruitDiamondRain: "Ice Skill Fruit: Diamond Rain",
    ItemId.IceSkillFruitAbsoluteFrost: "Ice Skill Fruit: Absolute Frost",
    ItemId.DarkSkillFruitShadowBurst: "Dark Skill Fruit: Shadow Burst",
    ItemId.DarkSkillFruitPoisonBlast: "Dark Skill Fruit: Poison Blast",
    ItemId.DarkSkillFruitSpiritFlame: "Dark Skill Fruit: Spirit Flame",
    ItemId.DarkSkillFruitDarkCannon: "Dark Skill Fruit: Dark Cannon",
    ItemId.DarkSkillFruitUmbralSurge: "Dark Skill Fruit: Umbral Surge",
    ItemId.DarkSkillFruitDarkShot: "Dark Skill Fruit: Dark Shot",
    ItemId.DarkSkillFruitNightmareBall: "Dark Skill Fruit: Nightmare Ball",
    ItemId.DarkSkillFruitDarkArrow: "Dark Skill Fruit: Dark Arrow",
    ItemId.DarkSkillFruitDarkLaser: "Dark Skill Fruit: Dark Laser",
    ItemId.DarkSkillFruitApocalypse: "Dark Skill Fruit: Apocalypse",
    ItemId.DarkSkillFruitDarkWhisp: "Dark Skill Fruit: Dark Whisp",
    ItemId.DragonSkillFruitDragonCannon: "Dragon Skill Fruit: Dragon Cannon",
    ItemId.DragonSkillFruitDragonBurst: "Dragon Skill Fruit: Dragon Burst",
    ItemId.DragonSkillFruitDraconicBreath: "Dragon Skill Fruit: Draconic Breath",
    ItemId.DragonSkillFruitComet: "Dragon Skill Fruit: Comet",
    ItemId.DragonSkillFruitBlastCannon: "Dragon Skill Fruit: Blast Cannon",
    ItemId.DragonSkillFruitDragonMeteor: "Dragon Skill Fruit: Dragon Meteor",
    ItemId.DragonSkillFruitBeamSlicer: "Dragon Skill Fruit: Beam Slicer",
    ItemId.DragonSkillFruitChargeCannon: "Dragon Skill Fruit: Charge Cannon",
    ItemId.PalReverser: "Pal Reverser",
    ItemId.ImplantMercyHit: "Implant: Mercy Hit",
    ItemId.ImplantNocturnal: "Implant: Nocturnal",
    ItemId.ImplantPhilanthropist: "Implant: Philanthropist",
    ItemId.ImplantImpatient: "Implant: Impatient",
    ItemId.ImplantSerenity: "Implant: Serenity",
    ItemId.ImplantFitAsAFiddle: "Implant: Fit as a Fiddle",
    ItemId.ImplantInfiniteStamina: "Implant: Infinite Stamina",
    ItemId.ImplantEternalEngine: "Implant: Eternal Engine",
    ItemId.ImplantNimble: "Implant: Nimble",
    ItemId.ImplantRunner: "Implant: Runner",
    ItemId.ImplantSwift: "Implant: Swift",
    ItemId.ImplantDaintyEater: "Implant: Dainty Eater",
    ItemId.ImplantDietLover: "Implant: Diet Lover",
    ItemId.ImplantMasteryOfFasting: "Implant: Mastery of Fasting",
    ItemId.ImplantPositiveThinker: "Implant: Positive Thinker",
    ItemId.ImplantWorkaholic: "Implant: Workaholic",
    ItemId.ImplantHeartOfTheImmovableKing: "Implant: Heart of the Immovable King",
    ItemId.ImplantBrave: "Implant: Brave",
    ItemId.ImplantFerocious: "Implant: Ferocious",
    ItemId.ImplantDemonGod: "Implant: Demon God",
    ItemId.ImplantHardSkin: "Implant: Hard Skin",
    ItemId.ImplantBurlyBody: "Implant: Burly Body",
    ItemId.ImplantDiamondBody: "Implant: Diamond Body",
    ItemId.ImplantSerious: "Implant: Serious",
    ItemId.ImplantArtisan: "Implant: Artisan",
    ItemId.ImplantRemarkableCraftsmanship: "Implant: Remarkable Craftsmanship",
    ItemId.ImplantMusclehead: "Implant: Musclehead",
    ItemId.ImplantVanguard: "Implant: Vanguard",
    ItemId.ImplantStrongholdStrategist: "Implant: Stronghold Strategist",
    ItemId.ImplantMotivationalLeader: "Implant: Motivational Leader",
    ItemId.ImplantNoble: "Implant: Noble",
    ItemId.ImplantAceSwimmer: "Implant: Ace Swimmer",
    ItemId.ImplantMineForeman: "Implant: Mine Foreman",
    ItemId.ImplantLoggingForeman: "Implant: Logging Foreman",
    ItemId.ImplantFineFurs: "Implant: Fine Furs",
    ItemId.ImplantSleekStroke: "Implant: Sleek Stroke",
    ItemId.ImplantWorkSlave: "Implant: Work Slave",
    ItemId.HighGradeTechnicalManual: "High Grade Technical Manual",
    ItemId.InnovativeTechnicalManual: "Innovative Technical Manual",
    ItemId.FutureTechnicalManual: "Future Technical Manual",
    ItemId.AncientTechnicalManual: "Ancient Technical Manual",
    ItemId.CopperKey: "Copper Key",
    ItemId.SilverKey: "Silver Key",
    ItemId.GoldKey: "Gold Key",
    ItemId.FishingMagnet: "Fishing Magnet",
    ItemId.RepairKit: "Repair Kit",
    ItemId.UnknownItemWaterBuildKit: "Unknown Item (WaterBuildKit)",
    ItemId.LilySSpearSchematic4: "Lily's Spear Schematic 4",
    ItemId.SwordSchematic1: "Sword Schematic 1",
    ItemId.SwordSchematic2: "Sword Schematic 2",
    ItemId.SwordSchematic3: "Sword Schematic 3",
    ItemId.SwordSchematic4: "Sword Schematic 4",
    ItemId.KatanaSchematic1: "Katana Schematic 1",
    ItemId.KatanaSchematic2: "Katana Schematic 2",
    ItemId.KatanaSchematic3: "Katana Schematic 3",
    ItemId.KatanaSchematic4: "Katana Schematic 4",
    ItemId.BeamSwordSchematic1: "Beam Sword Schematic 1",
    ItemId.BeamSwordSchematic2: "Beam Sword Schematic 2",
    ItemId.BeamSwordSchematic3: "Beam Sword Schematic 3",
    ItemId.BeamSwordSchematic4: "Beam Sword Schematic 4",
    ItemId.OldBowSchematic1: "Old Bow Schematic 1",
    ItemId.OldBowSchematic2: "Old Bow Schematic 2",
    ItemId.OldBowSchematic3: "Old Bow Schematic 3",
    ItemId.OldBowSchematic4: "Old Bow Schematic 4",
    ItemId.CrossbowSchematic1: "Crossbow Schematic 1",
    ItemId.CrossbowSchematic2: "Crossbow Schematic 2",
    ItemId.CrossbowSchematic3: "Crossbow Schematic 3",
    ItemId.CrossbowSchematic4: "Crossbow Schematic 4",
    ItemId.FireArrowCrossbowSchematic1: "Fire Arrow Crossbow Schematic 1",
    ItemId.FireArrowCrossbowSchematic2: "Fire Arrow Crossbow Schematic 2",
    ItemId.FireArrowCrossbowSchematic3: "Fire Arrow Crossbow Schematic 3",
    ItemId.FireArrowCrossbowSchematic4: "Fire Arrow Crossbow Schematic 4",
    ItemId.PoisonArrowCrossbowSchematic1: "Poison Arrow Crossbow Schematic 1",
    ItemId.PoisonArrowCrossbowSchematic2: "Poison Arrow Crossbow Schematic 2",
    ItemId.PoisonArrowCrossbowSchematic3: "Poison Arrow Crossbow Schematic 3",
    ItemId.PoisonArrowCrossbowSchematic4: "Poison Arrow Crossbow Schematic 4",
    ItemId.MakeshiftHandgunSchematic1: "Makeshift Handgun Schematic 1",
    ItemId.MakeshiftHandgunSchematic2: "Makeshift Handgun Schematic 2",
    ItemId.MakeshiftHandgunSchematic3: "Makeshift Handgun Schematic 3",
    ItemId.MakeshiftHandgunSchematic4: "Makeshift Handgun Schematic 4",
    ItemId.MusketSchematic1: "Musket Schematic 1",
    ItemId.MusketSchematic2: "Musket Schematic 2",
    ItemId.MusketSchematic3: "Musket Schematic 3",
    ItemId.MusketSchematic4: "Musket Schematic 4",
    ItemId.HandgunSchematic1: "Handgun Schematic 1",
    ItemId.HandgunSchematic2: "Handgun Schematic 2",
    ItemId.HandgunSchematic3: "Handgun Schematic 3",
    ItemId.HandgunSchematic4: "Handgun Schematic 4",
    ItemId.OldRevolverSchematic1: "Old Revolver Schematic 1",
    ItemId.OldRevolverSchematic2: "Old Revolver Schematic 2",
    ItemId.OldRevolverSchematic3: "Old Revolver Schematic 3",
    ItemId.OldRevolverSchematic4: "Old Revolver Schematic 4",
    ItemId.SingleShotRifleSchematic1: "Single-Shot Rifle Schematic 1",
    ItemId.SingleShotRifleSchematic2: "Single-Shot Rifle Schematic 2",
    ItemId.SingleShotRifleSchematic3: "Single-Shot Rifle Schematic 3",
    ItemId.SingleShotRifleSchematic4: "Single-Shot Rifle Schematic 4",
    ItemId.SemiAutoRifleSchematic1: "Semi-Auto Rifle Schematic 1",
    ItemId.SemiAutoRifleSchematic2: "Semi-Auto Rifle Schematic 2",
    ItemId.SemiAutoRifleSchematic3: "Semi-Auto Rifle Schematic 3",
    ItemId.SemiAutoRifleSchematic4: "Semi-Auto Rifle Schematic 4",
    ItemId.MakeshiftAssaultRifleSchematic1: "Makeshift Assault Rifle Schematic 1",
    ItemId.MakeshiftAssaultRifleSchematic2: "Makeshift Assault Rifle Schematic 2",
    ItemId.MakeshiftAssaultRifleSchematic3: "Makeshift Assault Rifle Schematic 3",
    ItemId.MakeshiftAssaultRifleSchematic4: "Makeshift Assault Rifle Schematic 4",
    ItemId.AssaultRifleSchematic1: "Assault Rifle Schematic 1",
    ItemId.AssaultRifleSchematic2: "Assault Rifle Schematic 2",
    ItemId.AssaultRifleSchematic3: "Assault Rifle Schematic 3",
    ItemId.AssaultRifleSchematic4: "Assault Rifle Schematic 4",
    ItemId.MakeshiftShotgunSchematic1: "Makeshift Shotgun Schematic 1",
    ItemId.MakeshiftShotgunSchematic2: "Makeshift Shotgun Schematic 2",
    ItemId.MakeshiftShotgunSchematic3: "Makeshift Shotgun Schematic 3",
    ItemId.MakeshiftShotgunSchematic4: "Makeshift Shotgun Schematic 4",
    ItemId.DoubleBarreledShotgunSchematic1: "Double-Barreled Shotgun Schematic 1",
    ItemId.DoubleBarreledShotgunSchematic2: "Double-Barreled Shotgun Schematic 2",
    ItemId.DoubleBarreledShotgunSchematic3: "Double-Barreled Shotgun Schematic 3",
    ItemId.DoubleBarreledShotgunSchematic4: "Double-Barreled Shotgun Schematic 4",
    ItemId.PumpActionShotgunSchematic1: "Pump-Action Shotgun Schematic 1",
    ItemId.PumpActionShotgunSchematic2: "Pump-Action Shotgun Schematic 2",
    ItemId.PumpActionShotgunSchematic3: "Pump-Action Shotgun Schematic 3",
    ItemId.PumpActionShotgunSchematic4: "Pump-Action Shotgun Schematic 4",
    ItemId.SemiAutoShotgunSchematic1: "Semi-Auto Shotgun Schematic 1",
    ItemId.SemiAutoShotgunSchematic2: "Semi-Auto Shotgun Schematic 2",
    ItemId.SemiAutoShotgunSchematic3: "Semi-Auto Shotgun Schematic 3",
    ItemId.SemiAutoShotgunSchematic4: "Semi-Auto Shotgun Schematic 4",
    ItemId.MakeshiftSMGSchematic1: "Makeshift SMG Schematic 1",
    ItemId.MakeshiftSMGSchematic2: "Makeshift SMG Schematic 2",
    ItemId.MakeshiftSMGSchematic3: "Makeshift SMG Schematic 3",
    ItemId.MakeshiftSMGSchematic4: "Makeshift SMG Schematic 4",
    ItemId.SMGSchematic1: "SMG Schematic 1",
    ItemId.SMGSchematic2: "SMG Schematic 2",
    ItemId.SMGSchematic3: "SMG Schematic 3",
    ItemId.SMGSchematic4: "SMG Schematic 4",
    ItemId.RocketLauncherSchematic1: "Rocket Launcher Schematic 1",
    ItemId.RocketLauncherSchematic2: "Rocket Launcher Schematic 2",
    ItemId.RocketLauncherSchematic3: "Rocket Launcher Schematic 3",
    ItemId.RocketLauncherSchematic4: "Rocket Launcher Schematic 4",
    ItemId.LaserRifleSchematic1: "Laser Rifle Schematic 1",
    ItemId.LaserRifleSchematic2: "Laser Rifle Schematic 2",
    ItemId.LaserRifleSchematic3: "Laser Rifle Schematic 3",
    ItemId.LaserRifleSchematic4: "Laser Rifle Schematic 4",
    ItemId.FlamethrowerSchematic1: "Flamethrower Schematic 1",
    ItemId.FlamethrowerSchematic2: "Flamethrower Schematic 2",
    ItemId.FlamethrowerSchematic3: "Flamethrower Schematic 3",
    ItemId.FlamethrowerSchematic4: "Flamethrower Schematic 4",
    ItemId.GrenadeLauncherSchematic1: "Grenade Launcher Schematic 1",
    ItemId.GrenadeLauncherSchematic2: "Grenade Launcher Schematic 2",
    ItemId.GrenadeLauncherSchematic3: "Grenade Launcher Schematic 3",
    ItemId.GrenadeLauncherSchematic4: "Grenade Launcher Schematic 4",
    ItemId.GuidedMissileLauncherSchematic1: "Guided Missile Launcher Schematic 1",
    ItemId.GuidedMissileLauncherSchematic2: "Guided Missile Launcher Schematic 2",
    ItemId.GuidedMissileLauncherSchematic3: "Guided Missile Launcher Schematic 3",
    ItemId.GuidedMissileLauncherSchematic4: "Guided Missile Launcher Schematic 4",
    ItemId.MultiGuidedMissileLauncherSchematic: "Multi Guided Missile Launcher Schematic",
    ItemId.MultiGuidedMissileLauncherSchematic1: "Multi Guided Missile Launcher Schematic 1",
    ItemId.MultiGuidedMissileLauncherSchematic2: "Multi Guided Missile Launcher Schematic 2",
    ItemId.MultiGuidedMissileLauncherSchematic3: "Multi Guided Missile Launcher Schematic 3",
    ItemId.MultiGuidedMissileLauncherSchematic4: "Multi Guided Missile Launcher Schematic 4",
    ItemId.GatlingGunSchematic1: "Gatling Gun Schematic 1",
    ItemId.GatlingGunSchematic2: "Gatling Gun Schematic 2",
    ItemId.GatlingGunSchematic3: "Gatling Gun Schematic 3",
    ItemId.GatlingGunSchematic4: "Gatling Gun Schematic 4",
    ItemId.LaserGatlingGunSchematic1: "Laser Gatling Gun Schematic 1",
    ItemId.LaserGatlingGunSchematic2: "Laser Gatling Gun Schematic 2",
    ItemId.LaserGatlingGunSchematic3: "Laser Gatling Gun Schematic 3",
    ItemId.LaserGatlingGunSchematic4: "Laser Gatling Gun Schematic 4",
    ItemId.PlasmaCannonSchematic1: "Plasma Cannon Schematic 1",
    ItemId.PlasmaCannonSchematic2: "Plasma Cannon Schematic 2",
    ItemId.PlasmaCannonSchematic3: "Plasma Cannon Schematic 3",
    ItemId.PlasmaCannonSchematic4: "Plasma Cannon Schematic 4",
    ItemId.CompoundBowSchematic1: "Compound Bow Schematic 1",
    ItemId.CompoundBowSchematic2: "Compound Bow Schematic 2",
    ItemId.CompoundBowSchematic3: "Compound Bow Schematic 3",
    ItemId.CompoundBowSchematic4: "Compound Bow Schematic 4",
    ItemId.AdvancedBowSchematic1: "Advanced Bow Schematic 1",
    ItemId.AdvancedBowSchematic2: "Advanced Bow Schematic 2",
    ItemId.AdvancedBowSchematic3: "Advanced Bow Schematic 3",
    ItemId.AdvancedBowSchematic4: "Advanced Bow Schematic 4",
    ItemId.OverheatRifleSchematic1: "Overheat Rifle Schematic 1",
    ItemId.OverheatRifleSchematic2: "Overheat Rifle Schematic 2",
    ItemId.OverheatRifleSchematic3: "Overheat Rifle Schematic 3",
    ItemId.OverheatRifleSchematic4: "Overheat Rifle Schematic 4",
    ItemId.ChargeRifleSchematic1: "Charge Rifle Schematic 1",
    ItemId.ChargeRifleSchematic2: "Charge Rifle Schematic 2",
    ItemId.ChargeRifleSchematic3: "Charge Rifle Schematic 3",
    ItemId.ChargeRifleSchematic4: "Charge Rifle Schematic 4",
    ItemId.EnergyShotgunSchematic1: "Energy Shotgun Schematic 1",
    ItemId.EnergyShotgunSchematic2: "Energy Shotgun Schematic 2",
    ItemId.EnergyShotgunSchematic3: "Energy Shotgun Schematic 3",
    ItemId.EnergyShotgunSchematic4: "Energy Shotgun Schematic 4",
    ItemId.MeteorLauncherSchematic4: "Meteor Launcher Schematic 4",
    ItemId.ExcaliburSchematic: "Excalibur Schematic",
    ItemId.ExcaliburSchematic1: "Excalibur Schematic 1",
    ItemId.ExcaliburSchematic2: "Excalibur Schematic 2",
    ItemId.ExcaliburSchematic3: "Excalibur Schematic 3",
    ItemId.ExcaliburSchematic4: "Excalibur Schematic 4",
    ItemId.TerraBladeSchematic: "Terra Blade Schematic",
    ItemId.TerraBladeSchematic1: "Terra Blade Schematic 1",
    ItemId.TerraBladeSchematic2: "Terra Blade Schematic 2",
    ItemId.TerraBladeSchematic3: "Terra Blade Schematic 3",
    ItemId.TerraBladeSchematic4: "Terra Blade Schematic 4",
    ItemId.VortexBeaterSchematic: "Vortex Beater Schematic",
    ItemId.VortexBeaterSchematic1: "Vortex Beater Schematic 1",
    ItemId.VortexBeaterSchematic2: "Vortex Beater Schematic 2",
    ItemId.VortexBeaterSchematic3: "Vortex Beater Schematic 3",
    ItemId.VortexBeaterSchematic4: "Vortex Beater Schematic 4",
    ItemId.NightglowSchematic: "Nightglow Schematic",
    ItemId.NightglowSchematic1: "Nightglow Schematic 1",
    ItemId.NightglowSchematic2: "Nightglow Schematic 2",
    ItemId.NightglowSchematic3: "Nightglow Schematic 3",
    ItemId.NightglowSchematic4: "Nightglow Schematic 4",
    ItemId.TerraprismaSchematic: "Terraprisma Schematic",
    ItemId.TerraprismaSchematic1: "Terraprisma Schematic 1",
    ItemId.TerraprismaSchematic2: "Terraprisma Schematic 2",
    ItemId.TerraprismaSchematic3: "Terraprisma Schematic 3",
    ItemId.TerraprismaSchematic4: "Terraprisma Schematic 4",
    ItemId.MarksmanRevolverSchematic1: "Marksman Revolver Schematic 1",
    ItemId.MarksmanRevolverSchematic2: "Marksman Revolver Schematic 2",
    ItemId.MarksmanRevolverSchematic3: "Marksman Revolver Schematic 3",
    ItemId.MarksmanRevolverSchematic4: "Marksman Revolver Schematic 4",
    ItemId.CoreEjectShotgunSchematic1: "Core Eject Shotgun Schematic 1",
    ItemId.CoreEjectShotgunSchematic2: "Core Eject Shotgun Schematic 2",
    ItemId.CoreEjectShotgunSchematic3: "Core Eject Shotgun Schematic 3",
    ItemId.CoreEjectShotgunSchematic4: "Core Eject Shotgun Schematic 4",
    ItemId.ClothOutfitSchematic1: "Cloth Outfit Schematic 1",
    ItemId.ClothOutfitSchematic2: "Cloth Outfit Schematic 2",
    ItemId.ClothOutfitSchematic3: "Cloth Outfit Schematic 3",
    ItemId.ClothOutfitSchematic4: "Cloth Outfit Schematic 4",
    ItemId.TropicalOutfitSchematic1: "Tropical Outfit Schematic 1",
    ItemId.TropicalOutfitSchematic2: "Tropical Outfit Schematic 2",
    ItemId.TropicalOutfitSchematic3: "Tropical Outfit Schematic 3",
    ItemId.TropicalOutfitSchematic4: "Tropical Outfit Schematic 4",
    ItemId.TundraOutfitSchematic1: "Tundra Outfit Schematic 1",
    ItemId.TundraOutfitSchematic2: "Tundra Outfit Schematic 2",
    ItemId.TundraOutfitSchematic3: "Tundra Outfit Schematic 3",
    ItemId.TundraOutfitSchematic4: "Tundra Outfit Schematic 4",
    ItemId.PeltArmorSchematic1: "Pelt Armor Schematic 1",
    ItemId.PeltArmorSchematic2: "Pelt Armor Schematic 2",
    ItemId.PeltArmorSchematic3: "Pelt Armor Schematic 3",
    ItemId.PeltArmorSchematic4: "Pelt Armor Schematic 4",
    ItemId.HeatResistantPeltArmorSchematic1: "Heat Resistant Pelt Armor Schematic 1",
    ItemId.HeatResistantPeltArmorSchematic2: "Heat Resistant Pelt Armor Schematic 2",
    ItemId.HeatResistantPeltArmorSchematic3: "Heat Resistant Pelt Armor Schematic 3",
    ItemId.HeatResistantPeltArmorSchematic4: "Heat Resistant Pelt Armor Schematic 4",
    ItemId.ColdResistantPeltArmorSchematic1: "Cold Resistant Pelt Armor Schematic 1",
    ItemId.ColdResistantPeltArmorSchematic2: "Cold Resistant Pelt Armor Schematic 2",
    ItemId.ColdResistantPeltArmorSchematic3: "Cold Resistant Pelt Armor Schematic 3",
    ItemId.ColdResistantPeltArmorSchematic4: "Cold Resistant Pelt Armor Schematic 4",
    ItemId.MetalArmorSchematic1: "Metal Armor Schematic 1",
    ItemId.MetalArmorSchematic2: "Metal Armor Schematic 2",
    ItemId.MetalArmorSchematic3: "Metal Armor Schematic 3",
    ItemId.MetalArmorSchematic4: "Metal Armor Schematic 4",
    ItemId.HeatResistantMetalArmorSchematic1: "Heat Resistant Metal Armor Schematic 1",
    ItemId.HeatResistantMetalArmorSchematic2: "Heat Resistant Metal Armor Schematic 2",
    ItemId.HeatResistantMetalArmorSchematic3: "Heat Resistant Metal Armor Schematic 3",
    ItemId.HeatResistantMetalArmorSchematic4: "Heat Resistant Metal Armor Schematic 4",
    ItemId.ColdResistantMetalArmorSchematic1: "Cold Resistant Metal Armor Schematic 1",
    ItemId.ColdResistantMetalArmorSchematic2: "Cold Resistant Metal Armor Schematic 2",
    ItemId.ColdResistantMetalArmorSchematic3: "Cold Resistant Metal Armor Schematic 3",
    ItemId.ColdResistantMetalArmorSchematic4: "Cold Resistant Metal Armor Schematic 4",
    ItemId.RefinedMetalArmorSchematic1: "Refined Metal Armor Schematic 1",
    ItemId.RefinedMetalArmorSchematic2: "Refined Metal Armor Schematic 2",
    ItemId.RefinedMetalArmorSchematic3: "Refined Metal Armor Schematic 3",
    ItemId.RefinedMetalArmorSchematic4: "Refined Metal Armor Schematic 4",
    ItemId.HeatResistantRefinedMetalArmorSchematic1: "Heat Resistant Refined Metal Armor Schematic 1",
    ItemId.HeatResistantRefinedMetalArmorSchematic2: "Heat Resistant Refined Metal Armor Schematic 2",
    ItemId.HeatResistantRefinedMetalArmorSchematic3: "Heat Resistant Refined Metal Armor Schematic 3",
    ItemId.HeatResistantRefinedMetalArmorSchematic4: "Heat Resistant Refined Metal Armor Schematic 4",
    ItemId.ColdResistantRefinedMetalArmorSchematic1: "Cold Resistant Refined Metal Armor Schematic 1",
    ItemId.ColdResistantRefinedMetalArmorSchematic2: "Cold Resistant Refined Metal Armor Schematic 2",
    ItemId.ColdResistantRefinedMetalArmorSchematic3: "Cold Resistant Refined Metal Armor Schematic 3",
    ItemId.ColdResistantRefinedMetalArmorSchematic4: "Cold Resistant Refined Metal Armor Schematic 4",
    ItemId.PalMetalArmorSchematic1: "Pal Metal Armor Schematic 1",
    ItemId.PalMetalArmorSchematic2: "Pal Metal Armor Schematic 2",
    ItemId.PalMetalArmorSchematic3: "Pal Metal Armor Schematic 3",
    ItemId.PalMetalArmorSchematic4: "Pal Metal Armor Schematic 4",
    ItemId.HeatResistantPalMetalArmorSchematic1: "Heat Resistant Pal Metal Armor Schematic 1",
    ItemId.HeatResistantPalMetalArmorSchematic2: "Heat Resistant Pal Metal Armor Schematic 2",
    ItemId.HeatResistantPalMetalArmorSchematic3: "Heat Resistant Pal Metal Armor Schematic 3",
    ItemId.HeatResistantPalMetalArmorSchematic4: "Heat Resistant Pal Metal Armor Schematic 4",
    ItemId.ColdResistantPalMetalArmorSchematic1: "Cold Resistant Pal Metal Armor Schematic 1",
    ItemId.ColdResistantPalMetalArmorSchematic2: "Cold Resistant Pal Metal Armor Schematic 2",
    ItemId.ColdResistantPalMetalArmorSchematic3: "Cold Resistant Pal Metal Armor Schematic 3",
    ItemId.ColdResistantPalMetalArmorSchematic4: "Cold Resistant Pal Metal Armor Schematic 4",
    ItemId.PlasteelArmorSchematic1: "Plasteel Armor Schematic 1",
    ItemId.PlasteelArmorSchematic2: "Plasteel Armor Schematic 2",
    ItemId.PlasteelArmorSchematic3: "Plasteel Armor Schematic 3",
    ItemId.PlasteelArmorSchematic4: "Plasteel Armor Schematic 4",
    ItemId.HeatResistantPlasteelArmorSchematic1: "Heat Resistant Plasteel Armor Schematic 1",
    ItemId.HeatResistantPlasteelArmorSchematic2: "Heat Resistant Plasteel Armor Schematic 2",
    ItemId.HeatResistantPlasteelArmorSchematic3: "Heat Resistant Plasteel Armor Schematic 3",
    ItemId.HeatResistantPlasteelArmorSchematic4: "Heat Resistant Plasteel Armor Schematic 4",
    ItemId.ColdResistantPlasteelArmorSchematic1: "Cold Resistant Plasteel Armor Schematic 1",
    ItemId.ColdResistantPlasteelArmorSchematic2: "Cold Resistant Plasteel Armor Schematic 2",
    ItemId.ColdResistantPlasteelArmorSchematic3: "Cold Resistant Plasteel Armor Schematic 3",
    ItemId.ColdResistantPlasteelArmorSchematic4: "Cold Resistant Plasteel Armor Schematic 4",
    ItemId.LightweightPlasteelArmorSchematic1: "Lightweight Plasteel Armor Schematic 1",
    ItemId.LightweightPlasteelArmorSchematic2: "Lightweight Plasteel Armor Schematic 2",
    ItemId.LightweightPlasteelArmorSchematic3: "Lightweight Plasteel Armor Schematic 3",
    ItemId.LightweightPlasteelArmorSchematic4: "Lightweight Plasteel Armor Schematic 4",
    ItemId.HexoliteArmorSchematic1: "Hexolite Armor Schematic 1",
    ItemId.HexoliteArmorSchematic2: "Hexolite Armor Schematic 2",
    ItemId.HexoliteArmorSchematic3: "Hexolite Armor Schematic 3",
    ItemId.HexoliteArmorSchematic4: "Hexolite Armor Schematic 4",
    ItemId.HeatResistantHexoliteArmorSchematic1: "Heat Resistant Hexolite Armor Schematic 1",
    ItemId.HeatResistantHexoliteArmorSchematic2: "Heat Resistant Hexolite Armor Schematic 2",
    ItemId.HeatResistantHexoliteArmorSchematic3: "Heat Resistant Hexolite Armor Schematic 3",
    ItemId.HeatResistantHexoliteArmorSchematic4: "Heat Resistant Hexolite Armor Schematic 4",
    ItemId.ColdResistantHexoliteArmorSchematic1: "Cold Resistant Hexolite Armor Schematic 1",
    ItemId.ColdResistantHexoliteArmorSchematic2: "Cold Resistant Hexolite Armor Schematic 2",
    ItemId.ColdResistantHexoliteArmorSchematic3: "Cold Resistant Hexolite Armor Schematic 3",
    ItemId.ColdResistantHexoliteArmorSchematic4: "Cold Resistant Hexolite Armor Schematic 4",
    ItemId.LightweightHexoliteArmorSchematic1: "Lightweight Hexolite Armor Schematic 1",
    ItemId.LightweightHexoliteArmorSchematic2: "Lightweight Hexolite Armor Schematic 2",
    ItemId.LightweightHexoliteArmorSchematic3: "Lightweight Hexolite Armor Schematic 3",
    ItemId.LightweightHexoliteArmorSchematic4: "Lightweight Hexolite Armor Schematic 4",
    ItemId.HallowedPlateMailSchematic: "Hallowed Plate Mail Schematic",
    ItemId.HallowedPlateMailSchematic1: "Hallowed Plate Mail Schematic 1",
    ItemId.HallowedPlateMailSchematic2: "Hallowed Plate Mail Schematic 2",
    ItemId.HallowedPlateMailSchematic3: "Hallowed Plate Mail Schematic 3",
    ItemId.HallowedPlateMailSchematic4: "Hallowed Plate Mail Schematic 4",
    ItemId.V1ArmorSchematic4: "V1 Armor Schematic 4",
    ItemId.V2ArmorSchematic4: "V2 Armor Schematic 4",
    ItemId.FeatheredHairBandSchematic1: "Feathered Hair Band Schematic 1",
    ItemId.FeatheredHairBandSchematic2: "Feathered Hair Band Schematic 2",
    ItemId.FeatheredHairBandSchematic3: "Feathered Hair Band Schematic 3",
    ItemId.FeatheredHairBandSchematic4: "Feathered Hair Band Schematic 4",
    ItemId.MetalHelmSchematic1: "Metal Helm Schematic 1",
    ItemId.MetalHelmSchematic2: "Metal Helm Schematic 2",
    ItemId.MetalHelmSchematic3: "Metal Helm Schematic 3",
    ItemId.MetalHelmSchematic4: "Metal Helm Schematic 4",
    ItemId.RefinedMetalHelmSchematic1: "Refined Metal Helm Schematic 1",
    ItemId.RefinedMetalHelmSchematic2: "Refined Metal Helm Schematic 2",
    ItemId.RefinedMetalHelmSchematic3: "Refined Metal Helm Schematic 3",
    ItemId.RefinedMetalHelmSchematic4: "Refined Metal Helm Schematic 4",
    ItemId.PalMetalHelmSchematic1: "Pal Metal Helm Schematic 1",
    ItemId.PalMetalHelmSchematic2: "Pal Metal Helm Schematic 2",
    ItemId.PalMetalHelmSchematic3: "Pal Metal Helm Schematic 3",
    ItemId.PalMetalHelmSchematic4: "Pal Metal Helm Schematic 4",
    ItemId.PlasteelHelmetSchematic1: "Plasteel Helmet Schematic 1",
    ItemId.PlasteelHelmetSchematic2: "Plasteel Helmet Schematic 2",
    ItemId.PlasteelHelmetSchematic3: "Plasteel Helmet Schematic 3",
    ItemId.PlasteelHelmetSchematic4: "Plasteel Helmet Schematic 4",
    ItemId.HexoliteHelmetSchematic1: "Hexolite Helmet Schematic 1",
    ItemId.HexoliteHelmetSchematic2: "Hexolite Helmet Schematic 2",
    ItemId.HexoliteHelmetSchematic3: "Hexolite Helmet Schematic 3",
    ItemId.HexoliteHelmetSchematic4: "Hexolite Helmet Schematic 4",
    ItemId.HallowedMaskSchematic: "Hallowed Mask Schematic",
    ItemId.HallowedMaskSchematic1: "Hallowed Mask Schematic 1",
    ItemId.HallowedMaskSchematic2: "Hallowed Mask Schematic 2",
    ItemId.HallowedMaskSchematic3: "Hallowed Mask Schematic 3",
    ItemId.HallowedMaskSchematic4: "Hallowed Mask Schematic 4",
    ItemId.HallowedHelmetSchematic: "Hallowed Helmet Schematic",
    ItemId.HallowedHelmetSchematic1: "Hallowed Helmet Schematic 1",
    ItemId.HallowedHelmetSchematic2: "Hallowed Helmet Schematic 2",
    ItemId.HallowedHelmetSchematic3: "Hallowed Helmet Schematic 3",
    ItemId.HallowedHelmetSchematic4: "Hallowed Helmet Schematic 4",
    ItemId.HallowedHeadgearSchematic: "Hallowed Headgear Schematic",
    ItemId.HallowedHeadgearSchematic1: "Hallowed Headgear Schematic 1",
    ItemId.HallowedHeadgearSchematic2: "Hallowed Headgear Schematic 2",
    ItemId.HallowedHeadgearSchematic3: "Hallowed Headgear Schematic 3",
    ItemId.HallowedHeadgearSchematic4: "Hallowed Headgear Schematic 4",
    ItemId.HallowedHoodSchematic: "Hallowed Hood Schematic",
    ItemId.HallowedHoodSchematic1: "Hallowed Hood Schematic 1",
    ItemId.HallowedHoodSchematic2: "Hallowed Hood Schematic 2",
    ItemId.HallowedHoodSchematic3: "Hallowed Hood Schematic 3",
    ItemId.HallowedHoodSchematic4: "Hallowed Hood Schematic 4",
    ItemId.MonarchSCrownSchematic1: "Monarch's Crown Schematic 1",
    ItemId.ZoeSHalloweenCostumeSchematic: "Zoe's Halloween Costume Schematic",
    ItemId.MonarchSCrownSchematic2: "Monarch's Crown Schematic 2",
    ItemId.MonarchSCrownSchematic3: "Monarch's Crown Schematic 3",
    ItemId.MonarchSCrownSchematic4: "Monarch's Crown Schematic 4",
    ItemId.BlueprintOfTheKingSCrown5: "Blueprint of the King's Crown 5",
    ItemId.GoldenCrownSchematic1: "Golden Crown Schematic 1",
    ItemId.GoldenCrownSchematic2: "Golden Crown Schematic 2",
    ItemId.GoldenCrownSchematic3: "Golden Crown Schematic 3",
    ItemId.GoldenCrownSchematic4: "Golden Crown Schematic 4",
    ItemId.BlueprintForGoldenCrown5: "Blueprint for Golden Crown 5",
    ItemId.LongEaredHeadbandSchematic1: "Long-Eared Headband Schematic 1",
    ItemId.LongEaredHeadbandSchematic2: "Long-Eared Headband Schematic 2",
    ItemId.LongEaredHeadbandSchematic3: "Long-Eared Headband Schematic 3",
    ItemId.LongEaredHeadbandSchematic4: "Long-Eared Headband Schematic 4",
    ItemId.ITEM5BlueprintsOfLongEaredHeadband: "5 Blueprints of Long-eared Headband",
    ItemId.WitchHatSchematic1: "Witch Hat Schematic 1",
    ItemId.WitchHatSchematic2: "Witch Hat Schematic 2",
    ItemId.WitchHatSchematic3: "Witch Hat Schematic 3",
    ItemId.WitchHatSchematic4: "Witch Hat Schematic 4",
    ItemId.DesignOfWitchHatNo5: "Design of Witch Hat No. 5",
    ItemId.SoftHatSchematic1: "Soft Hat Schematic 1",
    ItemId.SoftHatSchematic2: "Soft Hat Schematic 2",
    ItemId.SoftHatSchematic3: "Soft Hat Schematic 3",
    ItemId.SoftHatSchematic4: "Soft Hat Schematic 4",
    ItemId.BlueprintOfSoftHat5: "Blueprint of Soft Hat 5",
    ItemId.HelmetSchematic1: "Helmet Schematic 1",
    ItemId.HelmetSchematic2: "Helmet Schematic 2",
    ItemId.HelmetSchematic3: "Helmet Schematic 3",
    ItemId.HelmetSchematic4: "Helmet Schematic 4",
    ItemId.BlueprintOfHelmet5: "Blueprint of Helmet 5",
    ItemId.SilkHatSchematic1: "Silk Hat Schematic 1",
    ItemId.SilkHatSchematic2: "Silk Hat Schematic 2",
    ItemId.SilkHatSchematic3: "Silk Hat Schematic 3",
    ItemId.SilkHatSchematic4: "Silk Hat Schematic 4",
    ItemId.ITEM5SchematicDiagramsOfTheSilkHat: "5 Schematic Diagrams of the Silk Hat",
    ItemId.TricorneSchematic1: "Tricorne Schematic 1",
    ItemId.TricorneSchematic2: "Tricorne Schematic 2",
    ItemId.TricorneSchematic3: "Tricorne Schematic 3",
    ItemId.TricorneSchematic4: "Tricorne Schematic 4",
    ItemId.BlueprintOfTheTricornHat5: "Blueprint of the Tricorn Hat 5",
    ItemId.ExplorationCapSchematic1: "Exploration Cap Schematic 1",
    ItemId.ExplorationCapSchematic2: "Exploration Cap Schematic 2",
    ItemId.ExplorationCapSchematic3: "Exploration Cap Schematic 3",
    ItemId.ExplorationCapSchematic4: "Exploration Cap Schematic 4",
    ItemId.BlueprintOfExplorationHat5: "Blueprint of Exploration Hat 5",
    ItemId.GraduationCapSchematic1: "Graduation Cap Schematic 1",
    ItemId.GraduationCapSchematic2: "Graduation Cap Schematic 2",
    ItemId.GraduationCapSchematic3: "Graduation Cap Schematic 3",
    ItemId.GraduationCapSchematic4: "Graduation Cap Schematic 4",
    ItemId.Blueprint5OfUniversityHat: "Blueprint 5 of University Hat",
    ItemId.FarmingHatSchematic1: "Farming Hat Schematic 1",
    ItemId.FarmingHatSchematic2: "Farming Hat Schematic 2",
    ItemId.FarmingHatSchematic3: "Farming Hat Schematic 3",
    ItemId.FarmingHatSchematic4: "Farming Hat Schematic 4",
    ItemId.ITEM5DiagramsOfAgriculturalHat: "5 Diagrams of Agricultural Hat",
    ItemId.BowlerHatSchematic1: "Bowler Hat Schematic 1",
    ItemId.BowlerHatSchematic2: "Bowler Hat Schematic 2",
    ItemId.BowlerHatSchematic3: "Bowler Hat Schematic 3",
    ItemId.BowlerHatSchematic4: "Bowler Hat Schematic 4",
    ItemId.BlueprintOfBowlerHat5: "Blueprint of Bowler Hat 5",
    ItemId.TocotocoCapSchematic1: "Tocotoco Cap Schematic 1",
    ItemId.TocotocoCapSchematic2: "Tocotoco Cap Schematic 2",
    ItemId.TocotocoCapSchematic3: "Tocotoco Cap Schematic 3",
    ItemId.TocotocoCapSchematic4: "Tocotoco Cap Schematic 4",
    ItemId.DesignPlan5ForTheCrutchliHat: "Design Plan 5 for the Crutchli Hat",
    ItemId.GrinningTocotocoCapSchematic1: "Grinning Tocotoco Cap Schematic 1",
    ItemId.GrinningTocotocoCapSchematic2: "Grinning Tocotoco Cap Schematic 2",
    ItemId.GrinningTocotocoCapSchematic3: "Grinning Tocotoco Cap Schematic 3",
    ItemId.GrinningTocotocoCapSchematic4: "Grinning Tocotoco Cap Schematic 4",
    ItemId.GrinningCurlyHatBlueprint5: "Grinning Curly Hat Blueprint 5",
    ItemId.GumossCapSchematic1: "Gumoss Cap Schematic 1",
    ItemId.GumossCapSchematic2: "Gumoss Cap Schematic 2",
    ItemId.GumossCapSchematic3: "Gumoss Cap Schematic 3",
    ItemId.GumossCapSchematic4: "Gumoss Cap Schematic 4",
    ItemId.ITEM5BlueprintsOfNaemochiHat: "5 Blueprints of Naemochi Hat",
    ItemId.PenkingCapSchematic1: "Penking Cap Schematic 1",
    ItemId.PenkingCapSchematic2: "Penking Cap Schematic 2",
    ItemId.PenkingCapSchematic3: "Penking Cap Schematic 3",
    ItemId.PenkingCapSchematic4: "Penking Cap Schematic 4",
    ItemId.BlueprintOfCapppenHat5: "Blueprint of Capppen Hat 5",
    ItemId.KatressCapSchematic1: "Katress Cap Schematic 1",
    ItemId.KatressCapSchematic2: "Katress Cap Schematic 2",
    ItemId.KatressCapSchematic3: "Katress Cap Schematic 3",
    ItemId.KatressCapSchematic4: "Katress Cap Schematic 4",
    ItemId.DesignBlueprintOfClemenceHat5: "Design Blueprint of Clemence Hat 5",
    ItemId.LeezpunkHoodSchematic1: "Leezpunk Hood Schematic 1",
    ItemId.LeezpunkHoodSchematic2: "Leezpunk Hood Schematic 2",
    ItemId.LeezpunkHoodSchematic3: "Leezpunk Hood Schematic 3",
    ItemId.LeezpunkHoodSchematic4: "Leezpunk Hood Schematic 4",
    ItemId.UnknownItemBlueprintHeadEquip0255: "Unknown Item (Blueprint_HeadEquip025_5)",
    ItemId.KillamariCapSchematic1: "Killamari Cap Schematic 1",
    ItemId.KillamariCapSchematic2: "Killamari Cap Schematic 2",
    ItemId.KillamariCapSchematic3: "Killamari Cap Schematic 3",
    ItemId.KillamariCapSchematic4: "Killamari Cap Schematic 4",
    ItemId.UnknownItemBlueprintHeadEquip0265: "Unknown Item (Blueprint_HeadEquip026_5)",
    ItemId.RibbunyHeadbandSchematic1: "Ribbuny Headband Schematic 1",
    ItemId.RibbunyHeadbandSchematic2: "Ribbuny Headband Schematic 2",
    ItemId.RibbunyHeadbandSchematic3: "Ribbuny Headband Schematic 3",
    ItemId.RibbunyHeadbandSchematic4: "Ribbuny Headband Schematic 4",
    ItemId.UnknownItemBlueprintHeadEquip0285: "Unknown Item (Blueprint_HeadEquip028_5)",
    ItemId.SweeCapSchematic1: "Swee Cap Schematic 1",
    ItemId.SweeCapSchematic2: "Swee Cap Schematic 2",
    ItemId.SweeCapSchematic3: "Swee Cap Schematic 3",
    ItemId.SweeCapSchematic4: "Swee Cap Schematic 4",
    ItemId.UnknownItemBlueprintHeadEquip0315: "Unknown Item (Blueprint_HeadEquip031_5)",
    ItemId.DazziHatSchematic1: "Dazzi Hat Schematic 1",
    ItemId.DazziHatSchematic2: "Dazzi Hat Schematic 2",
    ItemId.DazziHatSchematic3: "Dazzi Hat Schematic 3",
    ItemId.DazziHatSchematic4: "Dazzi Hat Schematic 4",
    ItemId.UnknownItemBlueprintHeadEquip0325: "Unknown Item (Blueprint_HeadEquip032_5)",
    ItemId.BellanoirSSlabFragment: "Bellanoir's Slab Fragment",
    ItemId.BellanoirLiberoSSlabFragment: "Bellanoir Libero's Slab Fragment",
    ItemId.BlazamutRyuSlabFragment: "Blazamut Ryu Slab Fragment",
    ItemId.XenolordSlabFragment: "Xenolord Slab Fragment",
    ItemId.HartalisSlabFragment: "Hartalis Slab Fragment",
    ItemId.BellanoirLiberoUltraSlabFragment: "Bellanoir Libero (Ultra) Slab Fragment",
    ItemId.BlazamutRyuUltraSlabFragment: "Blazamut Ryu (Ultra) Slab Fragment",
    ItemId.XenolordUltraSlabFragment: "Xenolord (Ultra) Slab Fragment",
    ItemId.HartalisUltraSlabFragment: "Hartalis (Ultra) Slab Fragment",
    ItemId.BellanoirSSlab: "Bellanoir's Slab",
    ItemId.BellanoirLiberoSSlab: "Bellanoir Libero's Slab",
    ItemId.BlazamutRyuSlab: "Blazamut Ryu Slab",
    ItemId.XenolordSlab: "Xenolord Slab",
    ItemId.CelestialSigil: "Celestial Sigil",
    ItemId.HartalisSlab: "Hartalis Slab",
    ItemId.BellanoirLiberoUltraSlab: "Bellanoir Libero (Ultra) Slab",
    ItemId.BlazamutRyuUltraSlab: "Blazamut Ryu (Ultra) Slab",
    ItemId.XenolordUltraSlab: "Xenolord (Ultra) Slab",
    ItemId.CelestialSigilMaster: "Celestial Sigil [Master]",
    ItemId.HartalisUltraSlab: "Hartalis (Ultra) Slab",
    ItemId.PowerfulFishingMagnet: "Powerful Fishing Magnet",
    ItemId.RayneSyndicateFlagSchematic: "Rayne Syndicate Flag Schematic",
    ItemId.LyleenStatueSchematic: "Lyleen Statue Schematic",
    ItemId.FreePalAllianceFlagSchematic: "Free Pal Alliance Flag Schematic",
    ItemId.FreePalAllianceBannerSchematic: "Free Pal Alliance Banner Schematic",
    ItemId.WireFenceSchematic: "Wire Fence Schematic",
    ItemId.WoodenBarricadeSchematic: "Wooden Barricade Schematic",
    ItemId.MajesticWallTorchSchematic: "Majestic Wall Torch Schematic",
    ItemId.CeremonialCandlestickSchematic: "Ceremonial Candlestick Schematic",
    ItemId.MajesticCandlestickSchematic: "Majestic Candlestick Schematic",
    ItemId.PaperLanternSchematic: "Paper Lantern Schematic",
    ItemId.RedWoodenLanternSchematic: "Red Wooden Lantern Schematic",
    ItemId.YakumoStatueSchematic: "Yakumo Statue Schematic",
    ItemId.LaboratoryDeskSchematic: "Laboratory Desk Schematic",
    ItemId.LaboratoryChairSchematic: "Laboratory Chair Schematic",
    ItemId.MoonLordStatueSchematic: "Moon Lord Statue Schematic",
    ItemId.CelestialSigilSchematic: "Celestial Sigil Schematic",
    ItemId.BeginnerFishingRodGumossSchematic: "Beginner Fishing Rod (Gumoss) Schematic",
    ItemId.IntermediateFishingRodCroajiroSchematic: "Intermediate Fishing Rod (Croajiro) Schematic",
    ItemId.AdvancedFishingRodDepressoSchematic: "Advanced Fishing Rod (Depresso) Schematic",
    ItemId.UnknownItemBlueprintSalvageTreasureBoxKey01: "Unknown Item (Blueprint_Salvage_TreasureBoxKey01)",
    ItemId.UnknownItemBlueprintSalvageFishingBait1A: "Unknown Item (Blueprint_Salvage_FishingBait_1_A)",
    ItemId.UnknownItemBlueprintSalvageFishingBait1B: "Unknown Item (Blueprint_Salvage_FishingBait_1_B)",
    ItemId.UnknownItemBlueprintSalvageFishingBait2A: "Unknown Item (Blueprint_Salvage_FishingBait_2_A)",
    ItemId.UnknownItemBlueprintSalvageFishingBait2B: "Unknown Item (Blueprint_Salvage_FishingBait_2_B)",
    ItemId.UnknownItemBlueprintSalvageFishingBait3B: "Unknown Item (Blueprint_Salvage_FishingBait_3_B)",
    ItemId.AnimalSkin: "Animal Skin",
    ItemId.EnText1: "en Text +1",
    ItemId.EnText63: "en Text +63",
    ItemId.EnText64: "en Text +64",
    ItemId.EnText5: "en Text +5",
    ItemId.EnText7: "en Text +7",
    ItemId.EnText9: "en Text +9",
    ItemId.Claw: "Claw",
    ItemId.EnText12: "en Text +12",
    ItemId.EnText13: "en Text +13",
    ItemId.EnText14: "en Text +14",
    ItemId.EnText27: "en Text +27",
    ItemId.EnText28: "en Text +28",
    ItemId.Fang: "Fang",
    ItemId.EnText29: "en Text +29",
    ItemId.EnText30: "en Text +30",
    ItemId.EnText31: "en Text +31",
    ItemId.EnText32: "en Text +32",
    ItemId.EnText33: "en Text +33",
    ItemId.EnText35: "en Text +35",
    ItemId.GrilledMeat: "Grilled Meat",
    ItemId.Gunpowder: "Gunpowder",
    ItemId.EnText40: "en Text +40",
    ItemId.EnText45: "en Text +45",
    ItemId.EnText41: "en Text +41",
    ItemId.EnText43: "en Text +43",
    ItemId.EnText44: "en Text +44",
    ItemId.EnText47: "en Text +47",
    ItemId.RawMeat: "Raw Meat",
    ItemId.EnText49: "en Text +49",
    ItemId.RadarSphere: "Radar Sphere",
    ItemId.PalSphereDebug: "PalSphere_Debug",
    ItemId.EnText56: "en Text +56",
    ItemId.EnText61: "en Text +61",
    ItemId.EnText70: "en Text +70",
    ItemId.EnText2AssaultRifleNPC: "en Text +2",
    ItemId.EnText3: "en Text +3",
    ItemId.EnText8: "en Text +8",
    ItemId.EnText65: "en Text +65",
    ItemId.EnText66: "en Text +66",
    ItemId.EnText68: "en Text +68",
    ItemId.EnText34: "en Text +34",
    ItemId.EnText37: "en Text +37",
    ItemId.EnText36: "en Text +36",
    ItemId.EnText69: "en Text +69",
    ItemId.PaldiumClump: "Paldium Clump",
    ItemId.EnText54: "en Text +54",
    ItemId.EnText53: "en Text +53",
    ItemId.EnText52: "en Text +52",
    ItemId.EnText55: "en Text +55",
    ItemId.Dung: "Dung",
    ItemId.HugeDung: "Huge Dung",
    ItemId.EnText71: "en Text +71",
    ItemId.EnText72: "en Text +72",
    ItemId.EnText73: "en Text +73",
    ItemId.EnText60: "en Text +60",
    ItemId.PotatoSeedPotatoes: "PotatoSeedPotatoes",
    ItemId.EnText58: "en Text +58",
    ItemId.EnText15: "en Text +15",
    ItemId.EnText59: "en Text +59",
    ItemId.EnText4BakedPotato: "en Text +4",
    ItemId.Computer: "Computer",
    ItemId.Grape: "Grape",
    ItemId.Hop: "Hop",
    ItemId.Potage: "Potage",
    ItemId.Curry: "Curry",
    ItemId.Cheeseburger: "Cheeseburger",
    ItemId.Sandwich: "Sandwich",
    ItemId.CornSoup: "Corn Soup",
    ItemId.Stew: "Stew",
    ItemId.GrilledFish: "Grilled Fish",
    ItemId.SeafoodSoup: "Seafood Soup",
    ItemId.LuxuryOmelette: "LuxuryOmelette",
    ItemId.Beer: "Beer",
    ItemId.Wine: "Wine",
    ItemId.AntibioticNormal: "Antibiotic_Normal",
    ItemId.AntibioticGood: "Antibiotic_Good",
    ItemId.AntibioticSuper: "Antibiotic_Super",
    ItemId.FishingRodOld: "Fishing Rod_Old",
    ItemId.FishingRodGood: "Fishing Rod_Good",
    ItemId.FishingRodSuper: "Fishing Rod_Super",
    ItemId.FishingRodLegendary: "Fishing Rod_Legendary",
    ItemId.HyperGlider: "Hyper Glider",
    ItemId.UnknownItemPVGliderManta: "Unknown Item (PV_Glider_Manta)",
    ItemId.LightzHelmet: "Lightz Helmet",
    ItemId.GasMask: "Gas Mask",
    ItemId.NightVisionGoggles: "Night Vision Goggles",
    ItemId.EnText10: "en Text +10",
    ItemId.EnText11: "en Text +11",
    ItemId.EnText24: "en Text +24",
    ItemId.EnText17: "en Text +17",
    ItemId.EnText26: "en Text +26",
    ItemId.EnText21: "en Text +21",
    ItemId.EnText20: "en Text +20",
    ItemId.EnText23: "en Text +23",
    ItemId.EnText22: "en Text +22",
    ItemId.EnText18: "en Text +18",
    ItemId.EnText25: "en Text +25",
    ItemId.EnText16: "en Text +16",
    ItemId.EnText19: "en Text +19",
    ItemId.EnText: "en Text",
    ItemId.DragostropheSShotgun: "Dragostrophe's Shotgun",
    ItemId.BoltmaneSaddle: "Boltmane Saddle",
    ItemId.EnTextSPowerConverter: "en_text's Power Converter",
    ItemId.EnText62: "en Text +62",
    ItemId.DarkSkillFruitPsychoGravity: "Dark Skill Fruit: Psycho Gravity",
    ItemId.EnText51: "en Text +51",
    ItemId.EnText48: "en Text +48",
    ItemId.UnknownItemBlueprintTest: "Unknown Item (BlueprintTest)",
    ItemId.SummoningAltar: "Summoning Altar",
    ItemId.EnText50: "en Text +50",
    ItemId.EnText39: "en Text +39",
    ItemId.UNKNOWN: "-",
    ItemId.ITEM1: "- +1",
    ItemId.DogCoin: "Dog Coin",
    ItemId.EnText42: "en Text +42",
    ItemId.EnText6: "en Text +6",
    ItemId.UnknownItemPalGenderReverseTest: "Unknown Item (PalGenderReverseTest)",
    ItemId.UnknownItemPalPassiveSkillChangeTest: "Unknown Item (PalPassiveSkillChangeTest)",
    ItemId.UnknownItemPalPassiveSkillChangeTest2: "Unknown Item (PalPassiveSkillChangeTest2)",
    ItemId.UnknownItemTESTCaptureItemModifier: "Unknown Item (TEST_CaptureItemModifier)",
    ItemId.UnknownItemFishingRodTest: "Unknown Item (FishingRod_Test)",
    ItemId.EnText38: "en Text +38",
    ItemId.UnknownItemSweetCaramel: "Unknown Item (Sweet_Caramel)",
    ItemId.LifmunkEffigy: "Lifmunk Effigy",
    ItemId.HipLantern: "Hip Lantern",
    ItemId.EnhancedHipLantern: "Enhanced Hip Lantern",
    ItemId.SmallFeedBag: "Small Feed Bag",
    ItemId.AverageFeedBag: "Average Feed Bag",
    ItemId.LargeFeedBag: "Large Feed Bag",
    ItemId.HugeFeedBag: "Huge Feed Bag",
    ItemId.GiantFeedBag: "Giant Feed Bag",
    ItemId.MysteriousAccessoryBox: "Mysterious Accessory Box",
    ItemId.BoxOfMysteryAccessories: "Box of Mystery Accessories",
    ItemId.LockpickingToolV1: "Lockpicking Tool v1",
    ItemId.LockpickingToolV2: "Lockpicking Tool v2",
    ItemId.LockpickingToolV3: "Lockpicking Tool v3",
    ItemId.JolthogSGloves: "Jolthog's Gloves",
    ItemId.JolthogCrystSGloves: "Jolthog Cryst's Gloves",
    ItemId.FoxparksHarness: "Foxparks' Harness",
    ItemId.FoxparksCrystSHarness: "Foxparks Cryst's Harness",
    ItemId.MelpacaSaddle: "Melpaca Saddle",
    ItemId.SweepaSaddle: "Sweepa Saddle",
    ItemId.RushoarSaddle: "Rushoar Saddle",
    ItemId.CelaraySGloves: "Celaray's Gloves",
    ItemId.CelarayLuxSGloves: "Celaray Lux's Gloves",
    ItemId.LifmunkSSubmachineGun: "Lifmunk's Submachine Gun",
    ItemId.DirehowlSSaddledHarness: "Direhowl's Saddled Harness",
    ItemId.TanzeeSAssaultRifle: "Tanzee's Assault Rifle",
    ItemId.UnknownItemSkillUnlockMonkeyIce: "Unknown Item (SkillUnlock_Monkey_Ice)",
    ItemId.SurfentSaddle: "Surfent Saddle",
    ItemId.SurfentTerraSaddle: "Surfent Terra Saddle",
    ItemId.EikthyrdeerSaddle: "Eikthyrdeer Saddle",
    ItemId.EikthyrdeerTerraSaddle: "Eikthyrdeer Terra Saddle",
    ItemId.GrintaleSaddle: "Grintale Saddle",
    ItemId.HerbilSHarness: "Herbil's Harness",
    ItemId.PolapupSaddle: "Polapup Saddle",
    ItemId.UnivoltSaddle: "Univolt Saddle",
    ItemId.UnknownItemSkillUnlockKirinIce: "Unknown Item (SkillUnlock_Kirin_Ice)",
    ItemId.KillamariSGloves: "Killamari's Gloves",
    ItemId.KillamariPrimoSGloves: "Killamari Primo's Gloves",
    ItemId.TocotocoSGloves: "Tocotoco's Gloves",
    ItemId.NitewingSaddle: "Nitewing Saddle",
    ItemId.ArsoxSaddle: "Arsox Saddle",
    ItemId.FlopieSNecklace: "Flopie's Necklace",
    ItemId.DigtoiseSHeadband: "Digtoise's Headband",
    ItemId.PengulletRocketLauncher: "Pengullet Rocket Launcher",
    ItemId.PengulletLuxSRocketLauncher: "Pengullet Lux's Rocket Launcher",
    ItemId.DinossomSaddle: "Dinossom Saddle",
    ItemId.DinossomLuxSaddle: "Dinossom Lux Saddle",
    ItemId.DaedreamSNecklace: "Daedream's Necklace",
    ItemId.BroncherrySaddle: "Broncherry Saddle",
    ItemId.BroncherryAquaSaddle: "Broncherry Aqua Saddle",
    ItemId.VanwyrmSaddle: "Vanwyrm Saddle",
    ItemId.VanwyrmCrystSaddle: "Vanwyrm Cryst Saddle",
    ItemId.ChilletSaddle: "Chillet Saddle",
    ItemId.ChilletIgnisSaddle: "Chillet Ignis Saddle",
    ItemId.HangyuSGloves: "Hangyu's Gloves",
    ItemId.HangyuCrystSGlove: "Hangyu Cryst's Glove",
    ItemId.KingpacaSaddle: "Kingpaca Saddle",
    ItemId.KingpacaCrystSaddle: "Kingpaca Cryst Saddle",
    ItemId.ElphidranSaddle: "Elphidran Saddle",
    ItemId.ElphidranAquaSaddle: "Elphidran Aqua Saddle",
    ItemId.DazziSNecklace: "Dazzi's Necklace",
    ItemId.DazziNoctSNecklace: "Dazzi Noct's Necklace",
    ItemId.DazemuSaddle: "Dazemu Saddle",
    ItemId.GaleclawSGloves: "Galeclaw's Gloves",
    ItemId.MaraithSaddle: "Maraith Saddle",
    ItemId.GhanglerSaddle: "Ghangler Saddle",
    ItemId.GhanglerIgnisSaddle: "Ghangler Ignis Saddle",
    ItemId.BralohaSaddle: "Braloha Saddle",
    ItemId.PalumbaSaddle: "Palumba Saddle",
    ItemId.MossandaSGrenadeLauncher: "Mossanda's Grenade Launcher",
    ItemId.MossandaLuxSGrenadeLauncher: "Mossanda Lux's Grenade Launcher",
    ItemId.TarantrissSaddle: "Tarantriss Saddle",
    ItemId.ReptyroSaddle: "Reptyro Saddle",
    ItemId.ReptyroCrystSaddle: "Reptyro Cryst Saddle",
    ItemId.PyrinSaddle: "Pyrin Saddle",
    ItemId.PyrinNoctSaddle: "Pyrin Noct Saddle",
    ItemId.MammorestSaddle: "Mammorest Saddle",
    ItemId.MammorestCrystSaddle: "Mammorest Cryst Saddle",
    ItemId.AzurobeSaddle: "Azurobe Saddle",
    ItemId.AzurobeCrystSaddle: "Azurobe Cryst Saddle",
    ItemId.JormuntideSaddle: "Jormuntide Saddle",
    ItemId.JormuntideIgnisSaddle: "Jormuntide Ignis Saddle",
    ItemId.KitsunSaddle: "Kitsun Saddle",
    ItemId.KitsunNoctSaddle: "Kitsun Noct Saddle",
    ItemId.RayhoundSaddle: "Rayhound Saddle",
    ItemId.UnknownItemSkillUnlockThunderDogIce: "Unknown Item (SkillUnlock_ThunderDog_Ice)",
    ItemId.BlazehowlSaddle: "Blazehowl Saddle",
    ItemId.BlazehowlNoctSaddle: "Blazehowl Noct Saddle",
    ItemId.ReindrixSaddle: "Reindrix Saddle",
    ItemId.BeakonSaddle: "Beakon Saddle",
    ItemId.RagnahawkSaddle: "Ragnahawk Saddle",
    ItemId.FalerisSaddle: "Faleris Saddle",
    ItemId.FalerisAquaSaddle: "Faleris Aqua Saddle",
    ItemId.QuivernSaddle: "Quivern Saddle",
    ItemId.QuivernBotanSaddle: "Quivern Botan Saddle",
    ItemId.HelzephyrSaddle: "Helzephyr Saddle",
    ItemId.HelzephyrLuxSaddle: "Helzephyr Lux Saddle",
    ItemId.FenglopeSaddle: "Fenglope Saddle",
    ItemId.FenglopeLuxSaddle: "Fenglope Lux Saddle",
    ItemId.SuzakuSaddle: "Suzaku Saddle",
    ItemId.SuzakuAquaSaddle: "Suzaku Aqua Saddle",
    ItemId.YakumoSaddle: "Yakumo Saddle",
    ItemId.BlazamutSaddle: "Blazamut Saddle",
    ItemId.BlazamutRyuSaddle: "Blazamut Ryu Saddle",
    ItemId.WumpoSaddle: "Wumpo Saddle",
    ItemId.WumpoBotanSaddle: "Wumpo Botan Saddle",
    ItemId.WhalaskaSaddle: "Whalaska Saddle",
    ItemId.WhalaskaIgnisSaddle: "Whalaska Ignis Saddle",
    ItemId.UnknownItemSkillUnlockGrassGolem: "Unknown Item (SkillUnlock_GrassGolem)",
    ItemId.UnknownItemSkillUnlockGrassGolemDark: "Unknown Item (SkillUnlock_GrassGolem_Dark)",
    ItemId.UnknownItemSkillUnlockPyramidTurtle: "Unknown Item (SkillUnlock_PyramidTurtle)",
    ItemId.UnknownItemSkillUnlockKingSunfish: "Unknown Item (SkillUnlock_KingSunfish)",
    ItemId.UnknownItemSkillUnlockSumoDog: "Unknown Item (SkillUnlock_SumoDog)",
    ItemId.GrizzboltSMinigun: "Grizzbolt's Minigun",
    ItemId.ShadowbeakSaddle: "Shadowbeak Saddle",
    ItemId.AstegonSaddle: "Astegon Saddle",
    ItemId.RelaxaurusMissileLauncher: "Relaxaurus' Missile Launcher",
    ItemId.RelaxaurusLuxSMissileLauncher: "Relaxaurus Lux's Missile Launcher",
    ItemId.ShroomerSaddle: "Shroomer Saddle",
    ItemId.ShroomerNoctSaddle: "Shroomer Noct Saddle",
    ItemId.FrostallionSaddle: "Frostallion Saddle",
    ItemId.FrostallionNoctSaddle: "Frostallion Noct Saddle",
    ItemId.PaladiusSaddle: "Paladius Saddle",
    ItemId.NecromusSaddle: "Necromus Saddle",
    ItemId.JetragonSMissileLauncher: "Jetragon's Missile Launcher",
    ItemId.XenogardSaddle: "Xenogard Saddle",
    ItemId.SelyneSaddle: "Selyne Saddle",
    ItemId.SmokieSHarness: "Smokie's Harness",
    ItemId.UnknownItemSkillUnlockBlackPuppyIce: "Unknown Item (SkillUnlock_BlackPuppy_Ice)",
    ItemId.StarryonSaddle: "Starryon Saddle",
    ItemId.UnknownItemSkillUnlockNightBlueHorseNeutral: "Unknown Item (SkillUnlock_NightBlueHorse_Neutral)",
    ItemId.AzurmaneSaddle: "Azurmane Saddle",
    ItemId.GildaneSaddle: "Gildane Saddle",
    ItemId.NyafiaSShotgun: "Nyafia's Shotgun",
    ItemId.CelesdirSaddle: "Celesdir Saddle",
    ItemId.SilvegisSaddle: "Silvegis Saddle",
    ItemId.BastigorSHammer: "Bastigor's Hammer",
    ItemId.XenolordSaddle: "Xenolord Saddle",
    ItemId.NeptiliusSaddle: "Neptilius Saddle",
    ItemId.UnknownItemSkillUnlockVolcanoDragon: "Unknown Item (SkillUnlock_VolcanoDragon)",
    ItemId.HartalisSaddle: "Hartalis Saddle",
    ItemId.SmallPouch: "Small Pouch",
    ItemId.MediumPouch: "Medium Pouch",
    ItemId.LargePouch: "Large Pouch",
    ItemId.GiantPouch: "Giant Pouch",
    ItemId.HeavyWeightModule: "Heavy Weight Module",
    ItemId.CurveModule: "Curve Module",
    ItemId.SniperModule: "Sniper Module",
    ItemId.SliderModule: "Slider Module",
    ItemId.SniperModuleSphereModuleSniper2: "Sniper Module Ⅱ",
    ItemId.HomingModule: "Homing Module",
    ItemId.UnknownItemTESTBossDefeatReward: "Unknown Item (TEST_BossDefeatReward)",
    ItemId.ChilletBountyToken: "Chillet Bounty Token",
    ItemId.SweepaBountyToken: "Sweepa Bounty Token",
    ItemId.GumossBountyToken: "Gumoss Bounty Token",
    ItemId.DumudBountyToken: "Dumud Bounty Token",
    ItemId.PenkingBountyToken: "Penking Bounty Token",
    ItemId.AzurobeBountyToken: "Azurobe Bounty Token",
    ItemId.GrintaleBountyToken: "Grintale Bounty Token",
    ItemId.NitewingBountyToken: "Nitewing Bounty Token",
    ItemId.QuivernBountyToken: "Quivern Bounty Token",
    ItemId.FelbatBountyToken: "Felbat Bounty Token",
    ItemId.KingpacaBountyToken: "Kingpaca Bounty Token",
    ItemId.BroncherryBountyToken: "Broncherry Bounty Token",
    ItemId.KatressBountyToken: "Katress Bounty Token",
    ItemId.BushiBountyToken: "Bushi Bounty Token",
    ItemId.FenglopeBountyToken: "Fenglope Bounty Token",
    ItemId.PetalliaBountyToken: "Petallia Bounty Token",
    ItemId.BeakonBountyToken: "Beakon Bounty Token",
    ItemId.WarsectBountyToken: "Warsect Bounty Token",
    ItemId.BroncherryAquaBountyToken: "Broncherry Aqua Bounty Token",
    ItemId.ElphidranBountyToken: "Elphidran Bounty Token",
    ItemId.RelaxaurusBountyToken: "Relaxaurus Bounty Token",
    ItemId.UnivoltBountyToken: "Univolt Bounty Token",
    ItemId.ElizabeeBountyToken: "Elizabee Bounty Token",
    ItemId.MossandaLuxBountyToken: "Mossanda Lux Bounty Token",
    ItemId.LunarisBountyToken: "Lunaris Bounty Token",
    ItemId.VerdashBountyToken: "Verdash Bounty Token",
    ItemId.WumpoBotanBountyToken: "Wumpo Botan Bounty Token",
    ItemId.MammorestBountyToken: "Mammorest Bounty Token",
    ItemId.VaeletBountyToken: "Vaelet Bounty Token",
    ItemId.SibelyxBountyToken: "Sibelyx Bounty Token",
    ItemId.MenastingBountyToken: "Menasting Bounty Token",
    ItemId.SuzakuBountyToken: "Suzaku Bounty Token",
    ItemId.JormuntideBountyToken: "Jormuntide Bounty Token",
    ItemId.IceKingpacaBountyToken: "Ice Kingpaca Bounty Token",
    ItemId.DinossomLuxBountyToken: "Dinossom Lux Bounty Token",
    ItemId.AnubisBountyToken: "Anubis Bounty Token",
    ItemId.AstegonBountyToken: "Astegon Bounty Token",
    ItemId.BlazamutBountyToken: "Blazamut Bounty Token",
    ItemId.LyleenNoctBountyToken: "Lyleen Noct Bounty Token",
    ItemId.MenastingTerraBountyToken: "Menasting Terra Bounty Token",
    ItemId.KnocklemBountyToken: "Knocklem Bounty Token",
    ItemId.SplatterinaBountyToken: "Splatterina Bounty Token",
    ItemId.AzurmaneBountyToken: "Azurmane Bounty Token",
    ItemId.KitsunNoctBountyToken: "Kitsun Noct Bounty Token",
    ItemId.FenglopeLuxBountyToken: "Fenglope Lux Bounty Token",
    ItemId.CelesdirBountyToken: "Celesdir Bounty Token",
    ItemId.SilvegisBountyToken: "Silvegis Bounty Token",
    ItemId.FalerisAquaBountyToken: "Faleris Aqua Bounty Token",
    ItemId.JetragonBountyToken: "Jetragon Bounty Token",
    ItemId.FrostallionBountyToken: "Frostallion Bounty Token",
    ItemId.TwinKnightsBountyToken: "Twin Knights Bounty Token",
    ItemId.SmokieBountyToken: "Smokie Bounty Token",
    ItemId.NitemaryBountyToken: "Nitemary Bounty Token",
    ItemId.StarryonBountyToken: "Starryon Bounty Token",
    ItemId.PruneliaBountyToken: "Prunelia Bounty Token",
    ItemId.NyafiaBountyToken: "Nyafia Bounty Token",
    ItemId.GildaneBountyToken: "Gildane Bounty Token",
    ItemId.OmasculBountyToken: "Omascul Bounty Token",
    ItemId.TarantrisBountyToken: "Tarantris Bounty Token",
    ItemId.FrostallionNoctBountyToken: "Frostallion Noct Bounty Token",
    ItemId.FoxparksCrystBountyToken: "Foxparks Cryst Bounty Token",
    ItemId.DazziNoctBountyToken: "Dazzi Noct Bounty Token",
    ItemId.CryolinxTerraBountyToken: "Cryolinx Terra Bounty Token",
    ItemId.CaprityNoctBountyToken: "Caprity Noct Bounty Token",
    ItemId.LoupmoonCrystBountyToken: "Loupmoon Cryst Bounty Token",
    ItemId.RibbunyBotanBountyToken: "Ribbuny Botan Bounty Token",
    ItemId.WarsectTerraBountyToken: "Warsect Terra Bounty Token",
    ItemId.WhalaskaBountyToken: "Whalaska Bounty Token",
    ItemId.NeptiliusBountyToken: "Neptilius Bounty Token",
    ItemId.WhalaskaIgnisBountyToken: "Whalaska Ignis Bounty Token",
    ItemId.FarmerSSpecialDish: "Farmer's Special Dish",
    ItemId.ZoeSTatteredMemento: "Zoe's Tattered Memento",
    ItemId.ZoeSHalloweenCostume: "Zoe's Halloween Costume",
    ItemId.BreederSPreciousPal: "Breeder's Precious Pal",
    ItemId.TreasureMap: "Treasure Map",
    ItemId.TreasureMap1: "Treasure Map +1",
    ItemId.TreasureMap2: "Treasure Map +2",
    ItemId.TreasureMap3: "Treasure Map +3",
    ItemId.TreasureMap4: "Treasure Map +4",
    ItemId.ChampionSEmblem: "Champion's Emblem",
}
