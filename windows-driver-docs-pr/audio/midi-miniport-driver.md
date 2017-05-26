---
title: MIDI Miniport Driver
description: MIDI Miniport Driver
ms.assetid: 38aeba40-35da-4bfd-a8fe-cf8f7e96f286
keywords:
- audio miniport drivers WDK , MIDI
- miniport drivers WDK audio , MIDI
- MIDI miniport drivers WDK audio
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MIDI Miniport Driver


## <span id="midi_miniport_driver"></span><span id="MIDI_MINIPORT_DRIVER"></span>


A MIDI miniport driver manages the hardware-dependent functions of simple MIDI devices that lack advanced capabilities such as hardware sequencing and downloadable sounds (DLS). The MIDI port driver handles the timing of the delivery of MIDI messages to synthesizers. The MIDI miniport driver is responsible only for transporting the MIDI messages to the synthesizer in response to requests from the port driver. Devices with advanced MIDI capabilities should use a [DMus miniport driver](dmus-miniport-driver.md) instead.

A MIDI miniport driver should implement two interfaces:

-   The *miniport interface* initializes the miniport object and creates MIDI streams.

-   The *stream interface* manages a MIDI stream and exposes most of the miniport driver's functionality.

The miniport interface, [IMiniportMidi](https://msdn.microsoft.com/library/windows/hardware/ff536703), inherits the methods in the [IMiniport](https://msdn.microsoft.com/library/windows/hardware/ff536698) interface. **IMiniportMidi** provides the following additional methods:

[**IMiniportMidi::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536709)

Initializes the miniport object.

[**IMiniportMidi::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536710)

Creates a new stream object.

[**IMiniportMidi::Service**](https://msdn.microsoft.com/library/windows/hardware/ff536711)

Notifies the miniport driver of a request for service.

The stream interface, [IMiniportMidiStream](https://msdn.microsoft.com/library/windows/hardware/ff536704), inherits the methods in the **IUnknown** interface. **IMiniportMidiStream** provides the following additional methods:

[**IMiniportMidiStream::Read**](https://msdn.microsoft.com/library/windows/hardware/ff536705)

Reads input data from a MIDI capture device.

[**IMiniportMidiStream::SetFormat**](https://msdn.microsoft.com/library/windows/hardware/ff536706)

Sets the data format of the MIDI stream.

[**IMiniportMidiStream::SetState**](https://msdn.microsoft.com/library/windows/hardware/ff536707)

Sets the state of the MIDI stream.

[**IMiniportMidiStream::Write**](https://msdn.microsoft.com/library/windows/hardware/ff536708)

Writes output data to a MIDI synthesizer.

The MIDI port driver handles all timing issues in both directions and relies on the miniport driver to promptly move data on and off the adapter in response to the port driver's calls to the **IMiniportMidiStream** read and write methods.

PortCls contains built-in MIDI miniport drivers for MIDI devices that have FM synth and UART functions. For more information, see [**PcNewMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff537714).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20MIDI%20Miniport%20Driver%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


