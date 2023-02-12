# Importing libraries
import random
import copy

# Create a grid
def create_grid(x, y, box_size_x, box_size_y):

    start_x = int((x / 2 - x) + (box_size_x / 2))
    start_y = int((y / 2 - y) + (box_size_y / 2))
    x_limit = int(x / 2)
    y_limit = int(y / 2)

    grid = []

    while start_x < x_limit:
        while start_y < y_limit:
            grid.append([start_x, start_y])
            start_y += box_size_y

        start_y = int((y / 2 - y) + (box_size_y / 2))
        start_x += box_size_x

    return grid


# Call the function
grid = create_grid(1900, 1000, 190, 100)


# Create a color palette
def create_color_palette(*colors):
    color_palette = []
    for color in colors:
        color_palette.append(color)

    return color_palette


# Call the function
color_palette = create_color_palette(
    "green",
    "red",
    "blue",
    "saddlebrown",
    "#ff94c0",
    "cyan",
    "purple",
    "orange",
    "yellow",
)


# Randomize the grid locations function
def randomize_location(loc, val_x, val_y):
    loc[0] = random.randint(loc[0] - val_x, loc[0] + val_x)
    loc[1] = random.randint(loc[1] - val_y, loc[1] + val_y)
    return [loc[0], loc[1]]


# Define the number of training trials
num_of_training = 4

# Define the number of the experiment trials
num_of_trials = 24

# Create trials
trial_order = []
training_order = []

# Regular trials
for trial in range(num_of_trials):
    if trial >= num_of_trials / 2:
        trial_order.append(1)
    else:
        trial_order.append(0)

# Training trials
for trial in range(num_of_training):
    if trial >= num_of_training / 2:
        training_order.append(1)
    else:
        training_order.append(0)

# Shuffle the trials order
random.shuffle(trial_order)
random.shuffle(training_order)

shapeOrientation = 0
shapeName = ""

if expInfo["shape"] == "square":
    shapeOrientation = 0
    shapeName = "Square"
else:
    shapeOrientation = 45
    shapeName = "Diamond"


# Order:           1          0          1          0             0           0              1          1
shape1_shape = [
    "square",
    "square",
    "circle",
    "triangle",
    "triangle",
    "square",
    "square",
    "triangle",
]
shape2_shape = [
    "square",
    "triangle",
    "circle",
    "circle",
    "circle",
    "triangle",
    "square",
    "triangle",
]
shape1_color = [
    "red",
    "red",
    "blue",
    "saddlebrown",
    "cyan",
    "purple",
    "orange",
    "yellow",
]
shape2_color = [
    "red",
    "purple",
    "blue",
    "green",
    "cyan",
    "saddlebrown",
    "orange",
    "yellow",
]


answers = []
trainingCorrectAnswers = 0
successRate = 0

thisKey = ""

keys = event.getKeys()

if len(keys) > 0:
    for thisKey in keys:
        current_key = ord(thisKey[0])

        # Skip to next routine
        if current_key == 112 or current_key == 113:
            continueRoutine = False


# P - 112 | Identical
if current_key == 112:
    answers.append(112)

# Q - 113 | Non-Identical
if current_key == 113:
    answers.append(113)


currentStep = training_loop.thisN

circle_1.color = triangle_1.color = square_1.color = shape1_color[currentStep]
circle_2.color = triangle_2.color = square_2.color = shape2_color[currentStep]

currentShape1 = shape1_shape[currentStep]
currentShape2 = shape2_shape[currentStep]


for trial in range(8):

    # Identical
    if (
        shape1_shape[trial] == shape2_shape[trial]
        and shape1_color[trial] == shape1_color[trial]
    ):
        # Correct Answer
        if answers[trial] == 112:
            trainingCorrectAnswers += 1

    # Non-identical
    else:
        # Correct Answer
        if answers[trial] == 113:
            trainingCorrectAnswers += 1


successRate = trainingCorrectAnswers / 8 * 100
calculate_text.text = str(successRate) + "\n" + "אנא פנה\י לנסיינית."

