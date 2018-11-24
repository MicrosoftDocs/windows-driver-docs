---
title: EFI_DISPLAY_POWER_PROTOCOL.SetDisplayPowerState
description: EFI_DISPLAY_POWER_PROTOCOL.SetDisplayPowerState
ms.assetid: ee638d05-4d0e-45b0-a733-73923a7c045a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_DISPLAY\_POWER\_PROTOCOL.SetDisplayPowerState


Modifies the power state of the display and backlight.

## Syntax


```cpp
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



