---
title: WDI_TLV_DATAPATH_CAPABILITIES
description: WDI_TLV_DATAPATH_CAPABILITIES is a TLV that contains datapath capabilities.
ms.assetid: 7B545858-56A2-4655-91D5-37CA4EB61E1E
ms.date: 07/18/2017
keywords:
 - WDI_TLV_DATAPATH_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_DATAPATH\_CAPABILITIES


WDI\_TLV\_DATAPATH\_CAPABILITIES is a TLV that contains datapath capabilities.

## TLV Type


0xB9

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
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn926068" data-raw-source="[&lt;strong&gt;WDI_INTERCONNECT_TYPE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn926068)"><strong>WDI_INTERCONNECT_TYPE</strong></a> (UINT32)</td>
<td>Interconnect type.</td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Maximum number of peers.</td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Specifies transmit capability: Target priority queuing.
<p>Valid values are 0 and 1. If set to 0, WDI classifies Tx frames by Peer and TID and utilizes the full scheduler to select TX queues to transfer. It is recommended that this is set to false unless the target is capable of classification and Peer-TID queueing. If set to 1, WDI classifies Tx frames by Peer and TID and only provides queuing at a port level. WDI schedules backlogged port queues using a global DRR.</p></td>
</tr>
<tr class="even">
<td>UINT16</td>
<td>Specifies transmit capability: Maximum number of Scatter Gather elements in frame.
<p>WDI coalesces frames as necessary such that the IHV miniport does not receive a frame that requires more scatter gather elements than specified by this capability. For best performance, it is suggested that this capability is set higher than the typical frame as the coalescing requires a memory copy. If this capability is not greater than max frame size divided by page size, WDI may be unable to successfully coalesce the frame and it may be dropped.</p></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Specifies transmit capability: Explicit Send Complete flag required.
<p>Valid values are 0 and 1. If set to 0, the target/TAL generates a TX send complete for all frames. If set to 1, the target/TAL generates TX send completion indication only for frames that have this flag set in the frame’s metadata.</p></td>
</tr>
<tr class="even">
<td>UINT16</td>
<td>Specifies transmit capability: Minimum effective frame size.
<p>When dequeuing frames, the TxMgr treats frames smaller than this value as having an effective size of this value.</p></td>
</tr>
<tr class="odd">
<td>UINT16</td>
<td>Specifies transmit capability: Frame size granularity.
<p>This value is equal to the granularity of memory allocation per frame. For the purposes of dequeuing, the TxMgr treats a frame as having an effective size equal to the frame size plus the least amount of padding such that the effective size is an integer multiple of this value. This value must be set to a power of two.</p></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies transmit capability: Rx Tx forwarding.
<p>Valid values are 0 and 1. If set to 1, the target is capable of forwarding received frames.</p></td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Specifies transmit capability: Maximum throughput, in units of 0.5 Mbps.
<p>This value is used for the allocation of descriptors and buffers.</p></td>
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

 

 




