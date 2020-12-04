import sys


def print_python_version():
    # This print statement uses Python 3.8 syntax
    # tox will fail when trying to run this against Python 3.7
    print(f"{sys.version=}")

    # Comment out the above print statement and uncomment the following
    # print statement to make tox pass for both Python 3.7 and Python 3.8
    # print(f"sys.version={sys.version}")


print_python_version()
