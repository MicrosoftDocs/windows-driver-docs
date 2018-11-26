---
title: Creating Reliable Kernel-Mode Drivers
description: Creating Reliable Kernel-Mode Drivers
ms.assetid: 31bbf1fe-dc90-43e0-a53e-eca902ec343e
keywords: ["kernel-mode drivers WDK , reliability", "reliability WDK kernel", "reliability WDK kernel , about reliable drivers", "IRPs WDK kernel , reliability issues"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Creating Reliable Kernel-Mode Drivers





Drivers make up a significant percentage of the total code that executes in kernel mode. A kernel-mode driver is, in effect, a component of the operating system. Therefore, drivers that are reliable and secure contribute significantly to the overall trustworthiness of the operating system. To create a reliable kernel-mode driver, follow these guidelines:

-   Secure device objects properly.

    User access to a system's drivers and devices is controlled by security descriptors that the system assigns to device objects. Most often, the system sets device security parameters when a device is installed. For more information, see [Creating Secure Device Installations](https://msdn.microsoft.com/library/windows/hardware/ff540212). Sometimes it is appropriate for a driver to play a part in controlling access to its device. For more information, see [Securing Device Objects](securing-device-objects.md).

-   Validate device objects properly.

    If a driver creates multiple types of device objects, it must check which type it receives in each IRP. For more information, see [Failure to Validate Device Objects](failure-to-validate-device-objects.md).

-   Use "safe string" functions.

    When manipulating strings, a driver should use safe string functions instead of the string functions that are supplied with C/C++ language runtime libraries. For more information, see [Using Safe String Functions](using-safe-string-functions.md).

-   Validate object handles.

    Drivers that receive object handles as input must verify that the handles are valid, are accessible, and are of the type expected. For more information about using object handles, see the following topics:

    [Object Management](managing-kernel-objects.md)

    [Failure to Validate Object Handles](failure-to-validate-object-handles.md)

-   Support multiprocessors properly.

    Never assume that your driver will run only on single-processor systems. For information about programming techniques that you can use to ensure that your driver will function properly on multiprocessor systems, see the following topics:

    [Synchronization Techniques](synchronization-techniques.md)

    [Errors in a Multiprocessor Environment](errors-in-a-multiprocessor-environment.md)

-   Handle driver state properly.

    It is important to always verify that your driver is in the state you assume it to be in. For example, if the driver receives an IRP, is it already servicing an IRP of the same type? If the driver does not check for this situation, the first IRP could be lost. For more information, see [Failure to Check a Driver's State](failure-to-check-a-driver-s-state.md).

-   Validate IRP input values.

    It is essential, from both a reliability and a security perspective, to validate all values that are associated with an IRP, such as buffer addresses and lengths. The following topics provide information about validating IRP input values:

    [DispatchReadWrite Using Buffered I/O](dispatchreadwrite-using-buffered-i-o.md)

    [Errors in Buffered I/O](errors-in-buffered-i-o.md)

    [DispatchReadWrite Using Direct I/O](dispatchreadwrite-using-direct-i-o.md)

    [Errors in Direct I/O](errors-in-direct-i-o.md)

    [Security Issues for I/O Control Codes](security-issues-for-i-o-control-codes.md)

    [Errors in Referencing User-Space Addresses](errors-in-referencing-user-space-addresses.md)

-   Handle the I/O stack properly.

    When [passing IRPs down the driver stack](passing-irps-down-the-driver-stack.md), it is important for drivers to call [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355) or [**IoCopyCurrentIrpStackLocationToNext**](https://msdn.microsoft.com/library/windows/hardware/ff548387) to set up the next driver's I/O stack location. Do not write code that directly copies one I/O stack location to the next.

-   Handle IRP completion operations properly.

    A driver must never complete an IRP with a status value of STATUS\_SUCCESS unless it actually supports and processes the IRP. For information about the correct ways to handle IRP completion operations, see [Completing IRPs](completing-irps.md).

-   Handle IRP cancellation operations properly.

    Cancel operations can be difficult to code properly because they typically execute asynchronously. Problems in the code that handles cancel operations can go unnoticed for a long time, because this code is typically not executed frequently in a running system.

    Be sure to read and understand all of the information supplied under [Canceling IRPs](canceling-irps.md). Pay special attention to [Synchronizing IRP Cancellation](synchronizing-irp-cancellation.md) and [Points to Consider When Canceling IRPs](points-to-consider-when-canceling-irps.md).

    One way to avoid the synchronization problems that are associated with cancel operations is to implement a [cancel-safe IRP queue](cancel-safe-irp-queues.md). A cancel-safe IRP queue is a driver-managed queue that was introduced for Windows XP and later operating system versions, but is also backward-compatible to earlier versions.

-   Handle IRP cleanup and close operations properly.

    Be sure that you understand the difference between [**IRP\_MJ\_CLEANUP**](https://msdn.microsoft.com/library/windows/hardware/ff550718) and [**IRP\_MJ\_CLOSE**](https://msdn.microsoft.com/library/windows/hardware/ff550720) requests. Cleanup requests arrive after an application closes all handles on a file object, but sometimes before all I/O requests have completed. Close requests arrive after all I/O requests for the file object have been completed or canceled. For more information, see the following topics:

    [DispatchCreate, DispatchClose, and DispatchCreateClose Routines](dispatchcreate--dispatchclose--and-dispatchcreateclose-routines.md)

    [DispatchCleanup Routines](dispatchcleanup-routines.md)

    [Errors in Handling Cleanup and Close Operations](errors-in-handling-cleanup-and-close-operations.md)

For more information about handling IRPs correctly, see [Additional Errors in Handling IRPs](additional-errors-in-handling-irps.md).

### Using Driver Verifier

[Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) is the most important tool you can use to ensure the reliability of your driver. Driver Verifier can check for a variety of common driver problems, including some of those discussed in this section. However, use of Driver Verifier does not replace careful, thoughtful software design.

 

 




