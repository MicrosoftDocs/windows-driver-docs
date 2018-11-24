---
title: Standardized INF Keywords for VMQ
description: Standardized INF Keywords for VMQ
ms.assetid: 5DA92019-D2E0-41D9-9C31-94E464B824BA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standardized INF Keywords for VMQ


The following standardized INF keywords are defined to enable or disable support for the virtual machine queue (VMQ) features of network adapters.

<a href="" id="-vmq"></a>**\*VMQ**  
A value that describes whether the device has enabled or disabled the VMQ feature.

<a href="" id="-vmqlookaheadsplit"></a>**\*VMQLookaheadSplit**  
A value that describes whether the device has enabled or disabled the ability to split receive buffers into lookahead and post-lookahead buffers. The miniport driver reports this capability with the NDIS\_RECEIVE\_FILTER\_LOOKAHEAD\_SPLIT\_SUPPORTED flag in the **SupportedQueueProperties** member of the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure. For more information about this feature, see [Shared Memory in Receive Buffers](shared-memory-in-receive-buffers.md).

**Note**  Starting with NDIS 6.30, splitting packet data into separate lookahead buffers is no longer supported. Starting with Windows Server 2012, this INF keyword is obsolete.



<a href="" id="-vmqvlanfiltering"></a>**\*VMQVlanFiltering**  
A value that describes whether the device has enabled or disabled the ability to filter network packets by using the VLAN identifier in the media access control (MAC) header. The miniport driver reports this capability with the NDIS\_RECEIVE\_FILTER\_MAC\_HEADER\_VLAN\_ID\_SUPPORTED flag in **SupportedMacHeaderFields** member of the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure.

<a href="" id="-rssorvmqpreference"></a>**\*RssOrVmqPreference**  
A value that defines whether VMQ capabilities should be enabled instead of receive side scaling (RSS) capabilities.

