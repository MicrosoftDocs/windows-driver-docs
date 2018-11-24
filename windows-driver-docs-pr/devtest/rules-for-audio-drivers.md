---
title: Rules for Audio Drivers
description: The DDI compliance rules for audio (PortCls) miniport drivers verify the DDI interface between PortCls.sys and its miniport drivers.
ms.assetid: 65078F78-B7F2-41A7-BD3B-A90A4A77750F
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# Rules for Audio Drivers


The DDI compliance rules for audio (PortCls) miniport drivers verify the DDI interface between PortCls.sys and its miniport drivers.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="audio-pcaddadapterdevice.md" data-raw-source="[&lt;strong&gt;PcAddAdapterDevice&lt;/strong&gt;](audio-pcaddadapterdevice.md)"><strong>PcAddAdapterDevice</strong></a></p></td>
<td align="left"><p>The PcAddAdapterDevice rule specifies that a PortCls miniport driver correctly uses the <a href="audio-pcaddadapterdevice.md" data-raw-source="[&lt;strong&gt;PcAddAdapterDevice&lt;/strong&gt;](audio-pcaddadapterdevice.md)"><strong>PcAddAdapterDevice</strong></a> function, specifically that the <em>DeviceExtensionSize</em> should be either zero (0) or no less than PORT_CLASS_DEVICE_EXTENSION_SIZE.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="audio-pcallocateandmappages.md" data-raw-source="[&lt;strong&gt;PcAllocateAndMapPages&lt;/strong&gt;](audio-pcallocateandmappages.md)"><strong>PcAllocateAndMapPages</strong></a></p></td>
<td align="left"><p>The PcAllocateAndMapPages rule specifies that a PortCls miniport driver calls the following interfaces, using the correct parameters:</p>
<ul>
<li>IPortWaveRTStream::AllocatePagesForMdl</li>
<li>IPortWaveRTStream::AllocateContiguousPagesForMdl</li>
<li>IPortWaveRTStream::MapAllocatedPages</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="audio-pcallocatedpages.md" data-raw-source="[&lt;strong&gt;PcAllocatedPages&lt;/strong&gt;](audio-pcallocatedpages.md)"><strong>PcAllocatedPages</strong></a></p></td>
<td align="left"><p>The PcAllocatedPages rule specifies that a PortCls miniport driver frees previous allocated pages by calling AllocatePagesForMdl or AllocateContiguousPagesForMdl methods.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="audio-pcirqlddis.md" data-raw-source="[&lt;strong&gt;PcIrqlDDIs&lt;/strong&gt;](audio-pcirqlddis.md)"><strong>PcIrqlDDIs</strong></a></p></td>
<td align="left"><p>The PcIrqlDDIs rule specifies that a PortCls miniport driver must call PortCls DDIs at the correct IRQL level.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="audio-pcirqliport.md" data-raw-source="[&lt;strong&gt;PcIrqlIport&lt;/strong&gt;](audio-pcirqliport.md)"><strong>PcIrqlIport</strong></a></p></td>
<td align="left"><p>The PcIrqlIport rule specifies that a PortCls miniport driver must call PortCls IPort interfaces at the correct IRQL level.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="pcporequestpowerirp.md" data-raw-source="[&lt;strong&gt;PcPoRequestPowerIrp&lt;/strong&gt;](pcporequestpowerirp.md)"><strong>PcPoRequestPowerIrp</strong></a></p></td>
<td align="left"><p>This rule verifies that a PortCls miniport driver should not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559734" data-raw-source="[&lt;strong&gt;PoRequestPowerIrp&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559734)"><strong>PoRequestPowerIrp</strong></a> with <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744" data-raw-source="[&lt;strong&gt;IRP_MN_SET_POWER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551744)"><strong>IRP_MN_SET_POWER</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="audio-pcpropertyrequest.md" data-raw-source="[&lt;strong&gt;PcPropertyRequest&lt;/strong&gt;](audio-pcpropertyrequest.md)"><strong>PcPropertyRequest</strong></a></p></td>
<td align="left"><p>The PcPropertyRequest rule specifies that a PortCls miniport driver should never call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537687" data-raw-source="[&lt;strong&gt;PcCompletePendingPropertyRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537687)"><strong>PcCompletePendingPropertyRequest</strong></a> with an <em>NtStatus</em> value of STATUS_PENDING.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="audio-pcregisteradapterpower.md" data-raw-source="[&lt;strong&gt;PcRegisterAdapterPower&lt;/strong&gt;](audio-pcregisteradapterpower.md)"><strong>PcRegisterAdapterPower</strong></a></p></td>
<td align="left"><p>The PcRegisterAdapterPower rule specifies that a PortCls miniport driver should not:</p>
<ul>
<li>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff537724" data-raw-source="[&lt;strong&gt;PcRegisterAdapterPowerManagement&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537724)"><strong>PcRegisterAdapterPowerManagement</strong></a> twice without an intervening call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff537735" data-raw-source="[&lt;strong&gt;PcUnregisterAdapterPowerManagement&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537735)"><strong>PcUnregisterAdapterPowerManagement</strong></a>.</li>
<li>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff537735" data-raw-source="[&lt;strong&gt;PcUnregisterAdapterPowerManagement&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537735)"><strong>PcUnregisterAdapterPowerManagement</strong></a> without calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff537724" data-raw-source="[&lt;strong&gt;PcRegisterAdapterPowerManagement&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537724)"><strong>PcRegisterAdapterPowerManagement</strong></a> first.</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="audio-pctimedwavertstreamsetstate.md" data-raw-source="[&lt;strong&gt;PcTimedWaveRtStreamSetState&lt;/strong&gt;](audio-pctimedwavertstreamsetstate.md)"><strong>PcTimedWaveRtStreamSetState</strong></a></p></td>
<td align="left"><p>The PcTimedWaveRtStreamSetState rule specifies that a ProtCls miniport driver makes state transitions through <a href="https://msdn.microsoft.com/library/windows/hardware/ff536756" data-raw-source="[&lt;strong&gt;IMiniportWaveRTStream::SetState&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536756)"><strong>IMiniportWaveRTStream::SetState</strong></a> within the required time.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="audio-pcunmapallocatedpages.md" data-raw-source="[&lt;strong&gt;PcUnmapAllocatedPages&lt;/strong&gt;](audio-pcunmapallocatedpages.md)"><strong>PcUnmapAllocatedPages</strong></a></p></td>
<td align="left"><p>The PcUnmapAllocatedPages rule specifies that:</p>
<ul>
<li>A PortCls miniport driver doesn&#39;t map an MDL that is currently mapped without first unmapping it.</li>
<li>A PortCls miniport driver unmaps the memory prior to freeing it using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536738" data-raw-source="[IMiniportWaveRTStream](https://msdn.microsoft.com/library/windows/hardware/ff536738)">IMiniportWaveRTStream</a> interface.</li>
</ul></td>
</tr>
</tbody>
</table>

 

 

 





