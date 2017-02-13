---
title: D3dCreateSurfaceEx Handles
description: D3dCreateSurfaceEx Handles
ms.assetid: ada78f89-422b-470d-9423-09968ae113e8
keywords: ["context WDK Direct3D , D3dCreateSurfaceEx", "D3dCreateSurfaceEx"]
---

# D3dCreateSurfaceEx Handles


## <span id="ddk_d3dcreatesurfaceex_handles_gg"></span><span id="DDK_D3DCREATESURFACEEX_HANDLES_GG"></span>


Certain situations can cause [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) to be called for an invalid, destroyed surface. Drivers can robustly handle this case by simply ignoring any **D3dCreateSurfaceEx** call for a video memory surface that has an **fpVidMem** (a member of the [**DD\_SURFACE\_GLOBAL**](https://msdn.microsoft.com/library/windows/hardware/ff551726) structure) of zero. However, a driver can get a **D3dCreateSurfaceEx** call with a system memory surface that has an **fpVidMem** value of zero, which means that the system memory surface is in the process of being destroyed. The driver should then free any existing driver-side data related to this surface.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20D3dCreateSurfaceEx%20Handles%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




