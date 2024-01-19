---
title: Access to Nonresident Allocation
description: GPU access to allocations that aren't resident is illegal and result in a device removed for the application that generated the error.
ms.date: 01/12/2024
---

# Access to nonresident allocation

GPU access to allocations that aren't resident is illegal. Such access results in a device being removed for the application that generated the error.

There are two distinct models of handling such invalid access dependent on whether the faulting engine supports GPU virtual addressing:

* For engines that don’t support GPU virtual addressing and use the allocation and patch location list to patch memory references:

  An invalid access occurs when the user-mode driver submits an allocation list that references an allocation that isn't resident on the device (that is, the user-mode driver didn't called [*MakeResidentCb*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_makeresidentcb) on that allocation). When this invalid access occurs, the graphics kernel puts the faulty context/device in error.

* For engines that do support GPU virtual addressing but access a GPU virtual address (VA) that's invalid:

  The GPU is expected to raise an unrecoverable page fault in the form of an interrupt. When the page fault interrupt occurs, the kernel-mode driver needs to forward the error to the graphics kernel through a new page fault notification. When the graphics kernel receives this notification, it initiates an engine reset on the faulting engine and puts the faulty context/device in error. If the engine reset is unsuccessful, the graphics kernel promotes the error to a full adapter wide timeout detection and recovery (TDR).

  Accessing an invalid VA might happen either because there's no allocation behind the VA or there's a valid allocation but it wasn't made resident.
