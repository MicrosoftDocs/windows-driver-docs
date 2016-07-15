---
Description: MIDI Miniport Driver
MS-HAID: 'audio.midi\_miniport\_driver'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: MIDI Miniport Driver
---

# MIDI Miniport Driver


## <span id="midi_miniport_driver"></span><span id="MIDI_MINIPORT_DRIVER"></span>


A MIDI miniport driver manages the hardware-dependent functions of simple MIDI devices that lack advanced capabilities such as hardware sequencing and downloadable sounds (DLS). The MIDI port driver handles the timing of the delivery of MIDI messages to synthesizers. The MIDI miniport driver is responsible only for transporting the MIDI messages to the synthesizer in response to requests from the port driver. Devices with advanced MIDI capabilities should use a [DMus miniport driver](dmus-miniport-driver.md) instead.

A MIDI miniport driver should implement two interfaces:

-   The *miniport interface* initializes the miniport object and creates MIDI streams.

-   The *stream interface* manages a MIDI stream and exposes most of the miniport driver's functionality.

The miniport interface, [IMiniportMidi](audio.iminiportmidi), inherits the methods in the [IMiniport](audio.iminiport) interface. **IMiniportMidi** provides the following additional methods:

[**IMiniportMidi::Init**](audio.iminiportmidi_init)

Initializes the miniport object.
[**IMiniportMidi::NewStream**](audio.iminiportmidi_newstream)

Creates a new stream object.
[**IMiniportMidi::Service**](audio.iminiportmidi_service)

Notifies the miniport driver of a request for service.
The stream interface, [IMiniportMidiStream](audio.iminiportmidistream), inherits the methods in the **IUnknown** interface. **IMiniportMidiStream** provides the following additional methods:

[**IMiniportMidiStream::Read**](audio.iminiportmidistream_read)

Reads input data from a MIDI capture device.
[**IMiniportMidiStream::SetFormat**](audio.iminiportmidistream_setformat)

Sets the data format of the MIDI stream.
[**IMiniportMidiStream::SetState**](audio.iminiportmidistream_setstate)

Sets the state of the MIDI stream.
[**IMiniportMidiStream::Write**](audio.iminiportmidistream_write)

Writes output data to a MIDI synthesizer.
The MIDI port driver handles all timing issues in both directions and relies on the miniport driver to promptly move data on and off the adapter in response to the port driver's calls to the **IMiniportMidiStream** read and write methods.

PortCls contains built-in MIDI miniport drivers for MIDI devices that have FM synth and UART functions. For more information, see [**PcNewMiniport**](audio.pcnewminiport).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20MIDI%20Miniport%20Driver%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


