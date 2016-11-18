---
title: Developing and Debugging DRM Drivers
description: Developing and Debugging DRM Drivers
ms.assetid: 3450717a-fd27-4bea-8740-9d47b420ed32
keywords: ["Digital Rights Management WDK audio , recommendations", "DRM WDK audio , recommendations", "Digital Rights Management WDK audio , debugging", "DRM WDK audio , debugging", "debugging drivers WDK DRM"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Developing%20and%20Debugging%20DRM%20Drivers%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


