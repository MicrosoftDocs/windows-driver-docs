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

Initializes a [NET_ADAPTER_LINK_LAYER_CAPABILITIES](net-adapter-link-layer-capabilities.md) structure.

Syntax
------

```ManagedCPlusPlus
FORCEINLINE VOID NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT(
    _Out_ PNET_ADAPTER_LINK_LAYER_CAPABILITIES  LinkLayerCapabilities,
    _In_  NET_PACKET_FILTER_TYPES_FLAGS         SupportedPacketFilters,
    _In_  ULONG                                 MaxMulticastListSize,
    _In_  NET_ADAPTER_STATISTICS_FLAGS          SupportedStatistics,
    _In_  ULONG64                               MaxTxLinkSpeed,
    _In_  ULONG64                               MaxRxLinkSpeed,
    _In_range_(1,NDIS_MAX_PHYS_ADDRESS_LENGTH)
          USHORT                                PhysicalAddressLength,
    _In_reads_bytes_(PhysicalAddressLength) 
          PUCHAR                                PermanentPhysicalAddress,
    _In_reads_bytes_(PhysicalAddressLength) 
          PUCHAR                                CurrentPhysicalAddress
    ) 
```

Parameters
----------

*LinkLayerCapabilities* [out]  
A pointer to the driver-allocated [NET_ADAPTER_LINK_LAYER_CAPABILITIES](net-adapter-link-layer-capabilities.md) structure that describes the MAC capabilities of the adapter.

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

*PhysicalAddressLength* [in]  
The MAC address length, in bytes. The MAC address length is specific to the type of media.

*PermanentPhysicalAddress* [in]  
The permanent MAC address. For example, the [**OID_802_3_PERMANENT_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff569074) OID specifies the permanent MAC address for IEEE 802.3 drivers.

*CurrentPhysicalAddress* [in]  
The current MAC address. For example, the [**OID_802_3_CURRENT_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff569069) OID specifies the current MAC address for IEEE 802.3 drivers.

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

 






