---
title: NetRequestGetId method
topic_type:
- apiref
api_name:
- NetRequestGetId
api_location:
- netrequest.h
api_type:
- HeaderDef
---

# NetRequestGetId method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the NDIS_OID identifier associated with the specified network request object.

Syntax
------

```ManagedCPlusPlus
NDIS_OID NetRequestGetId(
  _In_ NETREQUEST Request
);
```

Parameters
----------

*Request* \[in\]  
A handle to a network request object.

Return value
------------

Returns the object identifier for the network request object. The value is an OID_XXX code. 

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

 

 





