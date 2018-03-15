---
title: NET_BUFFER_DATA_PHYSICAL_ADDRESS macro
author: windows-driver-content
description: The NET_BUFFER_DATA_PHYSICAL_ADDRESS macro retrieves the DataPhysicalAddress member of a NET_BUFFER structure.
ms.assetid: da9971ec-38ce-4489-a11a-886aab9c6e6c
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_DATA_PHYSICAL_ADDRESS macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_DATA\_PHYSICAL\_ADDRESS macro


The NET\_BUFFER\_DATA\_PHYSICAL\_ADDRESS macro retrieves the **DataPhysicalAddress** member of a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

Syntax
------

```ManagedCPlusPlus
NDIS_PHYSICAL_ADDRESS NET_BUFFER_DATA_PHYSICAL_ADDRESS(
   PNET_BUFFER _NB
);
```

Parameters
----------

*\_NB*   
A pointer to a NET\_BUFFER structure.

Return value
------------

NET\_BUFFER\_DATA\_PHYSICAL\_ADDRESS returns the **DataPhysicalAddress** member of a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

Remarks
-------

NDIS network drivers should use the NET\_BUFFER\_DATA\_PHYSICAL\_ADDRESS macro to get the **DataPhysicalAddress** member of a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

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
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.1 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376)

 

 




