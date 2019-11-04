---
title: DRM Functions
description: DRM Functions
ms.assetid: 7be96ab4-3c27-4e63-b0dd-71d814d804d7
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# DRM Functions


## <span id="ddk_drm_functions_ks"></span><span id="DDK_DRM_FUNCTIONS_KS"></span>


This section describes the DRM functions, which drivers use to manage the digital rights of kernel-streaming audio content in Windows. System driver component Drmk.sys contains the entry points for these functions. The definitions for these functions appear in header file drmk.h. For more information, see [Digital Rights Management](https://docs.microsoft.com/windows-hardware/drivers/audio/digital-rights-management).

This section describes the following DRM functions:

[**DrmAddContentHandlers**](https://docs.microsoft.com/windows-hardware/drivers/ddi/drmk/nf-drmk-drmaddcontenthandlers)

[**DrmCreateContentMixed**](https://docs.microsoft.com/windows-hardware/drivers/ddi/drmk/nf-drmk-drmcreatecontentmixed)

[**DrmDestroyContent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/drmk/nf-drmk-drmdestroycontent)

[**DrmForwardContentToDeviceObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/drmk/nf-drmk-drmforwardcontenttodeviceobject)

[**DrmForwardContentToFileObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/drmk/nf-drmk-drmforwardcontenttofileobject)

[**DrmForwardContentToInterface**](https://docs.microsoft.com/windows-hardware/drivers/ddi/drmk/nf-drmk-drmforwardcontenttointerface)

[**DrmGetContentRights**](https://docs.microsoft.com/windows-hardware/drivers/ddi/drmk/nf-drmk-drmgetcontentrights)

In addition, this section describes the following macro:

[**DEFINE\_DRMRIGHTS\_DEFAULT**](https://docs.microsoft.com/previous-versions/ff536254(v=vs.85))

 

 





