---
title: NdisSetNetBufferListProtocolId macro
author: windows-driver-content
description: The NdisSetNetBufferListProtocolId macro sets the protocol identifier in the NetBufferListInfo member of a NET_BUFFER_LIST structure.
ms.assetid: e143c914-cfb0-4c06-9da7-a2f5ef09afe2
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NdisSetNetBufferListProtocolId macro Network Drivers Starting with Windows Vista
---

# NdisSetNetBufferListProtocolId macro


The **NdisSetNetBufferListProtocolId** macro sets the protocol identifier in the **NetBufferListInfo** member of a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
VOID NdisSetNetBufferListProtocolId(
    _NBL,
    _ProtocolId
);
```

Parameters
----------

*\_NBL*   
A pointer to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

*\_ProtocolId*   
A protocol identifier, as one of the following values:

<a href="" id="ndis-protocol-id-default"></a>NDIS\_PROTOCOL\_ID\_DEFAULT  
A default protocol driver identifier.

<a href="" id="ndis-protocol-id-tcp-ip"></a>NDIS\_PROTOCOL\_ID\_TCP\_IP  
The TCP/IP protocol.

<a href="" id="ndis-protocol-id-ipx"></a>NDIS\_PROTOCOL\_ID\_IPX  
The IPX protocol.

<a href="" id="ndis-protocol-id-nbf"></a>NDIS\_PROTOCOL\_ID\_NBF  
The NetBEUI protocol.

Return value
------------

None

Remarks
-------

Drivers that create [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures should set the protocol identifier by calling the **NdisSetNetBufferListProtocolId** macro or by associating an identifier with a NET\_BUFFER\_LIST pool.

To associate a protocol identifier with a NET\_BUFFER\_LIST pool, call the [**NdisAllocateNetBufferListPool**](https://msdn.microsoft.com/library/windows/hardware/ff561611) function and specify the protocol identifier in the **ProtocolId** member of the [**NET\_BUFFER\_LIST\_POOL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh205394) structure.

Miniport, filter, and intermediate drivers set the protocol identifier to zero.

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


[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

[**NET\_BUFFER\_LIST\_POOL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh205394)

[**NdisAllocateNetBufferListPool**](https://msdn.microsoft.com/library/windows/hardware/ff561611)

[**NdisGetNetBufferListProtocolId**](https://msdn.microsoft.com/library/windows/hardware/ff562642)

 

 




