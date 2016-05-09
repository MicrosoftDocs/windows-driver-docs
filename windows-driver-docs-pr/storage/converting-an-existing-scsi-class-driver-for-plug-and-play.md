---
title: Converting an Existing SCSI Class Driver for Plug and Play
description: Converting an Existing SCSI Class Driver for Plug and Play
ms.assetid: b6570eef-f425-4b73-aa8a-7084f53bb10a
keywords: ["storage class drivers WDK , converting SCSI class drivers", "class drivers WDK storage , converting SCSI class drivers", "storage class drivers WDK , PnP", "class drivers WDK storage , PnP", "PnP WDK storage", "Plug and Play WDK storage", "converting SCSI class drivers"]
---

# Converting an Existing SCSI Class Driver for Plug and Play


## <span id="ddk_converting_an_existing_scsi_class_driver_for_plug_and_play_kg"></span><span id="DDK_CONVERTING_AN_EXISTING_SCSI_CLASS_DRIVER_FOR_PLUG_AND_PLAY_KG"></span>


To run successfully as a PnP driver, an existing SCSI class driver must be modified as follows:

-   Driver initialization code must follow the rules for initialization of a Plug and Play driver. Functionality in the **DriverEntry** routine of an existing SCSI driver is divided among the **DriverEntry**, *AddDevice*, and *DispatchPnP* routines of a storage class driver, as described in [Storage Class Driver's DriverEntry Routine](storage-class-driver-s-driverentry-routine.md), [Storage Class Driver's AddDevice Routine](storage-class-driver-s-adddevice-routine.md), and [Handling PnP Start in a Storage Class Driver](handling-pnp-start-in-a-storage-class-driver.md).

-   Code that builds SRBs must not set **PathId**, **TargetId**, and **Lun** fields to a target device address, and should initialize these fields to 0xFF. The device address is implicit in the PDO that represents a device and the driver must communicate only with such a device object, so it is unnecessary for the class driver to provide the device address.

-   Code that gets SCSI inquiry and capabilities data by issuing [**IOCTL\_SCSI\_GET\_INQUIRY\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff560509) and [**IOCTL\_SCSI\_GET\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff560502) requests should issue [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff560590) requests to retrieve device and adapter descriptors instead.

-   The driver must handle PnP requests to start, stop, and remove the device, and must have a mechanism to fail such a request if handling it would interfere with data transfers or system operations. For example, a driver should fail a query-remove, query-stop, or stop request if its device contains a system page file. Such a driver should handle paging notification requests (IRP\_MJ\_PNP with [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff550841) and notification type of **DeviceUsageTypePaging**) to maintain the count of page files on its device.

-   The driver must handle requests to change the power state of the device (IRP\_MJ\_POWER with [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699) and [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744)), and must block I/O to the device during power state transitions.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Converting%20an%20Existing%20SCSI%20Class%20Driver%20for%20Plug%20and%20Play%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




