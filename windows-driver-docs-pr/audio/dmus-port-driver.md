---
title: DMus Port Driver
description: DMus Port Driver
ms.assetid: 19828364-1b0d-4fc0-b142-9d776cbf1ada
keywords:
- DirectMusic WDK audio , port drivers
- DMus port drivers WDK audio
- PortCls WDK audio , port drivers
- audio miniport drivers WDK , port drivers
- miniport drivers WDK audio , port drivers
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DMus Port Driver


## <span id="dmus_port_driver"></span><span id="DMUS_PORT_DRIVER"></span>


The DMus port driver manages a Microsoft DirectMusic synthesizer or capture device. In contrast to the MIDI port driver, which supports only simple MIDI devices, the DMus port driver supports devices with advanced MIDI capabilities such as precision sequencer timing, downloadable sounds (DLS), and channel groups. The adapter driver implements a corresponding [DMus miniport driver](dmus-miniport-driver.md) that binds to the DMus port driver to form a DirectMusic filter (see [MIDI and DirectMusic Filters](midi-and-directmusic-filters.md)) that can render or capture a MIDI stream.

The DMus port driver exposes an [IPortDMus](https://msdn.microsoft.com/library/windows/hardware/ff536879) interface to the miniport driver. **IPortDMus** inherits the methods in base interface [IPort](https://msdn.microsoft.com/library/windows/hardware/ff536842). **IPortDMus** provides the following additional methods:

[**IPortDMus::Notify**](https://msdn.microsoft.com/library/windows/hardware/ff536880)

Notifies the port driver that the MIDI synthesizer or capture device has advanced to a new position in the MIDI stream.
[**IPortDMus::RegisterServiceGroup**](https://msdn.microsoft.com/library/windows/hardware/ff536882)

Registers a service group object with the port driver.
The registered service group contains a list of one or more service routines that are called by the port driver when the miniport driver calls **Notify**; for more information, see [Service Sink and Service Group Objects](service-sink-and-service-group-objects.md).

The DMus port driver also creates a memory [allocator](allocator.md) for each stream and exposes the allocator's [IAllocatorMXF](https://msdn.microsoft.com/library/windows/hardware/ff536491) interface to the miniport driver's stream object. **IAllocatorMXF** inherits the methods in base interface [IMXF](https://msdn.microsoft.com/library/windows/hardware/ff536782). **IAllocatorMXF** provides the following additional methods:

[**IAllocatorMXF::GetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536492)

Gets a buffer for a MIDI event or list of events that is too large to fit within a [**DMUS\_KERNEL\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/ff536340) structure.
[**IAllocatorMXF::GetBufferSize**](https://msdn.microsoft.com/library/windows/hardware/ff536493)

Gets the size in bytes of the buffer retrieved by the **GetBuffer** method.
[**IAllocatorMXF::GetMessage**](https://msdn.microsoft.com/library/windows/hardware/ff536494)

Gets a message buffer containing storage for a single structure of type DMUS\_KERNEL\_EVENT.
[**IAllocatorMXF::PutBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536495)

Not used.
The DMus port and miniport driver objects communicate with each other through their respective **IPortDMus** and [IMiniportMidi](https://msdn.microsoft.com/library/windows/hardware/ff536703) interfaces. In addition, the port driver communicates with the miniport driver's stream objects through their [IMXF](https://msdn.microsoft.com/library/windows/hardware/ff536782) interfaces, and a miniport driver's stream object communicates with the port driver's allocator through its **IAllocatorMXF** interface.

For more information about driver support for DirectMusic, see [Synthesizer Miniport Driver Overview](synthesizer-miniport-driver-overview.md).

In Windows XP and later, the **IPortDMus** and [IPortMidi](https://msdn.microsoft.com/library/windows/hardware/ff536891) interfaces are both implemented in a single internal driver module. This consolidation is facilitated by the similarity of these two interfaces. For example, the same methods are defined for both interfaces. Applications written for previous versions of Windows should see no change in the behavior of the **IPortMidi** and **IPortDMus** interfaces resulting from consolidation of the MIDI and DMus port drivers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20DMus%20Port%20Driver%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


