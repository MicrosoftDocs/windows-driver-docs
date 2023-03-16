---
title: Serial IRP major function codes
description: Documents serial IRP major function codes
keywords: ["serial devices WDK", "serial drivers WDK", "Serial IRP codes"]
ms.date: 10/17/2018
---

# Serial IRP major function codes

This topic documents the serial IRP major function codes.

Header: Wdm.h (include Wdm.h or Ntddk.h)

## IRP_MJ_CREATE

The [IRP_MJ_CREATE](../kernel/irp-mj-create.md) request opens a serial device.

### When sent

A client must open a serial device before it can access the port or a device connected to the port.

### Input Parameters

None.

### Output parameters

None.

### I/O status block

The **Information** field is set to zero.

The **Status** field is set to one of the following values:

|Status value|Description|
|----|----|
|STATUS_SUCCESS|The serial device was successfully opened.|
|STATUS_ACCESS_DENIED|The device is already open.|
|STATUS_DELETE_PENDING|Serial is in the process of removing the device.|
|STATUS_INSUFFICIENT_RESOURCES|The device is not in a Plug and Play Started state, or the driver could not allocate an internal data structure.|
|STATUS_NOT_A_DIRECTORY|A serial device cannot be opened as a directory.|
|STATUS_PENDING|Serial queued the request for later processing.|
|STATUS_SHARED_IRQ_BUSY|The interrupt assigned to the device is in use by another open device.|

### Operation

A serial device must be opened before it can be used. A serial device is an exclusive device; only one file can be open on a port at any given time.

## IRP_MJ_DEVICE_CONTROL

The IRP_MJ_DEVICE_CONTROL request operates a serial port.

### When sent

A client uses device control requests to:

* Get information about the port
* Get and set registers
* Get and set operating modes

For a description of the device control requests supported by Serial, see the [ntddser.h](/windows-hardware/drivers/ddi/ntddser/) header.

### Input parameters

Request specific

### Output parameters

Request specific

### I/O status block

Request specific

### Operation

Request specific

## IRP_MJ_FLUSH_BUFFERS

The [IRP_MJ_FLUSH_BUFFER](../kernel/irp-mj-flush-buffers.md) request flushes the internal write buffer of a serial device.

### When sent

A client uses a flush request to determine when Serial has completed all write requests the client sent before the flush request.

### Input parameters

None.

### Output parameters

None.

### I/O status block

The **Information** member is set to zero.

The **Status** member is set to one of the following status values:

|Status value|Description|
|----|----|
|STATUS_SUCCESS|The request completed successfully.|
|STATUS_CANCELLED|A client canceled the request. Serial also cancels a request if a device error occurs and Serial is configured to cancel a request if there is a device error.|
|STATUS_DELETE_PENDING|The driver is in the process of removing the device.|
|STATUS_PENDING|Serial queued the request for later processing.|

### Operation

Serial queues and starts processing write and flush requests in the order in which the requests are received. Serial completes a flush request after it calls **IoCompleteRequest** for all write requests that it received before a flush request. *However, completion of the flush request does not indicate that all the previously started write requests are completed by other drivers in the device stack.* For example, a filter driver might still be processing a write request. A client must check that a write request is completed by all drivers in the device stack before the client attempts to free or reuse a write request's IRP.

## IRP_MJ_INTERNAL_DEVICE_CONTROL
The [IRP_MJ_INTERNAL_DEVICE_CONTROL](../kernel/irp-mj-internal-device-control.md) request sets internal operating modes on a serial device.

### When sent

A client uses internal device control requests to:

* Get and reset basic settings
* Control wait/wake operation

For a description of the internal device control requests, see the [ntddser.h](/windows-hardware/drivers/ddi/ntddser/) header.

### Input parameters

Request specific

### Output parameters

Request specific

### I/O status block

Request specific

### Operation

Request specific

## IRP_MJ_PNP

The [IRP_MJ_PNP](../kernel/irp-mj-pnp.md) request supports Plug and Play.

### When sent

The PnP Manager sends IRP_MJ_PNP requests to query devices and to start, stop, and remove devices.

### Input parameters

Request specific

### Output parameters

Request specific

### I/O status block

Request specific

### Operation

Serial supports the following Plug and Play requests:

* [IRP_MN_CANCEL_REMOVE_DEVICE](../kernel/irp-mn-cancel-remove-device.md)
* [IRP_MN_CANCEL_STOP_DEVICE](../kernel/irp-mn-cancel-stop-device.md)
* [IRP_MN_FILTER_RESOURCE_REQUIREMENTS](../kernel/irp-mn-filter-resource-requirements.md)
* [IRP_MN_QUERY_CAPABILITIES](../kernel/irp-mn-query-capabilities.md)
* [IRP_MN_QUERY_DEVICE_RELATIONS](../kernel/irp-mn-query-device-relations.md)
* [IRP_MN_QUERY_ID](../kernel/irp-mn-query-id.md)
* [IRP_MN_QUERY_PNP_DEVICE_STATE](../kernel/irp-mn-query-pnp-device-state.md)
* [IRP_MN_QUERY_REMOVE_DEVICE](../kernel/irp-mn-query-remove-device.md)
* [IRP_MN_QUERY_RESOURCE_REQUIREMENTS](../kernel/irp-mn-query-resource-requirements.md)
* [IRP_MN_QUERY_STOP_DEVICE](../kernel/irp-mn-query-stop-device.md)
* [IRP_MN_REMOVE_DEVICE](../kernel/irp-mn-remove-device.md)
* [IRP_MN_START_DEVICE](../kernel/irp-mn-start-device.md)
* [IRP_MN_STOP_DEVICE](../kernel/irp-mn-stop-device.md)
* [IRP_MN_SURPRISE_REMOVAL](../kernel/irp-mn-surprise-removal.md)

