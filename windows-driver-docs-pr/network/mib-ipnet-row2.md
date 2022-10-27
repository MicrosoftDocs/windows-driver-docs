---
title: MIB_IPNET_ROW2 structure (Windows Drivers)
description: Learn more about the MIB_IPNET_ROW2 structure.
keywords:
- MIB_IPNET_ROW2
- PMIB_IPNET_ROW2
- netioapi/MIB_IPNET_ROW2
- netioapi/PMIB_IPNET_ROW2
ms.date: 10/25/2022
---

# MIB\_IPNET\_ROW2 structure

The MIB\_IPNET\_ROW2 structure stores information about a neighbor IP address.

## Syntax

``` c++
typedef struct _MIB_IPNET_ROW2 {
  SOCKADDR_INET     Address;
  NET_IFINDEX       InterfaceIndex;
  NET_LUID          InterfaceLuid;
  UCHAR             PhysicalAddress[IF_MAX_PHYS_ADDRESS_LENGTH];
  ULONG             PhysicalAddressLength;
  NL_NEIGHBOR_STATE State;
  union {
    struct {
      BOOLEAN IsRouter  :1;
      BOOLEAN IsUnreachable  :1;
    };
    UCHAR  Flags;
  };
  union {
    ULONG LastReachable;
    ULONG LastUnreachable;
  } ReachabilityTime;
} MIB_IPNET_ROW2, *PMIB_IPNET_ROW2;
```

## Members

- **Address**  
   The neighbor IP address. This member can be an IPv6 address or an IPv4 address.

- **InterfaceIndex**  
   The local index value for the network interface that is associated with this IP address. This index value might change when a network adapter is disabled and then enabled, or under other circumstances, and should not be considered persistent.

- **InterfaceLuid**  
   The locally unique identifier (LUID) for the network interface that is associated with this IP address.

- **PhysicalAddress**  
   The physical hardware address of the adapter for the network interface that is associated with this IP address.

- **PhysicalAddressLength**  
   The length, in bytes, of the physical hardware address that the **PhysicalAddress** member specifies. The maximum value that is supported is 32 bytes.

- **State**  
   An [**NL\_NEIGHBOR\_STATE**](/windows/win32/api/nldef/ne-nldef-nl_neighbor_state) network layer neighbor state type.

- **IsRouter**  
   A value that indicates if this IP address is a router.

- **IsUnreachable**  
   A value that indicates if this IP address is unreachable.

- **Flags**  
   A set of flags that indicate whether the IP address is a router and whether the IP address is unreachable.

- **ReachabilityTime**  
   The time that the node assumes that the neighbor is reachable or unreachable after the node receives information about the reachability of the neighbor.

   This union contains the following members:

    - **LastReachable**  
       The time, in milliseconds, that a node assumes that the neighbor will remain reachable after the node receives a reachability confirmation from the neighbor.

    - **LastUnreachable**  
       The time, in milliseconds, that a node assumes that the neighbor will remain unreachable after the node fails to receive a reachability confirmation from the neighbor.

## Remarks

The [**GetIpNetTable2**](getipnettable2.md) function enumerates the neighbor IP addresses on a local computer and returns this information in an [**MIB\_IPNET\_TABLE2**](mib-ipnet-table2.md) structure. For IPv4, this information includes addresses determined by using the Address Resolution Protocol (ARP). For IPv6, this information includes addresses determined by using the Neighbor Discovery (ND) protocol for IPv6 as specified in RFC 2461. For more information, see [Neighbor Discovery for IP Version 6 (IPv6)](https://go.microsoft.com/fwlink/p/?linkid=84044).

The [**GetIpNetEntry2**](getipnetentry2.md) function retrieves a single neighbor IP address and returns this information in a MIB\_IPNET\_ROW2 structure.

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

[**CreateIpNetEntry2**](createipnetentry2.md)

[**GetIpNetEntry2**](getipnetentry2.md)

[**GetIpNetTable2**](getipnettable2.md)

[**MIB\_IPNET\_TABLE2**](mib-ipnet-table2.md)

[**NL\_NEIGHBOR\_STATE**](/windows/win32/api/nldef/ne-nldef-nl_neighbor_state)
