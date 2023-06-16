---
title: Standardized INF Keywords for RSS
description: Standardized INF Keywords for RSS
keywords:
- receive-side scaling WDK networking , standardized INF keywords
- RSS WDK networking , standardized INF keywords
- standardized INF keywords WDK RSS
- INF entries WDK RSS
ms.date: 06/14/2023
---

# Standardized INF Keywords for RSS

The RSS interface supports [standardized INF keywords](standardized-inf-keywords-for-network-devices.md) that appear in the registry and are specified in INF files.

The following list shows the enumeration [standardized INF keywords](standardized-inf-keywords-for-network-devices.md) for RSS:

**\*RSS**  
Enable or disable support for RSS for miniport adapters.

**\*RSSProfile**  
The processor selection and load-balancing profile.

**Note:** Changes to the **\*RSSProfile** setting require an adapter restart.

**Note:** If **\*RSSProfile** is set to **NdisRssProfileBalanced**, you can't configure advanced keywords such as **\*RssBaseProcNumber**, **\*RssBaseProcGroup**,  **\*RssMaxProcNumber**,  **\*RssMaxProcGroup**, or **\*NumaNodeId**. You can configure **\*MaxRssProcessors** and **\*NumRSSQueues**. 

NDIS 6.30 added support for **\*RSSProfile**.

Enumeration standardized INF keywords have the following attributes:

SubkeyName  
The name of the keyword that you must specify in the INF file and that appears in the registry.

ParamDesc  
The display text that is associated with SubkeyName.

Value  
The enumeration integer value that is associated with each option in the list. This value is stored in NDI\\params\\ *SubkeyName*\\*Value*.
EnumDesc  
The display text that is associated with each value that appears in the menu.

Default  
The default value for the menu.

The following table describes the possible INF entries for the RSS enumeration keywords.

|SubkeyName|ParamDesc|Value|EnumDesc|
|--- |--- |--- |--- |
|**\*RSS**|Receive Side Scaling|0|Disabled|
|||1 (Default)|Enabled|
|**\*RSSProfile**|RSS load balancing profile|1|**ClosestProcessor**: Default behavior is consistent with that of Windows Server 2008 R2.|
|||2|**ClosestProcessorStatic**: No dynamic load-balancing - Distribute but don't load-balance at runtime.|
|||3|**NUMAScaling**: Assign RSS CPUs in a round robin basis across every NUMA node to enable applications that are running on NUMA servers to scale well.|
|||4 (Default)|**NUMAScalingStatic**: RSS processor selection is the same as for NUMA scalability without dynamic load-balancing.|
|||5|**ConservativeScaling**: RSS uses as few processors as possible to sustain the load. This option helps reduce the number of interrupts.|
|||6 (Default on heterogeneous CPU systems)|**NdisRssProfileBalanced**: RSS processor selection is based on traffic workload. Only available in [NetAdapterCx](../netcx/netadaptercx-receive-side-scaling-rss-.md), starting in WDK preview version 25197.|

The following list shows the [standardized INF keywords](standardized-inf-keywords-for-network-devices.md) for RSS that can be edited:

**\*RssBaseProcGroup**  
The number of the processor group for the processor number that is specified in the **\*RssBaseProcNumber** keyword.

**\*NumaNodeId**  
The preferred NUMA node that is used for the memory allocations of the network adapter. Also, the operating system attempts to use the CPUs from the preferred NUMA node first for RSS.

A driver for a PCI expansion card should not specify the NUMA node ID statically in its INF, since the closest node depends on which PCI slot the card is plugged into.  Only specify **\*NumaNodeId** if the network adapter is integrated into the system, the NUMA node is known in advance, and the node cannot be determined at runtime by querying ACPI.

**Note:** If this keyword is present and its value is less than the number of NUMA nodes in the computer, NDIS uses this value in the **PreferredNumaNode** member in the [**NDIS\_RSS\_PROCESSOR\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_rss_processor_info) structure.

 

**Note:** In Windows 8 the **\*NumaNodeId** value is ignored if the NIC RSS profile is set to **NUMAScaling**(2) or **NUMAScalingStatic**(3).

 

 **\*RssBaseProcNumber**  
The number of the base RSS processor in the specified group.

 **\*MaxRssProcessors**  
The maximum number of RSS processors.

 **\*RssMaxProcNumber**  
