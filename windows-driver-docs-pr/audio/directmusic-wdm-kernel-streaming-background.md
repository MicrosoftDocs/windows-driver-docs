---
title: DirectMusic WDM Kernel Streaming Background
description: DirectMusic WDM Kernel Streaming Background
ms.assetid: 851fa156-590a-43fb-9c49-df528f0ea608
keywords:
- DirectMusic kernel-mode WDK audio , WDM kernel streaming
- kernel-mode synths WDK audio , WDM kernel streaming
- WDM kernel streaming WDK audio
- kernel streaming WDK audio
- port drivers WDK audio , synthesizers
- hardware acceleration WDK audio
- miniport drivers WDK audio , kernel-mode hardware acceleration
- synthesizers WDK audio , kernel-mode hardware acceleration
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectMusic WDM Kernel Streaming Background


## <span id="directmusic_wdm_kernel_streaming_background"></span><span id="DIRECTMUSIC_WDM_KERNEL_STREAMING_BACKGROUND"></span>


This section may be useful for driver writers who are new to DirectMusic and WDM kernel streaming, or to anyone who wants a brief overview of kernel-mode architecture. Experienced WDM audio driver writers might want to skip to [Synthesizer Miniport Driver Overview](synthesizer-miniport-driver-overview.md). For a more general introduction to kernel streaming, see [Kernel Streaming](https://msdn.microsoft.com/library/windows/hardware/ff560842).

Historically, there were two types of drivers for Windows:

-   Windows 95-style VxDs

-   Drivers for the NT-based operating systems

Windows 98/Me contains ntkern.vxd, which has all the NT kernel services and allows most NT drivers to run on Windows 98/Me. WDM drivers use the NT driver environment for cross-platform compatibility. They also implement power management and Plug and Play.

WDM kernel streaming architecture had its roots in ActiveMovie (which became DirectShow), where the concept of filter chains was used for streaming media. Each filter in the chain could be a user-mode filter, a piece of user-mode code that served as a proxy for a kernel-mode filter, or even a piece of user-mode code that was marshaling a piece of hardware (see [Using AVStream with the Kernel Streaming Proxy Module](https://msdn.microsoft.com/library/windows/hardware/ff568671)). This architecture was brought into the Windows 2000 kernel to create kernel streaming.

The "pin" terminology comes originally from Microsoft DirectAnimation and DirectShow. A pin is now a kernel-streaming term for a target that can be used to connect one filter with another. For example, when there are two filters--the first with an "out" pin and the second with an "in" pin--the pins can be connected so that the first filter can pass a stream of data to the second filter. For more information, see [Audio Filter Graphs](audio-filter-graphs.md).

Kernel streaming is now part of WDM and is used by WDM Audio. DirectMusic uses the [WDMAud system driver](user-mode-wdm-audio-components.md#wdmaud_system_driver) as a kernel-mode component, passing its information down into kernel-mode in the form of I/O request packets (IRPs). All the DirectMusic interfaces are strictly WDM.

WDM kernel streaming audio filter chains are usually system-provided, but can also be provided by ISVs and IHVs. The [SysAudio system driver](kernel-mode-wdm-audio-components.md#sysaudio_system_driver) is a component that manages the filter chains. It locates the filters and hooks them together to construct a filter graph. (SysAudio is not itself a member of the graph.)

You do not need to be a kernel-streaming expert to implement your DMus miniport driver. Microsoft provides a large set of common code that vendors can leverage to make writing filters for DirectMusic easier. Vendors can write their miniport drivers to make use of the generic capabilities of the system-supplied DMus port driver. This approach is similar to the class driver/minidriver model that other Windows driver architectures use (for a comparison, see [WDM Audio Terminology](wdm-audio-terminology.md)).

WDM Audio has a component called PortCls (see [Port Class Adapter Driver and PortCls System Driver](kernel-mode-wdm-audio-components.md#port_class_adapter_driver_and_portcls_system_driver)), which is the class driver for several types of audio filters. These audio filters handle PCI wave devices, cyclical DMA wave devices, and MIDI devices. Instead of referring to the driver components as filters and mini-filters or as drivers and minidrivers, we refer to them as port and miniport drivers. PortCls contains a MIDI port driver, for example.

For each port driver, there can be different kinds of miniport drivers that do device-specific operations. For example, in Windows 98, there is one MIDI port driver and different miniport drivers can be connected to it, such as the MPU-401 device and FM synthesizer device. The port driver sequences MIDI data in the same way regardless of whether it is going to an FM or MPU device. The miniport driver handles the specifics of actually playing the MIDI data.

Because the sequencer is in the MIDI port driver itself, it holds the time-stamped data until it is due, then plays it through the appropriate miniport driver. For example, the MPU-401 miniport driver sends wave data to the device via the external synthesizer module. The miniport driver's output is managed by the port driver's wave sink.

The miniport driver stores up MIDI notes and when the wave sink, which is part of the MIDI port driver, asks for the next block of audio data, the miniport driver renders the requested amount of wave data into the specified memory location. For more information about this process, see [DirectMusic Miniport Driver Interface](directmusic-miniport-driver-interface.md).

Microsoft provides standard miniport driver functionality for all MPUs. Because the MPU specification defines exactly what the hardware should do and how it responds, Microsoft provides a miniport driver to handle MPUs as part of PortCls. All sound cards that have MPUs can use this same miniport driver.

The built-in miniport drivers in PortCls only attached to the MIDI port driver, so DirectMusic introduced the DMus port driver to attach to a DMus miniport driver. The DMus port driver handles MIDI sequencing and other functions for DirectMusic and manages MIDI, wave, and downloadable sounds (DLS) data. The sample MPU-401 adapter driver in the Windows Driver Kit (WDK) uses the DMus port driver and one of the DMus miniport drivers that are built into PortCls.

If all you need is MPU-401 functionality, use the built-in mpu401.sys miniport driver, which ships with the WDK. Just bind it to the DMus port driver and set an IRQ. Previously, this driver referenced the built-in interfaces that were identified by the **IID\_IPortMidi** (the MIDI port driver in PortCls) and **IID\_IMiniportDriverUart** (the MPU-401 miniport driver that is built into PortCls) class GUIDs (see [**PcNewPort**](https://msdn.microsoft.com/library/windows/hardware/ff537715) and [**PcNewMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff537714)). Now, the mpu401.sys driver references the **CLSID\_PortDMus** and **CLSID\_MiniportDriverDMusUART** GUIDs so that it can support DirectMusic.

When the DMus port driver receives MIDI data, it routes the data to the sequencer, which sorts each note on the basis of its time stamp. When the note is due, the sequencer passes it down to the miniport driver. The miniport driver implementation can specify how far in advance it wants to prefetch these notes.

When the DMus port driver receives a property-request containing DLS data (see [**KSPROPERTY\_SYNTH\_DLS\_DOWNLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff537396)), it routes the request directly to the miniport driver. Because these are just sounds that can be played, there is no need to involve the sequencer or wave sink when they are downloaded.

 

 




