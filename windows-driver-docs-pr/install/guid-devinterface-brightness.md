---
title: GUID_DEVINTERFACE_BRIGHTNESS
description: GUID_DEVINTERFACE_BRIGHTNESS
ms.assetid: a31b4e12-3702-4a24-98c0-cf8ae7d86a75
keywords: ["GUID_DEVINTERFACE_BRIGHTNESS Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_BRIGHTNESS
api_location:
- Dispmprt.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_BRIGHTNESS


The GUID_DEVINTERFACE_BRIGHTNESS [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for display adapter drivers that operate in the context of the [Windows Vista Display Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff570593) and support brightness control of monitor child devices.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Attribute</th>
<th align="left">Setting</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Identifier</p></td>
<td align="left"><p>GUID_DEVINTERFACE_BRIGHTNESS</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{FDE5BBA4-B3F9-46FB-BDAA-0728CE3100B4}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers register instances of this device interface class to notify the operating system and applications of the presence of brightness control interfaces for monitor child devices.

If the display miniport driver supports a direct-call brightness control interface for this [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509), a kernel-mode component can retrieve the direct-call interface by calling the miniport driver's [**DxgkDdiQueryInterface**](https://msdn.microsoft.com/library/windows/hardware/ff559764) function and supplying GUID_DEVINTERFACE_BRIGHTNESS to specify the interface type.

For information about brightness devices, see [Supporting Brightness Controls on Integrated Display Panels](https://msdn.microsoft.com/library/windows/hardware/ff569755) and [Brightness Control Interface](https://msdn.microsoft.com/library/windows/hardware/ff538260).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Dispmprt.h (include Dispmprt.h)</td>
</tr>
</tbody>
</table>

 

 





