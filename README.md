# TLP Python Menu 

# Screenshot
<img width="886" height="617" alt="menu" src="https://github.com/user-attachments/assets/8d68027c-c1b2-4a3a-bac3-18a2d4bc555a" />
<img width="649" height="481" alt="Term" src="https://github.com/user-attachments/assets/24fb55ee-4c9f-4dd3-b5f5-f68cef6f2ecb" />
<img width="970" height="617" alt="menutlp" src="https://github.com/user-attachments/assets/00f19a06-de98-40cc-b712-2b9d6bf63741" />


Hey everyone 👋 I'm a beginner vibe-coder, and this is a small project I built to make TLP easier to use.

TLP is a great Linux power management tool, but it has no simple menu — you have to remember a bunch of commands. So I made a small Python menu that wraps the most useful TLP commands in a terminal UI.

**Tested on:** Linux Mint 22 (MATE), should work on Ubuntu 24.04+ / Cinnamon / XFCE / any Debian-based distro.

---

## What it does

Simple terminal menu for TLP:

- Start TLP
- Switch between AC / battery mode
- USB autosuspend
- Charge once / full charge / discharge
- Show status, battery info, config
- Optionally launch **TLPUI** (GUI) if installed

---

## Requirements

- Linux (Debian/Ubuntu/Mint family)
- Python 3 (usually preinstalled)
- `tlp` package installed

---

## Installation

### 1. Install TLP

```bash
sudo apt update
sudo apt install tlp tlp-rdw
```

### 2. Install TLPUI (optional GUI)

```bash
sudo apt install flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install flathub com.github.d4nj1.tlpui
```

### 3. Clone this repo

```bash
git clone https://github.com/cr-sk-uk/tlp-menu-linux-guide.git
cd tlp-menu-linux-guide
chmod +x menu.py
```

### 4. Allow TLP commands without password

```bash
sudo visudo -f /etc/sudoers.d/tlp-python
```

Paste this line (replace `YOUR_USERNAME` with your Linux username):

```
YOUR_USERNAME ALL=(root) NOPASSWD: /usr/bin/tlp, /usr/bin/tlp-stat
```

Save: `Ctrl+O` → `Enter` → `Ctrl+X`

### 5. Run it

```bash
python3 menu.py
```

---

## Optional: make it a command

```bash
echo 'alias tlpmenu="python3 ~/tlp-menu-linux-guide/menu.py"' >> ~/.bashrc
source ~/.bashrc
```

Now just type:

```bash
tlpmenu
```

---

## Optional: set battery charge threshold (ThinkPad / supported laptops)

Edit `/etc/tlp.conf`:

```bash
sudo nano /etc/tlp.conf
```

Find these lines and uncomment them (remove `#`):

```
START_CHARGE_THRESH_BAT0=80
STOP_CHARGE_THRESH_BAT0=85
```

Then apply:

```bash
sudo systemctl restart tlp
sudo tlp-stat -b
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `sudo: a password is required` | Check `/etc/sudoers.d/tlp-python` |
| `command not found: tlp` | `sudo apt install tlp` |
| TLPUI doesn't launch | `flatpak list \| grep tlpui` |
| `Error: unknown command "stop"` | TLP has no `stop` — use `sudo systemctl stop tlp` |

---

## License

MIT — do whatever you want, just keep the credit.

---

## Thanks

Built with help from AI and a lot of trial and error. Hope it saves someone time. ❤️

If it helped you — give it a ⭐
