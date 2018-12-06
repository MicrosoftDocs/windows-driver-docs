---
title: EFI_DISPLAY_POWER_STATE
description: EFI_DISPLAY_POWER_STATE
ms.assetid: b4b0980b-db87-44e8-842c-afce0c8df0a0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_DISPLAY\_POWER\_STATE


This enumeration represents the charging state of the display and backlight. This enumeration is a parameter of the [EFI\_DISPLAY\_POWER\_PROTOCOL.GetDisplayPowerState](efi-display-power-protocolgetdisplaypowerstate.md) and [EFI\_DISPLAY\_POWER\_PROTOCOL.SetDisplayPowerState](efi-display-power-protocolsetdisplaypowerstate.md) functions.

## Syntax


```cpp
typedef enum _EFI_DISPLAY_POWER_STATE {  
    EfiDisplayPowerStateUnknown = 0,  
    EfiDisplayPowerStateOff,  
    EfiDisplayPowerStateMaximum,  
} EFI_DISPLAY_POWER_STATE;
```

## Elements


<a href="" id="efidisplaypowerstateunknown"></a>EfiDisplayPowerStateUnknown  
The power state is not initialized. This value can only be used for variable initialization; it cannot be passed to or returned by any [EFI\_DISPLAY\_POWER\_PROTOCOL](efi-display-power-protocol.md) function.

<a href="" id="efidisplaypowerstateoff"></a>EfiDisplayPowerStateOff  
When used with [EFI\_DISPLAY\_POWER\_PROTOCOL.GetDisplayPowerState](efi-display-power-protocolgetdisplaypowerstate.md), indicates that power to the display and backlight are turned off. When used with [EFI\_DISPLAY\_POWER\_PROTOCOL.SetDisplayPowerState](efi-display-power-protocolsetdisplaypowerstate.md), turns off power to the display and backlight.

<a href="" id="efidisplaypowerstatemaximum"></a>EfiDisplayPowerStateMaximum  
When used with [EFI\_DISPLAY\_POWER\_PROTOCOL.GetDisplayPowerState](efi-display-power-protocolgetdisplaypowerstate.md), indicates that the display and backlight have full power. When used with [EFI\_DISPLAY\_POWER\_PROTOCOL.SetDisplayPowerState](efi-display-power-protocolsetdisplaypowerstate.md), turns on full power to the display and backlight.

## Requirements


**Header:** User generated

## Related topics
[EFI\_DISPLAY\_POWER\_PROTOCOL](efi-display-power-protocol.md)  



