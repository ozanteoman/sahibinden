class NumberOfRoomsChoices(object):
    ONE_PLUS_ZERO = 0
    ONE_PLUS_ONE = 1
    TWO_PLUS_ZERO = 2
    TWO_PLUS_ONE = 3
    TWO_PLUS_TWO = 4
    THREE_PLUS_ONE = 5
    THREE_PLUS_TWO = 6
    FOUR_PLUS_ONE = 7
    FOUR_PLUS_TWO = 8
    FIVE_PLUS_ONE = 9
    FIVE_PLUS_TWO = 10

    CHOICES = (
        (ONE_PLUS_ZERO, "1+0"),
        (ONE_PLUS_ONE, "1+1"),
        (TWO_PLUS_ZERO, "2+0"),
        (TWO_PLUS_ONE, "2+1"),
        (TWO_PLUS_TWO, "2+2"),
        (THREE_PLUS_ONE, "3+1"),
        (THREE_PLUS_TWO, "3+2"),
        (FOUR_PLUS_ONE, "4+1"),
        (FOUR_PLUS_TWO, "4+2"),
        (FIVE_PLUS_ONE, "5+1"),
        (FIVE_PLUS_TWO, "5+2"),
    )


class NumberOfBuildingAgeChoices(object):
    ONE_AGE = 0
    TWO_AGE = 1
    THREE_AGE = 2
    FOUR_AGE = 3
    FIVE_AND_TEN = 4
    ELEVEN_AND_FIFTEEN = 5
    SIXTEEN_AND_TWENTY = 6

    CHOICES = (
        (ONE_AGE, "1"),
        (TWO_AGE, "2"),
        (THREE_AGE, "3"),
        (FOUR_AGE, "4"),
        (FIVE_AND_TEN, "5-10 Arası"),
        (ELEVEN_AND_FIFTEEN, "11-15 Arası"),
        (SIXTEEN_AND_TWENTY, "16-20 Arası"),
    )


class NumberOfFloorChoices(object):
    CELLAR = 0
    BASEMENT = 1
    ONE = 2
    TWO = 3
    THREE = 4
    FOUR = 5
    FIVE = 6
    SIX = 7
    SEVEN = 8
    EIGHT = 9
    NINE = 10
    TEN = 11
    ELEVEN = 12
    TWELVE = 13
    THIRTEEN = 14
    FOURTEEN = 15
    FIFTEEN = 16

    FLOOR_CHOICES = (
        (CELLAR, "Bodrum Kat"),
        (BASEMENT, "Zemin Kat"),
        (ONE, "1"),
        (TWO, "2"),
        (THREE, "3"),
        (FOUR, "4"),
        (FIVE, "5"),
        (SIX, "6"),
        (SEVEN, "7"),
        (EIGHT, "8"),
        (NINE, "9"),
        (TEN, "10"),
        (ELEVEN, "11"),
        (TWELVE, "12"),
        (THIRTEEN, "13"),
        (FOURTEEN, "14"),
        (FIFTEEN, "15")
    )

    FLOORS_CHOICES = (
        (ONE, "1"),
        (TWO, "2"),
        (THREE, "3"),
        (FOUR, "4"),
        (FIVE, "5"),
        (SIX, "6"),
        (SEVEN, "7"),
        (EIGHT, "8"),
        (NINE, "9"),
        (TEN, "10"),
        (ELEVEN, "11"),
        (TWELVE, "12"),
        (THIRTEEN, "13"),
        (FOURTEEN, "14"),
        (FIFTEEN, "15")
    )


class HeatingChoices(object):
    NONE = 0
    STOVE = 1
    NATURAL_GAS_STOVE = 2
    ROOM_HEATER = 3
    CENTRAL_HEATING = 4
    NATURAL_GAS = 5
    CLIMATE = 6
    FIREPLACE = 7

    CHOICES = (
        (NONE, "Yok"),
        (STOVE, "Soba"),
        (NATURAL_GAS_STOVE, "Doğalgaz Sobası"),
        (ROOM_HEATER, "Kat Kaloriferi"),
        (CENTRAL_HEATING, "Merkezi Isıtıcı"),
        (NATURAL_GAS, "Doğalgaz"),
        (CLIMATE, "Klima"),
        (FIREPLACE, "Şömine"),
    )


class NumberOfBathroomsChoices(object):
    NONE = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6

    CHOICES = (
        (NONE, "Yok"),
        (ONE, "1"),
        (TWO, "2"),
        (THREE, "3"),
        (FOUR, "4"),
        (FIVE, "5"),
        (SIX, "6"),
    )


class UsingStatusChoices(object):
    EMPTY = 0
    HIRED = 1
    LANDHOLDER = 2

    CHOICES = (
        (EMPTY, "Boş"),
        (HIRED, "Kiracılı"),
        (LANDHOLDER, "Mülk Sahibi"),
    )


class AdvertiseVisibilityChoices(object):
    PUBLIC = 0
    SELF = 1

    CHOICES = (
        (PUBLIC, "Herkes"),
        (SELF, "Sadece Ben"),
    )


class AdvertiseStatusChocies(object):
    ACTIVE = 0
    DELETED = 1

    CHOICES = (
        (ACTIVE, "Aktif"),
        (DELETED, "Silinmiş"),
    )
