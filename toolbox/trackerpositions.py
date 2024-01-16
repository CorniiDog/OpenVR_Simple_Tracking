import openvr, time
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R

#######################################################################################
# How to use this file
#######################################################################################
# This file is a library of functions that grabs the position and rotation of the headset,
# controllers, base stations, and trackers.
# To use this file, import it into your own file like this:
# import trackerpositions
#######################################################################################

#######################################################################################
# What this file does
#######################################################################################
# This file is used to grab the position and rotation of the headset, controllers,
# base stations, and trackers.
# NOTE: rotations are in degrees, not radians.
# To convert to radians, use np.radians(rotation) or set radians=True in the function call.
#######################################################################################

#######################################################################################
# Steps in main.py:
#######################################################################################
# 1. Import trackerpositions.py
# ex:
# import trackerpositions
#
# 2. Get headset position and rotation
# ex:
# headset_position, headset_rotation = trackerpositions.get_headset_pose()
#
# 3. Get left controller position and rotation
# ex:
# controller_position, controller_rotation = trackerpositions.get_left_controller_pose()
#
# 4. Get right controller position and rotation
# ex:
# controller_position, controller_rotation = trackerpositions.get_right_controller_pose()
#
# 5. Get base station position and rotation
# ex:
# base_station_position, base_station_rotation = trackerpositions.get_base_station_pose(0) # 0 is the index of the first base station
#
# 6. Get tracker position and rotation
# ex:
# tracker_position, tracker_rotation = trackerpositions.get_tracker_pose(0) # 0 is the index of the first tracker
#
#######################################################################################

#######################################################################################
# Setup and Configuration
#######################################################################################
# If no devices are connected, this will return [0, 0, 0] for position and [0, 0, 0] for rotation
must_return_positions = True
#######################################################################################

try:
    vr_system = openvr.init(openvr.VRApplication_Background)
except openvr.OpenVRError as e:
    print(e)
    print("Error: Could not initialize OpenVR. Is SteamVR running?")
    exit(1)


# def matrix_to_euler_angles(rotation_matrix):
#     # Convert rotation matrix to Euler angles (X-Y-Z, extrinsic rotations)
#     sy = np.sqrt(rotation_matrix[0][0] * rotation_matrix[0][0] + rotation_matrix[1][0] * rotation_matrix[1][0])
#     singular = sy < 1e-6
#     if not singular:
#         x = np.arctan2(rotation_matrix[2][1], rotation_matrix[2][2])
#         y = np.arctan2(-rotation_matrix[2][0], sy)
#         z = np.arctan2(rotation_matrix[1][0], rotation_matrix[0][0])
#     else:
#         x = np.arctan2(-rotation_matrix[1][2], rotation_matrix[1][1])
#         y = np.arctan2(-rotation_matrix[2][0], sy)
#         z = 0.0
#     return np.degrees(x), np.degrees(y), np.degrees(z)

def get_position_rotation_from_hmd_pose(hmd_pose):
    # Extract position and rotation from hmd_pose
    position = -hmd_pose.mDeviceToAbsoluteTracking[0][3], hmd_pose.mDeviceToAbsoluteTracking[2][3], hmd_pose.mDeviceToAbsoluteTracking[1][3]

    rotation = np.zeros((3, 3))
    for i in range(3):
        rotation[0][i] = -hmd_pose.mDeviceToAbsoluteTracking[0][i]
        rotation[1][i] = hmd_pose.mDeviceToAbsoluteTracking[2][i]
        rotation[2][i] = hmd_pose.mDeviceToAbsoluteTracking[1][i]

    rotation = R.from_matrix(rotation).as_euler('xyz', degrees=True)

    return position, rotation

def get_all_poses():
    global vr_system
    poses = vr_system.getDeviceToAbsoluteTrackingPose(openvr.TrackingUniverseStanding, 0,
                                                      openvr.k_unMaxTrackedDeviceCount)

    positions = []
    rotations = []
    for i in range(openvr.k_unMaxTrackedDeviceCount):
        hmd_pose = poses[i]
        position, rotation = get_position_rotation_from_hmd_pose(hmd_pose)
        positions.append(position)
        rotations.append(rotation)

    return positions, rotations

