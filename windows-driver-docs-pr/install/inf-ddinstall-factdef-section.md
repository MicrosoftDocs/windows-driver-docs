---
title: INF DDInstall.FactDef Section
description: This section should be used in an INF for any manually installed non-PnP device that an end-user might install.
ms.assetid: df2d46da-4e69-4e3c-b208-1ae0a0f771c9
keywords:
- INF DDInstall.FactDef Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DDInstall.FactDef Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF DDInstall.FactDef Section


**Note**  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

This section should be used in an INF for any manually installed non-PnP device that an end-user might install. This section specifies the factory-default hardware configuration settings, such as the bus-relative I/O ports and IRQ (if any), for such a card.

```cpp
[install-section-name.FactDef] |
[install-section-name.nt.FactDef] | 
[install-section-name.ntx86.FactDef] | 
[install-section-name.ntarm.FactDef] |  (Windows 8 and later versions of Windows)
[install-section-name.ntarm64.FactDef] | (Windows 10 version 1709 and later versions of Windows)
[install-section-name.ntia64.FactDef] |  (Windows XP and later versions of Windows)
[install-section-name.ntamd64.FactDef]  (Windows XP and later versions of Windows)
 
ConfigPriority=Priority-Value
[DMAConfig=[DMAattrs:]DMANum]
[IOConfig=io-range]
[MemConfig=mem-range]
[IRQConfig=[IRQattrs:]IRQNum]
... 
```

## Entries


<a href="" id="configpriority-priority-value"></a>**ConfigPriority=**<em>Priority-Value</em>  
Specifies one of the following priority values for this factory-default logical configuration.

| Priority value | Meaning                                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FORCECONFIG    | Specifies a forced configuration, which identifies the resources that the PnP manager must assign to a device.                                                                                            |
| DESIRED        | Provides the highest device performance. The PnP manager can dynamically configure the device with this configuration.                                                                                    |
| NORMAL         | Provides greater device performance than SUBOPTIMAL, but less performance than DESIRED. This is the typical priority value. The PnP manager can dynamically configure the device with this configuration. |
| SUBOPTIMAL     | Provides the lowest device performance. This configuration is not desirable, but it will work. The PnP manager can dynamically configure this configuration.                                              |
| RESTART        | Requires a system restart.                                                                                                                                                                                |
| REBOOT         | Requires a system restart.                                                                                                                                                                                |
| POWEROFF       | Requires a power cycle.                                                                                                                                                                                   |
| HARDRECONFIG   | Requires a jumper change.                                                                                                                                                                                 |
| HARDWIRED      | Cannot be changed.                                                                                                                                                                                        |
| DISABLED       | Indicates that the device is disabled.                                                                                                                                                                    |

 

<a href="" id="dmaconfig--dmaattrs--dmanum"></a>**DMAConfig=**\[<em>DMAattrs</em>**:**\]*DMANum*  
Specifies the bus-relative DMA channel as a decimal number. *DMAattrs* is optional if the device is connected on a bus that has only 8-bit DMA channels and the device uses standard system DMA. Otherwise, it can be one of the letters **D** for 32-bit DMA, **W** for 16-bit DMA, and **N** for 8-bit DMA, with **M** if the device uses bus-master DMA, and with one of the following (mutually exclusive) letters that indicate the type of DMA channel used: **A**, **B**, or **F**. If none of **A**, **B**, or **F** is specified, a standard DMA channel is assumed.

<a href="" id="ioconfig-io-range"></a>**IOConfig=**<em>io-range</em>  
Specifies the I/O port range for the device in the following form:

```cpp
start-end[([decode-mask][:alias-offset][:attr])]
```

<a href="" id="start"></a>*start*  
Specifies the (bus-relative) starting address of the I/O port range as a 64-bit hexadecimal value.

<a href="" id="end-"></a>*end*   
Specifies the ending address of the I/O port range, also as a 64-bit hexadecimal value.

<a href="" id="decode-mask-"></a>*decode-mask*   
Defines the alias type and can be any of the following.

| Mask value | Meaning         | IOR_Alias value |
|------------|-----------------|------------------|
| **3ff**    | 10-bit decode   | 0x04             |
| **fff**    | 12-bit decode   | 0x10             |
| **ffff**   | 16-bit decode   | 0x00             |
| **0**      | Positive decode | 0xFF             |

 

<a href="" id="alias-offset"></a>*alias-offset*  
Not used.

<a href="" id="attr"></a>*attr*  
Specifies the letter **M** if the specified range is in system memory. If omitted, the specified range is in I/O port space.

<a href="" id="memconfig-mem-range"></a>**MemConfig=**<em>mem-range</em>  
Specifies the memory range for the device in the following form:

```cpp
start-end[(attr)]
```

<a href="" id="start"></a>*start*  
Specifies the starting (bus-relative) address of the device memory range as a 64-bit hexadecimal value.

<a href="" id="end-"></a>*end*   
Specifies the ending address of the memory range, also as a 64-bit hexadecimal value.

<a href="" id="attr"></a>*attr*  
Specifies the attributes of the memory range as one or more of the following letters:

-   **R** (read-only)
-   **W** (write-only)
-   **RW** (read/write)
-   **C** (combined write allowed)
-   **H** (cacheable)
-   **F** (prefetchable)
-   **D** (card decode addressing is 32-bit, instead of 24-bit)

If both **R** and **W** are specified or if neither is specified, read/write is assumed.

<a href="" id="irqconfig--irqattrs--irqnum"></a>**IRQConfig=**\[<em>IRQattrs</em>**:**\]*IRQNum*  
Specifies the bus-relative IRQ that the device uses as a decimal number. *IRQattrs* is omitted if the device uses a bus-relative, edge-triggered IRQ. Otherwise, specify **L** to indicate a level-triggered IRQ, and **LS** if the device can share the IRQ line listed in this entry.

Remarks
-------

The specified *DDInstall* section must be referenced in a device-specific entry under the per-manufacturer *Models* section of the INF file. The case-insensitive extensions to the *install-section-name* shown in the formal syntax statement can be inserted into such a <em>DDInstall</em>**.FactDef** section name in cross-operating system and/or cross-platform INF files. For more information about these system-defined extensions, see [Creating an INF File](overview-of-inf-files.md).

This section must contain complete factory-default information for installing one device. The INF should specify this set of entries in the order best suited to how the driver initializes its device. If necessary, it can have more than one of any particular kind of entry.

For example, the INF for a device that used two DMA channels would have two **DMAConfig=** lines in its <em>DDInstall</em>**.FactDef** section.

The INF files of manually installed devices for which the factory-default logical configuration settings can be changed should also use the **LogConfig** directive in their *DDInstall* sections. In general, such an INF should specify the entries in each of its log config sections and in its <em>DDInstall</em>**.FactDef** section in the same order.

Examples
--------

This **IOConfig** entry specifies an I/O port region, 8 bytes in size, which can start at 2F8.

```cpp
IOConfig=2F8-2FF
```

This **MemConfig** entry specifies a memory region of 32K bytes that can start at D0000.

```cpp
MemConfig=D0000-D7FFF
```

## See also


[***DDInstall***](inf-ddinstall-section.md)

[**LogConfig**](inf-logconfig-directive.md)

 

 






