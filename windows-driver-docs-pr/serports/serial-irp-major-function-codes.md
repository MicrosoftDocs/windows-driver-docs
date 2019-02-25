---
title: Serial IRP major function codes
description: Documents serial IRP major function codes
keywords: ["serial devices WDK", "serial drivers WDK", "Serial IRP codes"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Serial IRP major function codes
This topic documents the following serial IRP major function codes:

* [IRP_MJ_CREATE](#irp_mj_create)
* [IRP_MJ_DEVICE_CONTROL](#irp_mj_device_control)
* [IRP_MJ_FLUSH_BUFFERS](#irp_mj_flush_buffers)
* [IRP_MJ_INTERNAL_DEVICE_CONTROL](#irp_mj_internal_device_control)
* [IRP_MJ_PNP](#irp_mj_pnp)
* [IRP_MJ_POWER](#irp_mj_power)
* [IRP_MJ_QUERY_INFORMATION](#irp_mj_query_information)
* [IRP_MJ_READ](#irp_mj_read)
* [IRP_MJ_SET_INFORMATION](#irp_mj_set_information)
* [IRP_MJ_SYSTEM_CONTROL](#irp_mj_system_control)
* [IRP_MJ_WRITE](#irp_mj_write)

Header: Wdm.h (include Wdm.h or Ntddk.h)

##  IRP_MJ_CREATE
The [IRP_MJ_CREATE](https://msdn.microsoft.com/library/windows/hardware/ff550729) request opens a serial device.

### When Sent
A client must open a serial device before it can access the port or a device connected to the port.

### Input Parameters
None.

### Output Parameters
None.

### I/O Status Block
The **Information** field is set to zero. 

The **Status** field is set to one of the following values:


STATUS_SUCCESS

The serial device was successfully opened.

STATUS_ACCESS_DENIED 

The device is already open.

STATUS_DELETE_PENDING 

Serial is in the process of removing the device.

STATUS_INSUFFICIENT_RESOURCES 

The device is not in a Plug and Play Started state, or the driver could not allocate an internal data structure.

STATUS_NOT_A_DIRECTORY 

A serial device cannot be opened as a directory.

STATUS_PENDING 

Serial queued the request for later processing.

STATUS_SHARED_IRQ_BUSY 

The interrupt assigned to the device is in use by another open device.

### Operation
A serial device must be opened before it can be used. A serial device is an exclusive device; only one file can be open on a port at any given time.

##  IRP_MJ_DEVICE_CONTROL
The IRP_MJ_DEVICE_CONTROL request operates a serial port.

### When Sent
A client uses device control requests to do the following:

* Get information about the port
* Get and set registers
* Get and set operating modes

For a description of the device control requests supported by Serial, see [Serial Device Control Requests](https://msdn.microsoft.com/library/windows/hardware/ff547466).

### Input Parameters
Request specific

### Output Parameters
Request specific

### I/O Status Block
Request specific

### Operation
Request specific

##  IRP_MJ_FLUSH_BUFFERS
The [IRP_MJ_FLUSH_BUFFER](https://msdn.microsoft.com/library/windows/hardware/ff550760) request flushes the internal write buffer of a serial device.

### When Sent
A client uses a flush request to determine when Serial has completed all write requests the client sent before the flush request.

### Input Parameters
None.

### Output Parameters
None.

### I/O Status Block
The **Information** member is set to zero.

The **Status** member is set to one of the following status values:


STATUS_SUCCESS
 
The request completed successfully.

STATUS_CANCELLED 

A client canceled the request. Serial also cancels a request if a device error occurs and Serial is configured to cancel a request if there is a device error.

STATUS_DELETE_PENDING 

The driver is in the process of removing the device.

STATUS_PENDING 

Serial queued the request for later processing.

### Operation
Serial queues and starts processing write and flush requests in the order in which the requests are received. Serial completes a flush request after it calls **IoCompleteRequest** for all write requests that it received before a flush request. *However, completion of the flush request does not indicate that all the previously started write requests are completed by other drivers in the device stack.* For example, a filter driver might still be processing a write request. A client must check that a write request is completed by all drivers in the device stack before the client attempts to free or reuse a write request's IRP.


##  IRP_MJ_INTERNAL_DEVICE_CONTROL
The [IRP_MJ_INTERNAL_DEVICE_CONTROL](https://msdn.microsoft.com/library/windows/hardware/ff550766) request sets internal operating modes on a serial device.

### When Sent
A client uses internal device control requests to do the following:

* Get and reset basic settings
* Control wait/wake operation

For a description of the internal device control requests, see [Serial Internal Device Control Requests](https://msdn.microsoft.com/library/windows/hardware/ff547480).

### Input Parameters
Request specific

### Output Parameters
Request specific

### I/O Status Block
Request specific

### Operation
Request specific


##   IRP_MJ_PNP
The [IRP_MJ_PNP](https://msdn.microsoft.com/library/windows/hardware/ff550772) request supports Plug and Play. 

### When Sent
The PnP Manager sends IRP_MJ_PNP requests to query devices and to start, stop, and remove devices.

### Input Parameters
Request specific

### Output Parameters
Request specific

### I/O Status Block
Request specific

### Operation
Serial supports the following Plug and Play requests:

* [IRP_MN_CANCEL_REMOVE_DEVICE](https://msdn.microsoft.com/library/windows/hardware/ff550823)
* [IRP_MN_CANCEL_STOP_DEVICE](https://msdn.microsoft.com/library/windows/hardware/ff550826)
* [IRP_MN_FILTER_RESOURCE_REQUIREMENTS](https://msdn.microsoft.com/library/windows/hardware/ff550874)
* [IRP_MN_QUERY_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff551664)
* [IRP_MN_QUERY_DEVICE_RELATIONS](https://msdn.microsoft.com/library/windows/hardware/ff551670)
* [IRP_MN_QUERY_ID](https://msdn.microsoft.com/library/windows/hardware/ff551679)
* [IRP_MN_QUERY_PNP_DEVICE_STATE](https://msdn.microsoft.com/library/windows/hardware/ff551698)
* [IRP_MN_QUERY_REMOVE_DEVICE](https://msdn.microsoft.com/library/windows/hardware/ff551705)
* [IRP_MN_QUERY_RESOURCE_REQUIREMENTS](https://msdn.microsoft.com/library/windows/hardware/ff551715)
* [IRP_MN_QUERY_STOP_DEVICE](https://msdn.microsoft.com/library/windows/hardware/ff551725)
* [IRP_MN_REMOVE_DEVICE](https://msdn.microsoft.com/library/windows/hardware/ff551738)
* [IRP_MN_START_DEVICE](https://msdn.microsoft.com/library/windows/hardware/ff551749)
* [IRP_MN_STOP_DEVICE](https://msdn.microsoft.com/library/windows/hardware/ff551755)
* [IRP_MN_SURPRISE_REMOVAL](https://msdn.microsoft.com/library/windows/hardware/ff551760)

Serial sends all other Plug and Play requests down the device stack without further processing.

Serial performs the following Serial-specific processing for Plug and Play requests:


IRP_MN_QUERY_ID (type BusQueryHardwardIDs)
 
If a serial device is on a multiport ISA card, Serial appends the wide character string "*PNP0502" to the string of hardware IDs.

IRP_MN_FILTER_RESOURCE_REQUIREMENTS 

serial devices on a multiport ISA card share the same interrupt status register and the same interrupt.

For a description of the generic operation of Plug and Play requests, see [Plug and Play Minor IRPs](https://msdn.microsoft.com/library/windows/hardware/ff558807).

##  IRP_MJ_POWER
The [IRP_MJ_POWER](https://msdn.microsoft.com/library/windows/hardware/ff550784) request controls power management.

### When Sent
The power manager uses power requests to query and set power states.

###  Input Parameters
Request specific

### Output Parameters
Request specific

### I/O Status Block
Request specific

### Operation
Serial supports the following power requests:

* [IRP_MN_QUERY_POWER](https://msdn.microsoft.com/library/windows/hardware/ff551699)
* [IRP_MN_SET_POWER](https://msdn.microsoft.com/library/windows/hardware/ff551744)

Serial sends all other power requests down the device stack to be completed by a lower-level driver.

Serial is the default power policy owner for a serial device stack that uses Serial as a function driver or a lower-level filter driver.

For more information about the generic operation of these requests, see [Rules for Handling Power IRPs](https://msdn.microsoft.com/library/windows/hardware/ff563629).


##  IRP_MJ_QUERY_INFORMATION
The [IRP_MJ_QUERY_INFORMATION](https://msdn.microsoft.com/library/windows/hardware/ff550788) request queries the end-of-file information for a serial device. 

### When Sent
A client uses a query information request to obtain standard information and position information about a file opened on a serial device.

### Input Parameters
The **Parameters.QueryFile.FileInformationClass** is set to **FileStandardInformation** or **FilePositionInformation**.

### Output Parameters

**FileStandardInformation** 
The **AssociatedIrp.SystemBuffer** member points to a client-allocated FILE_STANDARD_INFORMATION structure that Serial uses to output standard information.

**FilePositionInformation** 
The **AssociatedIrp.SystemBuffer** member points to a client-allocated FILE_POSITION_INFORMATION structure that Serial uses to output position information.

### I/O Status Block
If the request is successful, the **Information** member is set to zero.

The **Status** member is set to one of the following status values:


STATUS_SUCCESS
 
The request completed successfully.

STATUS_CANCELLED 

A client canceled the request. Serial also cancels a request if a device error occurs and Serial is configured to cancel a request if there is a device error.

STATUS_DELETE_PENDING 

Serial is in the process of removing the device.

STATUS_INVALID_PARAMETER 

The requested information is not supported.

STATUS_PENDING 

Serial queued the request for later processing.

### Operation
Serial supports requests of type **FileStandardInformation** and **FilePositionInformation**.

The standard file information is always set to zero or **FALSE**, as appropriate. The position information is always set to zero.


##  IRP_MJ_READ
A [IRP_MJ_READ](https://msdn.microsoft.com/library/windows/hardware/ff550794) request transfers data from a serial device to a client.

### When Sent
A client uses a read request whenever it reads data on a serial device.

### Input Parameters
The **Parameters.Read.Length** member is set to the number of bytes to transfer to the client's read buffer.

### Output Parameters
The **AssociatedIrp.SystemBuffer** member points to a client-allocated read buffer to which Serial copies data read on the serial device.

### I/O Status Block
The **Information** member is set to the number of bytes transferred to the client's read buffer.

The **Status** member is set to one of the following values:


STATUS_SUCCESS 

The request completed successfully.

STATUS_CANCELLED 

A client canceled the request. Serial also cancels a request if a device error occurs and Serial is configured to cancel a request if there is a device error.

STATUS_DELETE_PENDING 

Serial is in the process of removing the device.

STATUS_PENDING 

Serial queued the request for later processing.

STATUS_TIMEOUT 

The time to complete the request exceeded the total time-out value or the interval time-out value.

### Operation
A client can use time-out events to terminate a read request. Note, however, that when a serial device is opened, the time-out settings for the device are undefined. A kernel-mode client can use an [IOCTL_SERIAL_INTERNAL_BASIC_SETTINGS](https://msdn.microsoft.com/library/windows/hardware/ff546626) to set time-out parameters to zero (no time-out events are used). User-mode and kernel-mode clients can use an [IOCTL_SERIAL_SET_TIMEOUTS](https://msdn.microsoft.com/library/windows/hardware/ff546772) request to set time-out parameters. 

For more information about read and write time-outs, see [Setting Read and Write Timeouts for a Serial Device](https://msdn.microsoft.com/library/windows/hardware/ff547486).


##  IRP_MJ_SET_INFORMATION
The [IRP_MJ_SET_INFORMATION](https://msdn.microsoft.com/library/windows/hardware/ff550807) request sets the end-of-file information about a serial device.

### When Sent
A client uses a set information request to change the current end-of-file position of a file opened on a serial device.

### Input Parameters
The **Parameters.SetFile.FileInformationClass** member is set to **FileEndOfFileInformation** or **FileAllocationInformation**.

### Output Parameters
None.

### I/O Status Block
If the request is successful, the **Information** member is set to zero.

The **Status** member is set to one of the following status values:


STATUS_SUCCESS 

The request completed successfully.

STATUS_CANCELLED 

A client canceled the request. Serial also cancels a request if a device error occurs and Serial is configured to cancel a request if there is a device error.

STATUS_DELETE_PENDING 

Serial is in the process of removing the device.

STATUS_INVALID_PARAMETER 

The specified end-of-file information is not supported.

STATUS_PENDING 

Serial queued the request for later processing.

### Operation
Serial supports requests of type **FileEndOfFileInformation** and **FileAllocationInformation**. However, Serial does not actually set file information. The end-of-file position is always set to zero.


##  IRP_MJ_SYSTEM_CONTROL
The [IRP_MJ_SYSTEM_CONTROL](https://msdn.microsoft.com/library/windows/hardware/ff550813) request supports WMI requests.

### When Sent
A WMI kernel-mode component can send an IRP_MJ_SYSTEM_CONTROL request any time after Serial registers as a WMI provider for a serial device. WMI IRPs typically are sent when a user-mode data consumer has requested WMI data.

### Input Parameters
Request specific

### Output Parameters
Request specific

### I/O Status Block
For WMI requests, Serial sets the Status field to one of the following values:


STATUS_SUCCESS 

The request completed successfully.

STATUS_BUFFER_TOO_SMALL 

The size, in bytes, of the output buffer is less than the required size of the requested information.

STATUS_INSUFFICIENT_RESOURCES 

There were insufficient system resources to save the serial port name.

STATUS_INVALID_DEVICE_REQUEST 

The request is not valid.

STATUS_WMI_GUID_NOT_FOUND 

The WMI GUID is not supported.

### Operation
Serial uses [WmiSystemControl](https://msdn.microsoft.com/library/windows/hardware/ff565834) to handle WMI system control requests. Serial registers the following types of WMI library callback routines, which **WmiSystemControl** calls to handle WMI requests sent to a device:

* [DpWmiQueryReginfo](https://msdn.microsoft.com/library/windows/hardware/ff544097)
* [DpWmiQueryDataBlock](https://msdn.microsoft.com/library/windows/hardware/ff544096)
* [DpWmiSetDataBlock](https://msdn.microsoft.com/library/windows/hardware/ff544104)
* [DpWmiSetDataItem](https://msdn.microsoft.com/library/windows/hardware/ff544108)

Serial does not support any other system control requests. For non-WMI requests, Serial skips the current stack location, and sends the request down the device stack.

Serial registers the WMI GUIDS described in the following table.

Serial WMI GUID Associated data structure 

| SERIAL_PORT_WMI_NAME_GUID | USHORT followed by a WCSTR |
| ------------------------- | -------------------------- |
| SERIAL_PORT_WMI_COMM_GUID | SERIAL_WMI_COMM_DATA |
| SERIAL_PORT_WMI_HW_GUID | SERIAL_WMI_HW_DATA |
| SERIAL_PORT_WMI_PERF_GUID | SERIAL_WMI_PERF_DATA |
| SERIAL_PORT_WMI_PROPERTIES_GUID | WMI_SERIAL_PORT_PROPERTIES |


The WMI name of a serial device is the value of the entry value **PortName** under the Plug and Play registry key for the device.


##  IRP_MJ_WRITE
An [IRP_MJ_WRITE](https://msdn.microsoft.com/library/windows/hardware/ff550819) request transfers data from a client to a serial device.

### When Sent
A client uses a write request whenever it writes data to a serial device.

### Input Parameters
The **Parameters.Write.Length** member is set to the number of bytes to copy from a client-allocated write buffer to a serial device.

The **AssociatedIrp.SystemBuffer** member points to a client-allocated write buffer from which Serial copies data to the serial device.

### Output Parameters
None.

### I/O Status Block
The *Information* member is set to the number of bytes actually copied from the client's write buffer to the serial device.

The *Status* member is set to one of the following values:


STATUS_SUCCESS 

The request completed successfully.

STATUS_CANCELLED 

A client canceled the request. Serial also cancels a request if a device error occurs and Serial is configured to cancel a request if there is a device error.

STATUS_DELETE_PENDING 

Serial is in the process of removing the device.

STATUS_PENDING 

Serial queued the request for later processing.

STATUS_TIMEOUT 

The total time allowed for the write request was exceeded.

### Operation
A client can use time-out events to terminate a write request. Note, however, that when a serial device is opened, the time-out events set on a device are undefined. A kernel-mode client can use an [IOCTL_SERIAL_INTERNAL_BASIC_SETTINGS](https://msdn.microsoft.com/library/windows/hardware/ff546626) to set time-out parameters to zero (no time-out events are used) and an [IOCTL_SERIAL_SET_TIMEOUTS](https://msdn.microsoft.com/library/windows/hardware/ff546772) request to set time-out parameters. For more information about read and write time-outs, see [Setting Read and Write Timeouts for a Serial Device](https://msdn.microsoft.com/library/windows/hardware/ff547486).

## Related topics

[Plug and Play Minor IRPs](https://msdn.microsoft.com/library/windows/hardware/ff558807)

[Rules for Handling Power IRPs](https://msdn.microsoft.com/library/windows/hardware/ff563629)

[Serial Controller Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/serports/index.md)

