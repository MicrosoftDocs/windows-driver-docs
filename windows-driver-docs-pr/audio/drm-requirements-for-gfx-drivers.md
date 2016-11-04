---
title: DRM Requirements for GFX Drivers
description: DRM Requirements for GFX Drivers
ms.assetid: 9ab9a38a-319e-4c9c-a0e4-e258be94e673
keywords: ["digital rights management WDK GFX filters", "GFX filters WDK audio , DRM requirements", "DRM WDK GFX filters"]
---

# DRM Requirements for GFX Drivers


## <span id="drm_requirements_for_gfx_drivers"></span><span id="DRM_REQUIREMENTS_FOR_GFX_DRIVERS"></span>


The operating system requires that a GFX driver meets the same requirements for handling DRM-protected content as any other driver in the WDM audio system. In order to support [Digital Rights Management](digital-rights-management.md) (DRM), the GFX/AVStream filter implements a property handler for [**KSPROPERTY\_DRMAUDIOSTREAM\_CONTENTID**](https://msdn.microsoft.com/library/windows/hardware/ff537351). This handler calls [**DrmForwardContentToDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff536351) to advise the [DRMK system driver](kernel-mode-wdm-audio-components.md#drmk_system_driver) of the connected downstream pin that receives the content. The GFX/AVStream filter calls [**KsPinGetConnectedPinFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff563508) and [**KsPinGetConnectedPinDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff563507) to retrieve the FILE\_OBJECT and DEVICE\_OBJECT parameters to pass to **DrmForwardContentToDeviceObject**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20DRM%20Requirements%20for%20GFX%20Drivers%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


