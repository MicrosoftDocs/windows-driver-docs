---
title: WdfObjectGetCustomTypeData macro
author: windows-driver-content
description: The WdfObjectGetCustomTypeData macro retrieves the data that the driver previously associated with a framework object and custom type.
ms.assetid: 60A6546B-84C6-4A53-BAA1-3719DCBA63B4
keywords:
 - WdfObjectGetCustomTypeData macro
ms.author: windowsdriverdev
ms.date: 08/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WdfObjectGetCustomTypeData macro


\[Applies to KMDF and UMDF\]

The **WdfObjectGetCustomTypeData** macro retrieves the data that the driver previously associated with a framework object and custom type.

Syntax
------

```ManagedCPlusPlus
PULONG WdfObjectGetCustomTypeData(
  [in]  Handle,
  [in]  Type
);
```

Parameters
----------

*Handle* \[in\]  
A handle to a framework object.

*Type* \[in\]  
The symbol name of a custom type.

Return value
------------

**WdfObjectGetCustomTypeData** returns the data that the driver associated with a framework object and custom type in a previous call to [**WdfObjectAddCustomTypeWithData**](wdfobjectaddcustomtypewithdata.md).

Remarks
-------

For more information about object driver types, see [Framework Object Custom Types](https://msdn.microsoft.com/library/windows/hardware/hh406457).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
</tr>
<tr class="even">
<td><p>Minimum KMDF version</p></td>
<td><p>1.11</p></td>
</tr>
<tr class="odd">
<td><p>Minimum UMDF version</p></td>
<td><p>2.0</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wdfobject.h (include Wdf.h)</td>
</tr>
</tbody>
</table>

## See also


[**WDF\_DECLARE\_CUSTOM\_TYPE**](wdf-declare-custom-type.md)

[**WdfObjectAddCustomType**](wdfobjectaddcustomtype.md)

[**WdfObjectAddCustomTypeWithData**](wdfobjectaddcustomtypewithdata.md)

[**WdfObjectIsCustomType**](wdfobjectiscustomtype.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WdfObjectGetCustomTypeData%20macro%20%20RELEASE:%20%288/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


