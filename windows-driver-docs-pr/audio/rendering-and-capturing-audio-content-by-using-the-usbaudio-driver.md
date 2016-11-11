---
title: Rendering and Capturing Audio Content by Using the USBAudio Driver
description: Rendering and Capturing Audio Content by Using the USBAudio Driver
ms.assetid: 92a6ad18-75ba-4382-a6d1-42f28133a158
keywords: ["USBAudio class system driver WDK audio"]
---

# Rendering and Capturing Audio Content by Using the USBAudio Driver


## <span id="ddk_rendering_and_capturing_audio_content_by_using_the_usbaudio_driver"></span><span id="DDK_RENDERING_AND_CAPTURING_AUDIO_CONTENT_BY_USING_THE_USBAUDIO_DRIVER"></span>


The following figure shows how the [USBAudio class system driver](kernel-mode-wdm-audio-components.md#usbaudio_class_system_driver) is configured to render and capture audio content. In this figure, the USBAudio driver sprouts pins to represent the terminals on the USB Audio device. Audio components such as KMixer, WDMAud, and DirectSound connect to these pins to render output streams or capture input streams.

![diagram illustrating rendering and capturing audio content using the usbaudio driver](images/usbaud.png)

See the following for a description of the Microsoft Windows Driver Model (WDM) audio components:

[DirectSound System Component](user-mode-wdm-audio-components.md#directsound_system_component)

[WDMAud System Driver](user-mode-wdm-audio-components.md#wdmaud_system_driver)

[SBEmul System Driver](kernel-mode-wdm-audio-components.md#sbemul_system_driver)

[KMixer System Driver](kernel-mode-wdm-audio-components.md#kmixer_system_driver)

[Redbook System Driver](kernel-mode-wdm-audio-components.md#redbook_system_driver)

[Splitter System Driver](kernel-mode-wdm-audio-components.md#splitter_system_driver)

[SWMidi System Driver](kernel-mode-wdm-audio-components.md#swmidi_system_driver)

[DMusic System Driver](kernel-mode-wdm-audio-components.md#dmusic_system_driver)

See the following for more detail about the filter graphs located above the USBAudio driver:

[Rendering and Capturing Wave Content](rendering-and-capturing-wave-content.md)

[Rendering and Capturing MIDI Content](rendering-and-capturing-midi-content.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Rendering%20and%20Capturing%20Audio%20Content%20by%20Using%20the%20USBAudio%20Driver%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


