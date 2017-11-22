---
title: DRM Functions
description: DRM Functions
ms.assetid: 7be96ab4-3c27-4e63-b0dd-71d814d804d7
---

# DRM Functions


## <span id="ddk_drm_functions_ks"></span><span id="DDK_DRM_FUNCTIONS_KS"></span>


This section describes the DRM functions, which drivers use to manage the digital rights of kernel-streaming audio content in Windows Me, and Microsoft Windows XP and later. System driver component Drmk.sys contains the entry points for these functions. The definitions for these functions appear in header file drmk.h. For more information, see [Digital Rights Management](https://msdn.microsoft.com/library/windows/hardware/ff536260).

This section describes the following DRM functions:

[**DrmAddContentHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff536347)

[**DrmCreateContentMixed**](https://msdn.microsoft.com/library/windows/hardware/ff536348)

[**DrmDestroyContent**](https://msdn.microsoft.com/library/windows/hardware/ff536349)

[**DrmForwardContentToDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff536351)

[**DrmForwardContentToFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff536352)

[**DrmForwardContentToInterface**](https://msdn.microsoft.com/library/windows/hardware/ff536353)

[**DrmGetContentRights**](https://msdn.microsoft.com/library/windows/hardware/ff536354)

In addition, this section describes the following macro:

[**DEFINE\_DRMRIGHTS\_DEFAULT**](https://msdn.microsoft.com/library/windows/hardware/ff536254)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20DRM%20Functions%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




