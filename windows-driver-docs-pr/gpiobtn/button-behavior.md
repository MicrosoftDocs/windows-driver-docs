---
title: Button Behavior
description: This topic describes the expected behavior of hardware buttons.
ms.date: 10/17/2018
---

# Button behavior

This topic describes the expected behavior of hardware buttons.

## Required and optional buttons in Windows 10

|Operating system/device|Power|Volume up/Volume down|Start|Back/search|Camera|Rotation lock|
|---|---|---|---|---|---|---|
|Windows 10 Mobile|Required|Required|Required for phones that use a WVGA display. Optional for all other devices|Required for phones that use a WVGA display. Optional for all other devices|Optional|Not supported|
|Windows 10 for desktop editions (Home, Pro, Enterprise, and Education)/Tablets|Required|Required|Optional|Not supported|Not supported|Optional|
|Windows 10 for desktop editions/Other devices|Required|Required for devices with detachable keyboards. Optional for all other devices.|Optional|Not supported|Not supported|Optional|

For more information about button requirements:

- For Windows 10 Mobile, see section 2.6 in the [Minimum Hardware Requirements](/windows-hardware/design/minimum/minimum-hardware-requirements-overview).
- For Windows 10 for desktop editions, see section 3.6 in the [Minimum Hardware Requirements](/windows-hardware/design/minimum/minimum-hardware-requirements-overview).

## Button behavior in Windows 10

### Single button behavior in Windows 10

|Button|Activity|Windows 10 for desktop editions|Windows 10 Mobile|
|---|---|---|---|
|Power|Press and release|Toggle On/Off|Toggle On/Off|
|Power|Press and hold|Launch Shutdown Curtain|Launch Shutdown Curtain|
|Power|Long press and hold|Hard shutdown|Hardware reset|
|Search|Press and release|Not supported|Launch Cortana (in enabled markets)/Search|
|Search|Press and hold|Not supported|Launch Cortana or Search with Voice|
|Volume up|Press and release|Increment volume|Increment volume|
Volume up|Press and hold|Auto-repeat volume increment|Auto-repeat volume increment|
|Volume down|Press and release|Decrement volume|Decrement volume|
|Volume down|Press and hold|Auto-repeat volume decrement|Auto-repeat volume decrement|
|Back|Press and release|Previous app page/close app|Previous app page/close app|
|Back|Press and hold|Launch Task switcher|Launch switcher UI|
|Start||Toggle Start screen|Show Start screen|
|Rotation lock||Not supported|Not supported (there is a UI option)|
|Camera focus||Launch Camera application|Handled by Camera app (focus)|
|Camera shutter||Handled by Camera application|Launch Camera app / take picture|

### Button combination behavior in Windows 10

As noted, some button combinations in Windows 10 apply to the [Windows 10 button architecture](../hid/buttons.md) or the Windows 8.1 button architecture. All other button combinations in Windows 10 apply to either button architecture. It is recommended to describe hardware buttons using the Windows 10 architecture.

|Button combination|Windows 10 for desktop editions|Windows 10 Mobile|
|---|---|---|
|Start + Volume Up|Toggle on-screen narrator|Toggle on-screen narrator (provided that the corresponding ease-of-access setting is enabled)|
|Start + Volume Down|Take screenshot|Not supported|
|Start + Power|Ctrl+Alt+Del (only if using Windows 8.1 button architecture)|Not supported|
|Power + Volume Up|Take screenshot (only if using Windows 10 button architecture)|Take screenshot|
|Power + Volume Down|Ctrl+Alt+Del (only if using Windows 10 button architecture)|Launch the Windows Feedback app. Hardware reset (after 10 sec)|

## Button behavior in Windows 8.1

### Single button behavior in Windows 8.1

|Button|Action|Windows 8.1|Windows 8.1 Phone|
|---|---|---|---|
|Power|Press and release|Toggle On/Off|Toggle On/Off|
|Power|Press and hold|Launch Shutdown Curtain|Launch Shutdown Curtain|
|Power|Long press and hold|Hard shutdown|Hardware reset|
|Search|Press and release|Not supported|Launch Cortana|
|Search|Press and hold|Not supported|Launch Cortana with Voice|
|Volume up|Press and release|Increment volume|Increment volume|
|Volume up|Press and hold|Auto-repeat volume increment|Auto-repeat volume increment|
|Volume down|Press and release|Decrement volume|Decrement volume|
|Volume down|Press and hold|Auto-repeat volume decrement|Auto-repeat volume decrement|
|Back||Not supported|Not supported|
|Start||Toggle Start screen|Toggle Start screen|
|Rotation lock||Release: Lock rotation|Lock rotation|
|Camera focus||Not supported|Not applicable|
|Camera shutter||Not supported|Not applicable|

### Button combination behavior in Windows 8.1

|Button combination|Windows 8.1|Windows 8.1 Phone|
|---|---|---|
|Start + Volume Up|Toggle on-screen narrator|Not supported|
|Start + Volume Down|Take screenshot|Not supported|
|Start + Power|Ctrl+Alt+Del|Not supported|
|Power + Volume Up|Not supported|Take screenshot|
|Power + Volume Down|Not supported|Hardware reset (after 10 sec)|

## Related topics

[Windows 10 button architecture](../hid/buttons.md)  
[Minimum Hardware Requirements](/windows-hardware/design/minimum/minimum-hardware-requirements-overview)
