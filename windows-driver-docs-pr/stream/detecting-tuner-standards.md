---
title: Detecting Tuner Standards
description: Detecting Tuner Standards
ms.assetid: 02923d8f-d8a2-427d-8957-2ffb0273b84a
keywords:
- formats WDK video capture
- TV signal formats WDK video capture
- KSPROPERTY_TUNER_STANDARD_MODE
- detecting tuner standards WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Detecting Tuner Standards


**This section applies only to operating systems starting with Microsoft Windows Vista.**

A TV application might have difficulty retrieving the actual format of the TV signal from electronic program guide (EPG) information or channel tables. A video capture minidriver should support the [**KSPROPERTY\_TUNER\_STANDARD\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff565909) property to allow a TV application to more accurately detect the format of the TV signal. KSPROPERTY\_TUNER\_STANDARD\_MODE indicates to applications whether the minidriver can identify the tuner standard from the TV signal itself. If the minidriver supports standard detection, the KSPROPERTY\_TUNER\_STANDARD\_MODE property can set the tuning device to automatically detect the tuner standard from the signal. After automatic-detect mode is set, the tuning device itself can process any requests to the [**KSPROPERTY\_TUNER\_STANDARD**](https://msdn.microsoft.com/library/windows/hardware/ff565907) property.

A video capture minidriver that supports the KSPROPERTY\_TUNER\_STANDARD\_MODE property must be capable of automatically detecting all the analog standards that the tuning device supports. However, the digital standards are currently optional.

For analog signals, the audio standards (PAL\_B / PAL\_G - NICAM / BTSC) are the most difficult to detect. However, if suitable logic is embedded in the minidriver, the minidriver will be able to automatically detect these audio standards too.

 

 




