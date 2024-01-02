# Dofus bot AH

## Introduction
This document provides instructions on how to use the Auction House (AH) Bot. The AH Bot automates selling within the Auction House for you. Please follow the setup and instructions carefully to ensure the bot operates correctly.

**Launch the Bot:**
   - For users :
      - launch the Dofus-bot-AH/main/Dofus-bot-AH.exe file in and click on Start 
   - For devs:
      - Open your terminal or command prompt.
      - Navigate to the directory where the AH Bot files are located.
      - Run the command: `python3 main.py`
        
      Alternatively, you can compile the .exe:
      ```bash
      pyinstaller.exe --add-data "./icon.png;." --icon=icon.png -w .\main.py
      ```

## Instructions

1. **Open the Auction House (AH):** Before launching the bot, make sure you have the Auction House opened on Dofus.

2. **Navigate to the Sells Tab:** Within the Auction House, navigate to the 'Sells' tab where your items for sale are listed.

3. **Ensure Prices are Visible:** Confirm that the item prices are fully visible on the screen once you select an item in your bags. The bot relies on screen reading to function correctly, so it's crucial that all relevant information is displayed and unobstructed.

6. **Running the Bot:** Once the bot is running, it will automate tasks within the 'Sells' tab of the Auction House. Ensure not to use the mouse or keyboard as it may interfere with the bot's operations.

## Important Notes

- **Interruption:** If you need to stop the bot for any reason, you can do so by pressing the designated stop key (e.g., 'F8') and keeping it pressed until the bot stop.
- **Safety:** Make sure you understand the actions performed by the bot. Use the AH Bot responsibly and at your own risk (I recommand selling selling big items by hands and then selling junk with it).
- **Updates:** Keep the bot updated with the latest version for the best performance and new features.

## Prerequisites (FOR DEVS)
Before running the AH Bot, ensure you have the following:
- Python 3 installed on your system.

#### Necessary Dependencies (FOR DEVS):

- numpy
- OpenCV-Python (`cv2`)
- Pillow (`PIL`)
- pytesseract
- pyautogui
- keyboard

You can install these packages using pip. Run the following command:

```bash
pip install numpy opencv-python Pillow pytesseract pyautogui keyboard
```
## Troubleshooting

- If the bot doesn't seem to be working correctly, ensure that the Auction House screen hasn't changed and that all prices and necessary buttons are completely visible.
- For devs, check that your Python environment is correctly set up with all necessary dependencies installed.
- For more help/questions and if you'd like to contribute to the AH Bot project, contact me on discord "ledraz".


Thank you for using AH Bot! I hope it enhances your Auction House experience by selling all those bworks underwear 🤙🏻🤙🏻🤙🏻

![Alt text](https://media.discordapp.net/attachments/1127705561975230598/1191341301203996724/image.png?ex=65a5160c&is=6592a10c&hm=704d1d11bb10d77b407aa91e2cceca0c35b28121003ab303682a954df5ab0d06&=&format=webp&quality=lossless)

