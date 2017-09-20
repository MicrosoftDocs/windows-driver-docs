---
title: NET_ADAPTER_DATAPATH_CAPABILITIES_INIT method
topic_type:
- apiref
api_name:
- NET_ADAPTER_DATAPATH_CAPABILITIES_INIT
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_DATAPATH_CAPABILITIES_INIT method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes the [**NET_ADAPTER_DATAPATH_CAPABILITIES**](net-adapter-datapath-capabilities.md) structure.

Syntax
------

```cpp
FORCEINLINE VOID NET_ADAPTER_DATAPATH_CAPABILITIES_INIT(
  _Out_ PNET_ADAPTER_DATAPATH_CAPABILITIES DataPathCapabilities
);
```

Parameters
----------

*DataPathCapabilities* [out]  
A pointer to the driver-allocated [**NET_ADAPTER_DATAPATH_CAPABILITIES**](net-adapter-datapath-capabilities.md) structure.

Return value
------------

This method does not return a value.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 10</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netadapter.h</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NetAdapterSetDataPathCapabilities**](netadaptersetdatapathcapabilities.md)

 

 






