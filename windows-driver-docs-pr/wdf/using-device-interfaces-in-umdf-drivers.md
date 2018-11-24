---
title: Using Device Interfaces in UMDF Drivers
description: Using Device Interfaces in UMDF Drivers
ms.assetid: acb6da80-bd04-48f0-b42a-96463f091b0a
keywords:
- user-mode drivers WDK UMDF , device interfaces
- UMDF WDK , device interfaces
- User-Mode Driver Framework WDK , device interfaces
- device interfaces WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Device Interfaces in UMDF Drivers


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

A *device interface* is a symbolic link to a Plug and Play (PnP) device that an application can use to access the device. A user-mode application can pass the interface's symbolic link name to an API element, such as the Microsoft Win32 [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function. To obtain a device interface's symbolic link name, the user-mode application can call **SetupDi** functions. For more information about SetupDi functions, see SetupDi Device Interface Functions.

Each device interface belongs to a *device interface class*. For example, a driver stack for a CD-ROM device might provide an interface that belongs to the GUID\_DEVINTERFACE\_CDROM class. One of the CD-ROM device's drivers would register an instance of the GUID\_DEVINTERFACE\_CDROM class to inform the system and applications that a CD-ROM device is available. For more information about device interface classes, see [Introduction to Device Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff549460).

### Registering a Device Interface

To register an instance of a device interface class, a UMDF-based driver can call [**IWDFDevice::CreateDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff557016) from within its [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) callback function. If the driver supports multiple instances of the interface, it can assign a unique reference string to each instance.

### Enabling and Disabling a Device Interface

If creation succeeds, the framework automatically enables and disables the interface based on the device's PnP state.

In addition, a driver can disable and re-enable a device interface as necessary. For example, if a driver determines that its device has stopped responding, the driver can call [**IWDFDevice::AssignDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff557006) to disable the device's interfaces and prohibit applications from obtaining new handles to the interface. (Existing handles to the interface are not affected.) If the device later becomes available, the driver can call **IWDFDevice::AssignDeviceInterfaceState** again to re-enable the interfaces.

### Receiving Requests to Access a Device Interface

When an application requests access to a driver's device interface, the framework calls the driver's [**IQueueCallbackCreate::OnCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff556841) callback function. The driver can call [**IWDFFile::RetrieveFileName**](https://msdn.microsoft.com/library/windows/hardware/ff558939) to obtain the name of the device or file that the application is accessing. If the driver specified a reference string when it registered the device interface, the operating system includes the reference string in the file or device name that **IWDFFile::RetrieveFileName** returns.

### Creating Device Events

Your UMDF-based driver can create device-specific, custom events (called *device events*) by calling [**IWDFDevice::PostEvent**](https://msdn.microsoft.com/library/windows/hardware/ff558835). A driver that has registered to use any of the device's interfaces can receive notifications of a device's custom events. UMDF-based drivers receive such notifications by providing an [**IRemoteInterfaceCallbackEvent::OnRemoteInterfaceEvent**](https://msdn.microsoft.com/library/windows/hardware/ff556889) callback function.

Custom events are unique to the device. Both the developer of the driver that creates the event and the developer of the driver that receives the event must understand the meaning of the event.

### Accessing Another Driver's Device Interface

If you want your UMDF-based driver to send I/O requests to a device interface that another driver provides, you can create a [remote I/O target](general-i-o-targets-in-umdf.md) that represents the device interface.

First, your driver must register to receive a notification when a device interface is available. Use the following steps:

1.  When your driver calls [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899), the driver can provide an [IPnpCallbackRemoteInterfaceNotification](https://msdn.microsoft.com/library/windows/hardware/ff556772) interface. The [**IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival**](https://msdn.microsoft.com/library/windows/hardware/ff556775) callback function of this interface informs your driver when device interfaces are available.

2.  After your driver calls [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899), it can call [**IWDFDevice2::RegisterRemoteInterfaceNotification**](https://msdn.microsoft.com/library/windows/hardware/ff556939) for each device interface that the driver will use.

Subsequently, the framework calls the driver's [**IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival**](https://msdn.microsoft.com/library/windows/hardware/ff556775) callback function each time that a specified device interface becomes available. The callback function can call [**IWDFRemoteInterfaceInitialize::GetInterfaceGuid**](https://msdn.microsoft.com/library/windows/hardware/ff560238) and [**IWDFRemoteInterfaceInitialize::RetrieveSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff560242) to determine which device interface has arrived.

Your driver's [**IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival**](https://msdn.microsoft.com/library/windows/hardware/ff556775) callback function should typically do the following:

1.  Call [**IWDFDevice2::CreateRemoteInterface**](https://msdn.microsoft.com/library/windows/hardware/ff556925) to create a remote interface object, optionally providing [IRemoteInterfaceCallbackEvent](https://msdn.microsoft.com/library/windows/hardware/ff556887) and [IRemoteInterfaceCallbackRemoval](https://msdn.microsoft.com/library/windows/hardware/ff556891) interfaces.

2.  Call [**IWDFDevice2::CreateRemoteTarget**](https://msdn.microsoft.com/library/windows/hardware/ff556928) to create a remote target object, optionally providing an [IRemoteTargetCallbackRemoval](https://msdn.microsoft.com/library/windows/hardware/ff556894) interface.

3.  Call [**IWDFRemoteTarget::OpenRemoteInterface**](https://msdn.microsoft.com/library/windows/hardware/ff560276) to connect the device interface to the remote target.

    If the device interface is one that the SWENUM software device enumerator creates, your driver must call **OpenRemoteInterface** from a work item. (For example, see the **QueueUserWorkItem** function in the Windows SDK.)

Now the driver can format and send I/O requests to the remote I/O target.

In addition to the [**IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival**](https://msdn.microsoft.com/library/windows/hardware/ff556775) callback function, a UMDF-based driver can provide two additional callback functions to receive notifications of device interface events:

-   The [**IRemoteInterfaceCallbackRemoval::OnRemoteInterfaceRemoval**](https://msdn.microsoft.com/library/windows/hardware/ff556893) callback function notifies the driver when a device interface is removed.

-   The [**IRemoteInterfaceCallbackEvent::OnRemoteInterfaceEvent**](https://msdn.microsoft.com/library/windows/hardware/ff556889) callback function notifies the driver when a device's custom events arrive.

 

 





