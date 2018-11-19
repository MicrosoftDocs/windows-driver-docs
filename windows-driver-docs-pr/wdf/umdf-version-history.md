---
title: UMDF Version History
description: This topic lists versions of User-Mode Driver Framework (UMDF), the corresponding versions of the Windows operating system, and the changes made in each release.
ms.assetid: f3e895c6-6801-4033-adaa-d7d04a46db0a
keywords:
- UMDF WDK , revision history
- UMDF WDK , version information
- revision history WDK UMDF
- version information WDK UMDF
ms.date: 10/02/2018
ms.localizationpriority: medium
---

# UMDF Version History


This topic lists versions of User-Mode Driver Framework (UMDF), the corresponding versions of the Windows operating system, and the changes made in each release.

The following table shows the release history of the UMDF library:

|UMDF version|Release method|Included in this version of Windows|Drivers using it can run on|
|--- |--- |--- |--- |
|2.27|Windows 10, version 1809 WDK|Windows 10, version 1809 (October 2018 Update, Redstone 5)|Windows 10, version 1809|
|2.25|Windows 10, version 1803 WDK|Windows 10, version 1803 (April 2018 Update, Redstone 4)|Windows 10, version 1803|
|2.23|Windows 10, version 1709 WDK|Windows 10, version 1709 (Fall Creators Update, Redstone 3)|Windows 10, version 1709|
|2.21|Windows 10, version 1703 WDK|Windows 10, version 1703 (Creators Update, Redstone 2)|Windows 10, version 1703|
|2.19|Windows 10, version 1607 WDK|Windows 10, version 1607 (Anniversary Update, Redstone 1)|Windows 10, version 1607, Windows Server 2016 and later|
|2.17|Windows 10, version 1511 WDK|Windows 10, version 1511 (November Update, Threshold 2)|Windows 10, version 1511, Windows Server 2016 and later|
|2.15|Windows 10 WDK|Windows 10, version 1507 (Threshold 1)|Windows 10, version 1507, Windows Server 2016 and later|
|2.0|Windows Driver Kit (WDK) 8.1|Windows 8.1|Windows 8.1 and later|
|1.11|Windows Driver Kit (WDK) 8|Windows 8|Windows Vista and later|
|1.9|Windows 7 WDK|Windows 7|Windows XP and later|
|1.7|Windows Server 2008 WDK|Windows Vista with Service Pack 1 (SP1), Windows Server 2008|Windows XP and later|
|1.5|Windows Vista WDK|Windows Vista|Windows XP and later|


You can use the Windows Driver Kit (WDK) with Microsoft Visual Studio 2017 to build drivers that run on Windows 7 and later.

