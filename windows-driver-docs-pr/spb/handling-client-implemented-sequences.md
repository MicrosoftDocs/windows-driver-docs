---
Description: 'The optional EvtSpbControllerLock and EvtSpbControllerUnlock event callback functions perform complementary operations.'
MS-HAID: 'SPB.handling\_client\_implemented\_sequences'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: 'Handling Client-Implemented Sequences'
author: windows-driver-content
---

# Handling Client-Implemented Sequences


The optional [*EvtSpbControllerLock*](buses.evtspbcontrollerlock) and [*EvtSpbControllerUnlock*](buses.evtspbcontrollerunlock) event callback functions perform complementary operations. The *EvtSpbControllerLock* function is a handler for [**IOCTL\_SPB\_LOCK\_CONTROLLER**](buses.ioctl_spb_lock_controller) requests. The *EvtSpbControllerUnlock* function is a handler for [**IOCTL\_SPB\_UNLOCK\_CONTROLLER**](buses.ioctl_spb_unlock_controller) requests. A client (that is, the driver for a peripheral device on the bus) sends these requests to start and end [I/O transfer sequences](buses.i_o_transfer_sequences). Most SPB controller drivers do not support **IOCTL\_SPB\_LOCK\_CONTROLLER** and **IOCTL\_SPB\_UNLOCK\_CONTROLLER** requests and, therefore, do not implement *EvtSpbControllerLock* and *EvtSpbControllerUnlock* functions.

A client can perform an I/O transfer sequence as a series of simple transfer requests (that is, [**IRP\_MJ\_READ**](kernel.irp_mj_read) and [**IRP\_MJ\_WRITE**](kernel.irp_mj_write) requests). The first transfer in the sequence must be preceded by an **IOCTL\_SPB\_LOCK\_CONTROLLER** request—this request tells the SPB controller driver to lock the bus for the duration of the I/O transfer sequence. The last transfer must be followed by an **IOCTL\_SPB\_UNLOCK\_CONTROLLER** request, which tells the driver to unlock the bus. This type of I/O transfer sequence is called a [client-implemented sequence](buses.i_o_transfer_sequences#buses-client-implemented-sequences) to distinguish it from a [single-request sequence](buses.i_o_transfer_sequences#buses-single-request-sequences), which uses an [**IOCTL\_SPB\_EXECUTE\_SEQUENCE**](buses.ioctl_spb_execute_sequence) request instead of **IOCTL\_SPB\_LOCK\_CONTROLLER** and **IOCTL\_SPB\_UNLOCK\_CONTROLLER** requests.

While the driver for a peripheral device holds a lock on the bus, the bus controller allows access to no other peripheral devices on the bus. The details of the bus-locking operation depend on the bus type. For an I²C controller, a change in transfer direction (a read followed by a write, or vice versa) requires an I²C restart operation. For an SPI controller, the chip-select to the target device must remain asserted while the controller lock remains in effect. For more information, see [Atomic Bus Operations](buses.atomic_bus_operations).

Support for client-implemented transfer sequences is optional. Your SPB controller driver should claim to support them only if the controller can do the following:

-   Lock the bus for the duration of the client-implemented sequence.
-   Unlock the bus at any time. For example, if an unlock request occurs between byte transfers, the controller should be able to unlock the bus without waiting for the next byte transfer over the bus.

While the bus is locked, the client can send an arbitrary sequence of simple transfer requests. That is, the sequence can be of arbitrary length and can be any combination of reads and writes.

To indicate support for client-implemented sequences, an SPB controller driver implements an *EvtSpbControllerUnlock* function. If your driver implements this function, the SPB framework extension (SpbCx) accepts **IOCTL\_SPB\_LOCK\_CONTROLLER** and **IOCTL\_SPB\_UNLOCK\_CONTROLLER** requests from clients. Otherwise, SpbCx fails these requests by completing them with the STATUS\_NOT\_SUPPORTED status code.

An SPB controller driver that implements an *EvtSpbControllerUnlock* function is not required to implement an *EvtSpbControllerLock* function. However, an SPB controller driver that implements an *EvtSpbControllerLock* function must also implement an *EvtSpbControllerUnlock* function.

If your driver implements an *EvtSpbControllerUnlock* function but not an *EvtSpbControllerLock* function, SpbCx calls the *EvtSpbControllerUnlock* function to handle **IOCTL\_SPB\_UNLOCK\_CONTROLLER** requests, but simply completes **IOCTL\_SPB\_LOCK\_CONTROLLER** requests with STATUS\_SUCCESS status codes.

Your driver has two ways to detect the start of a client-implemented sequence. First, if your driver implements an *EvtSpbControllerLock* function, SpbCx calls this function to handle an **IOCTL\_SPB\_LOCK\_CONTROLLER** requests from a client. The driver can rely on this call occurring before the first transfer request in a sequence. Second, if your driver does not implement an *EvtSpbControllerLock* function, the driver can call the [**SpbRequestGetParameters**](buses.spbrequestgetparameters) method when the driver handles a simple transfer request from the client. To indicate that the requested transfer is the first transfer in a sequence, this method sets the **Position** member in the method's output structure to **SpbRequestSequencePositionFirst**.

The *EvtSpbControllerUnlock* callback is the only way that a driver can determine when a sequence ends. A driver that does not implement an *EvtSpbControllerUnlock* function cannot support client-implemented sequences.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BSPB\buses%5D:%20Handling%20Client-Implemented%20Sequences%20%20RELEASE:%20%286/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


