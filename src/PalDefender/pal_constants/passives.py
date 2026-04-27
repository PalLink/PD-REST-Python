from enum import Enum

class PassiveId(str, Enum):
    RemarkableCraftsmanship = "CraftSpeed_up3"
    DiamondBody = "Deffence_up3"
    Lucky = "Rare"
    Legend = "Legend"
    SirenOfTheVoid = "Witch"
    EternalFlame = "EternalFlame"
    Invader = "Invader"
    DemonGod = "PAL_ALLAttack_up3"
    MasteryOfFasting = "PAL_FullStomach_Down_3"
    HeartOfTheImmovableKing = "PAL_Sanity_Down_3"
    Swift = "MoveSpeed_up_3"
    EternalEngine = "Stamina_Up_3"
    Vampiric = "Vampire"
    Lunker = "Nushi"
    KingOfTheWaves = "SwimSpeed_up_3"
    Savior = "Salvation"
    Artisan = "CraftSpeed_up2"
    BurlyBody = "Deffence_up2"
    Ferocious = "PAL_ALLAttack_up2"
    Vanguard = "TrainerATK_UP_1"
    StrongholdStrategist = "TrainerDEF_UP_1"
    MotivationalLeader = "TrainerWorkSpeed_UP_1"
    MineForeman = "TrainerMining_up1"
    LoggingForeman = "TrainerLogging_up1"
    DietLover = "PAL_FullStomach_Down_2"
    Workaholic = "PAL_Sanity_Down_2"
    CelestialEmperor = "ElementBoost_Normal_2_PAL"
    FlameEmperor = "ElementBoost_Fire_2_PAL"
    LordOfTheSea = "ElementBoost_Aqua_2_PAL"
    LordOfLightning = "ElementBoost_Thunder_2_PAL"
    SpiritEmperor = "ElementBoost_Leaf_2_PAL"
    IceEmperor = "ElementBoost_Ice_2_PAL"
    EarthEmperor = "ElementBoost_Earth_2_PAL"
    LordOfTheUnderworld = "ElementBoost_Dark_2_PAL"
    DivineDragon = "ElementBoost_Dragon_2_PAL"
    Runner = "MoveSpeed_up_2"
    Philanthropist = "Test_PalEgg_HatchingSpeed_Up"
    Serenity = "CoolTimeReduction_Up_1"
    InfiniteStamina = "Stamina_Up_1"
    Noble = "SalePrice_Up_1"
    AceSwimmer = "SwimSpeed_up_2"
    Musclehead = "Noukin"
    Serious = "CraftSpeed_up1"
    HardSkin = "Deffence_up1"
    Brave = "PAL_ALLAttack_up1"
    Hooligan = "PAL_rude"
    Conceited = "PAL_conceited"
    Sadist = "PAL_sadist"
    Masochist = "PAL_masochist"
    WorkSlave = "PAL_CorporateSlave"
    Aggressive = "PAL_oraora"
    Abnormal = "ElementResist_Normal_1_PAL"
    SuntanLover = "ElementResist_Fire_1_PAL"
    Waterproof = "ElementResist_Aqua_1_PAL"
    InsulatedBody = "ElementResist_Thunder_1_PAL"
    BotanicalBarrier = "ElementResist_Leaf_1_PAL"
    HeatedBody = "ElementResist_Ice_1_PAL"
    EarthquakeResistant = "ElementResist_Earth_1_PAL"
    Cheery = "ElementResist_Dark_1_PAL"
    Dragonkiller = "ElementResist_Dragon_1_PAL"
    ZenMind = "ElementBoost_Normal_1_PAL"
    Pyromaniac = "ElementBoost_Fire_1_PAL"
    Hydromaniac = "ElementBoost_Aqua_1_PAL"
    Capacitor = "ElementBoost_Thunder_1_PAL"
    FragrantFoliage = "ElementBoost_Leaf_1_PAL"
    Coldblooded = "ElementBoost_Ice_1_PAL"
    PowerOfGaia = "ElementBoost_Earth_1_PAL"
    VeilOfDarkness = "ElementBoost_Dark_1_PAL"
    BloodOfTheDragon = "ElementBoost_Dragon_1_PAL"
    DaintyEater = "PAL_FullStomach_Down_1"
    PositiveThinker = "PAL_Sanity_Down_1"
    Nimble = "MoveSpeed_up_1"
    Nocturnal = "Nocturnal"
    Impatient = "CoolTimeReduction_Up_2"
    FitAsAFiddle = "Stamina_Up_2"
    FineFurs = "SalePrice_Up_2"
    OtherworldlyCells = "Alien"
    SleekStroke = "SwimSpeed_up_1"
    Clumsy = "CraftSpeed_down1"
    Downtrodden = "Deffence_down1"
    Coward = "PAL_ALLAttack_down1"
    Glutton = "PAL_FullStomach_Up_1"
    Unstable = "PAL_Sanity_Up_1"
    MercyHit = "NonKilling"
    Easygoing = "CoolTimeReduction_Down_1"
    Sickly = "Stamina_Down_1"
    Shabby = "SalePrice_Down_1"
    BottomlessStomach = "PAL_FullStomach_Up_2"
    Destructive = "PAL_Sanity_Up_2"
    Slacker = "CraftSpeed_down2"
    Brittle = "Deffence_down2"
    Pacifist = "PAL_ALLAttack_down2"