# If the participant successfully answered at least 75% of the answers
if successRate >= 75:
    repeat_training.finished = True
    continueRoutine = False


keys = event.getKeys()

if len(keys) > 0:
    for thisKey in keys:
        current_key = ord(thisKey[0])

        # Repeat the initial training - 'r'
        if current_key == 114:
            continueRoutine = False


# Save success rate
thisExp.addData("initialTraining_sucessRate", successRate)
thisExp.addData("initialTraining_loopNum", repeat_training.thisN)


thisExp.nextEntry()


# Randomize the grid locations
current_grid = copy.deepcopy(grid)
random.shuffle(current_grid)

# Add randomization for each block
# Set the block location
for idx, block in enumerate(
    [
        [img1_b1_t, img2_b1_t],
        [img1_b2_t, img2_b2_t],
        [img1_b3_t, img2_b3_t],
        [img1_b4_t, img2_b4_t],
    ]
):
    current_location = randomize_location(current_grid[idx], 38, 20)
    block[0].pos = block[1].pos = current_location


import random

# Randomize the color palette
random.shuffle(color_palette)

# Pick 5 Random colors
random_colors = []
random_colors += random.sample(color_palette, 5)

# Assign the first 5 colors to the blocks
for idx, block in enumerate(
    [
        [img1_b1_t, img2_b1_t],
        [img1_b2_t, img2_b2_t],
        [img1_b3_t, img2_b3_t],
        img1_b4_t,
        img2_b4_t,
    ]
):
    current_color = random_colors[idx]

    if type(block) == list:
        block[0].color = block[1].color = current_color
    else:
        if training_order[show_images_t.thisN] == 1:
            img1_b4_t.color = img2_b4_t.color = current_color
            break
        else:
            block.color = current_color


current_key = 0

keys = event.getKeys()

if len(keys) > 0:
    for thisKey in keys:
        current_key = ord(thisKey[0])

        if current_key == 112 or current_key == 113:
            redisplay_image_loop_t.finished = True
            continueRoutine = False

#        elif current_key == 115:
#            redisplay_image_loop_t.finished = False
#            continueRoutine = False
#


# List of locations
locations = []

# Randomize the grid locations
current_grid = copy.deepcopy(grid)
random.shuffle(current_grid)

# Add randomization for each block
# Set the block location
for idx, block in enumerate(
    [[img1_b1, img2_b1], [img1_b2, img2_b2], [img1_b3, img2_b3], [img1_b4, img2_b4]]
):
    current_location = randomize_location(current_grid[idx], 38, 20)
    block[0].pos = block[1].pos = current_location
    locations.append(current_location)


import random

# Randomize the color palette
random.shuffle(color_palette)

# Pick 5 Random colors
random_colors = []
random_colors += random.sample(color_palette, 5)

# Assign the first 5 colors to the blocks
for idx, block in enumerate(
    [[img1_b1, img2_b1], [img1_b2, img2_b2], [img1_b3, img2_b3], img1_b4, img2_b4]
):
    current_color = random_colors[idx]

    if type(block) == list:
        block[0].color = block[1].color = current_color
    else:
        if trial_order[show_images.thisN] == 1:
            img1_b4.color = img2_b4.color = current_color
            break
        else:
            block.color = current_color


if trial_order[show_images.thisN] == 1:
    img1_colors = img2_colors = random_colors[0:4]
else:
    img1_colors = random_colors[0:4]
    img2_colors = random_colors[0:3]
    img2_colors.append(random_colors[4])


# Records the `fullRoutineRT` start

if redisplay_image_loop.thisN == 0:
    fullRoutineStart = core.getTime()


answerVariant = ""
pressedKey = ""
numOfCorrectAnswers = 0
numOfWrongAnswers = 0
totalNumOfLoops = 0

current_key = 0

# Records the `singleRoutineRT` start
singleRoutineStart = core.getTime()


keys = event.getKeys()

