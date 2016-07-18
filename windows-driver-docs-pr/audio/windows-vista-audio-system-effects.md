---
title: Windows Vista Audio System Effects
description: This section describes the different technologies that are used to provide digital audio system effects on legacy Microsoft Windows operating systems.
ms.assetid: 773E7B58-F1B8-474C-992F-4060F9D88D4E
---

# Windows Vista Audio System Effects


This section describes the different technologies that are used to provide digital audio system effects on legacy Microsoft Windows operating systems.

The 32-bit versions of Windows Server 2003 and Windows XP provide support for global effects (GFX) filters, while Windows Vista uses system effects audio processing objects (APOs) to filter audio streams.

GFX filters are packaged as minidrivers and can apply an audio signal transform to the final audio mix that is rendered by an audio device. The effect is global because it affects all of the streams that are combined to create the final mix.

Conversely, sAPOs are not minidrivers and are not part of the audio driver. APOs are COM-based and are real-time, in-process objects that can be customized.

This section includes the following topics:.

[GFX Filters](gfx-filters.md)

[System Effects Audio Processing Objects](system-effects-audio-processing-objects.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Windows%20Vista%20Audio%20System%20Effects%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




