import os
import argparse

def generate_new_labels(current_dir, output_dir):

    directory = os.fsencode(current_dir)

    # get local class names
    with open(current_dir + "/classes.txt") as f:
        current_classes = f.readlines()
    f.close()

    # get desired class names
    with open(current_dir + "/classes_desired.txt") as f:
        desired_classes = f.readlines()
    f.close()

    # create mappping local class names to desired
    mapping = {}
    for current in range(len(current_classes)-1):
        found_mapping = False
        for desired in range(len(desired_classes)):
            if current_classes[current] == desired_classes[desired]:
                mapping[current] = desired
                found_mapping = True
                print(f"{current} corresponds to {desired}")
        if not found_mapping:
            raise ValueError(f"No correspondence found for {current_classes[current]}")

    # create output_dir if it does not exist
    isExist = os.path.exists(output_dir)
    if not isExist:
        os.makedirs(output_dir)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename != "classes.txt" and filename != "classes_desired.txt":
            if not filename.endswith('.txt'):
                raise ValueError(f"File {filename} does not have expected extension .txt")
            with open(current_dir + "/" + filename) as f:
                current_file = f.readlines()
            f.close()

            f = open(output_dir + "/" + filename, "w+")
            for line in current_file:
                line = list(line)
                line_class = int(line[0])
                line[0] = str(mapping[line_class])
                f.write(''.join(line))
            f.close()
        else:
            continue

    # add desired classes as current classes in output_dir
    f = open(output_dir + "/classes.txt", "w+")
    for desired_class in desired_classes:
        f.write(desired_class)
    f.close()
    print("Conversion done.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Get paths to directories.')
    parser.add_argument("--current_dir", help="enter directory including current labels")
    parser.add_argument("--output_dir", help="enter directory for new labels")

    params = parser.parse_args()

    generate_new_labels(params.current_dir, params.output_dir)