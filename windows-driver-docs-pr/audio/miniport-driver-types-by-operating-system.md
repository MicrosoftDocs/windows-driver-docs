---
Description: Miniport Driver Types by Operating System
MS-HAID: 'audio.miniport\_driver\_types\_by\_operating\_system'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Miniport Driver Types by Operating System
---

# Miniport Driver Types by Operating System


When you develop your own audio driver, you must determine whether your driver will work in conjunction with the PortCls system driver (Portcls.sys) or with the AVStream class system driver. If a video stream is not necessary, you will probably want a driver that works with the PortCls system driver. For more information about these two types of system drivers, see the [Introduction to Port Class](introduction-to-port-class.md) and [AVStream Overview](stream.avstream_overview) topics.

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
<td align="left"><p>[WaveCyclic](wavecyclic-miniport-driver.md)</p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
</tr>
<tr class="even">
<td align="left"><p>[WavePci](wavepci-miniport-driver.md)</p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[WaveRT](wavert-miniport-driver.md)</p></td>
<td align="left"></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Topology](topology-miniport-driver.md)</p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[MIDI](midi-miniport-driver.md)</p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
<td align="left"><p>x</p></td>
</tr>
<tr class="even">
<td align="left"><p>[DMus](dmus-miniport-driver.md)</p></td>
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Miniport%20Driver%20Types%20by%20Operating%20System%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


