---
title: MIB_IPINTERFACE_ROW structure (Windows Drivers)
description: Learn more about the MIB_IPINTERFACE_ROW structure.
keywords:
- MIB_IPINTERFACE_ROW
- PMIB_IPINTERFACE_ROW
- netioapi/MIB_IPINTERFACE_ROW
- netioapi/PMIB_IPINTERFACE_ROW
ms.date: 10/25/2022
ms.topic: reference
---

# MIB\_IPINTERFACE\_ROW structure

The MIB\_IPINTERFACE\_ROW structure stores interface management information for a particular IP address family on a network interface.

## Syntax

``` c++
typedef struct _MIB_IPINTERFACE_ROW {
  ADDRESS_FAMILY                 Family;
  NET_LUID                       InterfaceLuid;
  NET_IFINDEX                    InterfaceIndex;
  ULONG                          MaxReassemblySize;
  ULONG64                        InterfaceIdentifier;
  ULONG                          MinRouterAdvertisementInterval;
  ULONG                          MaxRouterAdvertisementInterval;
  BOOLEAN                        AdvertisingEnabled;
  BOOLEAN                        ForwardingEnabled;
  BOOLEAN                        WeakHostSend;
  BOOLEAN                        WeakHostReceive;
  BOOLEAN                        UseAutomaticMetric;
  BOOLEAN                        UseNeighborUnreachabilityDetection;
  BOOLEAN                        ManagedAddressConfigurationSupported;
  BOOLEAN                        OtherStatefulConfigurationSupported;
  BOOLEAN                        AdvertiseDefaultRoute;
  NL_ROUTER_DISCOVERY_BEHAVIOR   RouterDiscoveryBehavior;
  ULONG                          DadTransmits;
  ULONG                          BaseReachableTime;
  ULONG                          RetransmitTime;
  ULONG                          PathMtuDiscoveryTimeout;
  NL_LINK_LOCAL_ADDRESS_BEHAVIOR LinkLocalAddressBehavior;
  ULONG                          LinkLocalAddressTimeout;
  ULONG                          ZoneIndices[ScopeLevelCount];
  ULONG                          SitePrefixLength;
  ULONG                          Metric;
  ULONG                          NlMtu;
  BOOLEAN                        Connected;
  BOOLEAN                        SupportsWakeUpPatterns;
  BOOLEAN                        SupportsNeighborDiscovery;
  BOOLEAN                        SupportsRouterDiscovery;
  ULONG                          ReachableTime;
  NL_INTERFACE_OFFLOAD_ROD       TransmitOffload;
  NL_INTERFACE_OFFLOAD_ROD       ReceiveOffload;
  BOOLEAN                        DisableDefaultRoutes;
} MIB_IPINTERFACE_ROW, *PMIB_IPINTERFACE_ROW;
```

## Members

- **Family**  
   The address family. Possible values for the address family are listed in the Winsock2.h header file. Note that the values for the AF\_ address family and PF\_ protocol family constants are identical (for example, AF\_INET and PF\_INET), so you can use either constant.

   On Windows Vista and later versions of the Windows operating systems, possible values for this member are defined in the Ws2def.h header file. Note that the Ws2def.h header file is automatically included in Netioapi.h and you should never use Ws2def.h directly.

   The following values are currently supported:

    - AF\_INET  
      The IPv4 address family.

    - AF\_INET6  
       The IPv6 address family.

    - AF\_UNSPEC  
       The address family is unspecified.

- **InterfaceLuid**  
   The locally unique identifier (LUID) for the network interface.

- **InterfaceIndex**  
   The local index value for the network interface. This index value might change when a network adapter is disabled and then enabled, or under other circumstances, and should not be considered persistent.

- **MaxReassemblySize**  
   The maximum reassembly size, in bytes, of a fragmented IP packet. This member is currently set to zero and reserved for future use.

- **InterfaceIdentifier**  
   Reserved for future use. This member is currently set to zero.

- **MinRouterAdvertisementInterval**  
   The minimum router advertisement interval, in milliseconds, on this IP interface. This member defaults to 200 for IPv6. This member is applicable only if the **AdvertisingEnabled** member is set to **TRUE**.

- **MaxRouterAdvertisementInterval**  
   The maximum router advertisement interval, in milliseconds, on this IP interface. This member defaults to 600 for IPv6. This member is applicable only if the **AdvertisingEnabled** member is set to **TRUE**.