Serial sends all other Plug and Play requests down the device stack without further processing.

Serial performs the following Serial-specific processing for Plug and Play requests:

**IRP_MN_QUERY_ID** (type BusQueryHardwardIDs)

If a serial device is on a multiport ISA card, Serial appends the wide character string "*PNP0502" to the string of hardware IDs.

**IRP_MN_FILTER_RESOURCE_REQUIREMENTS**

Serial devices on a multiport ISA card share the same interrupt status register and the same interrupt.

For a description of the generic operation of Plug and Play requests, see [Plug and Play Minor IRPs](../kernel/plug-and-play-minor-irps.md).

## IRP_MJ_POWER

The [IRP_MJ_POWER](../kernel/irp-mj-power.md) request controls power management.

### When sent

The power manager uses power requests to query and set power states.

###  Input parameters

Request specific

### Output parameters

Request specific

### I/O status block

Request specific

### Operation

Serial supports the following power requests:

* [IRP_MN_QUERY_POWER](../kernel/irp-mn-query-power.md)
* [IRP_MN_SET_POWER](../kernel/irp-mn-set-power.md)

Serial sends all other power requests down the device stack to be completed by a lower-level driver.

Serial is the default power policy owner for a serial device stack that uses Serial as a function driver or a lower-level filter driver.

For more information about the generic operation of these requests, see [Rules for Handling Power IRPs](../kernel/calling-iocalldriver-versus-calling-pocalldriver.md).

## IRP_MJ_QUERY_INFORMATION

The [IRP_MJ_QUERY_INFORMATION](../kernel/irp-mj-query-information.md) request queries the end-of-file information for a serial device. 

### When sent

A client uses a query information request to obtain standard information and position information about a file opened on a serial device.

### Input parameters

The **Parameters.QueryFile.FileInformationClass** is set to **FileStandardInformation** or **FilePositionInformation**.

### Output parameters

|Parameter|Description|
|----|----|
|**FileStandardInformation**|The **AssociatedIrp.SystemBuffer** member points to a client-allocated FILE_STANDARD_INFORMATION structure that Serial uses to output standard information.|
|**FilePositionInformation**|The **AssociatedIrp.SystemBuffer** member points to a client-allocated FILE_POSITION_INFORMATION structure that Serial uses to output position information.|

### I/O status block

If the request is successful, the **Information** member is set to zero.

The **Status** member is set to one of the following status values:

|Status value|Description|
|----|----|
|STATUS_SUCCESS|The request completed successfully.|
|STATUS_CANCELLED|A client canceled the request. Serial also cancels a request if a device error occurs and Serial is configured to cancel a request if there is a device error.|
|STATUS_DELETE_PENDING|Serial is in the process of removing the device.|
|STATUS_INVALID_PARAMETER|The requested information is not supported.|
|STATUS_PENDING|Serial queued the request for later processing.|

### Operation

Serial supports requests of type **FileStandardInformation** and **FilePositionInformation**.

The standard file information is always set to zero or **FALSE**, as appropriate. The position information is always set to zero.

## IRP_MJ_READ

A [IRP_MJ_READ](../kernel/irp-mj-read.md) request transfers data from a serial device to a client.

### When sent

A client uses a read request whenever it reads data on a serial device.

### Input parameters

The **Parameters.Read.Length** member is set to the number of bytes to transfer to the client's read buffer.

### Output parameters

The **AssociatedIrp.SystemBuffer** member points to a client-allocated read buffer to which Serial copies data read on the serial device.

### I/O status block

The **Information** member is set to the number of bytes transferred to the client's read buffer.

The **Status** member is set to one of the following values:

|Status value|Description|
|----|----|
|STATUS_SUCCESS|The request completed successfully.|
|STATUS_CANCELLED|A client canceled the request. Serial also cancels a request if a device error occurs and Serial is configured to cancel a request if there is a device error.|
|STATUS_DELETE_PENDING|Serial is in the process of removing the device.|
|STATUS_PENDING|Serial queued the request for later processing.|
|STATUS_TIMEOUT|The time to complete the request exceeded the total time-out value or the interval time-out value.|

### Operation

A client can use time-out events to terminate a read request. Note, however, that when a serial device is opened, the time-out settings for the device are undefined. A kernel-mode client can use an [IOCTL_SERIAL_INTERNAL_BASIC_SETTINGS](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_internal_basic_settings) to set time-out parameters to zero (no time-out events are used). User-mode and kernel-mode clients can use an [IOCTL_SERIAL_SET_TIMEOUTS](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_timeouts) request to set time-out parameters. 

