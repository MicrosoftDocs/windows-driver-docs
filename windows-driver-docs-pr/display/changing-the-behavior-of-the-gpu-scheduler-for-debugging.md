---
title: Changing the Behavior of the GPU Scheduler for Debugging
description: Changing the Behavior of the GPU Scheduler for Debugging
ms.assetid: 72eef7bf-b775-4e02-acc6-b745a41c616a
keywords:
- GPU scheduler changes WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Changing the Behavior of the GPU Scheduler for Debugging


To help in debugging the driver, the behavior of the graphics processing unit (GPU) scheduler can be changed by configuring the registry.

You can enable or disable preemption requests from the GPU scheduler (see [Timeout Detection and Recovery](timeout-detection-and-recovery.md)) by using the following registry configuration:

```
KeyPath   : HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler
KeyValue  : EnablePreemption
ValueType : REG_DWORD
ValueData : 0 to disable preemption, 1 to enable preemption (default).
```

 

 





