---
title: Accessing User-Space Memory
author: windows-driver-content
description: Accessing User-Space Memory
ms.assetid: db0b6ba2-4cec-46c1-b13f-aba4c10a2d8c
keywords: ["memory management WDK kernel , user-space memory", "user-space memory WDK kernel", "virtual user-space memory WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Accessing User-Space Memory


## <a href="" id="ddk-accessing-user-space-memory-kg"></a>


Drivers cannot allocate user-space virtual memory because they run in kernel mode. In addition, a driver cannot access memory through user-mode virtual addresses unless it is running in the context of the user-mode thread that caused the driver's current I/O operation and it is using that thread's virtual addresses.

Only highest-level drivers, such as FSDs, can be sure their dispatch routines will be called in the context of such a user-mode thread. A highest-level driver can call [**MmProbeAndLockPages**](https://msdn.microsoft.com/library/windows/hardware/ff554664) to lock down a user buffer before setting up an IRP for lower drivers.

Lowest-level and intermediate drivers that set up their device objects for [buffered I/O](methods-for-accessing-data-buffers.md) or [direct I/O](methods-for-accessing-data-buffers.md) can rely on the I/O manager or a highest-level driver to pass valid access to locked-down user buffers or to system-space buffers in IRPs.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Accessing%20User-Space%20Memory%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


