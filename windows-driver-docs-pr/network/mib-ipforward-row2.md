---
title: MIB_IPFORWARD_ROW2 structure (Windows Drivers)
description: Learn more about the MIB_IPFORWARD_ROW2 structure.
keywords:
- MIB_IPFORWARD_ROW2
- PMIB_IPFORWARD_ROW2
- netioapi/MIB_IPFORWARD_ROW2
- netioapi/PMIB_IPFORWARD_ROW2
ms.date: 10/25/2022
---

# MIB\_IPFORWARD\_ROW2 structure

The MIB\_IPFORWARD\_ROW2 structure stores information about an IP route entry.

## Syntax

``` c++
typedef struct _MIB_IPFORWARD_ROW2 {
  NET_LUID          InterfaceLuid;
  NET_IFINDEX       InterfaceIndex;
  IP_ADDRESS_PREFIX DestinationPrefix;
  SOCKADDR_INET     NextHop;
  UCHAR             SitePrefixLength;
  ULONG             ValidLifetime;
  ULONG             PreferredLifetime;
  ULONG             Metric;
  NL_ROUTE_PROTOCOL Protocol;
  BOOLEAN           Loopback;
  BOOLEAN           AutoconfigureAddress;
  BOOLEAN           Publish;
  BOOLEAN           Immortal;
  ULONG             Age;
  NL_ROUTE_ORIGIN   Origin;
} MIB_IPFORWARD_ROW2, *PMIB_IPFORWARD_ROW2;
```

## Members

- **InterfaceLuid**  
   The locally unique identifier (LUID) for the network interface that is associated with this IP route entry.

- **InterfaceIndex**  
   The local index value for the network interface that is associated with this IP route entry. This index value might change when a network adapter is disabled and then enabled, or under other circumstances, and should not be considered persistent.

- **DestinationPrefix**  
   The IP address prefix for the destination IP address for this route.

- **NextHop**  
   For a remote route, the IP address of the next system or gateway that is along the route. If the route is to a local loopback address or an IP address on the local link, the next hop is unspecified (all zeros). For a local loopback route, this member should be an IPv4 address of 0.0.0.0 for an IPv4 route entry or an IPv6 address address of 0::0 for an IPv6 route entry.

- **SitePrefixLength**  
   The length, in bits, of the site prefix or network part of the IP address for this route. For an IPv4 route entry, any value that is greater than 32 is an illegal value. For an IPv6 route entry, any value that is greater than 128 is an illegal value. A value of 255 is typically used to represent an illegal value.

- **ValidLifetime**  
   The maximum time, in seconds, that the IP route entry is valid. A value of 0xffffffff is considered to be infinite.

- **PreferredLifetime**  
   The preferred time, in seconds, that the IP route entry is valid. A value of 0xffffffff is considered to be infinite.

- **Metric**  
   The route metric offset value for this IP route entry. Note the actual route metric that is used to compute the route preference is the interface metric that is specified in the **Metric** member of the [**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md) structure added to the route metric offset that is specified in this **Metric** member. The semantics of this metric are determined by the routing protocol that is specified in the **Protocol** member. If this metric is not used, its value should be set to -1. This value is documented in RFC 4292. For more information, see [IP Forwarding Table MIB](https://go.microsoft.com/fwlink/p/?linkid=84065).

- **Protocol**  
   The [**NL\_ROUTE\_PROTOCOL**](/windows/win32/api/nldef/ne-nldef-nl_route_protocol) routing mechanism type that this IP route was added with.

- **Loopback**  
   A value that specifies if the route is a loopback route (the gateway is on the local host).

- **AutoconfigureAddress**  
   A value that specifies if the IP address is autoconfigured.

- **Publish**  
   A value that specifies if the route is published.

- **Immortal**  
   A value that specifies if the route is immortal.

- **Age**  
   The number of seconds since the route was added or modified in the network routing table.

- **Origin**  
   A [**NL\_ROUTE\_ORIGIN**](/windows/win32/api/nldef/ne-nldef-nl_route_origin) IP route origin type.

## Remarks

The [**GetIpForwardTable2**](getipforwardtable2.md) function enumerates the IP route entries on a local computer and returns this information in a [**MIB\_IPFORWARD\_TABLE2**](mib-ipforward-table2.md) structure as an array of MIB\_IPFORWARD\_ROW2 entries.

The **GetIpForwardEntry2** function retrieves a single IP route entry and returns this information in a MIB\_IPFORWARD\_ROW2 structure.

An entry with the **Prefix** and the **PrefixLength** members of [**IP\_ADDRESS\_PREFIX**](ip-address-prefix.md) set to zero in the **DestinationPrefix** member in the MIB\_IPFORWARD\_ROW2 structure is considered a default route. The [**MIB\_IPFORWARD\_TABLE2**](mib-ipforward-table2.md) might contain multiple MIB\_IPFORWARD\_ROW2 entries with the **Prefix** and the **PrefixLength** members of the IP\_ADDRESS\_PREFIX set to zero in the **DestinationPrefix** member when there are multiple network adapters installed.

The **Metric** member of a MIB\_IPFORWARD\_ROW2 entry is a value that is assigned to an IP route for a particular network interface that identifies the cost that is associated with using that route. For example, the metric can be valued in terms of link speed, hop count, or time delay. Automatic metric is a feature on Windows XP and later versions of the Windows operating systems that automatically configures the metric for the local routes that are based on link speed. By default, the automatic metric feature is enabled (the **UseAutomaticMetric** member of the MIB\_IPINTERFACE\_ROW structure is set to **TRUE**) on Windows XP and later. You can also manually configure this feature to assign a specific metric to an IP route.

The route metric that is specified in the **Metric** member of the MIB\_IPFORWARD\_ROW2 structure represents only the route metric offset. The complete metric is a combination of this route metric offset added to the interface metric that is specified in the **Metric** member of the [**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md) structure of the associated interface. A driver can retrieve the interface metric by calling the [**GetIpInterfaceEntry**](getipinterfaceentry.md) function.

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Netioapi.h (include Netioapi.h)</td>
</tr>
</tbody>
</table>

## See also

[**CreateIpForwardEntry2**](createipforwardentry2.md)

[**DeleteIpForwardEntry2**](deleteipforwardentry2.md)

[**GetIpForwardEntry2**](getipforwardentry2.md)

[**GetIpForwardTable2**](getipforwardtable2.md)

[**GetIpInterfaceEntry**](getipinterfaceentry.md)

[**IP\_ADDRESS\_PREFIX**](ip-address-prefix.md)

[**MIB\_IPFORWARD\_TABLE2**](mib-ipforward-table2.md)

[**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md)

[**NL\_ROUTE\_ORIGIN**](/windows/win32/api/nldef/ne-nldef-nl_route_origin)

[**NL\_ROUTE\_PROTOCOL**](/windows/win32/api/nldef/ne-nldef-nl_route_protocol)

[**SetIpForwardEntry2**](setipforwardentry2.md)
