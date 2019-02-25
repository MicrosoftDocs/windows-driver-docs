---
title: Kernel-Mode Driver Components
description: Kernel-Mode Driver Components
ms.assetid: 79be2948-cc74-4f0b-8ffa-1e57f44d7b0c
keywords: ["kernel-mode drivers WDK , components", "kernel-mode drivers WDK , standard driver routines", "standard driver routines WDK kernel", "driver routines WDK kernel", "routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Kernel-Mode Driver Components





This section introduces the standard routines contained in kernel-mode drivers. Some of these *standard driver routines* are required; others are optional. The section also introduces *driver objects*, which contain pointers to each driver's standard routines.

Some drivers interact with a system-supplied port driver or class driver that defines much of the driver's required functionality. For example, a SCSI miniport driver primarily interacts with the SCSI port driver. For such drivers, see the class-specific documentation for details of required and optional driver support.

This section includes:

[Introduction to Standard Driver Routines](introduction-to-standard-driver-routines.md)

[Standard Driver Routine Requirements](standard-driver-routine-requirements.md)

[Introduction to Driver Objects](introduction-to-driver-objects.md)

[Writing a DriverEntry Routine](writing-a-driverentry-routine.md)

[Writing a Reinitialize Routine](writing-a-reinitialize-routine.md)

[Writing an AddDevice Routine](writing-an-adddevice-routine.md)

[Writing Dispatch Routines](writing-dispatch-routines.md)

[Writing an Unload Routine](writing-an-unload-routine.md)

 

 




