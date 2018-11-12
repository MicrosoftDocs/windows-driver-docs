---
title: IMXF Interfaces
description: IMXF Interfaces
ms.assetid: 3782f812-bb95-4735-9635-e721ccda92b5
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


All MIDI transport in the DirectMusic port and miniport driver is carried out using the same interface: [IMXF](https://msdn.microsoft.com/library/windows/hardware/ff536782).

**IMXF** is the COM interface for a DirectMusic MIDI transform filter. The miniport driver, the sequencer, and other entities in the port driver that handle MIDI data use **IMXF** as their common COM interface. When the miniport driver implements this interface, it can participate in MIDI transport. [IPortDMus](https://msdn.microsoft.com/library/windows/hardware/ff536879), which resides in PortCls, manages **IMXF**. The interface from the capture device to capture sink is also an **IMXF** interface.

MIDI data is transported between user mode and kernel mode in buffers of packed time-stamped data. The kernel port driver breaks these buffers into individual events (see [**DMUS\_KERNEL\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/ff536340)). The high-resolution MIDI sequencer passes these events to the miniport driver when the trigger time occurs.

On the input side, the kernel port driver extracts individual input messages from the miniport driver and builds packed buffers to pass up to user mode. Accordingly, the data transport model for DirectMusic miniport drivers consists of [**IMXF::PutMessage**](https://msdn.microsoft.com/library/windows/hardware/ff536791) and [**IAllocatorMXF::GetMessage**](https://msdn.microsoft.com/library/windows/hardware/ff536494).

The **IMXF** interface supports the following methods:

[**IMXF::ConnectOutput**](https://msdn.microsoft.com/library/windows/hardware/ff536785)

[**IMXF::DisconnectOutput**](https://msdn.microsoft.com/library/windows/hardware/ff536787)

[**IMXF::PutMessage**](https://msdn.microsoft.com/library/windows/hardware/ff536791)

[**IMXF::SetState**](https://msdn.microsoft.com/library/windows/hardware/ff536792)

The [IAllocatorMXF](https://msdn.microsoft.com/library/windows/hardware/ff536491) interface extends **IMXF** by adding the following methods:

[**IAllocatorMXF::GetMessage**](https://msdn.microsoft.com/library/windows/hardware/ff536494)

[**IAllocatorMXF::GetBufferSize**](https://msdn.microsoft.com/library/windows/hardware/ff536493)

[**IAllocatorMXF::GetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536492)

[**IAllocatorMXF::PutBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536495)

For more information about the use of these interfaces, see [Allocator](allocator.md).

 

 




