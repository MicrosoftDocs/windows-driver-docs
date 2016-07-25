---
title: Enabling and Disabling a Device Interface Instance
description: Enabling and Disabling a Device Interface Instance
ms.assetid: 4e3341c2-ba95-458e-8d92-a35545a773e0
keywords: ["interface classes WDK device installations", "disabling device interface instances", "IoSetDeviceInterfaceState", "device interface classes WDK device installations"]
---

# Enabling and Disabling a Device Interface Instance


## <a href="" id="ddk-enabling-and-disabling-a-device-interface-instance-dg"></a>


After successfully starting the device, the driver that registered the interface calls [**IoSetDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff549700) to enable an interface instance. The driver passes the symbolic link name returned by [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) together with the Boolean value **TRUE** to enable the interface instance.

If the driver can successfully start its device, it should call this routine while handling the Plug and Play (PnP) manager's [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request.

After the IRP\_MN\_START\_DEVICE request completes, the PnP manager issues device interface arrival notifications to any kernel-mode or user-mode components that requested them. For more information, see [Registering for Device Interface Change Notification](https://msdn.microsoft.com/library/windows/hardware/ff560884).

To disable a device interface instance, a driver calls [**IoSetDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff549700), passing the *SymbolicLinkName* returned by [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) and **FALSE** as the value of *Enable*.

A driver should disable a device's interfaces when it handles an [**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760) or [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request for the device. If a driver does not disable a device's interfaces when it handles these removal IRPs, it must not subsequently attempt to do this because the PnP manager will disable the interfaces when it removes the device.

A driver should not disable the interfaces when the device is stopped ([**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755)); instead, it should leave any device interfaces enabled and queue I/O requests until it receives another [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request. Similarly, a driver should not disable its interfaces when the device is put in a sleep state. It should queue I/O requests until the device wakes up. For more information, see [Supporting Devices that Have Wake-Up Capabilities](https://msdn.microsoft.com/library/windows/hardware/ff563907).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Enabling%20and%20Disabling%20a%20Device%20Interface%20Instance%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




