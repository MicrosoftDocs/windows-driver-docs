---
title: Using an IoTimer Routine
author: windows-driver-content
description: Using an IoTimer Routine
MS-HAID:
- 'Synchro\_c8bd324e-a1d2-41d5-917e-b365d6323e2f.xml'
- 'kernel.using\_an\_iotimer\_routine'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9de2d2ec-31c5-4a60-96bf-5da067d2d9db
keywords: ["IoTimer"]
---

# Using an IoTimer Routine


## <a href="" id="ddk-using-an-iotimer-routine-kg"></a>


While the timer for the associated device object is enabled, the [*IoTimer*](https://msdn.microsoft.com/library/windows/hardware/ff550381) routine is called approximately once per second. However, because the intervals at which each *IoTimer* routine is called depend on the resolution of the system clock, do not assume that an *IoTimer* routine will be called precisely on a one-second boundary.

**Note**  An *IoTimer* routine, like all DPC routines, is called at IRQL = DISPATCH\_LEVEL. While a DPC routine runs, all threads are prevented from running on the same processor. Driver developers should carefully design their *IoTimer* routines to run for as brief a time as possible.

 

Perhaps the most common use for an *IoTimer* routine is to time out device I/O operations for an IRP. Consider the following scenario for using an *IoTimer* routine as a running timer within a device driver:

1.  When it starts the device, the driver initializes a timer counter in the device extension to -1, indicating no current device I/O operations, and calls [**IoStartTimer**](https://msdn.microsoft.com/library/windows/hardware/ff550373) just before it returns STATUS\_SUCCESS.

    Each time the *IoTimer* routine is called, it checks whether the timer counter is -1, and, if so, returns control.

2.  The driver's [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine initializes the timer counter in the device extension to an upper limit, plus an additional second in case the *IoTimer* routine has just been run. It then uses [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) to call a *SynchCritSection\_1* routine, which programs the physical device for the operation requested by the current IRP.

3.  The driver's ISR resets the timer counter to -1 before queuing the driver's [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) routine or a [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972) routine.

4.  Each time the *IoTimer* routine is called, it checks whether the timer counter has been reset by the ISR to -1, and, if so, returns control. If not, the *IoTimer* routine uses **KeSynchronizeExecution** to call a *SynchCritSection\_2* routine, which adjusts the timer counter by some driver-determined number of seconds.

5.  The *SynchCritSection\_2* routine returns **TRUE** to the *IoTimer* routine as long as the current request has not yet timed out. If the timer counter goes to zero, the *SynchCritSection\_2* routine resets the timer counter to a driver-determined reset-timeout value, sets a reset-expected flag for itself (and for the *DpcForIsr*) in its context area, attempts to reset the device, and returns **TRUE**.

    The *SynchCritSection\_2* routine will be called again if its reset operation also times out on the device, when it returns **FALSE**. If its reset succeeds, the *DpcForIsr* routine determines that the device has been reset from the reset-expected flag and retries the request, repeating the actions of the *StartIo* routine as described in Step 2.

6.  If the *SynchCritSection\_2* routine returns **FALSE**, the *IoTimer* routine assumes the physical device is in an unknown state because an attempt to reset it has already failed. In these circumstances, the *IoTimer* routine queues a *CustomDpc* routine and returns. This *CustomDpc* routine logs a device I/O error, calls [**IoStartNextPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550358), fails the current IRP, and returns.

If this device driver's ISR resets the shared timer counter to -1, as described in Step 3, the driver's *DpcForIsr* routine completes the interrupt-driven I/O processing of the current IRP. The reset timer counter indicates that this device I/O operation has not timed out, so the *IoTimer* routine does not need to change the timer counter.

Under most circumstances, the preceding *SynchCritSection\_2* routine simply decrements the timer counter. The *SynchCritSection\_2* routine attempts to reset the device only if the current I/O operation has timed out, which is indicated when the timer counter goes to zero. And only if an attempt to reset the device has already failed does the *SynchCritSection\_2* routine return **FALSE** to the *IoTimer* routine.

Consequently, both the preceding *IoTimer* routine and its helper *SynchCritSection\_2* routine take very little time to execute under normal circumstances. By using an *IoTimer* routine in this manner, a device driver ensures that each valid device I/O request can be retried, if necessary, and that a *CustomDpc* routine will fail an IRP only if an uncorrectable hardware failure prevents the IRP from being satisfied. Moreover, the driver provides this functionality at very little cost in execution time.

The simplicity of the preceding scenario depends on a device that does only one operation at a time and on a driver that does not normally overlap I/O operations. A driver that carries out overlapped device I/O operations, or a higher-level driver that uses an *IoTimer* routine to time out a set of driver-allocated IRPs sent to more than one chain of lower drivers, would have more complex timeout scenarios to manage.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20an%20IoTimer%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


