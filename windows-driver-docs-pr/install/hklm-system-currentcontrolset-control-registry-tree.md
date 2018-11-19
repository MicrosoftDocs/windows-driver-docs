---
title: HKLM\SYSTEM\CurrentControlSet\Control Registry Tree
description: HKLM\SYSTEM\CurrentControlSet\Control registry tree contains information for controlling system startup and some aspects of device configuration.
ms.assetid: 58eacd32-425d-4224-8d37-21e2caf124cf
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HKLM\\SYSTEM\\CurrentControlSet\\Control Registry Tree





The **HKLM\\SYSTEM\\CurrentControlSet\\Control** registry tree contains information for controlling system startup and some aspects of device configuration. The following subkeys are of particular interest:

<a href="" id="class"></a>**Class**  
Contains information about the [device setup classes](device-setup-classes.md) on the system. There is a subkey for each class that is named using the GUID of the setup class. Each subkey contains information about a setup class, such as the class installer (if there is one), registered class upper-filter drivers, and registered class lower-filter drivers.

Each class subkey contains other subkeys known as *software keys* (or, *driver keys*) for each device instance of that class installed in the system. Each of these software keys is named by using a device instance ID, which is a base-10, four-digit ordinal value.

<a href="" id="codeviceinstallers"></a>**CoDeviceInstallers**  
Contains information about the class-specific co-installers that are registered on the system.

<a href="" id="deviceclasses"></a>**DeviceClasses**  
Contains information about the device interfaces on the system. There is a subkey for each [device interface class](device-interface-classes.md) and entries under those subkeys for each instance of an interface that is registered for the device interface class.

 

 





