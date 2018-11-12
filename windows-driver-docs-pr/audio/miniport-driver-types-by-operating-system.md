---
title: Miniport Driver Types by Operating System
description: Miniport Driver Types by Operating System
ms.assetid: 6ab0e4e4-5118-4df5-ba4e-7da66ce5880d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miniport Driver Types by Operating System


When you develop your own audio driver, you must determine whether your driver will work in conjunction with the PortCls system driver (Portcls.sys) or with the AVStream class system driver. If a video stream is not necessary, you will probably want a driver that works with the PortCls system driver. For more information about these two types of system drivers, see the [Introduction to Port Class](introduction-to-port-class.md) and [AVStream Overview](https://msdn.microsoft.com/library/windows/hardware/ff554240) topics.

The PortCls system driver (Portcls.sys) provides several built-in port drivers to support audio devices that render and capture wave and MIDI streams. Typically, a port driver provides the majority of the functionality for each class of audio subdevice.

Each port driver works in conjunction with a miniport driver. The miniport driver manages the hardware-dependent functions of a wave-rendering or wave-capture device. In other words, the miniport driver provides support for functionality that is specific to the hardware of the third party audio device.

The type of miniport driver that you develop is determined by your target Windows operating system and the features that are provided by your audio device. The following table shows the different types of miniport drivers and the Windows operating systems that support them.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Miniport driver</th>
<th align="left">Windows XP</th>
<th align="left">Windows Vista</th>
<th align="left">Windows 7</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="wavecyclic-miniport-driver.md" data-raw-source="[WaveCyclic](wavecyclic-miniport-driver.md)">WaveCyclic</a></p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wavepci-miniport-driver.md" data-raw-source="[WavePci](wavepci-miniport-driver.md)">WavePci</a></p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wavert-miniport-driver.md" data-raw-source="[WaveRT](wavert-miniport-driver.md)">WaveRT</a></p></td>
<td align="left"></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="topology-miniport-driver.md" data-raw-source="[Topology](topology-miniport-driver.md)">Topology</a></p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="midi-miniport-driver.md" data-raw-source="[MIDI](midi-miniport-driver.md)">MIDI</a></p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="dmus-miniport-driver.md" data-raw-source="[DMus](dmus-miniport-driver.md)">DMus</a></p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
</tr>
</tbody>
</table>

 

Each port driver implements an interface, which it presents to the miniport driver. To communicate with the port driver, the miniport driver must also implement an interface. For more information about the interfaces that are implemented by the miniport drivers, see [Miniport Interfaces](miniport-interfaces.md).

**Note**   In Windows Vista, audio stream processing for system effects is not provided by the audio driver. Audio stream processing is provided by user mode components called [system effects audio processing objects](system-effects-audio-processing-objects.md) (sAPOS).

 

**Note**   When you develop audio drivers for Windows Vista and later operating systems, be aware of the following:
-   You cannot obtain a logo qualification for a WaveCyclic- or a WavePci -based audio driver.

-   There is no support for kernel-mode software synthesizers for DMus. However, support is provided for hardware MIDI I/O.

 

 

 




