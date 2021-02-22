---
title: Preventing System Power State Changes
description: Preventing System Power State Changes
keywords: ["system power states WDK kernel , preventing changes", "state transitions WDK power management", "PoRegisterSystemState", "PoSetSystemState", "PoUnregisterSystemState", "working states WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Preventing System Power State Changes





Although drivers cannot directly set system power policy, the power manager provides three routines through which a driver can prevent system transitions out of the working state: [**PoSetSystemState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-posetsystemstate), [**PoRegisterSystemState**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-poregistersystemstate), and [**PoUnregisterSystemState**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pounregistersystemstate).

By calling **PoRegisterSystemState** or **PoSetSystemState**, a driver can notify the power manager that a user is present or that the driver requires use of the system or display.

**PoRegisterSystemState** allows a driver to register a continuous busy state. It returns a handle through which the driver can later change its settings. As long as the state registration is in effect, the power manager does not attempt to put the system to sleep. The driver cancels the state registration by calling **PoUnregisterSystemState**.

With **PoSetSystemState**, a driver notifies the power manager of the same conditions (user present, system required, display required), but this setting is not continuous. It has the effect of restarting any idle count downs associated with the specified conditions.

Using these routines, a driver can forestall many, but not all, transitions out of the working state. The power manager always shuts down the system when loss of power is imminent or when a user explicitly requests shutdown.

 

