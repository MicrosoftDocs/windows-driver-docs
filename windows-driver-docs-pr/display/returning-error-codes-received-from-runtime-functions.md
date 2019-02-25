---
title: Returning Error Codes Received from Runtime Functions
description: Returning Error Codes Received from Runtime Functions
ms.assetid: 4a2384e8-407f-4248-8b31-7c4e836b15dc
keywords:
- user-mode display drivers WDK Windows Vista , runtime function error codes
- runtime function error codes WDK display
- error codes WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Returning Error Codes Received from Runtime Functions


Calls to the [Direct3D version 9 user-mode display driver-supplied functions](https://msdn.microsoft.com/library/windows/hardware/ff552927) must return error codes that they receive when they call the [Direct3D runtime-supplied kernel-services accessing functions](https://msdn.microsoft.com/library/windows/hardware/ff552870). For example, the runtime might call a user-mode display driver function, such as the [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) function. This, in turn, calls a runtime-supplied function, such as the [**pfnAllocateCb**](https://msdn.microsoft.com/library/windows/hardware/ff568893) function, to perform a specific operation, in this case to allocate memory for the resource. If the user-mode display driver receives an error code from the call to the runtime-supplied function, it must return that error code back to the runtime.

**Note**   There is one exception to the rule that a driver must pass a runtime error code back to the runtime. When the driver calls the [**pfnAllocateCb**](https://msdn.microsoft.com/library/windows/hardware/ff568893) runtime-supplied function, to allocate video memory for optional resources when the video memory is already allocated, the rule does not apply. If **pfnAllocateCb** fails to allocate this video memory for optional resources that are only required to optimize performance, the driver should not report the out-of-memory error (E\_OUTOFMEMORY) back to the runtime.

 

 

 





