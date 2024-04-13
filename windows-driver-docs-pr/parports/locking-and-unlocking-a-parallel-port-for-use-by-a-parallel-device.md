---
title: Locking and Unlocking a Parallel Port
description: Locking and Unlocking a Parallel Port for Use by a Parallel Device
keywords:
- parallel devices WDK , port locking/unlocking
- locking WDK parallel devices
- unlocking parallel ports
- uninterrupted operations WDK parallel devices
- freeing parallel ports
ms.date: 03/03/2023
---

# Locking and Unlocking a Parallel Port for Use by a Parallel Device





To execute an uninterrupted sequence of operations on a parallel device, a client must allocate the parallel port and select the IEEE 1284.3 device on the port. A sequence of operations can include completing I/O requests and executing the callback routines provided by the parallel port bus driver. After completing a sequence of operations, a client must deselect the IEEE 1284.3 device and then free the parent parallel port.

The system-supplied bus driver for parallel ports supports the following internal device control requests to lock and unlock a parallel port:

[**IOCTL\_INTERNAL\_LOCK\_PORT**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_lock_port)

[**IOCTL\_INTERNAL\_LOCK\_PORT\_NO\_SELECT**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_lock_port_no_select)

[**IOCTL\_INTERNAL\_UNLOCK\_PORT**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_unlock_port)

[**IOCTL\_INTERNAL\_UNLOCK\_PORT\_NO\_DESELECT**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_unlock_port_no_deselect)

Microsoft recommends that clients use the lock port and unlock port requests if the devices can be operated by only using the functionality that these requests provide. Otherwise, clients can use the lock port no select and lock port no deselect requests. This provides a client additional flexibility to operate a device that uses a selection and deselection mechanism that does not conform to the IEEE 1284.3 daisy chain specifications. A client can use the lock port no select request to allocate the port, and then operate the device by using [device control requests for parallel devices](/windows-hardware/drivers/ddi/_parports/) and [parallel device callback routines](/windows-hardware/drivers/ddi/_parports/).

Clients can send individual I/O requests to parallel devices without the need to lock and unlock a parallel port because the parallel port bus driver administers port sharing among clients. The parallel port bus driver automatically allocates the parallel port immediately before it processes an I/O request and, if there are clients waiting for the port, frees the port immediately after completing the I/O request.

If the parallel port bus driver can allocate the port to the parallel device within a set time-out period, the device's worker thread completes the request. Otherwise, the parallel port bus driver completes the pending request with a status of STATUS\_DEVICE\_BUSY.

 

