---
Description: Driver Support for Legacy Audio Interfaces
MS-HAID: 'audio.driver\_support\_for\_legacy\_audio\_interfaces'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Driver Support for Legacy Audio Interfaces
---

# Driver Support for Legacy Audio Interfaces


## <span id="driver_support_for_legacy_audio_interfaces"></span><span id="DRIVER_SUPPORT_FOR_LEGACY_AUDIO_INTERFACES"></span>


The WDM audio system provides driver support for application programs that access audio devices through the legacy Windows multimedia functions. These functions include the following audio-specific APIs:

-   aux

-   mixer

-   midiIn

-   midiOut

-   waveIn

-   waveOut

For information about these APIs, see the Microsoft Windows SDK documentation. For a description of the system components that provide driver support for legacy audio functions, see [WDM Audio Components](wdm-audio-components.md).

This section discusses features that audio miniport drivers can implement to better support the audio capabilities that the Windows multimedia functions expose to application programs. These capabilities include wave-stream capture and rendering, MIDI recording and synthesis, and mixer control. In addition, this section describes several extensions to the legacy audio-specific APIs that applications can use to retrieve driver-specific information about audio devices.

This section discusses the following topics:

[Kernel Streaming Topology to Audio Mixer API Translation](kernel-streaming-topology-to-audio-mixer-api-translation.md)

[WDM Audio Extensions to Legacy Windows Multimedia APIs](wdm-audio-extensions-to-legacy-windows-multimedia-apis.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Driver%20Support%20for%20Legacy%20Audio%20Interfaces%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