def get_base_station_pose(base_station_index):
    global vr_system

    # Find the indices of all connected base stations
    base_station_indices = []
    for i in range(openvr.k_unMaxTrackedDeviceCount):
        device_class = vr_system.getTrackedDeviceClass(i)
        if device_class == openvr.TrackedDeviceClass_TrackingReference:
            is_connected = vr_system.isTrackedDeviceConnected(i)
            if is_connected:
                base_station_indices.append(i)

    if not base_station_indices:
        if must_return_positions:
            return [0, 0, 0], [0, 0, 0]
        print("Could not find any connected base stations")
        return None

    # Compute the adjusted index for the input base station
    if base_station_index < len(base_station_indices):
        adjusted_base_station_index = base_station_indices[base_station_index]
    else:
        return None

    # Get the pose of the base station
    poses = vr_system.getDeviceToAbsoluteTrackingPose(openvr.TrackingUniverseStanding, 0, openvr.k_unMaxTrackedDeviceCount)
    base_station_pose = poses[adjusted_base_station_index]

    position, rotation = get_position_rotation_from_hmd_pose(base_station_pose)

    return position, rotation



def get_headset_pose():
    global vr_system
    poses = vr_system.getDeviceToAbsoluteTrackingPose(openvr.TrackingUniverseStanding, 0,
                                                      openvr.k_unMaxTrackedDeviceCount)
    hmd_pose = poses[openvr.k_unTrackedDeviceIndex_Hmd + 0]

    position, rotation = get_position_rotation_from_hmd_pose(hmd_pose)

    return position, rotation

def get_left_controller_pose():
    global vr_system

    # Find the index of the left controller
    left_controller_index = None
    for i in range(openvr.k_unMaxTrackedDeviceCount):
        device_class = vr_system.getTrackedDeviceClass(i)
        if device_class == openvr.TrackedDeviceClass_Controller:
            role = vr_system.getControllerRoleForTrackedDeviceIndex(i)
            if role == openvr.TrackedControllerRole_LeftHand:
                left_controller_index = i
                break

    if left_controller_index is None:
        if must_return_positions:
            return [0, 0, 0], [0, 0, 0]
        print("Could not find left controller")
        return None

    # Get the pose of the left controller
    poses = vr_system.getDeviceToAbsoluteTrackingPose(openvr.TrackingUniverseStanding, 0, openvr.k_unMaxTrackedDeviceCount)
    controller_pose = poses[left_controller_index]

    position, rotation = get_position_rotation_from_hmd_pose(controller_pose)

    return position, rotation



def get_right_controller_pose():
    global vr_system

    # Find the index of the right controller
    right_controller_index = None
    for i in range(openvr.k_unMaxTrackedDeviceCount):
        device_class = vr_system.getTrackedDeviceClass(i)
        if device_class == openvr.TrackedDeviceClass_Controller:
            role = vr_system.getControllerRoleForTrackedDeviceIndex(i)
            if role == openvr.TrackedControllerRole_RightHand:
                right_controller_index = i
                break

    if right_controller_index is None:
        if must_return_positions:
            return [0, 0, 0], [0, 0, 0]
        print("Could not find right controller")
        return None

    # Get the pose of the right controller
    poses = vr_system.getDeviceToAbsoluteTrackingPose(openvr.TrackingUniverseStanding, 0, openvr.k_unMaxTrackedDeviceCount)
    controller_pose = poses[right_controller_index]

    position, rotation = get_position_rotation_from_hmd_pose(controller_pose)

    return position, rotation


def get_tracker_pose(index:int):
    global vr_system

    # Find the index of the waist tracker
    tracker_indexes = []
    for i in range(openvr.k_unMaxTrackedDeviceCount):
        device_class = vr_system.getTrackedDeviceClass(i)
        if device_class == openvr.TrackedDeviceClass_GenericTracker:
            tracker_indexes.append(i)
    if len(tracker_indexes) == 0:
        if must_return_positions:
            return [0, 0, 0], [0, 0, 0]
        print("Could not find any trackers")
        return None

    # Get the pose of the waist tracker
    poses = vr_system.getDeviceToAbsoluteTrackingPose(openvr.TrackingUniverseStanding, 0, openvr.k_unMaxTrackedDeviceCount)
    tracker_pose = poses[tracker_indexes[index]]

    position, rotation = get_position_rotation_from_hmd_pose(tracker_pose)

    return position, rotation

