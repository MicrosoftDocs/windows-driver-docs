---
title: Audio System Effects
description: Audio System Effects
ms.assetid: 4cbb3efb-fcfe-475b-8e15-b5c6a6b0fa1e
keywords:
- sAPO WDK
- LFX WDK
- GFX WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Audio System Effects


This section describes the different technologies that are used to provide digital audio system effects on Microsoft Windows operating systems.

The 32-bit versions of Windows Server 2003 and Windows XP provide support for global effects (GFX) filters, while Windows Vista uses system effects audio processing objects (sAPOs) to filter audio streams.

GFX filters are packaged as minidrivers and can apply an audio signal transform to the final audio mix that is rendered by an audio device. The effect is global because it affects all of the streams that are combined to create the final mix.

Conversely, sAPOs are not minidrivers and are not part of the audio driver. sAPOs are COM-based and are real-time, in-process objects that can be customized.

This section includes the following topics:.

[System Effects Audio Processing Objects](system-effects-audio-processing-objects.md)

 

 




