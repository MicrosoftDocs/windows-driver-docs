---
title: Using Device Interfaces (WDF)
description: Using Device Interfaces
keywords:
- device interfaces WDK KMDF
- registering device interfaces WDK KMDF
- receiving device interface access requests WDK KMDF
- device interface classes WDK KMDF
ms.date: 06/14/2023
---

# Using Device Interfaces (WDF)

A *device interface* is a symbolic link to a Plug and Play (PnP) device that an application can use to access the device. A user-mode application can pass the interface's symbolic link name to an API element, such as the Microsoft Win32 **CreateFile** function. To obtain a device interface's symbolic link name, the user-mode application can call [configuration manager functions](/windows/win32/api/cfgmgr32/) or [SetupApi functions](../install/setupapi.md). For more information, see [Enumerating installed device interfaces](../install/enumerating-installed-device-interface-classes.md).

Each device interface belongs to a *device interface class*. For example, a driver stack for a CD-ROM device might provide an interface that belongs to the GUID\_DEVINTERFACE\_CDROM class. One of the CD-ROM device's drivers would register an instance of the GUID\_DEVINTERFACE\_CDROM class to inform the system and applications that a CD-ROM device is available. For more information about device interface classes, see [Overview of Device Interface Classes](../install/overview-of-device-interface-classes.md).

### Registering a Device Interface

To register an instance of a device interface class, a framework-based driver can call [**WdfDeviceCreateDeviceInterface**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreatedeviceinterface) either before or after the device starts. If the driver supports multiple instances of the interface, it can assign a unique reference string to each instance.

After the driver has registered a device interface, the driver can call [**WdfDeviceRetrieveDeviceInterfaceString**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceretrievedeviceinterfacestring) to obtain the symbolic link name that the system has assigned to the device interface.

For information about other ways that drivers can register device interfaces, see [Registering a Device Interface Class](../install/registering-a-device-interface-class.md).

### Enabling and Disabling a Device Interface

Interfaces created before the device starts (for example from [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add), [*EvtChildListCreateDevice*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_create_device), or [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware)) are automatically enabled by the framework when the device goes through PnP enumeration and starts. To prevent the interface from being automatically enabled during PnP start, call [**WdfDeviceSetDeviceInterfaceStateEx**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetdeviceinterfacestateex) from the same callback function (set the *EnableInterface* parameter to FALSE) for that interface before PnP start.

Interfaces created after the device already starts won't be automatically enabled. The driver must call [**WdfDeviceSetDeviceInterfaceState**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetdeviceinterfacestate) or [**WdfDeviceSetDeviceInterfaceStateEx**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetdeviceinterfacestateex) to enable such interfaces.

All interfaces are automatically disabled when the device undergoes PnP removal. Note that any device power state changes or PnP resource rebalance do not change the interface's state.

A driver can disable and re-enable a device interface if necessary. For example, if a driver determines that its device has stopped responding, the driver can call [**WdfDeviceSetDeviceInterfaceState**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetdeviceinterfacestate) or [**WdfDeviceSetDeviceInterfaceStateEx**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetdeviceinterfacestateex) to disable the device's interfaces and prohibit applications from obtaining new handles to the interface. (Existing handles to the interface are not affected.) If the device later becomes available, the driver can call **WdfDeviceSetDeviceInterfaceState** or **WdfDeviceSetDeviceInterfaceStateEx** again to reenable the interfaces.

### Receiving Requests to Access a Device Interface

When an application or kernel-mode component requests access to a driver's device interface, the framework calls the driver's [*EvtDeviceFileCreate*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_file_create) callback function. The driver can call [**WdfFileObjectGetFileName**](/windows-hardware/drivers/ddi/wdffileobject/nf-wdffileobject-wdffileobjectgetfilename) to obtain the name of the device or file that the application or kernel-mode component is accessing. If the driver specified a reference string when it registered the device interface, the operating system includes the reference string in the file or device name that **WdfFileObjectGetFileName** returns.

### Accessing Another Driver's Device Interface

This section shows how a Kernel-Mode Driver Framework (KMDF) driver or a User-Mode Driver Framework (UMDF) version 2 driver registers for notification of arrival or removal of a device interface provided by another driver, and then creates a [remote I/O target](general-i-o-targets-in-umdf.md) to communicate with the device represented by the device interface.

