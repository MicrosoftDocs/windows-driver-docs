---
title: IRP Major Function Codes
description: IRP Major Function Codes
ms.date: 03/13/2020
---

# IRP Major Function Codes

Each driver-specific I/O stack location ([**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)) for every [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) contains a major function code (**IRP_MJ_*XXX***), which tells the driver what operation it or the underlying device driver should carry out to satisfy the I/O request. Each kernel-mode driver must provide dispatch routines for the major function codes that it must support.

The specific operations a driver carries out for a given **IRP_MJ_*XXX*** code depend somewhat on the underlying device, particularly for [**IRP_MJ_DEVICE_CONTROL**](irp-mj-device-control.md) and [**IRP_MJ_INTERNAL_DEVICE_CONTROL**](irp-mj-internal-device-control.md) requests. For example, the requests sent to a keyboard driver are necessarily somewhat different from those sent to a disk driver. However, the I/O manager defines the parameters and I/O stack location contents for each system-defined major function code.

Every higher-level driver must set up the appropriate I/O stack location in IRPs for the next-lower-level driver and call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver), either with each input IRP, or with a driver-created IRP (if the higher-level driver holds on to the input IRP). Consequently, every intermediate driver must supply a dispatch routine for each major function code that the underlying device driver handles. Otherwise, a new intermediate driver will "break the chain" whenever an application or still higher-level driver attempts to send an I/O request down to the underlying device driver.

File system drivers and legacy file system filter drivers also handle a required subset of system-defined **IRP_MJ_*XXX*** function codes, some with subordinate **IRP_MN_*XXX*** function codes. For more information on how to handle these IRPs, see [IRP major function codes for file system drivers and legacy FS filter drivers](../ifs/irp-major-function-codes-fs-filters.md).

Drivers handle IRPs set with some or all of the following major function codes:

[**IRP_MJ_CLEANUP**](irp-mj-cleanup.md)

[**IRP_MJ_CLOSE**](irp-mj-close.md)

[**IRP_MJ_CREATE**](irp-mj-create.md)

[**IRP_MJ_DEVICE_CONTROL**](irp-mj-device-control.md)

[**IRP_MJ_FILE_SYSTEM_CONTROL**](irp-mj-file-system-control.md)

[**IRP_MJ_FLUSH_BUFFERS**](irp-mj-flush-buffers.md)

[**IRP_MJ_INTERNAL_DEVICE_CONTROL**](irp-mj-internal-device-control.md)

[**IRP_MJ_PNP**](irp-mj-pnp.md)

[**IRP_MJ_POWER**](irp-mj-power.md)

[**IRP_MJ_QUERY_INFORMATION**](irp-mj-query-information.md)

[**IRP_MJ_READ**](irp-mj-read.md)

[**IRP_MJ_SET_INFORMATION**](irp-mj-set-information.md)

[**IRP_MJ_SHUTDOWN**](irp-mj-shutdown.md)

[**IRP_MJ_SYSTEM_CONTROL**](irp-mj-system-control.md)

[**IRP_MJ_WRITE**](irp-mj-write.md)

The input and output parameters described in this section are the function-specific parameters in the IRP.

For more information about IRPs, see [Handling IRPs](./handling-irps.md).
