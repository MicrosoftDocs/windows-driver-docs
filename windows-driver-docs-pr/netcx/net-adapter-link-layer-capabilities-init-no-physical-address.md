---
title: NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT_NO_PHYSICAL_ADDRESS method
topic_type:
- apiref
api_name:
- NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT_NO_PHYSICAL_ADDRESS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT_NO_PHYSICAL_ADDRESS method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes a [NET_ADAPTER_LINK_LAYER_CAPABILITIES](net-adapter-link-layer-capabilities.md) structure.

Syntax
------

```cpp
FORCEINLINE VOID NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT_NO_PHYSICAL_ADDRESS(
    _Out_ PNET_ADAPTER_LINK_LAYER_CAPABILITIES  LinkLayerCapabilities,
    _In_  NET_PACKET_FILTER_TYPES_FLAGS         SupportedPacketFilters,
    _In_  ULONG                                 MaxMulticastListSize,
    _In_  NET_ADAPTER_STATISTICS_FLAGS          SupportedStatistics,
    _In_  ULONG64                               MaxTxLinkSpeed,
    _In_  ULONG64                               MaxRxLinkSpeed,
    ) 
```

Parameters
----------

*LinkLayerCapabilities* [out]  
A pointer to the driver-allocated [NET_ADAPTER_LINK_LAYER_CAPABILITIES](net-adapter-link-layer-capabilities.md) structure that describes the link layer capabilities of the adapter.

*SupportedPacketFilters* [in]  
An enumeration of type [NET_PACKET_FILTER_TYPES_FLAGS](net-packet-filter-types-flags.md) that specifying packet filters the adapter supports.

*MaxMulticastListSize* [in]  
The multicast address list size for the adapter.

*SupportedStatistics* [in]  
A bitwise OR of [NET_ADAPTER_STATISTICS_FLAGS](net-adapter-statistics-flags.md)-typed flags specifying statistics the adapter supports.

*MaxTxLinkSpeed* [in]  
The maximum transmit link speed of the adapter in bits per second. For more information, see [**OID_GEN_MAX_LINK_SPEED**](https://msdn.microsoft.com/library/windows/hardware/ff569602).

*MaxRxLinkSpeed* [in]  
The maximum receive link speed of the adapter in bits per second. For more information, see [**OID_GEN_MAX_LINK_SPEED**](https://msdn.microsoft.com/library/windows/hardware/ff569602).

Remarks
-----
**NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT** zeroes out the [NET_ADAPTER_LINK_LAYER_CAPABILITIES](net-adapter-link-layer-capabilities.md) structure and then sets all of its members except for **PhysicalAddress**.

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

 






