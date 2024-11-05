---
title: HKLM\SYSTEM\CurrentControlSet\Control Registry Tree
description: HKLM\SYSTEM\CurrentControlSet\Control registry tree contains information for controlling system startup and some aspects of device configuration.
ms.date: 11/05/2024
---

# HKLM\\SYSTEM\\CurrentControlSet\\Control Registry Tree

The **HKLM\\SYSTEM\\CurrentControlSet\\Control** registry tree contains information for controlling system startup and some aspects of device configuration. The following subkeys are of particular interest:

## Class

Contains information about the [device setup classes](./overview-of-device-setup-classes.md) on the system. There's a subkey for each class that is named using the GUID of the setup class. Each subkey contains information about a setup class. Subkey information might include the class installer, registered class upper-filter drivers, and registered class lower-filter drivers.

## CoDeviceInstallers

Contains information about the class specific coinstallers that are registered on the system.

## DeviceClasses

Contains information about the device interfaces on the system. There's a subkey for each [device interface class](./overview-of-device-interface-classes.md).
