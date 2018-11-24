---
title: Writing an Unload Routine
description: Writing an Unload Routine
ms.assetid: 578f3499-28fc-412b-bbb7-75f8023fa7c1
keywords: ["standard driver routines WDK kernel , Unload routines", "driver routines WDK kernel , Unload routines", "routines WDK kernel , Unload routines", "Unload routines WDK kernel", "Unload routines WDK kernel , about Unload routines", "replacing drivers", "driver replacements WDK kernel", "unloading drivers", "reloading drivers WDK kernel", "driver unloading WDK kernel", "driver reloading WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Writing an Unload Routine





Any driver that can be replaced, or unloaded and reloaded, while the system is running must have an [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine. All WDM drivers must have *Unload* routines.

Although *Unload* routines are optional for non-WDM drivers, [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) will fail any driver that does not provide an *Unload* routine.

This section contains the following topics:

[Unload Routine Environment](unload-routine-environment.md)

[Unload Routine Functionality](unload-routine-functionality.md)

 

 




