---
title: Installing a New Device Setup Class for a Bus
description: Installing a New Device Setup Class for a Bus
ms.assetid: a94899b6-02e0-4181-bb14-5552806a8c9e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a New Device Setup Class for a Bus


If a new bus supports devices whose capabilities are significantly different from the capabilities provided by devices that belong to existing [device setup classes](device-setup-classes.md), you should install a new device setup class for the bus. For more information that helps you determine whether to install a new device setup class, see [Creating a New Device Setup Class](creating-a-new-device-setup-class.md).

To install a new device setup class for the bus, set related directives in the [**INF Version section**](inf-version-section.md), include an [**INF ClassInstall32 section**](inf-classinstall32-section.md), and include additional sections, as needed, that are referenced by the INF Class32 section.

The following annotated example illustrates the basic INF file entries you need to include to install a [device setup class](device-setup-classes.md). For information about the possible configuration settings of a device setup class, see [**INF ClassInstall32 section**](inf-classinstall32-section.md).

```cpp
[Version]
signature="$CHICAGO$"
; Specify a unique class name that identifies the manufacturer and the bus type
Class=%AbcSuperBus%

; Specify a unique GUID that identifies the device setup class
ClassGUID={17ed6609-9bc8-44ca-8548-abb79b13781b}

; Identify the provider of the INF file
Provider=%AbcCorp%

; Specify the version of the device driver
DriverVer=01/01/2007,1.0.0.0 

[ClassInstall32]
; Reference an AddReg directive that specifies class properties
Addreg=AbcSuperBusClassReg 

[AbcSuperBusClassReg]
; Specify the properties of the device setup class
HKR,,,,%AbcSuperBus%
HKR,,Icon,,-19
HKR,,NoInstallClass,,1
. . .
. . .
[Strings] 
AbcCorp="Abc Corporation"
AbcSuperBus="Abc Corporation Super Bus Controller"
```

 

 