For information on how to do this in a UMDF version 1 driver, see [Using Device Interfaces in UMDF Drivers](using-device-interfaces-in-umdf-drivers.md#accessing-another-drivers-device-interface).

To register for notification of device interface events, a KMDF driver calls [**IoRegisterPlugPlayNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterplugplaynotification), while a UMDF 2 driver calls [**CM\_Register\_Notification**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_register_notification). In both cases, the driver calls the appropriate routine from its [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function.

The following code example shows how a local UMDF 2 driver registers for notifications and then opens the remote I/O target.

1.  The remote driver registers for a device interface by calling [**WdfDeviceCreateDeviceInterface**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreatedeviceinterface) from [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add).
    ```cpp
        UNICODE_STRING ref;
        RtlInitUnicodeString(&ref, MY_HID_FILTER_REFERENCE_STRING);
        status = WdfDeviceCreateDeviceInterface(
                     hDevice,
                     (LPGUID) &GUID_DEVINTERFACE_MY_HIDFILTER_DRIVER,
                     &ref // ReferenceString
                 );

        if (!NT_SUCCESS (status)) {
            MyKdPrint( ("WdfDeviceCreateDeviceInterface failed 0x%x\n", status));
            return status;
        }

    ```

2.  The local driver calls [**CM\_Register\_Notification**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_register_notification) from [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) to register for notification when a device interface is available. Provide a pointer to a notification callback routine that the framework calls when device interfaces are available.
    ```cpp
    DWORD cmRet;
        CM_NOTIFY_FILTER cmFilter;

        ZeroMemory(&cmFilter, sizeof(cmFilter));
        cmFilter.cbSize = sizeof(cmFilter);
        cmFilter.FilterType = CM_NOTIFY_FILTER_TYPE_DEVICEINTERFACE;
        cmFilter.u.DeviceInterface.ClassGuid = GUID_DEVINTERFACE_MY_HIDFILTER_DRIVER;

        cmRet = CM_Register_Notification(
                    &cmFilter,                     // PCM_NOTIFY_FILTER pFilter,
                    (PVOID) hDevice,               // PVOID pContext,
                    MyCmInterfaceNotification,    // PCM_NOTIFY_CALLBACK pCallback,
                    &fdoData->CmNotificationHandle // PHCMNOTIFICATION pNotifyContext
                    );
        if (cmRet != CR_SUCCESS) {
            MyKdPrint( ("CM_Register_Notification failed, error %d\n", cmRet));
            status = STATUS_UNSUCCESSFUL;
            return status;
        }   
    ```

3.  The system calls the local driver's notification callback routine each time that the specified device interface arrives or is removed. The callback routine can examine the *EventData* parameter to determine which device interface has arrived. It might then queue a work item to open the device interface.
    ```cpp
    DWORD 
    MyCmInterfaceNotification(
        _In_ HCMNOTIFICATION       hNotify,
        _In_opt_ PVOID             Context,
        _In_ CM_NOTIFY_ACTION      Action,
        _In_reads_bytes_(EventDataSize) PCM_NOTIFY_EVENT_DATA EventData,
        _In_ DWORD                 EventDataSize
        )
    {
        PFDO_DATA fdoData;
        UNICODE_STRING name;
        WDFDEVICE device;
        NTSTATUS status;
        WDFWORKITEM workitem;

        UNREFERENCED_PARAMETER(hNotify);
        UNREFERENCED_PARAMETER(EventDataSize);

        device = (WDFDEVICE) Context;
        fdoData = ToasterFdoGetData(device);

        switch(Action) {
        case CM_NOTIFY_ACTION_DEVICEINTERFACEARRIVAL: 
            MyKdPrint( ("MyCmInterfaceNotification: Arrival of %S\n",
                EventData->u.DeviceInterface.SymbolicLink));

            //
            // Enqueue a work item to open target
            //

            break;
        case CM_NOTIFY_ACTION_DEVICEINTERFACEREMOVAL: 
            MyKdPrint( ("MyCmInterfaceNotification: removal of %S\n",
                EventData->u.DeviceInterface.SymbolicLink));
            break;
        default:
            MyKdPrint( ("MyCmInterfaceNotification: Arrival unknown action\n"));
            break;
        }

        return 0;
    }
    ```


4.  From the work item callback function, the local driver calls [**WdfIoTargetCreate**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetcreate) to create the remote target, and [**WdfIoTargetOpen**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetopen) to open a remote I/O target.

    When calling [**WdfIoTargetOpen**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetopen), the driver optionally registers an [*EvtIoTargetQueryRemove*](/windows-hardware/drivers/ddi/wdfiotarget/nc-wdfiotarget-evt_wdf_io_target_query_remove) callback function to receive removal notification, along with the opportunity to decline the removal. If the driver does not provide *EvtIoTargetQueryRemove*, the framework closes the I/O target when the device is removed.

    In rare cases, a UMDF 2 driver can call [**CM\_Register\_Notification**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_register_notification) a second time, to register for notification of device removal. For example, if the driver calls [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) to get a HANDLE to the device interface, it should register for notification of device removal so that it can properly respond to query remove attempts. In most cases, the UMDF 2 driver calls **CM\_Register\_Notification** only once, and relies on WDF support for device removal.

    ```cpp
    VOID 
    EvtWorkItem(
        _In_ WDFWORKITEM WorkItem
    )
    {
        // 
        // create and open remote target
        //

        return;
    }
    ```

## Related topics

[Registering for Notification of Device Interface Arrival and Device Removal](../install/registering-for-notification-of-device-interface-arrival-and-device-removal.md)
