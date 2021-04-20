---
title: Miniport Interfaces
description: Miniport Interfaces
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
<td align="left"><p><a href="/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwavecyclic" data-raw-source="[IPortWaveCyclic](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwavecyclic)">IPortWaveCyclic</a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavecyclic" data-raw-source="[IMiniportWaveCyclic](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavecyclic)">IMiniportWaveCyclic</a></p></td>
</tr>
<tr class="even">
<td align="left"><p>WavePci</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwavepci" data-raw-source="[IPortWavePci](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwavepci)">IPortWavePci</a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavepci" data-raw-source="[IMiniportWavePci](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavepci)">IMiniportWavePci</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>WaveRT</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwavert" data-raw-source="[IPortWaveRT](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwavert)">IPortWaveRT</a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavert" data-raw-source="[IMiniportWaveRT](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavert)">IMiniportWaveRT</a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Topology</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/portcls/nn-portcls-iporttopology" data-raw-source="[IPortTopology](/windows-hardware/drivers/ddi/portcls/nn-portcls-iporttopology)">IPortTopology</a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiporttopology" data-raw-source="[IMiniportTopology](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiporttopology)">IMiniportTopology</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>MIDI</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/portcls/nn-portcls-iportmidi" data-raw-source="[IPortMidi](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportmidi)">IPortMidi</a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportmidi" data-raw-source="[IMiniportMidi](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportmidi)">IMiniportMidi</a></p></td>
</tr>
<tr class="even">
<td align="left"><p>DirectMusic</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iportdmus" data-raw-source="[IPortDMus](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iportdmus)">IPortDMus</a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iminiportdmus" data-raw-source="[IMiniportDMus](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iminiportdmus)">IMiniportDMus</a></p></td>
</tr>
</tbody>
</table>

 

In the preceding table, all **IPortXxx** interfaces are derived from base interface [IPort](/windows-hardware/drivers/ddi/portcls/nn-portcls-iport), and all **IMiniportXxx** interfaces are derived from [IMiniport](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiport).

