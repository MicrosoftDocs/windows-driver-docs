---
title: NetRequestGetPortNumber method
topic_type:
- apiref
api_name:
- NetRequestGetPortNumber
api_location:
- netrequest.h
api_type:
- HeaderDef
---

# NetRequestGetPortNumber method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the port number for the network request object. 

Syntax
------

```cpp
NDIS_PORT_NUMBER NetRequestGetPortNumber(
  _In_ NETREQUEST Request
);
```

Parameters
----------

*Request* [in]  
A handle to a network request object.

Return value
------------

Returns the port number corresponding to the network request object.  If the port is unknown or default, returns zero.

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

See Also
-----
[**NDIS_OID_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)
