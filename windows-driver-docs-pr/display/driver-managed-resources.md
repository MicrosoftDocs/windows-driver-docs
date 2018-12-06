---
title: Driver-Managed Resources
description: Driver-Managed Resources
ms.assetid: f68b622a-247a-4a89-8d4c-c6a306b7fb3e
keywords:
- texture management WDK Direct3D , driver-managed resources
- driver-managed resources WDK Direct3D
- manageable resources WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver-Managed Resources


## <span id="ddk_driver_managed_resources_gg"></span><span id="DDK_DRIVER_MANAGED_RESOURCES_GG"></span>


In addition to supporting texture management as described in [Driver-Managed Textures](driver-managed-textures.md), a DirectX 8.1 driver can also manage resources in general, such as textures, volume textures, cube-map textures, vertex buffers, and index buffers.

The driver supports driver-managed resources by setting the **dwCaps2** member of the [**DDCORECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549248) structure to the DDCAPS2\_CANMANAGERESOURCE bit. The driver specifies this DDCORECAPS structure in the **ddCaps** member of a [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure. DD\_HALINFO is returned by [**DrvGetDirectDrawInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556229) in response to the initialization of the DirectDraw component of the driver.

 

 





