---
title: IP Helper
description: IP Helper
ms.assetid: c7cf1f47-ee0d-4c89-883b-717b719fcc2a
keywords:
- IP Helper WDK networking
- IP Helper WDK networking , about
- network drivers WDK , IP Helper
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IP Helper


## <a href="" id="ddk-ndis-register-access-interface-nr"></a>


Internet Protocol Helper (IP Helper) enables drivers to retrieve information about the network configuration of the local computer and to modify that configuration. IP Helper also provides notification mechanisms to make sure that a driver is notified when certain aspects of the local computer network configuration change. IP Helper is available in Windows Vista and later versions of the Microsoft Windows operating systems.

Many of the IP Helper functions pass structure parameters that represent data types that are associated with the Management Information Base (MIB) technology. The IP Helper functions use these MIB structures to represent various networking information.

The IP Helper documentation uses the terms "adapter" and "interface" extensively. An *adapter* is a legacy term that is an abbreviated form of *network adapter*, which originally referred to some form of network hardware. An adapter is a data link-level abstraction.

An *interface* is described in the IETF RFC documents as an abstract concept that represents a node's attachment to a link. An interface is an IP-level abstraction.

Your driver can use the following kernel-mode functions, MIB structures, and MIB and Network Layer (NL) enumerations to retrieve and modify configuration settings for Transmission Control Protocol/Internet Protocol (TCP/IP) transport on a local computer.

**Note**  When you are developing driver code, follow the instructions for [including header files.](including-header-files-for-ip-helper.md)

 

### Interface Conversion Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>ConvertInterfaceAliasToLuid</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546130)</p></td>
<td align="left"><p>Converts a locally unique identifier (LUID) for a network interface to the Unicode interface name.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ConvertInterfaceGuidToLuid</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546137)</p></td>
<td align="left"><p>Converts a globally unique identifier (GUID) for a network interface to the LUID for the interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ConvertInterfaceIndexToLuid</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546141)</p></td>
<td align="left"><p>Converts a local index for a network interface to the LUID for the interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ConvertInterfaceLuidToAlias</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546151)</p></td>
<td align="left"><p>Converts a LUID for a network interface to an interface alias.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ConvertInterfaceLuidToGuid</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546156)</p></td>
<td align="left"><p>Converts a LUID for a network interface to a GUID for the interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ConvertInterfaceLuidToIndex</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546167)</p></td>
<td align="left"><p>Converts a LUID for a network interface to the local index for the interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ConvertInterfaceLuidToNameA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546171)</p></td>
<td align="left"><p>Converts a LUID for a network interface to the ANSI interface name.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ConvertInterfaceLuidToNameW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546175)</p></td>
<td align="left"><p>Converts a LUID for a network interface to the Unicode interface name.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ConvertInterfaceNameToLuidA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546185)</p></td>
<td align="left"><p>Converts an ANSI network interface name to the LUID for the interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ConvertInterfaceNameToLuidW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546192)</p></td>
<td align="left"><p>Converts a Unicode network interface name to the LUID for the interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>if_indextoname</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553785)</p></td>
<td align="left"><p>Converts the local index for a network interface to the ANSI interface name.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>if_nametoindex</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553788)</p></td>
<td align="left"><p>Converts the ANSI interface name for a network interface to the local index for the interface.</p></td>
</tr>
</tbody>
</table>

 

### Interface Management Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>GetIfEntry2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552517)</p></td>
<td align="left"><p>Retrieves information for the specified interface on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>GetIfStackTable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552521)</p></td>
<td align="left"><p>Retrieves a table of network interface stack row entries that specify the relationship of the network interfaces on an interface stack.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>GetIfTable2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552524)</p></td>
<td align="left"><p>Retrieves the MIB-II interface table.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>GetIfTable2Ex</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552528)</p></td>
<td align="left"><p>Retrieves the MIB-II interface table, given a level of interface information to retrieve.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>GetInvertedIfStackTable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552531)</p></td>
<td align="left"><p>Retrieves a table of inverted network interface stack row entries that specify the relationship of the network interfaces on an interface stack.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>GetIpInterfaceEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552540)</p></td>
<td align="left"><p>Retrieves IP information for the specified interface on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>GetIpInterfaceTable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552543)</p></td>
<td align="left"><p>Retrieves the IP interface entries on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>InitializeIpInterfaceEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554883)</p></td>
<td align="left"><p>Initializes the members of a [<strong>MIB_IPINTERFACE_ROW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559254) structure entry with default values.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetIpInterfaceEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570774)</p></td>
<td align="left"><p>Sets the properties of an IP interface on the local computer.</p></td>
</tr>
</tbody>
</table>

 

