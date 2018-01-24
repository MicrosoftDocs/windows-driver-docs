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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Rules%20for%20Audio%20Drivers%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




