---
title: Locking and Unlocking Stream Pointers
author: windows-driver-content
description: Locking and Unlocking Stream Pointers
ms.assetid: 3826a5bc-4ba5-4ada-a8aa-e7bbd949187e
keywords: ["stream pointers WDK AVStream , locked and unlocked", "locked stream pointers WDK AVStream", "unlocked stream pointers WDK AVStream"]
---

# Locking and Unlocking Stream Pointers


## <a href="" id="ddk-locking-and-unlocking-stream-pointers-ksg"></a>


Each stream pointer maintains a lock status: either locked or unlocked.

Locked stream pointers are guaranteed to reference data in the queue. Data frames pointed to by locked stream pointers cannot be canceled. As such, minidrivers should minimize the time that they spend holding locked stream pointers.

An unlocked stream pointer is not guaranteed to reference a data frame within the queue. By holding an unlocked stream pointer, a minidriver can retain a data pointer, but still allow the frame to be canceled.

It is possible to access data pointed to by an unlocked stream pointer. If the *CancelCallback* routine you provide in [**KsStreamPointerClone**](https://msdn.microsoft.com/library/windows/hardware/ff567129) calls [**KsStreamPointerDelete**](https://msdn.microsoft.com/library/windows/hardware/ff567130), you should synchronize *CancelCallback* and any data access that it performs. The minidriver must ensure that the cancellation callback routine does not delete the stream pointer while another thread is using it.

If the cancellation callback routine does not call **KsStreamPointerDelete**, synchronization might not be necessary.

To lock a stream pointer, call [**KsStreamPointerLock**](https://msdn.microsoft.com/library/windows/hardware/ff567134). To unlock a stream pointer, call [**KsStreamPointerUnlock**](https://msdn.microsoft.com/library/windows/hardware/ff567137).

When an IRP is canceled, AVStream calls the cancellation callbacks for all unlocked stream pointers that point to frames within the IRP.

Unlock the leading and trailing edge stream pointers only when they are not in use.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Locking%20and%20Unlocking%20Stream%20Pointers%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


