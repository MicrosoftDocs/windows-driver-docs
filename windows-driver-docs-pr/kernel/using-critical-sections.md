---
title: Using Critical Sections
description: Using Critical Sections
ms.assetid: 439ba7ef-6473-40ca-9daa-a8c61d789d97
keywords: ["interrupt service routines WDK kernel , critical sections", "ISRs WDK kernel , critical sections", "InterruptService", "synchronization WDK kernel , interrupts"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using Critical Sections





Any driver that contains an [*InterruptService*](https://msdn.microsoft.com/library/windows/hardware/ff547958) routine will most likely require one or more critical sections to synchronize access to hardware resources or driver data among the ISR and other routines.

This section includes the following topics:

[Introduction to SynchCritSection Routines](introduction-to-synchcritsection-routines.md)

[Writing SynchCritSection Routines](writing-synchcritsection-routines.md)

 

 




