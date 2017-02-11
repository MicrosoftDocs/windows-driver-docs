---
title: NetRequestGetSwitchId method
topic_type:
- apiref
api_name:
- NetRequestGetSwitchId
api_location:
- netrequest.h
api_type:
- HeaderDef
---

# NetRequestGetSwitchId method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the switch identifier for the net request.

Syntax
------

```ManagedCPlusPlus
NDIS_NIC_SWITCH_ID NetRequestGetSwitchId(
  _In_ NETREQUEST Request
);
```

Parameters
----------

*Request* \[in\]  
A handle to a network request object.

Return value
------------

Returns an NDIS_NIC_SWITCH_ID value that specifies a switch identifier. The switch identifier is an integer between zero and the number of switches that the network adapter supports. An NDIS_DEFAULT_SWITCH_ID value indicates the default network adapter switch. 

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
<td align="left">Netrequest.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





