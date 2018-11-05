---
title: Handling SR-IOV, VMQ, and RSS Standardized INF Keywords
description: Handling SR-IOV, VMQ, and RSS Standardized INF Keywords
ms.assetid: EF556563-4097-4388-A563-29FC891AC626
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling SR-IOV, VMQ, and RSS Standardized INF Keywords


Network adapters that support single root I/O virtualization (SR-IOV), virtual machine queue (VMQ), and receive side scaling (RSS) can enable the use of these interfaces in the following way:

-   SR-IOV and VMQ can be enabled individually or at the same time.

-   RSS cannot be enabled on the network adapter when SR-IOV or VMQ is enabled.

The operating system enables the use of the SR-IOV, VMQ, or RSS interfaces in the following way:

-   When the network adapter is bound to the TCP/IP stack, the operating enables the use of the RSS feature.

-   When the network adapter is bound to the Hyper-V extensible switch driver stack, the operating system enables the use of either the SR-IOV or VMQ feature.

    For more information about the Hyper-V extensible switch, see [Hyper-V Extensible Switch](hyper-v-extensible-switch.md).

When the network adapter is unbound from the TCP/IP stack and the Hyper-V extensible switch driver stack, the miniport driver is halted and then reinitialized. Because of this, it is not possible for such network adapters to switch between RSS, VMQ, and SR-IOV automatically.

When NDIS calls the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, the miniport driver follows these steps before it reports its currently enabled SR-IOV, VMQ, or RSS capabilities to NDIS:

1.  The miniport driver reads the **\*SriovPreferred** keyword before reporting its currently enabled capabilities to NDIS.

    If the value of the **\*SriovPreferred** keyword is one, the miniport driver is configured for SR-IOV preference.

2.  The miniport driver reads the **\*RssOrVmqPreference** keyword before reporting its currently enabled capabilities to NDIS.

    If the value of the **\*RssOrVmqPreference** keyword is one, the miniport driver is configured for VMQ preference.

    If the value of the **\*RssOrVmqPreference** keyword is zero or the keyword is not present, the miniport driver is configured for RSS preference.

3.  If the miniport driver is configured for SR-IOV preference, it must read the **\*SRIOV** keyword to determine whether SR-IOV is enabled on the network adapter. If the keyword is set to one, the driver reports the currently enabled SR-IOV settings.

    For more information on how the miniport driver reports SR-IOV settings, see [Determining SR-IOV Capabilities](determining-sr-iov-capabilities.md).

    For more information about the SR-IOV keywords, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

    **Note**  If the miniport driver is configured for SR-IOV preference, it must not read any of the RSS standardized keywords. However, the driver must read the VMQ **\*VMQVlanFiltering** standardized keyword. This keyword specifies whether the miniport driver is enabled to filter network packets by using the virtual VLAN (VLAN) identifier in the media access control (MAC) header. The miniport driver reports this capability by setting the NDIS\_RECEIVE\_FILTER\_MAC\_HEADER\_VLAN\_ID\_SUPPORTED flag in the **SupportedMacHeaderFields** member of the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure. For more information on the **\*VMQVlanFiltering** standardized keyword, see [Standardized INF Keywords for VMQ](standardized-inf-keywords-for-vmq.md).

     

4.  If the miniport driver is configured for VMQ preference, it must read the **\*VMQ** keyword to determine whether VMQ is enabled on the network adapter. If the keyword is set to one, the driver reports the currently enabled VMQ settings. For more information on how the miniport driver reports VMQ settings, see [Determining the VMQ Capabilities of a Network Adapter](determining-the-vmq-capabilities-of-a-network-adapter.md).

    For more information about VMQ keywords, see [Standardized INF Keywords for VMQ](standardized-inf-keywords-for-vmq.md).

    **Note**  If the miniport driver is configured for VMQ preference, it must not read any of the RSS or SR-IOV standardized keywords.

     

5.  If the miniport driver is configured for RSS preference, it must read the **\*RSS** keyword to determine whether RSS is enabled on the network adapter. If the keyword is set to one, the driver reports the currently enabled RSS settings. For more information on how the miniport driver reports RSS settings, see [RSS Configuration](rss-configuration.md).

    For more information about the RSS keywords, see [Standardized INF Keywords for RSS](standardized-inf-keywords-for-rss.md).

    **Note**  If the miniport driver is configured for RSS preference, it must not read any of the VMQ or SR-IOV standardized keywords.

     

The following table describes how the miniport driver determines SR-IOV, VMQ, or RSS preference in order to enable the correct interface in the network adapter.

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
<th align="left"><em>SriovPreferred</th>
<th align="left"></em>RssOrVmqPreference</th>
<th align="left"><em>SRIOV</th>
<th align="left"></em>VMQ</th>
<th align="left">*RSS</th>
<th align="left">Enabled interface</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>SR-IOV and VMQ</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>VMQ</p></td>
</tr>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>1, 0, or not present in registry</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>None</p></td>
</tr>
<tr class="even">
<td align="left"><p>0, or not present in registry</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>VMQ</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0, or not present in registry</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>None</p></td>
</tr>
<tr class="even">
<td align="left"><p>0, or not present in registry</p></td>
<td align="left"><p>0, or not present in registry</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>RSS</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0, or not present in registry</p></td>
<td align="left"><p>0, or not present in registry</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>None</p></td>
</tr>
</tbody>
</table>

 

**Note**  When the SR-IOV and VMQ interfaces are both enabled, SR-IOV nondefault virtual ports (VPorts) that are attached to the PCI Express (PCIe) Physical Function (PF) are used instead of VM queues for the VMQ interface. For more information, see [Nondefault Virtual Ports and VMQ](nondefault-virtual-ports-and-vmq.md).

 

The miniport driver must advertise the capabilities of the currently enabled interface. For example, if SR-IOV is enabled, the miniport driver must advertise the SR-IOV capabilities but not the capabilities for VMQ or RSS. However, the miniport driver must always report the complete RSS, VMQ, and SR-IOV hardware capabilities regardless of which interface is enabled on the network adapter.

**Note**  The VMQ and SR-IOV interfaces use receive filtering over VM queues or SR-IOV virtual ports (VPorts). As a result, some receive filtering capabilities require the same or different settings when either of these interfaces are enabled. For more information on how to report the receive filtering capabilities for the SR-IOV interface, see [Determining Receive Filtering Capabilities](determining-receive-filtering-capabilities.md). For more information on how to report the receive filtering capabilities for the VMQ interface, see [Determining the VMQ Capabilities of a Network Adapter](determining-the-vmq-capabilities-of-a-network-adapter.md).

 

 

 





