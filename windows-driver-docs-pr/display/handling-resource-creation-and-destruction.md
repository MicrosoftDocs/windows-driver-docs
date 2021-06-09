---
title: Handling Resource Creation and Destruction
description: Handling Resource Creation and Destruction
keywords:
- resource creation WDK display
- resource destruction WDK display
- destroying resources WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Resource Creation and Destruction


To enable the Microsoft DirectX graphics kernel subsystem to properly track resource lifetime and to prevent memory leaks in the operating system, the user-mode display driver must properly create and destroy resources.

The Microsoft Direct3D runtime calls the following user-mode display driver functions to create user-mode resources.

-   [**CreateResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createresource) creates a new shared or unshared resource.

-   [**OpenResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_openresource) opens a view to an existing shared resource.

In both calls, the Direct3D runtime passes a unique *user-mode runtime resource handle* that the user-mode display driver uses to call back into the runtime. When *CreateResource* or *OpenResource* returns successfully, the user-mode display driver returns a unique user-mode handle that represents the resource. This handle is the *user-mode driver resource handle*. The runtime uses the user-mode driver resource handle in subsequent driver calls.

A one-to-one correspondence exists between the user-mode runtime resource handle and the user-mode driver resource handle. The Direct3D runtime and the user-mode display driver exchange the user-mode runtime and driver resource handles through the **hResource** members of the [**D3DDDIARG\_CREATERESOURCE**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddiarg_createresource) and [**D3DDDIARG\_OPENRESOURCE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_openresource) structures.

When the user-mode display driver calls the Direct3D runtime's [**pfnAllocateCb**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_allocatecb) function to create allocations for a user-mode resource, the driver should specify the user-mode runtime resource handle in the **hResource** member of the [**D3DDDICB\_ALLOCATE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddicb_allocate) structure that the *pData* parameter points to. The Direct3D runtime generates a unique kernel-mode handle to the resource and passes it back to the user-mode display driver in the **hKMResource** member of D3DDDICB\_ALLOCATE. The user-mode display driver can insert the kernel-mode resource handle in the command stream for the display miniport driver to use later.

**Note**   Although user-mode resource handles are always unique for each user-mode resource creation, kernel-mode resource handles are not always unique. When the Direct3D runtime calls the user-mode display driver's [**OpenResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_openresource) function to open a view to an existing shared resource, the runtime passes the resource's kernel-mode handle in the **hKMResource** member of the [**D3DDDIARG\_OPENRESOURCE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_openresource) structure that the *pResource* parameter points to. The runtime previously created this kernel-mode handle after the runtime called the user-mode display driver's [**CreateResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createresource) function.

 

To destroy a user-mode resource that *CreateResource* or *OpenResource* created, the Direct3D runtime passes the user-mode driver resource handle in the *hResource* parameter in a call to the user-mode display driver's [**DestroyResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_destroyresource) function. To release the kernel-mode resource handle and all of the allocations that are associated with the user-mode resource, the user-mode display driver passes the user-mode runtime resource handle in the **hResource** member of the [**D3DDDICB\_DEALLOCATE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddicb_deallocate) structure that the *pData* parameter points to in a call to the [*pfnDeallocateCb*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_deallocatecb) function.

Consider the following items when a user-mode display driver creates and destroys resources:

-   For allocations that the user-mode display driver creates in response to shared resources (that is, in response to [**CreateResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createresource) calls with the **SharedResource** bit-field flag set in the **Flags** member of [**D3DDDIARG\_CREATERESOURCE**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddiarg_createresource)), the driver must assign a non-**NULL** value to the **hResource** member of [**D3DDDICB\_ALLOCATE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddicb_allocate).

-   For allocations that the user-mode display driver creates in response to non-shared resources, the driver is not required to assign a non-**NULL** value to the **hResource** member of D3DDDICB\_ALLOCATE. If the driver assigns **NULL** to **hResource**, the allocations are associated with the device and not a particular resource (and kernel-mode resource handle). However, if allocations are truly related to a resource, the driver should associate the allocations with that resource.
    **Note**   A kernel-mode resource handle is created only if the user-mode display driver sets the **hResource** member of D3DDDICB\_ALLOCATE to the user-mode runtime resource handle that the driver received from the **hResource** member of the [**D3DDDIARG\_CREATERESOURCE**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddiarg_createresource) structure in a call to [**CreateResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createresource).

     

-   When [**DestroyResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_destroyresource) is called to destroy a non-shared user-mode resource, the user-mode display driver can call [*pfnDeallocateCb*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_deallocatecb) with the **hResource** member of [**D3DDDICB\_DEALLOCATE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddicb_deallocate) set to **NULL** only if the driver never associated any allocations with the resource. If the user-mode display driver associated allocations with the resource, the driver must call **pfnDeallocateCb** with the **hResource** member of D3DDDICB\_DEALLOCATE set to a non-**NULL** value; otherwise, a memory leak will occur.

 

