---
title: MIDI Miniport Driver
description: MIDI Miniport Driver
keywords:
- audio miniport drivers WDK , MIDI
- miniport drivers WDK audio , MIDI
- MIDI miniport drivers WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MIDI Miniport Driver


## <span id="midi_miniport_driver"></span><span id="MIDI_MINIPORT_DRIVER"></span>


A MIDI miniport driver manages the hardware-dependent functions of simple MIDI devices that lack advanced capabilities such as hardware sequencing and downloadable sounds (DLS). The MIDI port driver handles the timing of the delivery of MIDI messages to synthesizers. The MIDI miniport driver is responsible only for transporting the MIDI messages to the synthesizer in response to requests from the port driver. Devices with advanced MIDI capabilities should use a [DMus miniport driver](dmus-miniport-driver.md) instead.

A MIDI miniport driver should implement two interfaces:

-   The *miniport interface* initializes the miniport object and creates MIDI streams.

-   The *stream interface* manages a MIDI stream and exposes most of the miniport driver's functionality.

The miniport interface, [IMiniportMidi](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportmidi), inherits the methods in the [IMiniport](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiport) interface. **IMiniportMidi** provides the following additional methods:

[**IMiniportMidi::Init**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportmidi-init)

Initializes the miniport object.

[**IMiniportMidi::NewStream**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportmidi-newstream)

Creates a new stream object.

[**IMiniportMidi::Service**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportmidi-service)

Notifies the miniport driver of a request for service.

The stream interface, [IMiniportMidiStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportmidistream), inherits the methods in the **IUnknown** interface. **IMiniportMidiStream** provides the following additional methods:

[**IMiniportMidiStream::Read**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportmidistream-read)

Reads input data from a MIDI capture device.

[**IMiniportMidiStream::SetFormat**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportmidistream-setformat)

Sets the data format of the MIDI stream.

[**IMiniportMidiStream::SetState**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportmidistream-setstate)

Sets the state of the MIDI stream.

[**IMiniportMidiStream::Write**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportmidistream-write)

Writes output data to a MIDI synthesizer.

The MIDI port driver handles all timing issues in both directions and relies on the miniport driver to promptly move data on and off the adapter in response to the port driver's calls to the **IMiniportMidiStream** read and write methods.

PortCls contains built-in MIDI miniport drivers for MIDI devices that have FM synth and UART functions. For more information, see [**PcNewMiniport**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewminiport).

 

