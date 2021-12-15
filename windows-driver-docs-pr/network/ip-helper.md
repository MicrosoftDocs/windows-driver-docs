---
title: IP Helper Overview
description: IP Helper Overview
keywords:
- IP Helper WDK networking
- IP Helper WDK networking , about
- network drivers WDK , IP Helper
ms.date: 04/20/2017
---

# IP Helper Overview

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
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546130(v=vs.85)" data-raw-source="[&lt;strong&gt;ConvertInterfaceAliasToLuid&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546130(v=vs.85))"><strong>ConvertInterfaceAliasToLuid</strong></a></p></td>
<td align="left"><p>Converts a locally unique identifier (LUID) for a network interface to the Unicode interface name.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546137(v=vs.85)" data-raw-source="[&lt;strong&gt;ConvertInterfaceGuidToLuid&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546137(v=vs.85))"><strong>ConvertInterfaceGuidToLuid</strong></a></p></td>
<td align="left"><p>Converts a globally unique identifier (GUID) for a network interface to the LUID for the interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546141(v=vs.85)" data-raw-source="[&lt;strong&gt;ConvertInterfaceIndexToLuid&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546141(v=vs.85))"><strong>ConvertInterfaceIndexToLuid</strong></a></p></td>
<td align="left"><p>Converts a local index for a network interface to the LUID for the interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546151(v=vs.85)" data-raw-source="[&lt;strong&gt;ConvertInterfaceLuidToAlias&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546151(v=vs.85))"><strong>ConvertInterfaceLuidToAlias</strong></a></p></td>
<td align="left"><p>Converts a LUID for a network interface to an interface alias.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546156(v=vs.85)" data-raw-source="[&lt;strong&gt;ConvertInterfaceLuidToGuid&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546156(v=vs.85))"><strong>ConvertInterfaceLuidToGuid</strong></a></p></td>
<td align="left"><p>Converts a LUID for a network interface to a GUID for the interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546167(v=vs.85)" data-raw-source="[&lt;strong&gt;ConvertInterfaceLuidToIndex&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546167(v=vs.85))"><strong>ConvertInterfaceLuidToIndex</strong></a></p></td>
<td align="left"><p>Converts a LUID for a network interface to the local index for the interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546171(v=vs.85)" data-raw-source="[&lt;strong&gt;ConvertInterfaceLuidToNameA&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546171(v=vs.85))"><strong>ConvertInterfaceLuidToNameA</strong></a></p></td>
<td align="left"><p>Converts a LUID for a network interface to the ANSI interface name.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546175(v=vs.85)" data-raw-source="[&lt;strong&gt;ConvertInterfaceLuidToNameW&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546175(v=vs.85))"><strong>ConvertInterfaceLuidToNameW</strong></a></p></td>
<td align="left"><p>Converts a LUID for a network interface to the Unicode interface name.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546185(v=vs.85)" data-raw-source="[&lt;strong&gt;ConvertInterfaceNameToLuidA&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546185(v=vs.85))"><strong>ConvertInterfaceNameToLuidA</strong></a></p></td>
<td align="left"><p>Converts an ANSI network interface name to the LUID for the interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546192(v=vs.85)" data-raw-source="[&lt;strong&gt;ConvertInterfaceNameToLuidW&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546192(v=vs.85))"><strong>ConvertInterfaceNameToLuidW</strong></a></p></td>
<td align="left"><p>Converts a Unicode network interface name to the LUID for the interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff553785(v=vs.85)" data-raw-source="[&lt;strong&gt;if_indextoname&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff553785(v=vs.85))"><strong>if_indextoname</strong></a></p></td>
<td align="left"><p>Converts the local index for a network interface to the ANSI interface name.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff553788(v=vs.85)" data-raw-source="[&lt;strong&gt;if_nametoindex&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff553788(v=vs.85))"><strong>if_nametoindex</strong></a></p></td>
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
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552517(v=vs.85)" data-raw-source="[&lt;strong&gt;GetIfEntry2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552517(v=vs.85))"><strong>GetIfEntry2</strong></a></p></td>
<td align="left"><p>Retrieves information for the specified interface on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552521(v=vs.85)" data-raw-source="[&lt;strong&gt;GetIfStackTable&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552521(v=vs.85))"><strong>GetIfStackTable</strong></a></p></td>
<td align="left"><p>Retrieves a table of network interface stack row entries that specify the relationship of the network interfaces on an interface stack.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552524(v=vs.85)" data-raw-source="[&lt;strong&gt;GetIfTable2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552524(v=vs.85))"><strong>GetIfTable2</strong></a></p></td>
<td align="left"><p>Retrieves the MIB-II interface table.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552528(v=vs.85)" data-raw-source="[&lt;strong&gt;GetIfTable2Ex&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552528(v=vs.85))"><strong>GetIfTable2Ex</strong></a></p></td>
<td align="left"><p>Retrieves the MIB-II interface table, given a level of interface information to retrieve.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552531(v=vs.85)" data-raw-source="[&lt;strong&gt;GetInvertedIfStackTable&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552531(v=vs.85))"><strong>GetInvertedIfStackTable</strong></a></p></td>
<td align="left"><p>Retrieves a table of inverted network interface stack row entries that specify the relationship of the network interfaces on an interface stack.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552540(v=vs.85)" data-raw-source="[&lt;strong&gt;GetIpInterfaceEntry&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552540(v=vs.85))"><strong>GetIpInterfaceEntry</strong></a></p></td>
<td align="left"><p>Retrieves IP information for the specified interface on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552543(v=vs.85)" data-raw-source="[&lt;strong&gt;GetIpInterfaceTable&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552543(v=vs.85))"><strong>GetIpInterfaceTable</strong></a></p></td>
<td align="left"><p>Retrieves the IP interface entries on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff554883(v=vs.85)" data-raw-source="[&lt;strong&gt;InitializeIpInterfaceEntry&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff554883(v=vs.85))"><strong>InitializeIpInterfaceEntry</strong></a></p></td>
<td align="left"><p>Initializes the members of a <a href="/previous-versions/windows/hardware/drivers/ff559254(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_IPINTERFACE_ROW&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559254(v=vs.85))"><strong>MIB_IPINTERFACE_ROW</strong></a> structure entry with default values.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff570774(v=vs.85)" data-raw-source="[&lt;strong&gt;SetIpInterfaceEntry&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff570774(v=vs.85))"><strong>SetIpInterfaceEntry</strong></a></p></td>
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
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546204(v=vs.85)" data-raw-source="[&lt;strong&gt;CreateAnycastIpAddressEntry&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546204(v=vs.85))"><strong>CreateAnycastIpAddressEntry</strong></a></p></td>
<td align="left"><p>Adds a new anycast IP address entry on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546219(v=vs.85)" data-raw-source="[&lt;strong&gt;CreateSortedAddressPairs&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546219(v=vs.85))"><strong>CreateSortedAddressPairs</strong></a></p></td>
<td align="left"><p>Pairs a supplied list of destination addresses together with the host machine's local IP addresses and sorts the pairs according to the preferred order of communication.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546227(v=vs.85)" data-raw-source="[&lt;strong&gt;CreateUnicastIpAddressEntry&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546227(v=vs.85))"><strong>CreateUnicastIpAddressEntry</strong></a></p></td>
<td align="left"><p>Adds a new unicast IP address entry on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546363(v=vs.85)" data-raw-source="[&lt;strong&gt;DeleteAnycastIpAddressEntry&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546363(v=vs.85))"><strong>DeleteAnycastIpAddressEntry</strong></a></p></td>
<td align="left"><p>Deletes an existing anycast IP address entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546370(v=vs.85)" data-raw-source="[&lt;strong&gt;DeleteUnicastIpAddressEntry&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546370(v=vs.85))"><strong>DeleteUnicastIpAddressEntry</strong></a></p></td>
<td align="left"><p>Deletes an existing unicast IP address entry from the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552504(v=vs.85)" data-raw-source="[&lt;strong&gt;GetAnycastIpAddressEntry&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552504(v=vs.85))"><strong>GetAnycastIpAddressEntry</strong></a></p></td>
<td align="left"><p>Retrieves information for an existing anycast IP address entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552508(v=vs.85)" data-raw-source="[&lt;strong&gt;GetAnycastIpAddressTable&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552508(v=vs.85))"><strong>GetAnycastIpAddressTable</strong></a></p></td>
<td align="left"><p>Retrieves the anycast IP address table on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552565(v=vs.85)" data-raw-source="[&lt;strong&gt;GetMulticastIpAddressEntry&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552565(v=vs.85))"><strong>GetMulticastIpAddressEntry</strong></a></p></td>
<td align="left"><p>Retrieves information for an existing multicast IP address entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552570(v=vs.85)" data-raw-source="[&lt;strong&gt;GetMulticastIpAddressTable&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552570(v=vs.85))"><strong>GetMulticastIpAddressTable</strong></a></p></td>
<td align="left"><p>Retrieves the multicast IP address table on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552589(v=vs.85)" data-raw-source="[&lt;strong&gt;GetUnicastIpAddressEntry&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552589(v=vs.85))"><strong>GetUnicastIpAddressEntry</strong></a></p></td>
<td align="left"><p>Retrieves information for an existing unicast IP address entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552594(v=vs.85)" data-raw-source="[&lt;strong&gt;GetUnicastIpAddressTable&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552594(v=vs.85))"><strong>GetUnicastIpAddressTable</strong></a></p></td>
<td align="left"><p>Retrieves the unicast IP address table on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff554886(v=vs.85)" data-raw-source="[&lt;strong&gt;InitializeUnicastIpAddressEntry&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff554886(v=vs.85))"><strong>InitializeUnicastIpAddressEntry</strong></a></p></td>
<td align="left"><p>Initializes a <a href="/previous-versions/windows/hardware/drivers/ff559308(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_UNICASTIPADDRESS_ROW&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559308(v=vs.85))"><strong>MIB_UNICASTIPADDRESS_ROW</strong></a> structure with default values for a unicast IP address entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff568807(v=vs.85)" data-raw-source="[&lt;strong&gt;NotifyStableUnicastIpAddressTable&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff568807(v=vs.85))"><strong>NotifyStableUnicastIpAddressTable</strong></a></p></td>
<td align="left"><p>Retrieves the stable unicast IP address table on a local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff570800(v=vs.85)" data-raw-source="[&lt;strong&gt;SetUnicastIpAddressEntry&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff570800(v=vs.85))"><strong>SetUnicastIpAddressEntry</strong></a></p></td>
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
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546217(v=vs.85)" data-raw-source="[&lt;strong&gt;CreateIpNetEntry2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546217(v=vs.85))"><strong>CreateIpNetEntry2</strong></a></p></td>
<td align="left"><p>Creates a new neighbor IP address entry on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546368(v=vs.85)" data-raw-source="[&lt;strong&gt;DeleteIpNetEntry2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546368(v=vs.85))"><strong>DeleteIpNetEntry2</strong></a></p></td>
<td align="left"><p>Deletes a neighbor IP address entry from the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff550029(v=vs.85)" data-raw-source="[&lt;strong&gt;FlushIpNetTable2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff550029(v=vs.85))"><strong>FlushIpNetTable2</strong></a></p></td>
<td align="left"><p>Flushes the IP neighbor table on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552546(v=vs.85)" data-raw-source="[&lt;strong&gt;GetIpNetEntry2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552546(v=vs.85))"><strong>GetIpNetEntry2</strong></a></p></td>
<td align="left"><p>Retrieves information for a neighbor IP address entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552551(v=vs.85)" data-raw-source="[&lt;strong&gt;GetIpNetTable2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552551(v=vs.85))"><strong>GetIpNetTable2</strong></a></p></td>
<td align="left"><p>Retrieves the IP neighbor table on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff570686(v=vs.85)" data-raw-source="[&lt;strong&gt;ResolveIpNetEntry2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff570686(v=vs.85))"><strong>ResolveIpNetEntry2</strong></a></p></td>
<td align="left"><p>Resolves the physical address for a neighbor IP address entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff570775(v=vs.85)" data-raw-source="[&lt;strong&gt;SetIpNetEntry2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff570775(v=vs.85))"><strong>SetIpNetEntry2</strong></a></p></td>
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
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff550031(v=vs.85)" data-raw-source="[&lt;strong&gt;FlushIpPathTable&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff550031(v=vs.85))"><strong>FlushIpPathTable</strong></a></p></td>
<td align="left"><p>Flushes the IP path table on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552556(v=vs.85)" data-raw-source="[&lt;strong&gt;GetIpPathEntry&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552556(v=vs.85))"><strong>GetIpPathEntry</strong></a></p></td>
<td align="left"><p>Retrieves information for an IP path entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552559(v=vs.85)" data-raw-source="[&lt;strong&gt;GetIpPathTable&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552559(v=vs.85))"><strong>GetIpPathTable</strong></a></p></td>
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
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546209(v=vs.85)" data-raw-source="[&lt;strong&gt;CreateIpForwardEntry2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546209(v=vs.85))"><strong>CreateIpForwardEntry2</strong></a></p></td>
<td align="left"><p>Creates a new IP route entry on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff546365(v=vs.85)" data-raw-source="[&lt;strong&gt;DeleteIpForwardEntry2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546365(v=vs.85))"><strong>DeleteIpForwardEntry2</strong></a></p></td>
<td align="left"><p>Deletes an IP route entry from the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552511(v=vs.85)" data-raw-source="[&lt;strong&gt;GetBestRoute2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552511(v=vs.85))"><strong>GetBestRoute2</strong></a></p></td>
<td align="left"><p>Retrieves the IP route entry on the local computer for the best route to the specified destination IP address.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552535(v=vs.85)" data-raw-source="[&lt;strong&gt;GetIpForwardEntry2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552535(v=vs.85))"><strong>GetIpForwardEntry2</strong></a></p></td>
<td align="left"><p>Retrieves information for an IP route entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552536(v=vs.85)" data-raw-source="[&lt;strong&gt;GetIpForwardTable2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552536(v=vs.85))"><strong>GetIpForwardTable2</strong></a></p></td>
<td align="left"><p>Retrieves the IP route entries on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff554882(v=vs.85)" data-raw-source="[&lt;strong&gt;InitializeIpForwardEntry&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff554882(v=vs.85))"><strong>InitializeIpForwardEntry</strong></a></p></td>
<td align="left"><p>Initializes a <a href="/previous-versions/windows/hardware/drivers/ff559245(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_IPFORWARD_ROW2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559245(v=vs.85))"><strong>MIB_IPFORWARD_ROW2</strong></a> structure with default values for an IP route entry on the local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff570773(v=vs.85)" data-raw-source="[&lt;strong&gt;SetIpForwardEntry2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff570773(v=vs.85))"><strong>SetIpForwardEntry2</strong></a></p></td>
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
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff550045(v=vs.85)" data-raw-source="[&lt;strong&gt;FreeMibTable&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff550045(v=vs.85))"><strong>FreeMibTable</strong></a></p></td>
<td align="left"><p>Frees the buffer that is allocated by the functions that return tables of network interfaces, addresses, and routes (for example, <a href="/previous-versions/windows/hardware/drivers/ff552524(v=vs.85)" data-raw-source="[&lt;strong&gt;GetIfTable2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552524(v=vs.85))"><strong>GetIfTable2</strong></a> and <a href="/previous-versions/windows/hardware/drivers/ff552508(v=vs.85)" data-raw-source="[&lt;strong&gt;GetAnycastIpAddressTable&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552508(v=vs.85))"><strong>GetAnycastIpAddressTable</strong></a>).</p></td>
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
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff544864(v=vs.85)" data-raw-source="[&lt;strong&gt;CancelMibChangeNotify2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff544864(v=vs.85))"><strong>CancelMibChangeNotify2</strong></a></p></td>
<td align="left"><p>Deregisters the driver for change notifications for IP interface changes, IP address changes, IP route changes, and requests to retrieve the stable unicast IP address table.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff568805(v=vs.85)" data-raw-source="[&lt;strong&gt;NotifyIpInterfaceChange&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff568805(v=vs.85))"><strong>NotifyIpInterfaceChange</strong></a></p></td>
<td align="left"><p>Registers the driver to be notified for changes to all IP interfaces, IPv4 interfaces, or IPv6 interfaces on a local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff568806(v=vs.85)" data-raw-source="[&lt;strong&gt;NotifyRouteChange2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff568806(v=vs.85))"><strong>NotifyRouteChange2</strong></a></p></td>
<td align="left"><p>Registers to be notified for changes to IP route entries on a local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff568809(v=vs.85)" data-raw-source="[&lt;strong&gt;NotifyUnicastIpAddressChange&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff568809(v=vs.85))"><strong>NotifyUnicastIpAddressChange</strong></a></p></td>
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
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff552578(v=vs.85)" data-raw-source="[&lt;strong&gt;GetTeredoPort&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff552578(v=vs.85))"><strong>GetTeredoPort</strong></a></p></td>
<td align="left"><p>Retrieves the dynamic UDP port number that the Teredo client uses on the local computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff568808(v=vs.85)" data-raw-source="[&lt;strong&gt;NotifyTeredoPortChange&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff568808(v=vs.85))"><strong>NotifyTeredoPortChange</strong></a></p></td>
<td align="left"><p>Registers to be notified for changes to the UDP port number that the Teredo client uses for the Teredo service port on a local computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff568807(v=vs.85)" data-raw-source="[&lt;strong&gt;NotifyStableUnicastIpAddressTable&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff568807(v=vs.85))"><strong>NotifyStableUnicastIpAddressTable</strong></a></p></td>
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
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff557013(v=vs.85)" data-raw-source="[&lt;strong&gt;IP_ADDRESS_PREFIX&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff557013(v=vs.85))"><strong>IP_ADDRESS_PREFIX</strong></a></p></td>
<td align="left"><p>Stores an IP address prefix.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559190(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_ANYCASTIPADDRESS_ROW&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559190(v=vs.85))"><strong>MIB_ANYCASTIPADDRESS_ROW</strong></a></p></td>
<td align="left"><p>Stores information about an anycast IP address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559193(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_ANYCASTIPADDRESS_TABLE&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559193(v=vs.85))"><strong>MIB_ANYCASTIPADDRESS_TABLE</strong></a></p></td>
<td align="left"><p>Contains a table of anycast IP address entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559214(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_IF_ROW2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559214(v=vs.85))"><strong>MIB_IF_ROW2</strong></a></p></td>
<td align="left"><p>Stores information about a particular interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559224(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_IF_TABLE2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559224(v=vs.85))"><strong>MIB_IF_TABLE2</strong></a></p></td>
<td align="left"><p>Contains a table of logical and physical interface entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559207(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_IFSTACK_ROW&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559207(v=vs.85))"><strong>MIB_IFSTACK_ROW</strong></a></p></td>
<td align="left"><p>Represents the relationship between two network interfaces.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559210(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_IFSTACK_TABLE&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559210(v=vs.85))"><strong>MIB_IFSTACK_TABLE</strong></a></p></td>
<td align="left"><p>Contains a table of row entries in the network interface stack. This table specifies the relationship of the network interfaces on an interface stack.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559234(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_INVERTEDIFSTACK_ROW&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559234(v=vs.85))"><strong>MIB_INVERTEDIFSTACK_ROW</strong></a></p></td>
<td align="left"><p>Represents the relationship between two network interfaces.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559240(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_INVERTEDIFSTACK_TABLE&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559240(v=vs.85))"><strong>MIB_INVERTEDIFSTACK_TABLE</strong></a></p></td>
<td align="left"><p>Contains a table of inverted network interface stack row entries. This table specifies the relationship of the network interfaces on an interface stack in reverse order.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559245(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_IPFORWARD_ROW2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559245(v=vs.85))"><strong>MIB_IPFORWARD_ROW2</strong></a></p></td>
<td align="left"><p>Stores information about an IP route entry.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559252(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_IPFORWARD_TABLE2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559252(v=vs.85))"><strong>MIB_IPFORWARD_TABLE2</strong></a></p></td>
<td align="left"><p>Contains a table of IP route entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559254(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_IPINTERFACE_ROW&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559254(v=vs.85))"><strong>MIB_IPINTERFACE_ROW</strong></a></p></td>
<td align="left"><p>Stores interface management information for a particular IP address family on a network interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559260(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_IPINTERFACE_TABLE&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559260(v=vs.85))"><strong>MIB_IPINTERFACE_TABLE</strong></a></p></td>
<td align="left"><p>Contains a table of IP interface entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559263(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_IPNET_ROW2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559263(v=vs.85))"><strong>MIB_IPNET_ROW2</strong></a></p></td>
<td align="left"><p>Stores information about a neighbor IP address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559267(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_IPNET_TABLE2&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559267(v=vs.85))"><strong>MIB_IPNET_TABLE2</strong></a></p></td>
<td align="left"><p>Contains a table of neighbor IP address entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559270(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_IPPATH_ROW&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559270(v=vs.85))"><strong>MIB_IPPATH_ROW</strong></a></p></td>
<td align="left"><p>Stores information about an IP path entry.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559273(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_IPPATH_TABLE&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559273(v=vs.85))"><strong>MIB_IPPATH_TABLE</strong></a></p></td>
<td align="left"><p>Contains a table of IP path entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559277(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_MULTICASTIPADDRESS_ROW&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559277(v=vs.85))"><strong>MIB_MULTICASTIPADDRESS_ROW</strong></a></p></td>
<td align="left"><p>Stores information about a multicast IP address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559281(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_MULTICASTIPADDRESS_TABLE&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559281(v=vs.85))"><strong>MIB_MULTICASTIPADDRESS_TABLE</strong></a></p></td>
<td align="left"><p>Contains a table of multicast IP address entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559308(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_UNICASTIPADDRESS_ROW&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559308(v=vs.85))"><strong>MIB_UNICASTIPADDRESS_ROW</strong></a></p></td>
<td align="left"><p>Stores information about a unicast IP address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559322(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_UNICASTIPADDRESS_TABLE&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559322(v=vs.85))"><strong>MIB_UNICASTIPADDRESS_TABLE</strong></a></p></td>
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
<td align="left"><p><a href="/windows/win32/api/netioapi/ne-netioapi-mib_if_table_level" data-raw-source="[&lt;strong&gt;MIB_IF_TABLE_LEVEL&lt;/strong&gt;](/windows/win32/api/netioapi/ne-netioapi-_mib_if_table_level)"><strong>MIB_IF_TABLE_LEVEL</strong></a></p></td>
<td align="left"><p>Defines the level of interface information to retrieve.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff559286(v=vs.85)" data-raw-source="[&lt;strong&gt;MIB_NOTIFICATION_TYPE&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff559286(v=vs.85))"><strong>MIB_NOTIFICATION_TYPE</strong></a></p></td>
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
<td align="left"><p><a href="/windows/win32/api/nldef/ne-nldef-nl_address_type" data-raw-source="[&lt;strong&gt;NL_ADDRESS_TYPE&lt;/strong&gt;](/windows/win32/api/nldef/ne-nldef-nl_address_type)"><strong>NL_ADDRESS_TYPE</strong></a></p></td>
<td align="left"><p>Specifies the IP address type of the network layer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff568758(v=vs.85)" data-raw-source="[&lt;strong&gt;NL_DAD_STATE&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff568758(v=vs.85))"><strong>NL_DAD_STATE</strong></a></p></td>
<td align="left"><p>Defines the duplicate address detection (DAD) state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/nldef/ne-nldef-nl_link_local_address_behavior" data-raw-source="[&lt;strong&gt;NL_LINK_LOCAL_ADDRESS_BEHAVIOR&lt;/strong&gt;](/windows/win32/api/nldef/ne-nldef-_nl_link_local_address_behavior)"><strong>NL_LINK_LOCAL_ADDRESS_BEHAVIOR</strong></a></p></td>
<td align="left"><p>Defines the link local address behavior.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/nldef/ne-nldef-nl_neighbor_state" data-raw-source="[&lt;strong&gt;NL_NEIGHBOR_STATE&lt;/strong&gt;](/windows/win32/api/nldef/ne-nldef-_nl_neighbor_state)"><strong>NL_NEIGHBOR_STATE</strong></a></p></td>
<td align="left"><p>Defines the state of a network layer neighbor IP address, as described in RFC 2461, section 7.3.2.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff568762(v=vs.85)" data-raw-source="[&lt;strong&gt;NL_PREFIX_ORIGIN&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff568762(v=vs.85))"><strong>NL_PREFIX_ORIGIN</strong></a></p></td>
<td align="left"><p>Defines the origin of the prefix or network part of the IP address.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/nldef/ne-nldef-nl_route_origin" data-raw-source="[&lt;strong&gt;NL_ROUTE_ORIGIN&lt;/strong&gt;](/windows/win32/api/nldef/ne-nldef-_nl_route_origin)"><strong>NL_ROUTE_ORIGIN</strong></a></p></td>
<td align="left"><p>Defines the origin of the IP route.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/nldef/ne-nldef-nl_route_protocol" data-raw-source="[&lt;strong&gt;NL_ROUTE_PROTOCOL&lt;/strong&gt;](/windows/win32/api/nldef/ne-nldef-nl_route_protocol)"><strong>NL_ROUTE_PROTOCOL</strong></a></p></td>
<td align="left"><p>Defines the routing mechanism that an IP route was added with, as described in RFC 4292.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/nldef/ne-nldef-nl_router_discovery_behavior" data-raw-source="[&lt;strong&gt;NL_ROUTER_DISCOVERY_BEHAVIOR&lt;/strong&gt;](/windows/win32/api/nldef/ne-nldef-_nl_router_discovery_behavior)"><strong>NL_ROUTER_DISCOVERY_BEHAVIOR</strong></a></p></td>
<td align="left"><p>Defines the router discovery behavior, as described in RFC 2461.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff568768(v=vs.85)" data-raw-source="[&lt;strong&gt;NL_SUFFIX_ORIGIN&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff568768(v=vs.85))"><strong>NL_SUFFIX_ORIGIN</strong></a></p></td>
<td align="left"><p>Defines the origin of the suffix or host part of the IP address.</p></td>
</tr>
</tbody>
</table>

 

