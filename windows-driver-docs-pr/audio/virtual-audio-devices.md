---
title: Virtual Audio Devices
description: Virtual audio devices represent the filter graphs that render and capture audio content. The system audio driver (SysAudio) uses the available hardware and software components to determine the filter graphs to build.
ms.assetid: 0f8ddd2d-f852-4b35-8a18-16416081d3c0
keywords:
- virtual audio devices WDK
- SysAudio
- system audio devices WDK
- audio virtual devices WDK
- audio filter graphs WDK
- filter graphs WDK audio , virtual audio devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Virtual Audio Devices


Virtual audio devices represent the filter graphs that render and capture audio content. The system audio driver (SysAudio) uses the available hardware and software components to determine the filter graphs to build.

For more information about the system audio driver, see [SysAudio System Driver](kernel-mode-wdm-audio-components.md#sysaudio_system_driver).

## <span id="virtual_audio_devices"></span><span id="VIRTUAL_AUDIO_DEVICES"></span>


SysAudio's clients include DirectSound and the [WDMAud system driver](user-mode-wdm-audio-components.md#wdmaud_system_driver), which serves as the interface between WDM audio drivers and the audio-specific Microsoft Windows Multimedia APIs waveIn, waveOut, midiIn, midiOut, mixer, and aux (described in Microsoft Windows SDK documentation).

The [KsStudio utility](ksstudio-utility.md) in the Windows Driver Kit (WDK) is an example of an application that bypasses SysAudio and allows users to construct filter graphs manually.

Following PnP device enumeration, SysAudio takes stock of the registered audio hardware and software components in order to determine how to construct the various audio filter graphs that its clients might require.

After determining the list of filter graphs that it can build from the available hardware and software components, SysAudio registers these graphs as virtual audio devices for playback, recording, MIDI input/output, and mixing. SysAudio reserves the registry category KSCATEGORY\_AUDIO\_DEVICE exclusively for its virtual audio devices. Adapter drivers should not register themselves in this category.

A SysAudio client can treat a filter factory for a virtual audio device similarly to a filter factory for a hardware or software component. When asked by a client to instantiate a particular pin on a virtual device, SysAudio constructs the graph automatically and manages the graph's internal pin connections transparently to the client. This allows the client to treat a filter graph as a single filter, thereby avoiding complexities of graph management such as inter-filter communication.

 

 




