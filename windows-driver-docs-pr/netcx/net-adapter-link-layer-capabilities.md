---
title: NET_ADAPTER_LINK_LAYER_CAPABILITIES structure
---

# NET\_ADAPTER\_LINK\_LAYER\_CAPABILITIES structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Describes the MAC capabilities of the adapter.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_ADAPTER_LINK_LAYER_CAPABILITIES {
  ULONG                         Size;
  NET_PACKET_FILTER_TYPES_FLAGS SupportedPacketFilters;
  ULONG                         MaxMulticastListSize;
  NET_ADAPTER_PHYSICAL_ADDRESS  PhysicalAddress;
  NET_ADAPTER_STATISTICS_FLAGS  SupportedStatistics;
  ULONG64                       MaxTxLinkSpeed;
  ULONG64                       MaxRxLinkSpeed;
} NET_ADAPTER_LINK_LAYER_CAPABILITIES, *PNET_ADAPTER_LINK_LAYER_CAPABILITIES;
```

Members
-------

**Size**  
Size of this structure in bytes.

**SupportedPacketFilters**  
Indicates the packet filters that the adapter supports. This value is a bitwise OR of [**NET\_PACKET\_FILTER\_TYPES\_FLAGS**](net-packet-filter-types-flags.md)-typed flags.

**MaxMulticastListSize**  
The multicast address list size for the adapter.

**PhysicalAddress**  
A [**NET\_ADAPTER\_PHYSICAL\_ADDRESS**](net-adapter-physical-address.md) structure that specifies the physical (MAC) address of the adapter.

**SupportedStatistics**  
The statistics that the adapter supports. This value is a bitwise OR of [**NET\_ADAPTER\_STATISTICS\_FLAGS**](net-adapter-statistics-flags.md)-typed flags.

**MaxTxLinkSpeed**  
The maximum transmit link speed of the adapter in bits per second. For more information, see [**OID_GEN_MAX_LINK_SPEED**](https://msdn.microsoft.com/library/windows/hardware/ff569602).

**MaxRxLinkSpeed**  
The maximum receive link speed of the adapter in bits per second. For more information, see [**OID_GEN_MAX_LINK_SPEED**](https://msdn.microsoft.com/library/windows/hardware/ff569602).

Remarks
-------

The client driver passes an initialized **NET\_ADAPTER\_LINK\_LAYER\_CAPABILITIES** structure as an input parameter value to [**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md).

Call [**NET\_ADAPTER\_LINK\_LAYER\_CAPABILITIES\_INIT**](net-adapter-link-layer-capabilities-init.md) to initialize this structure.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netadapter.h</td>
</tr>
</tbody>
</table>

 

 





