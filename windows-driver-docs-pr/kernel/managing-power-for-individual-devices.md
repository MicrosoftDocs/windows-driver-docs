---
title: Managing Power for Individual Devices
description: Managing Power for Individual Devices
ms.assetid: 95c7e900-5d51-4eb7-8780-1c40befa3599
keywords: ["power management WDK kernel , device management", "device power management WDK kernel", "system power states WDK kernel", "conserving power WDK kernel", "change power states WDK kernel", "IRPs WDK power management", "I/O request packets WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Managing Power for Individual Devices





Drivers manage power for their devices by responding to [system power state](system-power-states.md) changes, detecting and shutting down idle devices, and powering up devices when they are needed.

This section covers the following topics related to device power management:

[Device Power States](device-power-states.md)

[Detecting an Idle Device](detecting-an-idle-device.md)

[Managing Device Power Policy](managing-device-power-policy.md)

[Handling IRP\_MN\_SET\_POWER for Device Power States](handling-irp-mn-set-power-for-device-power-states.md)

[Handling IRP\_MN\_QUERY\_POWER for Device Power States](handling-irp-mn-query-power-for-device-power-states.md)

[Sending IRP\_MN\_QUERY\_POWER or IRP\_MN\_SET\_POWER for Device Power States](sending-irp-mn-query-power-or-irp-mn-set-power-for-device-power-states.md)

[Detecting an Idle Device](detecting-an-idle-device.md)

[Supporting D3cold in a Driver](supporting-d3cold-in-a-driver.md)

 

 




