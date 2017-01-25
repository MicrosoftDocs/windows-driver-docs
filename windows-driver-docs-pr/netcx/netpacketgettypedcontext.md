---
title: NetPacketGetTypedContext method
description: Client drivers should not call this function directly. Instead, use NET\_PACKET\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME.
ms.assetid: 8050e118-ab90-4a65-a9ed-59a408983fce
keywords: ["NetPacketGetTypedContext method Network Drivers Starting with Windows Vista"]
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

Client drivers should not call this function directly. Instead, use [**NET\_PACKET\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME**](net-packet-declare-context-type-with-name.md).

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

*NetPacket* \[in\]  

*TypeInfo* \[in\]  

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
<td align="left">[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
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


[**NET\_PACKET\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME**](net-packet-declare-context-type-with-name.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NetPacketGetTypedContext%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





