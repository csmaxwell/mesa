import unittest

from mesa.space import ContinuousSpace
from test_grid import MockAgent

TEST_AGENTS = [(-20, -20), (-20, -20.05), (65, 18)]


class TestSpaceToroidal(unittest.TestCase):
    '''
    Testing a toroidal continuous space.
    '''

    def setUp(self):
        '''
        Create a test space and populate with Mock Agents.
        '''
        self.space = ContinuousSpace(70, 20, True, -30, -30, 100, 100)
        self.agents = []
        for i, pos in enumerate(TEST_AGENTS):
            a = MockAgent(i, None)
            self.agents.append(a)
            self.space.place_agent(a, pos)

    def test_agent_positions(self):
        '''
        Ensure that the agents are all placed properly.
        '''
        for i, pos in enumerate(TEST_AGENTS):
            a = self.agents[i]
            assert a.pos == pos

    def test_distance_calculations(self):
        '''
        Test toroidal distance calculations.
        '''
        pos_1 = (-30, -30)
        pos_2 = (70, 20)
        assert self.space.get_distance(pos_1, pos_2) == 0

        pos_3 = (-30, -20)
        assert self.space.get_distance(pos_1, pos_3) == 10

    def test_neighborhood_retrieval(self):
        '''
        Test neighborhood retrieval
        '''
        neighbors_1 = self.space.get_neighbors((-20, -20), 1)
        assert len(neighbors_1) == 2

        neighbors_2 = self.space.get_neighbors((40, -10), 10)
        assert len(neighbors_2) == 0

        neighbors_3 = self.space.get_neighbors((-30, -30), 10)
        assert len(neighbors_3) == 1


class TestSpaceNonToroidal(unittest.TestCase):
    '''
    Testing a toroidal continuous space.
    '''

    def setUp(self):
        '''
        Create a test space and populate with Mock Agents.
        '''
        self.space = ContinuousSpace(70, 20, False, -30, -30, 100, 100)
        self.agents = []
        for i, pos in enumerate(TEST_AGENTS):
            a = MockAgent(i, None)
            self.agents.append(a)
            self.space.place_agent(a, pos)

    def test_agent_positions(self):
        '''
        Ensure that the agents are all placed properly.
        '''
        for i, pos in enumerate(TEST_AGENTS):
            a = self.agents[i]
            assert a.pos == pos

    def test_distance_calculations(self):
        '''
        Test toroidal distance calculations.
        '''

        pos_2 = (70, 20)
        pos_3 = (-30, -20)
        assert self.space.get_distance(pos_2, pos_3) == 107.70329614269008

    def test_neighborhood_retrieval(self):
        '''
        Test neighborhood retrieval
        '''
        neighbors_1 = self.space.get_neighbors((-20, -20), 1)
        assert len(neighbors_1) == 2

        neighbors_2 = self.space.get_neighbors((40, -10), 10)
        assert len(neighbors_2) == 0

        neighbors_3 = self.space.get_neighbors((-30, -30), 10)
        assert len(neighbors_3) == 0

if __name__ == '__main__':
    unittest.main()
