---
title: WDF\_PTR\_ADD\_OFFSET\_TYPE macro
author: windows-driver-content
description: The WDF\_PTR\_ADD\_OFFSET\_TYPE macro adds an offset value to an address and returns the resulting address cast to the specified type.
ms.assetid: b46d0bbe-8401-4c97-8327-fecd3af50eca
keywords:
 - WDF_PTR_ADD_OFFSET_TYPE macro
ms.author: windowsdriverdev
ms.date: 08/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDF\_PTR\_ADD\_OFFSET\_TYPE macro


The **WDF\_PTR\_ADD\_OFFSET\_TYPE** macro adds an offset value to an address and returns the resulting address cast to the specified type.

Syntax
------

```ManagedCPlusPlus
_type WDF_PTR_ADD_OFFSET_TYPE(
    _ptr,
    _offset,
    _type
);
```

Parameters
----------

*\_ptr*   
Specifies an address.

*\_offset*   
Specifies the offset value in bytes.

*\_type*   
Specifies the data type to return.

Return value
------------

Returns a pointer to the resulting address. You select the data type of the return value in the *\_type* parameter of the macro.

Remarks
-------

The macro is defined as follows:

```ManagedCPlusPlus
#define WDF_PTR_ADD_OFFSET_TYPE(_ptr, _offset, _type) \
    ((_type) (((PUCHAR) (_ptr)) + (_offset)))
```

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
<td><p>1.5</p></td>
</tr>
<tr class="odd">
<td><p>Minimum UMDF version</p></td>
<td><p>2.0</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wdfcore.h (include Wdf.h)</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WDF_PTR_ADD_OFFSET_TYPE%20macro%20%20RELEASE:%20%288/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


