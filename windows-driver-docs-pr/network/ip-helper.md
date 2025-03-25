---
title: IP Helper Overview
description: Learn how IP Helper enables drivers to retrieve and modify information about the local computer's network configuration.
keywords:
- IP Helper WDK networking
- IP Helper WDK networking , about
- network drivers WDK , IP Helper
ms.date: 12/20/2024
ms.topic: concept-article
---

# IP Helper overview

Internet Protocol Helper (IP Helper) enables drivers to retrieve information about the local computer's network configuration and to modify that configuration. IP Helper also provides notification mechanisms to make sure that a driver is notified when certain aspects of the local computer network configuration change. IP Helper is available in Windows Vista and later versions of the Microsoft Windows operating systems.

Many of the IP Helper functions pass structure parameters that represent data types that are associated with the Management Information Base (MIB) technology. The IP Helper functions use these MIB structures to represent various networking information.

The IP Helper documentation uses the terms *adapter* and *interface* extensively. An *adapter* is a legacy term that's an abbreviated form of *network adapter*, which originally referred to some form of network hardware. An adapter is a data link-level abstraction.

An *interface* is described in the IETF RFC documents as an abstract concept that represents a node's attachment to a link. An interface is an IP-level abstraction.

Your driver can use the following kernel-mode functions, MIB structures, and MIB and network layer (NL) enumerations to retrieve and modify configuration settings for Transmission Control Protocol/Internet Protocol (TCP/IP) transport on a local computer.

> [!NOTE]
> When you develop driver code, follow the instructions for [including header files.](including-header-files-for-ip-helper.md)

### Interface conversion functions

| Function   | Description   |
|------------|---------------|
| [**ConvertInterfaceAliasToLuid**](/windows-hardware/drivers/network/convertinterfacealiastoluid) | Converts a locally unique identifier (LUID) for a network interface to the Unicode interface name.  |
| [**ConvertInterfaceGuidToLuid**](/windows-hardware/drivers/network/convertinterfaceguidtoluid)  | Converts a globally unique identifier (GUID) for a network interface to the LUID for the interface. |
| [**ConvertInterfaceIndexToLuid**](/windows-hardware/drivers/network/convertinterfaceindextoluid) | Converts a local index for a network interface to the LUID for the interface. |
| [**ConvertInterfaceLuidToAlias**](/windows-hardware/drivers/network/convertinterfaceluidtoalias) | Converts a LUID for a network interface to an interface alias.  |
| [**ConvertInterfaceLuidToGuid**](/windows-hardware/drivers/network/convertinterfaceluidtoguid)  | Converts a LUID for a network interface to a GUID for the interface. |
| [**ConvertInterfaceLuidToIndex**](/windows-hardware/drivers/network/convertinterfaceluidtoindex) | Converts a LUID for a network interface to the local index for the interface.  |
| [**ConvertInterfaceLuidToNameA**](/windows-hardware/drivers/network/convertinterfaceluidtonamea) | Converts a LUID for a network interface to the ANSI interface name.  |
| [**ConvertInterfaceLuidToNameW**](/windows-hardware/drivers/network/convertinterfaceluidtonamew) | Converts a LUID for a network interface to the Unicode interface name. |
| [**ConvertInterfaceNameToLuidA**](/windows-hardware/drivers/network/convertinterfacenametoluida) | Converts an ANSI network interface name to the LUID for the interface. |
| [**ConvertInterfaceNameToLuidW**](/windows-hardware/drivers/network/convertinterfacenametoluidw) | Converts a Unicode network interface name to the LUID for the interface.  |
| [**if_indextoname**](/windows-hardware/drivers/network/if-indextoname) | Converts the local index for a network interface to the ANSI interface name.  |
| [**if_nametoindex**](/windows-hardware/drivers/network/if-nametoindex) | Converts the ANSI interface name for a network interface to the local index for the interface.  |

### Interface management functions

| Function     | Description   |
|--------------|---------------|
| [**GetIfEntry2**](/windows-hardware/drivers/network/getifentry2)  | Retrieves information for the specified interface on the local computer. |
| [**GetIfStackTable**](/windows-hardware/drivers/network/getifstacktable)  | Retrieves a table of network interface stack row entries that specify the relationship of the network interfaces on an interface stack.  |
| [**GetIfTable2**](/windows-hardware/drivers/network/getiftable2)  | Retrieves the MIB-II interface table. |
| [**GetIfTable2Ex**](/windows-hardware/drivers/network/getiftable2ex) | Retrieves the MIB-II interface table, given a level of interface information to retrieve. |
| [**GetInvertedIfStackTable**](/windows-hardware/drivers/network/getinvertedifstacktable)  | Retrieves a table of inverted network interface stack row entries that specify the relationship of the network interfaces on an interface stack. |
| [**GetIpInterfaceEntry**](/windows-hardware/drivers/network/getipinterfaceentry) | Retrieves IP information for the specified interface on the local computer. |
| [**GetIpInterfaceTable**](/windows-hardware/drivers/network/getipinterfacetable)  | Retrieves the IP interface entries on the local computer.  |
| [**InitializeIpInterfaceEntry**](/windows-hardware/drivers/network/initializeipinterfaceentry) | Initializes the members of a [MIB_IPINTERFACE_ROW](/windows-hardware/drivers/network/mib-ipinterface-row) structure entry with default values. |
| [**SetIpInterfaceEntry**](/windows-hardware/drivers/network/setipinterfaceentry)  | Sets the properties of an IP interface on the local computer.  |

