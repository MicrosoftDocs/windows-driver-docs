---
title: WDI_TLV_RECEIVE_COALESCING_CAPABILITIES
description: WDI_TLV_RECEIVE_COALESCING_CAPABILITIES is a TLV that contains hardware assisted receive filter capabilities.
ms.assetid: 87BC1F55-90C6-4B22-9E8E-A54FF42515F3
ms.date: 07/18/2017
keywords:
 - WDI_TLV_RECEIVE_COALESCING_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_RECEIVE\_COALESCING\_CAPABILITIES


WDI\_TLV\_RECEIVE\_COALESCING\_CAPABILITIES is a TLV that contains hardware assisted receive filter capabilities.

## TLV Type


0x9A

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>UINT32</td>
<td>Enabled filter types. A bitwise OR of flags that specify the types of receive filters that are enabled. The following flags are valid.
<p></p>
<dl>
<dt>NDIS_RECEIVE_FILTER_VMQ_FILTERS_ENABLED</dt>
<dd><p>Specifies that VMQ filters are enabled.</p>
</dd>
<dt>NDIS_RECEIVE_FILTER_PACKET_COALESCING_FILTERS_ENABLED</dt>
<dd><p>Specifies that NDIS packet coalescing receive filters are enabled.</p>
</dd>
</dl></td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Enabled queue types. A bitwise OR of flags that specify the types of receive queues that are enabled. The following flag is valid.
<p></p>
<dl>
<dt>NDIS_RECEIVE_FILTER_VM_QUEUES_ENABLED</dt>
<dd><p>Specifies that virtual machine (VM) queues are enabled. VM queues are used when the miniport driver is enabled to use the VMQ interface.</p>
</dd>
</dl></td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>The number of VM queues that the network adapter supports.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Supported VM queue properties. A bitwise OR of flags that specify the VM queue properties that the network adapter supports. The following flags are valid.
<p></p>
<dl>
<dt>NDIS_RECEIVE_FILTER_MSI_X_SUPPORTED</dt>
<dd><p>The network adapter assigned an MSI-X table entry for each receive queue. Network adapters must not use one MSI-X table entry for multiple receive queues. This flag is mandatory for miniport drivers that support the VMQ or SR-IOV interface.</p>
</dd>
<dt>NDIS_RECEIVE_FILTER_VM_QUEUE_SUPPORTED</dt>
<dd><p>The network adapter provides the minimum requirements to support VM queue packet filtering. The miniport driver must set this flag if it is enabled to use the VMQ or SR-IOV interface.</p>
<p>For more information about VMQ requirements for VM queue packet filtering, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff570780" data-raw-source="[Setting and Clearing VMQ Filters](https://msdn.microsoft.com/library/windows/hardware/ff570780)">Setting and Clearing VMQ Filters</a>.</p>
<p>For more information about SR-IOV requirements for VM queue packet filtering, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh440224" data-raw-source="[Setting a Receive Filter on a Virtual Port](https://msdn.microsoft.com/library/windows/hardware/hh440224)">Setting a Receive Filter on a Virtual Port</a>.</p>
</dd>
<dt>NDIS_RECEIVE_FILTER_LOOKAHEAD_SPLIT_SUPPORTED</dt>
<dd><p>The network adapter supports VM queues that split an incoming received packet at the lookahead offset. This offset is equal to or greater than the requested lookahead size. The network adapter uses DMA to transfer the lookahead and post-lookahead data to separate shared memory segments.</p>
<div class="alert">
<strong>Note</strong>  Starting with NDIS 6.30, splitting packet data into separate lookahead buffers is no longer supported. Miniport drivers that support this version of NDIS must not set this flag.
</div>
<div>
 
</div>
</dd>
<dt>NDIS_RECEIVE_FILTER_DYNAMIC_PROCESSOR_AFFINITY_CHANGE_SUPPORTED</dt>
<dd><p>The network adapter supports the ability to dynamically change one of the following processor affinity attributes:</p>
<ul>
<li><p>The processor affinity of a VM queue in the VMQ interface. The processor affinity is changed through an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569794" data-raw-source="[OID_RECEIVE_FILTER_QUEUE_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569794)">OID_RECEIVE_FILTER_QUEUE_PARAMETERS</a>.</p></li>
<li><p>The processor affinity of a nondefault virtual port (VPort), which was created in the SR-IOV interface and is attached to the PCI Express (PCIe) physical function (PF) of the network adapter. The processor affinity is changed through an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451825" data-raw-source="[OID_NIC_SWITCH_VPORT_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451825)">OID_NIC_SWITCH_VPORT_PARAMETERS</a>.</p></li>
</ul>
</dd>
<dt>NDIS_RECEIVE_FILTER_INTERRUPT_VECTOR_COALESCING_SUPPORTED</dt>
<dd><p>The network adapter supports interrupt coalescing for received packets on any of the following:</p>
<ul>
<li><p>Multiple VM queues in the VMQ interface.</p></li>
<li><p>Multiple VPorts that are attached to the PF in the SR-IOV interface.</p></li>
</ul>
<p>If this flag is set, the network adapter must coalesce receive interrupts for VM queues or VPorts that have the same processor affinity.</p>
</dd>
<dt>NDIS_RECEIVE_FILTER_IMPLAT_MIN_OF_QUEUES_MODE</dt>
<dd><p>Indicates that the number of VM queues available is the minimum number of queues available from any member of a Load Balancing Failover (LBFO) team. This flag applies to LBFO filters only. This flag is not set for miniports.</p>
</dd>
<dt> NDIS_RECEIVE_FILTER_IMPLAT_SUM_OF_QUEUES_MODE</dt>
<dd><p>Indicates that the number of VM queues available is the sum of all the queues available from every member of an LBFO team. This flag applies to LBFO filters only. This flag is not set for miniports.</p>
</dd>
<dt>NDIS_RECEIVE_FILTER_PACKET_COALESCING_SUPPORTED_ON_DEFAULT_QUEUE</dt>
<dd><p>The network adapter supports NDIS packet coalescing. Packet coalescing is only supported on the default receive queue of the network adapter. This receive queue has an identifier of NDIS_DEFAULT_RECEIVE_QUEUE_ID.</p>
</dd>
</dl></td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Supported filter tests. A bitwise OR of flags that specify the test operations that a miniport driver supports. The following flags are valid.
<p></p>
<dl>
<dt>NDIS_RECEIVE_FILTER_TEST_HEADER_FIELD_EQUAL_SUPPORTED</dt>
<dd><p>The network adapter supports testing the selected header field to determine whether it is equal to a given value.</p>
<div class="alert">
<strong>Note</strong>  If the miniport driver supports the VMQ or SR-IOV interfaces, it must set this flag.
</div>
<div>
 
</div>
</dd>
<dt>NDIS_RECEIVE_FILTER_TEST_HEADER_FIELD_MASK_EQUAL_SUPPORTED</dt>
<dd><p>The network adapter supports masking (that is, a bitwise AND) of the selected header field to determine whether the result is equal to a specified value.</p>
</dd>
<dt>NDIS_RECEIVE_FILTER_TEST_HEADER_FIELD_NOT_EQUAL_SUPPORTED</dt>
<dd><p>The network adapter supports testing the selected header field to determine whether it is not equal to a specified value.</p>
</dd>
</dl></td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Supported headers. A bitwise OR of flags that specify the types of network packet headers that a miniport driver can inspect. The following flags are valid.
<p></p>
<dl>
<dt>NDIS_RECEIVE_FILTER_MAC_HEADER_SUPPORTED</dt>
<dd><p>The network adapter can inspect the media access control (MAC) header of a network packet. The <strong>SupportedMacHeaderFields</strong> member defines the various fields from the MAC header that can be inspected.</p>
</dd>
<dt>NDIS_RECEIVE_FILTER_ARP_HEADER_SUPPORTED</dt>
<dd><p>The network adapter can inspect the Address Resolution Protocol (ARP) header of a network packet. The <strong>SupportedArpHeaderFields</strong> member defines the various fields from the ARP header that can be inspected.</p>
</dd>
<dt>NDIS_RECEIVE_FILTER_IPV4_HEADER_SUPPORTED</dt>
<dd><p>The network adapter can inspect the IP version 4 (IPv4) header of a network packet. The <strong>SupportedIPv4HeaderFields</strong> member defines the various fields from the IPv4 header that can be inspected.</p>
</dd>
<dt>NDIS_RECEIVE_FILTER_IPV6_HEADER_SUPPORTED</dt>
<dd><p>The network adapter can inspect the IP version 6 (IPv6) header of a network packet. The <strong>SupportedIPv6HeaderFields</strong> member defines the various fields from the IPv6 header that can be inspected.</p>
</dd>
<dt>NDIS_RECEIVE_FILTER_UDP_HEADER_SUPPORTED</dt>
<dd><p>The network adapter can inspect the User Datagram Protocol (UDP) header of a network packet. The <strong>SupportedIPv6HeaderFields</strong> member defines the various fields from the UDP header that can be inspected.</p>
</dd>
</dl></td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Supported MAC header fields. A bitwise OR of flags that specify the types of MAC header fields that a miniport driver can inspect. The following flags are valid.
<p></p>
<dl>
<dt>NDIS_RECEIVE_FILTER_MAC_HEADER_DEST_ADDR_SUPPORTED</dt>
<dd><p>The network adapter supports inspecting and filtering that are based on the destination MAC address in the MAC header.</p>
<div class="alert">
<strong>Note</strong>  Starting with NDIS 6.30, miniport drivers that support the VMQ or SR-IOV interface must set this flag.
</div>
<div>
 
</div>
</dd>
<dt>NDIS_RECEIVE_FILTER_MAC_HEADER_SOURCE_ADDR_SUPPORTED</dt>
<dd><p>The network adapter supports inspecting and filtering that are based on the source MAC address in the MAC header.</p>
</dd>
<dt>NDIS_RECEIVE_FILTER_MAC_HEADER_PROTOCOL_SUPPORTED</dt>
<dd><p>The network adapter supports inspecting and filtering that are based on the EtherType identifier in the MAC header. For example, the EtherType identifier for IPv4 packets is 0x0800.</p>
</dd>
<dt>NDIS_RECEIVE_FILTER_MAC_HEADER_VLAN_ID_SUPPORTED</dt>
<dd><p>The network adapter supports inspecting and filtering that are based on the VLAN identifier in the MAC header.</p>
</dd>
<dt>NDIS_RECEIVE_FILTER_MAC_HEADER_PRIORITY_SUPPORTED</dt>
<dd><p>The network adapter supports inspecting and filtering that are based on the priority tag in the MAC header.</p>
</dd>
<dt>NDIS_RECEIVE_FILTER_MAC_HEADER_PACKET_TYPE_SUPPORTED</dt>
<dd><p>The network adapter supports inspecting and filtering that are based on the packet type field of the IEEE 802.2 subnetwork access protocol (SNAP) header in an 802.3 MAC header.</p>
</dd>
</dl></td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The maximum number of MAC header filters that the miniport driver supports.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Maximum queue groups. This value is reserved.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Maximum queues per queue group. This value is reserved.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>The minimum size, in bytes, that the network adapter supports for lookahead packet buffers.
<div class="alert">
<strong>Note</strong>  Starting with NDIS 6.30, splitting packet data into separate lookahead buffers is no longer supported. Miniport drivers that support this version of NDIS must set this member to zero.
</div>
<div>
 
</div></td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The maximum size, in bytes, that the network adapter supports for lookahead packet buffers.
<div class="alert">
<strong>Note</strong>  Starting with NDIS 6.30, splitting packet data into separate lookahead buffers is no longer supported. Miniport drivers that support this version of NDIS must set this member to zero.
</div>
<div>
 
</div></td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Supported ARP header fields. A bitwise OR of flags that specify the types of ARP header fields that a miniport driver can inspect. The following flags are valid.
<p></p>
<dl>
<dt>NDIS_RECEIVE_FILTER_ARP_HEADER_OPERATION_SUPPORTED</dt>
<dd><p>The network adapter supports receive filtering on the ARP operation field.</p>
</dd>
<dt> NDIS_RECEIVE_FILTER_ARP_HEADER_SPA_SUPPORTED</dt>
<dd><p>The network adapter supports receive filtering on the ARP source protocol address (SPA) field.</p>
</dd>
<dt> NDIS_RECEIVE_FILTER_ARP_HEADER_TPA_SUPPORTED</dt>
<dd><p>The network adapter supports receive filtering on the ARP target protocol address (TPA) field.</p>
</dd>
</dl></td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Supported IPv4 header fields. A bitwise OR of flags that specify the types of IPv4 header fields that a miniport driver can inspect. The following flag is valid.
<p></p>
<dl>
<dt> NDIS_RECEIVE_FILTER_IPV4_HEADER_PROTOCOL_SUPPORTED</dt>
<dd><p>The network adapter supports receive filtering on the IPv4 protocol field.</p>
</dd>
</dl></td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Supported IPv6 header fields. A bitwise OR of flags that specify the types of IPv6 header fields that a miniport driver can inspect. The following flag is valid.
<p></p>
<dl>
<dt> NDIS_RECEIVE_FILTER_IPV6_HEADER_PROTOCOL_SUPPORTED</dt>
<dd><p>The network adapter supports receive filtering on the IPv6 protocol field.</p>
</dd>
</dl></td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Supported UDP header fields. A bitwise OR of flags that specify the types of IPv6 header fields that a miniport driver can inspect. The following flag is valid.
<p></p>
<dl>
<dt> NDIS_RECEIVE_FILTER_UDP_HEADER_DEST_PORT_SUPPORTED</dt>
<dd><p>The network adapter supports receive filtering on the UDP destination port field.</p>
<div class="alert">
<strong>Note</strong>  If the received UDP packet contains IPv4 options or IPv6 extension headers, the network adapter can automatically drop the received packet and treat it as if it failed the UDP filter test.
</div>
<div>
 
</div>
</dd>
</dl></td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>The maximum number of tests on packet header fields that can be specified for a single packet coalescing filter. For more information about packet coalescing, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh451601" data-raw-source="[NDIS Packet Coalescing](https://msdn.microsoft.com/library/windows/hardware/hh451601)">NDIS Packet Coalescing</a>.
<div class="alert">
<strong>Note</strong>  Network adapters that support packet coalescing must support five or more packet header fields that can be specified for a single packet coalescing filter. If the adapter does not support packet coalescing, the miniport driver must set this value to zero.
</div>
<div>
 
</div></td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The maximum number of packet coalescing receive filters that are supported by the network adapter.
<div class="alert">
<strong>Note</strong>  Network adapters that support packet coalescing must support ten or more packet coalescing filters. If the adapter does not support packet coalescing, the miniport driver must set this value to zero.
</div>
<div>
 
</div></td>
</tr>
</tbody>
</table>

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864)

 

 




