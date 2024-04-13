---
title: Using Critical Sections
description: Using Critical Sections
keywords: ["interrupt service routines WDK kernel , critical sections", "ISRs WDK kernel , critical sections", "InterruptService", "synchronization WDK kernel , interrupts"]
ms.date: 06/16/2017
---

# Using Critical Sections





Any driver that contains an [*InterruptService*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kservice_routine) routine will most likely require one or more critical sections to synchronize access to hardware resources or driver data among the ISR and other routines.

This section includes the following topics:

[Introduction to SynchCritSection Routines](introduction-to-synchcritsection-routines.md)

[Writing SynchCritSection Routines](writing-synchcritsection-routines.md)

 

