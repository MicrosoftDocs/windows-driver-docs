---
title: HKLM\SYSTEM\CurrentControlSet\Control Registry Tree
description: HKLM\SYSTEM\CurrentControlSet\Control registry tree contains information for controlling system startup and some aspects of device configuration.
ms.date: 04/20/2017
---

# HKLM\\SYSTEM\\CurrentControlSet\\Control Registry Tree





The **HKLM\\SYSTEM\\CurrentControlSet\\Control** registry tree contains information for controlling system startup and some aspects of device configuration. The following subkeys are of particular interest:

<a href="" id="class"></a>**Class**  
Contains information about the [device setup classes](./overview-of-device-setup-classes.md) on the system. There is a subkey for each class that is named using the GUID of the setup class. Each subkey contains information about a setup class, such as the class installer (if there is one), registered class upper-filter drivers, and registered class lower-filter drivers.

<a href="" id="codeviceinstallers"></a>**CoDeviceInstallers**  
Contains information about the class-specific co-installers that are registered on the system.

<a href="" id="deviceclasses"></a>**DeviceClasses**  
Contains information about the device interfaces on the system. There is a subkey for each [device interface class](./overview-of-device-interface-classes.md).

 

