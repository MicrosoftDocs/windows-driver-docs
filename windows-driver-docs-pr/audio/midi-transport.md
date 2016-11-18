---
title: MIDI Transport
description: MIDI Transport
ms.assetid: ce9ec589-0aea-4ed9-a60d-50f2ddfb0c13
keywords: ["port drivers WDK audio , synthesizers", "miniport drivers WDK audio , synthesizers", "MIDI transport WDK audio", "wave sinks WDK audio , MIDI transport", "synthesizers WDK audio , MIDI transport"]
---

# MIDI Transport


## <span id="midi_transport"></span><span id="MIDI_TRANSPORT"></span>


The DMus port driver is involved on the front and back sides of the DMus miniport driver's synthesizer work. The port driver inputs a MIDI stream that consists of time-stamped MIDI data and routes the stream to the sequencer. The sequencer removes the time stamps and passes the raw MIDI messages to the miniport driver when their time stamps are due. (DLS data passes right through the port driver to the miniport driver with no preprocessing.)

When DMus miniport driver's MIDI input stream gets converted to wave data, its output is managed by the wave sink (also called a "synth sink" or "render sink").

The DMus port driver implements a kernel-streaming filter with an input pin that accepts DirectMusic data from the DirectMusic user-mode component, dmusic.dll. The port driver also has a wave-output pin that emits the synthesized audio stream. The wave sink manages this pin and tells the synth where in memory to write its data. This arrangement insulates the synth from the details of kernel streaming. Your DMus miniport driver needs only to deal with the details of synthesizing wave data from the input MIDI stream. The port driver sends the wave data out to the system, and SysAudio's filter graph connects the filters to make everything flow correctly. As shown in the following diagram, MIDI data comes into the DMus port driver and, after sequencing, is passed to the DMus miniport driver.

![diagram illustrating the flow of midi and dls data through the portdmus driver](images/dmportmi.png)

The miniport driver converts the MIDI data to wave format, which is rendered into a buffer that is designated by another part of the port driver: the wave sink. Then, instead of going out to DirectSound as it does in user mode, the wave output goes to the audio hardware through the [KMixer system driver](kernel-mode-wdm-audio-components.md#kmixer_system_driver). DirectSound is really just an API that exposes KMixer, and DirectSound acceleration consists of the mixer functions being accelerated in hardware instead of emulated in software by KMixer.

The [SysAudio system driver](kernel-mode-wdm-audio-components.md#sysaudio_system_driver), which builds the audio filter graph, connects the DMus port driver to a piece of hardware. The wave sink portion of the port driver hands the data out through its wave-out pin, which SysAudio can connect to the hardware device. It pulls wave data from the DMus miniport driver (without regard to whether it is a hardware or software synth), and handles all timing issues. Compared to user mode, the miniport driver is analogous to the synth, whereas the wave sink is just part of the port driver.

If a DMus miniport driver can provide its output back to the host, it exposes a wave pin with a data direction of KSPIN\_DATAFLOW\_OUT (see [**KSPIN**](https://msdn.microsoft.com/library/windows/hardware/ff563483)), which SysAudio recognizes and connects to KMixer.

For more information about the wave sink, see [A Wave Sink for Kernel-Mode Software Synthesizers](a-wave-sink-for-kernel-mode-software-synthesizers.md).

This section also includes:

[IMXF Interfaces](imxf-interfaces.md)

[Allocator](allocator.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20MIDI%20Transport%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


