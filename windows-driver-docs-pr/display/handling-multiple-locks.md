---
title: Handling Multiple Locks
description: Handling Multiple Locks
ms.assetid: d62b9577-d78f-431d-a5bf-c06c9be345c0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling Multiple Locks


With the Direct3D runtime, you can allow vertex and index buffers to have more than one lock outstanding. User-mode display drivers must handle multiple locks the same way as the runtime in the [Windows 2000 Display Driver Model](windows-2000-display-driver-model-design-guide.md).

A user-mode display driver must not fail a call to its [**LockAsync**](https://msdn.microsoft.com/library/windows/hardware/ff568214) function for a resource that is already locked. That is, the driver cannot fail any calls to its *LockAsync* function for a particular resource after the first call to its *LockAsync* function succeeds in locking that resource. Similarly, the driver cannot fail any calls to its [**Lock**](https://msdn.microsoft.com/library/windows/hardware/ff568213) function for a particular resource after the first call to its *Lock* function succeeds in locking that resource. The runtime matches each call that it makes to the driver's *LockAsync* function with a call to the driver's [**UnlockAsync**](https://msdn.microsoft.com/library/windows/hardware/ff570105) function. The runtime also matches each call that it makes to the driver's *Lock* function with a call to the driver's [**Unlock**](https://msdn.microsoft.com/library/windows/hardware/ff570104) function.

The user-mode display driver cannot fail a call to its [**UnlockAsync**](https://msdn.microsoft.com/library/windows/hardware/ff570105) function unless the resource that the [**D3DDDIARG\_UNLOCKASYNC**](https://msdn.microsoft.com/library/windows/hardware/ff543395) structure describes was not actually locked by a previous call to the driver's *LockAsync* function. Similarly, the driver cannot fail a call to its [**Unlock**](https://msdn.microsoft.com/library/windows/hardware/ff570104) function unless the resource that the [**D3DDDIARG\_UNLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff543394) structure describes was not actually locked by a previous call to the driver's *Lock* function. In situations in which the resources were not previously locked, *UnlockAsync* and *Unlock* return E\_INVALIDARG.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Handling%20Multiple%20Locks%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




