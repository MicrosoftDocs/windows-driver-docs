---
title: WDF\_PTR\_GET\_OFFSET macro
author: windows-driver-content
description: The WDF\_PTR\_GET\_OFFSET macro subtracts an address from another address and returns the resulting offset value.
ms.assetid: b5159207-ba5c-4924-a06e-725ccd3c8a12
keywords:
 - WDF_PTR_GET_OFFSET macro
ms.author: windowsdriverdev
ms.date: 08/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDF\_PTR\_GET\_OFFSET macro


The **WDF\_PTR\_GET\_OFFSET** macro subtracts an address from another address and returns the resulting offset value.

Syntax
------

```ManagedCPlusPlus
size_t WDF_PTR_GET_OFFSET(
    _base,
    _addr
);
```

Parameters
----------

*\_base*   
Specifies the value to subtract from the starting address.

*\_addr*   
Specifies the starting address.

Return value
------------

Returns the offset between the two specified addresses.

Remarks
-------

The macro is defined as follows:

```ManagedCPlusPlus
#define WDF_PTR_GET_OFFSET(_base, _addr) \
        (size_t) (((PUCHAR) _addr) - ((PUCHAR) _base))
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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WDF_PTR_GET_OFFSET%20macro%20%20RELEASE:%20%288/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


