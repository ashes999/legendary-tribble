from tribble.main import Main
from tribble.player import Player

from tests.utils.creature import Creature
from tests.utils.string_logger import StringLogger

class TestMain:
    def test_constructor_sets_floor_to_one_and_creates_new_player(self):
        m = Main()        
        assert m.floor_number == 1
        
        expected_player = Player()
        actual_player = m.player
        
        assert expected_player.total_health == actual_player.total_health
        assert expected_player.strength == actual_player.strength
        assert expected_player.defense == actual_player.defense
        assert expected_player.agility == actual_player.agility
        
    def test_process_command_prints_error_if_command_doesnt_exist(self):
        logger = StringLogger()
        m = Main(logger.log)
        m.process_command("hi", "")
        assert logger.messages.find("isn't a valid command") > -1
        
    def test_generate_floor_generates_at_least_N_monsters_for_floor_N(self):
        m = Main()
        m.generate_floor()
        assert len(m.monsters) >= 1
        
        m.floor_number = 10
        m.generate_floor()
        assert len(m.monsters) >= 10
        
    def test_fight_prints_error_if_monster_doesnt_exist(self):
        logger = StringLogger()
        m = Main(logger.log)
        m.generate_floor()
        m.fight("superduperawesomemonster")
        assert logger.messages.find("There doesn't seem to be any") > -1
        assert logger.messages.find("superduperawesomemonster") > -1
        
    def test_fight_fights_monster(self):
        logger = StringLogger()
        m = Main(logger.log, self.do_nothing)
        
        # Should be a pushover to defeat.
        c = Creature(10, 1, 1)
        c.name = "slime"
        m.monsters = [c]
        
        m.fight("slime")
        assert logger.messages.find("Victory") > -1
        assert c.current_health <= 0
        
    def do_nothing(a, b):
        pass