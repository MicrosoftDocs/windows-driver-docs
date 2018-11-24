---
title: Driver Verifier Options
description: Driver Verifier options and rule classes
ms.assetid: f251fe07-e68e-4d93-9aa5-9a0bc818756d
keywords:
- Driver Verifier WDK , options listed
- errors WDK Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Verifier options and rule classes


This topic describes the optional features and rule classes within Driver Verifier. 
See [Standard settings](#standard-settings) for the list of options included when you use the standard settings.

> [!NOTE]
> Some [automatic checks](automatic-checks.md) are always performed on a driver that is being verified, regardless of which options have been selected. If the driver uses memory at an improper IRQL, improperly calls or releases spin locks and memory allocations, improperly switches stacks, or frees memory pool without first removing timers, Driver Verifier will detect this behavior. When the driver is unloaded, Driver Verifier will check to see that it has properly released its resources.

## Enabling rule classes with /ruleclasses

Starting in Windows 10, version 17627 and later, you can enable rule classes with the following syntax:

`/ruleclasses or /rc [<ruleclass_1> <ruleclass_2> ... <ruleclass_k>]`

Note that when enabling multiple classes (represented by the positive decimal integer below), separate each integer with a space character. 

Descriptions for these rule classes can be found below.

### Standard rule classes

| Rule class | Decimal ID |
| -- | -- |
| Special pool        | 1 |
| Force IRQL checking | 2 |
| Pool tracking       | 4 |
| I/O verification    | 5 |
| Deadlock detection  | 6 |
| DMA checking | 8 |
| Security checks | 9 |
| Miscellaneous checks | 12 |
| DDI compliance checking | 18 |
| WDF Verification | 34 |

### Additional rule classes

These rule classes are intended for specific scenario testing. 
Rule classes are marked with (\*) require I/O Verification (5) that will be automatically enabled. Flags marked with (\**) support disabling of individual rules.

| Rule class | Decimal ID |
| -- | -- |
| Randomized low resources simulation        | 3 |
| Force pending I/O requests (*) | 10 |
| IRP logging       | 11 |
| Invariant MDL checking for stack (*)    | 14 |
| Invariant MDL checking for driver (*)  | 15 |
| Power framework delay fuzzing | 16 |
| Port/miniport interface checking | 17 |
| Systematic low resources simulation | 19 |
| DDI compliance checking (additional) | 20 |
| Kernel synchronization delay fuzzing | 24 |
| VM switch verification | 25 |
| Code integrity checks | 22 |

## Optional feature and rule class descriptions 

[Special Pool](special-pool.md)
    
When this option is enabled, Driver Verifier allocates most of the driver's memory requests from a special pool. This special pool is monitored for memory overruns, memory underruns, and memory that is accessed after it is freed.

[Force IRQL Checking](force-irql-checking.md)

When this option is enabled, Driver Verifier places extreme memory pressure on the driver by invalidating pageable code. If the driver attempts to access paged memory at the wrong IRQL or while holding a spin lock, Driver Verifier detects this behavior.

[Low Resources Simulation](low-resources-simulation.md) (called *Randomized low resources simulation* in Windows 8.1)

When this option is enabled, Driver Verifier randomly fails pool allocation requests and other resource requests. By injecting these allocation faults into the system, Driver Verifier tests the driver's ability to cope with a low-resource situation.

[Pool Tracking](pool-tracking.md)

When this option is enabled, Driver Verifier checks to see if the driver has freed all its memory allocations when it is unloaded. This reveals memory leaks.

[I/O Verification](i-o-verification.md)

When this option is active, Driver Verifier allocates the driver's IRPs from a special pool, and monitors the driver's I/O handling. This detects illegal or inconsistent use of I/O routines.

[Deadlock Detection](deadlock-detection.md)

(Windows XP and later) When this option is active, Driver Verifier monitors the driver's use of spin locks, mutexes, and fast mutexes. This detects if the driver's code has the potential for causing a deadlock at some point.

[Enhanced I/O Verification](enhanced-i-o-verification.md)

(Windows XP and later) When this option is active, Driver Verifier monitors the calls of several I/O Manager routines and performs stress testing of PnP IRPs, power IRPs and WMI IRPs. In Windows 7 and later versions of the Windows operating system, all the features of Enhanced I/O Verification are included as part of [I/O Verification](i-o-verification.md) and it is no longer available nor necessary to select this option in Driver Verifier Manager or from the command line.

[DMA Verification](dma-verification.md)

(Windows XP and later) When this option is active, Driver Verifier monitors the driver's use of DMA routines. This detects improper use of DMA buffers, adapters, and map registers.

[Security Checks](security-checks.md)

(Windows Vista and later) When this option is active, Driver Verifier looks for common errors that can result in security vulnerabilities, such as a reference to user-mode addresses by kernel-mode routines.

[Miscellaneous Checks](miscellaneous-checks.md)

(Windows Vista and later) When this option is active, Driver Verifier looks for common causes of driver crashes, such as the mishandling of freed memory.

[Force Pending I/O Requests](force-pending-i-o-requests.md)

(Windows Vista and later) When this option is active, Driver Verifier tests the driver's response to STATUS\_PENDING return values by returning STATUS\_PENDING for random calls to [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

[IRP Logging](irp-logging.md)

(Windows Server 2003 and later) When this option is active, Driver Verifier monitors a driver's use of IRPs and creates a log of IRP use.

[Disk Integrity Checking](disk-integrity-checking.md)

(Introduced in Windows Server 2003. Not available in Windows 7 and later.) When this option is active, Driver Verifier monitors hard disk access, and detects whether the disk is preserving its data correctly.

[SCSI Verification](scsi-verification.md)

(Windows XP and later) When this option is active, Driver Verifier monitors a SCSI miniport driver for improper use of exported SCSI port routines, excessive delays, and improper handling of SCSI requests.

[Storport Verification](dv-storport-verification.md)

(Windows Vista and later) When this option is active, Driver Verifier monitors a Storport miniport driver for improper use of exported Storport routines, excessive delays, and improper handling of Storport requests.

[Power Framework Delay Fuzzing](concurrency-stress-test.md)

(Starting with Windows 8) When this option is active, Driver Verifier randomizes thread schedules to help flush out concurrency errors in the drivers that use the [power management framework (PoFx)](https://msdn.microsoft.com/library/windows/hardware/hh406637). This option is not recommended for drivers that do not directly utilize the power management framework (PoFx)..

[DDI compliance checking](ddi-compliance-checking.md)

(Starting with Windows 8) When this option is active, Driver Verifier applies a set of device driver interface (DDI) rules that check for the proper interaction between a driver and the kernel interface of the operating system.

[Invariant MDL Checking for Stack](invariant-mdl-checking-for-stack.md)

(Starting with Windows 8) The [Invariant MDL Checking for Stack](invariant-mdl-checking-for-stack.md) option monitors how the driver handles invariant MDL buffers across the driver stack. Driver Verifier can detect illegal modification of invariant MDL buffers. To use this option, I/O Verification must be enabled on at least one driver.

[Invariant MDL Checking for Driver](invariant-mdl-checking-for-driver.md)

(Starting with Windows 8) The [Invariant MDL Checking for Driver](invariant-mdl-checking-for-driver.md) option monitors how the driver handles invariant MDL buffers on a per-driver basis. This option detects illegal modification of invariant MDL buffers. To use this option, you must enable I/O Verification on at least one driver.

[Stack Based Failure Injection](stack-based-failure-injection.md)

(Only available with Windows 8 and WDK 8) The [Stack Based Failure Injection](stack-based-failure-injection.md) option injects resource failures in kernel mode drivers. This option uses a special driver, KmAutoFail.sys, in conjunction with [Driver Verifier](driver-verifier.md) to penetrate driver error handling paths.

[Systematic low resources simulation](systematic-low-resource-simulation.md)

(Starting with Windows 8.1) The [Systematic low resources simulation](systematic-low-resource-simulation.md) option injects resource failures in kernel mode drivers.

[NDIS/WIFI verification](ndis-wifi-verification.md)

(Starting with Windows 8.1) When this option is active, Driver Verifier applies a set of NDIS and wireless LAN (WIFI) rules that check for the proper interaction between an NDIS miniport driver and the operating system kernel.

[Kernel synchronization delay fuzzing](kernel-synchronization-delay-fuzzing.md)

(Starting with Windows 8.1) This option randomizes thread schedules to help detect concurrency bugs in drivers.

[VM switch verification](vm-switch-verification.md)

(Starting with Windows 8.1) This option monitors filter drivers (*extensible switch extensions*) that run inside the [Hyper-V Extensible Switch](https://msdn.microsoft.com/library/windows/hardware/hh598161).

[Port/Miniport interface checking](port-miniport-interface-checking.md)

Port/miniport interface checking enables Driver Verifier to inspect the DDI interface between PortCls.sys and its audio miniport drivers, along with ks.sys and its AVStream miniport drivers. See Rules for AVStream drivers and Rules for audio drivers.

[Code integrity checking](code-integrity-checking.md)

When using virtualization-based security to isolate Code Integrity, the only way kernel memory can become executable is through a Code Integrity verification. This means that kernel memory pages can never be Writable and Executable (W+X) and executable code cannot be directly modified. The code integrity checks ensure compatibility of these code integrity rules, and detects violations.

[WDF verification](wdf-verification.md)

WDF Verification checks if a kernel-mode driver is following the Kernel-Mode Driver Framework (KMDF) requirements properly. 


## Standard settings

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
<td align="left"><p><a href="special-pool.md" data-raw-source="[Special Pool](special-pool.md)">Special Pool</a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="force-irql-checking.md" data-raw-source="[Force IRQL Checking](force-irql-checking.md)">Force IRQL Checking</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="pool-tracking.md" data-raw-source="[Pool Tracking](pool-tracking.md)">Pool Tracking</a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="i-o-verification.md" data-raw-source="[I/O Verification](i-o-verification.md)">I/O Verification</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="deadlock-detection.md" data-raw-source="[Deadlock Detection](deadlock-detection.md)">Deadlock Detection</a> (Windows XP and later)</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="enhanced-i-o-verification.md" data-raw-source="[Enhanced I/O Verification](enhanced-i-o-verification.md)">Enhanced I/O Verification</a> (In Windows 7 and later, this option is automatically activated when you select I/O Verification)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="dma-verification.md" data-raw-source="[DMA Verification](dma-verification.md)">DMA Verification</a> (Windows XP and later)</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="security-checks.md" data-raw-source="[Security Checks](security-checks.md)">Security Checks</a> (Windows XP and later)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="miscellaneous-checks.md" data-raw-source="[Miscellaneous Checks](miscellaneous-checks.md)">Miscellaneous Checks</a> (Windows Vista and later)</p></td>
</tr>
<tr class="even">
<td align="left"><a href="ddi-compliance-checking.md" data-raw-source="[DDI compliance checking](ddi-compliance-checking.md)">DDI compliance checking</a> (Starting with Windows 8)</td>
</tr>
</tbody>
</table>

 

## Driver Verifier options that require I/O Verification


There are four options that require you to first enable [I/O Verification](i-o-verification.md). If I/O Verification is not enabled, these options are not enabled.

-   [Force Pending I/O Requests](force-pending-i-o-requests.md)
-   [IRP Logging](irp-logging.md)
-   [Invariant MDL Checking for Stack](invariant-mdl-checking-for-stack.md)
-   [Invariant MDL Checking for Driver](invariant-mdl-checking-for-driver.md)

 

 





