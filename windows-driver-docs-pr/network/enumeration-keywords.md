---
title: Enumeration Keywords
description: Enumeration Keywords
keywords:
- installation keywords WDK networking , enumeration keywords
- enumeration keywords WDK NDIS miniport
ms.date: 4/08/2020
ms.localizationpriority: medium
---

# Enumeration Keywords

NDIS 6.0 and later versions of NDIS provide standardized enumeration keywords for miniport drivers of network devices. Enumeration keywords are associated with values that appear as a list in a menu.

The following example shows an INF file definition for an enumeration keyword.

```INF
HKR, Ndi\params\<SubkeyName>, ParamDesc, 0, "%<SubkeyName>%"
HKR, Ndi\params\<SubkeyName>, Type, 0, "enum"
HKR, Ndi\params\<SubkeyName>, Default, 0, "3"
HKR, Ndi\params\<SubkeyName>, Optional, 0, "0"
HKR, Ndi\params\<SubkeyName>\enum, "0", 0, "%Disabled%"
HKR, Ndi\params\<SubkeyName>\enum, "1", 0, "%Tx Enabled%"
HKR, Ndi\params\<SubkeyName>\enum, "2", 0, "%Rx Enabled%"
HKR, Ndi\params\<SubkeyName>\enum, "3", 0, "%Rx & Tx Enabled%"
```

The general enumeration keywords are:

**\*SpeedDuplex**  
Speed and duplex settings that a device supports. The device INF file should list only the settings that the associated device supports. That is, for an Ethernet 10/100 device that can support only full-duplex mode, settings for Gigabit or higher speeds or half duplex should not be listed in the associated INF file.

Speed values that are not specifically defined already with enumerated values of 0 through 10 may be set as a number that is the value directly in Mbps.  Direct values must be at least 1,000 Mbps (1 Gbps) and above.  Here are a few examples for specifying the speed directly:

| SpeedDuplex value | Resulting speed |
| ---| ---|
| 1,000 | 1 Gbps |
| 10,000 | 10 Gbps |
| 25,000 | 25 Gbps |
| 50,000 | 50 Gbps |
| 100,000 | 100 Gbps |

**\*FlowControl**  
The ability for the device to enable or disable flow control in the send or receive path.

**Note**  
Ethernet devices today support flow control, and the Windows 8 in-box drivers for LAN have flow control enabled by default. When a kernel debugger attaches to one of these LAN adapters, the NIC will start pushing flow control pause frames into the network. Most network switches will react by temporarily taking down the network for all other computers that are connected to the same hub. This is a common development scenario, and the end-user experience is both undesirable and difficult to diagnose.

**Note**  
Client and Server defaults are not the same; refer to the table of defaults below.

For this reason, in Windows 8 and later, NDIS will disable flow control automatically when debugging is enabled on the computer (for example, by typing **bcdedit /set debug on** at the command line). When kernel debugging is enabled and the miniport calls [**NdisReadConfiguration**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreadconfiguration) and passes "\*FlowControl" for the *Keyword* parameter, NDIS will override the configured value and return zero.

If you need to enable flow control while debugging, NDIS provides the **AllowFlowControlUnderDebugger** registry value to allow you to do that. The **AllowFlowControlUnderDebugger** registry value prevents NDIS from disabling flow control, and allows NICs to keep their configured behavior. It can be found under the following registry key:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**NDIS**\\**Parameters**

Set this registry value to 0x00000001.

If it does not exist, you can create a value with the name **AllowFlowControlUnderDebugger** and the type **REG\_DWORD** and set it to 0x00000001.

**\*PriorityVLANTag**  
A value that indicates whether the device has enabled or disabled the ability to insert the 802.1Q tags for packet priority and virtual LANs (VLANs). This keyword does not indicate whether the device enabled or disabled packet priority or VLAN tags. Instead, it describes the following:

- Whether the device inserts 802.1Q tags during a send operation
- Whether 802.1Q tag information is available in the [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) out-of-band (OOB) information
- Whether the device copies 802.1Q tags to OOB during receive operations

The miniport driver should remove the 802.1Q header from all receive packets regardless of the **\*PriorityVLANTag** setting. If the 802.1Q header is left in a packet, other drivers might not be able to parse the packet correctly.

If the Rx flag is enabled on the receive path, the miniport driver should copy the removed 802.1Q header into OOB.

