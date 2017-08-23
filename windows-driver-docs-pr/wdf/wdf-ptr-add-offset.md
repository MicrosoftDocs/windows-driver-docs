---
title: WDF\_PTR\_ADD\_OFFSET macro
author: windows-driver-content
description: The WDF\_PTR\_ADD\_OFFSET macro adds an offset value to an address and returns the resulting address.
ms.assetid: 21402be4-ef71-4828-b588-d178d66472e5
keywords:
 - WDF_PTR_ADD_OFFSET macro
ms.author: windowsdriverdev
ms.date: 08/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDF\_PTR\_ADD\_OFFSET macro


The **WDF\_PTR\_ADD\_OFFSET** macro adds an offset value to an address and returns the resulting address.

Syntax
------

```ManagedCPlusPlus
PVOID WDF_PTR_ADD_OFFSET(
    _ptr,
    _offset
);
```

Parameters
----------

*\_ptr*   
Specifies an address.

*\_offset*   
Specifies the offset value in bytes.

Return value
------------

Returns a pointer to the resulting address.

Remarks
-------

This macro invokes [**WDF\_PTR\_ADD\_OFFSET\_TYPE**](wdf-ptr-add-offset-type.md) with the *\_type* parameter set to PVOID.

The macro is defined as follows:

```ManagedCPlusPlus
#define WDF_PTR_ADD_OFFSET(_ptr, _offset) \
        WDF_PTR_ADD_OFFSET_TYPE(_ptr, _offset, PVOID)
```

Here is an example from the Toaster sample (toaster\\func\\featured\\wmi.c). In the example, the driver calls **WDF\_PTR\_ADD\_OFFSET** to add an offset to an address to determine a destination buffer address to pass to the [**WDF\_WMI\_BUFFER\_APPEND\_STRING**](https://msdn.microsoft.com/library/windows/hardware/ff553057) function.

```
        //
        // Write the instance name
        //
        size -= wnodeSize;
        status = WDF_WMI_BUFFER_APPEND_STRING(
            WDF_PTR_ADD_OFFSET(wnode, wnode->OffsetInstanceName),
            size,
            &amp;deviceName,
            &amp;length
            );

        //
        // Size was precomputed, this should never fail
        //
        ASSERT(NT_SUCCESS(status));


        //
        // Write the data, which is the model name as a string
        //
        size -= wnodeInstanceNameSize;
        WDF_WMI_BUFFER_APPEND_STRING(
            WDF_PTR_ADD_OFFSET(wnode,  wnode->DataBlockOffset),
            size,
            &amp;modelName,
            &amp;length
            );

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WDF_PTR_ADD_OFFSET%20macro%20%20RELEASE:%20%288/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


