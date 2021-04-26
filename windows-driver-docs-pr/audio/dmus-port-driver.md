---
title: DMus Port Driver
description: DMus Port Driver
keywords:
- DirectMusic WDK audio , port drivers
- DMus port drivers WDK audio
- PortCls WDK audio , port drivers
- audio miniport drivers WDK , port drivers
- miniport drivers WDK audio , port drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DMus Port Driver


## <span id="dmus_port_driver"></span><span id="DMUS_PORT_DRIVER"></span>


The DMus port driver manages a Microsoft DirectMusic synthesizer or capture device. In contrast to the MIDI port driver, which supports only simple MIDI devices, the DMus port driver supports devices with advanced MIDI capabilities such as precision sequencer timing, downloadable sounds (DLS), and channel groups. The adapter driver implements a corresponding [DMus miniport driver](dmus-miniport-driver.md) that binds to the DMus port driver to form a DirectMusic filter (see [MIDI and DirectMusic Filters](midi-and-directmusic-filters.md)) that can render or capture a MIDI stream.

The DMus port driver exposes an [IPortDMus](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iportdmus) interface to the miniport driver. **IPortDMus** inherits the methods in base interface [IPort](/windows-hardware/drivers/ddi/portcls/nn-portcls-iport). **IPortDMus** provides the following additional methods:

[**IPortDMus::Notify**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iportdmus-notify)

Notifies the port driver that the MIDI synthesizer or capture device has advanced to a new position in the MIDI stream.

[**IPortDMus::RegisterServiceGroup**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iportdmus-registerservicegroup)

Registers a service group object with the port driver.
The registered service group contains a list of one or more service routines that are called by the port driver when the miniport driver calls **Notify**; for more information, see [Service Sink and Service Group Objects](service-sink-and-service-group-objects.md).

The DMus port driver also creates a memory [allocator](allocator.md) for each stream and exposes the allocator's [IAllocatorMXF](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iallocatormxf) interface to the miniport driver's stream object. **IAllocatorMXF** inherits the methods in base interface [IMXF](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-imxf). **IAllocatorMXF** provides the following additional methods:

[**IAllocatorMXF::GetBuffer**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iallocatormxf-getbuffer)

Gets a buffer for a MIDI event or list of events that is too large to fit within a [**DMUS\_KERNEL\_EVENT**](/windows-hardware/drivers/ddi/dmusicks/ns-dmusicks-_dmus_kernel_event) structure.

[**IAllocatorMXF::GetBufferSize**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iallocatormxf-getbuffersize)

Gets the size in bytes of the buffer retrieved by the **GetBuffer** method.

[**IAllocatorMXF::GetMessage**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iallocatormxf-getmessage)

Gets a message buffer containing storage for a single structure of type DMUS\_KERNEL\_EVENT.

[**IAllocatorMXF::PutBuffer**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iallocatormxf-putbuffer)

Not used.
The DMus port and miniport driver objects communicate with each other through their respective **IPortDMus** and [IMiniportMidi](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportmidi) interfaces. In addition, the port driver communicates with the miniport driver's stream objects through their [IMXF](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-imxf) interfaces, and a miniport driver's stream object communicates with the port driver's allocator through its **IAllocatorMXF** interface.

For more information about driver support for DirectMusic, see [Synthesizer Miniport Driver Overview](synthesizer-miniport-driver-overview.md).

In Windows XP and later, the **IPortDMus** and [IPortMidi](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportmidi) interfaces are both implemented in a single internal driver module. This consolidation is facilitated by the similarity of these two interfaces. For example, the same methods are defined for both interfaces. Applications written for previous versions of Windows should see no change in the behavior of the **IPortMidi** and **IPortDMus** interfaces resulting from consolidation of the MIDI and DMus port drivers.

 

