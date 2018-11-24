---
title: Using Registry Values to Enable and Disable Task Offloading
description: Using Registry Values to Enable and Disable Task Offloading
ms.assetid: 32efd685-365c-4347-9599-fe429569d35b
keywords:
- task offload WDK TCP/IP transport , registry values
- registry WDK TCP/IP offload
- task offload WDK TCP/IP transport , enabling services
- task offload WDK TCP/IP transport , disabling services
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Registry Values to Enable and Disable Task Offloading





When you debug a driver's task offload functionality, you might find it useful to enable or disable task offload services with a registry key setting. There are standardized keywords that you can define in INF files and in the registry. For more information about standardized keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

Task offload keywords belong to one of two groups: granular keywords or grouped keywords. *Granular keywords* provide keywords per offload capability--Transport Layer differentiation, IP protocol differentiation. *Grouped keywords* provide combined keywords capability at the transport layer.

The granular keywords are defined as follows:

<a href="" id="-ipchecksumoffloadipv4"></a>**\*IPChecksumOffloadIPv4**  
Describes whether the device enabled or disabled the calculation of IPv4 checksums.

<a href="" id="-tcpchecksumoffloadipv4"></a>**\*TCPChecksumOffloadIPv4**  
Describes whether the device enabled or disabled the calculation of TCP Checksum over IPv4 packets.

<a href="" id="-tcpchecksumoffloadipv6"></a>**\*TCPChecksumOffloadIPv6**  
Describes whether the device enabled or disabled the calculation of TCP checksum over IPv6 packets.

<a href="" id="-udpchecksumoffloadipv4"></a>**\*UDPChecksumOffloadIPv4**  
Describes whether the device enabled or disabled the calculation of UDP Checksum over IPv4 packets.

<a href="" id="-udpchecksumoffloadipv6"></a>**\*UDPChecksumOffloadIPv6**  
Describes whether the device enabled or disabled the calculation of UDP Checksum over IPv6 packets.

<a href="" id="-lsov1ipv4"></a>**\*LsoV1IPv4**  
Describes whether the device enabled or disabled the segmentation of large TCP packets over IPv4 for large send offload version 1 (LSOv1).

<a href="" id="-lsov2ipv4"></a>**\*LsoV2IPv4**  
Describes whether the device enabled or disabled the segmentation of large TCP packets over IPv4 for large send offload version 2 (LSOv2).

<a href="" id="-lsov2ipv6"></a>**\*LsoV2IPv6**  
Describes whether the device enabled or disabled the segmentation of large TCP packets over IPv6 for large send offload version 2 (LSOv2).

<a href="" id="-ipsecoffloadv1ipv4"></a>**\*IPsecOffloadV1IPv4**  
Describes whether the device enabled or disabled the calculation of IPsec headers over IPv4.

<a href="" id="-ipsecoffloadv2"></a>**\*IPsecOffloadV2**  
Describes whether the device enabled or disabled IPsec offload version 2 (IPsecOV2). IPsecOV2 provides support for additional crypto-algorithms, IPv6, and co-existence with large send offload version 2 (LSOv2).

<a href="" id="-ipsecoffloadv2ipv4"></a>**\*IPsecOffloadV2IPv4**  
Describes whether the device enabled or disabled IPsecOV2 for IPv4 only.

