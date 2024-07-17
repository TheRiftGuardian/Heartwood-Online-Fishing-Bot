import pyautogui
import time
import pyscreeze
import keyboard

# Current graphic settings:
# Zoom level = 1
# Fullscreen
# Res = 1920x1080
# Target FPS = 30

def check_if_bar_present(confidence_level):
    pyautogui.locateOnScreen("bar_transparent.png", confidence=confidence_level, grayscale=False)
    return True


def check_for_caught(confidence_level):
    try:
        if check_if_bar_present(confidence_level):
            return False
    except:
        return True


def click_fish():
    bar_not_found_counter = 0
    character_position = (952, 600)

    fishing_stages = 0

    fish_caught = 0

    loop_activated = True

    print("Script Running")
    tackle_photos = ["fish1.png", "fish2.png"]

    time.sleep(3)

    while True:
        if keyboard.is_pressed('q'):
            print("Loop paused")
            loop_activated = False
        elif keyboard.is_pressed('r'):
            print("Loop starting in 3...")
            bar_not_found_counter = 0
            fishing_stages = 0
            fish_caught = 0
            loop_activated = True
        if loop_activated:
            print(f"Total Fish Caught: {fish_caught}")
            if fishing_stages == 0:
                print("Casting rod ...")
                pyautogui.moveTo(character_position[0] + 250,
                                 character_position[1], duration=0.3)
                pyautogui.click()
                pyautogui.move(50, 50)
                fishing_stages = fishing_stages + 1
                stage_one_timer = time.time()



            elif fishing_stages == 1:
                if time.time() - stage_one_timer >= 30:
                    print("Stuck in stage 1 for 40 seconds. Resetting")
                    fishing_stages = 0
                    time.sleep(1)
                for image in tackle_photos:
                    try:
                        # Fish bite
                        pyautogui.locateOnScreen(
                            image, confidence=0.70, grayscale=False)
                        pyautogui.click()
                        fishing_stages = fishing_stages + 1
                        print("Fish bite!")

                        # Reeling in
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        pass
                    except pyscreeze.ImageNotFoundException:
                        pass
            elif fishing_stages == 2:
                print("Checking now")
                try:
                    if check_if_bar_present(0.25):
                        print("Bar found, reeling in...")
                        fishing_stages = fishing_stages + 1
                        stage_three_timer = time.time()
                except pyautogui.ImageNotFoundException:
                    print("No bar found. 1")
                    bar_not_found_counter = bar_not_found_counter + 1
                    time.sleep(1)
                    if bar_not_found_counter >= 5:
                        fishing_stages = fishing_stages - 1
                except pyscreeze.ImageNotFoundException:
                    print("No bar found. 2")
            elif fishing_stages == 3:
                pyautogui.mouseDown()
                time.sleep(10)
                if time.time() - stage_three_timer >= 30:
                    fish_caught = fish_caught - 1
                    pyautogui.press('a')
                    pyautogui.press('a')
                    pyautogui.press('d')
                    pyautogui.press('d')
                    fishing_stages = 0
                    time.sleep(1)
                try:
                    if check_for_caught(0.35):
                        print("Fish was caught!")
                        pyautogui.mouseUp()
                        fish_caught = fish_caught + 1
                        fishing_stages = 0
                except pyautogui.ImageNotFoundException:
                    pass
                except pyscreeze.ImageNotFoundException:
                    pass
            else:
                pass
    exit()


click_fish()
