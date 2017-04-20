---
title: Driver-Managed Resources
description: Driver-Managed Resources
ms.assetid: f68b622a-247a-4a89-8d4c-c6a306b7fb3e
keywords:
- texture management WDK Direct3D , driver-managed resources
- driver-managed resources WDK Direct3D
- manageable resources WDK Direct3D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Driver-Managed Resources


## <span id="ddk_driver_managed_resources_gg"></span><span id="DDK_DRIVER_MANAGED_RESOURCES_GG"></span>


In addition to supporting texture management as described in [Driver-Managed Textures](driver-managed-textures.md), a DirectX 8.1 driver can also manage resources in general, such as textures, volume textures, cube-map textures, vertex buffers, and index buffers.

The driver supports driver-managed resources by setting the **dwCaps2** member of the [**DDCORECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549248) structure to the DDCAPS2\_CANMANAGERESOURCE bit. The driver specifies this DDCORECAPS structure in the **ddCaps** member of a [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure. DD\_HALINFO is returned by [**DrvGetDirectDrawInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556229) in response to the initialization of the DirectDraw component of the driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Driver-Managed%20Resources%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




