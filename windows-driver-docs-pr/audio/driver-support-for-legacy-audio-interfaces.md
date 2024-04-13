---
title: Driver Support for Legacy Audio Interfaces
description: Driver Support for Legacy Audio Interfaces
keywords:
- WDM audio drivers WDK , legacy interfaces
- audio drivers WDK , legacy interfaces
- legacy audio interfaces WDK audio
- interfaces WDK audio
- audio miniport drivers WDK , legacy interfaces
- miniport drivers WDK audio , legacy interfaces
- Windows multimedia support WDK audio
- multimedia WDK audio
- miniport interfaces WDK audio
ms.date: 04/20/2017
---

# Driver Support for Legacy Audio Interfaces

The WDM audio system provides driver support for application programs that access audio devices through the legacy Windows multimedia functions. These functions include the following audio-specific APIs:

- aux

- mixer

- midiIn

- midiOut

- waveIn

- waveOut

For information about these APIs, see the Microsoft Windows SDK documentation. For a description of the system components that provide driver support for legacy audio functions, see [WDM Audio Components](wdm-audio-components.md).

This section discusses features that audio miniport drivers can implement to better support the audio capabilities that the Windows multimedia functions expose to application programs. These capabilities include wave-stream capture and rendering, MIDI recording and synthesis, and mixer control. In addition, this section describes several extensions to the legacy audio-specific APIs that applications can use to retrieve driver-specific information about audio devices.

This section discusses the following topics:

[Kernel Streaming Topology to Audio Mixer API Translation](kernel-streaming-topology-to-audio-mixer-api-translation.md)

[WDM Audio Extensions to Legacy Windows Multimedia APIs](wdm-audio-extensions-to-legacy-windows-multimedia-apis.md)
