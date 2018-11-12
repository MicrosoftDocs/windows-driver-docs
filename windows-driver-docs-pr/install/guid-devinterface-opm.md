---
title: GUID_DEVINTERFACE_OPM
description: GUID_DEVINTERFACE_OPM
ms.assetid: bd999b09-d531-4b89-a306-83e1ca7cac64
keywords: ["GUID_DEVINTERFACE_OPM Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_OPM
api_location:
- Dispmprt.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_OPM


The GUID_DEVINTERFACE_OPM [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for display adapter drivers that operate in the context of the [Windows Vista Display Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff570593) and support output protection management (OPM) for monitor child devices.

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
<td align="left"><p>GUID_DEVINTERFACE_OPM</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{BF4672DE-6B4E-4BE4-A325-68A91EA49C09}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers register instances of this device interface class to notify the operating system and applications of the presence of OPM device interfaces.

If a display miniport driver supports a direct-call OPM interface for this [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509), a kernel-mode component can retrieve the direct-call interface by calling the miniport driver's [**DxgkDdiQueryInterface**](https://msdn.microsoft.com/library/windows/hardware/ff559764) function and supplying GUID_DEVINTERFACE_OPM to specify the interface type.

For information about OPM, see [Supporting Output Protection Manager](https://msdn.microsoft.com/library/windows/hardware/ff569879).

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

 

 





