---
title: INF DDInstall.FactDef section
description: This section should be used in an INF for any manually installed non-PnP device that an end-user might install.
keywords:
- INF DDInstall.FactDef Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DDInstall.FactDef Section
api_type:
- NA
ms.date: 06/01/2022
---

# INF DDInstall.FactDef section

> [!NOTE]
> If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

This section should be used in an INF for any manually installed non-PnP device that an end-user might install. This section specifies the factory-default hardware configuration settings, such as the bus-relative I/O ports and IRQ (if any), for such a card.

```inf
[install-section-name.FactDef] |
[install-section-name.nt.FactDef] | 
[install-section-name.ntx86.FactDef] | 
[install-section-name.ntia64.FactDef] | (Windows XP and later versions of Windows)
[install-section-name.ntamd64.FactDef] | (Windows XP and later versions of Windows)
[install-section-name.ntarm.FactDef] | (Windows 8 and later versions of Windows)
[install-section-name.ntarm64.FactDef] (Windows 10 version 1709 and later versions of Windows)
 
ConfigPriority=Priority-Value
[DMAConfig=[DMAattrs:]DMANum]
[IOConfig=io-range]
[MemConfig=mem-range]
[IRQConfig=[IRQattrs:]IRQNum]
```

## Entries

**ConfigPriority=**_Priority-Value_  
Specifies one of the following priority values for this factory-default logical configuration.

| Priority value | Meaning |
|--|--|
| FORCECONFIG | Specifies a forced configuration, which identifies the resources that the PnP manager must assign to a device. |
| DESIRED | Provides the highest device performance. The PnP manager can dynamically configure the device with this configuration. |
| NORMAL | Provides greater device performance than SUBOPTIMAL, but less performance than DESIRED. This is the typical priority value. The PnP manager can dynamically configure the device with this configuration. |
| SUBOPTIMAL | Provides the lowest device performance. This configuration is not desirable, but it will work. The PnP manager can dynamically configure this configuration. |
| RESTART | Requires a system restart. |
| REBOOT | Requires a system restart. |
| POWEROFF | Requires a power cycle. |
| HARDRECONFIG | Requires a jumper change. |
| HARDWIRED | Cannot be changed. |
| DISABLED | Indicates that the device is disabled. |

**DMAConfig=**[_DMAattrs_**:**]_DMANum_  
Specifies the bus-relative DMA channel as a decimal number. _DMAattrs_ is optional if the device is connected on a bus that has only 8-bit DMA channels and the device uses standard system DMA. Otherwise, it can be one of the letters **D** for 32-bit DMA, **W** for 16-bit DMA, and **N** for 8-bit DMA, with **M** if the device uses bus-master DMA, and with one of the following (mutually exclusive) letters that indicate the type of DMA channel used: **A**, **B**, or **F**. If none of **A**, **B**, or **F** is specified, a standard DMA channel is assumed.

**IOConfig=**_io-range_  
Specifies the I/O port range for the device in the following form:

```inf
start-end[([decode-mask][:alias-offset][:attr])]
```

_start_
Specifies the (bus-relative) starting address of the I/O port range as a 64-bit hexadecimal value.

_end_
Specifies the ending address of the I/O port range, also as a 64-bit hexadecimal value.

_decode-mask_
Defines the alias type and can be any of the following.

| Mask value | Meaning | IOR_Alias value |
|--|--|--|
| **3ff** | 10-bit decode | 0x04 |
| **fff** | 12-bit decode | 0x10 |
| **ffff** | 16-bit decode | 0x00 |
| **0** | Positive decode | 0xFF |

_alias-offset_  
Not used.

_attr_  
Specifies the letter **M** if the specified range is in system memory. If omitted, the specified range is in I/O port space.

**MemConfig=**_mem-range_  
Specifies the memory range for the device in the following form:

```inf
start-end[(attr)]
```

_start_
Specifies the starting (bus-relative) address of the device memory range as a 64-bit hexadecimal value.

_end_
Specifies the ending address of the memory range, also as a 64-bit hexadecimal value.

_attr_  
Specifies the attributes of the memory range as one or more of the following letters:

- **R** (read-only)
- **W** (write-only)
- **RW** (read/write)
- **C** (combined write allowed)
- **H** (cacheable)
- **F** (prefetchable)
- **D** (card decode addressing is 32-bit, instead of 24-bit)

If both **R** and **W** are specified or if neither is specified, read/write is assumed.

**IRQConfig=**[_IRQattrs_**:**]_IRQNum_  
Specifies the bus-relative IRQ that the device uses as a decimal number. _IRQattrs_ is omitted if the device uses a bus-relative, edge-triggered IRQ. Otherwise, specify **L** to indicate a level-triggered IRQ, and **LS** if the device can share the IRQ line listed in this entry.

## Remarks

The specified _DDInstall_ section must be referenced in a device-specific entry under the per-manufacturer _Models_ section of the INF file. The case-insensitive extensions to the _install-section-name_ shown in the formal syntax statement can be inserted into such a _DDInstall_**.FactDef** section name in cross-operating system and/or cross-platform INF files. For more information about these system-defined extensions, see [Creating an INF File](overview-of-inf-files.md).

This section must contain complete factory-default information for installing one device. The INF should specify this set of entries in the order best suited to how the driver initializes its device. If necessary, it can have more than one of any particular kind of entry.

For example, the INF for a device that used two DMA channels would have two **DMAConfig=** lines in its _DDInstall_.**FactDef** section.

The INF files of manually installed devices for which the factory-default logical configuration settings can be changed should also use the **LogConfig** directive in their _DDInstall_ sections. In general, such an INF should specify the entries in each of its log config sections and in its _DDInstall_**.FactDef** section in the same order.

## Examples

This **IOConfig** entry specifies an I/O port region, 8 bytes in size, which can start at 2F8.

```inf
IOConfig=2F8-2FF
```

This **MemConfig** entry specifies a memory region of 32K bytes that can start at D0000.

```inf
MemConfig=D0000-D7FFF
```

## See also

[**_DDInstall_**](inf-ddinstall-section.md)

[**LogConfig**](inf-logconfig-directive.md)
