---
title: NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT method
topic_type:
- apiref
api_name:
- NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT method initializes a [NET_ADAPTER_LINK_LAYER_CAPABILITIES](net-adapter-link-layer-capabilities.md) structure.

Syntax
------

```cpp
FORCEINLINE VOID NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT(
    _Out_ PNET_ADAPTER_LINK_LAYER_CAPABILITIES  LinkLayerCapabilities,
    _In_  NET_PACKET_FILTER_TYPES_FLAGS         SupportedPacketFilters,
    _In_  ULONG                                 MaxMulticastListSize,
    _In_  NET_ADAPTER_STATISTICS_FLAGS          SupportedStatistics,
    _In_  ULONG64                               MaxTxLinkSpeed,
    _In_  ULONG64                               MaxRxLinkSpeed
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
**NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT** zeroes out the [NET_ADAPTER_LINK_LAYER_CAPABILITIES](net-adapter-link-layer-capabilities.md) structure and then sets all of its members.

In NetAdapterCx version 1.1, the *PhysicalAddressLength*, *PermanentPhysicalAddress*, and *CurrentPhysicalAddress* parameters from version 1.0 were removed from this method. Link layer addresses are now initialized with the [NET_ADAPTER_LINK_LAYER_ADDRESS_INIT](net-adapter-link-layer-address-init.md) method and set with the [NetAdapterSetCurrentLinkLayerAddress](netadaptersetcurrentlinklayeraddress.md) method or the [NetAdapterSetPermanentLinkLayerAddress](netadaptersetpermanentlinklayeraddress.md), depending on the type of address.

Example
-----

```cpp
NET_ADAPTER_LINK_LAYER_CAPABILITIES linkLayerCapabilities;
NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT(
      &linkLayerCapabilities,
      NIC_SUPPORTED_FILTERS,
      NIC_MAX_MCAST_LIST,
      NIC_SUPPORTED_STATISTICS,
      maxXmitLinkSpeed,
      maxRcvLinkSpeed);
```

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
<td align="left"><p>Windows 10, version 1709</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netadapter.h (include NetAdapterCx.h) </td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 






