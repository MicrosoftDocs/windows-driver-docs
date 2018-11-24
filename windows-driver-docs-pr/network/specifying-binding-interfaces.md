---
title: Specifying Binding Interfaces
description: Specifying Binding Interfaces
ms.assetid: 49ef3eae-88e6-4424-8c3b-19e8c3bb734f
keywords:
- add-registry-sections WDK networking , binding interfaces
- binding interfaces WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying Binding Interfaces





For each network component that it installs, a network INF file must specify the upper and lower binding interfaces for the component by adding the **Interfaces** key to the **Ndi** key.

The **Interfaces** key has at least two values:

<a href="" id="upperrange"></a>**UpperRange**  
A REG\_SZ value that defines the interfaces to which the component can bind at its top edge.

<a href="" id="lowerrange"></a>**LowerRange**  
A REG\_SZ value that defines the interfaces to which the component can bind at its lower edge. For physical adapters, this interface should always be the network media, such as Ethernet, to which the adapter connects.

**Note**  The **DefUpper** and **DefLower** values in Windows 95/98/Me network INF files, however, are not supported for INF files that will be used on Windows 2000 and later versions of the operating system.

 

The following table lists the Microsoft-supplied **UpperRange** values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>netbios</p></td>
<td align="left"><p>NetBIOS</p></td>
</tr>
<tr class="even">
<td align="left"><p>ipx</p></td>
<td align="left"><p>IPX</p></td>
</tr>
<tr class="odd">
<td align="left"><p>tdi</p></td>
<td align="left"><p>TDI interface to TCP/IP</p></td>
</tr>
<tr class="even">
<td align="left"><p>ndis5</p></td>
<td align="left"><p>NDIS 5.x (ndis2, ndis3, and ndis4 should no longer be used). This value should be specified for any non-ATM network component, such as a non-ATM adapter, that interfaces with NDIS at its upper edge.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Ndisatm</p></td>
<td align="left"><p>NDIS 5.x with ATM support. Specified value for any ATM network component, such as an ATM adapter, whose upper edge interfaces with NDIS</p></td>
</tr>
<tr class="even">
<td align="left"><p>ndiswan</p></td>
<td align="left"><p>Upper edge for a WAN adapter. When specified, this value causes the operating system to automatically enable the WAN adapter for use with RAS</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Ndiscowan</p></td>
<td align="left"><p>Upper edge for a WAN adapter over which connection-oriented NDIS runs</p></td>
</tr>
<tr class="even">
<td align="left"><p>noupper</p></td>
<td align="left"><p>Upper edge for any component that does not expose an upper edge for binding; such a component typically has a private interface at its upper edge</p></td>
</tr>
<tr class="odd">
<td align="left"><p>winsock</p></td>
<td align="left"><p>The Windows socket interface</p></td>
</tr>
<tr class="even">
<td align="left"><p>ndis5_atalk</p></td>
<td align="left"><p>Upper edge for an NDIS 5.x Net component (adapter) that binds only to an AppleTalk interface at its upper edge</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ndis5_dlc</p></td>
<td align="left"><p>Upper edge for an NDIS 5.x Net component (adapter) that binds only to a DLC interface at its upper edge</p></td>
</tr>
<tr class="even">
<td align="left"><p>ndis5_ip</p></td>
<td align="left"><p>Upper edge for an NDIS 5.x Net component (adapter) that binds only to a TCP/IP interface at its upper edge</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ndis5_ipx</p></td>
<td align="left"><p>Upper edge for an NDIS 5.x Net component (adapter) that binds only to an IPX interface at its upper edge</p></td>
</tr>
<tr class="even">
<td align="left"><p>ndis5_nbf</p></td>
<td align="left"><p>Upper edge for an NDIS 5.x Net component (adapter) that binds only to a NetBEUI interface at its upper edge</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ndis5_streams</p></td>
<td align="left"><p>Upper edge for an NDIS 5.x Net component (adapter) that binds only to a streams interface at its upper edge. This value is obsolete for Windows XP and later operating systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>flpp4</p></td>
<td align="left"><p>A mobile broadband (MB) device that supports IPv4.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>flpp6</p></td>
<td align="left"><p>A mobile broadband (MB) device that supports IPv6.</p></td>
</tr>
</tbody>
</table>

 

