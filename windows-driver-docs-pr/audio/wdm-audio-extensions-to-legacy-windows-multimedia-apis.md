---
title: WDM Audio Extensions to Legacy Windows Multimedia APIs
description: WDM Audio Extensions to Legacy Windows Multimedia APIs
ms.assetid: a1009b7f-3720-454f-a128-ae148f781edc
keywords:
- WDM audio extensions WDK
- extended audio capabilities WDK audio
- WDM audio drivers WDK , extensions
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDM Audio Extensions to Legacy Windows Multimedia APIs


## <span id="wdm_audio_extensions_to_legacy_windows_multimedia_apis"></span><span id="WDM_AUDIO_EXTENSIONS_TO_LEGACY_WINDOWS_MULTIMEDIA_APIS"></span>


Recent versions of Windows have extended the audio functions in the Windows multimedia APIs aux, midiIn, midiOut, mixer, waveIn, and waveOut to output information about the status and capabilities of WDM audio drivers.

The [**auxGetDevCaps**](https://msdn.microsoft.com/library/windows/desktop/dd756712), [**midiInGetDevCaps**](https://msdn.microsoft.com/library/windows/desktop/dd798453), [**midiOutGetDevCaps**](https://msdn.microsoft.com/library/windows/desktop/dd798469), [**mixerGetDevCaps**](https://msdn.microsoft.com/library/windows/desktop/dd757300), [**waveInGetDevCaps**](https://msdn.microsoft.com/library/windows/desktop/dd743841), and [**waveOutGetDevCaps**](https://msdn.microsoft.com/library/windows/desktop/dd743857) functions can retrieve driver-specific information that uniquely identifies an audio device.

The Windows multimedia functions [**waveInMessage**](https://msdn.microsoft.com/library/windows/desktop/dd743846), [**waveOutMessage**](https://msdn.microsoft.com/library/windows/desktop/dd743865), [**midiInMessage**](https://msdn.microsoft.com/library/windows/desktop/dd798457), [**midiOutMessage**](https://msdn.microsoft.com/library/windows/desktop/dd798475), and [**mixerMessage**](https://msdn.microsoft.com/library/windows/desktop/dd757307) can retrieve the device interface name of a wave, MIDI, or mixer device. In addition, the **waveOutMessage**, **midiOutMessage**, and **waveInMessage** functions can retrieve the device IDs of the preferred audio devices for wave I/O, MIDI, and voice communications, respectively.

The following topics are discussed in this section:

[Extended Capabilities from a WDM Audio Driver](extended-capabilities-from-a-wdm-audio-driver.md)

[System-Intercepted Device Messages](system-intercepted-device-messages.md)

[Accessing the Preferred Device ID](accessing-the-preferred-device-id.md)

[Preferred Voice-Communications Device ID](preferred-voice-communications-device-id.md)

[Obtaining a Device Interface Name](obtaining-a-device-interface-name.md)

[Music Technology GUIDs](music-technology-guids.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20WDM%20Audio%20Extensions%20to%20Legacy%20Windows%20Multimedia%20APIs%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


