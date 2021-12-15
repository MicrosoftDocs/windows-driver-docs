---
title: Using Registry Values to Enable and Disable Task Offloading
description: Using Registry Values to Enable and Disable Task Offloading
keywords:
- task offload WDK TCP/IP transport , registry values
- registry WDK TCP/IP offload
- task offload WDK TCP/IP transport , enabling services
- task offload WDK TCP/IP transport , disabling services
ms.date: 10/30/2020
ms.custom: contperf-fy21q2 
---

# Using Registry Values to Enable and Disable Task Offloading





When you debug a driver's task offload functionality, you might find it useful to enable or disable task offload services with a registry key setting. There are standardized keywords that you can define in INF files and in the registry. For more information about standardized keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

Task offload keywords belong to one of two groups: granular keywords or grouped keywords. *Granular keywords* provide keywords per offload capability--Transport Layer differentiation, IP protocol differentiation. *Grouped keywords* provide combined keywords capability at the transport layer.

## Granular keywords

The granular keywords are defined as follows:

|Keyword|Description|
|--- |--- |
|**\*IPChecksumOffloadIPv4**|Describes whether the device enabled or disabled the calculation of IPv4 checksums.|
|**\*TCPChecksumOffloadIPv4**|Describes whether the device enabled or disabled the calculation of TCP Checksum over IPv4 packets.|
|**\*TCPChecksumOffloadIPv6**|Describes whether the device enabled or disabled the calculation of TCP checksum over IPv6 packets.|
|**\*UDPChecksumOffloadIPv4**|Describes whether the device enabled or disabled the calculation of UDP Checksum over IPv4 packets.|
|**\*UDPChecksumOffloadIPv6**|Describes whether the device enabled or disabled the calculation of UDP Checksum over IPv6 packets.|
|**\*LsoV1IPv4**|Describes whether the device enabled or disabled the segmentation of large TCP packets over IPv4 for large send offload version 1 (LSOv1).|
|**\*LsoV2IPv4**|Describes whether the device enabled or disabled the segmentation of large TCP packets over IPv4 for large send offload version 2 (LSOv2).|
|**\*LsoV2IPv6**|Describes whether the device enabled or disabled the segmentation of large TCP packets over IPv6 for large send offload version 2 (LSOv2).|
|**\*IPsecOffloadV1IPv4** |Describes whether the device enabled or disabled the calculation of IPsec headers over IPv4.|
|**\*IPsecOffloadV2** |Describes whether the device enabled or disabled IPsec offload version 2 (IPsecOV2). IPsecOV2 provides support for additional crypto-algorithms, IPv6, and co-existence with large send offload version 2 (LSOv2).|
|**\*IPsecOffloadV2IPv4**  |Describes whether the device enabled or disabled IPsecOV2 for IPv4 only.|

The following table describes the granular keywords that you can use to configure offload services.

