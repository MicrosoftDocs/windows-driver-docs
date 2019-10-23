---
title: When to Check the Driver's I/O Stack Location
description: When to Check the Driver's I/O Stack Location
ms.assetid: ca084221-7b07-4db0-a987-9dd8a66d169c
keywords: ["dispatch routines WDK kernel , I/O stack locations", "I/O stack locations WDK dispatch routines", "driver I/O stack locations WDK dispatch routines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# When to Check the Driver's I/O Stack Location





A major I/O function code is set in the driver's [I/O stack location](i-o-stack-locations.md) for each incoming IRP.

A driver's dispatch routine must check the driver's I/O stack location for the IRP to determine what to do if any of the following conditions hold:

-   The dispatch routine handles more than one major I/O function code.

-   The dispatch routine must handle a set of minor function codes for certain major function codes. IRPs with minor function codes include [**IRP\_MJ\_PNP**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-pnp) and [**IRP\_MJ\_POWER**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-power), as well as certain IRPs that the SCSI port driver and file system drivers must handle.

-   The dispatch routine of a device driver or of a closely coupled higher-level driver handles [**IRP\_MJ\_DEVICE\_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-device-control) or [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-internal-device-control) requests, which have an associated set of I/O control codes.

To get a pointer to a driver's I/O stack location, its dispatch routine calls [**IoGetCurrentIrpStackLocation**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation).

Higher-level drivers' dispatch routines always call **IoGetCurrentIrpStackLocation** and also call [**IoGetNextIrpStackLocation**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetnextirpstacklocation) to get a pointer to the next-lower driver's I/O stack location for IRPs that they set up for the next-lower driver, when [passing IRPs down the driver stack](passing-irps-down-the-driver-stack.md).

The [*DispatchDeviceControl*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine or [*DispatchInternalDeviceControl*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine of a device driver, or possibly of its closely coupled class driver(s), must determine which I/O control code is set in the driver's I/O stack location at **Parameters.DeviceIoControl.IoControlCode** for each request. The I/O control code is contained in the driver's I/O stack location.

In most cases, the *DispatchDeviceControl* or *DispatchInternalDeviceControl* routine of a higher-level driver simply passes an **IRP\_MJ\_DEVICE\_CONTROL** or **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** request on to the next-lower driver, after setting up its stack location in the IRP. However, SCSI class drivers must check for certain [SCSI Port I/O control codes](https://docs.microsoft.com/windows-hardware/drivers/ddi/index) so that they can set up the SCSI port driver's I/O stack location correctly before passing on these requests.

 

 




