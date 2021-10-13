---
title: EFI_DISPLAY_POWER_PROTOCOL
description: Provides information aboutEFI_DISPLAY_POWER_PROTOCOL.
ms.date: 08/20/2021
ms.localizationpriority: medium
---

# EFI_DISPLAY_POWER_PROTOCOL

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

**Revision**  
The revision to which the **EFI_DISPLAY_POWER_PROTOCOL** adheres. All future revisions must be backward compatible. If a future version is not backward compatible, a different GUID must be used.

The current revision is 0x00010000. Revision should be set to 0x00010000 by the firmware if this revision of the **EFI_BATTERY_CHARGING_PROTOCOL** is supported by the firmware.

**SetDisplayPowerState**  
Modifies the power state of the display and backlight. For more information, see [EFI_DISPLAY_POWER_PROTOCOL.SetDisplayPowerState](efi-display-power-protocolsetdisplaypowerstate.md).

**GetDisplayPowerState**  
Returns the current power state of the display and backlight. For more information, see [EFI_DISPLAY_POWER_PROTOCOL.GetDisplayPowerState](efi-display-power-protocolgetdisplaypowerstate.md).

## Requirements

**Header:** User generated
