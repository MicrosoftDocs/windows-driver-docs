---
title: NET_BUFFER_LIST_INFO macro
author: windows-driver-content
description: NET_BUFFER_LIST_INFO is a macro that NDIS drivers use to get and set information that applies to all the NET_BUFFER structures in a NET_BUFFER_LIST structure.
ms.assetid: 3ee2e7b5-1592-4913-a39d-44b815398c76
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_INFO macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_INFO macro


NET\_BUFFER\_LIST\_INFO is a macro that NDIS drivers use to get and set information that applies to all the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures in a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
PVOID NET_BUFFER_LIST_INFO(
   PNET_BUFFER_LIST _NBL,
   ULONG            _Id
);
```

Parameters
----------

*\_NBL*   
A pointer to a NET\_BUFFER\_LIST structure.

*\_Id*   
An ID that indicates the type of information to access from the **NetBufferListInfo** member of the NET\_BUFFER\_LIST structure that the *\_NBL* parameter specifies.

Return value
------------

NET\_BUFFER\_LIST\_INFO returns the information that is associated with the specified ID. The information is retrieved from the **NetBufferListInfo** member of the indicated NET\_BUFFER\_LIST structure.

Remarks
-------

For a list of the valid **NetBufferListInfo** IDs, see the [**NDIS\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566569) reference page.

The following example demonstrates getting a **NetBufferListInfo** value:

```
 value = NET_BUFFER_LIST_INFO(pNbl, Id);
```

The following example demonstrates setting a **NetBufferListInfo** value:

```
 NET_BUFFER_LIST_INFO(pNbl, Id) = value;
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
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566569)

[**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 




