---
title: Threading Model of User-Mode Display Driver
description: Threading Model of User-Mode Display Driver
ms.assetid: 43bb6032-5f34-434b-8404-aef6a424a2ee
keywords:
- threading WDK display , user-mode drivers
- synchronization WDK display , user-mode drivers
- user-mode display drivers WDK Windows Vista , synchronization
- user-mode display drivers WDK Windows Vista , threading
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Threading Model of User-Mode Display Driver


## <span id="ddk_thread_model_of_user_mode_display_driver_gg"></span><span id="DDK_THREAD_MODEL_OF_USER_MODE_DISPLAY_DRIVER_GG"></span>


The user-mode display driver is not loaded into multiple processes simultaneously--the user-mode display driver DLL is loaded into the address space of each process separately. Still, multiple threads can run in the user-mode display driver at the same time. However, each thread that is running in the user-mode display driver must access a different display device, which is created by a call to the user-mode display driver's [**CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540634) function. For example:

-   An application that creates two Microsoft Direct3D devices can have two threads that access these devices independently.

-   An application can use, on two different threads, a Direct3D device that the Microsoft DirectX 9.0 Direct3D runtime created along with a Microsoft DirectDraw device that the DirectX 5.0 runtime created.

**Note**   Two or more threads that are using the same display device can never run in the user-mode display driver simultaneously.

 

Like the display miniport driver, the user-mode display driver is not required to use any global data structures, because Direct3D devices are independent and state and resources from each device do not affect the other devices. If the user-mode display driver must maintain global cross-device data structures (such as, for a custom system memory heap manager), it must arbitrate access by using its own mechanisms. Such global data structures that the driver manages are strongly discouraged. Because the Direct3D runtime opens an independent "view" of the shared resource in each user-mode display device that must access the resource, cross-process or cross-device resources should not be handled differently from resources that a single process or device use. Lifetime and other management are handled by the DirectX graphics kernel subsystem (*Dxgkrnl.sys*).

On multiple-processor computers, the Direct3D runtime might call a user-mode display driver from a worker thread instead of from the main application thread. This multiple-processor optimization is transparent to the user-mode display driver. When the runtime uses multiple-processor optimization, it still ensures that only one thread that references a particular device runs in the driver at any given time.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Threading%20Model%20of%20User-Mode%20Display%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




