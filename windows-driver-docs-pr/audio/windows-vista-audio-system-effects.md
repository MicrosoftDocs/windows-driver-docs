---
title: Windows Vista Audio System Effects
description: This section describes the different technologies that are used to provide digital audio system effects on legacy Microsoft Windows operating systems.
ms.assetid: 773E7B58-F1B8-474C-992F-4060F9D88D4E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows Vista Audio System Effects


This section describes the different technologies that are used to provide digital audio system effects on legacy Microsoft Windows operating systems.

The 32-bit versions of Windows Server 2003 and Windows XP provide support for global effects (GFX) filters, while Windows Vista uses system effects audio processing objects (APOs) to filter audio streams.

GFX filters are packaged as minidrivers and can apply an audio signal transform to the final audio mix that is rendered by an audio device. The effect is global because it affects all of the streams that are combined to create the final mix.

Conversely, sAPOs are not minidrivers and are not part of the audio driver. APOs are COM-based and are real-time, in-process objects that can be customized.

This section includes the following topics:.

[System Effects Audio Processing Objects](system-effects-audio-processing-objects.md)

 

 




