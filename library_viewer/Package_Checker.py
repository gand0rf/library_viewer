class Package_Checker:
    def __init__(self):
        None

    def pkge_check(self, package):
        self.package = package
        match self.package:
            case 'beautifulsoup4':
                return 'bs4'
            case _:
                return self.package


if __name__ == '__main__':
    """
    pk1 = Package_Checker("pip")
    pk2 = Package_Checker("beautifulsoup4")
    print(pk1.pkge_check())
    print(pk2.pkge_check())
    """
    None