For more information about read and write time-outs, see [Setting Read and Write Timeouts for a Serial Device](/previous-versions/ff547486(v=vs.85)).

## IRP_MJ_SET_INFORMATION

The [IRP_MJ_SET_INFORMATION](../kernel/irp-mj-shutdown.md) request sets the end-of-file information about a serial device.

### When sent

A client uses a set information request to change the current end-of-file position of a file opened on a serial device.

### Input parameters
The **Parameters.SetFile.FileInformationClass** member is set to **FileEndOfFileInformation** or **FileAllocationInformation**.

### Output parameters

None.

### I/O status block

If the request is successful, the **Information** member is set to zero.

The **Status** member is set to one of the following status values:

|Status value|Description|
|----|----|
|STATUS_SUCCESS|The request completed successfully.|
|STATUS_CANCELLED|A client canceled the request. Serial also cancels a request if a device error occurs and Serial is configured to cancel a request if there is a device error.|
|STATUS_DELETE_PENDING|Serial is in the process of removing the device.|
|STATUS_INVALID_PARAMETER|The specified end-of-file information is not supported.|
|STATUS_PENDING|Serial queued the request for later processing.|

### Operation

Serial supports requests of type **FileEndOfFileInformation** and **FileAllocationInformation**. However, Serial does not actually set file information. The end-of-file position is always set to zero.

## IRP_MJ_SYSTEM_CONTROL

The [IRP_MJ_SYSTEM_CONTROL](../kernel/irp-mj-system-control.md) request supports WMI requests.

### When sent

A WMI kernel-mode component can send an IRP_MJ_SYSTEM_CONTROL request any time after Serial registers as a WMI provider for a serial device. WMI IRPs typically are sent when a user-mode data consumer has requested WMI data.

### Input parameters

Request specific

### Output parameters

Request specific

### I/O status block

For WMI requests, Serial sets the Status field to one of the following values:

|Status value|Description|
|----|----|
|STATUS_SUCCESS|The request completed successfully.|
|STATUS_BUFFER_TOO_SMALL|The size, in bytes, of the output buffer is less than the required size of the requested information.|
|STATUS_INSUFFICIENT_RESOURCES|There were insufficient system resources to save the serial port name.|
|STATUS_INVALID_DEVICE_REQUEST|The request is not valid.|
|STATUS_WMI_GUID_NOT_FOUND|The WMI GUID is not supported.|

### Operation

Serial uses [WmiSystemControl](/windows-hardware/drivers/ddi/wmilib/nf-wmilib-wmisystemcontrol) to handle WMI system control requests. Serial registers the following types of WMI library callback routines, which **WmiSystemControl** calls to handle WMI requests sent to a device:

* [DpWmiQueryReginfo](/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_query_reginfo_callback)
* [DpWmiQueryDataBlock](/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_query_datablock_callback)
* [DpWmiSetDataBlock](/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_set_datablock_callback)
* [DpWmiSetDataItem](/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_set_dataitem_callback)

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

## IRP_MJ_WRITE

An [IRP_MJ_WRITE](../kernel/irp-mj-write.md) request transfers data from a client to a serial device.

### When sent

A client uses a write request whenever it writes data to a serial device.

### Input parameters

The **Parameters.Write.Length** member is set to the number of bytes to copy from a client-allocated write buffer to a serial device.

The **AssociatedIrp.SystemBuffer** member points to a client-allocated write buffer from which Serial copies data to the serial device.

### Output parameters

None.

### I/O status block

The *Information* member is set to the number of bytes actually copied from the client's write buffer to the serial device.

The *Status* member is set to one of the following values:

|Status value|Description|
|----|----|
|STATUS_SUCCESS|The request completed successfully.|
|STATUS_CANCELLED|A client canceled the request. Serial also cancels a request if a device error occurs and Serial is configured to cancel a request if there is a device error.|
|STATUS_DELETE_PENDING|Serial is in the process of removing the device.|
|STATUS_PENDING|Serial queued the request for later processing.|
|STATUS_TIMEOUT|The total time allowed for the write request was exceeded.|

### Operation

A client can use time-out events to terminate a write request. Note, however, that when a serial device is opened, the time-out events set on a device are undefined. A kernel-mode client can use an [IOCTL_SERIAL_INTERNAL_BASIC_SETTINGS](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_internal_basic_settings) to set time-out parameters to zero (no time-out events are used) and an [IOCTL_SERIAL_SET_TIMEOUTS](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_timeouts) request to set time-out parameters. For more information about read and write time-outs, see [Setting Read and Write Timeouts for a Serial Device](/previous-versions/ff547486(v=vs.85)).

## Related topics

[Plug and Play Minor IRPs](../kernel/plug-and-play-minor-irps.md)

[Rules for Handling Power IRPs](../kernel/calling-iocalldriver-versus-calling-pocalldriver.md)

[Serial Controller Driver Design Guide](./index.md)
