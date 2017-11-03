import numpy as np

def getJointROM(data, jjoint_ind):
    # Get extremal values of a given joint_ind
    # data : output from getAnglesInDir
    # joint_ind : index to joint 
    return {'min': np.min(data['angles'][:,joint_ind]),'max':np.max(data['angles'][:,joint_ind])}

def getJointROM_frames(data, joint_ind, num_frames):
    # Tries to get a series of imags which show the ROM of a given joint by selecting rendered frames that are closest to linearly spaced values of the joint angle between its extremal values
    # data : output from getAnglesInDir
    # joint_ind : index to joint 
    # num_frames : number of frames to retrieve showing ROM

    # Get ROM
    rom = getJointROM(data,joint_ind)

    # Get ideal list of linearly spaced angles
    frame_angles_ideal = np.linspace(rom["min"],rom["max"],num=num_frames)

    # Get list of angles closest to ideal and their frame indices
    frame_angles_inds = np.argmin(np.abs(np.subtract(frame_angles_ideal.reshape(len(frame_angles_ideal),1),data["angles"][joint_ind])),axis=1)
    frame_angles = data["angles"][joint_ind][frame_angles_inds]

    # Get list of images
    image_list =  ['%012d_rendered.png' % x for x in frame_angles_inds]

    return {'frame_angles_ideal':frame_angles,'angles_frames':angles_frames,'frame_angles_inds':frame_angles_inds,'image_list':image_list}
