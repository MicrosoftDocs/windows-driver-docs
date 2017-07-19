---
title: NDIS\_MDL\_TO\_SPAN\_PAGES macro
author: windows-driver-content
description: The NDIS\_MDL\_TO\_SPAN\_PAGES macro retrieves the number of physical pages of memory that are being used to back a given MDL.
ms.assetid: 8c9df989-4a5f-4ec1-9544-29b59517a502
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
- NDIS_MDL_TO_SPAN_PAGES macro Network Drivers Starting with Windows Vista
---

# NDIS\_MDL\_TO\_SPAN\_PAGES macro


The **NDIS\_MDL\_TO\_SPAN\_PAGES** macro retrieves the number of physical pages of memory that are being used to back a given MDL.

Syntax
------

```ManagedCPlusPlus
int NDIS_MDL_TO_SPAN_PAGES(
   PMDL _Mdl
);
```

Parameters
----------

*\_Mdl*   
A pointer to an MDL.

Return value
------------

**NDIS\_MDL\_TO\_SPAN\_PAGES** returns the number of pages that are backing the virtual range for the MDL.

Remarks
-------

The **NDIS\_MDL\_TO\_SPAN\_PAGES** macro provides an MDL-based version of the [**NDIS\_BUFFER\_TO\_SPAN\_PAGES**](https://msdn.microsoft.com/library/windows/hardware/ff556922) function.

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
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
<tr class="even">
<td><p>IRQL</p></td>
<td><p>Any level</p></td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_BUFFER\_TO\_SPAN\_PAGES**](https://msdn.microsoft.com/library/windows/hardware/ff556922)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_MDL_TO_SPAN_PAGES%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


