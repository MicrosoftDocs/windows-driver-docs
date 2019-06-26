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
ms.custom: 19H1
---

# UMDF Version History


This topic lists versions of User-Mode Driver Framework (UMDF), the corresponding versions of the Windows operating system, and the changes made in each release.

The following table shows the release history of the UMDF library:

|UMDF version|Release method|Included in this version of Windows|Drivers using it can run on|
|--- |--- |--- |--- |
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


You can use the Windows Driver Kit (WDK) with Microsoft Visual Studio 2017 to build drivers that run on Windows 7 and later.

For help determining what version of WDF to use, see [Which framework version should I use?](building-and-loading-a-kmdf-driver.md#which-framework-version-should-i-use).

For information about the new features for UMDF drivers in Windows 10, see [What's New for WDF Drivers](index.md).

## UMDF Version 2.29

Unchanged from version 2.27.

## UMDF Version 2.27

* Added new API [**WdfDriverRetrieveDriverDataDirectoryString**](/windows-hardware/drivers/ddi/content/wdfdriver/nf-wdfdriver-wdfdriverretrievedriverdatadirectorystring)

## UMDF Version 2.25

* [Building a WDF driver for multiple versions of Windows](building-a-wdf-driver-for-multiple-versions-of-windows.md)
* [**WdfDeviceRetrieveDeviceDirectoryString**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceretrievedevicedirectorystring)

## UMDF Version 2.23

* Companion functionality added for internal use only.  For the new DDIs, see [Summary of WDF Callbacks and Methods](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_wdf/).

## UMDF Version 2.21

* [**WdfObjectDereferenceActual**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfobject/nf-wdfobject-wdfobjectdereferenceactual): Type of *File* parameter changed from PCHAR to PCCH.
* [**WdfObjectReferenceActual**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfobject/nf-wdfobject-wdfobjectreferenceactual): Type of *File* parameter changed from PCHAR to PCCH.

## UMDF Version 2.19

There are no changes or additions for UMDF Version 2.19.

## UMDF Version 2.17

This version adds UMDF support for the following existing interfaces:

-   [**WdfDeviceConfigureWdmIrpDispatchCallback**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceconfigurewdmirpdispatchcallback)
-   [*EvtDeviceWdmIrpDispatch*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_dispatch)
-   [**WdfDeviceWdmDispatchIrp**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchirp)
-   [**WdfDeviceWdmDispatchIrpToIoQueue**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchirptoioqueue)

For more information, see [Dispatching IRPs to I/O Queues](dispatching-irps-to-i-o-queues.md).

## UMDF Version 2.15

Here is the list of updated DDIs for version 2.15:

-   The new [**WdfDeviceOpenDevicemapKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceopendevicemapkey) method allows a driver to access subkeys and values under **HKEY\_LOCAL\_MACHINE\\HARDWARE\\DEVICEMAP**.

-   A UMDF driver can call [**WdfIoTargetWdmGetTargetFileHandle**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfiotarget/nf-wdfiotarget-wdfiotargetwdmgettargetfilehandle) to obtain a file handle to the next-lower kernel-mode driver in its stack. The driver can write data to that handle, bypassing the framework's abstractions for sending I/O to the local I/O target.

-   A UMDF driver can request that the underlying bus driver re-enumerate it. See [**WdfDeviceSetFailed**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicesetfailed).

-   Setting the **UmdfDirectHardwareAccess** directive is no longer always necessary for devices that have connection resources. See [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).

## UMDF Version 2.0


In addition to the shared functionality described in [Getting Started with UMDF](getting-started-with-umdf-version-2.md), UMDF version 2.0 adds:

-   Support for timers that do not wake the system if they expire when the system is in a low-power state. For more information, see [Using Timers](using-timers.md).
-   Added **CanWakeDevice** member to [**WDF\_INTERRUPT\_CONFIG**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/ns-wdfinterrupt-_wdf_interrupt_config) structure to support interrupts that can be used to bring a device from a low-power Dx state back to its fully on D0 state. For more information, see [Using an Interrupt to Wake a Device](using-an-interrupt-to-wake-a-device.md).
-   Single-component, single-state (F0) power management for UMDF drivers. For more information, see [**WdfDeviceAssignS0IdleSettings**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings).

-   Several debugger extension commands in Wdfkd.dll can now be used for UMDF 2.0 drivers as well. The extension library also contains the following new extension commands designed specifically for debugging UMDF 2.0 drivers:

    -   [**!wdfkd.wdfumdevstack**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wdfkd-wdfumdevstack)
    -   [**!wdfkd.wdfumdevstacks**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wdfkd-wdfumdevstacks)
    -   [**!wdfkd.wdfumdownirp**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wdfkd-wdfumdownirp)
    -   [**!wdfkd.wdfumfile**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wdfkd-wdfumfile)
    -   [**!wdfkd.wdfumirp**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wdfkd-wdfumirp)
    -   [**!wdfkd.wdfumirps**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wdfkd-wdfumirps)
    -   [**!wdfkd.wdfdeviceinterrupts**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wdfkd-wdfdeviceinterrupts)

    For a list of extension commands and framework applicability, see [Debugger Extensions](debugger-extensions-for-kmdf-drivers.md).

-   The [framework's event logger](using-the-framework-s-event-logger.md), or *In-flight Recorder* (IFR) has been updated to work for UMDF 2.0 drivers.
-   Other WDF debugger extensions have been updated to work with UMDF 2.0 drivers. For a full list of extension commands, including information about which ones apply to which framework, see [Debugger Extensions for WDF Drivers](debugger-extensions-for-kmdf-drivers.md).
-   Added **WdfIoTargetOpenLocalTargetByFile** to [**WDF\_IO\_TARGET\_OPEN\_TYPE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfiotarget/ne-wdfiotarget-_wdf_io_target_open_type) to allow UMDF drivers to send driver-created requests to lower targets that require an associated file object. For more information, see the Remarks of **WDF\_IO\_TARGET\_OPEN\_TYPE**.
-   The following UMDF-only routines:

    -   [*EvtRequestImpersonate*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nc-wdfrequest-evt_wdf_request_impersonate)
    -   [**WDF\_IO\_TARGET\_OPEN\_PARAMS\_INIT\_OPEN\_BY\_FILE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfiotarget/nf-wdfiotarget-wdf_io_target_open_params_init_open_by_file)
    -   [**WdfDeviceAllocAndQueryInterfaceProperty**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceallocandqueryinterfaceproperty)
    -   [**WdfDeviceAssignInterfaceProperty**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceassigninterfaceproperty)
    -   [**WdfDeviceGetDeviceStackIoType**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicegetdevicestackiotype)
    -   [**WdfDeviceGetHardwareRegisterMappedAddress**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicegethardwareregistermappedaddress)
    -   [**WdfDeviceMapIoSpace**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicemapiospace)
    -   [**WdfDevicePostEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicepostevent)
    -   [**WdfDeviceQueryInterfaceProperty**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicequeryinterfaceproperty)
    -   [**WdfDeviceUnmapIoSpace**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceunmapiospace)
    -   [**WdfFileObjectGetInitiatorProcessId**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdffileobject/nf-wdffileobject-wdffileobjectgetinitiatorprocessid) (added to KMDF 1.21)
    -   [**WdfFileObjectGetRelatedFileObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdffileobject/nf-wdffileobject-wdffileobjectgetrelatedfileobject)
    -   [**WdfRequestGetEffectiveIoType**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestgeteffectiveiotype)
    -   [**WdfRequestGetRequestorProcessId**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestgetrequestorprocessid) (added to KMDF 1.21)
    -   [**WdfRequestGetUserModeInitiatedIo**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestgetusermodedriverinitiatedio)
    -   [**WdfRequestImpersonate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestimpersonate)
    -   [**WdfRequestIsFromUserModeDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestisfromusermodedriver)
    -   [**WdfRequestRetrieveActivityId**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveactivityid)
    -   [**WdfRequestSetActivityId**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestsetactivityid)
    -   [**WdfRequestSetUserModeDriverInitiatedIo**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestsetusermodedriverinitiatedio)
-   The following KMDF/UMDF methods described in [Accessing the Unified Device Property Model](accessing-the-unified-device-property-model.md):

    -   [**WdfDeviceAllocAndQueryPropertyEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceallocandquerypropertyex)
    -   [**WdfDeviceAssignProperty**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceassignproperty)
    -   [**WdfDeviceInitSetIoTypeEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceinitsetiotypeex)
    -   [**WdfDeviceQueryPropertyEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicequerypropertyex)
    -   [**WdfFdoInitAllocAndQueryPropertyEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdffdo/nf-wdffdo-wdffdoinitallocandquerypropertyex)
    -   [**WdfFdoInitQueryPropertyEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdffdo/nf-wdffdo-wdffdoinitquerypropertyex)

    For more information, see [Accessing the Unified Device Property Model](accessing-the-unified-device-property-model.md).

-   Support for the following USB configuration types in [**WdfUsbTargetDeviceSelectConfigType**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/ne-wdfusb-_wdfusbtargetdeviceselectconfigtype):
    -   **WdfUsbTargetDeviceSelectConfigTypeSingleInterface**
    -   **WdfUsbTargetDeviceSelectConfigTypeMultiInterface**
    -   **WdfUsbTargetDeviceSelectConfigTypeInterfacesPairs**
-   Support for querying the following capability types in [**WdfUsbTargetDeviceQueryUsbCapability**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicequeryusbcapability):
    -   **GUID\_USB\_CAPABILITY\_DEVICE\_CONNECTION\_HIGH\_SPEED\_COMPATIBLE**
    -   **GUID\_USB\_CAPABILITY\_DEVICE\_CONNECTION\_SUPER\_SPEED\_COMPATIBLE**
-   Added [WDF Register/Port Access Functions](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfhwaccess/)

## UMDF Version 1.11


Version 1.11 adds the following driver-supplied callback interfaces and event callback functions:

-   [**IPnpCallbackHardware2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-ipnpcallbackhardware2)

-   [**IPnpCallbackHardwareInterrupt**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-ipnpcallbackhardwareinterrupt)

Version 1.11 adds the following framework-supplied interfaces:

-   [**IWDFCmResourceList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdfcmresourcelist)

-   [**IWDFDevice3**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdfdevice3)

-   [**IWDFFile3**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdffile3)

-   [**IWDFInterrupt**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdfinterrupt)

-   [**IWDFIoRequest3**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdfiorequest3)

-   [**IWDFUnifiedPropertyStore**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdfunifiedpropertystore)

-   [**IWDFUnifiedPropertyStoreFactory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdfunifiedpropertystorefactory)

-   [**IWDFWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdfworkitem)

Version 1.11 adds the following capabilities to UMDF-based drivers:

-   [Accessing Hardware and Handling Interrupts](accessing-hardware-and-handling-interrupts.md)

-   [Using Device Pooling in UMDF Drivers](using-device-pooling-in-umdf-drivers.md)

-   Added **UmdfHostProcessSharing**, **UmdfDirectHardwareAccess**, **UmdfRegisterAccessMode**, **UmdfFileObjectPolicy**, and **UmdfFsContextUsePolicy** directives, described in [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md)

-   [Well-known security identifiers (SID) for UMDF drivers](controlling-device-access.md)

-   Unified property store support, described in [Using the Registry in UMDF-based Drivers](https://docs.microsoft.com/windows-hardware/drivers/wdf/using-the-registry-in-umdf-1-x-drivers)

-   [**IoGetDeviceObjectPointer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetdeviceobjectpointer) is integrated to work with UMDF. In prior versions, this routine closes the handle to the device object after taking a reference on the device’s handle. This behavior was incompatible with UMDF’s expectation that the cleanup request on the device object won’t occur until after all the I/O is complete.

-   [Creating UMDF-based HID Minidrivers](creating-umdf-hid-minidrivers.md)

-   Enhanced support for [Supporting Idle Power-Down in UMDF-based Drivers](supporting-idle-power-down-in-umdf-drivers.md). The framework can now put the device in the D3cold power state when the idle timeout period expires. The framework can also cause the device to return to its working (D0) state when the system returns to its working (S0) state.

-   The following samples are new in UMDF 1.11: [WudfVhidmini](https://go.microsoft.com/fwlink/p/?linkid=256226), [NetNfpProvider](https://go.microsoft.com/fwlink/p/?linkid=256147).

## UMDF Version 1.9


Version 1.9 adds the following driver-supplied callback interfaces:

-   [IPnpCallbackRemoteInterfaceNotification](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-ipnpcallbackremoteinterfacenotification)

-   [IPowerPolicyCallbackWakeFromS0](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-ipowerpolicycallbackwakefroms0)

-   [IPowerPolicyCallbackWakeFromSx](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-ipowerpolicycallbackwakefromsx)

-   [IQueueCallbackIoCanceledOnQueue](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iqueuecallbackiocanceledonqueue)

-   [IRemoteInterfaceCallbackEvent](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iremoteinterfacecallbackevent)

-   [IRemoteInterfaceCallbackRemoval](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iremoteinterfacecallbackremoval)

-   [IRemoteTargetCallbackRemoval](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iremotetargetcallbackremoval)

-   [IWDFRemoteInterfaceInitialize](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdfremoteinterfaceinitialize)

Version 1.9 adds the following framework-supplied interfaces:

-   [IWDFDevice2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdfdevice2)

-   [IWDFDeviceInitialize2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdfdeviceinitialize2)

-   [IWDFFile2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdffile2)

-   [IWDFIoRequest2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdfiorequest2)

-   [IWDFIoTarget2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdfiotarget2)

-   [IWDFNamedPropertyStore2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdfnamedpropertystore2)

-   [IWDFPropertyStoreFactory](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdfpropertystorefactory)

-   [IWDFRemoteTarget](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdfremotetarget)

-   [IWDFUsbTargetPipe2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfusb/nn-wudfusb-iwdfusbtargetpipe2)

These interfaces add the following capabilities to UMDF-based drivers:

-   [Remote I/O targets](general-i-o-targets-in-umdf.md)

-   [Power policy ownership](power-policy-ownership-in-umdf.md)

-   The [direct I/O](https://docs.microsoft.com/windows-hardware/drivers/wdf/accessing-data-buffers-in-umdf-1-x-drivers) buffer access method

-   [Continuous readers](https://docs.microsoft.com/windows-hardware/drivers/wdf/working-with-usb-pipes-in-umdf-1-x-drivers) for USB devices

-   Enhanced support for [device interfaces](using-device-interfaces-in-umdf-drivers.md)

-   Enhanced ability to [cancel I/O requests](canceling-i-o-requests.md)

-   Enhanced access to the [registry](https://docs.microsoft.com/windows-hardware/drivers/wdf/using-the-registry-in-umdf-1-x-drivers)

 

 





