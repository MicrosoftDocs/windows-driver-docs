---
title: IMXF Interfaces
description: IMXF Interfaces
keywords:
- IMXF
- MIDI transport WDK audio
- wave sinks WDK audio , MIDI transport
- synthesizers WDK audio , MIDI transport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IMXF Interfaces


## <span id="imxf_interfaces"></span><span id="IMXF_INTERFACES"></span>


All MIDI transport in the DirectMusic port and miniport driver is carried out using the same interface: [IMXF](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-imxf).

**IMXF** is the COM interface for a DirectMusic MIDI transform filter. The miniport driver, the sequencer, and other entities in the port driver that handle MIDI data use **IMXF** as their common COM interface. When the miniport driver implements this interface, it can participate in MIDI transport. [IPortDMus](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iportdmus), which resides in PortCls, manages **IMXF**. The interface from the capture device to capture sink is also an **IMXF** interface.

MIDI data is transported between user mode and kernel mode in buffers of packed time-stamped data. The kernel port driver breaks these buffers into individual events (see [**DMUS\_KERNEL\_EVENT**](/windows-hardware/drivers/ddi/dmusicks/ns-dmusicks-_dmus_kernel_event)). The high-resolution MIDI sequencer passes these events to the miniport driver when the trigger time occurs.

On the input side, the kernel port driver extracts individual input messages from the miniport driver and builds packed buffers to pass up to user mode. Accordingly, the data transport model for DirectMusic miniport drivers consists of [**IMXF::PutMessage**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-imxf-putmessage) and [**IAllocatorMXF::GetMessage**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iallocatormxf-getmessage).

The **IMXF** interface supports the following methods:

[**IMXF::ConnectOutput**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-imxf-connectoutput)

[**IMXF::DisconnectOutput**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-imxf-disconnectoutput)

[**IMXF::PutMessage**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-imxf-putmessage)

[**IMXF::SetState**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-imxf-setstate)

The [IAllocatorMXF](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iallocatormxf) interface extends **IMXF** by adding the following methods:

[**IAllocatorMXF::GetMessage**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iallocatormxf-getmessage)

[**IAllocatorMXF::GetBufferSize**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iallocatormxf-getbuffersize)

[**IAllocatorMXF::GetBuffer**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iallocatormxf-getbuffer)

[**IAllocatorMXF::PutBuffer**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iallocatormxf-putbuffer)

For more information about the use of these interfaces, see [Allocator](allocator.md).

 

