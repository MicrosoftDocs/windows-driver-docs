---
title: Standardized INF Keywords for RSS
description: Standardized INF Keywords for RSS
ms.assetid: 0ea0d6f7-0dc5-40dd-a706-4712e19dbfdb
keywords:
- receive-side scaling WDK networking , standardized INF keywords
- RSS WDK networking , standardized INF keywords
- standardized INF keywords WDK RSS
- INF entries WDK RSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standardized INF Keywords for RSS





The RSS interface supports [standardized INF keywords](standardized-inf-keywords-for-network-devices.md) that appear in the registry and are specified in INF files.

The following list shows the enumeration [standardized INF keywords](standardized-inf-keywords-for-network-devices.md) for RSS:

<a href="" id="---------rss"></a> **\*RSS**  
Enable or disable support for RSS for miniport adapters.

<a href="" id="---------rssprofile"></a> **\*RSSProfile**  
The processor selection and load-balancing profile.

**Note**  Changes to the **\*RSSProfile** setting require an adapter restart.

 

Enumeration standardized INF keywords have the following attributes:

<a href="" id="subkeyname"></a>SubkeyName  
The name of the keyword that you must specify in the INF file and that appears in the registry.

<a href="" id="paramdesc"></a>ParamDesc  
The display text that is associated with SubkeyName.

<a href="" id="value"></a>Value  
The enumeration integer value that is associated with each option in the list. This value is stored in NDI\\params\\ *SubkeyName*\\*Value*.

<a href="" id="enumdesc"></a>EnumDesc  
The display text that is associated with each value that appears in the menu.

<a href="" id="default"></a>Default  
The default value for the menu.

The following table describes the possible INF entries for the RSS enumeration keywords.

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
<td align="left"><p><strong><em>RSS</strong></p></td>
<td align="left"><p>Receive Side Scaling</p></td>
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
<td align="left"><p><strong></em>RSSProfile</strong></p></td>
<td align="left"><p>RSS load balancing profile</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p><strong>ClosestProcessor</strong>: Default behavior is consistent with that of Windows Server 2008 R2.</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>2</p></td>
<td align="left"><p><strong>ClosestProcessorStatic</strong>: No dynamic load-balancing - Distribute but don&#39;t load-balance at runtime.</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>3</p></td>
<td align="left"><p><strong>NUMAScaling</strong>: Assign RSS CPUs in a round robin basis across every NUMA node to enable applications that are running on NUMA servers to scale well.</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>4</p>
<p>(Default)</p></td>
<td align="left"><p><strong>NUMAScalingStatic</strong>: RSS processor selection is the same as for NUMA scalability without dynamic load-balancing.</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>5</p></td>
<td align="left"><p><strong>ConservativeScaling</strong>: RSS uses as few processors as possible to sustain the load. This option helps reduce the number of interrupts.</p></td>
</tr>
</tbody>
</table>

 

NDIS 6.30 added support for **\*RSSProfile**.

The following list shows the [standardized INF keywords](standardized-inf-keywords-for-network-devices.md) for RSS that can be edited:

<a href="" id="---------rssbaseprocgroup"></a> **\*RssBaseProcGroup**  
The number of the processor group for the processor number that is specified in the **\*RssBaseProcNumber** keyword.

<a href="" id="---------numanodeid"></a> **\*NumaNodeId**  
The preferred NUMA node that is used for the memory allocations of the network adapter. Also, the operating system attempts to use the CPUs from the preferred NUMA node first for RSS.

A driver for a PCI expansion card should not specify the NUMA node ID statically in its INF, since the closest node depends on which PCI slot the card is plugged into.  Only specify **\*NumaNodeId** if the network adapter is integrated into the system, the NUMA node is known in advance, and the node cannot be determined at runtime by querying ACPI.

**Note**  If this keyword is present and its value is less than the number of NUMA nodes in the computer, NDIS uses this value in the **PreferredNumaNode** member in the [**NDIS\_RSS\_PROCESSOR\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567274) structure.

 

**Note**  In Windows 8 the **\*NumaNodeId** value is ignored if the NIC RSS profile is set to **NUMAScaling**(2) or **NUMAScalingStatic**(3).

 

<a href="" id="---------rssbaseprocnumber"></a> **\*RssBaseProcNumber**  
The number of the base RSS processor in the specified group.

<a href="" id="---------maxrssprocessors"></a> **\*MaxRssProcessors**  
The maximum number of RSS processors.

<a href="" id="---------rssmaxprocnumber"></a> **\*RssMaxProcNumber**  
The maximum processor number of the RSS interface.
If **\*RssMaxProcNumber** is specified, then **\*RssMaxProcGroup** should also be specified.

<a href="" id="---------rssmaxprocnumber"></a> **\*RssMaxProcNumber**  
The maximum processor number of the RSS interface.
If **\*RssMaxProcNumber** is specified, then **\*RssMaxProcGroup** should also be specified.

<a href="" id="---------rssmaxprocgroup"></a> **\*RssMaxProcGroup**
The maximum processor group of the RSS interface.

