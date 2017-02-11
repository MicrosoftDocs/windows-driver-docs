---
title: NetAdapterGetNetLuid method
topic_type:
- apiref
api_name:
- NetAdapterGetNetLuid
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NetAdapterGetNetLuid method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the NET_LUID that is assigned to a net adapter.

Syntax
------

```ManagedCPlusPlus
NET_LUID NetAdapterGetNetLuid(
  _In_ NETADAPTER Adapter
);
```

Parameters
----------

*Adapter* \[in\]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

Return value
------------

Returns the NET_LUID for the specified net adapter object.

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
<td align="left">Netadapter.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NET_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff568747)

 

 






