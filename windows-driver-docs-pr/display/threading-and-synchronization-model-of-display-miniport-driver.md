---
title: Threading and Synchronization Model of Display Miniport Driver
description: Threading and Synchronization Model of Display Miniport Driver
ms.assetid: 4e5cf498-a2d1-44d5-b7a3-427f48b5da50
keywords: ["threading WDK display , miniport drivers", "synchronization WDK display , miniport drivers", "miniport drivers WDK display , synchronization", "miniport drivers WDK display , threading"]
---

# Threading and Synchronization Model of Display Miniport Driver


## <span id="ddk_thread_model_of_video_miniport_driver_gg"></span><span id="DDK_THREAD_MODEL_OF_VIDEO_MINIPORT_DRIVER_GG"></span>


Multiple threads can be present within the display miniport driver at the same time. That is, in general, the display miniport driver is reentrant. However, some calls into the display miniport driver should not be reentrant because they either access graphics hardware or access global cross-thread data structures. Although reentrancy or nonreentrancy cannot be selected at a per-call level, the Windows Display Driver Model (WDDM) pre-assigns, per call, the following synchronization levels that define precisely what the driver should expect for the call:

-   [Threading and Synchronization Third Level](threading-and-synchronization-third-level.md)

-   [Threading and Synchronization Second Level](threading-and-synchronization-second-level.md)

-   [Threading and Synchronization First Level](threading-and-synchronization-first-level.md)

-   [Threading and Synchronization Zero Level](threading-and-synchronization-zero-level.md)

-   [Thread Synchronization and TDR](thread-synchronization-and-tdr.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Threading%20and%20Synchronization%20Model%20of%20Display%20Miniport%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




