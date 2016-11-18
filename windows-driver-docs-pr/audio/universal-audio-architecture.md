---
title: Universal Audio Architecture
description: The Microsoft Universal Audio Architecture (UAA) enables audio devices that comply with the architecture to rely entirely on the operating system for driver support.
ms.assetid: a42eff33-7952-4004-903d-9b202d1864b9
keywords: ["UAA WDK", "Universal Audio Architecture WDK", "audio devices WDK UAA", "PCI audio adapters WDK", "USB WDK audio", "IEEE 1394 WDK audio", "Intel High Definition Audio Specification", "WDM audio drivers WDK , Universal Audio Architecture", "audio drivers WDK , Universal Audio Architecture", "1394 WDK audio"]
---

# Universal Audio Architecture


The Microsoft Universal Audio Architecture (UAA) enables audio devices that comply with the architecture to rely entirely on the operating system for driver support.

To be UAA-compatible, a PCI audio adapter must conform to the Intel High Definition Audio specification, which is the successor to the Intel Audio Codec '97 (AC'97) specification. Unlike AC'97, Intel High Definition Audio (Intel HD Audio) standardizes the bus controller, in addition to the codec devices and the serial interface link (the link that connects the controller to the codecs). The UAA design guidelines for Intel HD Audio devices contain additional requirements that are not part of the Intel High Definition Audio specification. Windows Vista provides complete driver support for UAA-compliant PCI audio adapters.

To be UAA-compatible, a USB audio device must conform to both the USB audio specification and the UAA design guidelines for USB audio devices. USB audio devices can make use of the [USBAudio class system driver](kernel-mode-wdm-audio-components.md#usbaudio_class_system_driver) (Usbaudio.sys), which is supplied as part of Windows. By definition, a USB audio device that is compatible with the USBAudio class system driver in Windows is UAA-compliant.

To be UAA-compatible, an IEEE 1394 AV/C audio device must conform to both the relevant IEEE 1394 specifications and the UAA design guidelines for IEEE 1394 AV/C audio devices. IEEE 1394 audio devices can make use of the [AVCAudio class system driver](kernel-mode-wdm-audio-components.md#avcaudio_class_system_driver) (Avcaudio.sys), which is supplied as part of Windows.

For more information about the Microsoft UAA initiative, see the white paper titled *Universal Audio Architecture* on the [audio technology](http://go.microsoft.com/fwlink/p/?linkid=8751) page on the WHDC website. For more information about Intel HD Audio, see the [Intel HD Audio](http://go.microsoft.com/fwlink/p/?linkid=42508) website. For a list of related specifications for USB and IEEE 1394 audio devices, see [USBAudio Class System Driver](kernel-mode-wdm-audio-components.md#usbaudio_class_system_driver) and [AVCAudio Class System Driver](kernel-mode-wdm-audio-components.md#avcaudio_class_system_driver).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Universal%20Audio%20Architecture%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


