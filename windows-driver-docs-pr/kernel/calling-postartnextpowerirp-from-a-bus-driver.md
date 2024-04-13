---
title: Calling PoStartNextPowerIrp from a Bus Driver
description: Calling PoStartNextPowerIrp from a Bus Driver
keywords: ["bus drivers WDK power management", "power IRPs WDK kernel , PoStartNextPowerIrp", "PoStartNextPowerIrp"]
ms.date: 06/16/2017
---

# Calling PoStartNextPowerIrp from a Bus Driver





Beginning with Windows Vista, calling [**PoStartNextPowerIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-postartnextpowerirp) is not required and call to this routine performs no power management operation. However, in Windows Server 2003, Windows XP, and Windows 2000, a bus driver must call **PoStartNextPowerIrp** once for every [**IRP\_MN\_QUERY\_POWER**](./irp-mn-query-power.md) or [**IRP\_MN\_SET\_POWER**](./irp-mn-set-power.md) request that the driver receives.

A bus driver always calls this routine in its *DispatchPower* routine, before it calls the [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) routine.

 

