---
title: IMXF Interfaces
description: IMXF Interfaces
ms.assetid: 3782f812-bb95-4735-9635-e721ccda92b5
keywords:
- IMXF
- MIDI transport WDK audio
- wave sinks WDK audio , MIDI transport
- synthesizers WDK audio , MIDI transport
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20IMXF%20Interfaces%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


