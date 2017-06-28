---
title: Isolating Pageable Code
author: windows-driver-content
description: Isolating Pageable Code
ms.assetid: 86189154-606a-4df8-b3a9-040bbaffaa2f
keywords: ["pageable drivers WDK kernel , isolating code", "isolating pageable code", "spin locks WDK memory"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Isolating Pageable Code


## <a href="" id="ddk-isolating-pageable-code-kg"></a>


A routine that uses a spin lock cannot be paged. However, in some cases you can isolate the operations that require a spin lock in a separate routine that will not be included in the pageable section.

For example, consider the following fragment:

```
//  PAGED_CODE(); 
 
KeInitializeEvent( &amp;event, NotificationEvent, FALSE ); 
irp = IoBuildDeviceIoControlRequest( IRP_MJ_DEVICE_CONTROL, 
                                     DeviceObject, 
                                     (PVOID) NULL, 
                                     0, 
                                     (PVOID) NULL, 
                                     0, 
                                     FALSE, 
                                     &amp;event, 
                                     &amp;ioStatus ); 
if (irp) { 
   irpSp = IoGetNextIrpStackLocation( irp ); 
   irpSp->MajorFunction = IRP_MJ_FILE_SYSTEM_CONTROL; 
   irpSp->MinorFunction = IRP_MN_LOAD_FILE_SYSTEM; 
   status = IoCallDriver( DeviceObject, irp ); 
   if (status == STATUS_PENDING) { 
   (VOID) KeWaitForSingleObject( &amp;event, 
                                 Executive, 
                                 KernelMode, 
                                 FALSE, 
                                 (PLARGE_INTEGER) NULL ); 
   } 
} 

SPINLOCKUSE ! 
KeAcquireSpinLock( &amp;IopDatabaseLock, &amp;irql ); 
// Code inside spin lock ...

DeviceObject->ReferenceCount--; 
 
if (!DeviceObject->ReferenceCount &amp;&amp; !DeviceObject->AttachedDevice) { 
   //Unload the driver
   .
   .
   . 
} else { 
   KeReleaseSpinLock( &amp;IopDatabaseLock, irql ); 
} 
```

The preceding routine could be made pageable (saving about 160 bytes) by moving the few lines of code that reference a spin lock into a separate routine.

In addition, remember that driver code must not be marked as pageable if it calls any **Ke*Xxx*** support routines, such as [**KeReleaseMutex**](https://msdn.microsoft.com/library/windows/hardware/ff553140) or [**KeReleaseSemaphore**](https://msdn.microsoft.com/library/windows/hardware/ff553143), in which the *Wait* parameter is set to **TRUE**. Such a call returns with IRQL at DISPATCH\_LEVEL.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Isolating%20Pageable%20Code%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


