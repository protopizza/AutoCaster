
class Player(object):
    def __init__(self, id):
        self.id = id;
        self.dataId = 0;
        self.name = ""
        self.champion = ""
        self.isAlive = False
        self.team = 100
        self.participantId = 0
        self.health = 0
        self.mana = 0
        self.armor = 0
        self.mr = 0
        self.ad = 0
        self.ap = 0
        self.items = []
        self.spells = []
        self.spellLevels = []
        self.spellCDs = []
        self.kills = 0
        self.killCount = 0
        self.deaths = 0
        self.assists = 0
        self.attackSpeed = 0
        self.respawnTimer = 0
        self.attackSpeed = 0
        self.movementSpeed = 0
        self.cs = 0
        self.level = 1
        self.exp = 0
        self.goldTotal = 0
        self.goldCurrent = 0

    def update(self, propertyChangedEvent):
        if (propertyChangedEvent.propertyName == "Kills"):
            if (self.kills == propertyChangedEvent.value):
                return False;

            self.kills = propertyChangedEvent.value;
        elif (propertyChangedEvent.propertyName == "KillCount"):
            if (self.killCount == propertyChangedEvent.value):
                return False;

            self.killCount = propertyChangedEvent.value;
        elif (propertyChangedEvent.propertyName == "Heatlh"):
            if (self.health == propertyChangedEvent.value):
                return False;

            self.health = propertyChangedEvent.value;
        elif (propertyChangedEvent.propertyName == "Level"):
            if (self.level == propertyChangedEvent.value):
                return False;

            self.level = propertyChangedEvent.value;
        elif (propertyChangedEvent.propertyName == "GoldTotal"):
            if (self.goldTotal == propertyChangedEvent.value):
                return False;

            self.goldTotal = propertyChangedEvent.value;
        elif (propertyChangedEvent.propertyName == "GoldCurrent"):
            if (self.goldCurrent == propertyChangedEvent.value):
                return False;

            self.goldCurrent = propertyChangedEvent.value;

        return True;