---
title: GUID_DEVINTERFACE_I2C
description: GUID_DEVINTERFACE_I2C
ms.assetid: 765cecb7-b8ea-48ef-bdab-742da722e169
keywords: ["GUID_DEVINTERFACE_I2C Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_I2C
api_location:
- Dispmprt.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_I2C


The GUID_DEVINTERFACE_I2C [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for display adapter drivers that operate in the context of the [Windows Vista Display Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff570593) and perform I2C transactions with monitor child devices.

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
<td align="left"><p>GUID_DEVINTERFACE_I2C</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{2564AA4F-DDDB-4495-B497-6AD4A84163D7}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers register instances of this device interface class to notify the operating system and applications of the presence of I2C interfaces that perform transactions with monitor child devices.

If a display miniport driver supports a direct-call I2C interface for this [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509), a kernel-mode component can retrieve the direct-call interface by calling the miniport driver's [**DxgkDdiQueryInterface**](https://msdn.microsoft.com/library/windows/hardware/ff559764) function and supplying GUID_DEVINTERFACE_I2C to specify the interface type.

For information about the I2C bus, see [I2C Bus and Child Devices of the Display Adapter](https://msdn.microsoft.com/library/windows/hardware/ff567381).

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

 

 





