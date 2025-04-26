README - 7 Days to Die Auto-Backup Script
=========================================

Overview
--------
This script automatically launches 7 Days to Die via the Steam client, waits for you to exit the game, and then backs up your world save folder to a timestamped directory. It keeps only the most recent backups, rotating out older ones to save space.

Prerequisites
-------------
- **Windows OS** with Python 3 installed and accessible from the command line.
- **Steam client** installed and logged in.
- Basic familiarity with running scripts from a Command Prompt or PowerShell.

Files
-----
- **`backup_7d2d.py`**: The Python script that handles launching the game, monitoring its process, backing up saves, and pruning old backups.

Configuration
-------------
1. Open `backup_7d2d.py` in a text editor.
2. Locate the configuration section near the top of the file:

   ```python
   STEAM_EXE   = r"C:\Program Files (x86)\Steam\steam.exe"
   STEAM_APPID = "251570"
   SAVE_FOLDER = r"C:\Path\To\Your\7DaysToDie\Saves\WorldName\SaveName"
   BACKUP_ROOT = r"C:\Path\To\BackupFolder"
   ```

3. Update each variable to match your setup:
   - **`STEAM_EXE`**: Full path to `steam.exe` on your system.
   - **`STEAM_APPID`**: Steam AppID for 7 Days to Die (`251570`).
   - **`SAVE_FOLDER`**: Path to the specific save directory you want backed up.
   - **`BACKUP_ROOT`**: Directory where backup folders will be created.

4. Save and close the file.

Usage
-----
1. Open a **Command Prompt** or **PowerShell** window.
2. Navigate to the directory containing `backup_7d2d.py`:

   ```bat
   cd C:\Path\To\Script
   ```

3. Run the script with:

   ```bat
   python backup_7d2d.py
   ```

4. The script will perform the following steps:
   - Launch 7 Days to Die via Steam.
   - Detect when the game process starts and when it exits.
   - Copy your save folder into a new subfolder named `SaveBackup-YYYYMMDD-HHMMSS` inside `BACKUP_ROOT`.
   - Delete older backup folders beyond the configured retention count (defaults to 5).

Troubleshooting
---------------
- **Script does not start**: Ensure Python 3 is installed and added to your system PATH.
- **Game hangs on loading**: Make sure the Steam client is running and logged in before launching the script.
- **No backups appear**: Verify that the paths in the configuration exactly match your Steam and save locations.
- **Permission errors**: Run the script from a prompt with appropriate permissions or choose backup paths you have write access to.

Customization
-------------
- **Retention Count**: To keep more or fewer backups, modify the integer value in the pruning loop near the end of `backup_7d2d.py`.
- **Polling Intervals**: Adjust the `time.sleep()` durations to change how frequently the script checks for the game process.

Community Sharing
-----------------
Feel free to fork or adapt this script for your own 7 Days to Die setup. Contributions, suggestions, and improvements are welcome—please share back any enhancements in the community forum or repository.

License
-------
This script is released under the MIT License. See `LICENSE` for full details.