### IP address management functions

| Function  | Description  |
|-----------|--------------|
| [**CreateAnycastIpAddressEntry**](/windows-hardware/drivers/network/createanycastipaddressentry) | Adds a new anycast IP address entry on the local computer. |
| [**CreateSortedAddressPairs**](/windows-hardware/drivers/network/createsortedaddresspairs) | Pairs a supplied list of destination addresses together with the host machine's local IP addresses and sorts the pairs according to the preferred order of communication. |
| [**CreateUnicastIpAddressEntry**](/windows-hardware/drivers/network/createunicastipaddressentry) | Adds a new unicast IP address entry on the local computer.  |
| [**DeleteAnycastIpAddressEntry**](/windows-hardware/drivers/network/deleteanycastipaddressentry)  | Deletes an existing anycast IP address entry from the local computer.  |
| [**DeleteUnicastIpAddressEntry**](/windows-hardware/drivers/network/deleteunicastipaddressentry)  | Deletes an existing unicast IP address entry from the local computer.   |
| [**GetAnycastIpAddressEntry**](/windows-hardware/drivers/network/getanycastipaddressentry)  | Retrieves information for an existing anycast IP address entry on the local computer.   |
| [**GetAnycastIpAddressTable**](/windows-hardware/drivers/network/getanycastipaddresstable)  | Retrieves the anycast IP address table on the local computer.   |
| [**GetMulticastIpAddressEntry**](/windows-hardware/drivers/network/getmulticastipaddressentry)  | Retrieves information for an existing multicast IP address entry on the local computer.  |
| [**GetMulticastIpAddressTable**](/windows-hardware/drivers/network/getmulticastipaddresstable)  | Retrieves the multicast IP address table on the local computer.   |
| [**GetUnicastIpAddressEntry**](/windows-hardware/drivers/network/getunicastipaddressentry)  | Retrieves information for an existing unicast IP address entry on the local computer.  |
| [**GetUnicastIpAddressTable**](/windows-hardware/drivers/network/getunicastipaddresstable)  | Retrieves the unicast IP address table on the local computer.   |
| [**InitializeUnicastIpAddressEntry**](/windows-hardware/drivers/network/initializeunicastipaddressentry)  | Initializes a [MIB_UNICASTIPADDRESS_ROW](/windows-hardware/drivers/network/mib-unicastipaddress-row) structure with default values for a unicast IP address entry on the local computer.  |
| [**NotifyStableUnicastIpAddressTable**](/windows-hardware/drivers/network/notifystableunicastipaddresstable) | Retrieves the stable unicast IP address table on a local computer.  |
| [**SetUnicastIpAddressEntry**](/windows-hardware/drivers/network/setunicastipaddressentry)  | Sets the properties of an existing unicast IP address entry on the local computer.  |

### IP neighbor address management functions

| Function   | Description   |
|------------|---------------|
| [**CreateIpNetEntry2**](/windows-hardware/drivers/network/createipnetentry2)  | Creates a new neighbor IP address entry on the local computer.  |
| [**DeleteIpNetEntry2**](/windows-hardware/drivers/network/deleteipnetentry2)  | Deletes a neighbor IP address entry from the local computer.  |
| [**FlushIpNetTable2**](/windows-hardware/drivers/network/flushipnettable2)  | Flushes the IP neighbor table on the local computer.  |
| [**GetIpNetEntry2**](/windows-hardware/drivers/network/getipnetentry2)  | Retrieves information for a neighbor IP address entry on the local computer.  |
| [**GetIpNetTable2**](/windows-hardware/drivers/network/getipnettable2)  | Retrieves the IP neighbor table on the local computer.  |
| [**ResolveIpNetEntry2**](/windows-hardware/drivers/network/resolveipnetentry2)  | Resolves the physical address for a neighbor IP address entry on the local computer. |
| [**SetIpNetEntry2**](/windows-hardware/drivers/network/setipnetentry2)  | Sets the physical address of an existing neighbor IP address entry on the local computer. |

### IP path management functions

