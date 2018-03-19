---
title: NET_BUFFER_LIST_SET_HASH_TYPE macro
author: windows-driver-content
description: The NET_BUFFER_LIST_SET_HASH_TYPE macro sets the hash type information in a NET_BUFFER_LIST structure. Version Information Windows VistaSupported. NDIS 6.0 driversSupported.
ms.assetid: 46bd8e4b-3c52-4708-ac13-05f54ac28869
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_SET_HASH_TYPE macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_SET\_HASH\_TYPE macro


The NET\_BUFFER\_LIST\_SET\_HASH\_TYPE macro sets the hash type information in a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

**Version Information**

<a href="" id="windows-vista"></a>Windows Vista  
Supported.

<a href="" id="ndis-6-0-drivers"></a>NDIS 6.0 drivers  
Supported.

Syntax
------

```ManagedCPlusPlus
VOID NET_BUFFER_LIST_SET_HASH_TYPE(
  [in] PNET_BUFFER_LIST          NetBufferList,
  [in] ULONG            volatile HashType
);
```

Parameters
----------

*NetBufferList* \[in\]  
A pointer to a NET\_BUFFER\_LIST structure.

*HashType* \[in\]  
The hash type.

The hash type is an OR value of valid combinations of the following flags:

NDIS\_HASH\_IPV4

NDIS\_HASH\_TCP\_IPV4

NDIS\_HASH\_IPV6

NDIS\_HASH\_TCP\_IPV6

NDIS\_HASH\_IPV6\_EX

NDIS\_HASH\_TCP\_IPV6\_EX

For more information about hash types and the valid combinations of these flags, see [RSS Hashing Types](https://msdn.microsoft.com/library/windows/hardware/ff570726).

Return value
------------

None

## <a href="" id="ddk-net-buffer-list-set-hash-type-nr"></a>


Remarks
-------

A NIC (or its miniport driver) uses the receive side scaling (RSS) hash type to identify the portion of received network data that is used to calculate an RSS hash value.

For more information about the hash type, see [RSS Hashing Types](https://msdn.microsoft.com/library/windows/hardware/ff570726).

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

 

 




