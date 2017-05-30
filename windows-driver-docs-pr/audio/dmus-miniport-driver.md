---
title: DMus Miniport Driver
description: DMus Miniport Driver
ms.assetid: a0ce6545-2050-49fb-88b5-a75dcd4c7ebc
keywords:
- audio miniport drivers WDK , DMus
- miniport drivers WDK audio , DMus
- DirectMusic WDK audio , miniport drivers
- DMus miniport drivers WDK audio
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DMus Miniport Driver


## <span id="dmus_miniport_driver"></span><span id="DMUS_MINIPORT_DRIVER"></span>


A DMus miniport driver manages the hardware-dependent functions of advanced MIDI devices. These devices support DirectMusic capabilities such as precision sequencer timing, downloadable sounds (DLS), and channel groups. DMus miniport drivers can achieve high performance with devices such as MPU-401. Timing can be handled by either the miniport driver or the port driver, depending on the capabilities of the hardware. A DMus miniport driver can also support a software synthesizer that generates a wave output stream.

A DMus miniport driver for a MIDI hardware device should support two interfaces:

-   The miniport interface initializes the miniport object and creates MIDI streams.

-   The stream interface manages a MIDI stream and exposes most of the miniport driver's functionality.

The miniport interface, [IMiniportDMus](https://msdn.microsoft.com/library/windows/hardware/ff536699), inherits the methods in the [IMiniport](https://msdn.microsoft.com/library/windows/hardware/ff536698) interface. **IMiniportDMus** provides the following additional methods:

[**IMiniportDMus::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536700)

Initializes the miniport object.

[**IMiniportDMus::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536701)

Creates a new stream object.

[**IMiniportDMus::Service**](https://msdn.microsoft.com/library/windows/hardware/ff536702)

Notifies the miniport driver of a request for service.

The stream interface, [IMXF](https://msdn.microsoft.com/library/windows/hardware/ff536782), inherits the methods in the **IUnknown** interface. **IMXF** provides the following additional methods:

[**IMXF::ConnectOutput**](https://msdn.microsoft.com/library/windows/hardware/ff536785)

Connects this stream object, which is a data source, to the **IMXF** interface of another stream object, which is a data sink.

[**IMXF::DisconnectOutput**](https://msdn.microsoft.com/library/windows/hardware/ff536787)

Disconnects this stream object from the **IMXF** interface of another stream object that is a data sink.

[**IMXF::PutMessage**](https://msdn.microsoft.com/library/windows/hardware/ff536791)

Passes a [**DMUS\_KERNEL\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/ff536340) structure to the data sink.

[**IMXF::SetState**](https://msdn.microsoft.com/library/windows/hardware/ff536792)

Sets the state of the stream.

In addition, the DMus miniport driver's [ISynthSinkDMus](https://msdn.microsoft.com/library/windows/hardware/ff537011) interface provides DLS functionality for software synthesizers. **ISynthSinkDMus** inherits the methods in base interface **IMXF**. **ISynthSinkDMus** provides the following additional methods:

[**ISynthSinkDMus::RefTimeToSample**](https://msdn.microsoft.com/library/windows/hardware/ff537013)

Converts a reference time to a sample time.

[**ISynthSinkDMus::Render**](https://msdn.microsoft.com/library/windows/hardware/ff537015)

Renders wave data into a buffer for the wave sink.

[**ISynthSinkDMus::SampleToRefTime**](https://msdn.microsoft.com/library/windows/hardware/ff537018)

Converts a sample time to a reference time.

[**ISynthSinkDMus::SyncToMaster**](https://msdn.microsoft.com/library/windows/hardware/ff537019)

Synchronizes the sample clock to the master clock.

The port driver's wave sink calls **ISynthSinkDMus::Render** to read the wave PCM data that the synthesizer generates from its MIDI input stream. For more information about the wave sink, see [A Wave Sink for Kernel-Mode Software Synthesizers](a-wave-sink-for-kernel-mode-software-synthesizers.md).

The miniport driver calls the following interfaces on the DMus port driver:

[IPortDMus](https://msdn.microsoft.com/library/windows/hardware/ff536879)

[IAllocatorMXF](https://msdn.microsoft.com/library/windows/hardware/ff536491)

[IMasterClock](https://msdn.microsoft.com/library/windows/hardware/ff536696)

PortCls contains a built-in DMus miniport driver for a MIDI device with a UART function. For more information, see [**PcNewMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff537714).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20DMus%20Miniport%20Driver%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