- **AdvertisingEnabled**  
   A value that indicates if router advertising is enabled on this IP interface. The default for IPv6 is that router advertisement is enabled only if the interface is configured to act as a router. The default for IPv4 is that router advertisement is disabled.

- **ForwardingEnabled**  
   A value that indicates if IP forwarding is enabled on this IP interface.

- **WeakHostSend**  
   A value that indicates if weak host send mode is enabled on this IP interface.

- **WeakHostReceive**  
   A value that indicates if weak host receive mode is enabled on this IP interface.

- **UseAutomaticMetric**  
   A value that indicates if the IP interface uses automatic metric.

- **UseNeighborUnreachabilityDetection**  
   A value that indicates if neighbor unreachability detection is enabled on this IP interface.

- **ManagedAddressConfigurationSupported**  
   A value that indicates if the IP interface supports managed address configuration by using DHCP.

- **OtherStatefulConfigurationSupported**  
   A value that indicates if the IP interface supports other stateful configuration (for example, route configuration).

- **AdvertiseDefaultRoute**  
   A value that indicates if the IP interface advertises the default route. This member is applicable only if the **AdvertisingEnabled** member is set to **TRUE**.

- **RouterDiscoveryBehavior**  
   An [**NL\_ROUTER\_DISCOVERY\_BEHAVIOR**](/windows/win32/api/nldef/ne-nldef-nl_router_discovery_behavior) router discovery behavior type.

