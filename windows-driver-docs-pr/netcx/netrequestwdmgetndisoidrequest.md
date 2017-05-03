---
title: NetRequestWdmGetNdisOidRequest method
topic_type:
- apiref
api_name:
- NetRequestWdmGetNdisOidRequest
api_location:
- netrequest.h
api_type:
- HeaderDef
---

# NetRequestWdmGetNdisOidRequest method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the traditional WDM [**NDIS_OID_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure for the NETREQUEST.

Syntax
------

```cpp
PNDIS_OID_REQUEST NetRequestWdmGetNdisOidRequest(
  _In_ NETREQUEST Request
);
```

Parameters
----------

*Request* [in]  
A handle to a network request object.

Return value
------------

Pointer to the [**NDIS_OID_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure.

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
<td align="left"><p>&lt;=DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





