---
title: Bluetooth Low Energy Overview
description: This section provides an overview of Bluetooth Low Energy introduced in Windows 8
ms.assetid: 8783E31B-99A3-40EB-8A67-647AFAB7D4D3
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Bluetooth Low Energy Overview


Windows 8 introduces support for the Bluetooth Low Energy technology.

Bluetooth Low Energy introduces a new physical layer that shares the same frequency space as Bluetooth Basic Rate. Profiles that are developed on this technology are organized into the Generic Attribute Profile (or GATT).

Each profile defines the use of one or more services to create a use case or scenario. Compliant service implementations are constructed from characteristics organized in a way that conforms to the established schema defined on the Bluetooth Special Interest Group [developer website](http://developer.bluetooth.org/gatt/services/Pages/ServicesHome.aspx).

The diagram below illustrates the way objects are structured inside a typical GATT service.

![bluetooth low energy gatt service declarations](images/bthleservicedeclaration.png)

When a Bluetooth Low Energy device is paired with a Windows 8 machine, the device becomes part of the system and Windows will provide device objects to represent both the device and the primary services reported by the device.

![device object structure of the windows 8 bluetooth low energy implementation](images/bthlewin8supt.png)

Each device and its primary services are represented as device objects in Windows and these device objects can be queried and managed using the [device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff549791) such as [**SetupDiEnumDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff551010), and [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963).

In addition to the standard [Bluetooth Profile Driver functions](https://msdn.microsoft.com/library/windows/hardware/hh450828), Windows 8 introduces new [Bluetooth Low Energy functions](https://msdn.microsoft.com/library/windows/hardware/hh450825) which allows for the development of Bluetooth GATT client applications.

These functions allows for the enumeration of services and their objects (including services, characteristics and their descriptors) as well as read and write capabilities.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[bltooth\bltooth]:%20Bluetooth%20Low%20Energy%20Overview%20%20RELEASE:%20%283/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




