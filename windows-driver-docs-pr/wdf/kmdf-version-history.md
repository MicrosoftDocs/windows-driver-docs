---
title: KMDF Version History
description: This topic lists versions of Kernel-Mode Driver Framework (KMDF), the corresponding versions of the Windows operating system, and the changes made in each release.
ms.assetid: b920937c-2e5d-48cc-81b5-1462f5d03d75
keywords:
- kernel-mode drivers WDK KMDF , revision history
- KMDF WDK , revision history
- Kernel-Mode Driver Framework WDK , revision history
ms.date: 10/02/2018
ms.localizationpriority: medium
---

# KMDF Version History


This topic lists versions of Kernel-Mode Driver Framework (KMDF), the corresponding versions of the Windows operating system, and the changes made in each release.

The following table shows the release history of the KMDF library:

|KMDF version|Release method|Included in this version of Windows|Drivers using it run on|
|--- |--- |--- |--- |
|1.27|Windows 10, version 1809 WDK|Windows 10, version 1809 (October 2018 Update, Redstone 5)|Windows 10, version 1809|
|1.25|Windows 10, version 1803 WDK|Windows 10, version 1803 (April 2018 Update, Redstone 4)|Windows 10, version 1803|
|1.23|Windows 10, version 1709 WDK|Windows 10, version 1709 (Fall Creators Update, Redstone 3)|Windows 10, version 1709|
|1.21|Windows 10, version 1703 WDK|Windows 10, version 1703 (Creators Update, Redstone 2)|Windows 10, version 1703|
|1.19|Windows 10, version 1607 WDK|Windows 10, version 1607 (Anniversary Update, Redstone 1)|Windows 10 version 1607, Windows Server 2016 and later|
|1.17|Windows 10, version 1511 WDK|Windows 10, version 1511 (November Update, Threshold 2)|Windows 10 version 1511, Windows Server 2016 and later|
|1.15|Windows 10 WDK|Windows 10, version 1507 (Threshold 1)|Windows 10, version 1507, Windows Server 2016 and later|
|1.13|Windows 8.1 WDK|Windows 8.1|Windows 8.1 and later|
|1.11|Windows 8 WDK|Windows 8|Windows Vista and later|
|1.9|Windows 7 WDK|Windows 7|Windows XP and later|
|1.7|Windows Server 2008 WDK|Windows Vista with Service Pack 1 (SP1), Windows Server 2008|Windows 2000 and later|
|1.5|Windows Vista WDK|Windows Vista|Windows 2000 and later|
|1.1|Download only|None|Windows 2000 and later|
|1.0|Download only|None|Windows XP and later|

You can use the Windows Driver Kit (WDK) with Microsoft Visual Studio 2017 to build drivers that run on Windows 7 and later.

