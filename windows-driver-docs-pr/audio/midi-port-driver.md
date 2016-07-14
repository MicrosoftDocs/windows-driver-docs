---
Description: MIDI Port Driver
MS-HAID: 'audio.midi\_port\_driver'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: MIDI Port Driver
---

# MIDI Port Driver


## <span id="midi_port_driver"></span><span id="MIDI_PORT_DRIVER"></span>


The MIDI port driver manages a MIDI synthesizer or capture device. The adapter driver provides a corresponding [MIDI miniport driver](midi-miniport-driver.md) that binds to the MIDI port driver object to form a MIDI filter (see [MIDI and DirectMusic Filters](midi-and-directmusic-filters.md)) that can capture or render a MIDI stream.

The MIDI port driver exposes an [IPortMidi](audio.iportmidi) interface to the miniport driver. **IPortMidi** inherits the methods in base interface [IPort](audio.iport). **IPortMidi** provides the following additional methods:

[**IPortMidi::Notify**](audio.iportmidi_notify)

Notifies the port driver that the MIDI synthesizer or capture device has advanced to a new position in the MIDI stream.
[**IPortMidi::RegisterServiceGroup**](audio.iportmidi_registerservicegroup)

Registers a service group object with the port driver.
A service group contains a list of one or more service routines that are to be called when the miniport driver calls **Notify**; for more information, see [Service Sink and Service Group Objects](service-sink-and-service-group-objects.md).

The MIDI port and miniport driver objects communicate with each other through their respective **IPortMidi** and [IMiniportMidi](audio.iminiportmidi) interfaces. The miniport driver uses the port driver's **IPortMidi** interface to notify the port driver of hardware interrupts. In addition, the port driver communicates with the miniport driver's stream objects through their [IMiniportMidiStream](audio.iminiportmidistream) interfaces.

In Windows XP and later, the **IPortMidi** and [IPortDMus](audio.iportdmus) interfaces are both implemented in a single internal driver module. This consolidation is facilitated by the similarity of these two interfaces. For example, the same methods are defined for both interfaces. Applications written for previous versions of Windows should see no change in the behavior of the **IPortMidi** and **IPortDMus** interfaces resulting from consolidation of the MIDI and DMus port drivers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20MIDI%20Port%20Driver%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



