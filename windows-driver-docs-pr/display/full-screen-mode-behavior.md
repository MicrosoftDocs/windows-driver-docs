---
title: Full-Screen-Mode Behavior
description: Full-Screen-Mode Behavior
keywords:
- full-screen rotation WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Full-Screen-Mode Behavior


A user-mode display driver can determine that a rendering device is in full-screen mode:

-   If the **Fullscreen** bit-field flag is set in the **Flags** member of the [**D3DDDIARG\_OPENRESOURCE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_openresource) structure that the *pResource* parameter points to in a call to the driver's [**OpenResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_openresource) function.

-   If the **Primary** bit-field flag is set in the **Flags** member of the [**D3DDDIARG\_CREATERESOURCE**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddiarg_createresource) structure that the *pResource* parameter points to in a call to the driver's [**CreateResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createresource) function.

An application that is developed for Microsoft DirectX 9.0 or earlier will cause the Microsoft Direct3D runtime to call *OpenResource* to open the shared primary surface and then *CreateResource* to create any additional back buffers. A Microsoft DirectX 9L application will cause the Direct3D runtime to call *CreateResource* (without calling *OpenResource*) to create all swap-chain buffers. The Direct3D runtime specifies the primary surface orientation in the **Rotation** member of the [**D3DDDIARG\_OPENRESOURCE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_openresource) and [**D3DDDIARG\_CREATERESOURCE**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddiarg_createresource) structures that the *pResource* parameter points to in calls to both the [**OpenResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_openresource) and the [**CreateResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createresource) functions, respectively.

For a full-screen device, a user-mode display driver must lock a rotated resource, render to a rotated resource, and perform bit-block transfers (bitblt) from a rotated resource. Typically, the user-mode display driver creates interim render targets in the rotated orientation (all locks, bitblts, and renderings will go to these interim render targets) and primary allocations in the landscape orientation (that is, the orientation that the digital-to-analog converter \[DAC\] uses to scan out). When the user-mode display driver is called to flip the data, it performs a rotating bitblt from the interim render target to the landscape buffer before it calls the [**pfnPresentCb**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_presentcb) function to issue the flip command.

Whenever a user-mode display driver must perform a bitblt that involves a rotated resource and a non-rotated resource, the Direct3D runtime specifies the **Rotate** bit-field flag in the **Flags** member of the [**D3DDDIARG\_BLT**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_blt) structure in a call to the driver's [**Blt**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_blt) function to indicate to the driver that the proper rotation must occur for the bitblt.

DirectX 9L applications can be rotation-aware, which means that they will render everything in the proper orientation and will properly handle locks to a rotated buffer. When the Direct3D runtime creates a swap chain for a rotation-aware application, the runtime always specifies the rotation as D3DDDI\_ROTATION\_IDENTITY in the **Rotation** member of the [**D3DDDIARG\_CREATERESOURCE**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddiarg_createresource) structure because the user-mode display driver is not required to perform any special actions for the rotation-aware application to work.

 