For a complete list of callbacks and methods, and which frameworks and versions they apply to, see [Summary of WDF Callbacks and Methods](https://msdn.microsoft.com/library/windows/hardware/dn265591).

For information about the new features for KMDF drivers in Windows 10, see [What's New for WDF Drivers](index.md).

## KMDF Version 1.27

Unchanged from version 1.25.

## KMDF Version 1.25

* [Building a WDF driver for multiple versions of Windows](building-a-wdf-driver-for-multiple-versions-of-windows.md)

## KMDF Version 1.23

* Companion functionality added for internal use only.  For the new DDIs, see [Summary of WDF Callbacks and Methods](https://msdn.microsoft.com/library/windows/hardware/dn265591).

## KMDF Version 1.21

* [**WdfFileObjectGetInitiatorProcessId**](https://msdn.microsoft.com/library/windows/hardware/dn265614) was previously UMDF-only, now available in KMDF.
* [**WdfRequestGetRequestorProcessId**](https://msdn.microsoft.com/library/windows/hardware/dn265617) was previously UMDF-only, now available in KMDF.
* [**WdfObjectDereferenceActual**](https://msdn.microsoft.com/library/windows/hardware/ff548743): Type of *File* parameter changed from PCHAR to PCCH.
* [**WdfObjectReferenceActual**](https://msdn.microsoft.com/library/windows/hardware/ff548760): Type of *File* parameter changed from PCHAR to PCCH.

## KMDF Version 1.19

* Added [**WdfDmaTransactionSetSingleTransferRequirement**](https://msdn.microsoft.com/library/windows/hardware/988c7e70-3b2a-4a0f-91cf-dfab3ea07f05)
* Added **WDF_DMA_ENABLER_CONFIG_REQUIRE_SINGLE_TRANSFER** flag in [**WDF_DMA_ENABLER_CONFIG_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/hh439491)
* Added **STATUS_WDF_TOO_MANY_TRANSFERS** return value for [**WdfDmaTransactionInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff547099) and [**WdfDmaTransactionDmaCompleted**](https://msdn.microsoft.com/library/windows/hardware/ff547039)
* Added output messages for single transfer output to [**!wdfkd.wdfdmatransaction**](https://msdn.microsoft.com/library/windows/hardware/ff565721) and [**!wdfkd.wdfdmaenabler**](https://msdn.microsoft.com/library/windows/hardware/ff565717)
* For more info about single transfer DMA, see [Using Single Transfer DMA](using-single-transfer-dma.md).

## KMDF Version 1.15

-   The new [**WdfDeviceOpenDevicemapKey**](https://msdn.microsoft.com/library/windows/hardware/dn932458) method allows a driver to access subkeys and values under **HKEY\_LOCAL\_MACHINE\\HARDWARE\\DEVICEMAP**.

## KMDF Version 1.13


KMDF version 1.13 adds the following functionality:

-   Added **CanWakeDevice** member to [**WDF\_INTERRUPT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552347) structure to support interrupts that can be used to bring a device from a low-power Dx state back to its fully on D0 state. For more information, see [Using an Interrupt to Wake a Device](using-an-interrupt-to-wake-a-device.md).
-   Support for high resolution timers. For more information, see [Using Timers](using-timers.md).
-   Support for timers that do not wake the system if they expire when the system is in a low-power state. For more information, see [Using Timers](using-timers.md).
-   The following KMDF/UMDF methods described in [Accessing the Unified Device Property Model](accessing-the-unified-device-property-model.md):
    -   [**WdfDeviceAllocAndQueryPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/dn265599)
    -   [**WdfDeviceAssignProperty**](https://msdn.microsoft.com/library/windows/hardware/dn265601)
    -   [**WdfDeviceInitSetIoTypeEx**](https://msdn.microsoft.com/library/windows/hardware/dn265604)
    -   [**WdfDeviceQueryPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/dn265608)
    -   [**WdfFdoInitAllocAndQueryPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/dn265612)
    -   [**WdfFdoInitQueryPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/dn265613)

For information about UMDF versions, see [UMDF Version History](umdf-version-history.md).

## KMDF Version 1.11


Version 1.11 adds the following functionality:

-   [System-mode DMA](supporting-system-mode-dma.md)

-   Support for [passive-level interrupts](supporting-passive-level-interrupts.md)

-   [Functional power states](supporting-functional-power-states.md) for multiple components within a single device

-   [Dispatching IRPs to I/O Queues](dispatching-irps-to-i-o-queues.md)
-   The following methods:
    -   [**WdfDeviceConfigureWdmIrpDispatchCallback**](https://msdn.microsoft.com/library/windows/hardware/hh451093)
    -   [**WdfDeviceInitSetReleaseHardwareOrderOnFailure**](https://msdn.microsoft.com/library/windows/hardware/hh706196)
    -   [**WdfDeviceInitSetRemoveLockOptions**](https://msdn.microsoft.com/library/windows/hardware/hh451095)
    -   [**WdfDeviceWdmDispatchIrp**](https://msdn.microsoft.com/library/windows/hardware/hh451100)
    -   [**WdfDmaEnablerConfigureSystemProfile**](https://msdn.microsoft.com/library/windows/hardware/hh451108)
    -   [**WdfDmaTransactionAllocateResources**](https://msdn.microsoft.com/library/windows/hardware/hh451123)
    -   [**WdfDmaTransactionCancel**](https://msdn.microsoft.com/library/windows/hardware/hh451127)
    -   [**WdfDmaTransactionFreeResources**](https://msdn.microsoft.com/library/windows/hardware/hh451177)
    -   [**WdfDmaTransactionGetTransferInfo**](https://msdn.microsoft.com/library/windows/hardware/hh451179)
    -   [**WdfDmaTransactionInitializeUsingOffset**](https://msdn.microsoft.com/library/windows/hardware/hh451182)
    -   [**WdfDmaTransactionSetChannelConfigurationCallback**](https://msdn.microsoft.com/library/windows/hardware/hh451184)
    -   [**WdfDmaTransactionSetDeviceAddressOffset**](https://msdn.microsoft.com/library/windows/hardware/hh451188)
    -   [**WdfDmaTransactionSetImmediateExecution**](https://msdn.microsoft.com/library/windows/hardware/hh451190)
    -   [**WdfDmaTransactionSetTransferCompleteCallback**](https://msdn.microsoft.com/library/windows/hardware/hh439261)
    -   [**WdfDmaTransactionWdmGetTransferContext**](https://msdn.microsoft.com/library/windows/hardware/hh439267)
    -   [**WdfInterruptQueueWorkItemForIsr**](https://msdn.microsoft.com/library/windows/hardware/hh439270)
    -   [**WdfInterruptReportActive**](https://msdn.microsoft.com/library/windows/hardware/hh439273)
    -   [**WdfInterruptReportInactive**](https://msdn.microsoft.com/library/windows/hardware/hh439277)
    -   [**WdfInterruptTryToAcquireLock**](https://msdn.microsoft.com/library/windows/hardware/hh439284)
    -   [**WdfIoQueueStopAndPurge**](https://msdn.microsoft.com/library/windows/hardware/hh439289)
    -   [**WdfIoQueueStopAndPurgeSynchronously**](https://msdn.microsoft.com/library/windows/hardware/hh439293)
    -   [**WdfIoTargetPurge**](https://msdn.microsoft.com/library/windows/hardware/hh439338)
    -   [**WdfUsbTargetDeviceCreateIsochUrb**](https://msdn.microsoft.com/library/windows/hardware/hh439420)
    -   [**WdfUsbTargetDeviceCreateUrb**](https://msdn.microsoft.com/library/windows/hardware/hh439423)
    -   [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428)
    -   [**WdfUsbTargetDeviceQueryUsbCapability**](https://msdn.microsoft.com/library/windows/hardware/hh439434)
-   Added [*EvtDeviceUsageNotificationEx*](https://msdn.microsoft.com/library/windows/hardware/hh406365).

-   Added **IdleTimeoutType** and **ExcludeD3Cold** members to [**WDF\_DEVICE\_POWER\_POLICY\_IDLE\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/ff551270).

-   Added **ReportInactiveOnPowerDown** member to [**WDF\_INTERRUPT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552347).

-   Added **WdfIoTargetPurged** value to [**WDF\_IO\_TARGET\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff552390).

-   Added **WdfSpecialFileBoot** value to [**WDF\_SPECIAL\_FILE\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff552509).

-   Added **DbgWaitForSignalTimeoutInSec** to [Registry Values for Debugging Framework-based Drivers](registry-values-for-debugging-kmdf-drivers.md).

-   Added [InstallWdf](http://go.microsoft.com/fwlink/p/?linkid=256122), [MultiComp](http://go.microsoft.com/fwlink/p/?linkid=256158), and [SingleComp](http://go.microsoft.com/fwlink/p/?linkid=256158) samples.

## KMDF Version 1.9


Version 1.9 adds the following functionality:

-   [Guaranteed forward progress](guaranteeing-forward-progress-of-i-o-operations.md) for I/O queues

-   Support for [requeuing I/O requests](requeuing-i-o-requests.md) from a child device's I/O queue to a parent device's I/O queue

-   Ability to specify [queue-level synchronization](https://msdn.microsoft.com/library/windows/hardware/ff552518) for individual queue objects.

-   The following methods:
    -   [**WdfDeviceGetSystemPowerAction**](https://msdn.microsoft.com/library/windows/hardware/ff546022)
    -   [**WdfDeviceRemoveDependentUsageDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff546829)
    -   [**WdfInterruptSetExtendedPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff547381)
    -   [**WdfPdoInitAllowForwardingRequestToParent**](https://msdn.microsoft.com/library/windows/hardware/ff548789)
    -   [**WdfPdoInitAssignContainerID**](https://msdn.microsoft.com/library/windows/hardware/ff548792)
    -   [**WdfPreDeviceInstallEx**](https://msdn.microsoft.com/library/windows/hardware/ff548839)
    -   [**WdfRequestForwardToParentDeviceIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff549959)
    -   [**WdfRequestMarkCancelableEx**](https://msdn.microsoft.com/library/windows/hardware/ff549984)
-   Added the **NumberOfPresentedRequests** member to the [**WDF\_IO\_QUEUE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552359) structure so drivers can limit the number of I/O requests that the framework delivers to the driver from a parallel I/O queue.

-   Added the **WdfFileObjectCanBeOptional** flag to the [**WDF\_FILEOBJECT\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff551315) structure.

-   Added the **TolerableDelay** member to the [**WDF\_TIMER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552519) structure.

-   Added [WdfDefaultIdleInWorkingState and WdfDefaultWakeFromSleepState](user-control-of-device-idle-and-wake-behavior.md) registry values.

## KMDF Version 1.7


-   The [**WdfDeviceEnqueueRequest**](https://msdn.microsoft.com/library/windows/hardware/ff545945) method can be called at IRQL&lt;=DISPATCH\_LEVEL.

-   The [**WdfWorkItemEnqueue**](https://msdn.microsoft.com/library/windows/hardware/ff551203) method can be called if the specified work item is already on the work-item queue.

-   Added the [*EvtDeviceArmWakeFromSxWithReason*](https://msdn.microsoft.com/library/windows/hardware/ff540846) event callback function.

-   Added **ArmForWakeIfChildrenAreArmedForWake** and **IndicateChildWakeOnParentWake** members to the [**WDF\_DEVICE\_POWER\_POLICY\_WAKE\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/ff551277) structure.

## KMDF Version 1.5


-   [**WdfUsbInterfaceGetNumSettings**](https://msdn.microsoft.com/library/windows/hardware/ff550070)

-   Added the **DriverPoolTag** member to [**WDF\_DRIVER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551300).

## KMDF Version 1.1


-   The following methods:
    -   [**WdfCommonBufferCreateWithConfig**](https://msdn.microsoft.com/library/windows/hardware/ff545805)
    -   [**WdfDmaEnablerGetFragmentLength**](https://msdn.microsoft.com/library/windows/hardware/ff546986)
    -   [**WdfDmaEnablerWdmGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff547020)

## KMDF Version 1.0


Initial release.

 

 





