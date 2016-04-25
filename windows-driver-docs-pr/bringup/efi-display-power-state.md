---
title: EFI\_DISPLAY\_POWER\_STATE
description: EFI\_DISPLAY\_POWER\_STATE
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b4b0980b-db87-44e8-842c-afce0c8df0a0
---

# EFI\_DISPLAY\_POWER\_STATE


This enumeration represents the charging state of the display and backlight. This enumeration is a parameter of the [EFI\_DISPLAY\_POWER\_PROTOCOL.GetDisplayPowerState](efi-display-power-protocolgetdisplaypowerstate.md) and [EFI\_DISPLAY\_POWER\_PROTOCOL.SetDisplayPowerState](efi-display-power-protocolsetdisplaypowerstate.md) functions.

## Syntax


``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_DISPLAY_POWER_STATE%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