if len(keys) > 0:
    for thisKey in keys:
        current_key = ord(thisKey[0])

        if current_key == 112 or current_key == 113:
            redisplay_image_loop.finished = True
            continueRoutine = False

#        elif current_key == 115:
#            redisplay_image_loop.finished = False
#            continueRoutine = False


# Records the `singleRoutineRT` and `fullRoutineRT` end
routineEnd = core.getTime()


# imagesVariation:
# 1 - '==' Identical Images
# 0 - '!=' Non-Identical Images
redisplay_image_loop.addData("imagesVariation", trial_order[show_images.thisN])

if trial_order[show_images.thisN] == 0:
    redisplay_image_loop.addData("imagesVariationSign", "!=")
elif trial_order[show_images.thisN] == 1:
    redisplay_image_loop.addData("imagesVariationSign", "==")


# Key 112 = p
if current_key == 112:
    pressedKey = "p"
    if trial_order[show_images.thisN] == 1:
        redisplay_image_loop.addData("correctAnswerBoolean", True)
        redisplay_image_loop.addData("correctAnswer", 1)
        numOfCorrectAnswers += 1
    else:
        redisplay_image_loop.addData("correctAnswerBoolean", False)
        redisplay_image_loop.addData("correctAnswer", 0)
        numOfWrongAnswers += 1

    redisplay_image_loop.addData("fullRoutineRT", routineEnd - fullRoutineStart)
    redisplay_image_loop.addData("locations", locations)
    redisplay_image_loop.addData("img1Colors", img1_colors)
    redisplay_image_loop.addData("img2Colors", img2_colors)


# Key 113 = q
elif current_key == 113:
    pressedKey = "q"
    if trial_order[show_images.thisN] == 0:
        redisplay_image_loop.addData("correctAnswerBoolean", True)
        redisplay_image_loop.addData("correctAnswer", 1)
        numOfCorrectAnswers += 1
    else:
        redisplay_image_loop.addData("correctAnswerBoolean", False)
        redisplay_image_loop.addData("correctAnswer", 0)
        numOfWrongAnswers += 1

    redisplay_image_loop.addData("fullRoutineRT", routineEnd - fullRoutineStart)
    redisplay_image_loop.addData("locations", locations)
    redisplay_image_loop.addData("img1Colors", img1_colors)
    redisplay_image_loop.addData("img2Colors", img2_colors)

# Key 115 = 'space'
elif current_key == 115:
    pressedKey = "space"
    totalNumOfLoops += 1


# Saving data
redisplay_image_loop.addData("routineNumber", show_images.thisN)
redisplay_image_loop.addData("pressedKey", pressedKey)
redisplay_image_loop.addData("numOfCorrectAnswers", numOfCorrectAnswers)
redisplay_image_loop.addData("numOfWrongAnswers", numOfWrongAnswers)
redisplay_image_loop.addData("numOfLoops", redisplay_image_loop.thisN)
redisplay_image_loop.addData("totalNumOfLoops", totalNumOfLoops)
redisplay_image_loop.addData("singleRoutineRT", routineEnd - singleRoutineStart)


# Data Overview

thisExp.addData("numOfCorrectAnswers", numOfCorrectAnswers)
thisExp.addData("numOfWrongAnswers", numOfWrongAnswers)
thisExp.addData("totalNumOfLoops", totalNumOfLoops)
thisExp.addData("totalNumOfTrials", num_of_trials)
thisExp.addData("trialsOrder", trial_order)

genderBoolean = 0
if expInfo["gender"] == "woman":
    genderBoolean = 0
elif expInfo["gender"] == "man":
    genderBoolean = 1
else:
    genderBoolean = 2

thisExp.addData("genderBoolean", genderBoolean)
thisExp.addData("shapeBoolean", 0 if expInfo["shape"] == "square" else 1)
thisExp.addData(
    "handednessBoolean", 0 if expInfo["handedness"] == "right-handed" else 1
)

thisExp.nextEntry()
