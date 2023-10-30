---
title: KMDF Version History
description: This topic lists versions of Kernel-Mode Driver Framework (KMDF), the corresponding versions of the Windows operating system, and the changes made in each release.
keywords:
- kernel-mode drivers WDK KMDF , revision history
- KMDF WDK , revision history
- Kernel-Mode Driver Framework WDK , revision history
ms.date: 03/24/2023
---

# KMDF Version History

This topic lists versions of Kernel-Mode Driver Framework (KMDF), the corresponding versions of the Windows operating system, and the changes made in each release.

The following table shows the release history of the KMDF library. You can use the **In this article** sidebar on the right to navigate quickly to a specific version.

| KMDF version | Release method               | Included in this version of Windows                          | Drivers using it run on                                 |
|--------------|------------------------------|--------------------------------------------------------------|---------------------------------------------------------|
| 1.33         | Windows 11 WDK; WDK for Windows Server 2022 | Windows 11, version 21H2 (Cobalt); Windows Server 2022 (Iron)                              | Windows 11, version 21H2; Windows Server 2022 and later               |
| 1.31         | Windows 10, version 2004 WDK | Windows 10, version 2004 (May 2020 Update, Vibranium)        | Windows 10, version 2004 and later                      |
| 1.29         | Not released in WDK          | Windows 10, version 1903 (March 2019 Update, 19H1)           | Windows 10, version 1903 and later                      |
| 1.27         | Windows 10, version 1809 WDK | Windows 10, version 1809 (October 2018 Update, Redstone 5)   | Windows 10, version 1809 and later                      |
| 1.25         | Windows 10, version 1803 WDK | Windows 10, version 1803 (April 2018 Update, Redstone 4)     | Windows 10, version 1803 and later                      |
| 1.23         | Windows 10, version 1709 WDK | Windows 10, version 1709 (Fall Creators Update, Redstone 3)  | Windows 10, version 1709 and later                      |
| 1.21         | Windows 10, version 1703 WDK | Windows 10, version 1703 (Creators Update, Redstone 2)       | Windows 10, version 1703 and later                      |
| 1.19         | Windows 10, version 1607 WDK | Windows 10, version 1607 (Anniversary Update, Redstone 1)    | Windows 10 version 1607, Windows Server 2016 and later  |
| 1.17         | Windows 10, version 1511 WDK | Windows 10, version 1511 (November Update, Threshold 2)      | Windows 10 version 1511, Windows Server 2016 and later  |
| 1.15         | Windows 10 WDK               | Windows 10, version 1507 (Threshold 1)                       | Windows 10, version 1507, Windows Server 2016 and later |
| 1.13         | Windows 8.1 WDK              | Windows 8.1                                                  | Windows 8.1 and later                                   |
| 1.11         | Windows 8 WDK                | Windows 8                                                    | Windows Vista and later                                 |
| 1.9          | Windows 7 WDK                | Windows 7                                                    | Windows XP and later                                    |
| 1.7          | Windows Server 2008 WDK      | Windows Vista with Service Pack 1 (SP1); Windows Server 2008 | Windows 2000 and later                                  |
| 1.5          | Windows Vista WDK            | Windows Vista                                                | Windows 2000 and later                                  |
| 1.1          | Download only                | None                                                         | Windows 2000 and later                                  |
| 1.0          | Download only                | None                                                         | Windows XP and later                                    |

You can use the Windows Driver Kit (WDK) with Microsoft Visual Studio 2019 to build drivers that run on Windows 10 and later.

