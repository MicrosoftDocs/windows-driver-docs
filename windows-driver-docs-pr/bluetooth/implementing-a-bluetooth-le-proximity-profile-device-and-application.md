---
title: Bluetooth LE Proximity Profile Devices and Apps
description: Proximity detection is a common use of Bluetooth Low Energy (LE).
ms.assetid: 4BF27CBE-C89A-48DC-8536-1A5111CDB0C4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bluetooth LE Proximity Profile Devices and Apps


Proximity detection is a common use of Bluetooth Low Energy (LE). Windows 8.1 expands on the Bluetooth LE support introduced in Windows 8. This section provides guidelines to create a device implementation of the Proximity Profile that you can use to develop a UWP device app that's compatible with Windows 8.1.

Before you develop this app, you should be familiar with Bluetooth LE functions and the Bluetooth LE Proximity profile specification.

## <span id="Example_Service_Declaration"></span><span id="example_service_declaration"></span><span id="EXAMPLE_SERVICE_DECLARATION"></span>Example Service Declaration


Bluetooth Low Energy introduced a new physical layer that shares the same frequency space as Bluetooth Basic Rate. Low Energy Profiles are organized into what’s called the Generic Attribute Profile (or GATT).

A GATT profile declares one or more services that define a use case or scenario. To develop a compliant service implementation, you must organize *characteristics* so that they conform to the established schema defined on the [Bluetooth Special Interest Group (SIG) developer website](http://go.microsoft.com/fwlink/p/?linkid=320723).

This diagram shows how *characteristics* are structured inside a typical GATT service.

![example gatt service declaration](images/bthleservicedeclaration.png)

An example proximity profile is described further in [Bluetooth Proximity Profile](bluetooth-proximity-profile.md).

 

 





