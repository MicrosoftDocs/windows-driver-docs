---
title: Supporting PC Cards That Have Incomplete Configuration Registers
description: Supporting PC Cards That Have Incomplete Configuration Registers
ms.assetid: 62bdb1e7-ca45-42e6-bdf5-c48fb3ddb3fc
keywords:
- incomplete configuration registers WDK multifunction devices
- system-supplied multifunction bus drivers WDK
- mf.sys
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting PC Cards That Have Incomplete Configuration Registers





If a multifunction 16-bit PC Card device does not have configuration registers for each function, the vendor of such a device can use the system-supplied multifunction bus driver (mf.sys) but must provide a custom INF file and support for the individual functions.

The vendor of such a device on an NT-based platform can use the following system-supplied component:

-   A function driver for the multifunction device. (system-supplied)

    A custom INF for the device must specify mf.sys as the function driver for the device. The system-supplied mf.sys driver will then enumerate the functions of the device.

    See [Using the System-Supplied Multifunction Bus Driver](using-the-system-supplied-multifunction-bus-driver.md) for more information about using the system-supplied mf.sys driver.

The vendor of such a device must provide the following:

-   A custom INF file for the multifunction device. (vendor-supplied)

    The vendor must supply a multifunction INF file that specifies mf.sys as the multifunction bus driver, specifies the class "MultiFunction" (with its associated GUID as defined in devguid.h), and provides the missing configuration register information. See further information later in this section.

-   A PnP function driver for each function of the device. (vendor-supplied)

    Since the multifunction bus driver handles the multifunction semantics, the function drivers can be the same drivers that are used when the functions are packaged as individual devices.

-   An INF file for each function of the device. (vendor-supplied)

    The INF files can be the same files that are used when the functions are packaged as a individual devices. The INF files do not need any special multifunction semantics.

The vendor-supplied custom INF for such a device must specify:

-   mf.sys as the service for the device.

    See [Using the System-Supplied Multifunction Bus Driver](using-the-system-supplied-multifunction-bus-driver.md) for more information.

-   The resource requirements of the multifunction device.

    Specify the resource requirements in [**INF DDInstall.LogConfigOverride sections**](https://msdn.microsoft.com/library/windows/hardware/ff547339).

-   The hardware ID for each function of the device.

    Specify the hardware IDs in an [**INF DDInstall.HW section**](https://msdn.microsoft.com/library/windows/hardware/ff547330).

-   A resource map for each function of the device, identifying the parent resources required by each child function.

    Specify the resource maps in an INF *DDInstall*.**HW** section. See [Creating Resource Maps for a Multifunction Device](creating-resource-maps-for-a-multifunction-device.md) for more information about creating resource maps.

The INF must restate all the resource requirements specified by the device because if override configurations are present in the INF, the PnP manager does not use any device resource requirements from the device.

For such a device, the configuration option register can be programmed using a **PcCardConfig** entry, similar to programming a single-function device. The **PcCardConfig** entry contains information that applies to the entire device. The **PcCardConfig** entry is documented in [**INF LogConfig Directive**](https://msdn.microsoft.com/library/windows/hardware/ff547448).

When specifying a **PcCardConfig** entry for a multifunction device, the format of the *ConfigIndex* is the same as that defined for a single-function device. The configuration register for single-function PC Cards contains an index to a set of resources defined in that device's attributes. This directive can also be used with certain multifunction devices that use the index-based format of the configuration option register.

The following example shows an INF file for installing a multifunction device that uses mf.sys as its bus driver and has incomplete configuration registers.

```cpp
; MFSupra.inf
; This file installs the Supra Dual 56K modem
; Copyright 1999 Microsoft Corporation

[version]
Signature  = "$Windows NT$"
provider   = %MSFT%
Class      = MultiFunction              ; system-defined class
ClassGUID  = {4d36e971-e325-11ce-bfc1-08002be10318}

[ControlFlags]
ExcludeFromSelect=*SUP2440  ; don&#39;t include PnP devices in lists of
                            ; devices to be manually installed

[Manufacturer]
%M_Supra% = Supra

[Supra]
%Supra1% = Sup2231GoCard.mf, *SUP2440 

[Sup2231GoCard.mf.NT]
Include = mf.inf           ; specify that this device needs mf.sys
Needs = MFINSTALL.mf

[Sup2231GoCard.mf.NT.HW]
AddReg=Sup2231.mf.RegHW

[Sup2231.mf.RegHW]   
HKR, Child0000, HardwareID,  ,  MF\Shotgun_DEV0  ;modem1
HKR,Child0000,ResourceMap,1,00,02
HKR, Child0001, HardwareID,  ,  MF\Shotgun_DEV1  ;modem2
HKR,Child0001,ResourceMap,1,01,02

[Sup2231GoCard.mf.NT.Services]   
Include = mf.inf
Needs = MFINSTALL.mf.Services

[Sup2231GoCard.mf.NT.LogConfigOverride]   
LogConfig = Sup223x.mf.Override0, Sup223x.mf.Override1, \
 Sup223x.mf.Override2, Sup223x.mf.Override3

[Sup223x.mf.Override0]
ConfigPriority = NORMAL
IOConfig     = 2F8-2FF                  ; Com2
IOConfig     = 20@100-FFFF%FFE0         ; NIC I/O
IRQConfig    = 3,4,5,7,9,10,11,12,15          ; IRQ    
MemConfig    = 1000@0-FFFFFFFF%FFFFF000 ; Memory Descriptor
PCCardConfig = 59(W)                    ; ConfigIndex

[Sup223x.mf.Override1]
ConfigPriority = NORMAL
IOConfig     = 3E8-3EF                  ; Com3
IOConfig     = 20@100-FFFF%FFE0         ; NIC I/O
IRQConfig    = 3,4,5,7,9,10,11,12,15          ; IRQ    
MemConfig    = 1000@0-FFFFFFFF%FFFFF000 ; Memory Descriptor
PCCardConfig = 69(W)                    ; ConfigIndex

[Sup223x.mf.Override2]
ConfigPriority = NORMAL
IOConfig     = 2E8-2EF                  ; Com4
IOConfig     = 20@100-FFFF%FFE0         ; NIC I/O
IRQConfig    = 3,4,5,7,9,10,11,12,15          ; IRQ    
MemConfig    = 1000@0-FFFFFFFF%FFFFF000 ; Memory Descriptor
PCCardConfig = 79(W)                    ; ConfigIndex

[Sup223x.mf.Override3]
ConfigPriority = NORMAL
IOConfig     = 3F8-3FF                  ; Com1
IOConfig     = 20@100-FFFF%FFE0         ; NIC I/O
IRQConfig    = 3,4,5,7,9,10,11,12,15          ; IRQ
MemConfig    = 1000@0-FFFFFFFF%FFFFF000 ; Memory Descriptor
PCCardConfig = 49(W)                    ; ConfigIndex

[strings]
MSFT = "Microsoft"
M_Supra = "Supra"
Supra1 = "Supra Dual 56K modem"
```

An INF like the one shown above copies the ID and resource information for the child functions to the registry. The mf.sys driver retrieves the information from the registry when it enumerates the child functions of the device.








