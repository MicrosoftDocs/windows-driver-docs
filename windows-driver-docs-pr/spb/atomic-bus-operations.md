---
title: Atomic Bus Operations
description: To use certain hardware capabilities of an SPB-connected peripheral device, a client of the SPB controller (that is, a peripheral driver) might need to perform a sequence of data transfers to and from the device as an atomic bus operation.
ms.assetid: F8CD670F-C817-40BF-AF4B-5F3839E46EFB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Atomic Bus Operations


To use certain hardware capabilities of an SPB-connected peripheral device, a client of the SPB controller (that is, a peripheral driver) might need to perform a sequence of data transfers to and from the device as an atomic bus operation. The transfer sequence is atomic because no other client can transfer data to or from a device on the bus until the sequence finishes.

The typical way for a client to perform a transfer sequence as an atomic bus operation is to send an [**IOCTL\_SPB\_EXECUTE\_SEQUENCE**](https://msdn.microsoft.com/library/windows/hardware/hh450857) request to the target device. In this request, the client specifies the sequence as a list of simple read and write transfers. The list can be of arbitrary length. The reads and writes are performed in the order in which they are listed, and each read or write can transfer an arbitrary number of bytes. Most SPB controllers support **IOCTL\_SPB\_EXECUTE\_SEQUENCE** requests.

## SPB controller locks


A less common way to perform an atomic transfer sequence is to use an SPB controller lock. A client sends an [**IOCTL\_SPB\_LOCK\_CONTROLLER**](https://msdn.microsoft.com/library/windows/hardware/hh450858) request to acquire the lock, and an [**IOCTL\_SPB\_UNLOCK\_CONTROLLER**](https://msdn.microsoft.com/library/windows/hardware/hh450859) request to release the lock. When a client holds the controller lock, any sequence of simple read and write ([**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) and [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819)) requests that the client sends to the device are performed as an atomic operation on the bus.

Most SPB-connected peripheral devices do not require controller locks, and most SPB controller drivers do not implement support for these locks. However, a few clients might need to use controller locks to access devices that have unusual features.

For example, a device might implement device functions that can be accessed only through read-modify-write operations that are atomic on the bus. To perform such an operation, the client sends the following four I/O requests (in the order shown):

1.  **IOCTL\_SPB\_LOCK\_CONTROLLER** – Acquire the controller lock.
2.  **IRP\_MJ\_READ** – Read a block of data from a target device.
3.  **IRP\_MJ\_WRITE** – Write the modified data back to the device.
4.  **IOCTL\_SPB\_UNLOCK\_CONTROLLER** – Release the controller lock.

After the read operation in the preceding list, the client interprets the data that was read from the device, and modifies the data before writing it back to the device.

However, few SPB-connected devices have features that require controller locks. For most devices that require atomic bus operations, [**IOCTL\_SPB\_EXECUTE\_SEQUENCE**](https://msdn.microsoft.com/library/windows/hardware/hh450857) requests are sufficient.

Do not confuse SPB controller locks with SPB connection locks. In the atypical case in which two clients share access to the same SPB-connected peripheral device, either client can use a connection lock to temporarily obtain exclusive access to the device. For more information, see [SPB Connection Locks](https://msdn.microsoft.com/library/windows/hardware/jj819326).

## Hardware bus signals


To handle an [**IOCTL\_SPB\_EXECUTE\_SEQUENCE**](https://msdn.microsoft.com/library/windows/hardware/hh450857) request, an SPB controller driver configures the controller hardware to generate the appropriate signals on the bus during the transfer sequence. Peripheral devices attached to the bus might rely on these signals to detect when an atomic bus operation is underway. The set of hardware signals that an SPB controller uses to perform a transfer sequence as an atomic bus operation depends on the bus type.

For an I²C bus, the controller starts a sequence by transmitting a start bit on the bus, and ends a sequence by transmitting a stop bit. Between the start and stop bits, the sequence of data transfers to and from the device are performed as a single, atomic bus operation. Except for the final transfer in the sequence, each transfer is followed by an I²C restart operation (a repeated start bit that is not preceded by a stop bit).

For an SPI bus, the controller starts a sequence by asserting the chip-select line to the target device, and ends the sequence by deasserting the chip-select line. By keeping the chip-select line continuously asserted during a sequence of data transfers over the bus, the transfers are performed as a single, atomic bus operation.

## An example I²C device


A typical peripheral device on an I²C bus might implement several internal device functions. To access some of these functions, a client might use [**IOCTL\_SPB\_EXECUTE\_SEQUENCE**](https://msdn.microsoft.com/library/windows/hardware/hh450857) requests.

For example, an I²C peripheral device might contain the following two internal registers:

-   A *function-address register* to which the client writes the internal address of the device function to access.
-   A *data register* through which the client reads data from or writes data to the specified function address.

The I²C peripheral device in this example interprets the first byte written to the device after a start bit to be a function address to load into the function-address register. Any additional bytes transferred to or from the device before the sequence ends (as indicated by the stop bit) are treated by the device as data to be transferred through the data register.

To perform a write operation, the client sends a write ([**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819)) request in which the first byte in the write buffer is the function address, and the remaining bytes in the buffer are data to be written to the function address.

Reading from the device is more complicated. Assume that the I²C device in this example supports a "fast read" feature that automatically resets the function-address register to its default value, 0, when a stop bit is detected on the bus. With this feature, the client can read the data from the function address 0 without first having to write to the function-address register. This feature can improve the speed of device read operations, especially if most reads are from function address 0 and are relatively short.

However, to read a block of data from a nonzero function address, the client still must write a byte to the function-address register before reading the data block from the data register. The client must perform these write and read transfers as an atomic bus operation to prevent the bus controller from transmitting a stop bit after the write to the function-address register and before the read from the data register. Otherwise, the stop bit will cause the data to be read from function address 0 instead of from the nonzero function address.

The following list describes the series of I/O requests that a client sends to the I²C device in this example to perform a read-modify-write operation on data located at a nonzero function address in the device:

1.  **IOCTL\_SPB\_EXECUTE\_SEQUENCE** - Perform an I/O transfer sequence to read data from the device. The first transfer in this sequence is a byte write to the function-address register. The second transfer in the sequence is a read of some number of bytes from the selected function address. These two transfers are performed atomically on the bus.
2.  **IRP\_MJ\_WRITE** - Write data to the device. The first byte in the write buffer for this request is the value to write to the function-address register. The remaining bytes in the buffer are data to write to the selected function address.

Other patterns of requests might be used instead to perform this read-modify-write operation. For example, the **IRP\_MJ\_WRITE** request in step 2 can be replaced by an **IOCTL\_SPB\_EXECUTE\_SEQUENCE** request that specifies two data transfers, both of which are writes. The first transfer in the sequence loads a byte into the function-address register. The second transfer writes the data bytes to the selected function address. This request, unlike the **IRP\_MJ\_WRITE** request in step 2, does not require the client to combine the function-address byte and data bytes in the same write buffer.

To perform a read-modify-write on function address 0 in this device, the **IOCTL\_SPB\_EXECUTE\_SEQUENCE** request in step 1 of the previous list can be replaced by a simple read ([**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794)) request.

 

 