| Function  | Description   |
|-----------|---------------|
| [**FlushIpPathTable**](/windows-hardware/drivers/network/flushippathtable) | Flushes the IP path table on the local computer.                  |
| [**GetIpPathEntry**](/windows-hardware/drivers/network/getippathentry) | Retrieves information for an IP path entry on the local computer. |
| [**GetIpPathTable**](/windows-hardware/drivers/network/getippathtable) | Retrieves information for an IP path table on the local computer. |

### IP route management functions

| Function   | Description   |
|------------|---------------|
| [**CreateIpForwardEntry2**](/windows-hardware/drivers/network/createipforwardentry2)  | Creates a new IP route entry on the local computer.  |
| [**DeleteIpForwardEntry2**](/windows-hardware/drivers/network/deleteipforwardentry2)  | Deletes an IP route entry from the local computer.   |
| [**GetBestRoute2**](/windows-hardware/drivers/network/getbestroute2)   | Retrieves the IP route entry on the local computer for the best route to the specified destination IP address. |
| [**GetIpForwardEntry2**](/windows-hardware/drivers/network/getipforwardentry2)  | Retrieves information for an IP route entry on the local computer.   |
| [**GetIpForwardTable2**](/windows-hardware/drivers/network/getipforwardtable2)  | Retrieves the IP route entries on the local computer.   |
| [**InitializeIpForwardEntry**](/windows-hardware/drivers/network/initializeipforwardentry) | Initializes a [MIB_IPFORWARD_ROW2](/windows-hardware/drivers/network/mib-ipforward-row2) structure with default values for an IP route entry on the local computer.  |
| [**SetIpForwardEntry2**](/windows-hardware/drivers/network/setipforwardentry2) | Sets the properties of an IP route entry on the local computer.   |

### IP table memory management functions

| Function  | Description  |
|-----------|--------------|
| [**FreeMibTable**](/windows-hardware/drivers/network/freemibtable) | Frees the buffer that is allocated by the functions that return tables of network interfaces, addresses, and routes (for example, [GetIfTable2](/windows-hardware/drivers/network/getiftable2) and [GetAnycastIpAddressTable](/windows-hardware/drivers/network/getanycastipaddresstable)). |

### Notification functions

| Function   | Description   |
|------------|---------------|
| [**CancelMibChangeNotify2**](/windows-hardware/drivers/network/cancelmibchangenotify2)   | Deregisters the driver for change notifications for IP interface changes, IP address changes, IP route changes, and requests to retrieve the stable unicast IP address table. |
| [**NotifyIpInterfaceChange**](/windows-hardware/drivers/network/notifyipinterfacechange)  | Registers the driver to be notified for changes to all IP interfaces, IPv4 interfaces, or IPv6 interfaces on a local computer.                                                |
| [**NotifyRouteChange2**](/windows-hardware/drivers/network/notifyroutechange2)  | Registers to be notified for changes to IP route entries on a local computer.  |
| [**NotifyUnicastIpAddressChange**](/windows-hardware/drivers/network/notifyunicastipaddresschange) | Registers to be notified for changes to all unicast IP interfaces, unicast IPv4 addresses, or unicast IPv6 addresses on a local computer.  |

### Teredo IPv6 client management functions

| Function  | Description   |
|-----------|---------------|
| [**GetTeredoPort**](/windows-hardware/drivers/network/getteredoport)   | Retrieves the dynamic UDP port number that the Teredo client uses on the local computer.  |
| [**NotifyTeredoPortChange**](/windows-hardware/drivers/network/notifyteredoportchange)  | Registers to be notified for changes to the UDP port number that the Teredo client uses for the Teredo service port on a local computer. |
| [**NotifyStableUnicastIpAddressTable**](/windows-hardware/drivers/network/notifystableunicastipaddresstable)  | Retrieves the stable unicast IP address table on a local computer.   |

### MIB structures