**\*RssBaseProcGroup** together with **\*RssBaseProcNumber** form a PROCESSOR_NUMBER structure that identifies the smallest processor number that can be used with RSS.
**\*RssMaxProcGroup** together with **\*RssMaxProcNumber** form a PROCESSOR_NUMBER structure that identifies the maximum processor number that can be used with RSS.

For example, suppose **\*RssBaseProcGroup** is set to 1, **\*RssBaseProcNumber** is set to 16, **\*RssMaxProcGroup** is set to 3, and **\*RssMaxProcNumber** is set to 8.
Using <group>:<processor> notation, the base processor is 1:16 and the max processor is 3:8.
Then processors 0:0, 0:32, 1:0, and 1:15 will not be considered candidates for RSS, because they are below the base processor number.
Processors 1:16, 1:31, 2:0, 2:63, 3:0, and 3:8 will all be considered candidates for RSS, because they fall in the range 1:16 through 3:8.
Processors 3:9, 3:31, and 4:0 will not be considered candidates for RSS, because they are beyond the maximum processor number.

NDIS 6.20 added support for the **\*RssBaseProcGroup**, **\*NumaNodeId**, **\*RssBaseProcNumber**, and **\*MaxRssProcessors** keywords.

NDIS 6.30 added support for the **\*RssMaxProcNumber**, and **\*NumRSSQueues** keywords.

[Standardized INF keywords](standardized-inf-keywords-for-network-devices.md) that can be edited have the following attributes:

<a href="" id="subkeyname"></a>SubkeyName  
The name of the keyword that you must specify in the INF file and that appears in the registry.

<a href="" id="paramdesc"></a>ParamDesc  
The display text that is associated with SubkeyName.

<a href="" id="type"></a>Type  
The type of value that can be edited. The value can be either numeric (Int) or text that can be edited (Edit).

<a href="" id="default-value"></a>Default value  
The default value for the integer or text. &lt;IHV defined&gt; indicates that the value is associated with the particular independent hardware vendor (IHV) requirements.

<a href="" id="min"></a>Min  
The minimum value that is allowed for an integer. &lt;IHV defined&gt; indicates that the minimum value is associated with the particular IHV requirements.

<a href="" id="max"></a>Max  
The maximum value that is allowed for an integer. &lt;IHV defined&gt; indicates that the minimum value is associated with the particular IHV requirements.

The following table describes all of the RSS keywords that can be edited.

<table style="width:100%;">
<colgroup>
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">SubkeyName</th>
<th align="left">ParamDesc</th>
<th align="left">Type</th>
<th align="left">Default value</th>
<th align="left">Min</th>
<th align="left">Max</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong><em>RssBaseProcGroup</strong></p></td>
<td align="left"><p>RSS Base Processor Group</p></td>
<td align="left"><p>Int</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>MAXIMUM_GROUPS-1</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em>NumaNodeId</strong></p></td>
<td align="left"><p>Preferred NUMA node</p></td>
<td align="left"><p>Int</p></td>
<td align="left"><p>65535 (Any node)</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>System specific - cannot exceed 65534</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em>RssBaseProcNumber</strong></p></td>
<td align="left"><p>RSS Base Processor Number</p></td>
<td align="left"><p>Int</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>MAXIMUM_PROC_PER_GROUP-1</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em>MaxRssProcessors</strong></p></td>
<td align="left"><p>Maximum number of RSS Processors</p></td>
<td align="left"><p>Int</p></td>
<td align="left"><p>Windows Server 2008 defaults:</p>
<p>8 for 1G or slower adapters, 16 for 10G adapters</p>
<p>Windows 8 defaults:</p>
<p>For NICs with no MSI-X support - 2 for 1GbE or slower adapters, 4 for 10 GbE adapters.</p>
<p>For NICs with MSI-X support - 4 for 1GbE or slower adapters, 16 for 10 GbE adapters.</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>MAXIMUM_PROC_PER_SYSTEM</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em>RssMaxProcNumber</strong></p></td>
<td align="left"><p>Maximum RSS Processor Number</p></td>
<td align="left"><p>Int</p></td>
<td align="left"><p>MAXIMUM_PROC_PER_GROUP-1 (Default)</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>MAXIMUM_PROC_PER_GROUP-1</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em>NumRSSQueues</strong></p></td>
<td align="left"><p>Maximum Number of RSS Queues</p></td>
<td align="left"><p>Int</p></td>
<td align="left"><p>Device-specific</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Device-specific</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>*RSSMaxProcGroup</strong></p></td>
<td align="left"><p>RSS Max Processor Group</p></td>
<td align="left"><p>Int</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>MAXIMUM_GROUPS-1</p></td>
</tr>
</tbody>
</table>

 

**Note**  Although the valid range for **\*RssBaseProcGroup** is zero to MAXIMUM\_GROUPS-1, in Windows 7 it must be zero. Otherwise, the TCP/IP protocol will not use any processors for RSS.

 

**Note**  The default value for **\*NumaNodeId** (65535) means the network adapter is agnostic to NUMA node, and NDIS should not attempt to prefer any node over another.
If the **\*NumaNodeId** keyword is not present, then NDIS automatically selects the closest node based on hints from ACPI.


For more information about standardized INF keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

 

 





