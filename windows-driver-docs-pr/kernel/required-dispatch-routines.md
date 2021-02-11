---
title: Required Dispatch Routines
description: Required Dispatch Routines
keywords: ["dispatch routines WDK kernel , required", "required dispatch routines WDK kernel"]
ms.date: 12/06/2018
ms.localizationpriority: medium
---

# Required Dispatch Routines

Most drivers must handle the following *Dispatch* routines:

-   [*DispatchPnP*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

    [**IRP\_MJ\_PNP**](./irp-mj-pnp.md) indicates a request involving PnP device recognition, hardware configuration, or resource allocation. Such requests are typically sent to a device driver from the PnP manager or from a closely coupled higher-level driver.

-   [*DispatchPower*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

    [**IRP\_MJ\_POWER**](./irp-mj-power.md) indicates a request pertaining to the power state of either the device or the system. Such requests are sent to the device driver by either the power manager or a closely coupled higher-level driver.

-   [*DispatchCreate*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

    [**IRP\_MJ\_CREATE**](./irp-mj-create.md) indicates either that a user-mode protected subsystem, possibly on behalf of an application or subsystem-specific driver, has requested a handle for the file object associated with the target device object, or that a higher-level driver is connecting or attaching its device object to the target device object.

-   [*DispatchClose*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

    [**IRP\_MJ\_CLOSE**](./irp-mj-close.md) indicates that the last handle of the file object that was associated the target device object has been closed and released. All I/O requests have been completed or canceled, so there are no outstanding references to the file object pointer.

-   [*DispatchRead*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

    [**IRP\_MJ\_READ**](./irp-mj-read.md) indicates an I/O request to transfer data from the underlying physical device to the system.

-   [*DispatchWrite*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

    [**IRP\_MJ\_WRITE**](./irp-mj-write.md) indicates an I/O request to transfer data from the system to the underlying physical device.

-   [*DispatchDeviceControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

    [**IRP\_MJ\_DEVICE\_CONTROL**](./irp-mj-device-control.md) indicates a request that contains a system-defined, device-type-specific I/O control code specifying a device type-specific operation. Higher-level drivers pass these IRPs on to their underlying device drivers, which typically process the request by accessing the device.

-   [*DispatchInternalDeviceControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

    [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](./irp-mj-internal-device-control.md) indicates a request sent to the device driver, in most cases from a closely coupled higher-level driver, usually with a privately defined, driver-specific and device-type-specific or device-specific I/O control code requesting a device-type-specific or device-specific operation.

    Only certain kinds of drivers are required to handle system-defined internal device I/O control requests, including certain SCSI drivers, keyboard or mouse device drivers, and parallel drivers that interoperate with system-supplied drivers.

-   [*DispatchSystemControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

    [**IRP\_MJ\_SYSTEM\_CONTROL**](./irp-mj-system-control.md) is used to specify WMI requests to drivers. For more information about WMI, see [Windows Management Instrumentation](implementing-wmi.md).

The dispatch routines that a driver must provide vary according to the type and functionality of the underlying physical device. For device-type-specific information about IRP major function codes that drivers must handle, see the device-type specific documentation in the Windows Driver Kit (WDK).

 

