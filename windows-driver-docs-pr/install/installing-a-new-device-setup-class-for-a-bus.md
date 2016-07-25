---
title: Installing a New Device Setup Class for a Bus
description: Installing a New Device Setup Class for a Bus
ms.assetid: a94899b6-02e0-4181-bb14-5552806a8c9e
---

# Installing a New Device Setup Class for a Bus


If a new bus supports devices whose capabilities are significantly different from the capabilities provided by devices that belong to existing [device setup classes](device-setup-classes.md), you should install a new device setup class for the bus. For more information that helps you determine whether to install a new device setup class, see [Creating a New Device Setup Class](creating-a-new-device-setup-class.md).

To install a new device setup class for the bus, set related directives in the [**INF Version section**](inf-version-section.md), include an [**INF ClassInstall32 section**](inf-classinstall32-section.md), and include additional sections, as needed, that are referenced by the INF Class32 section.

The following annotated example illustrates the basic INF file entries you need to include to install a [device setup class](device-setup-classes.md). For information about the possible configuration settings of a device setup class, see [**INF ClassInstall32 section**](inf-classinstall32-section.md).

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installing%20a%20New%20Device%20Setup%20Class%20for%20a%20Bus%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




