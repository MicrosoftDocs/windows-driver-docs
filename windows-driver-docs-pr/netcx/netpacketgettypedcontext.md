---
title: NetPacketGetTypedContext method
topic_type:
- apiref
api_name:
- NetPacketGetTypedContext
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetPacketGetTypedContext method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Client drivers should not call this function directly. Instead, use [**NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME**](net-packet-declare-context-type-with-name.md).

Syntax
------

```ManagedCPlusPlus
PVOID NetPacketGetTypedContext(
  _In_ NET_PACKET              *NetPacket,
  _In_ PCNET_CONTEXT_TYPE_INFO TypeInfo
);
```

Parameters
----------

*NetPacket* [in]  

*TypeInfo* [in]  

Return value
------------

Returns a pointer to the packet's context space.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Universal</td>
</tr>
<tr class="even">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Netadapterpacket.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>Library</p></td>
<td align="left">NetAdapterCxStub.lib</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME**](net-packet-declare-context-type-with-name.md)

 

 






