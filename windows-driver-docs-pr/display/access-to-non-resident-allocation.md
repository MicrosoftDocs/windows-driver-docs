---
title: Access to non-resident allocation
description: GPU access to allocations which are not resident is illegal and will result in a device removed for the application that generated the error.
ms.date: 04/20/2017
---

# <span id="display.access_to_non-resident_allocation"></span>Access to non-resident allocation


Graphics processing unit (GPU) access to allocations which are not resident is illegal and will result in a device removed for the application that generated the error.

There are two distinct models of handling such invalid access dependent on whether the faulting engine supports GPU virtual addressing or not:

-   For engines which don’t support GPU virtual addressing and use the allocation and patch location list to patch memory references, an invalid access occurs when the user mode driver submits an allocation list which references an allocation which is not resident on the device (i.e. the user mode driver hasn’t called [*MakeResidentCb*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_makeresidentcb) on that allocation). When this occurs, the graphics kernel will put the faulty context/device in error.
-   For engines which do support GPU virtual addressing but access a GPU virtual address that is invalid, either because there is no allocation behind the virtual address or there is a valid allocation but it hasn’t been made resident, the GPU is expected to raise an unrecoverable page fault in the form of an interrupt. When the page fault interrupt occurs, the kernel mode driver will need to forward the error to the graphics kernel through a new page fault notification. Upon receiving this notification, the graphics kernel will initiate an engine reset on the faulting engine and put the faulty context/device in error. If the engine reset is unsuccessful, the graphics kernel will promote the error to a full adapter wide timeout detection and recovery (TDR).

 

