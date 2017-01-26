---
title: NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME macro
description: The NET\_PACKET\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME macro creates an accessor method with a specified name for a client driver's object-specific context space.
ms.assetid: 8A8240D4-DE32-4CBE-8AC3-FC19D4963F13
keywords: ["NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME macro Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME
api_location:
- netadapterpacket.h
api_type:
- HeaderDef
---

# NET\_PACKET\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME macro


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NET\_PACKET\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME macro creates an accessor method with a specified name for a client driver's object-specific context space.

Syntax
------

```ManagedCPlusPlus
void NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME(
    _contexttype,
    _castingfunction
);
```

Parameters
----------

*\_contexttype*   
The structure type name of a driver-defined structure that describes the contents of an object's context space.

*\_castingfunction*   
A C-language routine name. The macro uses this name as the name for the accessor method that it creates for the object's context space.

Return value
------------

This macro does not return a value.

Remarks
-------

You can use NET\_PACKET\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME to define one context per packet.

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
</tbody>
</table>

## See also


[**NetPacketGetTypedContext**](netpacketgettypedcontext.md)

[**WDF\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551252)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME%20macro%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