### IP Address Management Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>CreateAnycastIpAddressEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546204)</p></td>
<td align="left"><p>Adds a new anycast IP address entry on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>CreateSortedAddressPairs</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546219)</p></td>
<td align="left"><p>Pairs a supplied list of destination addresses together with the host machine's local IP addresses and sorts the pairs according to the preferred order of communication.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>CreateUnicastIpAddressEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546227)</p></td>
<td align="left"><p>Adds a new unicast IP address entry on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DeleteAnycastIpAddressEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546363)</p></td>
<td align="left"><p>Deletes an existing anycast IP address entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DeleteUnicastIpAddressEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546370)</p></td>
<td align="left"><p>Deletes an existing unicast IP address entry from the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>GetAnycastIpAddressEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552504)</p></td>
<td align="left"><p>Retrieves information for an existing anycast IP address entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>GetAnycastIpAddressTable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552508)</p></td>
<td align="left"><p>Retrieves the anycast IP address table on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>GetMulticastIpAddressEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552565)</p></td>
<td align="left"><p>Retrieves information for an existing multicast IP address entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>GetMulticastIpAddressTable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552570)</p></td>
<td align="left"><p>Retrieves the multicast IP address table on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>GetUnicastIpAddressEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552589)</p></td>
<td align="left"><p>Retrieves information for an existing unicast IP address entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>GetUnicastIpAddressTable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552594)</p></td>
<td align="left"><p>Retrieves the unicast IP address table on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>InitializeUnicastIpAddressEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554886)</p></td>
<td align="left"><p>Initializes a [<strong>MIB_UNICASTIPADDRESS_ROW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559308) structure with default values for a unicast IP address entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NotifyStableUnicastIpAddressTable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568807)</p></td>
<td align="left"><p>Retrieves the stable unicast IP address table on a local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetUnicastIpAddressEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570800)</p></td>
<td align="left"><p>Sets the properties of an existing unicast IP address entry on the local computer.</p></td>
</tr>
</tbody>
</table>

 

### IP Neighbor Address Management Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>CreateIpNetEntry2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546217)</p></td>
<td align="left"><p>Creates a new neighbor IP address entry on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DeleteIpNetEntry2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546368)</p></td>
<td align="left"><p>Deletes a neighbor IP address entry from the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FlushIpNetTable2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550029)</p></td>
<td align="left"><p>Flushes the IP neighbor table on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>GetIpNetEntry2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552546)</p></td>
<td align="left"><p>Retrieves information for a neighbor IP address entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>GetIpNetTable2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552551)</p></td>
<td align="left"><p>Retrieves the IP neighbor table on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ResolveIpNetEntry2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570686)</p></td>
<td align="left"><p>Resolves the physical address for a neighbor IP address entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetIpNetEntry2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570775)</p></td>
<td align="left"><p>Sets the physical address of an existing neighbor IP address entry on the local computer.</p></td>
</tr>
</tbody>
</table>

 

### IP Path Management Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>FlushIpPathTable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550031)</p></td>
<td align="left"><p>Flushes the IP path table on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>GetIpPathEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552556)</p></td>
<td align="left"><p>Retrieves information for an IP path entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>GetIpPathTable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552559)</p></td>
<td align="left"><p>Retrieves information for an IP path entry on the local computer.</p></td>
</tr>
</tbody>
</table>

 

### IP Route Management Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>CreateIpForwardEntry2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546209)</p></td>
<td align="left"><p>Creates a new IP route entry on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DeleteIpForwardEntry2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546365)</p></td>
<td align="left"><p>Deletes an IP route entry from the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>GetBestRoute2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552511)</p></td>
<td align="left"><p>Retrieves the IP route entry on the local computer for the best route to the specified destination IP address.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>GetIpForwardEntry2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552535)</p></td>
<td align="left"><p>Retrieves information for an IP route entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>GetIpForwardTable2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552536)</p></td>
<td align="left"><p>Retrieves the IP route entries on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>InitializeIpForwardEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554882)</p></td>
<td align="left"><p>Initializes a [<strong>MIB_IPFORWARD_ROW2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559245) structure with default values for an IP route entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetIpForwardEntry2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570773)</p></td>
<td align="left"><p>Sets the properties of an IP route entry on the local computer.</p></td>
</tr>
</tbody>
</table>

 

### IP Table Memory Management Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>FreeMibTable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550045)</p></td>
<td align="left"><p>Frees the buffer that is allocated by the functions that return tables of network interfaces, addresses, and routes (for example, [<strong>GetIfTable2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552524) and [<strong>GetAnycastIpAddressTable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552508)).</p></td>
</tr>
</tbody>
</table>

 

### Notification Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>CancelMibChangeNotify2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544864)</p></td>
<td align="left"><p>Deregisters the driver for change notifications for IP interface changes, IP address changes, IP route changes, and requests to retrieve the stable unicast IP address table.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NotifyIpInterfaceChange</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568805)</p></td>
<td align="left"><p>Registers the driver to be notified for changes to all IP interfaces, IPv4 interfaces, or IPv6 interfaces on a local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NotifyRouteChange2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568806)</p></td>
<td align="left"><p>Registers to be notified for changes to IP route entries on a local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NotifyUnicastIpAddressChange</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568809)</p></td>
<td align="left"><p>Registers to be notified for changes to all unicast IP interfaces, unicast IPv4 addresses, or unicast IPv6 addresses on a local computer.</p></td>
</tr>
</tbody>
</table>

 

