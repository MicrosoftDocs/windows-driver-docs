---
title: Driver Verifier What's New
description: Driver Verifier is available in all versions of Windows starting with Windows 2000. Each version introduces new features and checks for finding bugs in Windows drivers. This section summarizes the changes and provides links to related documentation.
ms.assetid: EAC30108-F8A2-4914-9218-2E0672982B7E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Verifier: What's New


[Driver Verifier](driver-verifier.md) is available in all versions of Windows starting with Windows 2000. Each version introduces new features and checks for finding bugs in Windows drivers. This section summarizes the changes and provides links to related documentation.

-   [Driver Verifier in Windows 10](#driver-verifier-in-windows-10)
-   [Driver Verifier in Windows 8.1](#driver-verifier-in-windows-8-1)
-   [Driver Verifier in Windows 8](#driver-verifier-in-windows-8)
-   [Driver Verifier in Windows 7](#driver-verifier-in-windows-7)
-   [Driver Verifier in Windows Vista](#driver-verifier-in-windows-vista)
-   [Driver Verifier in Windows XP](#driver-verifier-in-windows-xp)

## Driver Verifier in Windows 10


*Updated: May 8, 2018*

> [!IMPORTANT]
> Starting in versions after Windows 10 1803, running Driver Verifier will no longer automatically enable Windows Driver Framework (WDF) verification. Please note the following:  
> * You can still enable WDF verification as part of Driver Verifier's `/standard` flags. See [Driver Verifier Command Syntax](https://docs.microsoft.com/windows-hardware/drivers/devtest/verifier-command-line) for more information.
> * This change will impact you if you are enabling DV with syntax `/flags 0x209BB` as WDF verification will no longer be automatically enabled.

Starting with Windows 10, driver verifier includes new driver validation rules for the following technologies:

-   New [Rules for Audio Drivers](https://msdn.microsoft.com/library/windows/hardware/dn906757)
-   New [Rules for AVStream Drivers](https://msdn.microsoft.com/library/windows/hardware/dn906758)
-   Four new [Rules for KMDF Drivers](https://msdn.microsoft.com/library/windows/hardware/ff551709)
-   Three new [Rules for NDIS Drivers](https://msdn.microsoft.com/library/windows/hardware/ff551713)

## Driver Verifier in Windows 8-1


*Updated: June 17, 2013*

Starting with Windows 8.1, Driver Verifier introduces four new options for detecting errors.

-   The [NDIS/WIFI verification](ndis-wifi-verification.md) option applies a set of NDIS and wireless LAN rules that check for the proper interaction between an NDIS miniport driver and the operating system kernel.

-   The [Systematic low resources simulation](systematic-low-resource-simulation.md) option injects resource failures in kernel mode drivers.

-   The [Kernel synchronization delay fuzzing](kernel-synchronization-delay-fuzzing.md) option randomizes thread schedules to help detect concurrency bugs in the driver.

-   The [VM switch verification](vm-switch-verification.md) option monitors filter drivers (extensible switch extensions) that run inside the [Hyper-V Extensible Switch](https://msdn.microsoft.com/library/windows/hardware/hh598161).
-   New debugger extension: [**!ruleinfo**](https://msdn.microsoft.com/library/windows/hardware/dn265374)

## Driver Verifier in Windows 8


*Updated: October 20, 2012*

Starting with Windows 8, Driver Verifier introduces five new options for detecting errors.

-   The [Power Framework Delay Fuzzing](concurrency-stress-test.md) option inserts random execution delays to help detect concurrency bugs in drivers that use the power management framework (PoFx). The execution delays have upper-time limits. This option is not recommended for drivers that do not directly utilize the power management framework (PoFx).
-   The [DDI compliance checking](ddi-compliance-checking.md) option applies the same device driver interface (DDI) usage rules that [Static Driver Verifier](static-driver-verifier.md) uses to verify that your driver makes function calls at the required IRQL for the function. The DDI compliance checking is run as part of the standard Driver Verifier options.
-   The [Invariant MDL Checking for Stack](invariant-mdl-checking-for-stack.md) option monitors how the driver handles invariant MDL buffers across the driver stack.
-   The [Invariant MDL Checking for Driver](invariant-mdl-checking-for-driver.md) option monitors how the driver handles invariant MDL buffers on a per-driver basis.
-   The [Stack Based Failure Injection](stack-based-failure-injection.md) option injects resource allocation failures in kernel mode drivers.

When you build, deploy, and test your driver using Visual Studio 2012 and the WDK for Windows 8, you can also configure Driver Verifier to run on a test computer when you deploy your driver for testing.

## Driver Verifier in Windows 7


*Updated: October 22, 2012*

For information about new features that were added in Windows 7, see the white paper [Driver Verifier in Windows 7]( http://go.microsoft.com/fwlink/p/?linkid=309793).

For Windows 7, Driver Verifier has been enhanced with new tests and features that allow Driver Verifier to expose more classes of typical driver bugs.

-   Incorrect References to User Handles from Kernel Drivers
-   I/O Verification Improvements
-   Special Pool, Pool Tracking, and Low Resources Simulation Improvements
-   Incorrect Usage of Synchronization Mechanisms
-   Incorrect Object References
-   Pool Quota Charges from DPC Routine
-   System Shutdown Blocks or Delays
-   Improved Force Pending I/O Requests

In Windows 7, Driver Verifier provides checks for queued spin locks, these checks resemble those provided to spin locks in earlier Windows versions. These checks include the following:

-   Verifying that an operation that should raise the interrupt request level (IRQL) value, such as [**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899), is not actually lowering the IRQL value.

-   Verifying that an operation that should lower the IRQL value, such as [**KeReleaseInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553130), is not actually raising the IRQL value.

-   Trimming the System process’s working set if the [Force IRQL Checking](force-irql-checking.md) option is enabled, when the IRQL is being raised to DISPATCH\_LEVEL or above, in an attempt to expose possible references to pageable memory while the driver is running at elevated IRQL.

-   Predicting possible deadlocks when the Deadlock Detection option is enabled.

-   Trying to use the same KSPIN\_LOCK data structure both as a spin lock and as a stack queued spin lock when the Deadlock Detection option is enabled.

-   Checking for obviously incorrect pointer values, such as a user-mode virtual address that is used as a spin lock address.

-   Logging IRQL transitions in the Driver Verifier IRQL log. This information appears when you use the **!verifier 8** extension of the Windows Debuggers. See [**!verifier**](https://msdn.microsoft.com/library/windows/hardware/ff565591).

**Additional Debugging Information**

In Windows 7, Driver Verifier provides the following additional information that is useful for debugging:

There is a log with stack traces in chronological order for recent calls to [**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021) and [**KeLeaveCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552964) from verified drivers. The log contents are displayed by using the **!verifier 0x200** debugger extension of the Windows Debuggers. This information can be useful for understanding scenarios in which a thread is unexpectedly running in a critical region or is trying to leave a critical region that it has left already.

You can display additional information from the [Force Pending I/O Requests](force-pending-i-o-requests.md) Log by using the **!verifier 0x40** debugger extension. In earlier Windows versions, the log contained just one stack trace for each IRP that Driver Verifier forced to be pending. This was the stack trace from the time when [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) was called for the first time for the forced pending IRP. Windows 7 has at least two log entries, possibly more than two, for each forced pending IRP:

-   Stack trace at the time when Driver Verifier picked the IRP to be forced pending. Driver Verifier chooses some of the IRPs to be forced pending when one of the verified drivers calls [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).
-   Stack traces for each [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) call for the forced pending IRP before the completion reaches the verified driver. More than one **IoCompleteRequest** call can exist for the same IRP because one of the drivers can temporarily stop the completion from its completion routine and then resume it by calling **IoCompleteRequest** again.

There are more valid stack traces in the IRQL Transition log. This log is displayed by using **!verifier 8**. In Windows versions earlier than Windows 7, Driver Verifier could have tried to log some of these stack traces at elevated IRQL and failed to capture the stack trace because of the high IRQL value. In Windows 7, Driver Verifier tries to capture these stack traces:

-   Before raising the IRQL, for example, when a verified driver calls [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917).
-   After the IRQL is lowered, when a verified driver calls [**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145).

In this way, Driver Verifier can capture more of these IRQL transition stack traces.

**!analyze** can triage issues that are exposed by the Enhanced I/O Verifier checks (that are part of I/O Verifier in Windows 7). In earlier Windows versions, the Enhanced I/O Verifier error reporting consisted of displaying a description of the driver defect that was detected by Driver Verifier followed by a break into debugger. Running **!analyze** after such a break does not result in meaningful triage for many of these breaks because **!analyze** cannot use the information from the error description text that appears in the debugger. In Windows 7, the meaningful information about these driver defects is saved by Driver Verifier in memory. **!analyze** can find this information and perform a much more meaningful automatic triage for many of these breaks.

## Driver Verifier in Windows Vista


*Updated: February 9, 2009*

For information about new features that were added in Windows Vista, see the white paper [Driver Verifier in Windows Vista]( http://go.microsoft.com/fwlink/p/?linkid=309794).

For Windows Vista, Driver Verifier has been enhanced with new tests and features.

-   Enabling Driver Verifier and Changing Settings without Rebooting
-   Enhanced Low Resources Simulation
-   Force Pending I/O Requests
-   Security Checks
-   More Thorough I/O Verification
-   Enhanced IRQL Checking
-   Miscellaneous Checks
-   Locked Memory Page Tracking
-   Additional Automatic Checks

## Driver Verifier in Windows XP


*Updated: December 4, 2001*

Driver Verifier is a tool for monitoring Windows kernel-mode drivers and graphics drivers. Microsoft strongly encourages hardware manufacturers to test their drivers with Driver Verifier to ensure that drivers are not making illegal function calls or causing system corruption. Driver Verifier has been enhanced with new tests and features for Microsoft Windows XP.

Drivers submitted to WHQL for testing must pass Driver Verifier. New Driver Verifier features in Windows XP include:

-   Driver Verifier Manager, an all-new graphical user interface (GUI) for verifier.exe
-   New automatic check for Monitoring Stack Switching
-   New Driver Verifier options for DMA Verification (also known as HAL Verification), Deadlock Detection, and SCSI Verification
-   I/O Verification changes that combine "Level 1" and "Level 2" tests, optional Enhanced I/O Verification tests
-   New debugger extensions [**!deadlock**](https://msdn.microsoft.com/library/windows/hardware/ff562326) and [**!dma**](https://msdn.microsoft.com/library/windows/hardware/ff562369)
-   New bug checks: 0xE6 (DRIVER\_VERIFIER\_DMA\_VIOLATION) and 0xF1 (SCSI\_VERIFIER\_DETECTED\_VIOLATION)
-   Additional sub-codes for the existing bug check codes 0xC4 and 0xC9

Driver Verifier features also include:

-   **New Verifier command line options** The verifier.exe utility has a new parameter, *VolatileDriverList*, which can be used with the **/adddriver** keyword to specify a list of drivers to add to the volatile settings. *VolatileDriverList* can be used with the **/removedriver** keyword to specify a list of drivers to remove.
-   **New !verifier extensions** New [**!verifier**](https://msdn.microsoft.com/library/windows/hardware/ff565591) extensions display additional log information when monitoring low resources or IRQL raises and spin locks. Online help is also available.
    -   *Flags* set with 0x4 causes the display to include a log of faults injected by Driver Verifier during low resources simulation
    -   *Flags* set with 0x8 causes the display to include a log of the most recent IRQL changes made by the drivers being verified
    -   If *Flags* equals exactly 0x4 or 0x8, the Quantity parameter specifies the number of records or log entries to include in the display
    -   The **?** parameter shows a brief help text
-   **New !gdikdx.verifier extensions**

    A new **!gdikdx.verifier** extension, **!gdikdx.verifier -s**, lists statistics about the GDI callback functions called during low resources simulation for graphics drivers.

-   Online Help for Driver Verifier Manager Online Help for Driver Verifier Manager can be displayed in either of the following ways:
    -   Right-click an item in the Driver Verifier Manager window and choose **What's This?** from the pop-up menu.
    -   Click the question mark (**?**) in the upper-right corner of the window and then click an item in the Driver Verifier Manager window.

 

 