The following table lists the Microsoft-supplied **LowerRange** values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>ethernet</p></td>
<td align="left"><p>Lower edge for an Ethernet adapter</p></td>
</tr>
<tr class="even">
<td align="left"><p>atm</p></td>
<td align="left"><p>Lower edge for an ATM adapter</p></td>
</tr>
<tr class="odd">
<td align="left"><p>tokenring</p></td>
<td align="left"><p>Lower edge for a token ring adapter</p></td>
</tr>
<tr class="even">
<td align="left"><p>serial</p></td>
<td align="left"><p>Lower edge for a serial adapter</p></td>
</tr>
<tr class="odd">
<td align="left"><p>fddi</p></td>
<td align="left"><p>Lower edge for an FDDI adapter</p></td>
</tr>
<tr class="even">
<td align="left"><p>baseband</p></td>
<td align="left"><p>Lower edge for a baseband adapter</p></td>
</tr>
<tr class="odd">
<td align="left"><p>broadband</p></td>
<td align="left"><p>Lower edge for a broadband adapter</p></td>
</tr>
<tr class="even">
<td align="left"><p>bluetooth</p></td>
<td align="left"><p>Lower edge for a Bluetooth adapter</p></td>
</tr>
<tr class="odd">
<td align="left"><p>arcnet</p></td>
<td align="left"><p>Lower edge for an Arcnet adapter</p></td>
</tr>
<tr class="even">
<td align="left"><p>isdn</p></td>
<td align="left"><p>Lower edge for an ISDN adapter</p></td>
</tr>
<tr class="odd">
<td align="left"><p>localtalk</p></td>
<td align="left"><p>Lower edge for a LocalTalk adapter</p></td>
</tr>
<tr class="even">
<td align="left"><p>wan</p></td>
<td align="left"><p>Lower edge for a WAN adapter</p></td>
</tr>
<tr class="odd">
<td align="left"><p>nolower</p></td>
<td align="left"><p>Lower edge for any component that does not expose a lower edge for binding</p></td>
</tr>
<tr class="even">
<td align="left"><p>ndis5</p></td>
<td align="left"><p>NDIS 5.x. (ndis2, ndis3, and ndis4 should no longer be used.) For any network component whose lower edge interfaces through NDIS with non-ATM components</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Ndisatm</p></td>
<td align="left"><p>Ndis 5.x with ATM support. For any network component whose lower edge interfaces through NDIS with ATM components</p></td>
</tr>
<tr class="even">
<td align="left"><p>Wlan</p></td>
<td align="left"><p>Lower edge for a native 802.11 wireless LAN adapter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ppip</p></td>
<td align="left"><p>Lower edge for a mobile broadband (MB) adapter</p></td>
</tr>
<tr class="even">
<td align="left"><p>vwifi</p></td>
<td align="left"><p>Lower edge for a virtual wifi interface</p></td>
</tr>
</tbody>
</table>

 

The **UpperRange** and **LowerRange** values specify the types of interfaces -- not the actual components -- to which a component can bind. The binding engine binds a network component to all components that provide the specified interface at the appropriate (upper or lower) edge. For example, a protocol with a **LowerRange** of ndis5 binds to all components that have an **UpperRange** of ndis5, such as physical or virtual adapters.

If an NDIS 5.x Net component (adapter) works only with one or more specific protocols, then its **UpperRange** should be assigned one or more protocol-specific values, such as ndis5\_atalk, ndis5\_dlc, ndis5\_ip, ndis5\_ipx, ndis5\_nbf, or ndis5\_streams. Such a net class component should not be assigned an **UpperRange** value of ndis5, because this would cause that component to bind to all protocols that provide an ndis5 lower edge.

An INF-file-writer can define and use vendor-specific **UpperRange** and **LowerRange** values for private binding interfaces. For example, if a vendor wants to bind its adapter only to its own proprietary protocol driver, the INF-file-writer could specify **XXX** for the **UpperRange** of the adapter and **XXX** for the **LowerRange** of the proprietary protocol. The Windows 2000 binding engine will bind all components that have an **UpperRange** of **XXX** (in this case, the adapter) with all components that have a **LowerRange** of **XXX** (in this case, the proprietary protocol).

The following is an example of an *add-registry-section* that adds **UpperRange** and **LowerRange** values for an ATM adapter:

```INF
[addreg-section]
HKR, Ndi\Interfaces, UpperRange, 0, "ndisATM"
HKR, Ndi\Interfaces, LowerRange, 0, "atm"
```

 

 





