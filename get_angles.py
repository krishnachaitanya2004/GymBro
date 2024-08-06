import numpy as np

def cosine_angle(v1, v2):
    numer = np.dot(v1, v2)
    denom = np.linalg.norm(v1) * np.linalg.norm(v2)
    if denom == 0:
        if np.array_equal(v1, v2):
            return 0.0
        else:
            return 180.0
    degrees = np.degrees(np.arccos(numer / denom))
    return degrees

def calulate_angle(point1,point2,point3):
    v1 = point1[:2] - point2[:2]
    v2 = point3[:2] - point2[:2]
    return cosine_angle(v1, v2)

def get_angles(keypoints):
    nose = keypoints[0]
    left_shoulder = keypoints[5]
    right_shoulder = keypoints[6]
    left_elbow = keypoints[7]
    right_elbow = keypoints[8]
    left_wrist = keypoints[9]
    right_wrist = keypoints[10]
    left_hip = keypoints[11]
    right_hip = keypoints[12]
    left_knee = keypoints[13]
    right_knee = keypoints[14]
    left_ankle = keypoints[15]
    right_ankle = keypoints[16]
    neck = (left_shoulder + right_shoulder) / 2

    n_n_rs = calulate_angle(nose, neck, right_elbow)
    n_n_ls = calulate_angle(nose, neck, left_elbow)
    n_rs_re = calulate_angle( neck,right_shoulder,right_elbow)
    n_ls_le = calulate_angle( neck,left_shoulder,left_elbow)
    rs_re_rw = calulate_angle(right_shoulder,right_elbow,right_wrist)
    ls_le_lw = calulate_angle(left_shoulder,left_elbow,left_wrist)
    n_rh_rk = calulate_angle(neck,right_hip,right_knee)
    n_lh_lk = calulate_angle(neck,left_hip,left_knee)
    rh_rk_ra = calulate_angle(right_hip,right_knee,right_ankle)
    lh_lk_la = calulate_angle(left_hip,left_knee,left_ankle)

    angles = {
        "Nose-Neck-Right Shoulder": n_n_rs,
        "Nose-Neck-Left Shoulder": n_n_ls,
        "Neck-Right Shoulder-Right Elbow": n_rs_re,
        "Neck-Left Shoulder-Left Elbow": n_ls_le,
        "Right Shoulder-Right Elbow-Right Wrist": rs_re_rw,
        "Left Shoulder-Left Elbow-Left Wrist": ls_le_lw,
        "Neck-Right Hip-Right Knee": n_rh_rk,
        "Neck-Left Hip-Left Knee": n_lh_lk,
        "Right Hip-Right Knee-Right Ankle": rh_rk_ra,
        "Left Hip-Left Knee-Left Ankle": lh_lk_la
    }

    return angles




