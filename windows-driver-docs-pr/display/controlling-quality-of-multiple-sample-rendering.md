---
title: Controlling Quality of Multiple-Sample Rendering
description: Controlling Quality of Multiple-Sample Rendering
ms.assetid: 5a2f2d36-ab0d-4267-a921-c42621fa5d47
keywords: ["multiple-sample rendering WDK DirectX 9.0 , controlling quality", "rendering multisamples WDK DirectX 9.0 , controlling quality"]
---

# Controlling Quality of Multiple-Sample Rendering


## <span id="ddk_controlling_quality_of_multiple_sample_rendering_gg"></span><span id="DDK_CONTROLLING_QUALITY_OF_MULTIPLE_SAMPLE_RENDERING_GG"></span>


Before an application can request to create a surface with a specific multisampling technique, it should call the **IDirect3D9::CheckDeviceMultiSampleType** method to verify if the display device supports that technique. The runtime in turn sends a **GetDriverInfo2** request using the **D3DGDI2\_TYPE\_GETMULTISAMPLEQUALITYLEVELS** value to retrieve the number of quality levels for the particular multisample type and surface format associated with the technique. For more information about **GetDriverInfo2**, see [Supporting GetDriverInfo2](supporting-getdriverinfo2.md).

Whether the display device supports maskable multisampling (more than one sample for a multiple-sample render-target format plus antialias support) or just nonmaskable multisampling (only antialias support), the driver for the device must provide the number of quality levels for the D3DMULTISAMPLE\_NONMASKABLE multiple-sample type. Applications that just use multisampling for antialiasing purposes are then only required to query for the number of nonmaskable multiple-sample quality levels that the driver supports.

Besides verifying whether the display device supports the multisampling technique, **IDirect3D9::CheckDeviceMultiSampleType** also returns the number of quality levels associated with the technique.

When the application requests to create a surface, it uses a combination of surface format, multisample type, and number of quality levels whose support was previously verified. This ensures that the surface is created successfully. The runtime calls the driver's [*DdCanCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549213), [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263), or [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) function to create the surface. In this call, the runtime encodes the number of samples for the multiple-sampled surface into five bits (the DDSCAPS3\_MULTISAMPLE\_MASK mask) and the number of multiple-sample quality levels into three bits (the DDSCAPS3\_MULTISAMPLE\_QUALITY\_MASK mask) of the **dwCaps3** member of the [**DDSCAPS2**](https://msdn.microsoft.com/library/windows/hardware/ff550292) structure for the surface.

For more information about **IDirect3D9::CheckDeviceMultiSampleType**, see the latest DirectX SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Controlling%20Quality%20of%20Multiple-Sample%20Rendering%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




