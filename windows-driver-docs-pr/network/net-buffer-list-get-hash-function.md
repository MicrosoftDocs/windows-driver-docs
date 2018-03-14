---
title: NET_BUFFER_LIST_GET_HASH_FUNCTION macro
author: windows-driver-content
description: The NET_BUFFER_LIST_GET_HASH_FUNCTION macro gets the hash function information from a NET_BUFFER_LIST structure. Version Information Windows VistaSupported. NDIS 6.0 driversSupported.
ms.assetid: bb80344c-8f82-4446-9f6f-8c2d4cabfd5a
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_GET_HASH_FUNCTION macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_GET\_HASH\_FUNCTION macro


The NET\_BUFFER\_LIST\_GET\_HASH\_FUNCTION macro gets the hash function information from a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

**Version Information**

<a href="" id="windows-vista"></a>Windows Vista  
Supported.

<a href="" id="ndis-6-0-drivers"></a>NDIS 6.0 drivers  
Supported.

Syntax
------

```ManagedCPlusPlus
ULONG NET_BUFFER_LIST_GET_HASH_FUNCTION(
   PNET_BUFFER_LIST NetBufferList
);
```

Parameters
----------

*NetBufferList*   
A pointer to a NET\_BUFFER\_LIST structure.

Return value
------------

NET\_BUFFER\_LIST\_GET\_HASH\_FUNCTION returns the hash function used. For more information, see [RSS Hashing Functions](https://msdn.microsoft.com/library/windows/hardware/ff570725).

The hash function can be one of the following values:

**NdisHashFunctionToeplitz**

**NdisHashFunctionReserved1**

**NdisHashFunctionReserved2**

**NdisHashFunctionReserved3**

## <a href="" id="ddk-net-buffer-list-get-hash-function-nr"></a>


Remarks
-------

A NIC (or its miniport driver) uses the receive side scaling (RSS) hashing function to calculate an RSS hash value.

For more information about the hashing functions, see [RSS Hashing Functions](https://msdn.microsoft.com/library/windows/hardware/ff570725).

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

 

 




