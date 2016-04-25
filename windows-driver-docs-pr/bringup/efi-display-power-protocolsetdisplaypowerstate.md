---
title: EFI\_DISPLAY\_POWER\_PROTOCOL.SetDisplayPowerState
description: EFI\_DISPLAY\_POWER\_PROTOCOL.SetDisplayPowerState
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ee638d05-4d0e-45b0-a733-73923a7c045a
---

# EFI\_DISPLAY\_POWER\_PROTOCOL.SetDisplayPowerState


Modifies the power state of the display and backlight.

## Syntax


``` syntax
typedef EFI_STATUS (EFIAPI * EFI_DISPLAY_POWER_SETDISPLAYPOWERSTATE) (
    IN EFI_DISPLAY_POWER_PROTOCOL *This,
    IN EFI_DISPLAY_POWER_STATE PowerState 
    );
```

## Parameters


<a href="" id="this"></a>*This*  
\[in\] A pointer to the [EFI\_DISPLAY\_POWER\_PROTOCOL](efi-display-power-protocol.md) instance.

<a href="" id="powerstate"></a>*PowerState*  
\[in\] An [EFI\_DISPLAY\_POWER\_STATE](efi-display-power-state.md) value that specifies the new power state to set.

## Return value


Returns one of the following status codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Status Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>EFI_SUCCESS</p></td>
<td><p>The function returned successfully after changing the power state of both the display and backlight.</p></td>
</tr>
<tr class="even">
<td><p>EFI_INVALID_PARAMETER</p></td>
<td><p>A parameter was incorrect.</p></td>
</tr>
<tr class="odd">
<td><p>EFI_DEVICE_ERROR</p></td>
<td><p>The physical device reported an error.</p></td>
</tr>
</tbody>
</table>

 

## Remarks


This function should have no impact on any hardware component other than the display or backlight.

This function must allow redundant calls without returning an error code. Multiple calls to this function with the same *PowerState* argument must return success. The implementation of this function should avoid unnecessary work when handling redundant calls.

## Requirements


**Header:** User generated

## Related topics


[EFI\_DISPLAY\_POWER\_PROTOCOL](efi-display-power-protocol.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_DISPLAY_POWER_PROTOCOL.SetDisplayPowerState%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





