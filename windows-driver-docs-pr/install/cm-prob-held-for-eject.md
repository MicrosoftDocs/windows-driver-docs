---
title: CM_PROB_HELD_FOR_EJECT
description: CM_PROB_HELD_FOR_EJECT
keywords:
- CM_PROB_HELD_FOR_EJECT
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Code 47 - CM_PROB_HELD_FOR_EJECT

This Device Manager error message indicates that the device has been prepared for ejection.

## Error Code

47

### Display Message

"Windows cannot use this hardware device because it has been prepared for 'safe removal', but it has not been removed from the computer. (Code 47)"

"To fix this problem, unplug this device from your computer and then plug it in again."

### Recommended Resolution

Unplug the device and plug it in again. Alternatively, selecting **Restart Computer** will restart the computer and make the device available.

This error should occur only if the user invokes the hot-plug program to prepare the device for removal (which calls [**CM_Request_Device_Eject**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_request_device_ejectw)), or if the user presses a physical eject button (which calls [**IoRequestDeviceEject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iorequestdeviceeject)). The user can prepare a device that is currently not removable, such as a CD-ROM trapped between the laptop and the docking station tray.
