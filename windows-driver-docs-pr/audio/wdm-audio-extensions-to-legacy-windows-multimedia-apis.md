---
title: WDM Audio Extensions to Legacy Windows Multimedia APIs
description: WDM Audio Extensions to Legacy Windows Multimedia APIs
ms.assetid: a1009b7f-3720-454f-a128-ae148f781edc
keywords:
- WDM audio extensions WDK
- extended audio capabilities WDK audio
- WDM audio drivers WDK , extensions
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




