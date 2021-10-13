---
title: Accessing User-Space Memory
description: Accessing User-Space Memory
keywords: ["memory management WDK kernel , user-space memory", "user-space memory WDK kernel", "virtual user-space memory WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Accessing User-Space Memory


A driver cannot directly access memory through user-mode virtual addresses unless it is running in the context of the user-mode thread that caused the driver's current I/O operation and it is using that thread's virtual addresses.

Only highest-level drivers, such as FSDs, can be sure their dispatch routines will be called in the context of such a user-mode thread. A highest-level driver can call [**MmProbeAndLockPages**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmprobeandlockpages) to lock down a user buffer before setting up an IRP for lower drivers.

Lowest-level and intermediate drivers that set up their device objects for [buffered I/O](methods-for-accessing-data-buffers.md) or [direct I/O](methods-for-accessing-data-buffers.md) can rely on the I/O manager or a highest-level driver to pass valid access to locked-down user buffers or to system-space buffers in IRPs.

 

