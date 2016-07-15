---
Description: DMus Miniport Driver
MS-HAID: 'audio.dmus\_miniport\_driver'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: DMus Miniport Driver
---

# DMus Miniport Driver


## <span id="dmus_miniport_driver"></span><span id="DMUS_MINIPORT_DRIVER"></span>


A DMus miniport driver manages the hardware-dependent functions of advanced MIDI devices. These devices support DirectMusic capabilities such as precision sequencer timing, downloadable sounds (DLS), and channel groups. DMus miniport drivers can achieve high performance with devices such as MPU-401. Timing can be handled by either the miniport driver or the port driver, depending on the capabilities of the hardware. A DMus miniport driver can also support a software synthesizer that generates a wave output stream.

A DMus miniport driver for a MIDI hardware device should support two interfaces:

-   The miniport interface initializes the miniport object and creates MIDI streams.

-   The stream interface manages a MIDI stream and exposes most of the miniport driver's functionality.

The miniport interface, [IMiniportDMus](audio.iminiportdmus), inherits the methods in the [IMiniport](audio.iminiport) interface. **IMiniportDMus** provides the following additional methods:

[**IMiniportDMus::Init**](audio.iminiportdmus_init)

Initializes the miniport object.
[**IMiniportDMus::NewStream**](audio.iminiportdmus_newstream)

Creates a new stream object.
[**IMiniportDMus::Service**](audio.iminiportdmus_service)

Notifies the miniport driver of a request for service.
The stream interface, [IMXF](audio.imxf), inherits the methods in the **IUnknown** interface. **IMXF** provides the following additional methods:

[**IMXF::ConnectOutput**](audio.imxf_connectoutput)

Connects this stream object, which is a data source, to the **IMXF** interface of another stream object, which is a data sink.
[**IMXF::DisconnectOutput**](audio.imxf_disconnectoutput)

Disconnects this stream object from the **IMXF** interface of another stream object that is a data sink.
[**IMXF::PutMessage**](audio.imxf_putmessage)

Passes a [**DMUS\_KERNEL\_EVENT**](audio.dmus_kernel_event) structure to the data sink.
[**IMXF::SetState**](audio.imxf_setstate)

Sets the state of the stream.
In addition, the DMus miniport driver's [ISynthSinkDMus](audio.isynthsinkdmus) interface provides DLS functionality for software synthesizers. **ISynthSinkDMus** inherits the methods in base interface **IMXF**. **ISynthSinkDMus** provides the following additional methods:

[**ISynthSinkDMus::RefTimeToSample**](audio.isynthsinkdmus_reftimetosample)

Converts a reference time to a sample time.
[**ISynthSinkDMus::Render**](audio.isynthsinkdmus_render)

Renders wave data into a buffer for the wave sink.
[**ISynthSinkDMus::SampleToRefTime**](audio.isynthsinkdmus_sampletoreftime)

Converts a sample time to a reference time.
[**ISynthSinkDMus::SyncToMaster**](audio.isynthsinkdmus_synctomaster)

Synchronizes the sample clock to the master clock.
The port driver's wave sink calls **ISynthSinkDMus::Render** to read the wave PCM data that the synthesizer generates from its MIDI input stream. For more information about the wave sink, see [A Wave Sink for Kernel-Mode Software Synthesizers](a-wave-sink-for-kernel-mode-software-synthesizers.md).

The miniport driver calls the following interfaces on the DMus port driver:

[IPortDMus](audio.iportdmus)

[IAllocatorMXF](audio.iallocatormxf)

[IMasterClock](audio.imasterclock)

PortCls contains a built-in DMus miniport driver for a MIDI device with a UART function. For more information, see [**PcNewMiniport**](audio.pcnewminiport).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20DMus%20Miniport%20Driver%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


