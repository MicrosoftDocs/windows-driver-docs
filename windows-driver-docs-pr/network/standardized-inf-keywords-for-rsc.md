---
title: Standardized INF Keywords for RSC
description: Standardized INF Keywords for RSC
ms.assetid: 7418E02F-FD5A-4E58-AAA5-3055B98ED264
keywords:
- receive-side coalescing WDK networking , standardized INF keywords
- RSC WDK networking , standardized INF keywords
- standardized INF keywords WDK RSC
- INF entries WDK RSC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standardized INF Keywords for RSC





In Windows 8, Windows Server 2012, and later, the receive segment coalescing (RSC) interface supports [standardized INF keywords](standardized-inf-keywords-for-network-devices.md) that appear in the registry and are specified in INF files.

The following list shows the enumeration [standardized INF keywords](standardized-inf-keywords-for-network-devices.md) for RSC:

<a href="" id="-rscipv4"></a>**\*RscIPv4**  
Enable or disable support for RSC for the IPv4 datagram version.

<a href="" id="---------rscipv6"></a> **\*RscIPv6**  
Enable or disable support for RSC for the IPv6 datagram version.

Enumeration standardized INF keywords have the following attributes:

<a href="" id="subkeyname"></a>**SubkeyName**  
The name of the keyword that you must specify in the INF file and that appears in the registry.

<a href="" id="paramdesc"></a>**ParamDesc**  
The display text that is associated with **SubkeyName**.

<a href="" id="value"></a>**Value**  
The enumeration integer value that is associated with each option in the list. This value is stored in NDI\\params\\ *SubkeyName*\\*Value*.

<a href="" id="enumdesc"></a>**EnumDesc**  
The display text that is associated with each value that appears in the menu.

<a href="" id="default"></a>**Default**  
The default value for the menu.

The following table describes the possible INF entries for the RSC enumeration keywords.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">SubkeyName</th>
<th align="left">ParamDesc</th>
<th align="left">Value</th>
<th align="left">EnumDesc</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong><em>RscIPv4</strong></p></td>
<td align="left"><p>Recv Segment Coalescing (IPv4)</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1 (Default)</p></td>
<td align="left"><p>Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong></em>RscIPv6</strong></p></td>
<td align="left"><p>Recv Segment Coalescing (IPv6)</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1 (Default)</p></td>
<td align="left"><p>Enabled</p></td>
</tr>
</tbody>
</table>

 

For more information about standardized INF keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

For more information about using enumeration keywords, see [Enumeration Keywords](enumeration-keywords.md).

 

 





