---
title: MIDI Port Driver
description: MIDI Port Driver
ms.assetid: 4b403569-75c8-4cf4-bda1-efa9e004b529
keywords:
- MIDI port driver WDK audio
- PortCls WDK audio , port drivers
- audio miniport drivers WDK , port drivers
- miniport drivers WDK audio , port drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MIDI Port Driver


## <span id="midi_port_driver"></span><span id="MIDI_PORT_DRIVER"></span>


The MIDI port driver manages a MIDI synthesizer or capture device. The adapter driver provides a corresponding [MIDI miniport driver](midi-miniport-driver.md) that binds to the MIDI port driver object to form a MIDI filter (see [MIDI and DirectMusic Filters](midi-and-directmusic-filters.md)) that can capture or render a MIDI stream.

The MIDI port driver exposes an [IPortMidi](https://msdn.microsoft.com/library/windows/hardware/ff536891) interface to the miniport driver. **IPortMidi** inherits the methods in base interface [IPort](https://msdn.microsoft.com/library/windows/hardware/ff536842). **IPortMidi** provides the following additional methods:

[**IPortMidi::Notify**](https://msdn.microsoft.com/library/windows/hardware/ff536893)

Notifies the port driver that the MIDI synthesizer or capture device has advanced to a new position in the MIDI stream.
[**IPortMidi::RegisterServiceGroup**](https://msdn.microsoft.com/library/windows/hardware/ff536895)

Registers a service group object with the port driver.
A service group contains a list of one or more service routines that are to be called when the miniport driver calls **Notify**; for more information, see [Service Sink and Service Group Objects](service-sink-and-service-group-objects.md).

The MIDI port and miniport driver objects communicate with each other through their respective **IPortMidi** and [IMiniportMidi](https://msdn.microsoft.com/library/windows/hardware/ff536703) interfaces. The miniport driver uses the port driver's **IPortMidi** interface to notify the port driver of hardware interrupts. In addition, the port driver communicates with the miniport driver's stream objects through their [IMiniportMidiStream](https://msdn.microsoft.com/library/windows/hardware/ff536704) interfaces.

In Windows XP and later, the **IPortMidi** and [IPortDMus](https://msdn.microsoft.com/library/windows/hardware/ff536879) interfaces are both implemented in a single internal driver module. This consolidation is facilitated by the similarity of these two interfaces. For example, the same methods are defined for both interfaces. Applications written for previous versions of Windows should see no change in the behavior of the **IPortMidi** and **IPortDMus** interfaces resulting from consolidation of the MIDI and DMus port drivers.

 

 




