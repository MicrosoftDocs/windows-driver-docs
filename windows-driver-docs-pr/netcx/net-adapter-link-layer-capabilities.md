---
title: NET\_ADAPTER\_LINK\_LAYER\_CAPABILITIES structure
description: Describes the MAC capabilities of the adapter.
ms.assetid: 600211c2-e502-4c9f-b1ab-5fb5239b6652
keywords: ["NET_ADAPTER_LINK_LAYER_CAPABILITIES structure Network Drivers Starting with Windows Vista", "PNET_ADAPTER_LINK_LAYER_CAPABILITIES structure pointer Network Drivers Starting with Windows Vista"]
---

# NET\_ADAPTER\_LINK\_LAYER\_CAPABILITIES structure


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

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
TBD

**MaxRxLinkSpeed**  
TBD

Remarks
-------

The client driver passes an initialized **NET\_ADAPTER\_LINK\_LAYER\_CAPABILITIES** structure as an input parameter value to [**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md).

Call [**NET\_ADAPTER\_LINK\_LAYER\_CAPABILITIES\_INIT**](netvista-net_adapter_link_layer_capabilities_init) to initialize this structure.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_ADAPTER_LINK_LAYER_CAPABILITIES%20structure%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




