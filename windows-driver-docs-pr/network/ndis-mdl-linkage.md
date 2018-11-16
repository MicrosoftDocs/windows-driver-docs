---
title: NDIS_MDL_LINKAGE macro
description: The NDIS_MDL_LINKAGE macro retrieves a pointer to the next MDL that is associated with the specified MDL.
ms.assetid: 3d5a91cb-cb26-49fb-b510-75fc95f7f46b
ms.date: 07/18/2017
keywords:
 - NDIS_MDL_LINKAGE macro Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_MDL\_LINKAGE macro


The **NDIS\_MDL\_LINKAGE** macro retrieves a pointer to the next MDL that is associated with the specified MDL.

Syntax
------

```ManagedCPlusPlus
PVOID NDIS_MDL_LINKAGE(
   PMDL _Mdl
);
```

Parameters
----------

*\_Mdl*   
A pointer to an MDL.

Return value
------------

**NDIS\_MDL\_LINKAGE** returns a pointer to an MDL or **NULL** if there is no next MDL.

Remarks
-------

The **NDIS\_MDL\_LINKAGE** macro provides an MDL-based version of the [**NDIS\_BUFFER\_LINKAGE**](https://msdn.microsoft.com/library/windows/hardware/ff556919) function.

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


[**NDIS\_BUFFER\_LINKAGE**](https://msdn.microsoft.com/library/windows/hardware/ff556919)

 

 




