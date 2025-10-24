# Copyright (c) 2022-2024, The Berkeley Humanoid Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import gymnasium as gym

from . import agents, rough_env_cfg
from . import flat_env_cfg

##
# Register Gym environments.
##

gym.register(
    id="JasonLab-Isaac-Velocity-Rough-Jason-Q1-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": rough_env_cfg.JasonQ1RoughEnvCfg,
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:JasonQ1RoughPPORunnerCfg",
    },
)



gym.register(
    id="JasonLab-Isaac-Velocity-Flat-Jason-Q1-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": flat_env_cfg.JasonQ1FlatEnvCfg,
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:JasonQ1FlatPPORunnerCfg",
    },
)