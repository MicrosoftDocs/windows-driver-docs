---
title: Device-specific operations for I/O requests for parallel devices
description: Documents device-specific operations for I/O requests for parallel devices
keywords: ["Parallel devices WDK", "Parallel drivers WDK", "Parallel IRP codes"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Device-specific operations for I/O requests for parallel devices
This topic documents the following device-specific operations for I/O requests for parallel devices

* [IRP_MJ_CREATE](#irp_mj_create)
* [IRP_MJ_DEVICE_CONTROL](#irp_mj_device_control)
* [IRP_MJ_INTERNAL_DEVICE_CONTROL](#irp_mj_internal_device_control)
* [IRP_MJ_QUERY_INFORMATION](#irp_mj_query_information)
* [IRP_MJ_READ](#irp_mj_read)
* [IRP_MJ_WRITE](#irp_mj_write)


##  IRP_MJ_CREATE
The [IRP_MJ_CREATE](https://msdn.microsoft.com/library/windows/hardware/ff550729) request opens a parallel device.

### When Sent
A client must use an [IRP_MJ_CREATE](https://msdn.microsoft.com/library/windows/hardware/ff550729) request to open a parallel device before it can access the device.

### Input Parameters
None.

### Output Parameters
None.

### I/O Status Block
The Information member is set to zero.

The Status member is set to one of the following values:


STATUS_SUCCESS 

The device was opened successfully.

STATUS_ACCESS_DENIED 

The device is already open.

STATUS_DELETE_PENDING 

The device is in a Plug and Play surprised-removed state.

STATUS_DEVICE_REMOVED 

The device has been removed.

STATUS_INVALID_DEVICE_REQUEST 

There is no hardware present.

STATUS_NOT_A_DIRECTORY 

The device is not a directory.

### Operation
A parallel device is an exclusive device. If a parallel device is open, the system-supplied bus driver for parallel ports fails any subsequent [IRP_MJ_CREATE](https://msdn.microsoft.com/library/windows/hardware/ff550729) requests for the device until the device has been closed. A client must open a parallel device before it sends other I/O requests to the device or calls the [parallel device callback routines](https://msdn.microsoft.com/library/windows/hardware/ff544275).

For more information, see [Opening and Using a Parallel Device](https://msdn.microsoft.com/windows/hardware/drivers/parports/opening-and-using-a-parallel-device).


##  IRP_MJ_DEVICE_CONTROL
The [IRP_MJ_DEVICE_CONTROL](https://msdn.microsoft.com/library/windows/hardware/ff550744) request operates a parallel device.

### When Sent
A client uses device control requests for the following types of operations:

* Obtain information about a device
* Set the operating mode of the device

See [Device Control Requests for Parallel Devices](https://msdn.microsoft.com/library/windows/hardware/ff543945).

### Input Parameters
Request-specific.

### Output Parameters
Request-specific.

### I/O Status Block
The **Information** member is request-specific. 

The **Status** member is set to a request-specific value or to one of following generic status values:


STATUS_SUCCESS
 
The request completed successfully.

STATUS_CANCELLED 

The request was canceled.

STATUS_DELETE_PENDING 

The device is in the process of being removed.

STATUS_DEVICE_REMOVED 

The device has been removed.

STATUS_INVALID_PARAMETER 

The system-supplied bus driver for parallel ports does not support the request.

STATUS_PENDING 

The request is pending.

STATUS_UNSUCCESSFUL 

The request did not complete successfully.

### Operation
The operation is request-specific.


##  IRP_MJ_INTERNAL_DEVICE_CONTROL
The [IRP_MJ_INTERNAL_DEVICE_CONTROL](https://msdn.microsoft.com/library/windows/hardware/ff550766) request sets internal operating modes on a parallel device.

### When Sent
A client uses internal device control requests for the following types of operations:

* Set the parallel port's communication mode to IEEE 1284-compatible
* Obtain connection information about a parallel port
* Lock and unlock a parallel port for exclusive use by the device

See Internal [Device Control Requests for Parallel Devices](https://msdn.microsoft.com/library/windows/hardware/ff543945).

### Input Parameters
Request-specific.

### Output Parameters
Request-specific.

### I/O Status Block
The **Information** member is request-specific. 

The **Status** member is set to a request-specific value or to one of following generic status values:


STATUS_SUCCESS
 
The request completed successfully.

STATUS_CANCELLED 

The request was canceled.

STATUS_DELETE_PENDING 

The device is in the process of being removed.

STATUS_DEVICE_REMOVED 

The device has been removed.

STATUS_INVALID_PARAMETER 

The parallel bus driver does not support the request.

STATUS_PENDING 

The request is pending.

STATUS_UNSUCCESSFUL 

The request did not complete successfully.

### Operation

The operation is request-specific.


##  IRP_MJ_QUERY_INFORMATION
The [IRP_MJ_QUERY_INFORMATION](https://msdn.microsoft.com/library/windows/hardware/ff550788) request obtains information about the file that represents the parallel device.

### When Sent
A client sends a query information request to determine the file size or current byte offset of the file pointer.

### Input Parameters
The **Parameters.QueryFile.FileInformationClass** member is set to **FileStandardInformation** or **FilePositionInformation**.


**FileStandardInformation** request:
 
The **AssociatedIrp.SystemBuffer** member points to a [FILE_STANDARD_INFORMATION](https://msdn.microsoft.com/library/windows/hardware/ff545855) structure that the client allocates for output of file information.

The **Parameters.QueryFile.Length** member is set to the size, in bytes, of a **FILE_STANDARD_INFORMATION** structure.

**FilePositionInformation** request: 

**AssociatedIrp.SystemBuffer** points to a [FILE_POSITION_INFORMATION](https://msdn.microsoft.com/library/windows/hardware/ff545848) structure that the client allocates for output of file information.

The **Parameters.SetFile.Length** member is set to the size, in bytes, of a **FILE_POSITION_INFORMATION** structure.

### Output Parameters
**AssociatedIrp.SystemBuffer** points to the requested information.

**FileStandardInformation** request type: 

Sets the following members in the **FILE_STANDARD_INFORMATION** structure:

* **AllocationSize.QuadPart** set to zero.
* **EndOfFile** is set to the value of the **AllocationSize** member.
* **NumberOfLinks** is set to zero.
* **DeletePending** is set to **FALSE**.
* **Directory** is set to **FALSE**.

**FilePositionInformation** request type:
 
Sets the **CurrentByteOffset.QuadPart** member of a **FILE_POSITION_INFORMATION** structure to zero.

### I/O Status Block
If the request succeeds, the **Information** member is set to the size, in bytes, of the structure associated with the type of request. Otherwise, the **Information** member is set to zero.

The **Status** member is set to one of the following status values:


STATUS_SUCCESS 

The request completed successfully.

STATUS_BUFFER_TOO_SMALL 

The size, in bytes, of the structure, specified by the input parameter, is less than the size, in bytes, of the structure associated with the request type.

STATUS_DEVICE_REMOVED 

The device has been removed.

STATUS_INVALID_PARAMETER 

The specified type of information is not valid.

### Operation
The system-supplied bus driver for parallel ports supports queries for the following types of information:

* **FileStandardInformation**
* **FilePositionInformation**


##  IRP_MJ_READ
The [IRP_MJ_READ](https://msdn.microsoft.com/library/windows/hardware/ff550794) request obtains input data from a parallel device.

### When Sent
A client uses an [IRP_MJ_READ](https://msdn.microsoft.com/library/windows/hardware/ff550794) request to obtain input from a parallel device.

### Input Parameters
The **Parameters.Read.Length** member points to the number of bytes to read from the parallel device.

### Output Parameters
The **AssociatedIrp.SystemBuffer** member points to a read buffer that the client allocates for the read data. The buffer must be large enough to hold the requested number of bytes.

### I/O Status Block
The **Information** member is set to the number of bytes actually read from the parallel device.

The **Status** member is set to one of the following status values:


STATUS_SUCCESS
 
The request completed successfully.

STATUS_DELETE_PENDING 

The device is in the process of being removed.

STATUS_CANCELLED 

The request was canceled.

STATUS_PENDING 

The request is queued on a work queue for the parallel device.

STATUS_INVALID_PARAMETER 

The **Parameters.Write.ByteOffset** member is not zero. Note that both read and write requests use this member.

STATUS_DEVICE_REMOVED 

The device has been removed.

### Operation
The system-supplied bus driver for parallel ports uses the read protocol set for the parallel device. The default read protocol is NIBBLE_MODE. A client can negotiate a read protocol by using an [IOCTL_IEEE1284_NEGOTIATE](https://msdn.microsoft.com/library/windows/hardware/ff543978) request.

The parallel port bus driver sets a cancel routine for the read request, marks the read request as pending, and queues the read request on a work queue. The read request is held in the work queue in a state that can be canceled until the read request is either completed or canceled by the client.

For more information, see [Reading and Writing a Parallel Device](https://msdn.microsoft.com/windows/hardware/drivers/parports/reading-and-writing-a-parallel-device).


##  IRP_MJ_WRITE
The [IRP_MJ_WRITE](https://msdn.microsoft.com/library/windows/hardware/ff550819) request transfers output data to a parallel device.

### When Sent
A client uses an [IRP_MJ_WRITE](https://msdn.microsoft.com/library/windows/hardware/ff550819) request whenever it transfers output data to a parallel device.

### Input Parameters
The **AssociatedIrp.SystemBuffer** points to a write buffer that the client allocates for write data. The buffer must be large enough to hold the requested number of bytes to write to the parallel device.

The **Parameters.Write.Length** member points to the number of bytes to write to the parallel device.

### Output Parameters
None.

### I/O Status Block
The **Information** member is set to the number of bytes actually written to the parallel device.

The **Status** member is set to one of the following values:

STATUS_SUCCESS
 
The request completed successfully.

STATUS_DELETE_PENDING 

The device is in the process of being removed.

STATUS_CANCELLED 

The request was canceled.

STATUS_PENDING 

The request is queued on a work queue for the parallel device.

STATUS_INVALID_PARAMETER 

The **Parameters.Write.ByteOffset** member is not zero.

STATUS_DEVICE_REMOVED 

The device has been removed.

### Operation
The system-supplied bus driver for parallel ports transfers data by using the write protocol that is set for the parallel device. The default write protocol is CENTRONICS. A client can negotiate a write protocol by using an [IOCTL_IEEE1284_NEGOTIATE](https://msdn.microsoft.com/library/windows/hardware/ff543978) request. 

The parallel port bus driver sets a cancel routine for the write request, marks the write request as pending, and queues the write request on a work queue. The write request is held in a state that can be canceled until the request is either completed or canceled.

For more information, see [Reading and Writing a Parallel Device](https://msdn.microsoft.com/windows/hardware/drivers/parports/reading-and-writing-a-parallel-device).

## Related topics

[Device Control Requests for Parallel Devices](https://msdn.microsoft.com/library/windows/hardware/ff543945).

[FILE_POSITION_INFORMATION](https://msdn.microsoft.com/library/windows/hardware/ff545848) [FILE_STANDARD_INFORMATION](https://msdn.microsoft.com/library/windows/hardware/ff545855)

[Opening and Using a Parallel Device](https://msdn.microsoft.com/windows/hardware/drivers/parports/opening-and-using-a-parallel-device)

[Operating a Parallel Device Attached to a Parallel Port](https://msdn.microsoft.com/windows/hardware/drivers/parports/operating-a-parallel-device-attached-to-a-parallel-port.md)

[Parallel device callback routines](https://msdn.microsoft.com/library/windows/hardware/ff544275)

[Reading and Writing a Parallel Device](https://msdn.microsoft.com/windows/hardware/drivers/parports/reading-and-writing-a-parallel-device)

