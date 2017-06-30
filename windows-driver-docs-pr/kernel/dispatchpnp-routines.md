---
title: DispatchPnP Routines
author: windows-driver-content
description: DispatchPnP Routines
ms.assetid: 909d99ac-5bd3-4b12-bfb4-79713cf2a156
keywords: ["dispatch routines WDK kernel , DispatchPnP routine", "DispatchPnP routine", "PnP dispatch routines WDK kernel", "IRPs WDK kernel , Plug and Play dispatch routines", "Plug and Play dispatch routines WDK kernel", "IRP_MJ_PNP I/O function code"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DispatchPnP Routines


## <a href="" id="ddk-dispatchpnp-routines-kg"></a>


A driver's [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine supports [Plug and Play](implementing-plug-and-play.md) by handling IRPs for the [**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772) I/O function code. Associated with the **IRP\_MJ\_PNP** function code are several minor I/O function codes (see [Plug and Play Minor IRPs](https://msdn.microsoft.com/library/windows/hardware/ff558807)), some of which all drivers must handle and some of which can be optionally handled. The PnP manager uses these minor function codes to direct drivers to start, stop, and remove devices and to query drivers about their devices.

All drivers for a device must have the opportunity to handle PnP IRPs for the device, except in a few cases where a function or filter driver is allowed to fail the IRP.

Each driver's *DispatchPnP* routine must follow these rules:

-   A function or filter driver must pass PnP IRPs down to the next driver in the device stack, unless the function or filter driver handles the IRP and encounters a failure (due to insufficient resources, for example).

    All drivers for a device must have the opportunity to handle PnP IRPs for the device unless one of the drivers encounters an error. The PnP manager sends IRPs to the top driver in a device stack. Function and filter drivers pass the IRP down to the next driver, and the parent bus driver completes the IRP. See [Passing PnP IRPs Down the Device Stack](passing-pnp-irps-down-the-device-stack.md) for more information.

    A driver can fail an IRP if it tries to handle the IRP and encounters an error (such as insufficient resources). If a driver receives an IRP with a code it does not handle, the driver must not fail the IRP. It must pass such an IRP down to the next driver without modifying the IRP's status.

-   A driver must handle certain PnP IRPs and may optionally handle others.

    Each PnP driver is required to handle certain IRPs, such as [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738), and can optionally handle others. See [Plug and Play Minor IRPs](https://msdn.microsoft.com/library/windows/hardware/ff558807) for information about which IRPs are required and optional for each kind of driver (function drivers, filter drivers, and bus drivers).

    A driver can fail a required PnP IRP with an appropriate error status, but a driver must not return STATUS\_NOT\_SUPPORTED for such an IRP.

-   If a driver handles a PnP IRP successfully, the driver sets the IRP status to success. It does not depend on another driver in the stack to set the status.

    A driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS to inform the PnP manager that the driver handled the IRP successfully. For some IRPs, a non-bus driver might be able to rely on its parent bus driver to set the status to success. However, this is a risky practice. For consistency and robustness, a driver must set the IRP status to success for each PnP IRP it handles successfully.

-   If a driver fails an IRP, the driver completes the IRP with an error status and does not pass the IRP down to the next driver.

    To fail an IRP like [**IRP\_MN\_QUERY\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551725), a driver sets **Irp-&gt;IoStatus.Status** to STATUS\_UNSUCCESSFUL. Additional error status values for other IRPs include STATUS\_INSUFFICIENT\_RESOURCES and STATUS\_INVALID\_DEVICE\_STATE.

    Drivers do not set STATUS\_NOT\_SUPPORTED for IRPs that they handle. This is the initial status set by the PnP manager. If an IRP is completed with this status, it means that no drivers in the stack handled the IRP; all drivers just passed the IRP to the next driver.

-   A driver must handle a PnP IRP in its dispatch routine (on the IRP's way down the device stack), in an [**IoCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine (on the IRP's way back up the device stack), or both, as specified in the reference page for the IRP.

    Some PnP IRPs, such as [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738), must be handled first by the driver at the top of the device stack and then by each next-lower driver. Others, such as [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749), must be handled first by the parent bus driver. Still others, such as [**IRP\_MN\_QUERY\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551664), can be handled both on the way down the device stack and the way back up. See [Plug and Play Minor IRPs](https://msdn.microsoft.com/library/windows/hardware/ff558807) for the rules that apply to each PnP IRP. See [Postponing PnP IRP Processing Until Lower Drivers Finish](postponing-pnp-irp-processing-until-lower-drivers-finish.md) For information about handling PnP IRPs that must be processed first by the parent bus driver.

-   A driver must add information to an IRP on the IRP's way down the device stack and modify or remove information on the IRP's way back up.

    When returning information in response to a PnP query IRP, a driver must follow this convention to enable orderly information passing by the layered drivers for a device.

-   Except where explicitly documented, a driver must not depend on PnP IRPs being sent in any particular order.

-   When a driver sends a PnP IRP, it must send the IRP to the top driver in the device stack.

    Most PnP IRPs are sent by the PnP manager, but some can be sent by drivers (for example, [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687)). A driver must send a PnP IRP to the driver at the top of the device stack. Call [**IoGetAttachedDeviceReference**](https://msdn.microsoft.com/library/windows/hardware/ff549145) to get a pointer to the device object for the driver at the top of the device stack.

You should test your drivers with a checked build of the operating system. The checked build of the system verifies whether a driver follows many of the PnP rules listed above.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20DispatchPnP%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


