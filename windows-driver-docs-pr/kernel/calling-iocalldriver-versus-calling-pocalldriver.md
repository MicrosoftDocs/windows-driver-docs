---
title: Calling IoCallDriver versus Calling PoCallDriver
description: Calling IoCallDriver versus Calling PoCallDriver
ms.assetid: a47e2310-e89b-4552-bbe3-d4984ae8b564
keywords: ["PoCallDriver", "active power IRPs WDK kernel", "power IRPs WDK kernel , IoCallDriver versus PoCallDriver"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Calling IoCallDriver versus Calling PoCallDriver





Beginning with Windows Vista, a driver should call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) instead of [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654), to pass power IRPs to the next-lower driver. In Windows Server 2003, Windows XP, and Windows 2000, a driver must call **PoCallDriver**, not **IoCallDriver**, to pass power IRPs to the next-lower driver. Note, however, that drivers that use the same code to run both in Windows Vista and in earlier Windows versions, must call **PoCallDriver**, not **IoCallDriver**.

Beginning with Windows Vista, [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) and **IoCallDriver** ensure that the power manager properly synchronizes power IRPs throughout the system. In Windows Server 2003, Windows XP, and Windows 2000, **PoRequestPowerIrp**, **PoCallDriver**, and [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776), ensure that the power manager properly synchronizes power IRPs throughout the system.

The system limits the number of active power IRPs as follows:

-   No more than one system power IRP ([**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744), [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699)) can be active for each physical device object ([PDO](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdo)) at any given time.

-   No more than one device set-power IRP (**IRP\_MN\_SET\_POWER)** can be active for each PDO at any given time.

-   No more than one device power IRP that requires an inrush of power can be active anywhere in the system at any given time.

To ensure that two inrush devices do not attempt to power up simultaneously, the power manager keeps track of active inrush power IRPs across the whole system and allows only one to be active at a time. An additional inrush IRP cannot start until the active inrush IRP has completed.

Because of these restrictions on inrush IRPs, a device power IRP might block while an inrush IRP for another device completes. Driver writers should be aware of this behavior while debugging.

 

 




