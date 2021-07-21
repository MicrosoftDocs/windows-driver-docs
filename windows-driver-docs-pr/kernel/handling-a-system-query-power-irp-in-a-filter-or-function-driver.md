---
title: Handling a System Query-Power IRP in a Filter or Function Driver
description: Handling a System Query-Power IRP in a Filter or Function Driver
keywords: ["query-power IRPs WDK power management", "filter drivers WDK power management", "function drivers WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling a System Query-Power IRP in a Filter or Function Driver





A filter or function driver (that is not the power policy owner for a device) should pass a system query-power IRP to the next-lower driver, in the following steps:

1.  Call [**IoAcquireRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioacquireremovelock), passing the current IRP, to ensure that the driver does not receive a PnP [**IRP\_MN\_REMOVE\_DEVICE**](./irp-mn-remove-device.md) request while handling the power IRP.

    If **IoAcquireRemoveLock** returns a failure status, the driver should not continue processing the IRP. Instead, beginning with Windows Vista, the driver should call [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) to complete the IRP and return the failure status. In Windows Server 2003, Windows XP, and Windows 2000, the driver should call [**PoStartNextPowerIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-postartnextpowerirp), call **IoCompleteRequest** to complete the IRP, and return the failure status.

2.  Determine whether it should fail the query. For guidelines, see [Failing a System Query-Power IRP in a Filter or Function Driver](failing-a-system-query-power-irp-in-a-filter-or-function-driver.md) and complete processing as described in that section.

3.  Call [**PoStartNextPowerIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-postartnextpowerirp). (Windows Server 2003, Windows XP, and Windows 2000 only)

4.  Set the IRP stack location ([**IoSkipCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioskipcurrentirpstacklocation) or [**IoCopyCurrentIrpStackLocationToNext**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocopycurrentirpstacklocationtonext)). The driver can set an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine in the IRP, but doing so is rarely necessary.

5.  Call **IoCallDriver** (in Windows 7 and Windows Vista) or [**PoCallDriver**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver) (in Windows Server 2003, Windows XP, and Windows 2000) to pass the IRP to the next-lower driver.

6.  Call [**IoReleaseRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreleaseremovelock). However, if the driver set an *IoCompletion* routine for the IRP, make this call from the *IoCompletion* routine instead.

7.  Return STATUS\_PENDING from its [*DispatchPower*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine.

 

