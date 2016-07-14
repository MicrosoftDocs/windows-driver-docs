---
Description: Basic Functions of a WDM Audio Driver
MS-HAID: 'audio.basic\_functions\_of\_a\_wdm\_audio\_driver'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Basic Functions of a WDM Audio Driver
---

# Basic Functions of a WDM Audio Driver


## <span id="basic_functions_of_a_wdm_audio_driver"></span><span id="BASIC_FUNCTIONS_OF_A_WDM_AUDIO_DRIVER"></span>


A Microsoft Windows Driver Model (WDM) audio driver provides the following functionality:

-   The driver exposes all the types of input and output streams, and the number of instances of each stream type that it can support. The driver provides this information in the form of a set of pin factories and the number of pins that each factory can instantiate. For example, a simple audio device might input a single PCM audio stream and output a single PCM audio stream. The filter for this device contains two pin factories--one for the input stream an one for the output stream--and each pin factory supports only a single pin instance. If the adapter card contains only one of these devices, the adapter driver provides a filter factory containing only a single instance of a filter with these capabilities.

-   The driver supports one or more property sets. For example, all audio drivers should support [KSPROPSETID\_Audio](audio.kspropsetid_audio), but some audio drivers might support additional property sets as well. Clients of the driver use property requests both to discover a filter's capabilities and to change the filter's configurable settings.

-   The driver optionally supports a hardware clock. This clock should be readable and writable so that streams can synchronize with other streams on the same or different hardware. For additional information, see [KSPROPSETID\_Clock](stream.kspropsetid_clock).

-   The driver optionally supports other media interfaces, such as [**KSINTERFACE\_STANDARD\_STREAMING**](stream.ksinterface_standard_streaming), [**KSINTERFACE\_MEDIA\_WAVE\_QUEUED**](stream.ksinterface_media_wave_queued), or [**KSINTERFACE\_STANDARD\_LOOPED\_STREAMING**](stream.ksinterface_standard_looped_streaming).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Basic%20Functions%20of%20a%20WDM%20Audio%20Driver%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



