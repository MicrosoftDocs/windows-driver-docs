---
title: IRP Major Function Codes
description: IRP Major Function Codes
ms.date: 03/09/2020
ms.localizationpriority: medium
---

# IRP Major Function Codes


Each driver-specific I/O stack location ([**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)) for every [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) contains a major function code (IRP_MJ_XXX), which tells the driver what operation it or the underlying device driver should carry out to satisfy the I/O request. Each kernel-mode driver must provide dispatch routines for the major function codes that it must support.

The specific operations a driver carries out for a given **IRP\_MJ\_<em>XXX</em>** code depend somewhat on the underlying device, particularly for [**IRP\_MJ\_DEVICE\_CONTROL**](irp-mj-device-control.md) and [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](irp-mj-internal-device-control.md) requests. For example, the requests sent to a keyboard driver are necessarily somewhat different from those sent to a disk driver. However, the I/O manager defines the parameters and I/O stack location contents for each system-defined major function code.

Every higher-level driver must set up the appropriate I/O stack location in IRPs for the next-lower-level driver and call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver), either with each input IRP, or with a driver-created IRP (if the higher-level driver holds on to the input IRP). Consequently, every intermediate driver must supply a dispatch routine for each major function code that the underlying device driver handles. Otherwise, a new intermediate driver will "break the chain" whenever an application or still higher-level driver attempts to send an I/O request down to the underlying device driver.

File system drivers also handle a required subset of system-defined **IRP\_MJ\_<em>XXX</em>** function codes, some with subordinate **IRP\_MN\_<em>XXX</em>** function codes.

Drivers handle IRPs set with some or all of the following major function codes:

[**IRP\_MJ\_CLEANUP**](irp-mj-cleanup.md)

[**IRP\_MJ\_CLOSE**](irp-mj-close.md)

[**IRP\_MJ\_CREATE**](irp-mj-create.md)

[**IRP\_MJ\_DEVICE\_CONTROL**](irp-mj-device-control.md)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md)

[**IRP\_MJ\_FLUSH\_BUFFERS**](irp-mj-flush-buffers.md)

[**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](irp-mj-internal-device-control.md)

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)

[**IRP\_MJ\_POWER**](irp-mj-power.md)

[**IRP\_MJ\_QUERY\_INFORMATION**](irp-mj-query-information.md)

[**IRP\_MJ\_READ**](irp-mj-read.md)

[**IRP\_MJ\_SET\_INFORMATION**](irp-mj-set-information.md)

[**IRP\_MJ\_SHUTDOWN**](irp-mj-shutdown.md)

[**IRP\_MJ\_SYSTEM\_CONTROL**](irp-mj-system-control.md)

[**IRP\_MJ\_WRITE**](irp-mj-write.md)

The input and output parameters described in this section are the function-specific parameters in the IRP.

For more information about IRPs, see [Handling IRPs](./handling-irps.md).

 

