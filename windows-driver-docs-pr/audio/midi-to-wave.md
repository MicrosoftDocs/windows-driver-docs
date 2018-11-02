---
title: MIDI to Wave
description: MIDI to Wave
ms.assetid: 0c69ce48-ded0-44b8-9d34-20decb75058e
keywords:
- synthesizers WDK audio , MIDI-to-wave conversions
- MIDI-to-wave conversions WDK audio
- wave streams WDK audio
- custom synths WDK audio , MIDI-to-wave conversions
- user-mode synths WDK audio , MIDI-to-wave conversions
- converting MIDI to wave
- DirectMusic WDK audio , MIDI-to-wave conversions
- custom rendering in user mode WDK audio , MIDI-to-wave conversions
- DirectMusic custom rendering WDK audio , MIDI-to-wave conversions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MIDI to Wave


## <span id="midi_to_wave"></span><span id="MIDI_TO_WAVE"></span>


The main work of the synthesizer is done in two steps:

-   Getting MIDI messages

-   Mixing the rendered notes into the wave audio stream

This section details generally how this is done in user mode, although the concepts are essentially the same in kernel mode. See [Kernel Mode Hardware Acceleration DDI](kernel-mode-hardware-acceleration-ddi.md) for specifics on how to do the same with a kernel-mode miniport driver.

In user mode, the application calls [**IDirectMusicSynth::PlayBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536540) when it has MIDI messages ready to play. The application is responsible for calling **PlayBuffer** in a timely fashion and for time-stamping the buffer correctly, taking the [synthesizer latency](synthesizer-latency.md) into account. Your implementation of this method retrieves the waiting messages and stores them in an internal format, which is stamped with a time that is based on the reference time that is passed in with the buffer.

The wave sink calls [**IDirectMusicSynth::Render**](https://msdn.microsoft.com/library/windows/hardware/ff536541) whenever it is ready to receive data. For example, if the destination for the rendered data is a DirectSound secondary buffer, your implementation of [**IDirectMusicSynthSink::Activate**](https://msdn.microsoft.com/library/windows/hardware/ff536521) might set up a thread that waits for a DirectSound **PlayBuffer** notification. When the DirectSound buffer requires data, DirectSound notifies the thread, which in turn calls **Render**, passing in a pointer to the **IDirectSoundBuffer** object (described in the Microsoft Windows SDK documentation) and the number and position of the samples that are to be rendered.

The DirectSound buffer is circular. Because wraparound occurs at the end of the buffer, the possibility of a virtually contiguous region being split into two pieces must be taken into account. The wave sink typically handles the split by calling **Render** twice, once for each part of the locked portion of the DirectSound buffer, so that the **Render** method only has to deal with contiguous blocks of memory. The wave sink calls **IDirectSoundBuffer::Lock** on a DirectSound buffer to ask for write permission to a region within the buffer. For example, if the wave sink calls **Lock** on 2 kilobytes of data starting 1 kilobyte from the end of the buffer, then the call locks the last 1 kilobyte up to the end of the buffer and another 1 kilobyte starting at the beginning of the buffer. In this case, **Lock** actually returns two pointers and corresponding lengths, which together describe the region of the buffer that is locked. Each pointer is guaranteed to point to a contiguous block of memory.

Your implementation of the **Render** method is responsible for determining what must be done in response to the MIDI messages that are retrieved in **PlayBuffer**. From the *dwLength* parameter values of successive calls to **Render**, the method can keep track of the sample time and act on messages that are valid for the current rendering period. When a note-on message is processed, the note can be stored internally and rendered again on each pass through the method until a corresponding note-off message is received.

 

 




