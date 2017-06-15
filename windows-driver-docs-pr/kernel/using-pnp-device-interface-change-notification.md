---
title: Using PnP Device Interface Change Notification
author: windows-driver-content
description: Using PnP Device Interface Change Notification
MS-HAID:
- 'PlugPlay\_52c96b08-bae8-4f06-9493-aed27e691d0a.xml'
- 'kernel.using\_pnp\_device\_interface\_change\_notification'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2ed3518a-601f-4e9b-b375-a9fb62c937a9
keywords: ["notifications WDK PnP , device interface changes", "EventCategoryDeviceInterfaceChange notification", "device interface change notifications WDK PnP"]
---

# Using PnP Device Interface Change Notification


## <a href="" id="ddk-using-pnp-device-interface-change-notification-kg"></a>


A driver registers for **EventCategoryDeviceInterfaceChange** notification so the driver can be notified when device interfaces of a particular class arrive (are enabled) or are removed (disabled) on the machine. For example, a composite battery driver might register for notification of device interfaces of class battery so it can provide information to the operating system about total available battery power.

The following subsections discuss how to register for device interface change notification and how to handle device interface change events in a PnP notification callback routine:

[Registering for Device Interface Change Notification](registering-for-device-interface-change-notification.md)

[Handling Device Interface Change Events](handling-device-interface-change-events.md)

See [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) and related routines For information about device interfaces.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20PnP%20Device%20Interface%20Change%20Notification%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


