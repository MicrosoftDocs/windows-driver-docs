---
title: WDM Audio Extensions to Legacy Windows Multimedia APIs
description: WDM Audio Extensions to Legacy Windows Multimedia APIs
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

The [**auxGetDevCaps**](/previous-versions/dd756712(v=vs.85)), [**midiInGetDevCaps**](/previous-versions/dd798453(v=vs.85)), [**midiOutGetDevCaps**](/previous-versions/dd798469(v=vs.85)), [**mixerGetDevCaps**](/previous-versions/dd757300(v=vs.85)), [**waveInGetDevCaps**](/previous-versions/dd743841(v=vs.85)), and [**waveOutGetDevCaps**](/previous-versions/dd743857(v=vs.85)) functions can retrieve driver-specific information that uniquely identifies an audio device.

The Windows multimedia functions [**waveInMessage**](/previous-versions/dd743846(v=vs.85)), [**waveOutMessage**](/previous-versions/dd743865(v=vs.85)), [**midiInMessage**](/previous-versions/dd798457(v=vs.85)), [**midiOutMessage**](/previous-versions/dd798475(v=vs.85)), and [**mixerMessage**](/previous-versions/dd757307(v=vs.85)) can retrieve the device interface name of a wave, MIDI, or mixer device. In addition, the **waveOutMessage**, **midiOutMessage**, and **waveInMessage** functions can retrieve the device IDs of the preferred audio devices for wave I/O, MIDI, and voice communications, respectively.

The following topics are discussed in this section:

[Extended Capabilities from a WDM Audio Driver](extended-capabilities-from-a-wdm-audio-driver.md)

[System-Intercepted Device Messages](system-intercepted-device-messages.md)

[Accessing the Preferred Device ID](accessing-the-preferred-device-id.md)

[Preferred Voice-Communications Device ID](preferred-voice-communications-device-id.md)

[Obtaining a Device Interface Name](obtaining-a-device-interface-name.md)

[Music Technology GUIDs](music-technology-guids.md)

 

