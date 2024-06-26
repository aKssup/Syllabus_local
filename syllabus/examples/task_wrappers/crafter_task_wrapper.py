import gymnasium as gym
import numpy as np
from syllabus.core import TaskWrapper
from syllabus.task_space import TaskSpace

class CrafterTaskWrapper(TaskWrapper):
    """
    This wrapper allows you to change the task of a Crafter environment.
    """
    def __init__(self, env: gym.Env, seed=0):
        super().

