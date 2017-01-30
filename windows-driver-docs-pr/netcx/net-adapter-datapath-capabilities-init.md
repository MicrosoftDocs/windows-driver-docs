---
title: NET_ADAPTER_DATAPATH_CAPABILITIES_INIT method
description: Initializes the NET\_ADAPTER\_DATAPATH\_CAPABILITIES structure.
ms.assetid: 9fc99964-6e86-4c6d-8f1a-dca532c1aef2
keywords: ["NET_ADAPTER_DATAPATH_CAPABILITIES_INIT method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_DATAPATH_CAPABILITIES_INIT
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_DATAPATH\_CAPABILITIES\_INIT method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes the [**NET\_ADAPTER\_DATAPATH\_CAPABILITIES**](net-adapter-datapath-capabilities.md) structure.

Syntax
------

```ManagedCPlusPlus
FORCEINLINE VOID NET_ADAPTER_DATAPATH_CAPABILITIES_INIT(
  _Out_ PNET_ADAPTER_DATAPATH_CAPABILITIES DataPathCapabilities
);
```

Parameters
----------

*DataPathCapabilities* \[out\]  
A pointer to the driver-allocated [**NET\_ADAPTER\_DATAPATH\_CAPABILITIES**](net-adapter-datapath-capabilities.md) structure.

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

 

 






