---
title: Converting an Existing SCSI Class Driver for Plug and Play
description: Converting an Existing SCSI Class Driver for Plug and Play
keywords:
- storage class drivers WDK , converting SCSI class drivers
- class drivers WDK storage , converting SCSI class drivers
- storage class drivers WDK , PnP
- class drivers WDK storage , PnP
- PnP WDK storage
- Plug and Play WDK storage
- converting SCSI class drivers
ms.date: 04/20/2017
---

# Converting an Existing SCSI Class Driver for Plug and Play


## <span id="ddk_converting_an_existing_scsi_class_driver_for_plug_and_play_kg"></span><span id="DDK_CONVERTING_AN_EXISTING_SCSI_CLASS_DRIVER_FOR_PLUG_AND_PLAY_KG"></span>


To run successfully as a PnP driver, an existing SCSI class driver must be modified as follows:

-   Driver initialization code must follow the rules for initialization of a Plug and Play driver. Functionality in the **DriverEntry** routine of an existing SCSI driver is divided among the **DriverEntry**, *AddDevice*, and *DispatchPnP* routines of a storage class driver, as described in [Storage Class Driver's DriverEntry Routine](storage-class-driver-s-driverentry-routine.md), [Storage Class Driver's AddDevice Routine](storage-class-driver-s-adddevice-routine.md), and [Handling PnP Start in a Storage Class Driver](handling-pnp-start-in-a-storage-class-driver.md).

-   Code that builds SRBs must not set **PathId**, **TargetId**, and **Lun** fields to a target device address, and should initialize these fields to 0xFF. The device address is implicit in the PDO that represents a device and the driver must communicate only with such a device object, so it is unnecessary for the class driver to provide the device address.

-   Code that gets SCSI inquiry and capabilities data by issuing [**IOCTL\_SCSI\_GET\_INQUIRY\_DATA**](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_get_inquiry_data) and [**IOCTL\_SCSI\_GET\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_get_capabilities) requests should issue [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_query_property) requests to retrieve device and adapter descriptors instead.

-   The driver must handle PnP requests to start, stop, and remove the device, and must have a mechanism to fail such a request if handling it would interfere with data transfers or system operations. For example, a driver should fail a query-remove, query-stop, or stop request if its device contains a system page file. Such a driver should handle paging notification requests (IRP\_MJ\_PNP with [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](../kernel/irp-mn-device-usage-notification.md) and notification type of **DeviceUsageTypePaging**) to maintain the count of page files on its device.

-   The driver must handle requests to change the power state of the device (IRP\_MJ\_POWER with [**IRP\_MN\_QUERY\_POWER**](../kernel/irp-mn-query-power.md) and [**IRP\_MN\_SET\_POWER**](../kernel/irp-mn-set-power.md)), and must block I/O to the device during power state transitions.

 

