---
title: Passing PnP IRPs Down the Device Stack
description: Passing PnP IRPs Down the Device Stack
keywords: ["PnP WDK kernel , passing IRPs down device stack", "Plug and Play WDK kernel , passing IRPs down device stack", "IRPs WDK PnP", "I/O request packets WDK PnP", "passing IRPs down device stack WDK", "IoCompletion routine"]
ms.date: 06/16/2017
---

# Passing PnP IRPs Down the Device Stack





The PnP manager uses IRPs to direct drivers to start, stop, and remove devices and to query drivers about their devices. All PnP IRPs have the major function code [**IRP\_MJ\_PNP**](./irp-mj-pnp.md), and all PnP drivers must provide a [*DispatchPnP*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine to service this function code. The PnP manager initializes **Irp-&gt;IoStatus.Status** to STATUS\_NOT\_SUPPORTED when it sends an IRP. For more information, see [DispatchPnP Routines](dispatchpnp-routines.md).

For a list of PnP minor IRPs, see [Plug and Play Minor IRPs](plug-and-play-minor-irps.md).

All drivers for a device must have the opportunity to respond to a PnP IRP unless a driver in the stack fails the IRP. (See the following figure.)

![diagram illustrating passing a plug and play irp down the device stack.](images/passpnp.png)

No single driver for a device can assume that it is the only driver that will respond to a PnP IRP. Consider, for example, a function driver that responds to an [**IRP\_MN\_QUERY\_CAPABILITIES**](./irp-mn-query-capabilities.md) request and completes the IRP without passing it to the next-lower driver. None of the capabilities supported by lower drivers, such as a unique instance ID or power management capabilities supported by the parent bus driver, is reported.

A PnP IRP travels back up the device stack when the parent bus driver calls [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) and the I/O manager calls any [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routines registered by the function driver or filter drivers.

A function or filter driver must do the following when it receives a PnP IRP:

-   If the driver performs actions in response to the IRP:
    1.  Perform the appropriate actions.
    2.  Set **Irp-&gt;IoStatus.Status** to an appropriate status, such as STATUS\_SUCCESS. Set **Irp-&gt;IoStatus.Information**, if appropriate for the IRP.
    3.  Set up the next stack location with [**IoSkipCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioskipcurrentirpstacklocation) or [**IoCopyCurrentIrpStackLocationToNext**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocopycurrentirpstacklocationtonext). Call the latter routine if you set an *IoCompletion* routine.
    4.  Set an *IoCompletion* routine, if necessary.
    5.  Do not complete the IRP. (Do not call **IoCompleteRequest**.) The parent bus driver will complete the IRP.
-   If the driver does not perform actions for this IRP, it simply prepares to pass the IRP to the next driver:
    1.  Call **IoSkipCurrentIrpStackLocation** to remove its stack location from the IRP.
    2.  Do not set any fields in **Irp-&gt;IoStatus**.
    3.  Do not set an *IoCompletion* routine.
    4.  Do not complete the IRP. (Do not call **IoCompleteRequest**.) The parent bus driver will complete the IRP.

If a function or filter driver did not fail the IRP, it passes the IRP to the next-lower driver with [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver). A driver has a pointer to the next-lower driver; that pointer was returned from the [**IoAttachDeviceToDeviceStack**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack) call in the higher driver's [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine.

The parent bus driver completes the IRP after performing any tasks to respond to the IRP. After the bus driver calls **IoCompleteRequest**, the I/O manager calls any *IoCompletion* routines registered by the function or filter drivers for the device.

 

