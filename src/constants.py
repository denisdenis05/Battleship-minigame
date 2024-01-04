# ---------------------------------------
# INITIALIZATIONS
# ---------------------------------------

HIT_TILE = 1
EMPTY_TILE = -1
DIMENSION_OF_BOARD = 10
STARTING_NUMBER_OF_HITS = 0
NUMBER_OF_SHIPS = 5

# ---------------------------------------
# INDEXES
# ---------------------------------------


INDEX_OF_COLUMN_COORDINATES = 0
INDEX_OF_LINE_COORDINATES = 1

INDEX_OF_X_AXIS_VALUE = 0
INDEX_OF_Y_AXIS_VALUE = 1

INDEX_OF_BUTTON_RECTANGLE = 0
INDEX_OF_BUTTON_SURFACE = 1
INDEX_OF_TEXT_SURFACE = 2


# ---------------------------------------
# LOCATIONS
# ---------------------------------------

LOCATION_OF_BACKGROUND_IMAGE = "src/images/background_image.jpg"
LOCATION_OF_CHECKMARK_ICON = "src/images/checkmark_icon.png"
LOCATION_OF_POINTER_ICON = "src/images/pointer_icon.png"


# ---------------------------------------
# SHIPS
# ---------------------------------------

LENGTH_OF_SHIPS = {
    0: 2,
    1: 3,
    2: 3,
    3: 4,
    4: 5
}

NAME_OF_SHIPS = {
    0: "Patrol Boat",
    1: "Submarine",
    2: "Destroyer",
    3: "Battleship",
    4: "Carrier"
}

ID_OF_PATROL_BOAT = 0
ID_OF_SUBMARINE = 1
ID_OF_DESTROYER = 2
ID_OF_BATTLESHIP = 3
ID_OF_CARRIER = 4

SHIP_IS_HORIZONTAL = 0
SHIP_IS_VERTICAL = 1


THIS_SHIP_WAS_NOT_ADDED = 0
THIS_SHIP_WAS_ADDED = 1

# ---------------------------------------
# COORDINATES, OFFSETS AND SIZES
# ---------------------------------------

NUMBER_OF_SCREEN_SECTIONS = 2

TILE_DIMENSION_AS_PERCENTAGE_OF_SCREEN = 0.05
SPACING_BETWEEN_TILES = 5
GRID_OFFSET_X_AXIS = 15
GRID_OFFSET_Y_AXIS = 10

BOARD_BUILDER_TITLE_OFFSET = 50
BOARD_BUILDER_TITLE_SIZE = 30

MEDIUM_BUTTON_DIMENSIONS = (200, 50)

COORDINATES_OF_STARTING_SCREEN = (0, 0)


NUMBER_OF_BUTTONS_PER_ROW = 2
buttonsIconPositions = [(30, 200),
                        (30, 300),
                        (30, 400),
                        (30, 500),
                        (30, 600)]

firstRowFirstButtonPosition = (200, 100)
firstRowSecondButtonPosition = (200, 300)
secondRowFirstButtonPosition = (300, 100)
secondRowSecondButtonPosition = (300, 300)
thirdRowFirstButtonPosition = (400, 100)
thirdRowSecondButtonPosition = (400, 300)
fourthRowFirstButtonPosition = (500, 100)
fourthRowSecondButtonPosition = (500, 300)
fifthRowFirstButtonPosition = (600, 100)
fifthRowSecondButtonPosition = (600, 300)

# ---------------------------------------
# COLORS
# ---------------------------------------

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_GREY = (27, 27, 27)
COLOR_LIGHT_BLUE = (0, 0, 128)
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (255, 255, 0)

COLOR_OF_TILES_FOR_SHIP = {
    0: COLOR_BLACK,
    1: COLOR_RED,
    2: COLOR_WHITE,
    3: COLOR_GREY,
    4: COLOR_YELLOW
}

# ---------------------------------------
# TEXTS
# ---------------------------------------


BUILD_BOARD_CHOOSE_SHIPS_TEXT = "Choose each type of ship and position it on board"


# ---------------------------------------
# MISCELLANEOUS
# ---------------------------------------

VALUE_TO_ADD_SO_LAST_ELEMENT_IS_CONSIDERED = 1

