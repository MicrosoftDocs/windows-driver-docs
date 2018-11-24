---
title: DLS Download Support
description: DLS Download Support
ms.assetid: be080b53-0a9d-47fc-b07b-88052efdf9a8
keywords:
- downloadable sounds WDK audio
- DirectMusic custom rendering WDK audio , downloadable sounds
- custom rendering in user mode WDK audio , downloadable sounds
- DLS WDK audio
- instrument sounds WDK audio
- converting MIDI note messages
- MIDI note conversions WDK audio
- user-mode synths WDK audio , downloadable sounds
- custom synths WDK audio , downloadable sounds
- synthesizers WDK audio , downloadable sounds
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DLS Download Support


## <span id="custom_dls"></span><span id="CUSTOM_DLS"></span>


If you are writing your own synthesizer, you also have to provide support for downloadable sounds (DLS) so that the application can convert MIDI note messages to particular instrument sounds. Specifically, you should implement your [**IDirectMusicSynth::Download**](https://msdn.microsoft.com/library/windows/hardware/ff536532) method so that it can download instrument wave and articulation data to the synthesizer. This method should accept raw data (typically from a collection file) and store it in a form that can be used by your rendering engine.

When DirectMusic downloads DLS data to the driver, the format of the data buffer is defined in terms of several DirectMusic structures. The downloaded data begins with two structures:

<span id="DMUS_DOWNLOADINFO"></span><span id="dmus_downloadinfo"></span>DMUS\_DOWNLOADINFO  
A fixed-size header describing the information that is being downloaded.

<span id="DMUS_OFFSETTABLE"></span><span id="dmus_offsettable"></span>DMUS\_OFFSETTABLE  
An offset table that follows the header and describes the offsets of the various chunks of information within the downloaded data.

Following the offset table is the actual data, which can begin with either of the following:

<span id="DMUS_INSTRUMENT"></span><span id="dmus_instrument"></span>DMUS\_INSTRUMENT  
A structure describing a DLS instrument.

<span id="DMUS_WAVEDATA"></span><span id="dmus_wavedata"></span>DMUS\_WAVEDATA  
A structure containing a chunk of wave data in PCM format.

For more information about these data structures and the data formats that are used to download instrument and wave data, see the discussion of DirectMusic low-level DLS in the Microsoft Windows SDK documentation.

The DLS data format is identical in kernel and user modes.

The [KSPROPSETID\_Synth\_Dls](https://msdn.microsoft.com/library/windows/hardware/ff537488) property set contains properties that are used to download DLS samples and instruments to a DirectMusic synthesizer. This property set can be used to download both DLS Level 1 and DLS Level 2 data. Only the format of the downloaded data changes between DLS Levels 1 and 2.

 

 




