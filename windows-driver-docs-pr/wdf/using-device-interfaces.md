---
title: Using Device Interfaces
description: Using Device Interfaces
ms.assetid: 98199220-947e-462e-a50c-85d81ca50108
keywords:
- device interfaces WDK KMDF
- registering device interfaces WDK KMDF
- receiving device interface access requests WDK KMDF
- device interface classes WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Device Interfaces





A *device interface* is a symbolic link to a Plug and Play (PnP) device that an application can use to access the device. A user-mode application can pass the interface's symbolic link name to an API element, such as the Microsoft Win32 **CreateFile** function. To obtain a device interface's symbolic link name, the user-mode application can call **SetupDi** functions. For more information about **SetupDi** functions, see [Using Device Interface Functions](https://msdn.microsoft.com/library/windows/hardware/ff553567).

Each device interface belongs to a *device interface class*. For example, a driver stack for a CD-ROM device might provide an interface that belongs to the GUID\_DEVINTERFACE\_CDROM class. One of the CD-ROM device's drivers would register an instance of the GUID\_DEVINTERFACE\_CDROM class to inform the system and applications that a CD-ROM device is available. For more information about device interface classes, see [Introduction to Device Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff549460).

### Registering a Device Interface

To register an instance of a device interface class, a framework-based driver can call [**WdfDeviceCreateDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff545935) from within its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function. If the driver supports multiple instances of the interface, it can assign a unique reference string to each instance.

After the driver has registered a device interface, the driver can call [**WdfDeviceRetrieveDeviceInterfaceString**](https://msdn.microsoft.com/library/windows/hardware/ff546842) to obtain the symbolic link name that the system has assigned to the device interface.

For information about other ways that drivers can register device interfaces, see [Registering a Device Interface Class](https://msdn.microsoft.com/library/windows/hardware/ff549810).

### Enabling and Disabling a Device Interface

After a driver calls [**WdfDeviceCreateDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff545935), the framework automatically enables all of a device's interfaces when the device enters its working state and disables the interfaces when the device leaves its working state. If the driver specified a physical device object (PDO) when it called **WdfDeviceCreateDeviceInterface**, the framework re-enables the device's interfaces if a disabled device is re-enabled.

A driver can disable and re-enable a device interface if necessary. For example, if a driver determines that its device has stopped responding, the driver can call [**WdfDeviceSetDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff546878) to disable the device's interfaces and prohibit applications from obtaining new handles to the interface. (Existing handles to the interface are not affected.) If the device later becomes available, the driver can call **WdfDeviceSetDeviceInterfaceState** again to reenable the interfaces.

### Receiving Requests to Access a Device Interface

When an application or kernel-mode component requests access to a driver's device interface, the framework calls the driver's [*EvtDeviceFileCreate*](https://msdn.microsoft.com/library/windows/hardware/ff540868) callback function. The driver can call [**WdfFileObjectGetFileName**](https://msdn.microsoft.com/library/windows/hardware/ff547310) to obtain the name of the device or file that the application or kernel-mode component is accessing. If the driver specified a reference string when it registered the device interface, the operating system includes the reference string in the file or device name that **WdfFileObjectGetFileName** returns.

### Accessing Another Driver's Device Interface

This section shows how a Kernel-Mode Driver Framework (KMDF) driver or a User-Mode Driver Framework (UMDF) version 2 driver registers for notification of arrival or removal of a device interface provided by another driver, and then creates a [remote I/O target](general-i-o-targets-in-umdf.md) to communicate with the device represented by the device interface.

For information on how to do this in a UMDF version 1 driver, see [Using Device Interfaces in UMDF Drivers](using-device-interfaces-in-umdf-drivers.md#accessing-another-drivers-device-interface).

To register for notification of device interface events, a KMDF driver calls [**IoRegisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549526), while a UMDF 2 driver calls [**CM\_Register\_Notification**](https://msdn.microsoft.com/library/windows/hardware/hh780224). In both cases, the driver calls the appropriate routine from its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function.

The following code example shows how a local UMDF 2 driver registers for notifications and then opens the remote I/O target.

1.  The remote driver registers for a device interface by calling [**WdfDeviceCreateDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff545935) from [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693).
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

2.  The local driver calls [**CM\_Register\_Notification**](https://msdn.microsoft.com/library/windows/hardware/hh780224) from [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) to register for notification when a device interface is available. Provide a pointer to a notification callback routine that the framework calls when device interfaces are available.
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


4.  From the work item callback function, the local driver calls [**WdfIoTargetCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548591) to create the remote target, and [**WdfIoTargetOpen**](https://msdn.microsoft.com/library/windows/hardware/ff548634) to open a remote I/O target.

    When calling [**WdfIoTargetOpen**](https://msdn.microsoft.com/library/windows/hardware/ff548634), the driver optionally registers an [*EvtIoTargetQueryRemove*](https://msdn.microsoft.com/library/windows/hardware/ff541793) callback function to receive removal notification, along with the opportunity to decline the removal. If the driver does not provide *EvtIoTargetQueryRemove*, the framework closes the I/O target when the device is removed.

    In rare cases, a UMDF 2 driver can call [**CM\_Register\_Notification**](https://msdn.microsoft.com/library/windows/hardware/hh780224) a second time, to register for notification of device removal. For example, if the driver calls [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) to get a HANDLE to the device interface, it should register for notification of device removal so that it can properly respond to query remove attempts. In most cases, the UMDF 2 driver calls **CM\_Register\_Notification** only once, and relies on WDF support for device removal.

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


[Registering for Notification of Device Interface Arrival and Device Removal](https://msdn.microsoft.com/library/windows/hardware/dn858592)