For help determining what version of WDF to use, see [Which framework version should I use?](building-and-loading-a-kmdf-driver.md#which-framework-version-should-i-use).

For a complete list of callbacks and methods, and which frameworks and versions they apply to, see [Summary of WDF Callbacks and Methods](/windows-hardware/drivers/ddi/_wdf/).

For information about the new features for KMDF drivers in Windows 10, see [What's New for WDF Drivers](index.md).

For each KMDF version section below, the Windows version in which it was released is listed in parentheses.

## KMDF 1.33 (Windows 11, version 21H2; Windows Server 2022)

* For devices that specify **SystemManagedIdleTimeout** or **SystemManagedIdleTimeoutWithHint** in the [WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE](/windows-hardware/drivers/ddi/wdfdevice/ne-wdfdevice-_wdf_power_policy_idle_timeout_type) enumeration, when calling the [**WdfDeviceStopIdle**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle) macro with *WaitForD0* set to **FALSE**, if the device is still in D0 and the idle timeout period has not yet elapsed, **WdfDeviceStopIdle** returns STATUS_SUCCESS (in previous versions this resulted in a return value of STATUS_PENDING).
* [**WDF_POWER_FRAMEWORK_SETTINGS**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_power_framework_settings) structure has two new members (**PoFxDeviceFlags** and **DirectedPoFxEnabled**).

## KMDF 1.31 (Windows 10, version 2004)

* Added new API [**WdfDeviceSetDeviceInterfaceStateEx**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetdeviceinterfacestateex)
* Improved existing API [**WdfDeviceGetSystemPowerAction**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegetsystempoweraction)
* Added new API [**WdfPdoInitRemovePowerDependencyOnParent**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitremovepowerdependencyonparent)
* [Introduction to the Directed Power Management Framework](../kernel/introduction-to-the-directed-power-management-framework.md)

## KMDF 1.29 (Windows 10, version 1903)

Unchanged from version 1.25.

## KMDF 1.27 (Windows 10, version 1809)

Unchanged from version 1.25.

## KMDF 1.25 (Windows 10, version 1803)

* [Building a WDF driver for multiple versions of Windows](building-a-wdf-driver-for-multiple-versions-of-windows.md).

## KMDF 1.23 (Windows 10, version 1709)

* Companion functionality added for internal use only.  For more info, see [Wdfcompanion.h](/windows-hardware/drivers/ddi/wdfcompanion/).

## KMDF 1.21 (Windows 10, version 1703)

* [**WdfFileObjectGetInitiatorProcessId**](/windows-hardware/drivers/ddi/wdffileobject/nf-wdffileobject-wdffileobjectgetinitiatorprocessid) was previously UMDF-only, now available in KMDF.
* [**WdfRequestGetRequestorProcessId**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetrequestorprocessid) was previously UMDF-only, now available in KMDF.
* [**WdfObjectDereferenceActual**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdereferenceactual): Type of *File* parameter changed from PCHAR to PCCH.
* [**WdfObjectReferenceActual**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectreferenceactual): Type of *File* parameter changed from PCHAR to PCCH.
* Added WDF registry values **ObjectLeakDetectionLimit** and **ObjectsForLeakDetection** for debugging excessive object creation. For more info, see [Registry Values for Debugging WDF Drivers](./registry-values-for-debugging-kmdf-drivers.md).
* The SleepStudy software tool reports the number of power references that a KMDF driver has that are preventing the system from going to sleep.  For more info, see [Modern standby SleepStudy](/windows-hardware/design/device-experiences/modern-standby-sleepstudy).

## KMDF 1.19 (Windows 10, version 1607)

* Added [**WdfDmaTransactionSetSingleTransferRequirement**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionsetsingletransferrequirement)
* Added **WDF_DMA_ENABLER_CONFIG_REQUIRE_SINGLE_TRANSFER** flag in [**WDF_DMA_ENABLER_CONFIG_FLAGS**](/windows-hardware/drivers/ddi/wdfdmaenabler/ne-wdfdmaenabler-_wdf_dma_enabler_config_flags)
* Added **STATUS_WDF_TOO_MANY_TRANSFERS** return value for [**WdfDmaTransactionInitialize**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioninitialize) and [**WdfDmaTransactionDmaCompleted**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiondmacompleted)
* Added output messages for single transfer output to [**!wdfkd.wdfdmatransaction**](../debuggercmds/-wdfkd-wdfdmatransaction.md) and [**!wdfkd.wdfdmaenabler**](../debuggercmds/-wdfkd-wdfdmaenabler.md)
* For more info about single transfer DMA, see [Using Single Transfer DMA](using-single-transfer-dma.md).

## KMDF 1.15 (Windows 10, version 1507)

* The new [**WdfDeviceOpenDevicemapKey**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceopendevicemapkey) method allows a driver to access subkeys and values under **HKEY\_LOCAL\_MACHINE\\HARDWARE\\DEVICEMAP**.
* WDF source code is publicly available from [Windows Driver Frameworks](https://github.com/Microsoft/Windows-Driver-Frameworks). The private symbol files for WDF are available through the Microsoft Symbol Server. Also see [Debugging with WDF Source](https://github.com/Microsoft/Windows-Driver-Frameworks/wiki/Debugging-with-WDF-Source) and [Video: Debugging your driver with WDF source code](./video--debugging-your-driver-with-wdf-source-code.md).
* Inflight Trace Recorder (IFR) now available. Note this is separate from the [framework's event logger](./using-the-framework-s-event-logger.md). For more info, see [Inflight Trace Recorder (IFR) for logging traces](../devtest/using-wpp-recorder.md) and [Using Inflight Trace Recorder in KMDF and UMDF Drivers](using-wpp-software-tracing-in-kmdf-and-umdf-2-drivers.md).
* Support for interrupts for GPIO-backed devices. For more information, see [Creating an Interrupt Object](creating-an-interrupt-object.md).

## KMDF 1.13 (Windows 8.1)

KMDF version 1.13 adds the following functionality:

* Added **CanWakeDevice** member to [**WDF\_INTERRUPT\_CONFIG**](/windows-hardware/drivers/ddi/wdfinterrupt/ns-wdfinterrupt-_wdf_interrupt_config) structure to support interrupts that can be used to bring a device from a low-power Dx state back to its fully on D0 state. For more information, see [Using an Interrupt to Wake a Device](using-an-interrupt-to-wake-a-device.md).
* Support for high resolution timers. For more information, see [Using Timers](using-timers.md).
* Support for timers that do not wake the system if they expire when the system is in a low-power state. For more information, see [Using Timers](using-timers.md).
* The following KMDF/UMDF methods described in [Accessing the Unified Device Property Model](accessing-the-unified-device-property-model.md):
  * [**WdfDeviceAllocAndQueryPropertyEx**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandquerypropertyex)
  * [**WdfDeviceAssignProperty**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassignproperty)
  * [**WdfDeviceInitSetIoTypeEx**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetiotypeex)
  * [**WdfDeviceQueryPropertyEx**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicequerypropertyex)
  * [**WdfFdoInitAllocAndQueryPropertyEx**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitallocandquerypropertyex)
  * [**WdfFdoInitQueryPropertyEx**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitquerypropertyex)

For information about UMDF versions, see [UMDF Version History](umdf-version-history.md).

## KMDF 1.11 (Windows 8)

Version 1.11 adds the following functionality:

* [System-mode DMA](supporting-system-mode-dma.md)

* Support for [passive-level interrupts](supporting-passive-level-interrupts.md)

* [Functional power states](supporting-functional-power-states.md) for multiple components within a single device

* [Dispatching IRPs to I/O Queues](dispatching-irps-to-i-o-queues.md)
* The following methods:
  * [**WdfDeviceConfigureWdmIrpDispatchCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceconfigurewdmirpdispatchcallback)
  * [**WdfDeviceInitSetReleaseHardwareOrderOnFailure**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetreleasehardwareorderonfailure)
  * [**WdfDeviceInitSetRemoveLockOptions**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetremovelockoptions)
  * [**WdfDeviceWdmDispatchIrp**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchirp)
  * [**WdfDmaEnablerConfigureSystemProfile**](/windows-hardware/drivers/ddi/wdfdmaenabler/nf-wdfdmaenabler-wdfdmaenablerconfiguresystemprofile)
  * [**WdfDmaTransactionAllocateResources**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionallocateresources)
  * [**WdfDmaTransactionCancel**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioncancel)
  * [**WdfDmaTransactionFreeResources**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionfreeresources)
  * [**WdfDmaTransactionGetTransferInfo**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiongettransferinfo)
  * [**WdfDmaTransactionInitializeUsingOffset**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioninitializeusingoffset)
  * [**WdfDmaTransactionSetChannelConfigurationCallback**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionsetchannelconfigurationcallback)
  * [**WdfDmaTransactionSetDeviceAddressOffset**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionsetdeviceaddressoffset)
  * [**WdfDmaTransactionSetImmediateExecution**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionsetimmediateexecution)
  * [**WdfDmaTransactionSetTransferCompleteCallback**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionsettransfercompletecallback)
  * [**WdfDmaTransactionWdmGetTransferContext**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionwdmgettransfercontext)
  * [**WdfInterruptQueueWorkItemForIsr**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptqueueworkitemforisr)
  * [**WdfInterruptReportActive**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptreportactive)
  * [**WdfInterruptReportInactive**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptreportinactive)
  * [**WdfInterruptTryToAcquireLock**](/previous-versions/hh439284(v=vs.85))
  * [**WdfIoQueueStopAndPurge**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopandpurge)
  * [**WdfIoQueueStopAndPurgeSynchronously**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopandpurgesynchronously)
  * [**WdfIoTargetPurge**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetpurge)
  * [**WdfUsbTargetDeviceCreateIsochUrb**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateisochurb)
  * [**WdfUsbTargetDeviceCreateUrb**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateurb)
  * [**WdfUsbTargetDeviceCreateWithParameters**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters)
  * [**WdfUsbTargetDeviceQueryUsbCapability**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicequeryusbcapability)
* Added [*EvtDeviceUsageNotificationEx*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_usage_notification_ex).

* Added **IdleTimeoutType** and **ExcludeD3Cold** members to [**WDF\_DEVICE\_POWER\_POLICY\_IDLE\_SETTINGS**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_idle_settings).

* Added **ReportInactiveOnPowerDown** member to [**WDF\_INTERRUPT\_CONFIG**](/windows-hardware/drivers/ddi/wdfinterrupt/ns-wdfinterrupt-_wdf_interrupt_config).

* Added **WdfIoTargetPurged** value to [**WDF\_IO\_TARGET\_STATE**](/windows-hardware/drivers/ddi/wdfiotarget/ne-wdfiotarget-_wdf_io_target_state).

* Added **WdfSpecialFileBoot** value to [**WDF\_SPECIAL\_FILE\_TYPE**](/windows-hardware/drivers/ddi/wdfdevice/ne-wdfdevice-_wdf_special_file_type).

* Added **DbgWaitForSignalTimeoutInSec** to [Registry Values for Debugging Framework-based Drivers](registry-values-for-debugging-kmdf-drivers.md).

* Added [InstallWdf](/samples/browse/), [MultiComp](/samples/browse/), and [SingleComp](/samples/browse/) samples.

## KMDF 1.9 (Windows 7)

Version 1.9 adds the following functionality:

* [Guaranteed forward progress](guaranteeing-forward-progress-of-i-o-operations.md) for I/O queues

* Support for [requeuing I/O requests](requeuing-i-o-requests.md) from a child device's I/O queue to a parent device's I/O queue

* Ability to specify [queue-level synchronization](/windows-hardware/drivers/ddi/wdfobject/ne-wdfobject-_wdf_synchronization_scope) for individual queue objects.

* The following methods:
  * [**WdfDeviceGetSystemPowerAction**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegetsystempoweraction)
  * [**WdfDeviceRemoveDependentUsageDeviceObject**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceremovedependentusagedeviceobject)
  * [**WdfInterruptSetExtendedPolicy**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptsetextendedpolicy)
  * [**WdfPdoInitAllowForwardingRequestToParent**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitallowforwardingrequesttoparent)
  * [**WdfPdoInitAssignContainerID**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitassigncontainerid)
  * [**WdfPreDeviceInstallEx**](/windows-hardware/drivers/ddi/wdfinstaller/nf-wdfinstaller-wdfpredeviceinstallex)
  * [**WdfRequestForwardToParentDeviceIoQueue**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestforwardtoparentdeviceioqueue)
  * [**WdfRequestMarkCancelableEx**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelableex)
* Added the **NumberOfPresentedRequests** member to the [**WDF\_IO\_QUEUE\_CONFIG**](/windows-hardware/drivers/ddi/wdfio/ns-wdfio-_wdf_io_queue_config) structure so drivers can limit the number of I/O requests that the framework delivers to the driver from a parallel I/O queue.

* Added the **WdfFileObjectCanBeOptional** flag to the [**WDF\_FILEOBJECT\_CLASS**](/windows-hardware/drivers/ddi/wdfdevice/ne-wdfdevice-_wdf_fileobject_class) structure.

* Added the **TolerableDelay** member to the [**WDF\_TIMER\_CONFIG**](/windows-hardware/drivers/ddi/wdftimer/ns-wdftimer-_wdf_timer_config) structure.

* Added [WdfDefaultIdleInWorkingState and WdfDefaultWakeFromSleepState](user-control-of-device-idle-and-wake-behavior.md) registry values.

## KMDF 1.7 (Windows Vista with Service Pack 1; Windows Server 2008)

* The [**WdfDeviceEnqueueRequest**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceenqueuerequest) method can be called at IRQL&lt;=DISPATCH\_LEVEL.

* The [**WdfWorkItemEnqueue**](/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemenqueue) method can be called if the specified work item is already on the work-item queue.

* Added the [*EvtDeviceArmWakeFromSxWithReason*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_sx_with_reason) event callback function.

* Added **ArmForWakeIfChildrenAreArmedForWake** and **IndicateChildWakeOnParentWake** members to the [**WDF\_DEVICE\_POWER\_POLICY\_WAKE\_SETTINGS**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_wake_settings) structure.

## KMDF 1.5 (Windows Vista)

* [**WdfUsbInterfaceGetNumSettings**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfacegetnumsettings)

* Added the **DriverPoolTag** member to [**WDF\_DRIVER\_CONFIG**](/windows-hardware/drivers/ddi/wdfdriver/ns-wdfdriver-_wdf_driver_config).

## KMDF 1.1 (not released in a Windows version)

* The following methods:
  * [**WdfCommonBufferCreateWithConfig**](/windows-hardware/drivers/ddi/wdfcommonbuffer/nf-wdfcommonbuffer-wdfcommonbuffercreatewithconfig)
  * [**WdfDmaEnablerGetFragmentLength**](/windows-hardware/drivers/ddi/wdfdmaenabler/nf-wdfdmaenabler-wdfdmaenablergetfragmentlength)
  * [**WdfDmaEnablerWdmGetDmaAdapter**](/windows-hardware/drivers/ddi/wdfdmaenabler/nf-wdfdmaenabler-wdfdmaenablerwdmgetdmaadapter)

## KMDF 1.0 (not released in a Windows version)

Initial release.
