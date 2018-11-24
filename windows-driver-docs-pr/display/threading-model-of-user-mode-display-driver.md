---
title: Threading Model of User-Mode Display Driver
description: Threading Model of User-Mode Display Driver
ms.assetid: 43bb6032-5f34-434b-8404-aef6a424a2ee
keywords:
- threading WDK display , user-mode drivers
- synchronization WDK display , user-mode drivers
- user-mode display drivers WDK Windows Vista , synchronization
- user-mode display drivers WDK Windows Vista , threading
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Threading Model of User-Mode Display Driver


## <span id="ddk_thread_model_of_user_mode_display_driver_gg"></span><span id="DDK_THREAD_MODEL_OF_USER_MODE_DISPLAY_DRIVER_GG"></span>


The user-mode display driver is not loaded into multiple processes simultaneously--the user-mode display driver DLL is loaded into the address space of each process separately. Still, multiple threads can run in the user-mode display driver at the same time. However, each thread that is running in the user-mode display driver must access a different display device, which is created by a call to the user-mode display driver's [**CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540634) function. For example:

-   An application that creates two Microsoft Direct3D devices can have two threads that access these devices independently.

-   An application can use, on two different threads, a Direct3D device that the Microsoft DirectX 9.0 Direct3D runtime created along with a Microsoft DirectDraw device that the DirectX 5.0 runtime created.

**Note**   Two or more threads that are using the same display device can never run in the user-mode display driver simultaneously.

 

Like the display miniport driver, the user-mode display driver is not required to use any global data structures, because Direct3D devices are independent and state and resources from each device do not affect the other devices. If the user-mode display driver must maintain global cross-device data structures (such as, for a custom system memory heap manager), it must arbitrate access by using its own mechanisms. Such global data structures that the driver manages are strongly discouraged. Because the Direct3D runtime opens an independent "view" of the shared resource in each user-mode display device that must access the resource, cross-process or cross-device resources should not be handled differently from resources that a single process or device use. Lifetime and other management are handled by the DirectX graphics kernel subsystem (*Dxgkrnl.sys*).

On multiple-processor computers, the Direct3D runtime might call a user-mode display driver from a worker thread instead of from the main application thread. This multiple-processor optimization is transparent to the user-mode display driver. When the runtime uses multiple-processor optimization, it still ensures that only one thread that references a particular device runs in the driver at any given time.

 

 