### Teredo IPv6 Client Management Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>GetTeredoPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552578)</p></td>
<td align="left"><p>Retrieves the dynamic UDP port number that the Teredo client uses on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NotifyTeredoPortChange</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568808)</p></td>
<td align="left"><p>Registers to be notified for changes to the UDP port number that the Teredo client uses for the Teredo service port on a local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NotifyStableUnicastIpAddressTable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568807)</p></td>
<td align="left"><p>Retrieves the stable unicast IP address table on a local computer.</p></td>
</tr>
</tbody>
</table>

 

### MIB Structures

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Structure</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>IP_ADDRESS_PREFIX</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557013)</p></td>
<td align="left"><p>Stores an IP address prefix.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MIB_ANYCASTIPADDRESS_ROW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559190)</p></td>
<td align="left"><p>Stores information about an anycast IP address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MIB_ANYCASTIPADDRESS_TABLE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559193)</p></td>
<td align="left"><p>Contains a table of anycast IP address entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MIB_IF_ROW2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559214)</p></td>
<td align="left"><p>Stores information about a particular interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MIB_IF_TABLE2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559224)</p></td>
<td align="left"><p>Contains a table of logical and physical interface entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MIB_IFSTACK_ROW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559207)</p></td>
<td align="left"><p>Represents the relationship between two network interfaces.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MIB_IFSTACK_TABLE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559210)</p></td>
<td align="left"><p>Contains a table of row entries in the network interface stack. This table specifies the relationship of the network interfaces on an interface stack.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MIB_INVERTEDIFSTACK_ROW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559234)</p></td>
<td align="left"><p>Represents the relationship between two network interfaces.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MIB_INVERTEDIFSTACK_TABLE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559240)</p></td>
<td align="left"><p>Contains a table of inverted network interface stack row entries. This table specifies the relationship of the network interfaces on an interface stack in reverse order.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MIB_IPFORWARD_ROW2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559245)</p></td>
<td align="left"><p>Stores information about an IP route entry.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MIB_IPFORWARD_TABLE2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559252)</p></td>
<td align="left"><p>Contains a table of IP route entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MIB_IPINTERFACE_ROW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559254)</p></td>
<td align="left"><p>Stores interface management information for a particular IP address family on a network interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MIB_IPINTERFACE_TABLE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559260)</p></td>
<td align="left"><p>Contains a table of IP interface entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MIB_IPNET_ROW2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559263)</p></td>
<td align="left"><p>Stores information about a neighbor IP address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MIB_IPNET_TABLE2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559267)</p></td>
<td align="left"><p>Contains a table of neighbor IP address entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MIB_IPPATH_ROW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559270)</p></td>
<td align="left"><p>Stores information about an IP path entry.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MIB_IPPATH_TABLE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559273)</p></td>
<td align="left"><p>Contains a table of IP path entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MIB_MULTICASTIPADDRESS_ROW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559277)</p></td>
<td align="left"><p>Stores information about a multicast IP address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MIB_MULTICASTIPADDRESS_TABLE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559281)</p></td>
<td align="left"><p>Contains a table of multicast IP address entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MIB_UNICASTIPADDRESS_ROW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559308)</p></td>
<td align="left"><p>Stores information about a unicast IP address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MIB_UNICASTIPADDRESS_TABLE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559322)</p></td>
<td align="left"><p>Contains a table of unicast IP address entries.</p></td>
</tr>
</tbody>
</table>

 

### MIB Enumerations

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Enumeration</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>MIB_IF_TABLE_LEVEL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559229)</p></td>
<td align="left"><p>Defines the level of interface information to retrieve.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MIB_NOTIFICATION_TYPE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559286)</p></td>
<td align="left"><p>Defines the notification type that is passed to a callback function when a notification occurs.</p></td>
</tr>
</tbody>
</table>

 

### NL Enumerations

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Enumeration</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>NL_ADDRESS_TYPE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568757)</p></td>
<td align="left"><p>Specifies the IP address type of the network layer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NL_DAD_STATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568758)</p></td>
<td align="left"><p>Defines the duplicate address detection (DAD) state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NL_LINK_LOCAL_ADDRESS_BEHAVIOR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568760)</p></td>
<td align="left"><p>Defines the link local address behavior.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NL_NEIGHBOR_STATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568761)</p></td>
<td align="left"><p>Defines the state of a network layer neighbor IP address, as described in RFC 2461, section 7.3.2.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NL_PREFIX_ORIGIN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568762)</p></td>
<td align="left"><p>Defines the origin of the prefix or network part of the IP address.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NL_ROUTE_ORIGIN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568764)</p></td>
<td align="left"><p>Defines the origin of the IP route.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NL_ROUTE_PROTOCOL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568766)</p></td>
<td align="left"><p>Defines the routing mechanism that an IP route was added with, as described in RFC 4292.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NL_ROUTER_DISCOVERY_BEHAVIOR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568763)</p></td>
<td align="left"><p>Defines the router discovery behavior, as described in RFC 2461.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NL_SUFFIX_ORIGIN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568768)</p></td>
<td align="left"><p>Defines the origin of the suffix or host part of the IP address.</p></td>
</tr>
</tbody>
</table>

 

 

 