Otherwise, if the Rx flag is disabled, the miniport driver should not copy the removed 802.1Q header into OOB.

If the Tx flag is enabled on the transmit path, the miniport driver should do the following:

- Insert the 802.1Q header into each outgoing packet and fill it up with the data from OOB (if any non-zero data exists in OOB).
- Advertise appropriate **MacOptions** in [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) (**NDIS\_MAC\_OPTION\_8021P\_PRIORITY** and **NDIS\_MAC\_OPTION\_8021Q\_VLAN**).

Otherwise, if the Tx flag is disabled, then:

- The miniport filter should not honor 802.1Q information in OOB (and therefore not insert any tag).
- The miniport filter should not advertise appropriate **MacOptions** in [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes).

**Note**  If the miniport driver supports NDIS quality of service (QoS), it must also read the **\*QOS** keyword value. Based on the **\*QOS** keyword value, the **\*PriorityVLANTag** keyword values are interpreted differently. For more information, see [Standardized INF Keywords for NDIS QoS](standardized-inf-keywords-for-ndis-qos.md).

 <a href="" id="-interruptmoderation"></a>**\*InterruptModeration**  
A value that describes whether the device enabled or disabled interrupt moderation. Interrupt moderation algorithms are device-dependent. The device manufacturer can use non-standardized keywords to support algorithmic settings. For more information about interrupt moderation, see [Interrupt Moderation](interrupt-moderation.md).

<a href="" id="-rss"></a>**\*RSS**  
A value that describes whether the device enabled or disabled receive side scaling (RSS). For more information about RSS, see [Receive Side Scaling](./receive-side-scaling-version-2-rssv2-.md).

<a href="" id="-headerdatasplit"></a>**\*HeaderDataSplit**  
A value that describes whether the device enabled or disabled header-data split. For more information about header-data split, see [Header-Data Split](header-data-split.md).

The following keywords are associated with connection offload services:

**\*TCPConnectionOffloadIPv4**

**\*TCPConnectionOffloadIPv6**

For more information about the connection offload keywords, see [Using Registry Values to Enable and Disable Connection Offloading](using-registry-values-to-enable-and-disable-connection-offloading.md).

The following keywords are associated with task offload services:

**\*IPChecksumOffloadIPv4**

**\*TCPChecksumOffloadIPv4**

**\*TCPChecksumOffloadIPv6**

**\*UDPChecksumOffloadIPv4**

**\*UDPChecksumOffloadIPv6**

**\*LsoV1IPv4**

**\*LsoV2IPv4**

**Note**  For devices that support both large send offload version 1 (LSOv1) and LSOv2 over IPv4, only the **\*LsoV2IPv4** keyword should be used in the INF file and registry values. If, for example, the **\*LsoV2IPv4** keyword appears in the INF file and the **\*LsoV1IPv4** keyword appears in the registry (or vice versa), the **\*LsoV2IPv4** keyword always takes precedence.

 **\*LsoV2IPv6**

**\*IPsecOffloadV1IPv4**

**\*IPsecOffloadV2**

**\*IPsecOffloadV2IPv4**

**\*TCPUDPChecksumOffloadIPv4**

**\*TCPUDPChecksumOffloadIPv6**

For more information about the TCP/IP offload keywords, see [Using Registry Values to Enable and Disable Task Offloading](using-registry-values-to-enable-and-disable-task-offloading.md).

The columns in the table at the end of this topic describe the following attributes for enumeration keywords:

SubkeyName  
The name of the keyword that you must specify in the INF file and that appears in the registry.

ParamDesc  
The display text that is associated with **SubkeyName**.

Value  
The enumeration integer value that is associated with each option in the list. This value is stored in **NDI\\params\\**<em>SubkeyName</em>**\\**<em>Value</em>.

EnumDesc  
The display text that is associated with each value that appears in the menu.

Default  
The default value for the menu.

The following table lists all of the keywords and describes the values that a driver must use for the preceding attributes. For more information about a keyword, search for the keyword in the WDK documentation.

