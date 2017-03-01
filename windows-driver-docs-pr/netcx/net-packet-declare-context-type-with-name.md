---
title: NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME macro
topic_type:
- apiref
api_name:
- NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME
api_location:
- netadapterpacket.h
api_type:
- HeaderDef
---

# NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME macro


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME macro creates an accessor method with a specified name for a client driver's object-specific context space.

Syntax
------

```cpp
void NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME(
    _contexttype,
    _castingfunction
);
```

Parameters
----------

*_contexttype*   
The structure type name of a driver-defined structure that describes the contents of an object's context space.

*_castingfunction*   
A C-language routine name. The macro uses this name as the name for the accessor method that it creates for the object's context space.

Return value
------------

This macro does not return a value.

Remarks
-------

You can use NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME to define one context per packet.

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
</tbody>
</table>

## See also


[**NetPacketGetTypedContext**](netpacketgettypedcontext.md)

[**WDF_DECLARE_CONTEXT_TYPE_WITH_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551252)

 

 






