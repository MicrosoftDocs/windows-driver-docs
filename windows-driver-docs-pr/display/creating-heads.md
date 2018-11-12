---
title: Creating Heads
description: Creating Heads
ms.assetid: 0b6d4aa0-e3c9-45df-998d-d6dfca5ab720
keywords:
- heads WDK DirectX 9.0
- multiple-head hardware WDK DirectX 9.0 , creating heads
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Heads


## <span id="ddk_creating_heads_gg"></span><span id="DDK_CREATING_HEADS_GG"></span>


The Microsoft DirectX 9.0 driver creates one Microsoft Direct3D context for each multiple-head card and a Microsoft DirectDraw object for each head on each multiple-head card. Therefore, the creation process for the multiple-head card has a per-head part and a cross-head part. The per-head part corresponds roughly to DirectDraw DDI calls, the cross-head part to Direct3D DDI calls.

The point of connection across the various heads is the Direct3D handle that is created by the driver's [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) function. The driver assigns a unique Direct3D handle to each surface across all heads in the group. The Direct3D context on the master head manages all these handles and can target any render target that is created on any head, most notably the back buffers in the flipping chains on the subordinate heads. The **D3dCreateSurfaceEx** function for each subordinate head must be able to update the handle lookup table that is managed by the master head. Subsequently, these handles are only used in calls to the driver's [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function for the master head.

The driver only creates textures and other resources on the master head.

The driver creates and works with heads as described in the following sequence:

1.  For each head, the following operations are performed to set up the display mode and primary-flipping surfaces:
    -   The runtime sets the display mode.
    -   The runtime creates the DirectDraw object.
    -   The runtime creates a primary flipping chain and possibly a Z buffer. The runtime specifies the **DDSCAPS2\_ADDITIONALPRIMARY** (0x80000000) capability bit in the **dwCaps2** member of the [**DDSCAPS2**](https://msdn.microsoft.com/library/windows/hardware/ff550292) structure for each surface (including the Z buffer) to indicate an additional primary surface for a multiple-head card. The runtime calls the driver's [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) function.
    -   The runtime calls the driver's [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) function, first for the master and in the order defined by **AdapterOrdinalInGroup** for the subordinates. In this call, the Direct3D handle that the runtime passes is guaranteed to be unique across all the heads in the group. The driver can insert a reference into a subordinate head's handle lookup table. However, because a Direct3D context is not created on subordinate heads, no [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) commands are issued to any subordinate heads. Therefore, inserting this reference is not necessary.
    -   After the runtime calls [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) for all heads (including the master), a further [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) call is made for each subordinate head's flipping chain on the master head's DirectDraw object. The driver makes an entry in the master head's handle lookup table for each front, back, and depth/stencil buffer for each subordinate head.

2.  The runtime calls the driver's [*D3dContextCreate*](https://msdn.microsoft.com/library/windows/hardware/ff542178) function only for the DirectDraw object on the master head. This is the only context that is used while the application runs.

3.  When the application requests to create textures and resources, the runtime call the driver's [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) and [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) functions through the master head.

4.  When the application makes rendering calls, the runtime calls the driver's [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function on the master head using the appropriate operation codes.

    When the application performs other operations, the following calls are routed to master and subordinate heads:

    -   As described in step one, [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) calls are made to supply the driver with handles for each subordinate head's flipping chain. These handles are typically used with the **D3DDP2OP\_SETRENDERTARGET** operation code token when the application renders a frame into the back buffer of one of the subordinate head's swap chains.
    -   The runtime calls the driver's [*DdFlip*](https://msdn.microsoft.com/library/windows/hardware/ff549306) function on each head (master and subordinates) to present back buffers to primary surfaces for those heads. This call never presents a back buffer from one head to another head's primary surface. The flipping chains on each head are completely independent.
    -   The runtime might call the driver's [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) function to copy the back buffer to the front buffer for any head. This call never copies a back buffer from one head to another head's front buffer.
    -   The runtime can call the driver's [*DdGetScanLine*](https://msdn.microsoft.com/library/windows/hardware/ff549497) function on any head because this call relates to the state of the monitor and not the Direct3D context.
    -   The runtime can call the driver's [*DdLock*](https://msdn.microsoft.com/library/windows/hardware/ff549599) function on any head's back buffer.

    The application can either allocate a Z buffer with each head or allocate one Z buffer to use with each head sequentially. In the former case, the runtime calls the driver's [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) function on each head (master and subordinates) as described in step one. In the latter case, the runtime calls the driver's *DdCreateSurface* function only on the master head. In either case, the runtime calls the driver's [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) function to supply handles to all Z buffers that are unique across all heads in the group.

 

 





