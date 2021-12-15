---
title: DMus Miniport Driver
description: DMus Miniport Driver
keywords:
- audio miniport drivers WDK , DMus
- miniport drivers WDK audio , DMus
- DirectMusic WDK audio , miniport drivers
- DMus miniport drivers WDK audio
ms.date: 04/20/2017
---

# DMus Miniport Driver


## <span id="dmus_miniport_driver"></span><span id="DMUS_MINIPORT_DRIVER"></span>


A DMus miniport driver manages the hardware-dependent functions of advanced MIDI devices. These devices support DirectMusic capabilities such as precision sequencer timing, downloadable sounds (DLS), and channel groups. DMus miniport drivers can achieve high performance with devices such as MPU-401. Timing can be handled by either the miniport driver or the port driver, depending on the capabilities of the hardware. A DMus miniport driver can also support a software synthesizer that generates a wave output stream.

A DMus miniport driver for a MIDI hardware device should support two interfaces:

-   The miniport interface initializes the miniport object and creates MIDI streams.

-   The stream interface manages a MIDI stream and exposes most of the miniport driver's functionality.

The miniport interface, [IMiniportDMus](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iminiportdmus), inherits the methods in the [IMiniport](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiport) interface. **IMiniportDMus** provides the following additional methods:

[**IMiniportDMus::Init**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iminiportdmus-init)

Initializes the miniport object.

[**IMiniportDMus::NewStream**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iminiportdmus-newstream)

Creates a new stream object.

[**IMiniportDMus::Service**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iminiportdmus-service)

Notifies the miniport driver of a request for service.

The stream interface, [IMXF](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-imxf), inherits the methods in the **IUnknown** interface. **IMXF** provides the following additional methods:

[**IMXF::ConnectOutput**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-imxf-connectoutput)

Connects this stream object, which is a data source, to the **IMXF** interface of another stream object, which is a data sink.

[**IMXF::DisconnectOutput**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-imxf-disconnectoutput)

Disconnects this stream object from the **IMXF** interface of another stream object that is a data sink.

[**IMXF::PutMessage**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-imxf-putmessage)

Passes a [**DMUS\_KERNEL\_EVENT**](/windows-hardware/drivers/ddi/dmusicks/ns-dmusicks-_dmus_kernel_event) structure to the data sink.

[**IMXF::SetState**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-imxf-setstate)

Sets the state of the stream.

In addition, the DMus miniport driver's [ISynthSinkDMus](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-isynthsinkdmus) interface provides DLS functionality for software synthesizers. **ISynthSinkDMus** inherits the methods in base interface **IMXF**. **ISynthSinkDMus** provides the following additional methods:

[**ISynthSinkDMus::RefTimeToSample**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-isynthsinkdmus-reftimetosample)

Converts a reference time to a sample time.

[**ISynthSinkDMus::Render**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-isynthsinkdmus-render)

Renders wave data into a buffer for the wave sink.

[**ISynthSinkDMus::SampleToRefTime**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-isynthsinkdmus-sampletoreftime)

Converts a sample time to a reference time.

[**ISynthSinkDMus::SyncToMaster**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-isynthsinkdmus-synctomaster)

Synchronizes the sample clock to the master clock.

The port driver's wave sink calls **ISynthSinkDMus::Render** to read the wave PCM data that the synthesizer generates from its MIDI input stream. For more information about the wave sink, see [A Wave Sink for Kernel-Mode Software Synthesizers](a-wave-sink-for-kernel-mode-software-synthesizers.md).

The miniport driver calls the following interfaces on the DMus port driver:

[IPortDMus](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iportdmus)

[IAllocatorMXF](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iallocatormxf)

[IMasterClock](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-imasterclock)

PortCls contains a built-in DMus miniport driver for a MIDI device with a UART function. For more information, see [**PcNewMiniport**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewminiport).

 