|SubkeyName|ParamDesc|Value|EnumDesc|
|--- |--- |--- |--- |
|**\*SpeedDuplex**|Speed & Duplex|0 (Default)|Auto Negotiation|
|||1|10 Mbps Half Duplex|
|||2|10 Mbps Full Duplex|
|||3|100 Mbps Half Duplex|
|||4|100 Mbps Full Duplex|
|||5|1.0 Gbps Half Duplex|
|||6|1.0 Gbps Full Duplex|
|||7|10 Gbps Full Duplex|
|||8|20 Gbps Full Duplex|
|||9|40 Gbps Full Duplex|
|||10|100 Gbps Full Duplex|
|**\*FlowControl**|Flow Control|0 (Server Default)|Tx & Rx Disabled|
|||1|Tx Enabled|
|||2|Rx Enabled|
|||3 (Client Default)|Rx & Tx Enabled|
|||4|Auto Negotiation|
|**\*PriorityVLANTag**|Packet Priority & VLAN|0|Packet Priority & VLAN Disabled|
|||1|Packet Priority Enabled|
|||2|VLAN Enabled|
|||3 (Default)|Packet Priority & VLAN Enabled|
|**\*InterruptModeration**|Interrupt Moderation|0|Disabled|
|||1 (Default)|Enabled|
|**\*RSS**|Receive Side Scaling|0|Disabled|
|||1 (Default)|Enabled|
|**\*HeaderDataSplit**|Header Data Split|0 (Default)|Disabled|
|||1|Enabled|
|**\*TCPConnectionOffloadIPv4**|TCP Connection Offload (IPv4)|0|Disabled|
|||1 (Default)|Enabled|
|**\*TCPConnectionOffloadIPv6**|TCP Connection Offload (IPv6)|0|Disabled|
|||1 (Default)|Enabled|
|**\*IPChecksumOffloadIPv4**|IPv4 Checksum Offload|0|Disabled|
|||1|Tx Enabled|
|||2|Rx Enabled|
|||3 (Default)|Rx & Tx Enabled|
|**\*TCPChecksumOffloadIPv4**|TCP Checksum Offload (IPv4)|0|Disabled|
|||1|Tx Enabled|
|||2|Rx Enabled|
|||3 (Default)|Rx & Tx Enabled|
|**\*TCPChecksumOffloadIPv6**|TCP Checksum Offload (IPv6)|0|Disabled|
|||1|Tx Enabled|
|||2|Rx Enabled|
|||3 (Default)|Rx & Tx Enabled|
|**\*UDPChecksumOffloadIPv4**|UDP Checksum Offload (IPv4)|0|Disabled|
|||1|Tx Enabled|
|||2|Rx Enabled|
|||3 (Default)|Rx & Tx Enabled|
|**\*UDPChecksumOffloadIPv6**|UDP Checksum Offload (IPv6)|0|Disabled|
|||1|Tx Enabled|
|||2|Rx Enabled|
|||3 (Default)|Rx & Tx Enabled|
|**\*LsoV1IPv4**|Large Send Offload Version 1 (IPv4)|0|Disabled|
|||1 (Default)|Enabled|
|**\*LsoV2IPv4**|Large Send Offload Version 2 (IPv4)|0|Disabled|
|||1 (Default)|Enabled|
|**\*LsoV2IPv6**|Large Send Offload Version 2 (IPv6)|0|Disabled|
|||1 (Default)|Enabled|
|**\*IPsecOffloadV1IPv4**|IPsec Offload Version 1 (IPv4)|0|Disabled|
|||1|Auth Header Enabled|
|||2|ESP Enabled|
|||3 (Default)|Auth Header & ESP Enabled|
|**\*IPsecOffloadV2**|IPsec Offload|0|Disabled|
|||1|Auth Header Enabled|
|||2|ESP Enabled|
|||3 (Default)|Auth Header & ESP Enabled|
|**\*IPsecOffloadV2IPv4**|IPsec Offload (IPv4 only)|0|Disabled|
|||1|Auth Header Enabled|
|||2|ESP Enabled|
|||3 (Default)|Auth Header & ESP Enabled|
|**\*TCPUDPChecksumOffloadIPv4**|TCP/UDP Checksum Offload (IPv4)|0|Disabled|
|||1|Tx Enabled|
|||2|Rx Enabled|
|||3 (Default)|Tx and Rx Enabled|
|**\*TCPUDPChecksumOffloadIPv6**|TCP/UDP Checksum Offload (IPv6)|0|Disabled|
|||1|Tx Enabled|
|||2|Rx Enabled|
|||3 (Default)|Tx and Rx Enabled|


