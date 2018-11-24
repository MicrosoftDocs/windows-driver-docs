---
title: Requesting and Using Surface Memory
description: Requesting and Using Surface Memory
ms.assetid: 7913acc6-ff30-4f2a-8389-37a79940ae8b
keywords:
- surface memory WDK display
- listing surfaces WDK display
- resource object surface memory WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Requesting and Using Surface Memory


## <span id="ddk_requesting_and_using_surface_memory_gg"></span><span id="DDK_REQUESTING_AND_USING_SURFACE_MEMORY_GG"></span>


The user-mode display driver receives calls to its [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) function when the Microsoft Direct3D runtime requires the creation of a list of surfaces. The Direct3D runtime specifies a resource handle to the list of surfaces that the user-mode display driver uses to call back into the runtime. The user-mode display driver creates a resource object to represent the list of surfaces, generates a unique handle to this object, and returns the handle back to the Direct3D runtime. The runtime uses this unique handle in subsequent driver calls to identify the list of surfaces. The runtime identifies a particular surface by specifying the index of the surface in the array contained in the **pSurfList** member of the [**D3DDDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542963) structure.

Because the user-mode display driver receives the driver-defined resource handle in calls that refer to the resource, the driver is not required to perform a costly handle lookup in order to locate the driver-defined resource object. Likewise, so that the runtime is also not required to perform a handle lookup, the user-mode display driver uses the Direct3D runtime-defined resource handle when the user-mode display driver calls back into the runtime.

The user-mode display driver calls the [**pfnAllocateCb**](https://msdn.microsoft.com/library/windows/hardware/ff568893) function to allocate memory for the surfaces. In the **pfnAllocateCb** call, the user-mode display driver can pass private data for the list of surfaces and for each individual surface in the **pPrivateDriverData** members of the [**D3DDDICB\_ALLOCATE**](https://msdn.microsoft.com/library/windows/hardware/ff544137) and [**D3DDDI\_ALLOCATIONINFO**](https://msdn.microsoft.com/library/windows/hardware/ff544364) structures, respectively. However, the user-mode display driver cannot receive private data from the **pPrivateDriverData** members. The user-mode display driver can allocate memory for this private data and can free the memory after the **pfnAllocateCb** call returns, or can use stack memory to pass this private data. The **pfnAllocateCb** function returns to the user-mode display driver a handle to each allocation for each allocated surface.

**Note**   The user-mode display driver must call the **pfnAllocateCb** function once for each shared surface for each device. For example, if device 1 creates a shared surface that is also used by devices 2, 3, and 4, then devices 2, 3, and 4 must also call **pfnAllocateCb** once for the shared surface in order to retrieve the allocation handle.

 

The user-mode display driver must track each surface to each allocation handle, typically, by maintaining a surface-to-allocation handle table. The user-mode display driver should store each allocation handle within the driver-defined resource object.

When the Direct3D runtime performs an operation on a previously allocated surface (for example, in a call to the user-mode display driver's [**Blt**](https://msdn.microsoft.com/library/windows/hardware/ff538251) function), the user-mode display driver receives the handle to the resource, possibly with a surface index. The user-mode display driver uses this resource handle to retrieve the driver-defined resource object. The driver obtains the allocation handles that are stored in the resource object and assembles them in the command buffer. The user-mode display driver uses the allocation handles that correspond to the surfaces when calling the [**pfnRenderCb**](https://msdn.microsoft.com/library/windows/hardware/ff568923) function to submit a command buffer to the display miniport driver. The display miniport driver can call the [**DxgkCbGetHandleData**](https://msdn.microsoft.com/library/windows/hardware/ff559515) function to determine to which surface allocations the user-mode display driver refers.

 

 





