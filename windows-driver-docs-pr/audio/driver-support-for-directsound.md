---
title: Driver Support for DirectSound
description: Driver Support for DirectSound
ms.assetid: a32a2a01-4ecd-485f-8293-402a0bcc8336
keywords: ["WDM audio drivers WDK , DirectSound", "audio drivers WDK , DirectSound", "DirectSound WDK audio", "DirectSound WDK audio , about DirectSound", "miniport drivers WDK audio , DirectSound"]
---

# Driver Support for DirectSound


## <span id="driver_support_for_directsound"></span><span id="DRIVER_SUPPORT_FOR_DIRECTSOUND"></span>


The WDM audio system provides driver support for application programs that access audio devices through the Microsoft DirectSound API. For a description of the system components that provide DirectSound driver support, see [WDM Audio Components](wdm-audio-components.md).

The following section discusses the features that audio miniport drivers can implement to better support the audio capabilities that the DirectSound API exposes to application programs. These capabilities include hardware acceleration of 2D and 3D sound effects, support for a variety of speaker configurations, and capture effects such as acoustic echo cancellation for full-duplex telephone conferencing.

This section presents the following topics:

[DirectSound Hardware Acceleration in WDM Audio](directsound-hardware-acceleration-in-wdm-audio.md)

[DirectSound Speaker-Configuration Settings](directsound-speaker-configuration-settings.md)

[DirectSound Capture Effects](directsound-capture-effects.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Driver%20Support%20for%20DirectSound%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


