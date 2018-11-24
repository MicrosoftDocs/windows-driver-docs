---
title: Developing and Debugging DRM Drivers
description: Developing and Debugging DRM Drivers
ms.assetid: 3450717a-fd27-4bea-8740-9d47b420ed32
keywords:
- Digital Rights Management WDK audio , recommendations
- DRM WDK audio , recommendations
- Digital Rights Management WDK audio , debugging
- DRM WDK audio , debugging
- debugging drivers WDK DRM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Developing and Debugging DRM Drivers


## <span id="developing_and_debugging_drm_drivers"></span><span id="DEVELOPING_AND_DEBUGGING_DRM_DRIVERS"></span>


The following checklist may help driver writers avoid some common pitfalls:

-   If the driver disables wave-out capture and S/PDIF output while DRM-protected content plays, the driver should remember to enable them again after the DRM-protected content finishes playing (and the DRM buffer is destroyed).

-   If the device performs hardware mixing, the driver should keep track of any changes in composite usage rights that occur when streams are added to or removed from the mix. Any time the mix includes one or more copy-protected DRM streams, for example, capture should be muted. It should remain muted if capture is turned on while the protected mix is playing.

-   After a change to the filter graph or to the property settings that are associated with a stream, the driver might need to immediately update the stream's copy-protection and output-enable settings. The driver should synchronize its operation to prevent protected content from being copied to a capture buffer or digital output. For example, when the input stream to a capture multiplexer changes, the driver should not allow secure content to become vulnerable during the time required to turn muting on and off.

The [DRMK system driver](kernel-mode-wdm-audio-components.md#drmk_system_driver) prevents the kernel debugger from connecting while DRM-protected content is playing. Anti-debugging armor is one of several measures that DRMK uses to make protected content opaque. Once your driver is ready to be tested, however, you can debug its DRM-compliant features by using the following technique:

-   Temporarily modify the wave stream's **SetState** method (for example, see [**IMiniportWavePciStream::SetState**](https://msdn.microsoft.com/library/windows/hardware/ff536733)) to call [**IDrmAudioStream::SetContentId**](https://msdn.microsoft.com/library/windows/hardware/ff536570) and set the [**DRMRIGHTS**](https://msdn.microsoft.com/library/windows/hardware/ff536355) parameter's **CopyProtect** member to **TRUE**.

-   After you finish debugging, remember to remove the **SetContentId** call.

With this technique, you can play unprotected content as though it were DRM-protected content but avoid disabling the debugger.

For example, you can use the debugger to verify that your driver prevents the content from being recorded. Try to trick the driver into enabling recording of the wave-out stream through the capture MUX by changing the SndVol32 program's volume and mute settings. The sliders should reflect the changes you make to their settings, which are persistent, but the capture MUX should continue to mute the wave-out stream until the "protected" content finishes playing. Only then should the new settings take effect.

 

 




