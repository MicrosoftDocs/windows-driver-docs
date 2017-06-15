---
title: IoTimer Routines
author: windows-driver-content
description: IoTimer Routines
MS-HAID:
- 'Synchro\_94c58b61-68a2-4ea3-8aca-d3daccf4537c.xml'
- 'kernel.iotimer\_routines'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: bc69c7b5-ce63-435e-b5b4-0d65ee153d31
keywords: ["synchronization WDK kernel , timers", "IoTimer", "device time-outs WDK kernel", "time-outs WDK kernel", "timing operations WDK kernel", "timeout device I/O operations WDK kernel"]
---

# IoTimer Routines


## <a href="" id="ddk-iotimer-routines-kg"></a>


Drivers that need to be called periodically to determine if a device operation has timed out, to update some driver-defined variable (such as a counter), or to time any operation for which small time intervals are not required, can use an [*IoTimer*](https://msdn.microsoft.com/library/windows/hardware/ff550381) routine. An *IoTimer* routine is actually a DPC routine, associated with a device object, that the I/O manager calls once per second. A driver can have an *IoTimer* routine for each device object that it creates.

In general, a driver should use an *IoTimer* routine to time operations that require regular one-second intervals. To time operations that require variable intervals or intervals shorter than once per second, a driver should allocate a timer object. For more information, see [Timer Objects and DPCs](timer-objects-and-dpcs.md).

This section contains the following topics:

[Registering and Enabling an IoTimer Routine](registering-and-enabling-an-iotimer-routine.md)

[Providing IoTimer Context Information](providing-iotimer-context-information.md)

[Using an IoTimer Routine](using-an-iotimer-routine.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IoTimer%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


