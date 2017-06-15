---
title: Removing a Device
author: windows-driver-content
description: Removing a Device
MS-HAID:
- 'PlugPlay\_eb802af7-b83a-4bcd-9e15-856a5e74ab0d.xml'
- 'kernel.removing\_a\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8184987f-5c46-4dd6-aad2-3c32b14205fd
keywords: ["PnP WDK kernel , removing devices", "Plug and Play WDK kernel , removing devices", "removing devices", "notifications WDK PnP , removing devices", "IRPs WDK PnP", "I/O request packets WDK PnP"]
---

# Removing a Device


## <a href="" id="ddk-removing-a-device-kg"></a>


The PnP manager directs drivers to remove their device objects for a device when the device has been, or is being, physically removed from the machine. The PnP manager also sends a *remove* IRP when a user requests to update the drivers for a device and, on Windows 2000 and later, when the device is disabled or fails to start.

The following sections describe when the PnP manager issues *remove* IRPs and what drivers must do to respond to those IRPs. This section covers the following topics:

[Understanding When Remove IRPs Are Issued](understanding-when-remove-irps-are-issued.md)

[Handling an IRP\_MN\_QUERY\_REMOVE\_DEVICE Request](handling-an-irp-mn-query-remove-device-request.md)

[Handling an IRP\_MN\_REMOVE\_DEVICE Request](handling-an-irp-mn-remove-device-request.md)

[Handling an IRP\_MN\_CANCEL\_REMOVE\_DEVICE Request](handling-an-irp-mn-cancel-remove-device-request.md)

[Handling an IRP\_MN\_SURPRISE\_REMOVAL Request](handling-an-irp-mn-surprise-removal-request.md)

[Using Remove Locks](using-remove-locks.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Removing%20a%20Device%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


