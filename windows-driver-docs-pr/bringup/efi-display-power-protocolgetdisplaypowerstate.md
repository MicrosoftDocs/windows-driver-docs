---
title: EFI_DISPLAY_POWER_PROTOCOL.GetDisplayPowerState
description: EFI_DISPLAY_POWER_PROTOCOL.GetDisplayPowerState
ms.assetid: 8c5fe55f-903e-4ef0-b3cf-8b764af767cf
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_DISPLAY\_POWER\_PROTOCOL.GetDisplayPowerState


Returns the current power state of the display and backlight.

## Syntax


```cpp
typedef EFI_STATUS (EFIAPI * EFI_DISPLAY_POWER_GETDISPLAYPOWERSTATE) (
    IN EFI_DISPLAY_POWER_PROTOCOL *This,
    OUT EFI_DISPLAY_POWER_STATE *PowerState 
    );
```

## Parameters


<a href="" id="this"></a>*This*  
\[in\] A pointer to the [EFI\_DISPLAY\_POWER\_PROTOCOL](efi-display-power-protocol.md) instance.

<a href="" id="powerstate"></a>*PowerState*  
\[out\] A pointer to an [EFI\_DISPLAY\_POWER\_STATE](efi-display-power-state.md) value that receives the current power state.

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
<td><p>The function returned successfully.</p></td>
</tr>
<tr class="even">
<td><p>EFI_INVALID_PARAMETER</p></td>
<td><p>A parameter was invalid.</p></td>
</tr>
<tr class="odd">
<td><p>EFI_DEVICE_ERROR</p></td>
<td><p>The physical device reported an error.</p></td>
</tr>
</tbody>
</table>

 

## Requirements


**Header:** User generated

## Related topics
[EFI\_DISPLAY\_POWER\_PROTOCOL](efi-display-power-protocol.md)  



