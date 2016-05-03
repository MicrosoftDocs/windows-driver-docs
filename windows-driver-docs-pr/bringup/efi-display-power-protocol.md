---
title: EFI\_DISPLAY\_POWER\_PROTOCOL
author: windows-driver-content
description: EFI\_DISPLAY\_POWER\_PROTOCOL
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 61ccf856-7e0b-4f1b-9be9-7b8a31339a6b
---

# EFI\_DISPLAY\_POWER\_PROTOCOL


This protocol allows the UEFI battery charging application to turn off the screen after a specified idle duration while charging in the UEFI environment.

## Syntax


``` syntax
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_DISPLAY_POWER_PROTOCOL%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


