---
title: NetRequestGetVPortId method
description: .
ms.assetid: d4a49f40-6f8b-42df-b7a2-b6978953ac42
keywords: ["NetRequestGetVPortId method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetRequestGetVPortId
api_location:
- netrequest.h
api_type:
- HeaderDef
---

# NetRequestGetVPortId method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the VPortId for the NETREQUEST.

Syntax
------

```ManagedCPlusPlus
NDIS_NIC_SWITCH_VPORT_ID NetRequestGetVPortId(
  _In_ NETREQUEST Request
);
```

Parameters
----------

*Request* \[in\]  
A handle to a network request object.

Return value
------------

Returns an NDIS_NIC_SWITCH_VPORT_ID value that specifies the identifier associated with the net request object. 

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

 

 





