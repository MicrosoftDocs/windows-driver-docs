---
title: Creating Driver-Side Surface Structures
description: Creating Driver-Side Surface Structures
ms.assetid: d5e2e6ee-8853-4a17-b1c6-48c75474b2b7
keywords:
- context WDK Direct3D , driver-side surface structures
- driver-side surface structures WDK Direct3D
- D3dCreateSurfaceEx
- surfaces WDK DirectDraw , driver-side structures
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Creating Driver-Side Surface Structures


## <span id="ddk_creating_driver_side_surface_structures_gg"></span><span id="DDK_CREATING_DRIVER_SIDE_SURFACE_STRUCTURES_GG"></span>


The DirectDraw runtime calls the driver's [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) entry point after it has called the [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) entry point and allocated memory for the surface. The runtime calls *D3dCreateSurfaceEx* only for those surfaces tagged with DDSCAPS\_TEXTURE, DDSCAPS\_EXECUTEBUFFER, DDSCAPS\_3DDEVICE, or DDSCAPS\_ZBUFFER flags.

Before calling [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840), the runtime assigns an integer value as a handle to the surface. This value is stored in the **dwSurfaceHandle** member of the DDRAWI\_DDSURFACE\_MORE structure (as pointed to by the **lpSurfMore** member of the DDRAWI\_DDSURFACE\_LCL structure). See [**DD\_SURFACE\_MORE**](https://msdn.microsoft.com/library/windows/hardware/ff551737) and [**DD\_SURFACE\_LOCAL**](https://msdn.microsoft.com/library/windows/hardware/ff551733), which are aliases for the DDRAWI\_DDSURFACE\_MORE and DDRAWI\_DDSURFACE\_LCL structures.

These integer values start at one and are kept as small as possible. (Zero is a guaranteed invalid value for a surface handle.) The intention is that a driver can keep an array of pointers into its own structures. As soon as it receives a handle (when *D3dCreateSurfaceEx* is called) that is beyond the end of the array, it can reallocate the array and continue. The Direct3D runtime passes no handle value to the driver before that handle is shown to the driver via *D3dCreateSurfaceEx*. However, the driver should be robust enough to handle values that are out-of-range, or that refer to a slot in the handle table that has been freed (that is a handle for which [*DdDestroySurface*](https://msdn.microsoft.com/library/windows/hardware/ff549281) has been called). Note that since zero is a guaranteed invalid value, the zero entry in the handle table can be reused for other purposes. The *Perm3* sample driver uses the zero entry to store the current length of the array.

**Note**   The Microsoft Windows Driver Kit (WDK) does not contain the 3Dlabs Permedia3 sample display driver (*Perm3.h*). You can get this sample driver from the Windows Server 2003 SP1 Driver Development Kit (DDK), which you can download from the [DDK - Windows Driver Development Kit](http://go.microsoft.com/fwlink/p/?linkid=21859) page of the WDHC website.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Creating%20Driver-Side%20Surface%20Structures%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




