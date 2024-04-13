---
title: Sending a Device Set-Power IRP in Response to a System Set-Power IRP
description: Sending a Device Set-Power IRP in Response to a System Set-Power IRP
keywords: ["sending set-power IRPs", "set-power IRPs WDK power management"]
ms.date: 06/16/2017
---

# Sending a Device Set-Power IRP in Response to a System Set-Power IRP





The device power policy owner should take the following steps to respond to a system set-power IRP:

1.  Call [**IoAcquireRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioacquireremovelock), passing the current IRP as the *Tag* parameter, to ensure that the driver does not receive a Plug and Play [**IRP\_MN\_REMOVE\_DEVICE**](./irp-mn-remove-device.md) request while handling the power IRP.

    If **IoAcquireRemoveLock** returns a failure status, the driver should not continue processing the IRP. Instead, starting with Windows Vista, the driver should call [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) to complete the request and then return the failure status. In Windows Server 2003, Windows XP, and Windows 2000, the driver should first call [**PoStartNextPowerIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-postartnextpowerirp), call **IoCompleteRequest** to complete the IRP, and then return the failure status.

2.  Set up the IRP stack location for the next-lower driver by calling [**IoCopyCurrentIrpStackLocationToNext**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocopycurrentirpstacklocationtonext).

3.  Set an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine in the system set-power IRP.

4.  Call [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) to mark the system set-power IRP as pending.

5.  Call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) (starting with Windows Vista) or [**PoCallDriver**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver) (in Windows Server 2003, Windows XP, and Windows 2000) to pass the system set-power IRP to the next-lower driver.

6.  Return STATUS\_PENDING from its [*DispatchPower*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine.

In the *IoCompletion* routine (see Step 3 in the preceding list), the device power policy owner sends a device set-power IRP as follows:

1.  Inspect the system set-power IRP to get the requested system power state. Choose an appropriate device power state for that system power state. For further information, see [Determining the Correct Device Power State](determining-the-correct-device-power-state.md).

2.  Call [**PoRequestPowerIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-porequestpowerirp) to send an [**IRP\_MN\_SET\_POWER**](./irp-mn-set-power.md) for the device power state determined in Step 1. The power policy owner must send the device set-power request even if the device is already in that state.

3.  Specify a power-completion callback routine (*CompletionFunction*) in the call to **PoRequestPowerIrp** and pass the system set-power IRP in the *Context* buffer.

4.  Return STATUS\_MORE\_PROCESSING\_REQUIRED from the *IoCompletion* routine, so that the driver can finish processing the system set-power IRP in the power-completion callback routine.

Remember that the device power policy owner not only sends the device set-power IRP but also must handle this IRP as it travels through the device stack. Consequently, a device power policy owner might have not only a power-completion callback routine associated with the device set-power IRP and an *IoCompletion* routine for the system set-power IRP, but also an *IoCompletion* routine for the device set-power IRP. For further information, see [Handling IRP\_MN\_SET\_POWER for Device Power States](handling-irp-mn-set-power-for-device-power-states.md).

After the I/O manager calls all the *IoCompletion* routines that were set as the device set-power IRP traveled down the device stack, the I/O manager calls the power-completion callback routine. By this time, all drivers in the stack have completed the device set-power IRP and the device power transition is complete.

The power-completion callback routine must do the following:

1.  Call [**PoStartNextPowerIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-postartnextpowerirp) to start the next power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only.)

2.  Complete the system set-power IRP ([**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest)) with the status returned for the device set-power IRP.

3.  Call [**IoReleaseRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreleaseremovelock) to free the previously acquired lock.

4.  Return the status with which the set-power IRPs completed.

 

