---
title: NET_BUFFER_LIST_SET_HASH_FUNCTION macro
author: windows-driver-content
description: The NET_BUFFER_LIST_SET_HASH_FUNCTION macro sets the hash function information in a NET_BUFFER_LIST structure. Version InformationWindows VistaSupported. NDIS 6.0 driversSupported.
ms.assetid: 01257316-b037-4e7a-8084-d2cc8ad2a55a
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_SET_HASH_FUNCTION macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_SET\_HASH\_FUNCTION macro


The NET\_BUFFER\_LIST\_SET\_HASH\_FUNCTION macro sets the hash function information in a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

**Version Information**

<a href="" id="windows-vista"></a>Windows Vista  
Supported.

<a href="" id="ndis-6-0-drivers"></a>NDIS 6.0 drivers  
Supported.

Syntax
------

```ManagedCPlusPlus
VOID NET_BUFFER_LIST_SET_HASH_FUNCTION(
  [in] PNET_BUFFER_LIST          NetBufferList,
  [in] ULONG            volatile HashFunctionUsed
);
```

Parameters
----------

*NetBufferList* \[in\]  
A pointer to a NET\_BUFFER\_LIST structure.

*HashFunctionUsed* \[in\]  
The hash function that is used. For more information, see [RSS Hashing Functions](https://msdn.microsoft.com/library/windows/hardware/ff570725).

The hash function can be one of the following:

**NdisHashFunctionToeplitz**

**NdisHashFunctionReserved1**

**NdisHashFunctionReserved2**

**NdisHashFunctionReserved3**

Return value
------------

None

## <a href="" id="ddk-net-buffer-list-set-hash-function-nr"></a>


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

 

 




