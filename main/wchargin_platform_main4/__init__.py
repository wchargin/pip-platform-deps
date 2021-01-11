__version__ = "0.1.0a0"


def get():
    try:
        import wchargin_platform_dep4
    except ImportError:
        return "universal"
    else:
        return wchargin_platform_dep4.BUILT_FOR


if __name__ == "__main__":
    print(get())
