---
title: Calling IoCallDriver Versus Calling PoCallDriver
description: Calling IoCallDriver versus Calling PoCallDriver
keywords: ["PoCallDriver", "active power IRPs WDK kernel", "power IRPs WDK kernel , IoCallDriver versus PoCallDriver"]
ms.date: 06/16/2017
---

# Calling IoCallDriver versus Calling PoCallDriver





Beginning with Windows Vista, a driver should call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) instead of [**PoCallDriver**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver), to pass power IRPs to the next-lower driver. In Windows Server 2003, Windows XP, and Windows 2000, a driver must call **PoCallDriver**, not **IoCallDriver**, to pass power IRPs to the next-lower driver. Note, however, that drivers that use the same code to run both in Windows Vista and in earlier Windows versions, must call **PoCallDriver**, not **IoCallDriver**.

Beginning with Windows Vista, [**PoRequestPowerIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-porequestpowerirp) and **IoCallDriver** ensure that the power manager properly synchronizes power IRPs throughout the system. In Windows Server 2003, Windows XP, and Windows 2000, **PoRequestPowerIrp**, **PoCallDriver**, and [**PoStartNextPowerIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-postartnextpowerirp), ensure that the power manager properly synchronizes power IRPs throughout the system.

The system limits the number of active power IRPs as follows:

-   No more than one system power IRP ([**IRP\_MN\_SET\_POWER**](./irp-mn-set-power.md), [**IRP\_MN\_QUERY\_POWER**](./irp-mn-query-power.md)) can be active for each physical device object (PDO) at any given time.

-   No more than one device set-power IRP (**IRP\_MN\_SET\_POWER)** can be active for each PDO at any given time.

-   No more than one device power IRP that requires an inrush of power can be active anywhere in the system at any given time.

To ensure that two inrush devices do not attempt to power up simultaneously, the power manager keeps track of active inrush power IRPs across the whole system and allows only one to be active at a time. An additional inrush IRP cannot start until the active inrush IRP has completed.

Because of these restrictions on inrush IRPs, a device power IRP might block while an inrush IRP for another device completes. Driver writers should be aware of this behavior while debugging.

