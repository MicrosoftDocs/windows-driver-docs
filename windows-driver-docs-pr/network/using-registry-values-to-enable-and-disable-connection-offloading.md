---
title: Using Registry Values to Enable and Disable Connection Offloading
description: Using Registry Values to Enable and Disable Connection Offloading
ms.assetid: dd5d1e8a-0c6f-40d2-8a33-4d6fc70c17d5
keywords:
- connection offload WDK TCP/IP transport , registry values
- registry WDK TCP/IP offload
- connection offload WDK TCP/IP transport , enabling services
- connection offload WDK TCP/IP transport , disabling services
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Registry Values to Enable and Disable Connection Offloading





When you debug a driver's connection offload functionality, you might find it useful to enable or disable connection offload services with a registry key setting. There are standardized keywords that you can define in INF files and in the registry. For more information about standardized keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

The connection offload keywords are defined as follows:

<a href="" id="-tcpconnectionoffloadipv4"></a>**\*TCPConnectionOffloadIPv4**  
Describes whether the device enabled or disabled the offload of TCP connections over IPv4.

<a href="" id="-tcpconnectionoffloadipv6"></a>**\*TCPConnectionOffloadIPv6**  
Describes whether the device enabled or disabled the offload of TCP connections over IPv6.

The following table describes the grouped keywords that you can use to configure offload services.

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
<td align="left"><p><strong><em>TCPConnectionOffloadIPv4</strong></p></td>
<td align="left"><p>TCP Connection Offload (IPv4)</p></td>
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
<td align="left"><p><strong></em>TCPConnectionOffloadIPv6</strong></p></td>
<td align="left"><p>TCP Connection Offload (IPv6)</p></td>
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

 

 

 





