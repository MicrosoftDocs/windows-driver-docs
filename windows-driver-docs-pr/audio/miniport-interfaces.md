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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miniport Interfaces


## <span id="miniport_interfaces"></span><span id="MINIPORT_INTERFACES"></span>


As described in [Supporting a Device](supporting-a-device.md), the PortCls system driver provides a set of built-in port drivers for managing wave and MIDI devices. To use one of these port drivers to manage a particular type of audio device, the adapter driver must provide a corresponding miniport driver that complements the port driver by managing all the device's hardware-dependent functions.

This section discusses the following miniport driver types:

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536899" data-raw-source="[IPortWaveCyclic](https://msdn.microsoft.com/library/windows/hardware/ff536899)">IPortWaveCyclic</a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536714" data-raw-source="[IMiniportWaveCyclic](https://msdn.microsoft.com/library/windows/hardware/ff536714)">IMiniportWaveCyclic</a></p></td>
</tr>
<tr class="even">
<td align="left"><p>WavePci</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536905" data-raw-source="[IPortWavePci](https://msdn.microsoft.com/library/windows/hardware/ff536905)">IPortWavePci</a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536724" data-raw-source="[IMiniportWavePci](https://msdn.microsoft.com/library/windows/hardware/ff536724)">IMiniportWavePci</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>WaveRT</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536920" data-raw-source="[IPortWaveRT](https://msdn.microsoft.com/library/windows/hardware/ff536920)">IPortWaveRT</a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536737" data-raw-source="[IMiniportWaveRT](https://msdn.microsoft.com/library/windows/hardware/ff536737)">IMiniportWaveRT</a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Topology</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536896" data-raw-source="[IPortTopology](https://msdn.microsoft.com/library/windows/hardware/ff536896)">IPortTopology</a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536712" data-raw-source="[IMiniportTopology](https://msdn.microsoft.com/library/windows/hardware/ff536712)">IMiniportTopology</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>MIDI</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536891" data-raw-source="[IPortMidi](https://msdn.microsoft.com/library/windows/hardware/ff536891)">IPortMidi</a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536703" data-raw-source="[IMiniportMidi](https://msdn.microsoft.com/library/windows/hardware/ff536703)">IMiniportMidi</a></p></td>
</tr>
<tr class="even">
<td align="left"><p>DirectMusic</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536879" data-raw-source="[IPortDMus](https://msdn.microsoft.com/library/windows/hardware/ff536879)">IPortDMus</a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536699" data-raw-source="[IMiniportDMus](https://msdn.microsoft.com/library/windows/hardware/ff536699)">IMiniportDMus</a></p></td>
</tr>
</tbody>
</table>

 

In the preceding table, all **IPortXxx** interfaces are derived from base interface [IPort](https://msdn.microsoft.com/library/windows/hardware/ff536842), and all **IMiniportXxx** interfaces are derived from [IMiniport](https://msdn.microsoft.com/library/windows/hardware/ff536698).

 

 




