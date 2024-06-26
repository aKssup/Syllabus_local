import gymnasium as gym
import numpy as np
from syllabus.core import TaskWrapper
from syllabus.task_space import TaskSpace

class CrafterTaskWrapper(TaskWrapper):
    """
    This wrapper allows you to change the task of a Crafter environment.
    """
    def __init__(self, env: gym.Env, area=(64, 64), view=(9, 9), size=(64, 64), seed=None):
        super().__init__(env)
        self.task_space = TaskSpace()
        self.task = np.random.randint(0, 2**31 - 1) if seed is None else seed
        

