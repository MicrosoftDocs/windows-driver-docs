---
title: HKLM\\SYSTEM\\CurrentControlSet\\Control Registry Tree
description: HKLM\\SYSTEM\\CurrentControlSet\\Control Registry Tree
ms.assetid: 58eacd32-425d-4224-8d37-21e2caf124cf
---

# HKLM\\SYSTEM\\CurrentControlSet\\Control Registry Tree


## <a href="" id="ddk-the-hklm-system-currentcontrolset-control-tree-dg"></a>


The **HKLM\\SYSTEM\\CurrentControlSet\\Control** registry tree contains information for controlling system startup and some aspects of device configuration. The following subkeys are of particular interest:

<a href="" id="class"></a>**Class**  
Contains information about the [device setup classes](device-setup-classes.md) on the system. There is a subkey for each class that is named using the GUID of the setup class. Each subkey contains information about a setup class, such as the class installer (if there is one), registered class upper-filter drivers, and registered class lower-filter drivers.

Each class subkey contains other subkeys known as *software keys* (or, *driver keys*) for each device instance of that class installed in the system. Each of these software keys is named by using a device instance ID, which is a base-10, four-digit ordinal value.

<a href="" id="codeviceinstallers"></a>**CoDeviceInstallers**  
Contains information about the class-specific co-installers that are registered on the system.

<a href="" id="deviceclasses"></a>**DeviceClasses**  
Contains information about the device interfaces on the system. There is a subkey for each [device interface class](device-interface-classes.md) and entries under those subkeys for each instance of an interface that is registered for the device interface class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20HKLM\SYSTEM\CurrentControlSet\Control%20Registry%20Tree%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




