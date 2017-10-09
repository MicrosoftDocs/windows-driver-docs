---
title: GUID\_DEVINTERFACE\_I2C
description: GUID\_DEVINTERFACE\_I2C
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
---

# GUID\_DEVINTERFACE\_I2C


The GUID\_DEVINTERFACE\_I2C [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for display adapter drivers that operate in the context of the [Windows Vista Display Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff570593) and perform I2C transactions with monitor child devices.

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

If a display miniport driver supports a direct-call I2C interface for this [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509), a kernel-mode component can retrieve the direct-call interface by calling the miniport driver's [**DxgkDdiQueryInterface**](https://msdn.microsoft.com/library/windows/hardware/ff559764) function and supplying GUID\_DEVINTERFACE\_I2C to specify the interface type.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20GUID_DEVINTERFACE_I2C%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




