import pkg_resources

path_to_test_file = pkg_resources.resource_filename(__name__, 'privateprefs/data/prefs.txt')

if __name__ == "__main__":
    # path workaround, but works for ci
    path_without_ci_dic = path_to_test_file.replace("privateprefs\\ci\\", "privateprefs\\")
    with open(path_without_ci_dic, "w") as file:
        file.write("")