|SubkeyName|ParamDesc|Value|EnumDesc|
|--- |--- |--- |--- |
|**_IPChecksumOffloadIPv4_**|IPv4 Checksum Offload|0|Disabled|
|||1|Tx Enabled|
|||2|Rx Enabled|
|||3 (Default)|Rx & Tx Enabled|
|**TCPChecksumOffloadIPv4**|TCP Checksum Offload (IPv4)|0|Disabled|
|||1|Tx Enabled|
|||2|Rx Enabled|
|||3 (Default)|Rx & Tx Enabled|
|**_TCPChecksumOffloadIPv6_**|TCP Checksum Offload (IPv6)|0|Disabled|
|||1|Tx Enabled|
|||2|Rx Enabled|
|||3 (Default)|Rx & Tx Enabled|
|**UDPChecksumOffloadIPv4**|UDP Checksum Offload (IPv4)|0|Disabled|
|||1|Tx Enabled|
|||2|Rx Enabled|
|||3 (Default)|Rx & Tx Enabled|
|**_UDPChecksumOffloadIPv6_**|UDP Checksum Offload (IPv6)|0|Disabled|
|||1|Tx Enabled|
|||2|Rx Enabled|
|||3 (Default)|Rx & Tx Enabled|
|**LsoV1IPv4**|Large Send Offload Version 1 (IPv4)|0|Disabled|
|||1 (Default)|Enabled|
|**_LsoV2IPv4_**|Large Send Offload V2 (IPv4)|0|Disabled|
|||1 (Default)|Enabled|
|**LsoV2IPv6**|Large Send Offload V2 (IPv6)|0|Disabled|
|||1 (Default)|Enabled|
|**_IPsecOffloadV1IPv4_**|IPsec Offload Version 1 (IPv4)|0|Disabled|
|||1|Auth Header Enabled|
|||2|ESP Enabled|
|||3 (Default)|Auth Header & ESP Enabled|
|**IPsecOffloadV2**|IPsec Offload|0|Disabled|
|||1|Auth Header Enabled|
|||2|ESP Enabled|
|||3 (Default)|Auth Header & ESP Enabled|
|***IPsecOffloadV2IPv4**|IPsec Offload (IPv4 only)|0|Disabled|
|||1|Auth Header Enabled|
|||2|ESP Enabled|
|||3 (Default)|Auth Header & ESP Enabled|

 

> [!NOTE]
> The INF file can support granular keywords that are displayed in the Advanced Property page of the UI. The miniport driver must read all of the granular settings from the registry at initialization, including settings that are not displayed, to register NDIS offload capabilities.

## Grouped keywords

The grouped keywords are defined as follows:

|Keyword|Description|
|--- |--- |
|**\*TCPUDPChecksumOffloadIPv4**|Describes whether the device enabled or disabled the calculation of IP, TCP, and UDP checksum over IPv4.|
|**\*TCPUDPChecksumOffloadIPv6**|Describes whether the device enabled or disabled the calculation of TCP and UDP checksum over IPv6.|


The following table describes the grouped keywords that you can use to configure offload services.

|SubkeyName|ParamDesc|Value|EnumDesc|
|--- |--- |--- |--- |
|**_TCPUDPChecksumOffloadIPv4_**|TCP/UDP Checksum Offload (IPv4)|0|Disabled|
|||1|Tx Enabled|
|||2|Rx Enabled|
|||3 (Default)|Tx & Rx Enabled|
|**TCPUDPChecksumOffloadIPv6**|TCP/UDP Checksum Offload (IPv6)|0|Disabled|
|||1|Tx Enabled|
|||2|Rx Enabled|
|||3 (Default)|Tx & Rx Enabled|
 

There are restrictions on the combinations of offloads that can be enabled. For example, if a miniport adapter supports LSOV1 or LSOV2, the miniport adapter also calculates the IP and TCP checksums. For more information about valid combinations of offloads, see [Combining Types of Task Offloads](combining-types-of-task-offloads.md).

If task offload services are disabled with a registry key setting, protocol drivers must not issue the [OID\_OFFLOAD\_ENCAPSULATION](./oid-offload-encapsulation.md) object identifier (OID).

You can use the following registry values to enable or disable task offloading for the TCP/IP protocol:

<a href="" id="hkey-local-machine-system-currentcontrolset-services-tcpip-parameters-disabletaskoffload-------"></a>**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\TCPIP\\Parameters\\DisableTaskOffload**   
Setting this value to one disables all of the task offloads from the TCP/IP transport. Setting this value to zero enables all of the task offloads.

<a href="" id="hkey-local-machine-system-currentcontrolset-services-ipsec-enabledoffload-------"></a>**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\Ipsec\\EnabledOffload**   
Setting this value to zero disables Internet protocol security (IPsec) offloads from the TCP/IP transport. The offloading of TCP/IP checksum tasks, large send offload version 1 (LSOV1), and large send offload version 2 (LSOV2) are not affected. Setting this value to one enables IPsec offloads.

 

