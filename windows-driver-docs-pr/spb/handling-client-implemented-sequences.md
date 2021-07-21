---
title: Handling Client-Implemented Sequences
description: The optional EvtSpbControllerLock and EvtSpbControllerUnlock event callback functions perform complementary operations.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Client-Implemented Sequences


The optional [*EvtSpbControllerLock*](/windows-hardware/drivers/ddi/spbcx/nc-spbcx-evt_spb_controller_lock) and [*EvtSpbControllerUnlock*](/windows-hardware/drivers/ddi/spbcx/nc-spbcx-evt_spb_controller_unlock) event callback functions perform complementary operations. The *EvtSpbControllerLock* function is a handler for [**IOCTL\_SPB\_LOCK\_CONTROLLER**](https://msdn.microsoft.com/library/windows/hardware/hh450858) requests. The *EvtSpbControllerUnlock* function is a handler for [**IOCTL\_SPB\_UNLOCK\_CONTROLLER**](https://msdn.microsoft.com/library/windows/hardware/hh450859) requests. A client (that is, the driver for a peripheral device on the bus) sends these requests to start and end [I/O transfer sequences](./i-o-transfer-sequences.md). Most SPB controller drivers do not support **IOCTL\_SPB\_LOCK\_CONTROLLER** and **IOCTL\_SPB\_UNLOCK\_CONTROLLER** requests and, therefore, do not implement *EvtSpbControllerLock* and *EvtSpbControllerUnlock* functions.

A client can perform an I/O transfer sequence as a series of simple transfer requests (that is, [**IRP\_MJ\_READ**](../kernel/irp-mj-read.md) and [**IRP\_MJ\_WRITE**](../kernel/irp-mj-write.md) requests). The first transfer in the sequence must be preceded by an **IOCTL\_SPB\_LOCK\_CONTROLLER** request—this request tells the SPB controller driver to lock the bus for the duration of the I/O transfer sequence. The last transfer must be followed by an **IOCTL\_SPB\_UNLOCK\_CONTROLLER** request, which tells the driver to unlock the bus. This type of I/O transfer sequence is called a [client-implemented sequence](./i-o-transfer-sequences.md#client-implemented-sequences) to distinguish it from a [single-request sequence](./i-o-transfer-sequences.md#single-request-sequences), which uses an [**IOCTL\_SPB\_EXECUTE\_SEQUENCE**](https://msdn.microsoft.com/library/windows/hardware/hh450857) request instead of **IOCTL\_SPB\_LOCK\_CONTROLLER** and **IOCTL\_SPB\_UNLOCK\_CONTROLLER** requests.

While the driver for a peripheral device holds a lock on the bus, the bus controller allows access to no other peripheral devices on the bus. The details of the bus-locking operation depend on the bus type. For an I²C controller, a change in transfer direction (a read followed by a write, or vice versa) requires an I²C restart operation. For an SPI controller, the chip-select to the target device must remain asserted while the controller lock remains in effect. For more information, see [Atomic Bus Operations](./atomic-bus-operations.md).

Support for client-implemented transfer sequences is optional. Your SPB controller driver should claim to support them only if the controller can do the following:

-   Lock the bus for the duration of the client-implemented sequence.
-   Unlock the bus at any time. For example, if an unlock request occurs between byte transfers, the controller should be able to unlock the bus without waiting for the next byte transfer over the bus.

While the bus is locked, the client can send an arbitrary sequence of simple transfer requests. That is, the sequence can be of arbitrary length and can be any combination of reads and writes.

To indicate support for client-implemented sequences, an SPB controller driver implements an *EvtSpbControllerUnlock* function. If your driver implements this function, the SPB framework extension (SpbCx) accepts **IOCTL\_SPB\_LOCK\_CONTROLLER** and **IOCTL\_SPB\_UNLOCK\_CONTROLLER** requests from clients. Otherwise, SpbCx fails these requests by completing them with the STATUS\_NOT\_SUPPORTED status code.

An SPB controller driver that implements an *EvtSpbControllerUnlock* function is not required to implement an *EvtSpbControllerLock* function. However, an SPB controller driver that implements an *EvtSpbControllerLock* function must also implement an *EvtSpbControllerUnlock* function.

If your driver implements an *EvtSpbControllerUnlock* function but not an *EvtSpbControllerLock* function, SpbCx calls the *EvtSpbControllerUnlock* function to handle **IOCTL\_SPB\_UNLOCK\_CONTROLLER** requests, but simply completes **IOCTL\_SPB\_LOCK\_CONTROLLER** requests with STATUS\_SUCCESS status codes.

Your driver has two ways to detect the start of a client-implemented sequence. First, if your driver implements an *EvtSpbControllerLock* function, SpbCx calls this function to handle an **IOCTL\_SPB\_LOCK\_CONTROLLER** requests from a client. The driver can rely on this call occurring before the first transfer request in a sequence. Second, if your driver does not implement an *EvtSpbControllerLock* function, the driver can call the [**SpbRequestGetParameters**](/windows-hardware/drivers/ddi/spbcx/nf-spbcx-spbrequestgetparameters) method when the driver handles a simple transfer request from the client. To indicate that the requested transfer is the first transfer in a sequence, this method sets the **Position** member in the method's output structure to **SpbRequestSequencePositionFirst**.

The *EvtSpbControllerUnlock* callback is the only way that a driver can determine when a sequence ends. A driver that does not implement an *EvtSpbControllerUnlock* function cannot support client-implemented sequences.

 

