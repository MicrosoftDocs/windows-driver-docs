---
title: Synchronizing the Use of a Parallel Port
author: windows-driver-content
description: Synchronizing the Use of a Parallel Port
MS-HAID:
- 'vspd\_3371cf0f-b94e-4a92-acf1-e30dd642f4f6.xml'
- 'parports.synchronizing\_the\_use\_of\_a\_parallel\_port'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ea3a1998-9e31-4047-9193-6b402db222c9
keywords: ["parallel ports WDK , synchronization", "synchronization WDK parallel ports"]
---

# Synchronizing the Use of a Parallel Port


## <a href="" id="ddk-synchronizing-the-use-of-a-parallel-port-kg"></a>


Clients must synchronize their use of a parallel port by allocating a parallel port before using it and freeing the port after they are done using it.

Alternatively, a client can select and deselect an IEEE 1284.3 device (which automatically allocates and frees a parallel port) − see [Selecting and Deselecting an IEEE 1284 Device Attached to a Parallel Port](selecting-and-deselecting-an-ieee-1284-device-attached-to-a-parallel-p.md).

A client uses the following device control requests to allocate and free a parallel port:

[**IOCTL\_INTERNAL\_PARALLEL\_PORT\_ALLOCATE**](https://msdn.microsoft.com/library/windows/hardware/ff544023)

[**IOCTL\_INTERNAL\_PARALLEL\_PORT\_FREE**](https://msdn.microsoft.com/library/windows/hardware/ff544026)

A kernel-mode client can also use the system-supplied [parallel port callback routines](https://msdn.microsoft.com/library/windows/hardware/ff544307) that are obtained by using an [**IOCTL\_INTERNAL\_GET\_PARALLEL\_PORT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff544002) request. This request returns a [**PARALLEL\_PORT\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff544322) structure that includes the following pointers to system-supplied callbacks:

-   The **TryAllocatePort** member is a pointer to a [*PPARALLEL\_TRY\_ALLOCATE\_ROUTINE*](https://msdn.microsoft.com/library/windows/hardware/ff544550) callback, which is a nonblocking routine that tries to allocate a parallel port.

-   The **QueryNumWaiters** member is a pointer to a [*PPARALLEL\_QUERY\_WAITERS\_ROUTINE*](https://msdn.microsoft.com/library/windows/hardware/ff544532) callback, which returns the number of port allocate and device select requests that are queued on the work queue of a parallel port.

-   The **FreePort** member is a pointer to a [*PPARALLEL\_FREE\_ROUTINE*](https://msdn.microsoft.com/library/windows/hardware/ff544509) callback, which frees a parallel port.

The [**IOCTL\_INTERNAL\_PARALLEL\_PORT\_ALLOCATE**](https://msdn.microsoft.com/library/windows/hardware/ff544023) request requires the least handling by a client because the system-supplied function driver for parallel ports queues the request for the client if the parallel port is already allocated. The function driver completes an allocate request with a status of STATUS\_SUCCESS after it allocates the port to a client. A client can cancel a pending allocate request at any time because of an unacceptable time-out delay or some other device-specific condition.

**Note**   The [**PPARALLEL\_TRY\_ALLOCATE\_ROUTINE**](https://msdn.microsoft.com/library/windows/hardware/ff544550) callback returns immediately (is nonblocking). If a client uses only the **PPARALLEL\_TRY\_ALLOCATE\_ROUTINE** callback to attempt to allocate a parallel port for which other clients are contending, the parallel port function driver might never allocate the port to the client. To ensure success, a client must use a parallel port allocate request. (The parallel port function driver queues, and subsequently processes, port allocate and device select requests in the order in which the requests are received.)

 

After the parallel port function driver allocates a parallel port to a client, the client has exclusive access to the port. The client must call the [**PPARALLEL\_FREE\_ROUTINE**](https://msdn.microsoft.com/library/windows/hardware/ff544509) callback to free the port. After the client frees the port, the parallel port function driver removes the next request (a port allocate or device select request), if any, from the port's work queue and completes the request.

A client should use the [**PPARALLEL\_QUERY\_WAITERS\_ROUTINE**](https://msdn.microsoft.com/library/windows/hardware/ff544532) callback to determine if there are other clients waiting for a parallel port. A client that needs to allocate a port for an extended period of time should periodically call the **PPARALLEL\_QUERY\_WAITERS\_ROUTINE** callback to determine if other clients are waiting to acquire the port, and, if clients are waiting, free the port as soon as possible.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Synchronizing%20the%20Use%20of%20a%20Parallel%20Port%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


