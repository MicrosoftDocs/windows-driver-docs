---
title: Handling System Power State Requests
description: Handling System Power State Requests
ms.assetid: c4547b72-107e-4335-a7bd-081376962da0
keywords: ["power states WDK kernel", "power management WDK kernel , power state requests", "system power states WDK kernel , power state requests", "requests WDK power management", "IRPs WDK power management", "I/O request packets WDK power management", "power requests WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling System Power State Requests





All drivers must be able to respond to system power state requests if the system is to sleep, hibernate, and wake successfully. A driver for a device changes the [device power state](device-power-states.md) for the device in response to system power state requests.

If any driver does not support system power management, individual devices can sleep and wake, but the power manager cannot put the system as a whole into a sleeping state.

The following topics cover details of handling system power state requests:

[System Power States](system-power-states.md)

[System Power Policy](system-power-policy.md)

[Preventing System Power State Changes](preventing-system-power-state-changes.md)

[Handling IRP\_MN\_QUERY\_POWER for System Power States](handling-irp-mn-query-power-for-system-power-states.md)

[Handling IRP\_MN\_SET\_POWER for System Power States](handling-irp-mn-set-power-for-system-power-states.md)

 

 