| Structure  | Description    |
|------------|----------------|
| [**IP_ADDRESS_PREFIX**](/windows-hardware/drivers/network/ip-address-prefix)  | Stores an IP address prefix.  |
| [**MIB_ANYCASTIPADDRESS_ROW**](/windows-hardware/drivers/network/mib-anycastipaddress-row)  | Stores information about an anycast IP address.   |
| [**MIB_ANYCASTIPADDRESS_TABLE**](/windows-hardware/drivers/network/mib-anycastipaddress-table)   | Contains a table of anycast IP address entries.   |
| [**MIB_IF_ROW2**](/windows-hardware/drivers/network/mib-if-row2)  | Stores information about a particular interface.      |
| [**MIB_IF_TABLE2**](/windows-hardware/drivers/network/mib-if-table2)   | Contains a table of logical and physical interface entries.   |
| [**MIB_IFSTACK_ROW**](/windows-hardware/drivers/network/mib-ifstack-row)  | Represents the relationship between two network interfaces.    |
| [**MIB_IFSTACK_TABLE**](/windows-hardware/drivers/network/mib-ifstack-table)  | Contains a table of row entries in the network interface stack. This table specifies the relationship of the network interfaces on an interface stack.  |
| [**MIB_INVERTEDIFSTACK_ROW**](/windows-hardware/drivers/network/mib-invertedifstack-row)  | Represents the relationship between two network interfaces.   |
| [**MIB_INVERTEDIFSTACK_TABLE**](/windows-hardware/drivers/network/mib-invertedifstack-table)  | Contains a table of inverted network interface stack row entries. This table specifies the relationship of the network interfaces on an interface stack in reverse order. |
| [**MIB_IPFORWARD_ROW2**](/windows-hardware/drivers/network/mib-ipforward-row2)  | Stores information about an IP route entry.  |
| [**MIB_IPFORWARD_TABLE2**](/windows-hardware/drivers/network/mib-ipforward-table2)   | Contains a table of IP route entries.    |
| [**MIB_IPINTERFACE_ROW**](/windows-hardware/drivers/network/mib-ipinterface-row)  | Stores interface management information for a particular IP address family on a network interface.   |
| [**MIB_IPINTERFACE_TABLE**](/windows-hardware/drivers/network/mib-ipinterface-table)  | Contains a table of IP interface entries.   |
| [**MIB_IPNET_ROW2**](/windows-hardware/drivers/network/mib-ipnet-row2)  | Stores information about a neighbor IP address.   |
| [**MIB_IPNET_TABLE2**](/windows-hardware/drivers/network/mib-ipnet-table2)   | Contains a table of neighbor IP address entries.   |
| [**MIB_IPPATH_ROW**](/windows-hardware/drivers/network/mib-ippath-row)   | Stores information about an IP path entry.   |
| [**MIB_IPPATH_TABLE**](/windows-hardware/drivers/network/mib-ippath-table)  | Contains a table of IP path entries.  |
| [**MIB_MULTICASTIPADDRESS_ROW**](/windows-hardware/drivers/network/mib-multicastipaddress-row)  | Stores information about a multicast IP address.   |
| [**MIB_MULTICASTIPADDRESS_TABLE**](/windows-hardware/drivers/network/mib-multicastipaddress-table) | Contains a table of multicast IP address entries.     |
| [**MIB_UNICASTIPADDRESS_ROW**](/windows-hardware/drivers/network/mib-unicastipaddress-row)  | Stores information about a unicast IP address.   |
| [**MIB_UNICASTIPADDRESS_TABLE**](/windows-hardware/drivers/network/mib-unicastipaddress-table)  | Contains a table of unicast IP address entries.   |

### MIB enumerations

| Enumeration  | Description    |
|--------------|----------------|
| [**MIB_IF_TABLE_LEVEL**](/windows/win32/api/netioapi/ne-netioapi-mib_if_table_level) | Defines the level of interface information to retrieve.  |
| [**MIB_NOTIFICATION_TYPE**](/windows-hardware/drivers/network/mib-notification-type) | Defines the notification type that is passed to a callback function when a notification occurs. |

### NL enumerations

| Enumeration  | Description   |
|--------------|---------------|
| [**NL_ADDRESS_TYPE**](/windows/win32/api/nldef/ne-nldef-nl_address_type)  | Specifies the IP address type of the network layer.  |
| [**NL_DAD_STATE**](/windows-hardware/drivers/network/nl-dad-state)  | Defines the duplicate address detection (DAD) state.   |
| [**NL_LINK_LOCAL_ADDRESS_BEHAVIOR**](/windows/win32/api/nldef/ne-nldef-nl_link_local_address_behavior)  | Defines the link local address behavior.  |
| [**NL_NEIGHBOR_STATE**](/windows/win32/api/nldef/ne-nldef-nl_neighbor_state)  | Defines the state of a network layer neighbor IP address, as described in RFC 2461, section 7.3.2. |
| [**NL_PREFIX_ORIGIN**](/windows-hardware/drivers/network/nl-prefix-origin)  | Defines the origin of the prefix or network part of the IP address.  |
| [**NL_ROUTE_ORIGIN**](/windows/win32/api/nldef/ne-nldef-nl_route_origin)  | Defines the origin of the IP route.  |
| [**NL_ROUTE_PROTOCOL**](/windows/win32/api/nldef/ne-nldef-nl_route_protocol)  | Defines the routing mechanism that an IP route was added with, as described in RFC 4292.  |
| [**NL_ROUTER_DISCOVERY_BEHAVIOR**](/windows/win32/api/nldef/ne-nldef-nl_router_discovery_behavior)  | Defines the router discovery behavior, as described in RFC 2461.   |
| [**NL_SUFFIX_ORIGIN**](/windows-hardware/drivers/network/nl-suffix-origin)  | Defines the origin of the suffix or host part of the IP address.   |
