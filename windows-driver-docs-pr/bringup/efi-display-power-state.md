---
title: EFI_DISPLAY_POWER_STATE
description: Provides information about the EFI_DISPLAY_POWER_STATE enumeration.
ms.date: 02/24/2023
ms.topic: reference
---

# EFI_DISPLAY_POWER_STATE

This enumeration represents the charging state of the display and backlight. This enumeration is a parameter of the [EFI_DISPLAY_POWER_PROTOCOL.GetDisplayPowerState](efi-display-power-protocolgetdisplaypowerstate.md) and [EFI_DISPLAY_POWER_PROTOCOL.SetDisplayPowerState](efi-display-power-protocolsetdisplaypowerstate.md) functions.

## Syntax

```cpp
typedef enum _EFI_DISPLAY_POWER_STATE {  
    EfiDisplayPowerStateUnknown = 0,  
    EfiDisplayPowerStateOff,  
    EfiDisplayPowerStateMaximum,  
} EFI_DISPLAY_POWER_STATE;
```

## Elements

EfiDisplayPowerStateUnknown  
The power state is not initialized. This value can only be used for variable initialization; it cannot be passed to or returned by any [EFI_DISPLAY_POWER_PROTOCOL](efi-display-power-protocol.md) function.

EfiDisplayPowerStateOff  
When used with [EFI_DISPLAY_POWER_PROTOCOL.GetDisplayPowerState](efi-display-power-protocolgetdisplaypowerstate.md), indicates that power to the display and backlight are turned off. When used with [EFI_DISPLAY_POWER_PROTOCOL.SetDisplayPowerState](efi-display-power-protocolsetdisplaypowerstate.md), turns off power to the display and backlight.

EfiDisplayPowerStateMaximum  
When used with [EFI_DISPLAY_POWER_PROTOCOL.GetDisplayPowerState](efi-display-power-protocolgetdisplaypowerstate.md), indicates that the display and backlight have full power. When used with [EFI_DISPLAY_POWER_PROTOCOL.SetDisplayPowerState](efi-display-power-protocolsetdisplaypowerstate.md), turns on full power to the display and backlight.

## Requirements

**Header:** User generated

## Related topics

[EFI_DISPLAY_POWER_PROTOCOL](efi-display-power-protocol.md)  
