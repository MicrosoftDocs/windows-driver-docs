---
title: Connecting an Interrupt Service Routine to a Parallel Port
description: Connecting an Interrupt Service Routine to a Parallel Port
keywords:
- parallel ports WDK , interrupt service routines
- interrupt service routines WDK parallel ports
- deferred port check routines WDK parallel ports
ms.date: 04/20/2017
---

# Connecting an Interrupt Service Routine to a Parallel Port





A kernel-mode client can use a [**IOCTL\_INTERNAL\_PARALLEL\_CONNECT\_INTERRUPT**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_parallel_connect_interrupt) request to connect an interrupt service routine and a *deferred port check routine* to the operation of the parallel port function driver.

**Note**   Microsoft does not recommend using a client-supplied interrupt routine. The use of interrupts might cause system instability. By default, the IOCTL\_INTERNAL\_PARALLEL\_CONNECT\_INTERRUPT request is disabled.

 

To facilitate the porting and development of drivers for parallel devices, the system-supplied function driver for parallel ports supports a registry flag that kernel-mode clients can use to enable and disable a connect interrupt request. The connect interrupt request is enabled by the registry entry value **EnableConnectInterruptIoctl** under the Plug and Play registry key for the parallel port. The entry value has type REG\_DWORD and the default value is 0x0 (disabled). A value that is not equal to 0x0 enables the connect interrupt request.

The connect interrupt request returns a [**PARALLEL\_INTERRUPT\_INFORMATION**](/windows-hardware/drivers/ddi/parallel/ns-parallel-_parallel_interrupt_information) structure that includes a pointer to the parallel port's interrupt object and the following pointers to system-supplied callback routines:

-   The **TryAllocatePortAtInterruptLevel** member is a pointer to a nonblocking [*PPARALLEL\_TRY\_ALLOCATE\_ROUTINE (ISR)*](/windows-hardware/drivers/ddi/parallel/nc-parallel-pparallel_try_allocate_routine) callback, which a kernel-mode driver can use in an ISR to allocate a parallel port.

-   The **FreePortFromInterruptLevel** member is a pointer to a nonblocking [*PPARALLEL\_FREE\_ROUTINE (ISR)*](/windows-hardware/drivers/ddi/parallel/nc-parallel-pparallel_free_routine) callback that a kernel-mode driver can use in an ISR to free a parallel port.

The interrupt service routine is called at IRQL = DIRQL after a hardware interrupt on the parallel port. If a driver connects an interrupt service routine and has an **Unload** routine, the driver must send an [**IOCTL\_INTERNAL\_PARALLEL\_DISCONNECT\_INTERRUPT**](/windows-hardware/drivers/ddi/parallel/ni-parallel-ioctl_internal_parallel_disconnect_interrupt) request in its **Unload** routine.

The deferred port check routine is called after the parallel port is freed and when there are no pending requests to allocate the port or select an IEEE 1284.3 device. A driver can use the deferred port check routine to enable interrupts.

If a client's interrupt service routine is called when the client does not have a port allocated, the client can attempt to quickly allocate the port by calling the PPARALLEL\_TRY\_ALLOCATE\_ROUTINE (ISR) callback. The client can also use the PPARALLEL\_FREE\_ROUTINE (ISR) callback to free the port.

Because a parallel port is shared by drivers, the parallel port function driver maintains a list of interrupt service routines and deferred port check routines connected to a parallel port. The parallel port function driver calls all connected interrupt routines and deferred port check routines in the order in which they were connected.

 

