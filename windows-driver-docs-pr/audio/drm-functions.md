---
title: DRM Functions
description: DRM Functions
ms.date: 11/28/2017
---

# DRM Functions


## <span id="ddk_drm_functions_ks"></span><span id="DDK_DRM_FUNCTIONS_KS"></span>


This section describes the DRM functions, which drivers use to manage the digital rights of kernel-streaming audio content in Windows. System driver component Drmk.sys contains the entry points for these functions. The definitions for these functions appear in header file drmk.h. For more information, see [Digital Rights Management](./digital-rights-management.md).

This section describes the following DRM functions:

[**DrmAddContentHandlers**](/windows-hardware/drivers/ddi/drmk/nf-drmk-drmaddcontenthandlers)

[**DrmCreateContentMixed**](/windows-hardware/drivers/ddi/drmk/nf-drmk-drmcreatecontentmixed)

[**DrmDestroyContent**](/windows-hardware/drivers/ddi/drmk/nf-drmk-drmdestroycontent)

[**DrmForwardContentToDeviceObject**](/windows-hardware/drivers/ddi/drmk/nf-drmk-drmforwardcontenttodeviceobject)

[**DrmForwardContentToFileObject**](/windows-hardware/drivers/ddi/drmk/nf-drmk-drmforwardcontenttofileobject)

[**DrmForwardContentToInterface**](/windows-hardware/drivers/ddi/drmk/nf-drmk-drmforwardcontenttointerface)

[**DrmGetContentRights**](/windows-hardware/drivers/ddi/drmk/nf-drmk-drmgetcontentrights)

In addition, this section describes the following macro:

[**DEFINE\_DRMRIGHTS\_DEFAULT**](/previous-versions/ff536254(v=vs.85))

 

