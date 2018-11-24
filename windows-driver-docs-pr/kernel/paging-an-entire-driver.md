---
title: Paging an Entire Driver
description: Paging an Entire Driver
ms.assetid: d861160f-e429-4ff3-9ca6-4fce4d5d6c1b
keywords: ["pageable drivers WDK kernel , paging entire drivers", "paging entire drivers WDK", "reference counts WDK pageable drivers", "overriding pageable or nonpageable attributes WDK"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Paging an Entire Driver





A driver that uses the **MmLockPagable*Xxx*** support routines and specifies paged and discardable sections consists of nonpaged sections, paged sections, and an INIT section that is discarded after driver initialization.

After a device driver connects interrupts for the devices it manages, the driver's interrupt handling path must be resident in system space. The interrupt-handling code must be part of the driver section that cannot be paged out, in case an interrupt occurs.

Two additional memory manager routines, [**MmPageEntireDriver**](https://msdn.microsoft.com/library/windows/hardware/ff554650) and [**MmResetDriverPaging**](https://msdn.microsoft.com/library/windows/hardware/ff554680), can be used to override the pageable or nonpageable attributes of all sections that make up a driver image. These routines enable a driver to be paged out in its entirety when the device it manages is not being used and cannot generate interrupts.

Examples of system drivers that are completely pageable are the win32k.sys driver, the serial driver, the mailslot driver, the beep driver and the null driver.

A serial driver is typically used intermittently. Until a port it manages is opened, a serial driver can be paged out completely. As soon as a port is opened, the parts of the serial driver that must be memory-resident must be brought into nonpaged system space. Other parts of the driver can remain pageable.

A driver that can be completely paged out should call **MmPageEntireDriver** during driver initialization before interrupts are connected.

When a device managed by a paged-out driver receives an open request, the driver is paged in. Then, the driver must call [**MmResetDriverPaging**](https://msdn.microsoft.com/library/windows/hardware/ff554680) before it connects to interrupts. Calling **MmResetDriverPaging** causes the memory manager to treat the driver's sections according to the attributes acquired during compilation and linkage. Any section that is nonpaged, such as a text section, will be paged into nonpaged system memory; pageable sections will be paged in as they are referenced.

Such a driver must keep a reference count of open handles to its devices. The driver increments the count at each open request for any device and decrements the count at each close request. When the count reaches zero, the driver should disconnect interrupts and then call **MmPageEntireDriver**. If a driver manages more than one device, the count must be zero for all such devices before the driver can call **MmPageEntireDriver**.

It is the driver's responsibility to do whatever synchronization is necessary when changing the reference count, and to prevent the reference count from changing while the pageable state of the driver is changing. That is, in SMP computers, the driver must make sure that **MmPageEntireDriver** cannot be in progress on one processor, while on another processor, an open call is causing interrupts to be connected and the reference count to be incremented.

 

 




