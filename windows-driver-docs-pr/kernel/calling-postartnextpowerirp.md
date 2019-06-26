---
title: Calling PoStartNextPowerIrp
description: Calling PoStartNextPowerIrp
ms.assetid: 8b3fb578-2ac2-4a04-ac99-1cfd51b07b01
keywords: ["power IRPs WDK kernel , PoStartNextPowerIrp", "PoStartNextPowerIrp"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Calling PoStartNextPowerIrp





Beginning with Windows Vista, calling [**PoStartNextPowerIrp**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-postartnextpowerirp) is not required and a call to this routine performs no power management operation. However, in Windows Server 2003, Windows XP, and Windows 2000, after a driver processes a query-power IRP or a set-power IRP, the driver must call **PoStartNextPowerIrp** to notify the power manager that it is ready to receive another power IRP. Drivers must call **PoStartNextPowerIrp** while the IRP stack location points to the current driver and before calling [**PoCallDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-pocalldriver).

A driver must call this routine once for each [**IRP\_MN\_QUERY\_POWER**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-power) or [**IRP\_MN\_SET\_POWER**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-set-power) request that it receives. Drivers do not need to call **PoStartNextPowerIrp** when handling [**IRP\_MN\_WAIT\_WAKE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-wait-wake) or [**IRP\_MN\_POWER\_SEQUENCE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-power-sequence) requests.

When a driver calls **PoStartNextPowerIrp**, the current IRP stack location must point to the current driver. As a general rule, this call is best made from an [*IoCompletion*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-io_completion_routine) routine. **PoStartNextPowerIrp** must be called before [**IoCompleteRequest**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocompleterequest), [**IoSkipCurrentIrpStackLocation**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer), and **PoCallDriver**. Calling the routines in the other order might cause a system deadlock.

Even if a driver fails the IRP, it must nevertheless call **PoStartNextPowerIrp** to inform the power manager that it is ready to handle another power IRP.

The following sections clarify when each type of driver should call this routine:

[Calling PoStartNextPowerIrp from a Filter Driver](calling-postartnextpowerirp-from-a-filter-driver.md)

[Calling PoStartNextPowerIrp from a Device Power Policy Owner](calling-postartnextpowerirp-from-a-device-power-policy-owner.md)

[Calling PoStartNextPowerIrp from a Bus Driver](calling-postartnextpowerirp-from-a-bus-driver.md)

 

 




