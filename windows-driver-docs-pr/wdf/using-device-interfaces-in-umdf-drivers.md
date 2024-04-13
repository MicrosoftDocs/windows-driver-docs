---
title: Using Device Interfaces in UMDF Drivers
description: Using Device Interfaces in UMDF Drivers
keywords:
- user-mode drivers WDK UMDF , device interfaces
- UMDF WDK , device interfaces
- User-Mode Driver Framework WDK , device interfaces
- device interfaces WDK UMDF
ms.date: 04/20/2017
---

# Using Device Interfaces in UMDF Drivers


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

A *device interface* is a symbolic link to a Plug and Play (PnP) device that an application can use to access the device. A user-mode application can pass the interface's symbolic link name to an API element, such as the Microsoft Win32 [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) function. To obtain a device interface's symbolic link name, the user-mode application can call **SetupDi** functions. For more information about SetupDi functions, see SetupDi Device Interface Functions.

Each device interface belongs to a *device interface class*. For example, a driver stack for a CD-ROM device might provide an interface that belongs to the GUID\_DEVINTERFACE\_CDROM class. One of the CD-ROM device's drivers would register an instance of the GUID\_DEVINTERFACE\_CDROM class to inform the system and applications that a CD-ROM device is available. For more information about device interface classes, see [Introduction to Device Interfaces](../install/overview-of-device-interface-classes.md).

### Registering a Device Interface

To register an instance of a device interface class, a UMDF-based driver can call [**IWDFDevice::CreateDeviceInterface**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createdeviceinterface) from within its [**IDriverEntry::OnDeviceAdd**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) callback function. If the driver supports multiple instances of the interface, it can assign a unique reference string to each instance.

### Enabling and Disabling a Device Interface

If creation succeeds, the framework automatically enables and disables the interface based on the device's PnP state.

In addition, a driver can disable and re-enable a device interface as necessary. For example, if a driver determines that its device has stopped responding, the driver can call [**IWDFDevice::AssignDeviceInterfaceState**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-assigndeviceinterfacestate) to disable the device's interfaces and prohibit applications from obtaining new handles to the interface. (Existing handles to the interface are not affected.) If the device later becomes available, the driver can call **IWDFDevice::AssignDeviceInterfaceState** again to re-enable the interfaces.

### Receiving Requests to Access a Device Interface

When an application requests access to a driver's device interface, the framework calls the driver's [**IQueueCallbackCreate::OnCreateFile**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackcreate-oncreatefile) callback function. The driver can call [**IWDFFile::RetrieveFileName**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdffile-retrievefilename) to obtain the name of the device or file that the application is accessing. If the driver specified a reference string when it registered the device interface, the operating system includes the reference string in the file or device name that **IWDFFile::RetrieveFileName** returns.

### Creating Device Events

Your UMDF-based driver can create device-specific, custom events (called *device events*) by calling [**IWDFDevice::PostEvent**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-postevent). A driver that has registered to use any of the device's interfaces can receive notifications of a device's custom events. UMDF-based drivers receive such notifications by providing an [**IRemoteInterfaceCallbackEvent::OnRemoteInterfaceEvent**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iremoteinterfacecallbackevent-onremoteinterfaceevent) callback function.

Custom events are unique to the device. Both the developer of the driver that creates the event and the developer of the driver that receives the event must understand the meaning of the event.

### Accessing Another Driver's Device Interface

If you want your UMDF-based driver to send I/O requests to a device interface that another driver provides, you can create a [remote I/O target](general-i-o-targets-in-umdf.md) that represents the device interface.

First, your driver must register to receive a notification when a device interface is available. Use the following steps:

1.  When your driver calls [**IWDFDriver::CreateDevice**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdriver-createdevice), the driver can provide an [IPnpCallbackRemoteInterfaceNotification](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallbackremoteinterfacenotification) interface. The [**IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackremoteinterfacenotification-onremoteinterfacearrival) callback function of this interface informs your driver when device interfaces are available.

2.  After your driver calls [**IWDFDriver::CreateDevice**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdriver-createdevice), it can call [**IWDFDevice2::RegisterRemoteInterfaceNotification**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice2-registerremoteinterfacenotification) for each device interface that the driver will use.

Subsequently, the framework calls the driver's [**IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackremoteinterfacenotification-onremoteinterfacearrival) callback function each time that a specified device interface becomes available. The callback function can call [**IWDFRemoteInterfaceInitialize::GetInterfaceGuid**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfremoteinterfaceinitialize-getinterfaceguid) and [**IWDFRemoteInterfaceInitialize::RetrieveSymbolicLink**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfremoteinterfaceinitialize-retrievesymboliclink) to determine which device interface has arrived.

Your driver's [**IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackremoteinterfacenotification-onremoteinterfacearrival) callback function should typically do the following:

1.  Call [**IWDFDevice2::CreateRemoteInterface**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice2-createremoteinterface) to create a remote interface object, optionally providing [IRemoteInterfaceCallbackEvent](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iremoteinterfacecallbackevent) and [IRemoteInterfaceCallbackRemoval](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iremoteinterfacecallbackremoval) interfaces.

2.  Call [**IWDFDevice2::CreateRemoteTarget**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice2-createremotetarget) to create a remote target object, optionally providing an [IRemoteTargetCallbackRemoval](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iremotetargetcallbackremoval) interface.

3.  Call [**IWDFRemoteTarget::OpenRemoteInterface**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfremotetarget-openremoteinterface) to connect the device interface to the remote target.

    If the device interface is one that the SWENUM software device enumerator creates, your driver must call **OpenRemoteInterface** from a work item. (For example, see the **QueueUserWorkItem** function in the Windows SDK.)

Now the driver can format and send I/O requests to the remote I/O target.

In addition to the [**IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackremoteinterfacenotification-onremoteinterfacearrival) callback function, a UMDF-based driver can provide two additional callback functions to receive notifications of device interface events:

-   The [**IRemoteInterfaceCallbackRemoval::OnRemoteInterfaceRemoval**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iremoteinterfacecallbackremoval-onremoteinterfaceremoval) callback function notifies the driver when a device interface is removed.

-   The [**IRemoteInterfaceCallbackEvent::OnRemoteInterfaceEvent**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iremoteinterfacecallbackevent-onremoteinterfaceevent) callback function notifies the driver when a device's custom events arrive.

 

