---
title: DRM Requirements for GFX Drivers
description: DRM Requirements for GFX Drivers
ms.assetid: 9ab9a38a-319e-4c9c-a0e4-e258be94e673
keywords:
- digital rights management WDK GFX filters
- GFX filters WDK audio , DRM requirements
- DRM WDK GFX filters
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# DRM Requirements for GFX Drivers


## <span id="drm_requirements_for_gfx_drivers"></span><span id="DRM_REQUIREMENTS_FOR_GFX_DRIVERS"></span>


The operating system requires that a GFX driver meets the same requirements for handling DRM-protected content as any other driver in the WDM audio system. In order to support [Digital Rights Management](digital-rights-management.md) (DRM), the GFX/AVStream filter implements a property handler for [**KSPROPERTY\_DRMAUDIOSTREAM\_CONTENTID**](https://msdn.microsoft.com/library/windows/hardware/ff537351). This handler calls [**DrmForwardContentToDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff536351) to advise the [DRMK system driver](kernel-mode-wdm-audio-components.md#drmk_system_driver) of the connected downstream pin that receives the content. The GFX/AVStream filter calls [**KsPinGetConnectedPinFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff563508) and [**KsPinGetConnectedPinDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff563507) to retrieve the FILE\_OBJECT and DEVICE\_OBJECT parameters to pass to **DrmForwardContentToDeviceObject**.

 

 




