# Copyright (c) 2024-2025 Ziqi Fan
# SPDX-License-Identifier: Apache-2.0

from isaaclab.utils import configclass

from .rough_env_cfg import JasonQ1RoughEnvCfg


@configclass
class JasonQ1FlatEnvCfg(JasonQ1RoughEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()

        # 添加关节驱动刚度配置
        self.scene.robot.spawn.joint_drive.gains.stiffness = 100.0  # 设置刚度值
        # 如果需要，也可以设置阻尼值
        if hasattr(self.scene.robot.spawn.joint_drive.gains, 'damping'):
            self.scene.robot.spawn.joint_drive.gains.damping = 10.0

        # override rewards
        self.rewards.base_height_l2.params["sensor_cfg"] = None
        # change terrain to flat
        self.scene.terrain.terrain_type = "plane"
        self.scene.terrain.terrain_generator = None
        # no height scan
        self.scene.height_scanner = None
        self.observations.policy.height_scan = None
        self.observations.critic.height_scan = None
        # no terrain curriculum
        self.curriculum.terrain_levels = None

        # Rewards
        self.rewards.lin_vel_z_l2.weight = -0.2

        # If the weight of rewards is 0, set rewards to None
        if self.__class__.__name__ == "JasonQ1FlatEnvCfg":
            self.disable_zero_weight_rewards()