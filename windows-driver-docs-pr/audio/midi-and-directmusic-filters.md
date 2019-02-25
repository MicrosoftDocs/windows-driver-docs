---
title: MIDI and DirectMusic Filters
description: MIDI and DirectMusic Filters
ms.assetid: 622aa4ae-c855-4088-bc1a-30dff7a24d23
keywords:
- audio filters WDK audio , MIDI
- audio filters WDK audio , DirectMusic
- DirectMusic WDK audio , filters
- MIDI filters WDK audio
- enumerating audio devices WDK
- system-supplied miniport drivers WDK audio
- system-supplied port drivers WDK audio
- synthesizers WDK audio , filters
- filters WDK audio , MIDI
- filters WDK audio , DirectMusic
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MIDI and DirectMusic Filters


## <span id="midi_and_directmusic_filters"></span><span id="MIDI_AND_DIRECTMUSIC_FILTERS"></span>


MIDI and DirectMusic filters represent devices that synthesize, output, or capture MIDI music data. Applications typically access the capabilities of these devices either through the DirectMusic API or through the Microsoft Windows Multimedia **midiOut***Xxx* and **midiIn***Xxx* functions. For more information about these interfaces, see the Microsoft Windows SDK documentation.

A MIDI or DirectMusic *synthesizer* filter receives as input a MIDI stream consisting of time-stamped MIDI events. The filter outputs either of the following:

-   A wave-formatted digital audio stream

-   Analog audio signals that can drive a set of speakers

A MIDI or DirectMusic *output* filter receives as input a MIDI stream consisting of time-stamped MIDI events. The filter outputs raw MIDI messages to an external MIDI sound module.

A MIDI or DirectMusic *capture* filter takes as input a series of raw MIDI messages from a MIDI keyboard or other external MIDI device. The filter outputs a MIDI stream consisting of time-stamped MIDI events.

A single MIDI or DirectMusic filter can perform a combination of the three functions--synthesis, output, and capture--depending on the capabilities of the device that the filter represents. For example, a pure MPU-401 device performs output and capture but not synthesis.

### <span id="MIDI_Filter"></span><span id="midi_filter"></span><span id="MIDI_FILTER"></span>MIDI Filter

A MIDI filter is implemented as a port/miniport driver pair. A MIDI filter factory creates a MIDI filter as follows:

-   It instantiates a MIDI miniport driver object.

