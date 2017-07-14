---
title: NdisSetNetBufferListProtocolId macro
description: The NdisSetNetBufferListProtocolId macro sets the protocol identifier in the NetBufferListInfo member of a NET\_BUFFER\_LIST structure.
MS-HAID:
- 'ndis\_netbuf\_macros\_ref\_aaa04a11-5651-4dbb-ac5f-9d77f0fee6a1.xml'
- 'netvista.ndissetnetbufferlistprotocolid'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e143c914-cfb0-4c06-9da7-a2f5ef09afe2
keywords: ["NdisSetNetBufferListProtocolId macro Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NdisSetNetBufferListProtocolId
api_location:
- Ndis.h
api_type:
- HeaderDef
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NdisSetNetBufferListProtocolId%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





