#!/usr/bin/env python3
import os, subprocess, time, shutil, datetime

# ─── CONFIGURE THESE ────────────────────────────────────────────────
# Path to your Steam client executable:
STEAM_EXE   = r"C:\Program Files (x86)\Steam\steam.exe"

# 7 Days to Die’s Steam AppID (not your Steam user ID):
STEAM_APPID = "251570"

# Your specific 7DtD save folder:
SAVE_FOLDER = r"C:\Users\garre\AppData\Roaming\7DaysToDie\Saves\Fluffy Panda 1.0 Australia 10k\Panda 1"

# Where you’d like to keep your rolling backups (5 most recent):
BACKUP_ROOT = r"C:\Users\garre\7DTDM\Panda1 Rolling Saves"
# ────────────────────────────────────────────────────────────────────

def is_running(process_name):
    """Return True if a process with the given name is running."""
    tasks = subprocess.check_output("tasklist", shell=True).decode(errors="ignore")
    return process_name.lower() in tasks.lower()

def main():
    # Ensure backup folder exists
    os.makedirs(BACKUP_ROOT, exist_ok=True)

    # 1) Launch via Steam
    print("▶ Launching 7 Days to Die via Steam…")
    subprocess.Popen([STEAM_EXE, "-silent", "-applaunch", STEAM_APPID])

    # 2) Wait for the game process to appear
    print("⏳ Waiting for the game to start…")
    while not is_running("7DaysToDie.exe"):
        time.sleep(2)

    # 3) Wait for it to exit
    print("⏳ Game running—waiting for you to quit…")
    while is_running("7DaysToDie.exe"):
        time.sleep(5)

    # 4) Backup
    print("✅ Game closed. Backing up your save…")
    ts   = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    dest = os.path.join(BACKUP_ROOT, f"SaveBackup-{ts}")
    shutil.copytree(SAVE_FOLDER, dest)

    # 5) Prune old backups (keep latest 5)
    backups = sorted(
        [d for d in os.listdir(BACKUP_ROOT)
         if os.path.isdir(os.path.join(BACKUP_ROOT, d))],
        reverse=True
    )
    for old in backups[5:]:
        path = os.path.join(BACKUP_ROOT, old)
        print(f"🗑 Deleting old backup: {old}")
        shutil.rmtree(path)

    print(f"🎉 Backup complete! Kept the latest 5 in:\n    {BACKUP_ROOT}")

if __name__ == "__main__":
    main()

