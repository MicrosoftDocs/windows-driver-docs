---
title: Programming a Device for an I/O Operation
description: Programming a Device for an I/O Operation
keywords: ["critical section routines WDK kernel", "I/O WDK kernel , device programming"]
ms.date: 06/16/2017
---

# Programming a Device for an I/O Operation





Use the following general guidelines for designing, writing, and calling [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routines that program a device for I/O operations:

-   A *SynchCritSection* routine that programs the device for I/O operations must return control as quickly as possible.

    For this reason, the *SynchCritSection* routine should do only what is necessary to set up the device for I/O. Therefore, the driver should perform all IRP preprocessing, initializing state information for other driver routines, and acquiring hardware resources before it calls the *SynchCritSection* routine.

-   A device driver can have multiple *SynchCritSection* routines to program the device.

    For example, the driver of a device for which setting up a read request differs markedly from setting up certain device control requests might have separate *SynchCritSection* routines to program its device for each type of request.

-   Every *SynchCritSection* routine must return control as quickly as possible, because running any *SynchCritSection* routine prevents the driver's ISR from executing.

    You should not write a single, large, general-purpose *SynchCritSection* routine with a **switch** statement or many nested **if..then..else** statements to determine what operations it will carry out or what state information to update. On the other hand, you should avoid writing numerous *SynchCritSection* routines that program only a single device register.

 

