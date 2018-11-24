---
title: NDIS_MDL_TO_SPAN_PAGES macro
description: The NDIS_MDL_TO_SPAN_PAGES macro retrieves the number of physical pages of memory that are being used to back a given MDL.
ms.assetid: 8c9df989-4a5f-4ec1-9544-29b59517a502
ms.date: 07/18/2017
keywords:
- NDIS_MDL_TO_SPAN_PAGES macro Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