- **DadTransmits**  
   The number of consecutive messages that are sent while the driver performs duplicate address detection on a tentative IP unicast address. A value of zero indicates that duplicate address detection is not performed on tentative IP addresses. A value of one indicates a single transmission with no follow up retransmissions. For IPv4, the default value for this member is 3. For IPv6, the default value for this member is 1. For IPv6, these messages are sent as IPv6 Neighbor Solicitation (NS) requests. This member is defined as DupAddrDetectTransmits in RFC 2462. For more information, see IPv6 ["Stateless Address Autoconfiguration"](https://go.microsoft.com/fwlink/p/?linkid=84044).

- **BaseReachableTime**  
   The base for random reachable time, in milliseconds. The member is described in RFC 2461. For more information, see ["Neighbor Discovery for IP Version 6 (IPv6)"](https://go.microsoft.com/fwlink/p/?linkid=84044).

- **RetransmitTime**  
   The IPv6 Neighbor Solicitation (NS) time-out, in milliseconds. The member is described in RFC 2461. For more information, see ["Neighbor Discovery for IP Version 6 (IPv6)"](https://go.microsoft.com/fwlink/p/?linkid=84044).

- **PathMtuDiscoveryTimeout**  
   The path MTU discovery time-out, in milliseconds.

- **LinkLocalAddressBehavior**  
   A [**NL\_LINK\_LOCAL\_ADDRESS\_BEHAVIOR**](/windows/win32/api/nldef/ne-nldef-nl_link_local_address_behavior) link local address behavior type.

- **LinkLocalAddressTimeout**  
   The link local IP address time-out, in milliseconds.

- **ZoneIndices**  
   An array that specifies the zone part of scope IDs.

- **SitePrefixLength**  
   The site prefix length, in bits, of the IP interface address. The length, in bits, of the site prefix or network part of the IP interface address. For an IPv4 address, any value that is greater than 32 is an illegal value. For an IPv6 address, any value that is greater than 128 is an illegal value. A value of 255 is typically used to represent an illegal value.

- **Metric**  
   The interface metric. Note that the actual route metric that is used to compute the route preference is the summation of the route metric offset that is specified in the **Metric** member of the [**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md) structure and the interface metric that is specified in this member.

- **NlMtu**  
   The network layer MTU size, in bytes.

- **Connected**  
   A value that indicates if the interface is connected to a network access point.

- **SupportsWakeUpPatterns**  
   A value that specifies if the network interface supports Wake on LAN.

- **SupportsNeighborDiscovery**  
   A value that specifies if the IP interface support neighbor discovery.

- **SupportsRouterDiscovery**  
   A value that specifies if the IP interface support neighbor discovery.

- **ReachableTime**  
   The base for random reachable time, in milliseconds. The member is described in RFC 2461. For more information, see [Neighbor Discovery for IP Version 6 (IPv6)](https://go.microsoft.com/fwlink/p/?linkid=84044).

- **TransmitOffload**  
   A set of flags that indicate the transmit offload capabilities for the IP interface. The NL\_INTERFACE\_OFFLOAD\_ROD structure is defined in the Nldef.h header file.

- **ReceiveOffload**  
   A set of flags that indicate the receive offload capabilities for the IP interface. The NL\_INTERFACE\_OFFLOAD\_ROD structure is defined in the Nldef.h header file.

- **DisableDefaultRoutes**  
   A value that indicates if using default route on the interface should be disabled. VPN clients can use this member to restrict split tunneling.

## Remarks

The **Family**, **InterfaceLuid**, and **InterfaceIndex** members uniquely identify a MIB\_IPINTERFACE\_ROW entry.

When a unicast packet arrives at a host, IP must determine whether the packet is locally destined (its destination matches an address that is assigned to an interface of the host). IP implementations that follow a weak host model accept any locally destined packet, regardless of the interface that the packet was received on. IP implementations that follow the strong host model accept only locally destined packets if the destination address in the packet matches an address that is assigned to the interface that the packet was received on. The weak host model provides better network connectivity. However, it also makes hosts susceptible to multihome-based network attacks.

The current IPv4 implementation in the Windows Server 2003 and Windows XP operating systems uses the weak host model. The TCP/IP stack on Windows Vista and later versions of the Windows operating systems supports the strong host model for both IPv4 and IPv6 and is configured to use the strong host mode by default (the **WeakHostReceive** and **WeakHostSend** members are set to **FALSE**). You can configure the TCP/IP stack on Windows Vista and later to use a weak host model.

A metric is a value that is assigned to an IP route for a particular network interface that identifies the cost that is associated with using that route. For example, the metric can be valued in terms of link speed, hop count, or time delay. Automatic metric is a feature on Windows XP and later that automatically configures the metric for the local routes that are based on link speed. By default, the automatic metric feature is enabled (the **UseAutomaticMetric** is set to **TRUE**) on Windows XP and later. You can also manually configure this feature to assign a specific metric to an IP route.

The automatic metric feature can be useful when the routing table contains multiple routes for the same destination. For example, a computer that has a 10 megabit network interface and a 100 megabit network interface has a default gateway that is configured on both network interfaces. When **UseAutomaticMetric** is **TRUE**, this feature can force all traffic that is destined for the Internet, for example, to use the fastest network interface that is available.

The interface metric that is specified in the **Metric** member represents only the metric for the interface. The complete routing metric is a combination of this interface metric added to the route metric offset that is specified in the **Metric** member of the MIB\_IPFORWARD\_ROW2 structure of a route entry that is specified on this interface.

Unprivileged simultaneous access to multiple networks of different security requirements creates a security hole and enables an unprivileged driver to accidentally relay data between the two networks. A typical example is simultaneous access to a virtual private network (VPN) and the Internet. Windows Server 2003 and Windows XP use a weak host model, where Remote Access Service (RAS) prevents such simultaneous access by increasing the route metric of all default routes over other interfaces. Therefore, all traffic is routed through the VPN interface, disrupting other network connectivity.

On Windows Vista and later, by default, a strong host model is used. If a source IP address is specified in the route lookup by using the [**GetBestRoute2**](getbestroute2.md) function, the route lookup is restricted to the interface of the source IP address. The route metric modification by RAS has no effect because the list of potential routes does not even have the route for the VPN interface, which enables traffic to the Internet. Your driver can use the **DisableDefaultRoutes** member of the MIB\_IPINTERFACE\_ROW structure to disable using the default route on an interface. VPN clients can use this member as a security measure to restrict split tunneling when split tunneling is not required by the VPN client. A VPN client can call the [**SetIpInterfaceEntry**](setipinterfaceentry.md) function to set the **DisableDefaultRoutes** member to **TRUE** when it is required. A VPN client can query the current state of the **DisableDefaultRoutes** member by calling the [**GetIpInterfaceEntry**](getipinterfaceentry.md) function.

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

[**GetBestRoute2**](getbestroute2.md)

[**GetIpInterfaceEntry**](getipinterfaceentry.md)

[**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md)

[**MIB\_IPINTERFACE\_TABLE**](mib-ipinterface-table.md)

[**NET\_LUID**](net-luid-value.md)

[**NL\_LINK\_LOCAL\_ADDRESS\_BEHAVIOR**](/windows/win32/api/nldef/ne-nldef-nl_link_local_address_behavior)

[**NL\_ROUTER\_DISCOVERY\_BEHAVIOR**](/windows/win32/api/nldef/ne-nldef-nl_router_discovery_behavior)

[**SetIpInterfaceEntry**](setipinterfaceentry.md)
