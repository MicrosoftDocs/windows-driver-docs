---
title: Full-Screen-Mode Behavior
description: Full-Screen-Mode Behavior
ms.assetid: 43e7fec0-4e4d-401c-80c7-3e0710313214
keywords:
- full-screen rotation WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Full-Screen-Mode Behavior


A user-mode display driver can determine that a rendering device is in full-screen mode:

-   If the **Fullscreen** bit-field flag is set in the **Flags** member of the [**D3DDDIARG\_OPENRESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff543232) structure that the *pResource* parameter points to in a call to the driver's [**OpenResource**](https://msdn.microsoft.com/library/windows/hardware/ff568611) function.

-   If the **Primary** bit-field flag is set in the **Flags** member of the [**D3DDDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542963) structure that the *pResource* parameter points to in a call to the driver's [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) function.

An application that is developed for Microsoft DirectX 9.0 or earlier will cause the Microsoft Direct3D runtime to call *OpenResource* to open the shared primary surface and then *CreateResource* to create any additional back buffers. A Microsoft DirectX 9L application will cause the Direct3D runtime to call *CreateResource* (without calling *OpenResource*) to create all swap-chain buffers. The Direct3D runtime specifies the primary surface orientation in the **Rotation** member of the [**D3DDDIARG\_OPENRESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff543232) and [**D3DDDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542963) structures that the *pResource* parameter points to in calls to both the [**OpenResource**](https://msdn.microsoft.com/library/windows/hardware/ff568611) and the [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) functions, respectively.

For a full-screen device, a user-mode display driver must lock a rotated resource, render to a rotated resource, and perform bit-block transfers (bitblt) from a rotated resource. Typically, the user-mode display driver creates interim render targets in the rotated orientation (all locks, bitblts, and renderings will go to these interim render targets) and primary allocations in the landscape orientation (that is, the orientation that the digital-to-analog converter \[DAC\] uses to scan out). When the user-mode display driver is called to flip the data, it performs a rotating bitblt from the interim render target to the landscape buffer before it calls the [**pfnPresentCb**](https://msdn.microsoft.com/library/windows/hardware/ff568916) function to issue the flip command.

Whenever a user-mode display driver must perform a bitblt that involves a rotated resource and a non-rotated resource, the Direct3D runtime specifies the **Rotate** bit-field flag in the **Flags** member of the [**D3DDDIARG\_BLT**](https://msdn.microsoft.com/library/windows/hardware/ff542884) structure in a call to the driver's [**Blt**](https://msdn.microsoft.com/library/windows/hardware/ff538251) function to indicate to the driver that the proper rotation must occur for the bitblt.

DirectX 9L applications can be rotation-aware, which means that they will render everything in the proper orientation and will properly handle locks to a rotated buffer. When the Direct3D runtime creates a swap chain for a rotation-aware application, the runtime always specifies the rotation as D3DDDI\_ROTATION\_IDENTITY in the **Rotation** member of the [**D3DDDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542963) structure because the user-mode display driver is not required to perform any special actions for the rotation-aware application to work.

 

 