This is a hidden keyword value that must not be specified in the INF file and is not displayed in **Advanced** property page for the network adapter. For more information, see [Handling VMQ and RSS INF Keywords](#vmq-rss).

VMQ standardized INF keywords are enumeration keywords. The following table describes the possible INF entries for the VMQ standardized INF keywords.

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
<td align="left"><p><strong><em>VMQ</strong></p></td>
<td align="left"><p>Virtual Machine Queues</p></td>
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
<td align="left"><p><strong></em>VMQLookaheadSplit</strong></p></td>
<td align="left"><p>VMQ Lookahead Split</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p>
<div class="alert">
<strong>Note</strong>  Starting with NDIS 6.30, this keyword is no longer supported.
</div>
<div>

</div></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1 (Default)</p></td>
<td align="left"><p>Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em>VMQVlanFiltering</strong></p></td>
<td align="left"><p>VMQ VLAN Filtering</p></td>
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
<td align="left"><p><strong></em>RssOrVmqPreference</strong></p></td>
<td align="left"><p>Note: The ParamDesc and EnumDesc entries for this subkey cannot be used in either INF files or a user interface. For more information, see <a href="#vmq-rss" data-raw-source="[Handling VMQ and RSS INF Keywords](#vmq-rss)">Handling VMQ and RSS INF Keywords</a>.</p></td>
<td align="left"><p>0 (Default)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  Report RSS capabilities
</div>
<div>

</div></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1</p></td>
<td align="left"><div class="alert">
<strong>Note</strong><br/><p>Report VMQ capabilities</p>
</div>
<div>

</div></td>
</tr>
</tbody>
</table>



The columns in this table describe the following attributes for an enumeration keyword:

<a href="" id="subkeyname"></a>SubkeyName  
The name of the keyword that you must specify in the INF file. This name also appears in the registry under the **NDI**\\**params** key for the network adapter.

<a href="" id="paramdesc"></a>ParamDesc  
The display text that is associated with the SubkeyName INF entry.

**Note**  The independent hardware vendor (IHV) can define any descriptive text for the SubkeyName.



<a href="" id="value"></a>Value  
The enumeration integer value that is associated with each SubkeyName in the list.

<a href="" id="enumdesc"></a>EnumDesc  
The display text that is associated with each value that appears in the **Advanced** property page.

For more information about standardized INF keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

### <a href="" id="vmq-rss"></a>Handling VMQ and RSS INF Keywords

Network adapters that support VMQ and receive side scaling (RSS) cannot use these features simultaneously. The operating system enables the use of the RSS or VMQ features in the following way:

-   When the network adapter is bound to the TCP/IP stack, the operating enables the use of the RSS feature.

-   When the network adapter is bound to the Hyper-V extensible switch driver stack, the operating system enables the use of the VMQ feature.

    For more information, see [Hyper-V Extensible Switch](hyper-v-extensible-switch.md).

Because the network adapter is not disabled and then re-enabled when it is unbound from the TCP/IP stack and bound to the Hyper-V driver stack (or the reverse), it is not possible for such network adapters to switch between VMQ and RSS automatically.

When NDIS calls the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, the miniport driver follows these steps before it reports its currently-enabled VMQ or RSS capabilities to NDIS:

1.  The miniport driver reads the **\*RssOrVmqPreference** keyword before reporting its currently-enabled capabilities to NDIS.

    If the value of the **\*RssOrVmqPreference** keyword is 1, the miniport driver is configured for VMQ preference.

    If the value of the **\*RssOrVmqPreference** keyword is zero or the keyword is not present, the miniport driver is configured for RSS preference.

2.  If the miniport driver is configured for VMQ preference, it must read the **\*VMQ** keyword to determine if VMQ is enabled on the network adapter. If the keyword is set to 1, the driver reports the currently-enabled VMQ settings. For more information on how the miniport driver reports VMQ settings, see [Determining the VMQ Capabilities of a Network Adapter](determining-the-vmq-capabilities-of-a-network-adapter.md).

    For more information about the VMQ keywords, see Standardized INF Keywords for VMQ.

    **Note**  If the miniport driver is configured for VMQ preference, it must not read any of the RSS standardized keywords.



3.  If the miniport driver is configured for RSS preference, it must read the **\*RSS** keyword to determine if RSS is enabled on the network adapter. If the keyword is set to 1, the driver reports the currently-enabled RSS settings. For more information on how the miniport driver reports RSS settings, see [RSS Configuration](rss-configuration.md).

    For more information about the RSS keywords, see [Standardized INF Keywords for RSS](standardized-inf-keywords-for-rss.md).

    **Note**  If the miniport driver is configured for RSS preference, it must not read any of the VMQ standardized keywords.



The following table describes how the miniport driver determines RSS or VMQ preference and advertises capabilities based on registry keywords:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left"><em>RssOrVmqPreference</th>
<th align="left"></em>VMQ</th>
<th align="left">*RSS</th>
<th align="left">VMQ or RSS capabilities advertised</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>VMQ</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>None</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0, or not present in registry</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>RSS</p></td>
</tr>
<tr class="even">
<td align="left"><p>0, or not present in registry</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>None</p></td>
</tr>
</tbody>
</table>



**Note**  The miniport driver must always report the complete RSS and VMQ hardware capabilities regardless of the values of these keywords. These keyword settings only affect how the driver reports the currently-enabled RSS and VMQ capabilities.



### Reserved Registry Keywords

If the miniport driver supports VMQ and the VMQ interface is enabled on the network adapter, the driver must not read the following RSS INF entries:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">SubkeyName</th>
<th align="left">ParamDesc</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p></p>
<p><strong><em>RssMaxProcNumber</strong></p></td>
<td align="left"><p>The maximum processor number of the RSS interface.</p></td>
<td align="left"><p>0 through (MAXIMUM_PROC_PER_GROUP-1),</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p><strong></em>MaxRssProcessors</strong></p></td>
<td align="left"><p>The maximum number of RSS processors.</p></td>
<td align="left"><p>1 through MAXIMUM_PROC_PER_SYSTEM.</p></td>
</tr>
</tbody>
</table>



The miniport driver that supports VMQ must not read the following subkeys under the **HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**services**\\**VMSMP**\\**Parameters** registry key.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">SubkeyName</th>
<th align="left">ParamDesc</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p></p>
<p><strong>TenGigVmqEnabled</strong></p></td>
<td align="left"><p>Enable or disable VMQ on all 10 gigabits per second (Gbps) network adapters.</p></td>
<td align="left"><p>0=System default (disabled for Windows Server 2008 R2).</p>
<p>1=Enabled.</p>
<p>2=Explicitly disabled.</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p><strong>BelowTenGigVmqEnabled</strong></p></td>
<td align="left"><p>Enable or disable VMQ on all network adapters that support less than 10 Gbps.</p></td>
<td align="left"><p>0=System default (disabled for Windows Server 2008 R2).</p>
<p>1=Enabled.</p>
<p>2=Explicitly disabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<p><strong><em>RssMaxProcNumber</strong></p></td>
<td align="left"><p>The maximum processor number of the RSS interface.</p></td>
<td align="left"><p>0 through (MAXIMUM_PROC_PER_GROUP-1),</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p><strong></em>MaxRssProcessors</strong></p></td>
<td align="left"><p>The maximum number of RSS processors.</p></td>
<td align="left"><p>1 through MAXIMUM_PROC_PER_SYSTEM.</p></td>
</tr>
</tbody>
</table>











