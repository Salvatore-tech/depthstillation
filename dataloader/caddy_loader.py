import os

IMG_EXTENSIONS= [
    '.jpg', '.JPG', '.jpeg', '.JPEG',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP'
]

def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

# biograd-A
#   true_negatives
#       raw
#       depths
#   true_positives
#       raw
#       depths
def caddy_loader(filepath):
    raw_path_A_negatives = os.path.join(filepath, 'biograd-A/true_negatives/raw')
    depth_path_A_negatives = os.path.join(filepath, 'biograd-A/true_negatives/depths')

    # raw_path_A_positives = os.path.join(filepath, 'biograd-A/true_positives/raw')
    # depth_path_A_positives = os.path.join(filepath, 'biograd-A/true_positives/depths')

    raw_negatives_A = []
    depths_negatives_A = []

    files = [file for file in os.listdir(raw_path_A_negatives)]
    for file in files:
        raw_negatives_A.append(os.path.join(filepath, raw_path_A_negatives, file))

    files = [file for file in os.listdir(depth_path_A_negatives)]
    for file in files:
        depths_negatives_A.append(os.path.join(filepath, depth_path_A_negatives, file))

    return raw_negatives_A, depths_negatives_A
