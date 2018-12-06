---
title: Custom Audio Drivers
description: Custom Audio Drivers
ms.assetid: d5f19a72-0b43-4fe1-b0e1-0198344b4d19
keywords:
- WDM audio drivers WDK , custom
- audio drivers WDK , custom
- custom audio drivers WDK
- vendor-supplied drivers WDK audio
- PortCls WDK audio , custom audio drivers
ms.date: 05/08/2018
ms.localizationpriority: medium
---

# Custom Audio Drivers


Audio devices that are not UAA-compatible require vendor-supplied custom drivers. In addition, a UAA-compatible audio adapter can incorporate proprietary features that are not supported by the UAA class drivers; these features are accessible to applications only if the vendor provides a custom audio driver. Only the standard UAA features are accessible through the system-supplied UAA drivers. For information about UAA-supported features, see the [Universal Audio Architecture](https://download.microsoft.com/download/9/c/5/9c5b2167-8017-4bae-9fde-d599bac8184a/UAA_Guidelines.doc) white paper.

Two options are available to hardware vendors for writing custom audio drivers: developing a custom audio-adapter driver for use with the PortCls system driver (Portcls.sys), or developing a custom minidriver for use with the AVStream class system driver (Ks.sys).

Most custom drivers for audio adapters use PortCls, which is supplied as part of the operating system. The PortCls system driver (Portcls.sys) contains a built-in audio-driver infrastructure that makes the task of writing a custom audio driver easier. PortCls implements several port drivers, each of which is specialized to manage the generic functions of a particular type of wave, MIDI, or mixer device. After selecting an appropriate set of port drivers to manage the audio functions on the audio adapter, the vendor develops a complementary set of miniport drivers that work in conjunction with the selected port drivers and control the hardware-dependent features of the audio devices.

The vendor can also support an audio device by developing a custom AVStream class minidriver. The minidriver works in conjunction with the AVStream class system driver, which is supplied as part of the operating system. Implementing an AVStream driver is more difficult than using PortCls, but doing so might still be appropriate for devices that integrate audio and video. An AVStream driver might also be necessary for an existing USB or IEEE 1394 audio device that fails to comply with the requirements of the system-supplied USBAudio or AVCAudio class system driver.

For nearly all PCI audio adapters that require vendor-supplied custom drivers, vendors should choose PortCls.

The AVStream class system driver (Ks.sys) lacks most of the audio-specific support functions that exist in PortCls.

For more information about PortCls, see [Introduction to Port Class](introduction-to-port-class.md). For more information about AVStream, see [AVStream Overview](https://msdn.microsoft.com/library/windows/hardware/ff554240).

 

 




