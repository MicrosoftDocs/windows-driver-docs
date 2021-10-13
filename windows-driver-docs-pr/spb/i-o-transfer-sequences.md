---
title: I/O Transfer Sequences
description: The SPB framework extension (SpbCx) supports I/O transfer sequences.
ms.date: 09/14/2021
ms.localizationpriority: medium
---

# I/O Transfer Sequences

The SPB framework extension (SpbCx) supports I/O transfer sequences. An I/O transfer sequence is an ordered set of bus transfers (read and write operations) that is performed as a single, atomic bus operation. All of the transfers in an I/O transfer sequence access the same target device on the bus. While a sequence is being performed, no other devices on the bus can be accessed, even though the SPB controller driver might receive I/O requests for other devices before the I/O transfer sequence completes.

An example of an I/O transfer sequence is a write-read operation, which is a bus write operation followed by a bus read operation. A client peripheral device driver might use this type of sequence to write to a function-select register in an SPB-connected peripheral device, and then read the value of the selected device function. These two transfers can be of different lengths. For example, the write operation might transfer one byte of data, and the read operation might transfer many bytes of data.

## Types of I/O Transfer Sequences

A client can initiate an I/O transfer sequence in one of these ways:

1. The client can specify the entire sequence in an [IOCTL_SPB_EXECUTE_SEQUENCE](./spb-ioctls.md#ioctl_spb_execute_sequence) I/O control request. This request enables the SPB controller driver to use whatever hardware-specific performance optimizations are available to perform the transfer sequence. For more information, see [Single-Request Sequences](#single-request-sequences).

1. The client can send an [IOCTL_SPB_LOCK_CONTROLLER](./spb-ioctls.md#ioctl_spb_lock_controller-control-code) I/O control request to lock the controller at the start of a sequence, and send an [IOCTL_SPB_UNLOCK_CONTROLLER](./spb-ioctls.md#ioctl_spb_unlock_controller-control-code) when the sequence is complete. While the controller is locked, the client sends a separate I/O request ([IRP_MJ_READ](../kernel/irp-mj-read.md) or [IRP_MJ_WRITE](../kernel/irp-mj-write.md)) for each read or write operation in the sequence. For more information, see [Client-Implemented Sequences](#client-implemented-sequences).

Whenever possible, a client should use the **IOCTL_SPB_EXECUTE_SEQUENCE** request, which is faster, is less prone to errors, and significantly decreases the time during which other clients are locked out of the bus. However, a client can use the **IOCTL_SPB_LOCK_CONTROLLER** and **IOCTL_SPB_UNLOCK_CONTROLLER** requests if it must look at the value that is read during one of the transfers in the sequence before it can initiate a later transfer in the sequence. In this case, careful design is required to avoid locking other clients out of the bus for longer than is necessary, and a badly designed peripheral driver can degrade overall system performance.

## Single-Request Sequences

To improve performance, your SPB controller driver should implement an [EvtSpbControllerIoSequence](/windows-hardware/drivers/ddi/spbcx/nc-spbcx-evt_spb_controller_sequence) callback function to handle [IOCTL_SPB_EXECUTE_SEQUENCE](./spb-ioctls.md#ioctl_spb_execute_sequence) requests. This approach adds some complexity to the SPB controller driver but avoids requiring the client to perform an I/O transfer sequence as a series of individual read and write operations while other clients are locked out of the bus.

> [!NOTE]
> Implementation of an **EvtSpbControllerIoSequence** function is strongly recommended, and might become a requirement for Windows 8.

 The implementation of a transfer sequence is similar to that of a simple read or write operation, but additionally requires updates to the stored state of the sequence operation between the individual transfers in the sequence. After the first transfer completes, the SPB controller driver updates the sequence state to select the next transfer in the sequence. The sequence state is stored in the device context and includes the [SPBREQUEST](./spbcx-object-handles.md) handle that is passed to the **EvtSpbControllerIoSequence** callback. The SPB controller driver uses this handle to obtain the buffer, length, direction, and position parameters for the individual transfers in the sequence. For more information about obtaining these parameters, see [SpbRequestGetTransferParameters](/windows-hardware/drivers/ddi/spbcx/nf-spbcx-spbrequestgettransferparameters).

If the SPB controller driver is unable to perform the requested **IOCTL_SPB_EXECUTE_SEQUENCE** operation, it completes the request with a failure code. If such a failure occurs, the client can, as an option, lock the bus, explicitly perform the I/O transfer sequence as a series of simple I/O requests, and then unlock the bus. For more information, see [Client-Implemented Sequences](#client-implemented-sequences).

SpbCx does parameter checking on **IOCTL_SPB_*XXX*** requests that it receives from peripheral device drivers. For **IOCTL_SPB_EXECUTE_SEQUENCE** requests, SpbCx rejects both empty sequences and sequences that contain NULL buffer pointers or zero-length buffers.

The SPB controller driver should verify that the length of each transfer in a sequence does not exceed the driver-specified limit. For example, the SkeletonI2C sample driver in the Windows Driver Kit (WDK) fails a **IOCTL_SPB_EXECUTE_SEQUENCE** request that specifies a transfer exceeding 4K bytes and sets the status code for this request to STATUS_INVALID_PARAMETER. Before initiating a sequence operation for a **IOCTL_SPB_EXECUTE_SEQUENCE** request, the driver should validate the parameters for all transfers in the sequence to verify that the operation can be successfully completed.

SpbCx never precedes an **EvtSpbControllerIoSequence** callback with an [*EvtSpbControllerLock*](/windows-hardware/drivers/ddi/spbcx/nc-spbcx-evt_spb_controller_lock) callback, and it never follows an **EvtSpbControllerIoSequence** callback with an [*EvtSpbControllerUnlock*](/windows-hardware/drivers/ddi/spbcx/nc-spbcx-evt_spb_controller_lock) callback.

## Client-Implemented Sequences

A client of an SPB controller driver can explicitly perform an I/O transfer sequence as a series of simple reads and writes. The client can be either a kernel-mode driver or a user-mode driver that controls a peripheral device that is attached to the bus. Before the first transfer in the sequence, the client sends an [IOCTL_SPB_LOCK_CONTROLLER](./spb-ioctls.md#ioctl_spb_lock_controller-control-code) request to the target device to prevent other, unrelated bus accesses from occurring between the transfers in the sequence. Next, the client sends [IRP_MJ_READ](../kernel/irp-mj-read.md) and [IRP_MJ_WRITE](../kernel/irp-mj-write.md) requests to perform the transfers in the sequence. Finally, the client sends an [IOCTL_SPB_UNLOCK_CONTROLLER](./spb-ioctls.md#ioctl_spb_unlock_controller-control-code) request to release the lock.

A client might need to implement this type of I/O transfer sequence if a later transfer in the sequence has a dependency on an earlier transfer. For example, the first read might indicate how many more bytes to subsequently read or write. If no such dependency exists, however, the client should send an [IOCTL_SPB_EXECUTE_SEQUENCE](./spb-ioctls.md#ioctl_spb_execute_sequence) request to the SPB controller driver, which can perform the sequence more efficiently.

Between the **IOCTL_SPB_LOCK_CONTROLLER** request that starts a client-implemented sequence, and the **IOCTL_SPB_UNLOCK_CONTROLLER** request that ends the sequence, the only I/O requests that the client can send to the target device are **IRP_MJ_READ** and **IRP_MJ_WRITE** requests. Any violation of this rule is an error.

SPB locks are used only to guarantee that a sequence of reads and writes is performed as an atomic bus operation, and should be used exclusively for that purpose.

For more information, see [Handling Client-Implemented Sequences](./handling-client-implemented-sequences.md).