The maximum processor number of the RSS interface.
If **\*RssMaxProcNumber** is specified, then **\*RssMaxProcGroup** should also be specified.

 **\*NumRSSQueues**  
The number of RSS queues.

 **\*RssMaxProcGroup**
The maximum processor group of the RSS interface.

**\*RssBaseProcGroup** together with **\*RssBaseProcNumber** form a PROCESSOR_NUMBER structure that identifies the smallest processor number that can be used with RSS.
**\*RssMaxProcGroup** together with **\*RssMaxProcNumber** form a PROCESSOR_NUMBER structure that identifies the maximum processor number that can be used with RSS.

For example, suppose **\*RssBaseProcGroup** is set to 1, **\*RssBaseProcNumber** is set to 16, **\*RssMaxProcGroup** is set to 3, and **\*RssMaxProcNumber** is set to 8.
Using `<group>:<processor>` notation, the base processor is 1:16 and the max processor is 3:8.
Then processors 0:0, 0:32, 1:0, and 1:15 will not be considered candidates for RSS, because they are below the base processor number.
Processors 1:16, 1:31, 2:0, 2:63, 3:0, and 3:8 will all be considered candidates for RSS, because they fall in the range 1:16 through 3:8.
Processors 3:9, 3:31, and 4:0 will not be considered candidates for RSS, because they are beyond the maximum processor number.

NDIS 6.20 added support for the **\*RssBaseProcGroup**, **\*NumaNodeId**, **\*RssBaseProcNumber**, and **\*MaxRssProcessors** keywords.

NDIS 6.30 added support for the **\*RssMaxProcNumber**, and **\*NumRSSQueues** keywords.

[Standardized INF keywords](standardized-inf-keywords-for-network-devices.md) that can be edited have the following attributes:

SubkeyName  
The name of the keyword that you must specify in the INF file and that appears in the registry.

ParamDesc  
The display text that is associated with SubkeyName.

Type  
The type of value that can be edited. The value can be either numeric (Int) or text that can be edited (Edit).

Default value  
The default value for the integer or text. &lt;IHV defined&gt; indicates that the value is associated with the particular independent hardware vendor (IHV) requirements.

Min  
The minimum value that is allowed for an integer. &lt;IHV defined&gt; indicates that the minimum value is associated with the particular IHV requirements.

Max  
The maximum value that is allowed for an integer. &lt;IHV defined&gt; indicates that the minimum value is associated with the particular IHV requirements.

The following table describes all of the RSS keywords that can be edited.


|SubkeyName|ParamDesc|Type|Default value|Min|Max|
|--- |--- |--- |--- |--- |--- |
|**\*RssBaseProcGroup**|RSS Base Processor Group|Int|0|0|MAXIMUM_GROUPS-1|
|**\*NumaNodeId**|Preferred NUMA node|Int|65535 (Any node)|0|System specific - cannot exceed 65535|
|**\*RssBaseProcNumber**|RSS Base Processor Number|Int|0|0|MAXIMUM_PROC_PER_GROUP-1|
|**\*MaxRssProcessors**|Maximum number of RSS Processors|Int|16|1|MAXIMUM_PROC_PER_SYSTEM|
|**\*RssMaxProcNumber**|Maximum RSS Processor Number|Int|MAXIMUM_PROC_PER_GROUP-1 (Default)|0|MAXIMUM_PROC_PER_GROUP-1|
|**\*NumRSSQueues**|Maximum Number of RSS Queues|Int|16|1|Device-specific|
|**\*RSSMaxProcGroup**|RSS Max Processor Group|Int|0|0|MAXIMUM_GROUPS-1|
 

**Note:** Although the valid range for **\*RssBaseProcGroup** is zero to MAXIMUM\_GROUPS-1, in Windows 7 it must be zero. Otherwise, the TCP/IP protocol will not use any processors for RSS.


**Note:** The default value for **\*NumaNodeId** (65535) means the network adapter is agnostic to NUMA node, and NDIS should not attempt to prefer any node over another.
If the **\*NumaNodeId** keyword is not present, then NDIS automatically selects the closest node based on hints from ACPI.

**Note:** The max value for **\*MaxRssProcessors** may be set to the maximum number of processors that the NIC can support. NDIS will automatically cap this value to be the maximum number of processors on the current system.

For more information about standardized INF keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

 

