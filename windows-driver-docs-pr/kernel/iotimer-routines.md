---
title: IoTimer Routines
description: IoTimer Routines
ms.assetid: bc69c7b5-ce63-435e-b5b4-0d65ee153d31
keywords: ["synchronization WDK kernel , timers", "IoTimer", "device time-outs WDK kernel", "time-outs WDK kernel", "timing operations WDK kernel", "timeout device I/O operations WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# IoTimer Routines





Drivers that need to be called periodically to determine if a device operation has timed out, to update some driver-defined variable (such as a counter), or to time any operation for which small time intervals are not required, can use an [*IoTimer*](https://msdn.microsoft.com/library/windows/hardware/ff550381) routine. An *IoTimer* routine is actually a DPC routine, associated with a device object, that the I/O manager calls once per second. A driver can have an *IoTimer* routine for each device object that it creates.

In general, a driver should use an *IoTimer* routine to time operations that require regular one-second intervals. To time operations that require variable intervals or intervals shorter than once per second, a driver should allocate a timer object. For more information, see [Timer Objects and DPCs](timer-objects-and-dpcs.md).

This section contains the following topics:

[Registering and Enabling an IoTimer Routine](registering-and-enabling-an-iotimer-routine.md)

[Providing IoTimer Context Information](providing-iotimer-context-information.md)

[Using an IoTimer Routine](using-an-iotimer-routine.md)

 

 




