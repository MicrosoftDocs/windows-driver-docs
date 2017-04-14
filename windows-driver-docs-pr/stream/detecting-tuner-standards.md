---
title: Detecting Tuner Standards
author: windows-driver-content
description: Detecting Tuner Standards
ms.assetid: 02923d8f-d8a2-427d-8957-2ffb0273b84a
keywords: ["formats WDK video capture", "TV signal formats WDK video capture", "KSPROPERTY_TUNER_STANDARD_MODE", "detecting tuner standards WDK video capture"]
---

# Detecting Tuner Standards


**This section applies only to operating systems starting with Microsoft Windows Vista.**

A TV application might have difficulty retrieving the actual format of the TV signal from electronic program guide (EPG) information or channel tables. A video capture minidriver should support the [**KSPROPERTY\_TUNER\_STANDARD\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff565909) property to allow a TV application to more accurately detect the format of the TV signal. KSPROPERTY\_TUNER\_STANDARD\_MODE indicates to applications whether the minidriver can identify the tuner standard from the TV signal itself. If the minidriver supports standard detection, the KSPROPERTY\_TUNER\_STANDARD\_MODE property can set the tuning device to automatically detect the tuner standard from the signal. After automatic-detect mode is set, the tuning device itself can process any requests to the [**KSPROPERTY\_TUNER\_STANDARD**](https://msdn.microsoft.com/library/windows/hardware/ff565907) property.

A video capture minidriver that supports the KSPROPERTY\_TUNER\_STANDARD\_MODE property must be capable of automatically detecting all the analog standards that the tuning device supports. However, the digital standards are currently optional.

For analog signals, the audio standards (PAL\_B / PAL\_G - NICAM / BTSC) are the most difficult to detect. However, if suitable logic is embedded in the minidriver, the minidriver will be able to automatically detect these audio standards too.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Detecting%20Tuner%20Standards%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