For information about the new features for UMDF drivers in Windows 10, see [What's New for WDF Drivers](index.md).

## UMDF Version 2.27

* Added new API [**WdfDriverRetrieveDriverDataDirectoryString**](/windows-hardware/drivers/ddi/content/wdfdriver/nf-wdfdriver-wdfdriverretrievedriverdatadirectorystring)

## UMDF Version 2.25

* [Building a WDF driver for multiple versions of Windows](building-a-wdf-driver-for-multiple-versions-of-windows.md)
* [**WdfDeviceRetrieveDeviceDirectoryString**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceretrievedevicedirectorystring)

## UMDF Version 2.23

* Companion functionality added for internal use only.  For the new DDIs, see [Summary of WDF Callbacks and Methods](https://msdn.microsoft.com/library/windows/hardware/dn265591).

## UMDF Version 2.21

* [**WdfObjectDereferenceActual**](https://msdn.microsoft.com/library/windows/hardware/ff548743): Type of *File* parameter changed from PCHAR to PCCH.
* [**WdfObjectReferenceActual**](https://msdn.microsoft.com/library/windows/hardware/ff548760): Type of *File* parameter changed from PCHAR to PCCH.

## UMDF Version 2.19

There are no changes or additions for UMDF Version 2.19.

## UMDF Version 2.17

This version adds UMDF support for the following existing interfaces:

-   [**WdfDeviceConfigureWdmIrpDispatchCallback**](https://msdn.microsoft.com/library/windows/hardware/hh451093)
-   [*EvtDeviceWdmIrpDispatch*](https://msdn.microsoft.com/library/windows/hardware/hh406404)
-   [**WdfDeviceWdmDispatchIrp**](https://msdn.microsoft.com/library/windows/hardware/hh451100)
-   [**WdfDeviceWdmDispatchIrpToIoQueue**](https://msdn.microsoft.com/library/windows/hardware/hh451105)

For more information, see [Dispatching IRPs to I/O Queues](dispatching-irps-to-i-o-queues.md).

## UMDF Version 2.15

Here is the list of updated DDIs for version 2.15:

-   The new [**WdfDeviceOpenDevicemapKey**](https://msdn.microsoft.com/library/windows/hardware/dn932458) method allows a driver to access subkeys and values under **HKEY\_LOCAL\_MACHINE\\HARDWARE\\DEVICEMAP**.

-   A UMDF driver can call [**WdfIoTargetWdmGetTargetFileHandle**](https://msdn.microsoft.com/library/windows/hardware/ff548683) to obtain a file handle to the next-lower kernel-mode driver in its stack. The driver can write data to that handle, bypassing the framework's abstractions for sending I/O to the local I/O target.

-   A UMDF driver can request that the underlying bus driver re-enumerate it. See [**WdfDeviceSetFailed**](https://msdn.microsoft.com/library/windows/hardware/ff546890).

-   Setting the **UmdfDirectHardwareAccess** directive is no longer always necessary for devices that have connection resources. See [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).

## UMDF Version 2.0


In addition to the shared functionality described in [Getting Started with UMDF](getting-started-with-umdf-version-2.md), UMDF version 2.0 adds:

-   Support for timers that do not wake the system if they expire when the system is in a low-power state. For more information, see [Using Timers](using-timers.md).
-   Added **CanWakeDevice** member to [**WDF\_INTERRUPT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552347) structure to support interrupts that can be used to bring a device from a low-power Dx state back to its fully on D0 state. For more information, see [Using an Interrupt to Wake a Device](using-an-interrupt-to-wake-a-device.md).
-   Single-component, single-state (F0) power management for UMDF drivers. For more information, see [**WdfDeviceAssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545903).

-   Several debugger extension commands in Wdfkd.dll can now be used for UMDF 2.0 drivers as well. The extension library also contains the following new extension commands designed specifically for debugging UMDF 2.0 drivers:

    -   [**!wdfkd.wdfumdevstack**](https://msdn.microsoft.com/library/windows/hardware/dn265379)
    -   [**!wdfkd.wdfumdevstacks**](https://msdn.microsoft.com/library/windows/hardware/dn265380)
    -   [**!wdfkd.wdfumdownirp**](https://msdn.microsoft.com/library/windows/hardware/dn265381)
    -   [**!wdfkd.wdfumfile**](https://msdn.microsoft.com/library/windows/hardware/dn265382)
    -   [**!wdfkd.wdfumirp**](https://msdn.microsoft.com/library/windows/hardware/dn265383)
    -   [**!wdfkd.wdfumirps**](https://msdn.microsoft.com/library/windows/hardware/dn265384)
    -   [**!wdfkd.wdfdeviceinterrupts**](https://msdn.microsoft.com/library/windows/hardware/dn265378)

    For a list of extension commands and framework applicability, see [Debugger Extensions](debugger-extensions-for-kmdf-drivers.md).

-   The [framework's event logger](using-the-framework-s-event-logger.md), or *In-flight Recorder* (IFR) has been updated to work for UMDF 2.0 drivers.
-   Other WDF debugger extensions have been updated to work with UMDF 2.0 drivers. For a full list of extension commands, including information about which ones apply to which framework, see [Debugger Extensions for WDF Drivers](debugger-extensions-for-kmdf-drivers.md).
-   Added **WdfIoTargetOpenLocalTargetByFile** to [**WDF\_IO\_TARGET\_OPEN\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff552386) to allow UMDF drivers to send driver-created requests to lower targets that require an associated file object. For more information, see the Remarks of **WDF\_IO\_TARGET\_OPEN\_TYPE**.
-   The following UMDF-only routines:

    -   [*EvtRequestImpersonate*](https://msdn.microsoft.com/library/windows/hardware/dn265581)
    -   [**WDF\_IO\_TARGET\_OPEN\_PARAMS\_INIT\_OPEN\_BY\_FILE**](https://msdn.microsoft.com/library/windows/hardware/dn265641)
    -   [**WdfDeviceAllocAndQueryInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/dn265598)
    -   [**WdfDeviceAssignInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/dn265600)
    -   [**WdfDeviceGetDeviceStackIoType**](https://msdn.microsoft.com/library/windows/hardware/dn265602)
    -   [**WdfDeviceGetHardwareRegisterMappedAddress**](https://msdn.microsoft.com/library/windows/hardware/dn265603)
    -   [**WdfDeviceMapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/dn265605)
    -   [**WdfDevicePostEvent**](https://msdn.microsoft.com/library/windows/hardware/dn265606)
    -   [**WdfDeviceQueryInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/dn265607)
    -   [**WdfDeviceUnmapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/dn265610)
    -   [**WdfFileObjectGetInitiatorProcessId**](https://msdn.microsoft.com/library/windows/hardware/dn265614) (added to KMDF 1.21)
    -   [**WdfFileObjectGetRelatedFileObject**](https://msdn.microsoft.com/library/windows/hardware/dn265615)
    -   [**WdfRequestGetEffectiveIoType**](https://msdn.microsoft.com/library/windows/hardware/dn265616)
    -   [**WdfRequestGetRequestorProcessId**](https://msdn.microsoft.com/library/windows/hardware/dn265617) (added to KMDF 1.21)
    -   [**WdfRequestGetUserModeInitiatedIo**](https://msdn.microsoft.com/library/windows/hardware/dn265618)
    -   [**WdfRequestImpersonate**](https://msdn.microsoft.com/library/windows/hardware/dn265619)
    -   [**WdfRequestIsFromUserModeDriver**](https://msdn.microsoft.com/library/windows/hardware/dn265620)
    -   [**WdfRequestRetrieveActivityId**](https://msdn.microsoft.com/library/windows/hardware/dn265621)
    -   [**WdfRequestSetActivityId**](https://msdn.microsoft.com/library/windows/hardware/dn265622)
    -   [**WdfRequestSetUserModeDriverInitiatedIo**](https://msdn.microsoft.com/library/windows/hardware/dn265623)
-   The following KMDF/UMDF methods described in [Accessing the Unified Device Property Model](accessing-the-unified-device-property-model.md):

    -   [**WdfDeviceAllocAndQueryPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/dn265599)
    -   [**WdfDeviceAssignProperty**](https://msdn.microsoft.com/library/windows/hardware/dn265601)
    -   [**WdfDeviceInitSetIoTypeEx**](https://msdn.microsoft.com/library/windows/hardware/dn265604)
    -   [**WdfDeviceQueryPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/dn265608)
    -   [**WdfFdoInitAllocAndQueryPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/dn265612)
    -   [**WdfFdoInitQueryPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/dn265613)

    For more information, see [Accessing the Unified Device Property Model](accessing-the-unified-device-property-model.md).

-   Support for the following USB configuration types in [**WdfUsbTargetDeviceSelectConfigType**](https://msdn.microsoft.com/library/windows/hardware/ff550102):
    -   **WdfUsbTargetDeviceSelectConfigTypeSingleInterface**
    -   **WdfUsbTargetDeviceSelectConfigTypeMultiInterface**
    -   **WdfUsbTargetDeviceSelectConfigTypeInterfacesPairs**
-   Support for querying the following capability types in [**WdfUsbTargetDeviceQueryUsbCapability**](https://msdn.microsoft.com/library/windows/hardware/hh439434):
    -   **GUID\_USB\_CAPABILITY\_DEVICE\_CONNECTION\_HIGH\_SPEED\_COMPATIBLE**
    -   **GUID\_USB\_CAPABILITY\_DEVICE\_CONNECTION\_SUPER\_SPEED\_COMPATIBLE**
-   Added [WDF Register/Port Access Functions](https://msdn.microsoft.com/library/windows/hardware/dn265662)

## UMDF Version 1.11


Version 1.11 adds the following driver-supplied callback interfaces and event callback functions:

-   [**IPnpCallbackHardware2**](https://msdn.microsoft.com/library/windows/hardware/hh439727)

-   [**IPnpCallbackHardwareInterrupt**](https://msdn.microsoft.com/library/windows/hardware/hh439744)

Version 1.11 adds the following framework-supplied interfaces:

-   [**IWDFCmResourceList**](https://msdn.microsoft.com/library/windows/hardware/hh439762)

-   [**IWDFDevice3**](https://msdn.microsoft.com/library/windows/hardware/hh451197)

-   [**IWDFFile3**](https://msdn.microsoft.com/library/windows/hardware/hh451275)

-   [**IWDFInterrupt**](https://msdn.microsoft.com/library/windows/hardware/hh451283)

-   [**IWDFIoRequest3**](https://msdn.microsoft.com/library/windows/hardware/hh451337)

-   [**IWDFUnifiedPropertyStore**](https://msdn.microsoft.com/library/windows/hardware/hh451399)

-   [**IWDFUnifiedPropertyStoreFactory**](https://msdn.microsoft.com/library/windows/hardware/hh451403)

-   [**IWDFWorkItem**](https://msdn.microsoft.com/library/windows/hardware/hh406734)

Version 1.11 adds the following capabilities to UMDF-based drivers:

-   [Accessing Hardware and Handling Interrupts](accessing-hardware-and-handling-interrupts.md)

-   [Using Device Pooling in UMDF Drivers](using-device-pooling-in-umdf-drivers.md)

-   Added **UmdfHostProcessSharing**, **UmdfDirectHardwareAccess**, **UmdfRegisterAccessMode**, **UmdfFileObjectPolicy**, and **UmdfFsContextUsePolicy** directives, described in [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md)

-   [Well-known security identifiers (SID) for UMDF drivers](controlling-device-access.md)

-   Unified property store support, described in [Using the Registry in UMDF-based Drivers](https://msdn.microsoft.com/library/windows/hardware/ff561381)

-   [**IoGetDeviceObjectPointer**](https://msdn.microsoft.com/library/windows/hardware/ff549198) is integrated to work with UMDF. In prior versions, this routine closes the handle to the device object after taking a reference on the device’s handle. This behavior was incompatible with UMDF’s expectation that the cleanup request on the device object won’t occur until after all the I/O is complete.

-   [Creating UMDF-based HID Minidrivers](creating-umdf-hid-minidrivers.md)

-   Enhanced support for [Supporting Idle Power-Down in UMDF-based Drivers](supporting-idle-power-down-in-umdf-drivers.md). The framework can now put the device in the D3cold power state when the idle timeout period expires. The framework can also cause the device to return to its working (D0) state when the system returns to its working (S0) state.

-   The following samples are new in UMDF 1.11: [WudfVhidmini](http://go.microsoft.com/fwlink/p/?linkid=256226), [NetNfpProvider](http://go.microsoft.com/fwlink/p/?linkid=256147).

## UMDF Version 1.9


Version 1.9 adds the following driver-supplied callback interfaces:

-   [IPnpCallbackRemoteInterfaceNotification](https://msdn.microsoft.com/library/windows/hardware/ff556772)

-   [IPowerPolicyCallbackWakeFromS0](https://msdn.microsoft.com/library/windows/hardware/ff556815)

-   [IPowerPolicyCallbackWakeFromSx](https://msdn.microsoft.com/library/windows/hardware/ff556825)

-   [IQueueCallbackIoCanceledOnQueue](https://msdn.microsoft.com/library/windows/hardware/ff556857)

-   [IRemoteInterfaceCallbackEvent](https://msdn.microsoft.com/library/windows/hardware/ff556887)

-   [IRemoteInterfaceCallbackRemoval](https://msdn.microsoft.com/library/windows/hardware/ff556891)

-   [IRemoteTargetCallbackRemoval](https://msdn.microsoft.com/library/windows/hardware/ff556894)

-   [IWDFRemoteInterfaceInitialize](https://msdn.microsoft.com/library/windows/hardware/ff560232)

Version 1.9 adds the following framework-supplied interfaces:

-   [IWDFDevice2](https://msdn.microsoft.com/library/windows/hardware/ff556918)

-   [IWDFDeviceInitialize2](https://msdn.microsoft.com/library/windows/hardware/ff556967)

-   [IWDFFile2](https://msdn.microsoft.com/library/windows/hardware/ff558915)

-   [IWDFIoRequest2](https://msdn.microsoft.com/library/windows/hardware/ff558988)

-   [IWDFIoTarget2](https://msdn.microsoft.com/library/windows/hardware/ff559175)

-   [IWDFNamedPropertyStore2](https://msdn.microsoft.com/library/windows/hardware/ff560168)

-   [IWDFPropertyStoreFactory](https://msdn.microsoft.com/library/windows/hardware/ff560223)

-   [IWDFRemoteTarget](https://msdn.microsoft.com/library/windows/hardware/ff560247)

-   [IWDFUsbTargetPipe2](https://msdn.microsoft.com/library/windows/hardware/ff560394)

These interfaces add the following capabilities to UMDF-based drivers:

-   [Remote I/O targets](general-i-o-targets-in-umdf.md)

-   [Power policy ownership](power-policy-ownership-in-umdf.md)

-   The [direct I/O](https://msdn.microsoft.com/library/windows/hardware/ff554413) buffer access method

-   [Continuous readers](https://msdn.microsoft.com/library/windows/hardware/ff561479) for USB devices

-   Enhanced support for [device interfaces](using-device-interfaces-in-umdf-drivers.md)

-   Enhanced ability to [cancel I/O requests](canceling-i-o-requests.md)

-   Enhanced access to the [registry](https://msdn.microsoft.com/library/windows/hardware/ff561381)

 

 





