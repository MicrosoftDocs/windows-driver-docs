---
title: Handling Resource Creation and Destruction
description: Handling Resource Creation and Destruction
ms.assetid: d443bdc3-1c5a-4372-9e6a-b8a4d21499b9
keywords:
- resource creation WDK display
- resource destruction WDK display
- destroying resources WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling Resource Creation and Destruction


To enable the Microsoft DirectX graphics kernel subsystem to properly track resource lifetime and to prevent memory leaks in the operating system, the user-mode display driver must properly create and destroy resources.

The Microsoft Direct3D runtime calls the following user-mode display driver functions to create user-mode resources.

-   [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) creates a new shared or unshared resource.

-   [**OpenResource**](https://msdn.microsoft.com/library/windows/hardware/ff568611) opens a view to an existing shared resource.

In both calls, the Direct3D runtime passes a unique *user-mode runtime resource handle* that the user-mode display driver uses to call back into the runtime. When *CreateResource* or *OpenResource* returns successfully, the user-mode display driver returns a unique user-mode handle that represents the resource. This handle is the *user-mode driver resource handle*. The runtime uses the user-mode driver resource handle in subsequent driver calls.

A one-to-one correspondence exists between the user-mode runtime resource handle and the user-mode driver resource handle. The Direct3D runtime and the user-mode display driver exchange the user-mode runtime and driver resource handles through the **hResource** members of the [**D3DDDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542963) and [**D3DDDIARG\_OPENRESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff543232) structures.

When the user-mode display driver calls the Direct3D runtime's [**pfnAllocateCb**](https://msdn.microsoft.com/library/windows/hardware/ff568893) function to create allocations for a user-mode resource, the driver should specify the user-mode runtime resource handle in the **hResource** member of the [**D3DDDICB\_ALLOCATE**](https://msdn.microsoft.com/library/windows/hardware/ff544137) structure that the *pData* parameter points to. The Direct3D runtime generates a unique kernel-mode handle to the resource and passes it back to the user-mode display driver in the **hKMResource** member of D3DDDICB\_ALLOCATE. The user-mode display driver can insert the kernel-mode resource handle in the command stream for the display miniport driver to use later.

**Note**   Although user-mode resource handles are always unique for each user-mode resource creation, kernel-mode resource handles are not always unique. When the Direct3D runtime calls the user-mode display driver's [**OpenResource**](https://msdn.microsoft.com/library/windows/hardware/ff568611) function to open a view to an existing shared resource, the runtime passes the resource's kernel-mode handle in the **hKMResource** member of the [**D3DDDIARG\_OPENRESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff543232) structure that the *pResource* parameter points to. The runtime previously created this kernel-mode handle after the runtime called the user-mode display driver's [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) function.

 

To destroy a user-mode resource that *CreateResource* or *OpenResource* created, the Direct3D runtime passes the user-mode driver resource handle in the *hResource* parameter in a call to the user-mode display driver's [**DestroyResource**](https://msdn.microsoft.com/library/windows/hardware/ff552795) function. To release the kernel-mode resource handle and all of the allocations that are associated with the user-mode resource, the user-mode display driver passes the user-mode runtime resource handle in the **hResource** member of the [**D3DDDICB\_DEALLOCATE**](https://msdn.microsoft.com/library/windows/hardware/ff544161) structure that the *pData* parameter points to in a call to the [*pfnDeallocateCb*](https://msdn.microsoft.com/library/windows/hardware/ff568898) function.

Consider the following items when a user-mode display driver creates and destroys resources:

-   For allocations that the user-mode display driver creates in response to shared resources (that is, in response to [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) calls with the **SharedResource** bit-field flag set in the **Flags** member of [**D3DDDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542963)), the driver must assign a non-**NULL** value to the **hResource** member of [**D3DDDICB\_ALLOCATE**](https://msdn.microsoft.com/library/windows/hardware/ff544137).

-   For allocations that the user-mode display driver creates in response to non-shared resources, the driver is not required to assign a non-**NULL** value to the **hResource** member of D3DDDICB\_ALLOCATE. If the driver assigns **NULL** to **hResource**, the allocations are associated with the device and not a particular resource (and kernel-mode resource handle). However, if allocations are truly related to a resource, the driver should associate the allocations with that resource.
    **Note**   A kernel-mode resource handle is created only if the user-mode display driver sets the **hResource** member of D3DDDICB\_ALLOCATE to the user-mode runtime resource handle that the driver received from the **hResource** member of the [**D3DDDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542963) structure in a call to [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688).

     

-   When [**DestroyResource**](https://msdn.microsoft.com/library/windows/hardware/ff552795) is called to destroy a non-shared user-mode resource, the user-mode display driver can call [*pfnDeallocateCb*](https://msdn.microsoft.com/library/windows/hardware/ff568898) with the **hResource** member of [**D3DDDICB\_DEALLOCATE**](https://msdn.microsoft.com/library/windows/hardware/ff544161) set to **NULL** only if the driver never associated any allocations with the resource. If the user-mode display driver associated allocations with the resource, the driver must call **pfnDeallocateCb** with the **hResource** member of D3DDDICB\_DEALLOCATE set to a non-**NULL** value; otherwise, a memory leak will occur.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Handling%20Resource%20Creation%20and%20Destruction%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




