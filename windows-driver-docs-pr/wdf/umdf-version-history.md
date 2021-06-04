---
title: UMDF Version History
description: This topic lists versions of User-Mode Driver Framework (UMDF), the corresponding versions of the Windows operating system, and the changes made in each release.
keywords:
- UMDF WDK , revision history
- UMDF WDK , version information
- revision history WDK UMDF
- version information WDK UMDF
ms.date: 04/22/2021
ms.localizationpriority: medium
---

# UMDF Version History


This topic lists versions of User-Mode Driver Framework (UMDF), the corresponding versions of the Windows operating system, and the changes made in each release.

The following table shows the release history of the UMDF library:

|UMDF version|Release method|Included in this version of Windows|Drivers using it can run on|
|--- |--- |--- |--- |
|2.33|WDK for Windows Server 2022|Windows Server 2022 (Iron)|Windows Server 2022 and later|
|2.31|Windows 10, version 2004 WDK|Windows 10, version 2004 (May 2020 Update, Vibranium)|Windows 10, version 2004 and later|
|2.29|Not released in WDK|Windows 10, version 1903 (March 2019 Update, 19H1)|Windows 10, version 1903 and later|
|2.27|Windows 10, version 1809 WDK|Windows 10, version 1809 (October 2018 Update, Redstone 5)|Windows 10, version 1809 and later|
|2.25|Windows 10, version 1803 WDK|Windows 10, version 1803 (April 2018 Update, Redstone 4)|Windows 10, version 1803 and later|
|2.23|Windows 10, version 1709 WDK|Windows 10, version 1709 (Fall Creators Update, Redstone 3)|Windows 10, version 1709 and later|
|2.21|Windows 10, version 1703 WDK|Windows 10, version 1703 (Creators Update, Redstone 2)|Windows 10, version 1703 and later|
|2.19|Windows 10, version 1607 WDK|Windows 10, version 1607 (Anniversary Update, Redstone 1)|Windows 10, version 1607, Windows Server 2016 and later|
|2.17|Windows 10, version 1511 WDK|Windows 10, version 1511 (November Update, Threshold 2)|Windows 10, version 1511, Windows Server 2016 and later|
|2.15|Windows 10 WDK|Windows 10, version 1507 (Threshold 1)|Windows 10, version 1507, Windows Server 2016 and later|
|2.0|Windows Driver Kit (WDK) 8.1|Windows 8.1|Windows 8.1 and later|
|1.11|Windows Driver Kit (WDK) 8|Windows 8|Windows Vista and later|
|1.9|Windows 7 WDK|Windows 7|Windows XP and later|
|1.7|Windows Server 2008 WDK|Windows Vista with Service Pack 1 (SP1), Windows Server 2008|Windows XP and later|
|1.5|Windows Vista WDK|Windows Vista|Windows XP and later|


You can use the Windows Driver Kit (WDK) with Microsoft Visual Studio 2019 to build drivers that run on Windows 10 and later.

