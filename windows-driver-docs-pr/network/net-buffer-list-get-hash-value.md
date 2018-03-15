---
title: NET_BUFFER_LIST_GET_HASH_VALUE macro
author: windows-driver-content
description: The NET_BUFFER_LIST_GET_HASH_VALUE macro gets the hash value information from a NET_BUFFER_LIST structure. Version Information Windows VistaSupported. NDIS 6.0 driversSupported.
ms.assetid: 7e3794e4-1afe-416f-b8f8-689f6397fc6a
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_GET_HASH_VALUE macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_GET\_HASH\_VALUE macro


The NET\_BUFFER\_LIST\_GET\_HASH\_VALUE macro gets the hash value information from a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

**Version Information**

<a href="" id="windows-vista"></a>Windows Vista  
Supported.

<a href="" id="ndis-6-0-drivers"></a>NDIS 6.0 drivers  
Supported.

Syntax
------

```ManagedCPlusPlus
ULONG NET_BUFFER_LIST_GET_HASH_VALUE(
   PNET_BUFFER_LIST NetBufferList
);
```

Parameters
----------

*NetBufferList*   
A pointer to a NET\_BUFFER\_LIST structure.

Return value
------------

NET\_BUFFER\_LIST\_GET\_HASH\_VALUE returns the hash value formatted as a ULONG.

## <a href="" id="ddk-net-buffer-list-get-hash-value-nr"></a>


Remarks
-------

For more information about the hash value, see [RSS Hashing Functions](https://msdn.microsoft.com/library/windows/hardware/ff570725).

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
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 




