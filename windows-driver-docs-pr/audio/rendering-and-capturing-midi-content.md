---
title: Rendering and Capturing MIDI Content
description: Rendering and Capturing MIDI Content
keywords:
- MIDI content rendering WDK audio
- MIDI content capturing WDK audio
ms.date: 04/20/2017
---

# Rendering and Capturing MIDI Content


## <span id="rendering_and_capturing_midi_content"></span><span id="RENDERING_AND_CAPTURING_MIDI_CONTENT"></span>


The following diagram shows the relationship between the system-supplied Microsoft Windows Driver Model (WDM) audio components that support rendering and capturing MIDI content.

:::image type="content" source="images/midi.png" alt-text="Diagram showing the relationship between system-supplied WDM audio components for rendering and capturing MIDI content.":::

See the following for a description of the Microsoft Windows Driver Model (WDM) audio components:

[DirectMusic System Component](user-mode-wdm-audio-components.md#directmusic_system_component)

[WDMAud System Driver](user-mode-wdm-audio-components.md#wdmaud_system_driver)

[SBEmul System Driver](kernel-mode-wdm-audio-components.md#sbemul_system_driver)

[SysAudio System Driver](kernel-mode-wdm-audio-components.md#sysaudio_system_driver)

[KMixer System Driver](kernel-mode-wdm-audio-components.md#kmixer_system_driver)

[SWMidi System Driver](kernel-mode-wdm-audio-components.md#swmidi_system_driver)

[DMusic System Driver](kernel-mode-wdm-audio-components.md#dmusic_system_driver)

[Port Class Adapter Driver and PortCls System Driver](kernel-mode-wdm-audio-components.md#port_class_adapter_driver_and_portcls_system_driver)

[USBAudio Class System Driver](kernel-mode-wdm-audio-components.md#usbaudio_class_system_driver)

See the following for more information about the configuration of the port class adapter driver and the USBAudio driver:

[Rendering and Capturing Audio Content by Using a Port Class Audio Adapter](rendering-and-capturing-audio-content-by-using-a-port-class-audio-adap.md)

[Rendering and Capturing Audio Content by Using the USBAudio Driver](rendering-and-capturing-audio-content-by-using-the-usbaudio-driver.md)

 

 




