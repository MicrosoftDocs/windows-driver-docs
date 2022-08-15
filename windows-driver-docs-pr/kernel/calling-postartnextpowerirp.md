---
title: Calling PoStartNextPowerIrp
description: Calling PoStartNextPowerIrp
keywords: ["power IRPs WDK kernel , PoStartNextPowerIrp", "PoStartNextPowerIrp"]
ms.date: 07/21/2021
---

# Calling PoStartNextPowerIrp

Beginning with Windows Vista, calling [**PoStartNextPowerIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-postartnextpowerirp) is not required and a call to this routine performs no power management operation. However, in Windows Server 2003, Windows XP, and Windows 2000, after a driver processes a query-power IRP or a set-power IRP, the driver must call **PoStartNextPowerIrp** to notify the power manager that it is ready to receive another power IRP. Drivers must call **PoStartNextPowerIrp** while the IRP stack location points to the current driver and before calling [**PoCallDriver**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver).

A driver must call this routine once for each [**IRP\_MN\_QUERY\_POWER**](./irp-mn-query-power.md) or [**IRP\_MN\_SET\_POWER**](./irp-mn-set-power.md) request that it receives. Drivers do not need to call **PoStartNextPowerIrp** when handling [**IRP\_MN\_WAIT\_WAKE**](./irp-mn-wait-wake.md) or [**IRP\_MN\_POWER\_SEQUENCE**](./irp-mn-power-sequence.md) requests.

When a driver calls **PoStartNextPowerIrp**, the current IRP stack location must point to the current driver. As a general rule, this call is best made from an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine. **PoStartNextPowerIrp** must be called before [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest), [**IoSkipCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioskipcurrentirpstacklocation), and **PoCallDriver**. Calling the routines in the other order might cause a system deadlock.

Even if a driver fails the IRP, it must nevertheless call **PoStartNextPowerIrp** to inform the power manager that it is ready to handle another power IRP.

The following sections clarify when each type of driver should call this routine:

[Calling PoStartNextPowerIrp from a Filter Driver](calling-postartnextpowerirp-from-a-filter-driver.md)

[Calling PoStartNextPowerIrp from a Device Power Policy Owner](calling-postartnextpowerirp-from-a-device-power-policy-owner.md)

[Calling PoStartNextPowerIrp from a Bus Driver](calling-postartnextpowerirp-from-a-bus-driver.md)
