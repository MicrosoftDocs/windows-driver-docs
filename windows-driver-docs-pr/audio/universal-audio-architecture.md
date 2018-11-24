---
title: Universal Audio Architecture
description: The Microsoft Universal Audio Architecture (UAA) enables audio devices that comply with the architecture to rely entirely on the operating system for driver support.
ms.assetid: a42eff33-7952-4004-903d-9b202d1864b9
keywords:
- UAA WDK
- Universal Audio Architecture WDK
- audio devices WDK UAA
- PCI audio adapters WDK
- USB WDK audio
- IEEE 1394 WDK audio
- Intel High Definition Audio Specification
- WDM audio drivers WDK , Universal Audio Architecture
- audio drivers WDK , Universal Audio Architecture
- 1394 WDK audio
ms.date: 05/08/2018
ms.localizationpriority: medium
---

# Universal Audio Architecture


The Microsoft Universal Audio Architecture (UAA) enables audio devices that comply with the architecture to rely entirely on the operating system for driver support.

To be UAA-compatible, a PCI audio adapter must conform to the Intel High Definition Audio specification, which is the successor to the Intel Audio Codec '97 (AC'97) specification. Unlike AC'97, Intel High Definition Audio (Intel HD Audio) standardizes the bus controller, in addition to the codec devices and the serial interface link (the link that connects the controller to the codecs). The UAA design guidelines for Intel HD Audio devices contain additional requirements that are not part of the Intel High Definition Audio specification. Windows Vista provides complete driver support for UAA-compliant PCI audio adapters.

To be UAA-compatible, a USB audio device must conform to both the USB audio specification and the UAA design guidelines for USB audio devices. USB audio devices can make use of the [USBAudio class system driver](kernel-mode-wdm-audio-components.md#usbaudio_class_system_driver) (Usbaudio.sys), which is supplied as part of Windows. By definition, a USB audio device that is compatible with the USBAudio class system driver in Windows is UAA-compliant.

To be UAA-compatible, an IEEE 1394 AV/C audio device must conform to both the relevant IEEE 1394 specifications and the UAA design guidelines for IEEE 1394 AV/C audio devices. IEEE 1394 audio devices can make use of the [AVCAudio class system driver](kernel-mode-wdm-audio-components.md#avcaudio_class_system_driver) (Avcaudio.sys), which is supplied as part of Windows.

For more information about the Microsoft UAA initiative, see the [Universal Audio Architecture](https://download.microsoft.com/download/9/c/5/9c5b2167-8017-4bae-9fde-d599bac8184a/UAA_Guidelines.doc) white paper. For more information about Intel HD Audio, see the [Intel HD Audio](https://go.microsoft.com/fwlink/p/?linkid=42508) website. For a list of related specifications for USB and IEEE 1394 audio devices, see [USBAudio Class System Driver](kernel-mode-wdm-audio-components.md#usbaudio_class_system_driver) and [AVCAudio Class System Driver](kernel-mode-wdm-audio-components.md#avcaudio_class_system_driver).

 

 




