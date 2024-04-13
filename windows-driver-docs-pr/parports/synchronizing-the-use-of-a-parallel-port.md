---
title: Synchronizing the Use of a Parallel Port
description: Synchronizing the Use of a Parallel Port
keywords:
- parallel ports WDK , synchronization
- synchronization WDK parallel ports
ms.date: 03/03/2023
---

# Synchronizing the Use of a Parallel Port





Clients must synchronize their use of a parallel port by allocating a parallel port before using it and freeing the port after they are done using it.

Alternatively, a client can select and deselect an IEEE 1284.3 device (which automatically allocates and frees a parallel port) − see [Selecting and Deselecting an IEEE 1284 Device Attached to a Parallel Port](selecting-and-deselecting-an-ieee-1284-device-attached-to-a-parallel-p.md).

A client uses the following device control requests to allocate and free a parallel port:

[**IOCTL\_INTERNAL\_PARALLEL\_PORT\_ALLOCATE**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_parallel_port_allocate)

[**IOCTL\_INTERNAL\_PARALLEL\_PORT\_FREE**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_parallel_port_free)

A kernel-mode client can also use the system-supplied [parallel port callback routines](/windows-hardware/drivers/ddi/_parports/) that are obtained by using an [**IOCTL\_INTERNAL\_GET\_PARALLEL\_PORT\_INFO**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_get_parallel_port_info) request. This request returns a [**PARALLEL\_PORT\_INFORMATION**](/windows-hardware/drivers/ddi/parallel/ns-parallel-_parallel_port_information) structure that includes the following pointers to system-supplied callbacks:

-   The **TryAllocatePort** member is a pointer to a [*PPARALLEL\_TRY\_ALLOCATE\_ROUTINE*](/previous-versions/windows/hardware/drivers/ff544550(v=vs.85)) callback, which is a nonblocking routine that tries to allocate a parallel port.

-   The **QueryNumWaiters** member is a pointer to a [*PPARALLEL\_QUERY\_WAITERS\_ROUTINE*](/windows-hardware/drivers/ddi/parallel/nc-parallel-pparallel_query_waiters_routine) callback, which returns the number of port allocate and device select requests that are queued on the work queue of a parallel port.

-   The **FreePort** member is a pointer to a [*PPARALLEL\_FREE\_ROUTINE*](/windows-hardware/drivers/ddi/parallel/nc-parallel-pparallel_free_routine) callback, which frees a parallel port.

The [**IOCTL\_INTERNAL\_PARALLEL\_PORT\_ALLOCATE**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_parallel_port_allocate) request requires the least handling by a client because the system-supplied function driver for parallel ports queues the request for the client if the parallel port is already allocated. The function driver completes an allocate request with a status of STATUS\_SUCCESS after it allocates the port to a client. A client can cancel a pending allocate request at any time because of an unacceptable time-out delay or some other device-specific condition.

**Note**   The [**PPARALLEL\_TRY\_ALLOCATE\_ROUTINE**](/previous-versions/windows/hardware/drivers/ff544550(v=vs.85)) callback returns immediately (is nonblocking). If a client uses only the **PPARALLEL\_TRY\_ALLOCATE\_ROUTINE** callback to attempt to allocate a parallel port for which other clients are contending, the parallel port function driver might never allocate the port to the client. To ensure success, a client must use a parallel port allocate request. (The parallel port function driver queues, and subsequently processes, port allocate and device select requests in the order in which the requests are received.)

 

After the parallel port function driver allocates a parallel port to a client, the client has exclusive access to the port. The client must call the [**PPARALLEL\_FREE\_ROUTINE**](/windows-hardware/drivers/ddi/parallel/nc-parallel-pparallel_free_routine) callback to free the port. After the client frees the port, the parallel port function driver removes the next request (a port allocate or device select request), if any, from the port's work queue and completes the request.

A client should use the [**PPARALLEL\_QUERY\_WAITERS\_ROUTINE**](/windows-hardware/drivers/ddi/parallel/nc-parallel-pparallel_query_waiters_routine) callback to determine if there are other clients waiting for a parallel port. A client that needs to allocate a port for an extended period of time should periodically call the **PPARALLEL\_QUERY\_WAITERS\_ROUTINE** callback to determine if other clients are waiting to acquire the port, and, if clients are waiting, free the port as soon as possible.

 

