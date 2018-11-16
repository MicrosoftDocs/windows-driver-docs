---
title: SPB I/O Requests
description: These IOCTLs are sent by a client (peripheral driver) handled by controller driver.
ms.assetid: 4b8ed75e-1f03-4b7a-ad9d-0dfa9b20274c
ms.date: 11/29/2017
ms.localizationpriority: medium
---

# SPB I/O Requests
The system-supplied CTL_CODE macro, which is described in Defining I/O Control Codes, is used to define IOCTL_SPB_* control codes in Spb.h.

|Topic | Description|
|------|:----------------|
|[IOCTL_SPB_EXECUTE_SEQUENCE](#ioctl-spb-execute-sequence) | The IOCTL_SPB_EXECUTE_SEQUENCE I/O control code enables a client (peripheral driver) of the SPB controller driver to perform a sequence of transfers (reads and writes) as a single, atomic operation with one I/O request. The designated device on the bus is the target for all transfers in the sequence.|
|[IOCTL_SPB_FULL_DUPLEX](#ioctl-spb-full-duplex) | The IOCTL_SPB_FULL_DUPLEX control code is used by a client (peripheral driver) to request a full-duplex I/O operation. Full-duplex I/O operations are supported by controllers for buses such as SPI that can simultaneously read and write data.|
|[IOCTL_SPB_LOCK_CONNECTION](#ioctl-spb-lock-connection) | The IOCTL_SPB_LOCK_CONNECTION control code is used by a client (peripheral driver) to acquire the connection lock on an SPB-connected target device that is shared with another client. While a client holds the connection lock, this client has exclusive access to the device.|
|[IOCTL_SPB_LOCK_CONTROLLER](#ioctl-spb-lock-controller) | The IOCTL_SPB_LOCK_CONTROLLER control code is used by a client (peripheral driver) to lock the SPB controller. While the controller is locked, the client has exclusive use of the bus to access the specified target device for the lock.
|[IOCTL_SPB_UNLOCK_CONNECTION](#ioctl-spb-unlock-connection) | The I/O control code is used by a client (peripheral driver) to release the connection lock on an SPB-connected target device that is shared with another client. The client previously sent an IOCTL_SPB_LOCK_CONNECTION request to acquire exclusive access to the device.|
|[IOCTL_SPB_UNLOCK_CONTROLLER](#ioctl-spb-unlock-controller) |The IOCTL_SPB_UNLOCK_CONTROLLER I/O control code is used by a client (peripheral driver) to unlock the SPB controller. The client previously locked the controller to gain exclusive use of the bus to access a target device on the bus.|

## <a href='#ioctl-spb-execute-sequence' id='ioctl-spb-execute-sequence'>IOCTL_SPB_EXECUTE_SEQUENCE</a>

The IOCTL_SPB_EXECUTE_SEQUENCE I/O control code enables a client (peripheral driver) of the SPB controller driver to perform a sequence of transfers (reads and writes) as a single, atomic operation with one I/O request. The designated device on the bus is the target for all transfers in the sequence.

By specifying a sequence of fixed-length transfers as a single, atomic operation, the IOCTL_SPB_EXECUTE_SEQUENCE I/O control request enables the controller driver to optimize the I/O transfers and improve performance.

The client sends this I/O control request to the file object for the target device.

An SPB controller driver registers an EvtSpbControllerIoSequence callback function to perform the bus transfers for an I/O transfer sequence. The SPB framework extension (SpbCx) calls this function to pass an IOCTL_SPB_EXECUTE_SEQUENCE request to the SPB controller driver for processing.

### Input Buffer
The input buffer is an SPB_TRANSFER_LIST structure, which contains a list of pointers to the client's data buffers. This list contains a data buffer for each transfer (read or write) in the I/O transfer sequence.
### Input Buffer Length
The size of an SPB_TRANSFER_LIST structure.

### Status block
If the operation is successful, the controller driver sets the Status member to STATUS_SUCCESS, and sets the Information member to the total number of bytes transferred during the sequence.

This operation might fail for various reasons, which can include low resources, invalid client input, and device malfunction.

If the controller driver starts to process the I/O request, but an error occurs during one of the transfers in the sequence (for example, the target device signals a NACK to decline the transfer), the controller driver aborts the remaining transfers in the sequence. The driver then sets the completion status to STATUS_SUCCESS, sets the Information member to the number of bytes that were successfully transferred before the error occurred, and completes the request.

## <a href='#ioctl-spb-full-duplex' id='ioctl-spb-full-duplex'>IOCTL_SPB_FULL_DUPLEX control code</a>

The IOCTL_SPB_FULL_DUPLEX control code is used by a client (peripheral driver) to request a full-duplex I/O operation. Full-duplex I/O operations are supported by controllers for buses such as SPI that can simultaneously read and write data.
The system-supplied CTL_CODE macro, which is described in Defining I/O Control Codes, is used to define IOCTL_SPB_FULL_DUPLEX as follows.

The user-mode driver or kernel-mode driver for a device on the bus sends this I/O control request to the file object for the target device.

This IOCTL is supported only by SPB controller drivers for buses, such as SPI, that can read and write data simultaneously.

The write and read buffers for the full-duplex transfer are described by an SPB_TRANSFER_LIST structure. This structure must use the following format:
- The array of SPB_TRANSFER_LIST_ENTRY structures contains exactly two elements. The first element describes the write buffer (Direction = SpbTransferDirectionToDevice). The second element describes the read buffer (Direction = SpbTransferDirectionFromDevice).
- The DelayInUs members of the two SPB_TRANSFER_LIST_ENTRY structures must be zero.
  The buffer formats for the write buffer and read buffer can be any of the following:
  -    SpbTransferBufferFormatSimple
  -    SpbTransferBufferFormatList
  -    SpbTransferBufferFormatSimpleNonPaged
  -    SpbTransferBufferFormatMdl
  The last two formats in the preceding list can be used only by kernel-mode clients. The formats for the write and read buffers are not required to be the same. For more information about these buffer formats, see SPB_TRANSFER_BUFFER_FORMAT.

A successful operation might set the Information member to a value that is less than the sum of the sizes of the write buffer and read buffer, which can occur if the request is canceled, or if the operation cannot write the full contents of the write buffer to the device, or completely fill the read buffer with data read from the device.

The write and read buffer sizes are not required to be the same. If the write buffer is larger than the read buffer, the operation continues to write data from the write buffer after the read buffer is full. If the read buffer is larger than the write buffer, the operation continues to fill the read buffer after the write buffer is emptied.

If an SPB controller driver registers an EvtSpbControllerIoOther callback function, the SPB framework extension (SpbCx) calls this function to pass an IOCTL_SPB_FULL_DUPLEX request to the SPB controller driver for processing. SpbCx does not perform any parameter checking, transfer list validation, or other processing for an IOCTL_SPB_FULL_DUPLEX request.

For more information about how an SPB controller driver implements support for this IOCTL, see Handling IOCTL_SPB_FULL_DUPLEX Requests.

### Input Buffer
A pointer to an SPB_TRANSFER_LIST structure that contains pointers to the client's input and output data buffers. This structure contains a Transfers array of exactly two elements. The first element describes the buffer that contains the data to write to the device. The second element describes the buffer used to hold the data read from the device.
For more information about how an SPB controller driver implements a custom I/O control (IOCTL) request that uses SPB_TRANSFER_LIST structures to describe buffers, see Using the SPB_TRANSFER_LIST Structure for Custom IOCTLs.

### Input Buffer Length
The size of an SPB_TRANSFER_LIST structure.

### Status block
If the operation is successful, the controller driver sets the Status member to STATUS_SUCCESS, and sets the Information member to the total number of bytes transferred (bytes read plus bytes written) during the full-duplex operation.

This operation might fail for various reasons, which can include low resources, invalid client input, and device malfunction.


## <a href='#ioctl-spb-lock-connection' id='ioctl-spb-lock-connection'>IOCTL_SPB_LOCK_CONNECTION control code</a>

The IOCTL_SPB_LOCK_CONNECTION control code is used by a client (peripheral driver) to acquire the connection lock on an SPB-connected target device that is shared with another client. While a client holds the connection lock, this client has exclusive access to the device.
The system-supplied CTL_CODE macro, which is described in Defining I/O Control Codes, is used to define IOCTL_SPB_LOCK_CONNECTION as follows.

The IOCTL_SPB_LOCK_CONNECTION and IOCTL_SPB_UNLOCK_CONNECTION requests acquire and release the connection lock on a target device that is attached to a simple peripheral bus. Most clients do not use these I/O control requests. These requests are used only if two clients share access to the same target device. For more information, see SPB Connection Locks.

Two clients can open separate logical connections to the same target device and use the connection lock when either client requires exclusive access to the device. When one client holds the lock, I/O requests to the device from the second client are automatically deferred until the first client releases the lock.

A client can simultaneously hold a connection lock on the target device and a controller lock on the SPB controller. The IOCTL_SPB_LOCK_CONTROLLER and IOCTL_SPB_UNLOCK_CONTROLLER requests acquire and release the controller lock. The client must acquire the connection lock before acquiring the controller lock, and must release the controller lock before releasing the connection lock. A client uses a controller lock to perform an ordered set of bus transfers (read and write operations) as a single, atomic bus operation. For more information, see I/O Transfer Sequences.

A connection lock is automatically terminated if an IRP_MJ_CLEANUP request is sent to a target device while the connection is locked on the device. A cleanup request is sent to a target device when a client closes its file handle to the device.

### Status block
If the operation is successful, the Status member is set to STATUS_SUCCESS.

If the operation fails, the Status member is set to an appropriate error status code.

If the client already holds either the connection lock on the target device or the controller lock on the SPB controller, this operation fails with Status = STATUS_INVALID_DEVICE_REQUEST. This operation might fail for other reasons, which can include low resources, invalid client input, and device malfunction.

## <a href='#ioctl-spb-lock-controller' id='ioctl-spb-lock-controller'>IOCTL_SPB_LOCK_CONTROLLER control code</a>

The IOCTL_SPB_LOCK_CONTROLLER control code is used by a client (peripheral driver) to lock the SPB controller. While the controller is locked, the client has exclusive use of the bus to access the specified target device for the lock.
The system-supplied CTL_CODE macro, which is described in Defining I/O Control Codes, is used to define IOCTL_SPB_LOCK_CONTROLLER as follows.

To obtain exclusive use of the bus to access a target device, a client (peripheral driver) sends this IOCTL to the file object for the target. After this IOCTL completes, the controller is locked, and all I/O transfers (read or write) on the bus access the designated target. Between transfers, the controller keeps the target device selected but stops the clock.

The controller remains locked until the client sends an IOCTL_SPB_UNLOCK_CONTROLLER request to unlock the controller. When the client's sequence of transfers to or from the target device is completed, the client must unlock the controller so that the controller can process I/O requests for other targets on the bus.

A lock is automatically terminated if an IRP_MJ_CLEANUP request is sent to a target device while the controller is locked on the target. A cleanup request is sent to a target when a client closes its handle to the target.

SPB controllers are not required to support IOCTL_SPB_LOCK_CONTROLLER and IOCTL_SPB_UNLOCK_CONTROLLER requests, and peripheral device drivers should not assume that they are supported.

If an SPB controller driver registers an EvtSpbControllerLock callback function, the SPB framework extension (SpbCx) calls this function to pass an IOCTL_SPB_LOCK_CONTROLLER request to the SPB controller driver for processing.


### Status block
If the operation is successful, the Status member is set to STATUS_SUCCESS.
This IOCTL can return an error status for a number of reasons, including failure to configure the controller to operate in exclusive-access mode. In this mode, the controller keeps the target device selected so that it is the exclusive target for all I/O transfers on the bus. The controller remains in this mode until it is unlocked.

## <a href='#ioctl-spb-unlock-connection' id='#ioctl-spb-unlock-connection'>IOCTL_SPB_UNLOCK_CONNECTION control code</a>

The IOCTL_SPB_UNLOCK_CONNECTION I/O control code is used by a client (peripheral driver) to release the connection lock on an SPB-connected target device that is shared with another client. The client previously sent an IOCTL_SPB_LOCK_CONNECTION request to acquire exclusive access to the device.

The IOCTL_SPB_LOCK_CONNECTION and IOCTL_SPB_UNLOCK_CONNECTION requests acquire and release the connection lock on a target device that is attached to a simple peripheral bus. Most clients do not use these I/O control requests. These requests are used only if two clients share access to the same target device. For more information, see SPB Connection Locks.

After a client (peripheral driver) sends a IOCTL_SPB_LOCK_CONNECTION request to a target device on the bus, and the request successfully completes, the connection remains locked until the client sends an IOCTL_SPB_UNLOCK_CONNECTION request to unlock the connection.

The client sends an IOCTL_SPB_UNLOCK_CONNECTION request to release the connection lock to the target device when the client no longer requires exclusive access to the device. The connection must be unlocked so that the other client can access the device.

### Status block
If the operation is successful, the Status member is set to STATUS_SUCCESS.

If the operation fails, the Status member is set to an appropriate error status code. If the client does not hold the connection lock on the target device, or if the client still holds the connection lock on the SPB controller, this operation fails with Status = STATUS_INVALID_DEVICE_REQUEST. This operation might fail for other reasons, which can include low resources, invalid client input, and device malfunction.

## <a href='#ioctl-spb-unlock-controller' id='#ioctl-spb-unlock-controller'>IOCTL_SPB_UNLOCK_CONTROLLER control code</a>

The IOCTL_SPB_UNLOCK_CONTROLLER I/O control code is used by a client (peripheral driver) to unlock the SPB controller. The client previously locked the controller to gain exclusive use of the bus to access a target device on the bus.

After a client (peripheral driver) sends a IOCTL_SPB_LOCK_CONTROLLER I/O control request to a target device on the bus, the controller remains locked until the client sends an IOCTL_SPB_UNLOCK_CONTROLLER I/O control request to unlock the controller. The client sends these I/O control requests to the file object for the target device.

The client sends an IOCTL_SPB_UNLOCK_CONTROLLER request when it has completed a sequence of transfers on the bus and wants to release the target device. The controller must be unlocked so that it can process I/O requests for other targets on the bus.

SPB controllers are not required to support IOCTL_SPB_LOCK_CONTROLLER and IOCTL_SPB_UNLOCK_CONTROLLER requests, and peripheral device drivers should not assume that they are supported.

The SPB framework extension (SpbCx) calls an SPB controller driver's optional EvtSpbControllerUnlock callback function to pass an IOCTL_SPB_LOCK_CONTROLLER request to the SPB controller driver for processing.

## Status block
If the operation is successful, the Status member is set to STATUS_SUCCESS.
This IOCTL can fail only if it is sent by a client that does not have the controller locked for exclusive access to the designated target.

