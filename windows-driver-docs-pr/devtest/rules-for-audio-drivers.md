---
title: Rules for Audio Drivers
description: The DDI compliance rules for audio (PortCls) miniport drivers verify the DDI interface between PortCls.sys and its miniport drivers.
ms.assetid: 65078F78-B7F2-41A7-BD3B-A90A4A77750F
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
<td align="left"><p>[<strong>PcAddAdapterDevice</strong>](audio-pcaddadapterdevice.md)</p></td>
<td align="left"><p>The PcAddAdapterDevice rule specifies that a PortCls miniport driver correctly uses the [<strong>PcAddAdapterDevice</strong>](audio-pcaddadapterdevice.md) function, specifically that the <em>DeviceExtensionSize</em> should be either zero (0) or no less than PORT_CLASS_DEVICE_EXTENSION_SIZE.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PcAllocateAndMapPages</strong>](audio-pcallocateandmappages.md)</p></td>
<td align="left"><p>The PcAllocateAndMapPages rule specifies that a PortCls miniport driver calls the following interfaces, using the correct parameters:</p>
<ul>
<li>IPortWaveRTStream::AllocatePagesForMdl</li>
<li>IPortWaveRTStream::AllocateContiguousPagesForMdl</li>
<li>IPortWaveRTStream::MapAllocatedPages</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PcAllocatedPages</strong>](audio-pcallocatedpages.md)</p></td>
<td align="left"><p>The PcAllocatedPages rule specifies that a PortCls miniport driver frees previous allocated pages by calling AllocatePagesForMdl or AllocateContiguousPagesForMdl methods.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PcIrqlDDIs</strong>](audio-pcirqlddis.md)</p></td>
<td align="left"><p>The PcIrqlDDIs rule specifies that a PortCls miniport driver must call PortCls DDIs at the correct IRQL level.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PcIrqlIport</strong>](audio-pcirqliport.md)</p></td>
<td align="left"><p>The PcIrqlIport rule specifies that a PortCls miniport driver must call PortCls IPort interfaces at the correct IRQL level.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PcPoRequestPowerIrp</strong>](pcporequestpowerirp.md)</p></td>
<td align="left"><p>This rule verifies that a PortCls miniport driver should not call [<strong>PoRequestPowerIrp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559734) with [<strong>IRP_MN_SET_POWER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551744).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PcPropertyRequest</strong>](audio-pcpropertyrequest.md)</p></td>
<td align="left"><p>The PcPropertyRequest rule specifies that a PortCls miniport driver should never call the [<strong>PcCompletePendingPropertyRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537687) with an <em>NtStatus</em> value of STATUS_PENDING.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PcRegisterAdapterPower</strong>](audio-pcregisteradapterpower.md)</p></td>
<td align="left"><p>The PcRegisterAdapterPower rule specifies that a PortCls miniport driver should not:</p>
<ul>
<li>Call [<strong>PcRegisterAdapterPowerManagement</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537724) twice without an intervening call to [<strong>PcUnregisterAdapterPowerManagement</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537735).</li>
<li>Call [<strong>PcUnregisterAdapterPowerManagement</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537735) without calling [<strong>PcRegisterAdapterPowerManagement</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537724) first.</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PcTimedWaveRtStreamSetState</strong>](audio-pctimedwavertstreamsetstate.md)</p></td>
<td align="left"><p>The PcTimedWaveRtStreamSetState rule specifies that a ProtCls miniport driver makes state transitions through [<strong>IMiniportWaveRTStream::SetState</strong>](https://msdn.microsoft.com/library/windows/hardware/ff536756) within the required time.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PcUnmapAllocatedPages</strong>](audio-pcunmapallocatedpages.md)</p></td>
<td align="left"><p>The PcUnmapAllocatedPages rule specifies that:</p>
<ul>
<li>A PortCls miniport driver doesn't map an MDL that is currently mapped without first unmapping it.</li>
<li>A PortCls miniport driver unmaps the memory prior to freeing it using the [IMiniportWaveRTStream](https://msdn.microsoft.com/library/windows/hardware/ff536738) interface.</li>
</ul></td>
</tr>
</tbody>
</table>

 

 

 





