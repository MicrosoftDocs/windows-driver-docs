---
title: Calling PoStartNextPowerIrp from a Bus Driver
description: Calling PoStartNextPowerIrp from a Bus Driver
ms.assetid: 4e23ebe1-c939-48e1-82bf-cdb4980a5a7b
keywords: ["bus drivers WDK power management", "power IRPs WDK kernel , PoStartNextPowerIrp", "PoStartNextPowerIrp"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Calling PoStartNextPowerIrp from a Bus Driver





Beginning with Windows Vista, calling [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) is not required and call to this routine performs no power management operation. However, in Windows Server 2003, Windows XP, and Windows 2000, a bus driver must call **PoStartNextPowerIrp** once for every [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699) or [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request that the driver receives.

A bus driver always calls this routine in its *DispatchPower* routine, before it calls the [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) routine.

 

 




