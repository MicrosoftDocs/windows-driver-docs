---
title: Connecting to a Parallel Device
description: Connecting to a Parallel Device
keywords:
- parallel devices WDK , connections
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Connecting to a Parallel Device





A client uses the [**IOCTL\_INTERNAL\_PARCLASS\_CONNECT**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_parclass_connect) request to obtain a [**PARCLASS\_INFORMATION**](/windows-hardware/drivers/ddi/parallel/ns-parallel-_parclass_information) structure that contains:

-   I/O resources allocated to the parallel port

-   Hardware capabilities of the parallel port

-   Pointers to callback routines that a kernel-mode driver can use to set the IEEE 1284 operating modes for a parallel device - see [Setting and Clearing a Communication Mode for a Parallel Device](setting-and-clearing-a-communication-mode-for-a-parallel-device.md)

-   Pointers to callback routines that a kernel-mode driver can use to read and write a parallel device - see [Reading and Writing a Parallel Device](reading-and-writing-a-parallel-device.md).

The callback routines provide functionality that a typical function driver needs. Using the callback routines is more efficient than using equivalent device control requests.

A client disconnects from a device by using a [**IOCTL\_INTERNAL\_PARCLASS\_DISCONNECT**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_parclass_disconnect) request.

 

