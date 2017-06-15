---
title: Introduction to Cancel Routines
author: windows-driver-content
description: Introduction to Cancel Routines
MS-HAID:
- 'IRPs\_819bb2cc-7128-48e0-abac-2bac2d65e88f.xml'
- 'kernel.introduction\_to\_cancel\_routines'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 99f7f045-2b2f-4fb3-ac1c-99ab76fa46ad
keywords: ["canceling IRPs, about canceling IRPs", "Cancel routines, about Cancel routines", "associated IRP"]
---

# Introduction to Cancel Routines


## <a href="" id="ddk-introduction-to-cancel-routines-kg"></a>


Any driver in which IRPs can be held in a pending state for an indefinite interval must have one or more [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routines. For example, a keyboard driver might wait indefinitely for a user to press a key. Conversely, if a driver will never queue more IRPs than it can complete in five minutes, it probably does not need a *Cancel* routine.

Suppose a user-mode thread makes an I/O request, which is queued by a highest-level device driver's dispatch routine, and the requesting thread is terminated while the IRP is queued. IRPs queued on behalf of a terminated thread should be canceled. Consequently, the driver must set a driver-supplied *Cancel* routine in each IRP that it queues.

A driver that creates associated IRPs must cancel them when the master IRP is canceled. Because associated IRPs are not associated with a requesting thread, the master IRP's *Cancel* routine is responsible for canceling any associated IRPs when the master IRP is canceled.

The number of *Cancel* routines any driver has depends on the driver's design. In general, a driver should have a *Cancel* routine for each stage in its I/O processing at which an IRP might be held in a pending state for an indefinite interval. Such pending IRPs are said to be *held in a cancelable state*.

Consider the following design guidelines:

-   The highest-level driver in a chain of layered drivers must have at least one *Cancel* routine if it queues IRPs or otherwise holds IRPs in a cancelable state. It can have more than one *Cancel* routine, if necessary.

-   Lower-level drivers in which IRPs can be held in a cancelable state for relatively long intervals also should have one or more *Cancel* routines.

-   If a driver manages its own internal queues of IRPs, it should have a separate *Cancel* routine for each of its queues.

Some highest-level drivers for interactive devices, such as keyboard, mouse, sound, parallel class and serial drivers, must have *Cancel* routines. Some lower-level drivers, such as a parallel port driver that holds IRPs queued for some number of higher-level class drivers for relatively long intervals, also should have *Cancel* routines.

Mass-storage device drivers, along with intermediate drivers layered over them, are unlikely to have *Cancel* routines. It is the responsibility of a file system driver to handle the cancellation of file I/O requests, while the IRPs input to lower-level mass-storage drivers are usually processed to completion too quickly to be cancelable.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Introduction%20to%20Cancel%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


