---
title: Presentation
description: Presentation
ms.assetid: 23a01b5b-0654-4c43-ac96-a75810fa20df
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , presentation
- presentation WDK DirectX 8.0
- rendering results visible WDK DirectX 8.0
- visible results WDK DirectX 8.0
- DDLT_PRESENTATION
- DDBLT_LAST_PRESENTATION
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Presentation


## <span id="ddk_presentation_gg"></span><span id="DDK_PRESENTATION_GG"></span>


DirectX 8.0 formalizes the concept of "presentation" (or making the results of rendering visible to the user) in the API. Previously, this was accomplished either by page flipping in full screen mode or by blitting in windowed mode. Applications use the new **Present** API to perform either full screen flipping or windowed mode blitting. However, this mechanism is not yet exposed at the DDI level. The runtime simply maps the **Present** API to either the [*DdFlip*](https://msdn.microsoft.com/library/windows/hardware/ff549306) or [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) DDI entry points depending on the application mode.

DirectX 8.0 has added two new DirectDraw blt flags that are passed to the driver as notification of when a blt operation is actually part of a **Present** and therefore marks a frame boundary. These new flags are DDBLT\_PRESENTATION and DDBLT\_LAST\_PRESENTATION. Two flags are necessary because clipping may result in a single **Present** call invoking multiple blt operations in the driver. In this case, all of the blts that are invoked as a result of the **Present** operation have the DDBLT\_PRESENTATION flag set. However, only the final blt of the sequence used to perform the **Present** has the DDBLT\_LAST\_PRESENTATION bit set. Therefore, if blt is used to implement a **Present** call, the driver sees zero or more blts with the DDBLT\_PRESENTATION bit set followed by exactly one blt with both the DDLT\_PRESENTATION and DDBLT\_LAST\_PRESENTATION bits set. These flags are never set by the application. Only the runtime is allowed to pass these flags to a blt. In addition, these flags are only passed to drivers supporting the DirectX 8.0 DDI.

The driver is only permitted to queue a maximum of three frames. If the driver sees a blt call with DDBLT\_PRESENTATION set and it already has three DDBLT\_LAST\_PRESENTATION blts queued it must fail the call with DDERR\_WASSTILLDRAWING. The runtime retries until the queue has drained sufficiently.

If the driver cannot effectively determine when a DDBLT\_LAST\_PRESENTATION blt in the queue has been retired, then the driver must not queue frames at all. DDBLT\_LAST\_PRESENTATION should cause such drivers to return DDERR\_WASSTILLDRAWING until the accelerator is completely finished, exactly as if the application had called **Lock** on the source surface before calling **Blt**.

Finally, in the case of multiple windowed applications running simultaneously, the driver should count presentation blts based on the source of each blt, rather than the primary, that is, the driver is allowed to queue three frames per window/render target. This results in better performance.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Presentation%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




