---
title: Returning Error Codes Received from Runtime Functions
description: Returning Error Codes Received from Runtime Functions
ms.assetid: 4a2384e8-407f-4248-8b31-7c4e836b15dc
keywords:
- user-mode display drivers WDK Windows Vista , runtime function error codes
- runtime function error codes WDK display
- error codes WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Returning Error Codes Received from Runtime Functions


Calls to the [Direct3D version 9 user-mode display driver-supplied functions](https://msdn.microsoft.com/library/windows/hardware/ff552927) must return error codes that they receive when they call the [Direct3D runtime-supplied kernel-services accessing functions](https://msdn.microsoft.com/library/windows/hardware/ff552870). For example, the runtime might call a user-mode display driver function, such as the [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) function. This, in turn, calls a runtime-supplied function, such as the [**pfnAllocateCb**](https://msdn.microsoft.com/library/windows/hardware/ff568893) function, to perform a specific operation, in this case to allocate memory for the resource. If the user-mode display driver receives an error code from the call to the runtime-supplied function, it must return that error code back to the runtime.

**Note**   There is one exception to the rule that a driver must pass a runtime error code back to the runtime. When the driver calls the [**pfnAllocateCb**](https://msdn.microsoft.com/library/windows/hardware/ff568893) runtime-supplied function, to allocate video memory for optional resources when the video memory is already allocated, the rule does not apply. If **pfnAllocateCb** fails to allocate this video memory for optional resources that are only required to optimize performance, the driver should not report the out-of-memory error (E\_OUTOFMEMORY) back to the runtime.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Returning%20Error%20Codes%20Received%20from%20Runtime%20Functions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




