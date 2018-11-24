---
title: SPB Connection Locks
description: Connection locks are useful for enabling two clients to share access to a target peripheral device on a simple peripheral bus (SPB).
ms.assetid: 073D9854-0F51-4518-A22B-0A0546694E30
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SPB Connection Locks


Connection locks are useful for enabling two clients to share access to a target peripheral device on a [simple peripheral bus](https://msdn.microsoft.com/library/windows/hardware/hh450903) (SPB). Both clients can open logical connections to the same target device and use the connection lock when either client requires exclusive access to the device to perform a series of I/O operations. When one client holds the connection lock, requests by the second client to access the device are automatically deferred until the first client releases the lock.

A client uses the [**IOCTL\_SPB\_LOCK\_CONNECTION**](https://msdn.microsoft.com/library/windows/hardware/jj819324) and [**IOCTL\_SPB\_UNLOCK\_CONNECTION**](https://msdn.microsoft.com/library/windows/hardware/jj819325) requests to acquire and release the connection lock on a target device on an SPB. A client sends these I/O control (IOCTL) requests to the file object for the device.

The driver for an SPB-connected peripheral device is typically either a User-Mode Driver Framework (UMDF) driver or Kernel-Mode Driver Framework (KMDF) driver. To send an IOCTL request to an SPB-connected peripheral device, a UMDF driver calls a method such as [**IWDFIoRequest::Send**](https://msdn.microsoft.com/library/windows/hardware/ff559149). A KMDF driver calls a method such as [**WdfIoTargetSendIoctlSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548660).

Typically, connection locks are unnecessary. Most client drivers always have exclusive access to a target device on an SPB. A connection lock is needed only in the relatively rare case in which two clients must share access to the same target device, and one or both clients must sometimes have exclusive access to the device for a series of I/O operations.

By default, if two clients share a target device, the [SPB framework extension](https://msdn.microsoft.com/library/windows/hardware/hh406203) (SpbCx) serializes I/O requests for the device according to the order in which they arrive in the SpbCx request queue. The connection lock overrides the default ordering of requests. After one client acquires the connection lock, SpbCx holds back I/O requests that it receives from the second client until the first client releases the lock.

In the current implementation of SpbCx, the primary use of connection locks is to enable the client driver for a target device to share access to the device with the ACPI driver, Acpi.sys. Acpi.sys is a system-supplied driver that manages certain core-resource devices on behalf of the ACPI firmware for the hardware platform. For example, a platform that uses a System on a Chip (SoC) might also contain a power management integrated circuit (PMIC) that is accessed by both Acpi.sys and a client driver.

A client driver is responsible for determining whether it requires a connection lock for I/O operations that require exclusive access to a target device. If a driver requires connection locks in some hardware platforms or platform configurations, but not in others, the driver developer and platform developer must agree on a driver-specific mechanism for determining when connection locks are to be used. Typically, information about whether to use connection locks is included in the platform firmware. For example, the vendor-defined information block in the ACPI resource descriptor for the device might contain a flag bit to indicate whether the driver shares the device with Acpi.sys.

## Connection lock example


A typical use of a connection lock is to implement an atomic read-modify-write operation. If two clients share access to the same target device on a simple peripheral bus (SPB), either client can use the connection lock to merge a read operation and a write operation into a single, atomic read-modify-write operation. The connection lock prevents the other client from accessing the target device between the read and write operations.

The following list describes the series of I/O requests that a client might send to an SPB-connected target device to perform a read-modify-write operation on the device:

1.  [**IOCTL\_SPB\_LOCK\_CONNECTION**](https://msdn.microsoft.com/library/windows/hardware/jj819324) – Acquire the connection lock on the target device.
2.  [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) – Read a block of data from the device address so that the client can interpret and modify the data.
3.  [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819) – Write the modified block of data to the device address.
4.  [**IOCTL\_SPB\_UNLOCK\_CONNECTION**](https://msdn.microsoft.com/library/windows/hardware/jj819325) – Release the connection lock on the target device.

The preceding list might be appropriate for a simple device that implements a single device function.

However, a more complex device might implement several device functions. This device might contain a function-address register that the client loads at the start of a data transfer. For this device, an [**IOCTL\_SPB\_EXECUTE\_SEQUENCE**](https://msdn.microsoft.com/library/windows/hardware/hh450857) request can combine the loading of the function-address register and the data transfer that follows into a single atomic bus operation. For more information, see the description of the example I²C device in [Atomic Bus Operations](https://msdn.microsoft.com/library/windows/hardware/jj850339).

## Comparison with controller locks


A client uses a connection lock to obtain exclusive access to a target device, but the connection lock does not prevent data transfers to or from other devices on the bus.

To perform a series of data transfers as an atomic bus operation, clients typically use an [**IOCTL\_SPB\_EXECUTE\_SEQUENCE**](https://msdn.microsoft.com/library/windows/hardware/hh450857) request. A less common way to perform an atomic bus operation is to use a controller lock. A client sends [**IOCTL\_SPB\_LOCK\_CONTROLLER**](https://msdn.microsoft.com/library/windows/hardware/hh450858) and [**IOCTL\_SPB\_UNLOCK\_CONTROLLER**](https://msdn.microsoft.com/library/windows/hardware/hh450859) requests to a acquire and release a controller lock.

Controller locks are distinct from connection locks. A controller lock enables a sequence of I/O transfers to and from a target device on the bus to be performed as a single, atomic bus operation. While the controller lock is in effect, transfers to or from other devices on the bus are deferred until the controller lock is released. For more information, see [Atomic Bus Operations](https://msdn.microsoft.com/library/windows/hardware/jj850339).

**Note**  In some implementations, a connection lock might, as a side effect, prevent transfers to other devices on the bus. However, this behavior is implementation-dependent and client drivers should not rely on it. In contrast, a controller lock reliably prevents another client from accessing the same target device as the client that holds the controller lock, and clients can safely depend on this behavior.

 

A client might need to acquire both a connection lock and a controller lock before performing a set of I/O operations on a target device. The connection lock prevents a second client that shares access to the same target device from performing I/O operations on the device, and the controller lock prevents clients for other devices on the bus from performing I/O operations on these other devices. (I/O operations that are prevented from occurring while these locks are held are simply deferred until the locks are released.)

When a client acquires both a connection lock and a controller lock for a target device on an SPB, the client must acquire the connection lock before acquiring the controller lock, and must release the controller lock before releasing the connection lock. After a client acquires a connection lock, the client can, if necessary, acquire and release the controller lock as many times as is necessary before the client releases the connection lock.

Nested acquisitions of a connection lock are illegal. After a client has acquired a connection lock, the client must not try to acquire the lock again until the client first releases the lock. Similarly, nested acquisitions of a controller lock are not allowed.

 

 




