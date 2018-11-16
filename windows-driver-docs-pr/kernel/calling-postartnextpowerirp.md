---
title: Calling PoStartNextPowerIrp
description: Calling PoStartNextPowerIrp
ms.assetid: 8b3fb578-2ac2-4a04-ac99-1cfd51b07b01
keywords: ["power IRPs WDK kernel , PoStartNextPowerIrp", "PoStartNextPowerIrp"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Calling PoStartNextPowerIrp





Beginning with Windows Vista, calling [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) is not required and a call to this routine performs no power management operation. However, in Windows Server 2003, Windows XP, and Windows 2000, after a driver processes a query-power IRP or a set-power IRP, the driver must call **PoStartNextPowerIrp** to notify the power manager that it is ready to receive another power IRP. Drivers must call **PoStartNextPowerIrp** while the IRP stack location points to the current driver and before calling [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654).

A driver must call this routine once for each [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699) or [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request that it receives. Drivers do not need to call **PoStartNextPowerIrp** when handling [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) or [**IRP\_MN\_POWER\_SEQUENCE**](https://msdn.microsoft.com/library/windows/hardware/ff551644) requests.

When a driver calls **PoStartNextPowerIrp**, the current IRP stack location must point to the current driver. As a general rule, this call is best made from an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine. **PoStartNextPowerIrp** must be called before [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343), [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355), and **PoCallDriver**. Calling the routines in the other order might cause a system deadlock.

Even if a driver fails the IRP, it must nevertheless call **PoStartNextPowerIrp** to inform the power manager that it is ready to handle another power IRP.

The following sections clarify when each type of driver should call this routine:

[Calling PoStartNextPowerIrp from a Filter Driver](calling-postartnextpowerirp-from-a-filter-driver.md)

[Calling PoStartNextPowerIrp from a Device Power Policy Owner](calling-postartnextpowerirp-from-a-device-power-policy-owner.md)

[Calling PoStartNextPowerIrp from a Bus Driver](calling-postartnextpowerirp-from-a-bus-driver.md)

 

 




