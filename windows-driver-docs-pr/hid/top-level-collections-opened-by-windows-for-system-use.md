---
title: Top-Level Collections Opened by Windows for System Use
description: Top-Level Collections Opened by Windows for System Use
keywords:
- top-level collections WDK HID
ms.date: 04/20/2017
---

# Top-Level Collections Opened by Windows for System Use

Windows opens the following [top-level collections](top-level-collections.md) for system use:

| Device Type            | Usage Page | Usage ID | Windows Client                                                                                     | Access Mode |
|------------------------|:----------:|:--------:|----------------------------------------------------------------------------------------------------|-------------|
| Pointer                | 0x01       | 0x01     | Win32 subsystem                                                                                    | Exclusive   |
| Mouse                  | 0x01       | 0x02     | Win32 subsystem                                                                                    | Exclusive   |
| Joystick               | 0x01       | 0x04     | DirectInput                                                                                        | Shared      |
| Game pad               | 0x01       | 0x05     | DirectInput                                                                                        | Shared      |
| Keyboard               | 0x01       | 0x06     | Win32 subsystem                                                                                    | Exclusive   |
| Keypad                 | 0x01       | 0x07     | Win32 subsystem                                                                                    | Exclusive   |
| System Control         | 0x01       | 0x80     | Win32 subsystem                                                                                    | Shared      |
| Consumer Audio Control | 0x0C       | 0x01     | hidserv.exe in Windows 2000 and hidserv.dll (one of the SVC host services) in Microsoft Windows XP | Shared      |