For help determining what version of WDF to use, see [Which framework version should I use?](building-and-loading-a-kmdf-driver.md#which-framework-version-should-i-use).

For information about the new features for UMDF drivers in Windows 10, see [What's New for WDF Drivers](index.md).

## UMDF Version 2.33

* For devices that specify **SystemManagedIdleTimeout** or **SystemManagedIdleTimeoutWithHint** in the [WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE](/windows-hardware/drivers/ddi/wdfdevice/ne-wdfdevice-_wdf_power_policy_idle_timeout_type) enumeration, when calling the [**WdfDeviceStopIdle**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle) macro with *WaitForD0* set to **FALSE**, if the device is still in D0 and the idle timeout period has not yet elapsed, **WdfDeviceStopIdle** returns STATUS_SUCCESS (in previous versions this resulted in a return value of STATUS_PENDING).
* [**WdfDeviceWdmAssignPowerFrameworkSettings**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmassignpowerframeworksettings) function now supports UMDF.
* [**WDF_POWER_FRAMEWORK_SETTINGS**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_power_framework_settings) structure has two new members (**PoFxDeviceFlags** and **DirectedPoFxEnabled**) and can now be used with UMDF. For UMDF, only the **Size**, **PoFxDeviceFlags**, and **DirectedPoFxEnabled** members are used. Other fields are ignored and must be set to zero. The framework does this automatically when a UMDF driver calls the [**WDF_POWER_FRAMEWORK_SETTINGS_INIT**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdf_power_framework_settings_init) function.

## UMDF Version 2.31

* Added new API [**WdfDeviceSetDeviceInterfaceStateEx**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetdeviceinterfacestateex)
* Improved existing API [**WdfDeviceGetSystemPowerAction**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegetsystempoweraction)
* Added per-driver **HostProcessDbgBreakOnDriverLoad** registry value. For info, see [Registry Values for Debugging WDF Drivers](./registry-values-for-debugging-kmdf-drivers.md).
* [Introduction to the Directed Power Management Framework](../kernel/introduction-to-the-directed-power-management-framework.md)

## UMDF Version 2.29

Unchanged from version 2.27.

## UMDF Version 2.27

* Added new API [**WdfDriverRetrieveDriverDataDirectoryString**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriverretrievedriverdatadirectorystring)

## UMDF Version 2.25

* [Building a WDF driver for multiple versions of Windows](building-a-wdf-driver-for-multiple-versions-of-windows.md)
* [**WdfDeviceRetrieveDeviceDirectoryString**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceretrievedevicedirectorystring)

## UMDF Version 2.23

* Companion functionality added for internal use only.  For the new DDIs, see [Summary of WDF Callbacks and Methods](/windows-hardware/drivers/ddi/_wdf/).

## UMDF Version 2.21

* [**WdfObjectDereferenceActual**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdereferenceactual): Type of *File* parameter changed from PCHAR to PCCH.
* [**WdfObjectReferenceActual**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectreferenceactual): Type of *File* parameter changed from PCHAR to PCCH.

## UMDF Version 2.19

There are no changes or additions for UMDF Version 2.19.

## UMDF Version 2.17

This version adds UMDF support for the following existing interfaces:

-   [**WdfDeviceConfigureWdmIrpDispatchCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceconfigurewdmirpdispatchcallback)
-   [*EvtDeviceWdmIrpDispatch*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_dispatch)
-   [**WdfDeviceWdmDispatchIrp**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchirp)
-   [**WdfDeviceWdmDispatchIrpToIoQueue**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchirptoioqueue)

For more information, see [Dispatching IRPs to I/O Queues](dispatching-irps-to-i-o-queues.md).

## UMDF Version 2.15

Here is the list of updated DDIs for version 2.15:

-   The new [**WdfDeviceOpenDevicemapKey**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceopendevicemapkey) method allows a driver to access subkeys and values under **HKEY\_LOCAL\_MACHINE\\HARDWARE\\DEVICEMAP**.

-   A UMDF driver can call [**WdfIoTargetWdmGetTargetFileHandle**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetwdmgettargetfilehandle) to obtain a file handle to the next-lower kernel-mode driver in its stack. The driver can write data to that handle, bypassing the framework's abstractions for sending I/O to the local I/O target.

-   A UMDF driver can request that the underlying bus driver re-enumerate it. See [**WdfDeviceSetFailed**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetfailed).

-   Setting the **UmdfDirectHardwareAccess** directive is no longer always necessary for devices that have connection resources. See [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).

## UMDF Version 2.0


In addition to the shared functionality described in [Getting Started with UMDF](getting-started-with-umdf-version-2.md), UMDF version 2.0 adds:

-   Support for timers that do not wake the system if they expire when the system is in a low-power state. For more information, see [Using Timers](using-timers.md).
-   Added **CanWakeDevice** member to [**WDF\_INTERRUPT\_CONFIG**](/windows-hardware/drivers/ddi/wdfinterrupt/ns-wdfinterrupt-_wdf_interrupt_config) structure to support interrupts that can be used to bring a device from a low-power Dx state back to its fully on D0 state. For more information, see [Using an Interrupt to Wake a Device](using-an-interrupt-to-wake-a-device.md).
-   Single-component, single-state (F0) power management for UMDF drivers. For more information, see [**WdfDeviceAssignS0IdleSettings**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings).

-   Several debugger extension commands in Wdfkd.dll can now be used for UMDF 2.0 drivers as well. The extension library also contains the following new extension commands designed specifically for debugging UMDF 2.0 drivers:

    -   [**!wdfkd.wdfumdevstack**](../debugger/-wdfkd-wdfumdevstack.md)
    -   [**!wdfkd.wdfumdevstacks**](../debugger/-wdfkd-wdfumdevstacks.md)
    -   [**!wdfkd.wdfumdownirp**](../debugger/-wdfkd-wdfumdownirp.md)
    -   [**!wdfkd.wdfumfile**](../debugger/-wdfkd-wdfumfile.md)
    -   [**!wdfkd.wdfumirp**](../debugger/-wdfkd-wdfumirp.md)
    -   [**!wdfkd.wdfumirps**](../debugger/-wdfkd-wdfumirps.md)
    -   [**!wdfkd.wdfdeviceinterrupts**](../debugger/-wdfkd-wdfdeviceinterrupts.md)

    For a list of extension commands and framework applicability, see [Debugger Extensions](debugger-extensions-for-kmdf-drivers.md).

-   The [framework's event logger](using-the-framework-s-event-logger.md), or *In-flight Recorder* (IFR) has been updated to work for UMDF 2.0 drivers.
-   Other WDF debugger extensions have been updated to work with UMDF 2.0 drivers. For a full list of extension commands, including information about which ones apply to which framework, see [Debugger Extensions for WDF Drivers](debugger-extensions-for-kmdf-drivers.md).
-   Added **WdfIoTargetOpenLocalTargetByFile** to [**WDF\_IO\_TARGET\_OPEN\_TYPE**](/windows-hardware/drivers/ddi/wdfiotarget/ne-wdfiotarget-_wdf_io_target_open_type) to allow UMDF drivers to send driver-created requests to lower targets that require an associated file object. For more information, see the Remarks of **WDF\_IO\_TARGET\_OPEN\_TYPE**.
-   The following UMDF-only routines:

    -   [*EvtRequestImpersonate*](/windows-hardware/drivers/ddi/wdfrequest/nc-wdfrequest-evt_wdf_request_impersonate)
    -   [**WDF\_IO\_TARGET\_OPEN\_PARAMS\_INIT\_OPEN\_BY\_FILE**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdf_io_target_open_params_init_open_by_file)
    -   [**WdfDeviceAllocAndQueryInterfaceProperty**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandqueryinterfaceproperty)
    -   [**WdfDeviceAssignInterfaceProperty**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigninterfaceproperty)
    -   [**WdfDeviceGetDeviceStackIoType**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegetdevicestackiotype)
    -   [**WdfDeviceGetHardwareRegisterMappedAddress**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegethardwareregistermappedaddress)
    -   [**WdfDeviceMapIoSpace**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicemapiospace)
    -   [**WdfDevicePostEvent**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicepostevent)
    -   [**WdfDeviceQueryInterfaceProperty**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicequeryinterfaceproperty)
    -   [**WdfDeviceUnmapIoSpace**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceunmapiospace)
    -   [**WdfFileObjectGetInitiatorProcessId**](/windows-hardware/drivers/ddi/wdffileobject/nf-wdffileobject-wdffileobjectgetinitiatorprocessid) (added to KMDF 1.21)
    -   [**WdfFileObjectGetRelatedFileObject**](/windows-hardware/drivers/ddi/wdffileobject/nf-wdffileobject-wdffileobjectgetrelatedfileobject)
    -   [**WdfRequestGetEffectiveIoType**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgeteffectiveiotype)
    -   [**WdfRequestGetRequestorProcessId**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetrequestorprocessid) (added to KMDF 1.21)
    -   [**WdfRequestGetUserModeInitiatedIo**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetusermodedriverinitiatedio)
    -   [**WdfRequestImpersonate**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestimpersonate)
    -   [**WdfRequestIsFromUserModeDriver**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestisfromusermodedriver)
    -   [**WdfRequestRetrieveActivityId**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveactivityid)
    -   [**WdfRequestSetActivityId**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsetactivityid)
    -   [**WdfRequestSetUserModeDriverInitiatedIo**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsetusermodedriverinitiatedio)
-   The following KMDF/UMDF methods described in [Accessing the Unified Device Property Model](accessing-the-unified-device-property-model.md):

    -   [**WdfDeviceAllocAndQueryPropertyEx**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandquerypropertyex)
    -   [**WdfDeviceAssignProperty**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassignproperty)
    -   [**WdfDeviceInitSetIoTypeEx**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetiotypeex)
    -   [**WdfDeviceQueryPropertyEx**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicequerypropertyex)
    -   [**WdfFdoInitAllocAndQueryPropertyEx**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitallocandquerypropertyex)
    -   [**WdfFdoInitQueryPropertyEx**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitquerypropertyex)

    For more information, see [Accessing the Unified Device Property Model](accessing-the-unified-device-property-model.md).

-   Support for the following USB configuration types in [**WdfUsbTargetDeviceSelectConfigType**](/windows-hardware/drivers/ddi/wdfusb/ne-wdfusb-_wdfusbtargetdeviceselectconfigtype):
    -   **WdfUsbTargetDeviceSelectConfigTypeSingleInterface**
    -   **WdfUsbTargetDeviceSelectConfigTypeMultiInterface**
    -   **WdfUsbTargetDeviceSelectConfigTypeInterfacesPairs**
-   Support for querying the following capability types in [**WdfUsbTargetDeviceQueryUsbCapability**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicequeryusbcapability):
    -   **GUID\_USB\_CAPABILITY\_DEVICE\_CONNECTION\_HIGH\_SPEED\_COMPATIBLE**
    -   **GUID\_USB\_CAPABILITY\_DEVICE\_CONNECTION\_SUPER\_SPEED\_COMPATIBLE**
-   Added [WDF Register/Port Access Functions](/windows-hardware/drivers/ddi/wdfhwaccess/)

## UMDF Version 1.11


Version 1.11 adds the following driver-supplied callback interfaces and event callback functions:

-   [**IPnpCallbackHardware2**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallbackhardware2)

-   [**IPnpCallbackHardwareInterrupt**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallbackhardwareinterrupt)

Version 1.11 adds the following framework-supplied interfaces:

-   [**IWDFCmResourceList**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfcmresourcelist)

-   [**IWDFDevice3**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdevice3)

-   [**IWDFFile3**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdffile3)

-   [**IWDFInterrupt**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfinterrupt)

-   [**IWDFIoRequest3**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfiorequest3)

-   [**IWDFUnifiedPropertyStore**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfunifiedpropertystore)

-   [**IWDFUnifiedPropertyStoreFactory**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfunifiedpropertystorefactory)

-   [**IWDFWorkItem**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfworkitem)

Version 1.11 adds the following capabilities to UMDF-based drivers:

-   [Accessing Hardware and Handling Interrupts](accessing-hardware-and-handling-interrupts.md)

-   [Using Device Pooling in UMDF Drivers](using-device-pooling-in-umdf-drivers.md)

-   Added **UmdfHostProcessSharing**, **UmdfDirectHardwareAccess**, **UmdfRegisterAccessMode**, **UmdfFileObjectPolicy**, and **UmdfFsContextUsePolicy** directives, described in [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md)

-   [Well-known security identifiers (SID) for UMDF drivers](controlling-device-access.md)

-   Unified property store support, described in [Using the Registry in UMDF-based Drivers](./using-the-registry-in-umdf-1-x-drivers.md)

-   [**IoGetDeviceObjectPointer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceobjectpointer) is integrated to work with UMDF. In prior versions, this routine closes the handle to the device object after taking a reference on the device’s handle. This behavior was incompatible with UMDF’s expectation that the cleanup request on the device object won’t occur until after all the I/O is complete.

-   [Creating UMDF-based HID Minidrivers](creating-umdf-hid-minidrivers.md)

-   Enhanced support for [Supporting Idle Power-Down in UMDF-based Drivers](supporting-idle-power-down-in-umdf-drivers.md). The framework can now put the device in the D3cold power state when the idle timeout period expires. The framework can also cause the device to return to its working (D0) state when the system returns to its working (S0) state.

-   The following samples are new in UMDF 1.11: [WudfVhidmini](/samples/browse/), [NetNfpProvider](/samples/browse/).

## UMDF Version 1.9


Version 1.9 adds the following driver-supplied callback interfaces:

-   [IPnpCallbackRemoteInterfaceNotification](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallbackremoteinterfacenotification)

-   [IPowerPolicyCallbackWakeFromS0](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipowerpolicycallbackwakefroms0)

-   [IPowerPolicyCallbackWakeFromSx](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipowerpolicycallbackwakefromsx)

-   [IQueueCallbackIoCanceledOnQueue](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iqueuecallbackiocanceledonqueue)

-   [IRemoteInterfaceCallbackEvent](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iremoteinterfacecallbackevent)

-   [IRemoteInterfaceCallbackRemoval](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iremoteinterfacecallbackremoval)

-   [IRemoteTargetCallbackRemoval](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iremotetargetcallbackremoval)

-   [IWDFRemoteInterfaceInitialize](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfremoteinterfaceinitialize)

Version 1.9 adds the following framework-supplied interfaces:

-   [IWDFDevice2](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdevice2)

-   [IWDFDeviceInitialize2](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdeviceinitialize2)

-   [IWDFFile2](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdffile2)

-   [IWDFIoRequest2](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfiorequest2)

-   [IWDFIoTarget2](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfiotarget2)

-   [IWDFNamedPropertyStore2](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfnamedpropertystore2)

-   [IWDFPropertyStoreFactory](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfpropertystorefactory)

-   [IWDFRemoteTarget](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfremotetarget)

-   [IWDFUsbTargetPipe2](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbtargetpipe2)

These interfaces add the following capabilities to UMDF-based drivers:

-   [Remote I/O targets](general-i-o-targets-in-umdf.md)

-   [Power policy ownership](power-policy-ownership-in-umdf.md)

-   The [direct I/O](./accessing-data-buffers-in-umdf-1-x-drivers.md) buffer access method

-   [Continuous readers](./working-with-usb-pipes-in-umdf-1-x-drivers.md) for USB devices

-   Enhanced support for [device interfaces](using-device-interfaces-in-umdf-drivers.md)

-   Enhanced ability to [cancel I/O requests](canceling-i-o-requests.md)

-   Enhanced access to the [registry](./using-the-registry-in-umdf-1-x-drivers.md)

