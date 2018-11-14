---
title: DRM Functions
description: DRM Functions
ms.assetid: 7be96ab4-3c27-4e63-b0dd-71d814d804d7
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