-   It instantiates a MIDI port driver object by calling [**PcNewPort**](https://msdn.microsoft.com/library/windows/hardware/ff537715) with GUID value **CLSID\_PortMidi**.

-   It calls the port driver's [**IPort::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536943) method to bind the miniport driver to the port driver.

The code example in [Subdevice Creation](subdevice-creation.md) illustrates this process. The port and miniport drivers communicate with each other through their [IPortMidi](https://msdn.microsoft.com/library/windows/hardware/ff536891) and [IMiniportMidi](https://msdn.microsoft.com/library/windows/hardware/ff536703) interfaces.

To support MIDI output and synthesizer devices, the MIDI port driver contains a software sequencer that outputs raw MIDI messages to the miniport driver with a timer resolution of one millisecond.

### <span id="DirectMusic_Filter"></span><span id="directmusic_filter"></span><span id="DIRECTMUSIC_FILTER"></span>DirectMusic Filter

A DirectMusic filter provides a superset of the functionality of a MIDI filter. The superset includes these additional capabilities:

-   DLS (downloadable sound) resources that contain waveform and articulation data describing MIDI instruments. A [**KSPROPERTY\_SYNTH\_DLS\_DOWNLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff537396) set-property request downloads a DLS resource to a filter.

-   Channel groups for expanding the number of selectable instruments. The [**DMUS\_KERNEL\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/ff536340) structure, which is used to package each time-stamped MIDI message in a MIDI stream, specifies which channel group to use for that message.

-   64-bit time stamps with 100-nanosecond resolution in support of hardware MIDI sequencing. The DMUS\_KERNEL\_EVENT structure specifies the high-resolution time stamp for a MIDI message.

With channel groups, the number of notes that can be played simultaneously is no longer limited to the 16 channels of the original MIDI specification. It is limited only by the number of voices available in the synthesizer.

A DirectMusic filter is implemented as a port/miniport driver pair. A DirectMusic filter factory creates a DirectMusic filter as follows:

-   It instantiates a DMus (DirectMusic) miniport driver object.

-   It instantiates a DMus port driver object by calling [**PcNewPort**](https://msdn.microsoft.com/library/windows/hardware/ff537715) with GUID value **CLSID\_PortDMus**.

-   It calls the port driver's [**IPort::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536943) method to bind the miniport driver to the port driver.

The code example in [Subdevice Creation](subdevice-creation.md) illustrates this process. The port and miniport drivers communicate with each other through their [IPortDMus](https://msdn.microsoft.com/library/windows/hardware/ff536879) and [IMiniportDMus](https://msdn.microsoft.com/library/windows/hardware/ff536699) interfaces.

To support DirectMusic synthesizer devices, the DMus port driver contains a low-resolution (one millisecond) software sequencer that can output time-stamped MIDI events to the hardware sequencer's buffer in advance of when they are scheduled to be played. To support DirectMusic output devices, the port driver's software sequencer can also be configured to output raw MIDI messages at the times they are to be played.

### <span id="Enumerating_MIDI_and_DirectMusic_Devices"></span><span id="enumerating_midi_and_directmusic_devices"></span><span id="ENUMERATING_MIDI_AND_DIRECTMUSIC_DEVICES"></span>Enumerating MIDI and DirectMusic Devices

When enumerating MIDI input or output devices through the Windows Multimedia **midiInXxx** or **midiOutXxx** functions, an application can see only WDM devices whose miniport drivers expose *MIDI pins*. These are pins that manage raw MIDI streams but lack support for advanced features such as DLS and channel groups. However, when enumerating devices through DirectMusic, an application can see WDM devices with both MIDI pins and *DirectMusic pins*. DirectMusic pins manage time-stamped MIDI streams and support DLS and channel groups.

When implementing a custom miniport driver, a hardware vendor typically writes either a MIDI miniport driver or a DMus miniport driver, but not both. A MIDI miniport driver can expose only MIDI pins. However, a DMus miniport driver can expose both MIDI and DirectMusic pins, which eliminates the need to write a separate MIDI miniport driver. For an example of a MIDI pin on a DirectMusic filter, see the Dmusuart sample audio driver in the Windows Driver Kit (WDK).

When specifying a data range for a MIDI or DirectMusic pin, a MIDI or DMus miniport driver specifies a major format of type KSDATAFORMAT\_TYPE\_MUSIC and a subformat of type KSDATARANGE\_SUBTYPE\_MIDI for a MIDI pin or KSDATARANGE\_SUBTYPE\_DIRECTMUSIC for a DirectMusic pin. Examples of data range descriptors for MIDI and DirectMusic pins appear in [MIDI Stream Data Range](midi-stream-data-range.md) and [DirectMusic Stream Data Range](directmusic-stream-data-range.md), respectively.

A MIDI pin instance on a MIDI filter exposes an [IMiniportMidiStream](https://msdn.microsoft.com/library/windows/hardware/ff536704) interface. A MIDI or DirectMusic pin instance on a DirectMusic filter exposes an [IMXF](https://msdn.microsoft.com/library/windows/hardware/ff536782) interface.

In Windows Me/98, DirectMusic sometimes enumerates the same MPU-401 device twice. The reason is that some hardware vendors expose their MPU-401 devices both as legacy, pre-WDM MIDI devices and as WDM devices. For the legacy device, DirectMusic enumerates an MPU-401 device that represents the direct path from DMusic.dll to Ihvaudio.dll. For the WDM device, DirectMusic enumerates the same MPU-401 device through a circuitous path consisting of the following sequence of components:

1.  DMusic.dll

2.  DMusic16.dll

3.  MMSystem.dll

4.  WDMAud.drv

5.  WDMAud.sys

6.  The vendor's miniport driver

The MIDI synthesizer that shows up in the Windows multimedia control panel (Mmsys.cpl) will have the same name as the WDM device.

### <span id="System-Supplied_Port_and_Miniport_Drivers"></span><span id="system-supplied_port_and_miniport_drivers"></span><span id="SYSTEM-SUPPLIED_PORT_AND_MINIPORT_DRIVERS"></span>System-Supplied Port and Miniport Drivers

Several system-supplied MIDI and DMus miniport drivers are built into the PortCls system driver:

-   The FMSynth miniport driver provides an interface to a MIDI device that implements OPL3-style FM synthesis.

-   The UART miniport driver supports a MIDI device with an MPU-401 hardware interface, but this driver is now obsolete (after Windows 98 Gold) and is supported only for existing adapter drivers. New adapter driver code should instead use the DMusUART miniport driver (in Windows 98 SE and Windows Me, and in Windows 2000 and later), which supersedes UART and implements a superset of its functionality.

Adapter drivers can access the system-supplied miniport drivers by calling the [**PcNewMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff537714) function. The FMSynth and DMusUART miniport drivers are also included as sample audio drivers in the Windows Driver Kit (WDK). By modifying the source code in these samples, hardware vendors can extend the drivers to manage their devices' proprietary features.

DMusUART is an example of a DMus miniport driver that exposes both MIDI and DirectMusic pins, but does not support either DLS downloads or hardware sequencing. The miniport driver's DirectMusic rendering pin has a synth node ([**KSNODETYPE\_SYNTHESIZER**](https://msdn.microsoft.com/library/windows/hardware/ff537203)) that supports several [KSPROPSETID\_Synth](https://msdn.microsoft.com/library/windows/hardware/ff537486) properties. The miniport driver includes itself in categories KSCATEGORY\_RENDER and KSCATEGORY\_CAPTURE, but not in KSCATEGORY\_SYNTHESIZER (because it does not contain an internal synthesizer). For details, see the DMusUART sample audio driver in the WDK.

Note that in Windows XP and later, the MIDI and DMus port drivers use the same internal software implementation. This means that the **CLSID\_PortMidi** and **CLSID\_PortDMus** GUIDs are equivalent when calling **PcNewPort**. Applications written for previous versions of Windows should see no change in behavior resulting from consolidation of the MIDI and DMus port drivers.

 

 




