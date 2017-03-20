---
title: Full-Screen-Mode Behavior
description: Full-Screen-Mode Behavior
ms.assetid: 43e7fec0-4e4d-401c-80c7-3e0710313214
keywords: ["full-screen rotation WDK display"]
---

# Full-Screen-Mode Behavior


A user-mode display driver can determine that a rendering device is in full-screen mode:

-   If the **Fullscreen** bit-field flag is set in the **Flags** member of the [**D3DDDIARG\_OPENRESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff543232) structure that the *pResource* parameter points to in a call to the driver's [**OpenResource**](https://msdn.microsoft.com/library/windows/hardware/ff568611) function.

-   If the **Primary** bit-field flag is set in the **Flags** member of the [**D3DDDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542963) structure that the *pResource* parameter points to in a call to the driver's [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) function.

An application that is developed for Microsoft DirectX 9.0 or earlier will cause the Microsoft Direct3D runtime to call *OpenResource* to open the shared primary surface and then *CreateResource* to create any additional back buffers. A Microsoft DirectX 9L application will cause the Direct3D runtime to call *CreateResource* (without calling *OpenResource*) to create all swap-chain buffers. The Direct3D runtime specifies the primary surface orientation in the **Rotation** member of the [**D3DDDIARG\_OPENRESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff543232) and [**D3DDDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542963) structures that the *pResource* parameter points to in calls to both the [**OpenResource**](https://msdn.microsoft.com/library/windows/hardware/ff568611) and the [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) functions, respectively.

For a full-screen device, a user-mode display driver must lock a rotated resource, render to a rotated resource, and perform bit-block transfers (bitblt) from a rotated resource. Typically, the user-mode display driver creates interim render targets in the rotated orientation (all locks, bitblts, and renderings will go to these interim render targets) and primary allocations in the landscape orientation (that is, the orientation that the digital-to-analog converter \[DAC\] uses to scan out). When the user-mode display driver is called to flip the data, it performs a rotating bitblt from the interim render target to the landscape buffer before it calls the [**pfnPresentCb**](https://msdn.microsoft.com/library/windows/hardware/ff568916) function to issue the flip command.

Whenever a user-mode display driver must perform a bitblt that involves a rotated resource and a non-rotated resource, the Direct3D runtime specifies the **Rotate** bit-field flag in the **Flags** member of the [**D3DDDIARG\_BLT**](https://msdn.microsoft.com/library/windows/hardware/ff542884) structure in a call to the driver's [**Blt**](https://msdn.microsoft.com/library/windows/hardware/ff538251) function to indicate to the driver that the proper rotation must occur for the bitblt.

DirectX 9L applications can be rotation-aware, which means that they will render everything in the proper orientation and will properly handle locks to a rotated buffer. When the Direct3D runtime creates a swap chain for a rotation-aware application, the runtime always specifies the rotation as D3DDDI\_ROTATION\_IDENTITY in the **Rotation** member of the [**D3DDDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542963) structure because the user-mode display driver is not required to perform any special actions for the rotation-aware application to work.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Full-Screen-Mode%20Behavior%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




