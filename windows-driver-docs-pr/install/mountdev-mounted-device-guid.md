---
title: MOUNTDEV\_MOUNTED\_DEVICE\_GUID
description: MOUNTDEV\_MOUNTED\_DEVICE\_GUID
ms.assetid: 48d127ed-414b-40bb-8a35-6472c8783b81
keywords: ["MOUNTDEV_MOUNTED_DEVICE_GUID Device and Driver Installation"]
topic_type:
- apiref
api_name:
- MOUNTDEV_MOUNTED_DEVICE_GUID
api_location:
- Mountmgr.h
api_type:
- HeaderDef
---

# MOUNTDEV\_MOUNTED\_DEVICE\_GUID


The MOUNTDEV\_MOUNTED\_DEVICE\_GUID [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for volume devices.

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
<td align="left"><p>MOUNTDEV_MOUNTED_DEVICE_GUID</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{53F5630D-B6BF-11D0-94F2-00A0C91EFB8B}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The MOUNTDEV\_MOUNTED\_DEVICE\_GUID identifier for this device interface class is an alias for the [**GUID\_DEVINTERFACE\_VOLUME**](guid-devinterface-volume.md) device interface class.

The storage [samples](http://go.microsoft.com/fwlink/p/?LinkId=618052) in the WDK includes the [ClassPnP Storage Class Driver Library](http://go.microsoft.com/fwlink/p/?linkid=256095) that uses MOUNTDEV\_MOUNTED\_DEVICE\_GUID to register instances of the GUID\_DEVINTERFACE\_VOLUME device interface class.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Mountmgr.h (include Mountmgr.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID\_DEVINTERFACE\_VOLUME**](guid-devinterface-volume.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20MOUNTDEV_MOUNTED_DEVICE_GUID%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