The following table describes the granular keywords that you can use to configure offload services.

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
<td align="left"><p><strong><em>IPChecksumOffloadIPv4</strong></p></td>
<td align="left"><p>IPv4 Checksum Offload</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Tx Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Rx Enabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>3 (Default)</p></td>
<td align="left"><p>Rx &amp; Tx Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong></em>TCPChecksumOffloadIPv4</strong></p></td>
<td align="left"><p>TCP Checksum Offload (IPv4)</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Tx Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Rx Enabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>3 (Default)</p></td>
<td align="left"><p>Rx &amp; Tx Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em>TCPChecksumOffloadIPv6</strong></p></td>
<td align="left"><p>TCP Checksum Offload (IPv6)</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Tx Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Rx Enabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>3 (Default)</p></td>
<td align="left"><p>Rx &amp; Tx Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong></em>UDPChecksumOffloadIPv4</strong></p></td>
<td align="left"><p>UDP Checksum Offload (IPv4)</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Tx Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Rx Enabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>3 (Default)</p></td>
<td align="left"><p>Rx &amp; Tx Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em>UDPChecksumOffloadIPv6</strong></p></td>
<td align="left"><p>UDP Checksum Offload (IPv6)</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Tx Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Rx Enabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>3 (Default)</p></td>
<td align="left"><p>Rx &amp; Tx Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong></em>LsoV1IPv4</strong></p></td>
<td align="left"><p>Large Send Offload Version 1 (IPv4)</p></td>
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
<td align="left"><p><strong><em>LsoV2IPv4</strong></p></td>
<td align="left"><p>Large Send Offload V2 (IPv4)</p></td>
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
<td align="left"><p><strong></em>LsoV2IPv6</strong></p></td>
<td align="left"><p>Large Send Offload V2 (IPv6)</p></td>
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
<td align="left"><p><strong><em>IPsecOffloadV1IPv4</strong></p></td>
<td align="left"><p>IPsec Offload Version 1 (IPv4)</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Auth Header Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>2</p></td>
<td align="left"><p>ESP Enabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>3 (Default)</p></td>
<td align="left"><p>Auth Header &amp; ESP Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong></em>IPsecOffloadV2</strong></p></td>
<td align="left"><p>IPsec Offload</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Auth Header Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>2</p></td>
<td align="left"><p>ESP Enabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>3 (Default)</p></td>
<td align="left"><p>Auth Header &amp; ESP Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>*IPsecOffloadV2IPv4</strong></p></td>
<td align="left"><p>IPsec Offload (IPv4 only)</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Auth Header Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>2</p></td>
<td align="left"><p>ESP Enabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>3 (Default)</p></td>
<td align="left"><p>Auth Header &amp; ESP Enabled</p></td>
</tr>
</tbody>
</table>

 

**Note**  The INF file can support granular keywords that are displayed in the Advanced Property page of the UI. The miniport driver must read all of the granular settings from the registry at initialization, including settings that are not displayed, to register NDIS offload capabilities.

 

The grouped keywords are defined as follows:

<a href="" id="-tcpudpchecksumoffloadipv4"></a>**\*TCPUDPChecksumOffloadIPv4**  
Describes whether the device enabled or disabled the calculation of IP, TCP, and UDP checksum over IPv4.

<a href="" id="-tcpudpchecksumoffloadipv6"></a>**\*TCPUDPChecksumOffloadIPv6**  
Describes whether the device enabled or disabled the calculation of TCP and UDP checksum over IPv6.

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
<td align="left"><p><strong><em>TCPUDPChecksumOffloadIPv4</strong></p></td>
<td align="left"><p>TCP/UDP Checksum Offload (IPv4)</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Tx Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Rx Enabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>3 (Default)</p></td>
<td align="left"><p>Tx &amp; Rx Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong></em>TCPUDPChecksumOffloadIPv6</strong></p></td>
<td align="left"><p>TCP/UDP Checksum Offload (IPv6)</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Tx Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Rx Enabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>3 (Default)</p></td>
<td align="left"><p>Tx &amp; Rx Enabled</p></td>
</tr>
</tbody>
</table>

 

There are restrictions on the combinations of offloads that can be enabled. For example, if a miniport adapter supports LSOV1 or LSOV2, the miniport adapter also calculates the IP and TCP checksums. For more information about valid combinations of offloads, see [Combining Types of Task Offloads](combining-types-of-task-offloads.md).

If task offload services are disabled with a registry key setting, protocol drivers must not issue the [OID\_OFFLOAD\_ENCAPSULATION](https://msdn.microsoft.com/library/windows/hardware/ff569762) object identifier (OID).

You can use the following registry values to enable or disable task offloading for the TCP/IP protocol:

<a href="" id="hkey-local-machine-system-currentcontrolset-services-tcpip-parameters-disabletaskoffload-------"></a>**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\TCPIP\\Parameters\\DisableTaskOffload**   
Setting this value to one disables all of the task offloads from the TCP/IP transport. Setting this value to zero enables all of the task offloads.

<a href="" id="hkey-local-machine-system-currentcontrolset-services-ipsec-enabledoffload-------"></a>**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\Ipsec\\EnabledOffload**   
Setting this value to zero disables Internet protocol security (IPsec) offloads from the TCP/IP transport. The offloading of TCP/IP checksum tasks, large send offload version 1 (LSOV1), and large send offload version 2 (LSOV2) are not affected. Setting this value to one enables IPsec offloads.

 

 





