---
title: NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT method
description: Initializes a NET_ADAPTER_LINK_LAYER_CAPABILITIES structure.
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

*LinkLayerCapabilities* \[out\]  

*LinkSSupportedPacketFilterspeed* \[in\]  

*MaxMulticastListSize* \[in\]  

*SupportedStatistics* \[in\]  

*MaxTxLinkSpeed* \[in\]  

*MaxRxLinkSpeed* \[in\]  

*PhysicalAddressLength* \[in\]  
*PermanentPhysicalAddress* \[in\]  
*CurrentPhysicalAddress* \[in\]  


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

 






