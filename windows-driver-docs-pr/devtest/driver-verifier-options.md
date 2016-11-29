---
title: Driver Verifier Options
description: Driver Verifier Options
ms.assetid: f251fe07-e68e-4d93-9aa5-9a0bc818756d
keywords: ["Driver Verifier WDK , options listed", "errors WDK Driver Verifier"]
---

# Driver Verifier Options


## <span id="ddk_driver_verifier_options_tools"></span><span id="DDK_DRIVER_VERIFIER_OPTIONS_TOOLS"></span>


The following sections describe the optional features of Driver Verifier. See [Standard settings](#standard-options) for the list of options included when you use the standard settings.

-   [Automatic Checks](automatic-checks.md)

    These checks are always performed on a driver that is being verified, regardless of which options have been selected. If the driver uses memory at an improper IRQL, improperly calls or releases spin locks and memory allocations, improperly switches stacks, or frees memory pool without first removing timers, Driver Verifier will detect this behavior. When the driver is unloaded, Driver Verifier will check to see that it has properly released its resources.

-   [Special Pool](special-pool.md)

    When this option is active, Driver Verifier allocates most of the driver's memory requests from a special pool. This special pool is monitored for memory overruns, memory underruns, and memory that is accessed after it is freed.

-   [Force IRQL Checking](force-irql-checking.md)

    When this option is active, Driver Verifier places extreme memory pressure on the driver by invalidating pageable code. If the driver attempts to access paged memory at the wrong IRQL or while holding a spin lock, Driver Verifier detects this behavior.

-   [Low Resources Simulation](low-resources-simulation.md) (called *Randomized low resources simulation* in Windows 8.1)

    When this option is active, Driver Verifier randomly fails pool allocation requests and other resource requests. By injecting these allocation faults into the system, Driver Verifier tests the driver's ability to cope with a low-resource situation.

-   [Pool Tracking](pool-tracking.md)

    When this option is active, Driver Verifier checks to see if the driver has freed all its memory allocations when it is unloaded. This reveals memory leaks.

-   [I/O Verification](i-o-verification.md)

    When this option is active, Driver Verifier allocates the driver's IRPs from a special pool, and monitors the driver's I/O handling. This detects illegal or inconsistent use of I/O routines.

-   [Deadlock Detection](deadlock-detection.md)

    (Windows XP and later) When this option is active, Driver Verifier monitors the driver's use of spin locks, mutexes, and fast mutexes. This detects if the driver's code has the potential for causing a deadlock at some point.

-   [Enhanced I/O Verification](enhanced-i-o-verification.md)

    (Windows XP and later) When this option is active, Driver Verifier monitors the calls of several I/O Manager routines and performs stress testing of PnP IRPs, power IRPs and WMI IRPs. In Windows 7 and later versions of the Windows operating system, all the features of Enhanced I/O Verification are included as part of [I/O Verification](i-o-verification.md) and it is no longer available nor necessary to select this option in Driver Verifier Manager or from the command line.

-   [DMA Verification](dma-verification.md)

    (Windows XP and later) When this option is active, Driver Verifier monitors the driver's use of DMA routines. This detects improper use of DMA buffers, adapters, and map registers.

-   [Security Checks](security-checks.md)

    (Windows Vista and later) When this option is active, Driver Verifier looks for common errors that can result in security vulnerabilities, such as a reference to user-mode addresses by kernel-mode routines.

-   [Miscellaneous Checks](miscellaneous-checks.md)

    (Windows Vista and later) When this option is active, Driver Verifier looks for common causes of driver crashes, such as the mishandling of freed memory.

-   [Force Pending I/O Requests](force-pending-i-o-requests.md)

    (Windows Vista and later) When this option is active, Driver Verifier tests the driver's response to STATUS\_PENDING return values by returning STATUS\_PENDING for random calls to [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

-   [IRP Logging](irp-logging.md)

    (Windows Server 2003 and later) When this option is active, Driver Verifier monitors a driver's use of IRPs and creates a log of IRP use.

-   [Disk Integrity Checking](disk-integrity-checking.md)

    (Introduced in Windows Server 2003. Not available in Windows 7 and later.) When this option is active, Driver Verifier monitors hard disk access, and detects whether the disk is preserving its data correctly.

-   [SCSI Verification](scsi-verification.md)

    (Windows XP and later) When this option is active, Driver Verifier monitors a SCSI miniport driver for improper use of exported SCSI port routines, excessive delays, and improper handling of SCSI requests.

-   [Storport Verification](dv-storport-verification.md)

    (Windows Vista and later) When this option is active, Driver Verifier monitors a Storport miniport driver for improper use of exported Storport routines, excessive delays, and improper handling of Storport requests.

-   [Power Framework Delay Fuzzing](concurrency-stress-test.md)

    (Starting with Windows 8) When this option is active, Driver Verifier randomizes thread schedules to help flush out concurrency errors in the drivers that use the [power management framework (PoFx)](https://msdn.microsoft.com/library/windows/hardware/hh406637). This option is not recommended for drivers that do not directly utilize the power management framework (PoFx)..

-   [DDI compliance checking](ddi-compliance-checking.md)

    (Starting with Windows 8) When this option is active, Driver Verifier applies a set of device driver interface (DDI) rules that check for the proper interaction between a driver and the kernel interface of the operating system.

-   [Invariant MDL Checking for Stack](invariant-mdl-checking-for-stack.md)

    (Starting with Windows 8) The [Invariant MDL Checking for Stack](invariant-mdl-checking-for-stack.md) option monitors how the driver handles invariant MDL buffers across the driver stack. Driver Verifier can detect illegal modification of invariant MDL buffers. To use this option, I/O Verification must be enabled on at least one driver.

-   [Invariant MDL Checking for Driver](invariant-mdl-checking-for-driver.md)

    (Starting with Windows 8) The [Invariant MDL Checking for Driver](invariant-mdl-checking-for-driver.md) option monitors how the driver handles invariant MDL buffers on a per-driver basis. This option detects illegal modification of invariant MDL buffers. To use this option, you must enable I/O Verification on at least one driver.

-   [Stack Based Failure Injection](stack-based-failure-injection.md)

    (Only available with Windows 8 and WDK 8) The [Stack Based Failure Injection](stack-based-failure-injection.md) option injects resource failures in kernel mode drivers. This option uses a special driver, KmAutoFail.sys, in conjunction with [Driver Verifier](driver-verifier.md) to penetrate driver error handling paths.

-   [Systematic low resources simulation](systematic-low-resource-simulation.md)

    (Starting with Windows 8.1) The [Systematic low resources simulation](systematic-low-resource-simulation.md) option injects resource failures in kernel mode drivers.

-   [NDIS/WIFI verification](ndis-wifi-verification.md)

    (Starting with Windows 8.1) When this option is active, Driver Verifier applies a set of NDIS and wireless LAN (WIFI) rules that check for the proper interaction between an NDIS miniport driver and the operating system kernel.

-   [Kernel synchronization delay fuzzing](kernel-synchronization-delay-fuzzing.md)

    (Starting with Windows 8.1) This option randomizes thread schedules to help detect concurrency bugs in drivers.

-   [VM switch verification](vm-switch-verification.md)

    (Starting with Windows 8.1) This option monitors filter drivers (*extensible switch extensions*) that run inside the [Hyper-V Extensible Switch](https://msdn.microsoft.com/library/windows/hardware/hh598161).

## <span id="standard_options"></span><span id="STANDARD_OPTIONS"></span>Standard settings


<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Options included in the standard settings</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[Special Pool](special-pool.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Force IRQL Checking](force-irql-checking.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Pool Tracking](pool-tracking.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[I/O Verification](i-o-verification.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Deadlock Detection](deadlock-detection.md) (Windows XP and later)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Enhanced I/O Verification](enhanced-i-o-verification.md) (In Windows 7 and later, this option is automatically activated when you select I/O Verification)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[DMA Verification](dma-verification.md) (Windows XP and later)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Security Checks](security-checks.md) (Windows XP and later)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Miscellaneous Checks](miscellaneous-checks.md) (Windows Vista and later)</p></td>
</tr>
<tr class="even">
<td align="left">[DDI compliance checking](ddi-compliance-checking.md) (Starting with Windows 8)</td>
</tr>
</tbody>
</table>

 

## <span id="Driver_Verifier_options_that_require_I_O_Verification"></span><span id="driver_verifier_options_that_require_i_o_verification"></span><span id="DRIVER_VERIFIER_OPTIONS_THAT_REQUIRE_I_O_VERIFICATION"></span>Driver Verifier options that require I/O Verification


There are four options that require you to first enable [I/O Verification](i-o-verification.md). If I/O Verification is not enabled, these options are not enabled.

-   [Force Pending I/O Requests](force-pending-i-o-requests.md)
-   [IRP Logging](irp-logging.md)
-   [Invariant MDL Checking for Stack](invariant-mdl-checking-for-stack.md)
-   [Invariant MDL Checking for Driver](invariant-mdl-checking-for-driver.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Driver%20Verifier%20Options%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




