# Dofus bot AH

## Introduction
This document provides instructions on how to use the Auction House (AH) Bot. The AH Bot automates selling and undercutting prices within the Auction House for you. Please follow the setup and instructions carefully to ensure the bot operates correctly.

**Launch the Bot:**
   - For users :
      - launch the Dofus-bot-AH/main/Dofus-bot-AH.exe file and click on Start 
   - For devs:
      - Open your terminal or command prompt.
      - Navigate to the directory where the AH Bot files are located.
      - Run the command: `python3 main.py`
        
      Alternatively, you can compile the .exe:
      ```bash
      pyinstaller.exe --add-data "./icon.png;." --icon=icon.png -w .\main.py
      ```

## Instructions

1. **Open the Auction House (AH):** Before starting the bot, make sure you have the Auction House opened on Dofus.

2. **Navigate to the Sells Tab:** Within the Auction House, navigate to the 'Sells' tab where your items for sale are listed.

3. **Ensure Prices are Visible:** Confirm that the item prices are fully visible on the screen once you select an item in your bags. The bot relies on screen reading to function correctly, so it's crucial that all relevant information is displayed and unobstructed.

4. **Ensure that the items are sorted correctly:**
   - FOR SELLING: the items in your bag should be "sorted by name"
   - FOR REPRICING: the items in the AH window should be sorted by "time left" in increasing order (low time should be at the top)

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

![Alt text](https://cdn.discordapp.com/attachments/501002294687694850/1192052713974939678/image.png?ex=65a7ac9a&is=6595379a&hm=40b1a46a44ee3708a1ee1a6fd25d789342ab804fe429462510d69c057f0825de&)
