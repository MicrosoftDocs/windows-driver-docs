---
title: Miniport Interfaces
description: Miniport Interfaces
ms.assetid: 50b92adc-a63c-4242-9ec9-4d97151f0f91
keywords:
- audio miniport drivers WDK , interfaces
- miniport drivers WDK audio , interfaces
- miniport interfaces WDK audio
- port class drivers WDK audio
- PortCls WDK audio , interfaces
- interfaces WDK audio
- built-in port drivers WDK audio
- stream interfaces WDK audio
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Miniport Interfaces


## <span id="miniport_interfaces"></span><span id="MINIPORT_INTERFACES"></span>


As described in [Supporting a Device](supporting-a-device.md), the PortCls system driver provides a set of five built-in port drivers for managing wave and MIDI devices. To use one of these port drivers to manage a particular type of audio device, the adapter driver must provide a corresponding miniport driver that complements the port driver by managing all the device's hardware-dependent functions.

This section discusses the following five miniport driver types:

[WaveRT Miniport Driver](wavert-miniport-driver.md)

Complements the WaveRT port driver by managing the hardware-dependent functions of a wave rendering or capture device that uses a cyclic buffer for audio data.
[Topology Miniport Driver](topology-miniport-driver.md)

Complements the Topology port driver by managing the various hardware controls (for example, volume level) in the audio adapter's mixer circuitry.
[MIDI Miniport Driver](midi-miniport-driver.md)

Complements the MIDI port driver by managing the hardware-dependent functions of a simple MIDI device.
[DMus Miniport Driver](dmus-miniport-driver.md)

Complements the DMus port driver by managing the hardware-dependent functions of an advanced MIDI device.
Each port driver implements an **IPortXxx** interface, which it presents to the miniport driver. In turn, the miniport driver must implement an **IMiniportXxx** interface, which the port driver uses to communicate with the miniport driver. The following table shows the **IPortXxx** interface and the corresponding **IMiniportXxx** interface for each device type.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Device Type</th>
<th align="left">Port Driver Interface</th>
<th align="left">Miniport Driver Interface</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>WaveCyclic</p></td>
<td align="left"><p>[IPortWaveCyclic](https://msdn.microsoft.com/library/windows/hardware/ff536899)</p></td>
<td align="left"><p>[IMiniportWaveCyclic](https://msdn.microsoft.com/library/windows/hardware/ff536714)</p></td>
</tr>
<tr class="even">
<td align="left"><p>WavePci</p></td>
<td align="left"><p>[IPortWavePci](https://msdn.microsoft.com/library/windows/hardware/ff536905)</p></td>
<td align="left"><p>[IMiniportWavePci](https://msdn.microsoft.com/library/windows/hardware/ff536724)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>WaveRT</p></td>
<td align="left"><p>[IPortWaveRT](https://msdn.microsoft.com/library/windows/hardware/ff536920)</p></td>
<td align="left"><p>[IMiniportWaveRT](https://msdn.microsoft.com/library/windows/hardware/ff536737)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Topology</p></td>
<td align="left"><p>[IPortTopology](https://msdn.microsoft.com/library/windows/hardware/ff536896)</p></td>
<td align="left"><p>[IMiniportTopology](https://msdn.microsoft.com/library/windows/hardware/ff536712)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MIDI</p></td>
<td align="left"><p>[IPortMidi](https://msdn.microsoft.com/library/windows/hardware/ff536891)</p></td>
<td align="left"><p>[IMiniportMidi](https://msdn.microsoft.com/library/windows/hardware/ff536703)</p></td>
</tr>
<tr class="even">
<td align="left"><p>DirectMusic</p></td>
<td align="left"><p>[IPortDMus](https://msdn.microsoft.com/library/windows/hardware/ff536879)</p></td>
<td align="left"><p>[IMiniportDMus](https://msdn.microsoft.com/library/windows/hardware/ff536699)</p></td>
</tr>
</tbody>
</table>

 

In the preceding table, all **IPortXxx** interfaces are derived from base interface [IPort](https://msdn.microsoft.com/library/windows/hardware/ff536842), and all **IMiniportXxx** interfaces are derived from [IMiniport](https://msdn.microsoft.com/library/windows/hardware/ff536698).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Miniport%20Interfaces%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


