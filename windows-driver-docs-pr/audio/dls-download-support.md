---
title: DLS Download Support
description: DLS Download Support
ms.assetid: be080b53-0a9d-47fc-b07b-88052efdf9a8
keywords: ["downloadable sounds WDK audio", "DirectMusic custom rendering WDK audio , downloadable sounds", "custom rendering in user mode WDK audio , downloadable sounds", "DLS WDK audio", "instrument sounds WDK audio", "converting MIDI note messages", "MIDI note conversions WDK audio", "user-mode synths WDK audio , downloadable sounds", "custom synths WDK audio , downloadable sounds", "synthesizers WDK audio , downloadable sounds"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20DLS%20Download%20Support%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




