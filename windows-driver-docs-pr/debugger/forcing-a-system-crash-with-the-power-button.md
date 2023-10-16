---
title: Forcing a System Crash with the Power Button
description: Forcing a System Crash with the Power Button
keywords: ["boot process, causing system crash from power button", "system crash, power button", "bug check, power button"]
ms.date: 10/13/2023
---

# Forcing a System Crash with the Power Button

A [Bug Check 0x1C8: MANUALLY_INITIATED_POWER_BUTTON_HOLD](bug-check-0x1c8--manually-initiated-power-button-hold.md) manual system crash can be forced by pressing and holding the power button when the following registry value is set in the registry key shown:

```reg
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power]
"PowerButtonBugcheck"=dword:00000001
```

If this registry value does *not* exist, the system must be rebooted for this change to take effect.

If this registry value *does* exist and the value is changed, the system does *not* need to be rebooted for the change to take effect.

The bug check occurs when the power button is held for 7 seconds, but released before the UEFI Reset occurs at 10 seconds.

To support Long Power Button Hold, the device needs a General Purpose I/O (GPIO) based Power Button, Firmware to route the power event to the Windows Power Manager, and for the bug check feature to be enabled in the registry.

This feature is available in Windows 10 1809 / Windows Server 2019 and newer.
