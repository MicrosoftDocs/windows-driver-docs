---
title: Driver Support for DirectSound
description: Driver Support for DirectSound
ms.assetid: a32a2a01-4ecd-485f-8293-402a0bcc8336
keywords:
- WDM audio drivers WDK , DirectSound
- audio drivers WDK , DirectSound
- DirectSound WDK audio
- DirectSound WDK audio , about DirectSound
- miniport drivers WDK audio , DirectSound
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Support for DirectSound


## <span id="driver_support_for_directsound"></span><span id="DRIVER_SUPPORT_FOR_DIRECTSOUND"></span>


The WDM audio system provides driver support for application programs that access audio devices through the Microsoft DirectSound API. For a description of the system components that provide DirectSound driver support, see [WDM Audio Components](wdm-audio-components.md).

The following section discusses the features that audio miniport drivers can implement to better support the audio capabilities that the DirectSound API exposes to application programs. These capabilities include hardware acceleration of 2D and 3D sound effects, support for a variety of speaker configurations, and capture effects such as acoustic echo cancellation for full-duplex telephone conferencing.

This section presents the following topics:

[DirectSound Hardware Acceleration in WDM Audio](directsound-hardware-acceleration-in-wdm-audio.md)

[DirectSound Speaker-Configuration Settings](directsound-speaker-configuration-settings.md)

[DirectSound Capture Effects](directsound-capture-effects.md)

 

 




