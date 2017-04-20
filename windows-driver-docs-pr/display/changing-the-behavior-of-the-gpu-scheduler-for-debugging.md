---
title: Changing the Behavior of the GPU Scheduler for Debugging
description: Changing the Behavior of the GPU Scheduler for Debugging
ms.assetid: 72eef7bf-b775-4e02-acc6-b745a41c616a
keywords:
- GPU scheduler changes WDK display
ms.author: windows-driver-content
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Changing%20the%20Behavior%20of%20the%20GPU%20Scheduler%20for%20Debugging%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




