---
title: PC cards with incomplete configuration register addresses
description: Information on supporting PC cards with incomplete configuration register addresses
ms.assetid: 2a708ca5-a119-4ef5-81ee-d9e40e7a5255
keywords:
- incomplete configuration registers WDK multifunction devices
- system-supplied multifunction bus drivers WDK
- mf.sys
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PC cards with incomplete configuration register addresses


If a multifunction 16-bit PC Card device has configuration registers for each function but does not contain pointers in attribute memory to all register sets (does not support the LONGLINK\_MFC tuple), the vendor of such a device can use the system-supplied multifunction bus driver (mf.sys) but must provide a custom INF file and support for the individual functions.

The vendor of such a device on an NT-based platform can use a system-supplied function driver for the multifunction device.

A custom INF for the device must specify mf.sys as the function driver for the device. The system-supplied mf.sys driver will then enumerate the functions of the device.

See [Using the System-Supplied Multifunction Bus Driver](using-the-system-supplied-multifunction-bus-driver.md) for more information about using the system-supplied mf.sys driver.

The vendor of such a device must provide the following:

-   A custom INF file for the multifunction device. (vendor-supplied)

    The vendor must supply a multifunction INF file that specifies mf.sys as the multifunction bus driver, specifies the class "MultiFunction" (with its associated GUID as defined in devguid.h), and provides the missing configuration register address(es). See further information later in this section.

-   A PnP function driver for each function of the device. (vendor-supplied)

    Since the multifunction bus driver handles the multifunction semantics, the function drivers can be the same drivers that are used when the functions are packaged as individual devices.

-   An INF file for each function of the device. (vendor-supplied)

    The INF files can be the same files that are used when the functions are packaged as individual devices. The INF files do not need any special multifunction semantics.

The custom INF for such a multifunction device must contain at least one [**INF DDInstall.LogConfigOverride section**](https://msdn.microsoft.com/library/windows/hardware/ff547339). The override section must contain an **MfCardConfig** entry for each function, identifying the location of each set of configuration registers.

The INF must restate all the resource requirements specified by the device because if override configurations are present in the INF, the PnP manager does not use any device resource requirements from the device.

Specify the **MfCardConfig** entries using the syntax described in [**INF LogConfig Directive**](https://msdn.microsoft.com/library/windows/hardware/ff547448).

For example, consider the following excerpt from a custom INF for a multifunction PC Card device that contains a modem and a network adapter:

```cpp
;...
 
[DDInstall.LogConfigOverride]
LogConfig = DDInstall.Override0
 
[DDInstall.Override0]
IOConfig     =    3F8-3FF                  ; Com1
IOConfig     =    10@100-FFFF%FFF0         ; NIC I/O
IRQConfig    =    3,4,5,7,9,10,11          ; IRQ
MemConfig    =    2000@0-FFFFFFFF%FFFFE000 ; Memory Descriptor 0
MemConfig    =    1000@0-FFFFFFFF%FFFFF000 ; Memory Descriptor 1
MfCardConfig =    1000:47:0(A)
MfCardConfig =    1080:47:1
;...
```

The example shows two **MfCardConfig** entries, one for each function of the device. The first **MfCardConfig** entry contains the following information:

<a href="" id="1000--configregbase-"></a>1000 (*ConfigRegBase*)  
Specifies that there is a set of configuration registers in the attribute memory of the card at offset 0x1000. In this example, the information in these registers describes the modem function on the card.

<a href="" id="47--configoptions-"></a>47 (*ConfigOptions*)  
Specifies the hexadecimal value for the bus driver to program into the configuration option register at the *ConfigRegBase* offset (0x1000).

<a href="" id="0--ioconfigindex-"></a>0 (*IoConfigIndex*)  
Specifies that the I/O resources for this function are listed in the first **IOConfig** entry in this section. An index of zero indicates the first entry, which in this example is "**IOConfig** = 3F8-3FF".

<a href="" id="a--attrs-"></a>A (*attrs*)  
Directs the bus driver to turn on audio enable for this function, which is typical for a modem.

The second **MfCardConfig** entry contains information about the second function on the device (the network adapter, in this example). This entry specifies that there is a second set of configuration registers at offset 0x1080. The bus driver will write the *ConfigOptions* value of 0x47 to the configuration option register for this function. The *IoConfigIndex* value of one directs the bus driver to use the second **IOConfig** entry in this section (**IOConfig** = 10@100-FFFF%FFF0) to program the I/O base and limit registers for this function.

Include more than one *DDInstall*.**Override***N* section in the INF to specify more than one choice of nonsequential I/O port ranges.

If the device uses a memory window that is not based at zero, the *DDInstall*.**Override***N* section(s) must also include a **PcCardConfig** entry. If an override section has both an **MfCardConfig** entry and a **PcCardConfig** entry, the PCMCIA bus driver ignores the *ConfigIndex* value in the **PcCardConfig** entry and just uses the *MemoryCardBaseN* information. See [Supporting PC Cards That Have Incomplete Configuration Registers](supporting-pc-cards-that-have-incomplete-configuration-registers.md) for more information about the **PcCardConfig** entry.

 

 




