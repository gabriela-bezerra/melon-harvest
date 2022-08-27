############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings = pairing

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(
        "musk",
        "1998",
        "green",
        True,
        True,
        "Muskmelon"

    )
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    casaba = MelonType(
        "cas",
        "2003",
        "orange",
        True,
        False,
        "Casaba"
    )
    casaba.add_pairing("strawberries, mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType(
        "cren",
        "1996",
        "green",
        True,
        False,
        "Crenshaw"

    )
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType(
        "yw",
        "2013",
        "yellow",
        True,
        True,
        "Yellow Watermelon"

    )

    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


melon_list = make_melon_types()


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with \n - {melon.pairings}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # create empty dictionary
    # set keys to "reporting codes"
    # set value as melontype instance

    # { yw: melon type with code yw , ... }
    melon_code = {}

    for melon_type in melon_types:
        melon_code[melon_type.code] = melon_type

    return melon_code


# print(make_melon_types)
# print(make_melon_type_lookup(melon_list))
# print_pairing_info(melon_list)


############
# Part 2   #
############


class Melon():
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def __init__(self, type, shape, color, field, harvested_by):

        self.type = type,
        self.shape = shape,
        self.color = color,
        self.field = field,
        self.harvested_by = harvested_by

    def is_sellable(self):
        if self.shape and self.color > 5 and self.field != 3:
            return "CAN BE SOLD"
        else:
            return "NOT SELLABLE"

    # def __repr__(self):
    #     return f""
    #     pass


def make_melons():
    """Returns a list of Melon objects."""

    # Fill in the rest

    melons_harvested = []

    # melon_type = # look up which melon type has the code
    # use melon_type as an attribute of Melon
    melon_type_lookup = make_melon_type_lookup(melon_list)

    melon_1 = Melon(
        melon_type_lookup["yw"],
        8,
        7,
        2,
        "Sheila"
    )
    melons_harvested.append(melon_1)

    melon_2 = Melon(
        melon_type_lookup["yw"],
        2,
        3,
        4,
        "Sheila"
    )
    melons_harvested.append(melon_2)

    melon_3 = Melon(
        melon_type_lookup["yw"],
        9,
        8,
        3,
        "Sheila"
    )
    melons_harvested.append(melon_3)

    melon_4 = Melon(
        melon_type_lookup["cas"],
        10,
        6,
        35,
        "Sheila"

    )
    melons_harvested.append(melon_4)

    melon_5 = Melon(
        melon_type_lookup["cren"],
        8,
        9,
        34,
        "Michael"
    )
    melons_harvested.append(melon_5)

    melon_6 = Melon(
        melon_type_lookup["cren"],
        8,
        2,
        35,
        "Michael"
    )
    melons_harvested.append(melon_6)

    melon_7 = Melon(
        melon_type_lookup["cren"],
        2,
        3,
        4,
        "Michael"
    )
    melons_harvested.append(melon_7)

    melon_8 = Melon(
        melon_type_lookup["musk"],
        6,
        7,
        4,
        "Michael"
    )
    melons_harvested.append(melon_8)

    melon_9 = Melon(
        melon_type_lookup["yw"],
        7,
        10,
        3,
        "Sheila"
    )
    melons_harvested.append(melon_9)

    return melons_harvested


# make_melons()


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest

    melons = make_melons()

    for melon in melons:
        print(
            f"Harvested by {melon.harvested_by} from Field {melon.field} {melon.is_sellable()}")


get_sellability_report(melon_list)