PASSIVE_ID_TO_NAME = {
    PassiveId.RemarkableCraftsmanship: "Remarkable Craftsmanship",
    PassiveId.DiamondBody: "Diamond Body",
    PassiveId.Lucky: "Lucky",
    PassiveId.Legend: "Legend",
    PassiveId.SirenOfTheVoid: "Siren of the Void",
    PassiveId.EternalFlame: "Eternal Flame",
    PassiveId.Invader: "Invader",
    PassiveId.DemonGod: "Demon God",
    PassiveId.MasteryOfFasting: "Mastery of Fasting",
    PassiveId.HeartOfTheImmovableKing: "Heart of the Immovable King",
    PassiveId.Swift: "Swift",
    PassiveId.EternalEngine: "Eternal Engine",
    PassiveId.Vampiric: "Vampiric",
    PassiveId.Lunker: "Lunker",
    PassiveId.KingOfTheWaves: "King of the Waves",
    PassiveId.Savior: "Savior",
    PassiveId.Artisan: "Artisan",
    PassiveId.BurlyBody: "Burly Body",
    PassiveId.Ferocious: "Ferocious",
    PassiveId.Vanguard: "Vanguard",
    PassiveId.StrongholdStrategist: "Stronghold Strategist",
    PassiveId.MotivationalLeader: "Motivational Leader",
    PassiveId.MineForeman: "Mine Foreman",
    PassiveId.LoggingForeman: "Logging Foreman",
    PassiveId.DietLover: "Diet Lover",
    PassiveId.Workaholic: "Workaholic",
    PassiveId.CelestialEmperor: "Celestial Emperor",
    PassiveId.FlameEmperor: "Flame Emperor",
    PassiveId.LordOfTheSea: "Lord of the Sea",
    PassiveId.LordOfLightning: "Lord of Lightning",
    PassiveId.SpiritEmperor: "Spirit Emperor",
    PassiveId.IceEmperor: "Ice Emperor",
    PassiveId.EarthEmperor: "Earth Emperor",
    PassiveId.LordOfTheUnderworld: "Lord of the Underworld",
    PassiveId.DivineDragon: "Divine Dragon",
    PassiveId.Runner: "Runner",
    PassiveId.Philanthropist: "Philanthropist",
    PassiveId.Serenity: "Serenity",
    PassiveId.InfiniteStamina: "Infinite Stamina",
    PassiveId.Noble: "Noble",
    PassiveId.AceSwimmer: "Ace Swimmer",
    PassiveId.Musclehead: "Musclehead",
    PassiveId.Serious: "Serious",
    PassiveId.HardSkin: "Hard Skin",
    PassiveId.Brave: "Brave",
    PassiveId.Hooligan: "Hooligan",
    PassiveId.Conceited: "Conceited",
    PassiveId.Sadist: "Sadist",
    PassiveId.Masochist: "Masochist",
    PassiveId.WorkSlave: "Work Slave",
    PassiveId.Aggressive: "Aggressive",
    PassiveId.Abnormal: "Abnormal",
    PassiveId.SuntanLover: "Suntan Lover",
    PassiveId.Waterproof: "Waterproof",
    PassiveId.InsulatedBody: "Insulated Body",
    PassiveId.BotanicalBarrier: "Botanical Barrier",
    PassiveId.HeatedBody: "Heated Body",
    PassiveId.EarthquakeResistant: "Earthquake Resistant",
    PassiveId.Cheery: "Cheery",
    PassiveId.Dragonkiller: "Dragonkiller",
    PassiveId.ZenMind: "Zen Mind",
    PassiveId.Pyromaniac: "Pyromaniac",
    PassiveId.Hydromaniac: "Hydromaniac",
    PassiveId.Capacitor: "Capacitor",
    PassiveId.FragrantFoliage: "Fragrant Foliage",
    PassiveId.Coldblooded: "Coldblooded",
    PassiveId.PowerOfGaia: "Power of Gaia",
    PassiveId.VeilOfDarkness: "Veil of Darkness",
    PassiveId.BloodOfTheDragon: "Blood of the Dragon",
    PassiveId.DaintyEater: "Dainty Eater",
    PassiveId.PositiveThinker: "Positive Thinker",
    PassiveId.Nimble: "Nimble",
    PassiveId.Nocturnal: "Nocturnal",
    PassiveId.Impatient: "Impatient",
    PassiveId.FitAsAFiddle: "Fit as a Fiddle",
    PassiveId.FineFurs: "Fine Furs",
    PassiveId.OtherworldlyCells: "Otherworldly Cells",
    PassiveId.SleekStroke: "Sleek Stroke",
    PassiveId.Clumsy: "Clumsy",
    PassiveId.Downtrodden: "Downtrodden",
    PassiveId.Coward: "Coward",
    PassiveId.Glutton: "Glutton",
    PassiveId.Unstable: "Unstable",
    PassiveId.MercyHit: "Mercy Hit",
    PassiveId.Easygoing: "Easygoing",
    PassiveId.Sickly: "Sickly",
    PassiveId.Shabby: "Shabby",
    PassiveId.BottomlessStomach: "Bottomless Stomach",
    PassiveId.Destructive: "Destructive",
    PassiveId.Slacker: "Slacker",
    PassiveId.Brittle: "Brittle",
    PassiveId.Pacifist: "Pacifist",
}
