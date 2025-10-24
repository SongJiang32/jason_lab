# Copyright (c) 2022-2024, The Berkeley Humanoid Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import isaaclab.sim as sim_utils
from isaaclab.actuators import DelayedPDActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg

from jason_lab.assets import ISAACLAB_ASSETS_DATA_DIR

JASON_Q1_CFG = ArticulationCfg(
    spawn=sim_utils.UrdfFileCfg(
        fix_base=False,
        merge_fixed_joints=True,
        replace_cylinders_with_capsules=False,    
        asset_path=f"{ISAACLAB_ASSETS_DATA_DIR}/Robots/jason/q1_description/urdf/q1.urdf",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=4, solver_velocity_iteration_count=0
        ),
        joint_drive=sim_utils.UrdfConverterCfg.JointDriveCfg(
            gains=sim_utils.UrdfConverterCfg.JointDriveCfg.PDGainsCfg(stiffness=0, damping=0)
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.449),   # 随机化出生高度，默认值为 (0.0, 0.0, 0.30)，实际采样由 reset 事件控制
        joint_pos={
            'hip_yaw_l': 0.4,
            'hip_yaw_r': -0.4,
            'hip_roll_l': -0.1,
            'hip_roll_r': 0.1,
            'hip_pitch_l': -1.5,
            'hip_pitch_r': 1.5,
            'knee_pitch_l': 1.0,
            'knee_pitch_r': -1.0,
            'ankle_pitch_l': -1.3,
            'ankle_pitch_r': 1.3,
        },
    ),
    actuators={
        "hip_yaw": DelayedPDActuatorCfg(
            joint_names_expr=["hip_yaw_.*"],
            effort_limit=23.7,  # Base.asset.effort or urdf
            velocity_limit=30.0,
            stiffness=55.0,     # Base.pd_gains.stiffness['hip_yaw']
            damping=0.3,        # Base.pd_gains.damping['hip_yaw']
            armature=0.0,       # Base.asset.armature
            friction=0.02,
            min_delay=0,
            max_delay=4,
        ),
        "hip_roll": DelayedPDActuatorCfg(
            joint_names_expr=["hip_roll_.*"],
            effort_limit=23.7,
            velocity_limit=30.0,
            stiffness=105.0,    # Base.pd_gains.stiffness['hip_roll']
            damping=2.5,        # Base.pd_gains.damping['hip_roll']
            armature=0.0,
            friction=0.02,
            min_delay=0,
            max_delay=4,
        ),
        "hip_pitch": DelayedPDActuatorCfg(
            joint_names_expr=["hip_pitch_.*"],
            effort_limit=23.7,
            velocity_limit=30.0,
            stiffness=75.0,     # Base.pd_gains.stiffness['hip_pitch']
            damping=0.3,        # Base.pd_gains.damping['hip_pitch']
            armature=0.0,
            friction=0.02,
            min_delay=0,
            max_delay=4,
        ),
        "knee_pitch": DelayedPDActuatorCfg(
            joint_names_expr=["knee_pitch_.*"],
            effort_limit=23.7,
            velocity_limit=30.0,
            stiffness=45.0,     # Base.pd_gains.stiffness['knee']
            damping=0.5,        # Base.pd_gains.damping['knee']
            armature=0.0,
            friction=0.02,
            min_delay=0,
            max_delay=4,
        ),
        "ankle_pitch": DelayedPDActuatorCfg(
            joint_names_expr=["ankle_pitch_.*"],
            effort_limit=23.7,
            velocity_limit=30.0,
            stiffness=30.0,     # Base.pd_gains.stiffness['ankle']
            damping=0.25,       # Base.pd_gains.damping['ankle']
            armature=0.0,
            friction=0.02,
            min_delay=0,
            max_delay=4,
        ),
    },
    soft_joint_pos_limit_factor=0.95,
)
