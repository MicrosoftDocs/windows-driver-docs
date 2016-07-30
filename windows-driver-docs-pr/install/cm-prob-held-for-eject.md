---
title: CM\_PROB\_HELD\_FOR\_EJECT
description: CM\_PROB\_HELD\_FOR\_EJECT
ms.assetid: 8d67ad71-276d-4dea-b3fb-61fedcfba789
keywords: ["CM_PROB_HELD_FOR_EJECT"]
---

# CM\_PROB\_HELD\_FOR\_EJECT


## <a href="" id="ddk-cm-prob-held-for-eject-dg"></a>


The device has been prepared for ejection.

### Error Code

47

### Display Message (Windows XP and later versions of Windows)

"Windows cannot use this hardware device because it has been prepared for 'safe removal', but it has not been removed from the computer. (Code 47)"

"To fix this problem, unplug this device from your computer and then plug it in again."

### Recommended Resolution (Windows XP and later versions of Windows)

Unplug the device and plug it in again. Alternatively, selecting **Restart Computer** will restart the computer and make the device available.

This error should occur only if the user invokes the hot-plug program to prepare the device for removal (which calls [**CM\_Request\_Device\_Eject**](https://msdn.microsoft.com/library/windows/hardware/ff539806)), or if the user presses a physical eject button (which calls [**IoRequestDeviceEject**](https://msdn.microsoft.com/library/windows/hardware/ff549647)). The user can prepare a device that is currently not removable, such as a CD-ROM trapped between the laptop and the docking station tray.

 

 





