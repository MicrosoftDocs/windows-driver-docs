---
title: Driver-Managed Textures
description: Driver-Managed Textures
ms.assetid: 7ec56b86-dc29-41c3-91f4-2a30e9116b61
keywords:
- texture management WDK Direct3D , driver-managed
- driver-managed textures WDK Direct3D
- manageable textures WDK Direct3D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Driver-Managed Textures


## <span id="ddk_driver_managed_textures_gg"></span><span id="DDK_DRIVER_MANAGED_TEXTURES_GG"></span>


The driver can manage textures that have been marked as manageable. These DirectDrawSurface objects are marked as manageable with the DDSCAPS2\_TEXTUREMANAGE flag in the **dwCaps2** member of the structure referred to by **lpSurfMore-&gt;ddCapsEx**. (**lpSurfMore** and **ddCapsEx** are members of the [**DD\_SURFACE\_LOCAL**](https://msdn.microsoft.com/library/windows/hardware/ff551733) and [**DD\_SURFACE\_MORE**](https://msdn.microsoft.com/library/windows/hardware/ff551737) structures, respectively.)

The driver supports driver-managed textures by setting the **dwCaps2** member of the [**DDCORECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549248) structure to the DDCAPS2\_CANMANAGETEXTURE bit. The driver specifies this DDCORECAPS structure in the **ddCaps** member of a [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure. DD\_HALINFO is returned by [**DrvGetDirectDrawInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556229) in response to the initialization of the DirectDraw component of the driver.

The driver can then create the necessary surfaces in video or nonlocal memory in a "lazy" fashion. That is, the driver leaves the textures in backing surfaces until it requires them, which is just before rasterizing a primitive that makes use of the texture.

Surfaces should be evicted primarily by their priority assignment. The driver responds to the D3DDP2OP\_SETPRIORITY operation code in the [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) command stream. This operation code sets the priority for a given surface. As a secondary measure, the driver should use a least-recently-used (LRU) scheme to evict surfaces. The driver uses this scheme whenever the priority of two or more textures is identical in a particular scenario. Logically, any surface that is in use should not be evicted at all.

If a driver supports managed surfaces, then the driver may receive a special [*DdDestroySurface*](https://msdn.microsoft.com/library/windows/hardware/ff549281) call for a managed surface in the case where video memory is lost, such as when a mode switch occurs. In this case the DRAWISURF\_INVALID flag is set and the driver simply evicts the video memory copy of this managed surface and keeps other structures intact. Otherwise, the driver performs a regular destroy surface call.

The driver should handle [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) and [*DdLock*](https://msdn.microsoft.com/library/windows/hardware/ff549599) calls appropriately when managing textures. This is because any change to the backing surface image must be propagated into the video memory copy of the surface before the texture is used again. The driver should determine if it is better to update just a portion of the surface or all of it. For example, if the driver's *DdLock* function is called to modify only a portion of a backing (system memory) image of the video memory copy of a surface, then when the driver's *DdBlt* function is called the driver can optimize the update by just blitting the necessary subsurface from system memory into video memory.

The driver is allowed to perform texture management in order to perform optimization transformations on the textures or to decide for itself where and when to transfer textures in memory.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Driver-Managed%20Textures%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




