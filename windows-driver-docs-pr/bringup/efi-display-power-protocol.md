---
title: EFI_DISPLAY_POWER_PROTOCOL
description: EFI_DISPLAY_POWER_PROTOCOL
ms.assetid: 61ccf856-7e0b-4f1b-9be9-7b8a31339a6b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_DISPLAY\_POWER\_PROTOCOL


This protocol allows the UEFI battery charging application to turn off the screen after a specified idle duration while charging in the UEFI environment.

## Syntax


```cpp
#define EFI_DISPLAY_POWER_PROTOCOL_GUID \
  {0xf352021d, 0x9593, 0x4432, {0xbf, 0x4, 0x67, 0xb9, 0xf3, 0xb7, 0x60, 0x8};

typedef struct _EFI_DISPLAY_POWER_PROTOCOL {  
    UINT32                                    Revision;  
    EFI_DISPLAY_POWER_SETDISPLAYPOWERSTATE    SetDisplayPowerState;  
    EFI_DISPLAY_POWER_GETDISPLAYPOWERSTATE    GetDisplayPowerState;  
} EFI_DISPLAY_POWER_PROTOCOL;
```

## Members


<a href="" id="revision"></a>**Revision**  
The revision to which the **EFI\_DISPLAY\_POWER\_PROTOCOL** adheres. All future revisions must be backward compatible. If a future version is not backward compatible, a different GUID must be used.

The current revision is 0x00010000. Revision should be set to 0x00010000 by the firmware if this revision of the **EFI\_BATTERY\_CHARGING\_PROTOCOL** is supported by the firmware.

<a href="" id="setdisplaypowerstate"></a>**SetDisplayPowerState**  
Modifies the power state of the display and backlight. For more information, see [EFI\_DISPLAY\_POWER\_PROTOCOL.SetDisplayPowerState](efi-display-power-protocolsetdisplaypowerstate.md).

<a href="" id="getdisplaypowerstate"></a>**GetDisplayPowerState**  
Returns the current power state of the display and backlight. For more information, see [EFI\_DISPLAY\_POWER\_PROTOCOL.GetDisplayPowerState](efi-display-power-protocolgetdisplaypowerstate.md).

## Requirements


**Header:** User generated

 

 




