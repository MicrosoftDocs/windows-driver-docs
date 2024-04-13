---
title: INF LogConfig Directive
description: A LogConfig directive references one or more INF-writer-defined sections, each of which specifies a logical configuration of hardware resources.
keywords:
- INF LogConfig Directive Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF LogConfig Directive
api_type:
- NA
ms.date: 07/17/2023
---

# INF LogConfig directive

[!INCLUDE [Caution invalid INF directive](../includes/inf-directive-invalid-22h2.md)]

A **LogConfig** directive references one or more INF-writer-defined sections, each of which specifies a logical configuration of hardware resources − the interrupt request lines, memory ranges, I/O ports, and DMA channels that can be used by the device. Each *log-config-section* specifies an alternative set of bus-relative hardware resources that can be used by the device.

```inf
[DDInstall] | 
[DDInstall.LogConfigOverride] 
  
LogConfig=log-config-section[,log-config-section]...
```

INF files for non-PnP devices use this directive to create basic configurations.

INF files for PnP devices use this directive only to create override configurations.

Each named section referenced by a **LogConfig** directive has the following form:

```inf
[log-config-section]
 
ConfigPriority=priority-value[,config-type]
[DMAConfig=[DMAattrs:]DMANum[,DMANum]...]
[IOConfig=io-range[,io-range]...]
[MemConfig=mem-range[,mem-range]...]
[IRQConfig=[IRQattrs:]IRQNum[,IRQNum]...]
[PcCardConfig=ConfigIndex[:[MemoryCardBase1][:MemoryCardBase2]][(attrs)]]
[MfCardConfig=ConfigRegBase:ConfigOptions[:IoResourceIndex][(attrs)]...]
...
```

## Entries

**ConfigPriority**=*priority-value*  
Specifies the priority value for this logical configuration, as one of the following:

DESIRED  
Soft configured, most optimal.

NORMAL  
Soft configured, less optimal than DESIRED. This is the typical setting.

NORMAL should be specified if the *log-config-section* was defined in a [***DDInstall*.LogConfigOverride**](inf-ddinstall-logconfigoverride-section.md) section, and no *config-type* value can be specified.

SUBOPTIMAL  
Soft configured, less optimal than NORMAL.

HARDRECONFIG  
Requires a jumper change to reconfigure.

HARDWIRED  
Cannot be changed.

RESTART  
Requires restart to take effect.

REBOOT  
This is the same as RESTART.

POWEROFF  
Requires power cycle to take effect.

DISABLED  
Hardware/device is disabled.

**DMAConfig**=\[*DMAattrs:*\]*DMANum*\[**,**DMANum\]...\]  
*DMAattrs* is optional if the device is connected on a bus that has only 8-bit DMA channels and the device uses standard system DMA. Otherwise, it can be one of the following letters:

| Letter | Meaning |
|--|--|
| **D** | 32-bit DMA |
| **W** | 16-bit DMA |
| **N** | 8-bit DMA |

If the device uses bus-master DMA, you must use **M** with one of the following (mutually exclusive) letters that indicates the type of DMA channel used: **A**, **B**, or **F**. If neither **A**, **B**, or **F** are specified, a standard DMA channel is assumed.

*DMANum* specifies one or more bus-relative DMA channels as decimal numbers, each separated from the next by a comma (,).

**IOConfig**=_io-range_\[**,**_io-range_\]...  
Specifies one or more I/O port ranges for the device, in either of the following forms:

*start-end*\[**(**\[*decode-mask*\]\[*:alias-offset*\]\[*:attr*\]**)**\]  (Type 1 I/O range)  

*start*  
Specifies the starting address of the I/O port range as a 64-bit hexadecimal address.

*end*  
Specifies the ending address of the I/O port range, also as a 64-bit hexadecimal address.

*decode-mask*  
Defines the alias type and can be any of the following:

| Mask value | Meaning | IOR_Alias value |
|--|--|--|
| **3ff** | 10-bit decode | 0x04 |
| **fff** | 12-bit decode | 0x10 |
| **ffff** | 16-bit decode | 0x00 |
| **0** | Positive decode | 0xFF |

*alias-offset*  
Not used.

*attr*  
Specifies the letter **M** if the given range is in system memory. If omitted, the given range is in I/O port space.

_size_**@**_min-max_\[**%**_align-mask_\]\[**(**\[*decode-mask*\]\[**:**_alias-offset_\]\[**:**_attr_\])\]  (Type 2 I/O range)  

*size*  
Specifies the number of bytes required for the I/O port range as a 32-bit hexadecimal value.

*min*  
Specifies the lowest possible starting address of the I/O port range as a 64-bit hexadecimal address.

*max*  
Specifies the highest possible ending address of the I/O port range as a 64-bit hexadecimal address.

*align-mask*  
Optionally specifies a 64-bitmask that is used in a bitwise AND operation to align the start of the I/O port range on an integral (usually 32-bit or 64-bit) address boundary.

*decode-mask*  
Defines the alias type and can be any of the following:

| Mask value | Meaning | IOR_Alias value |
|--|--|--|
| **3ff** | 10-bit decode | 0x04 |
| **fff** | 12-bit decode | 0x10 |
| **ffff** | 16-bit decode | 0x00 |
| **0** | Positive decode | 0xFF |

*alias-offset*  
Not used.

*attr*  
Specifies the letter **M** if the given range is in system memory. If omitted, the given range is in I/O port space.

**MemConfig**=_mem-range_\[**,**_mem-range_\]...  
Specifies one or more memory ranges for the device in one of the following forms:

```inf
start-end[(attr)] | size@min-max[%align-mask][(attr)]
```

*start*  
Specifies the starting (bus-relative) physical address of the device memory range as a 64-bit hexadecimal value.

*end*  
Specifies the ending physical address of the memory range, also as a 64-bit hexadecimal value.

*attr*  
Specifies the attributes of the memory range as one or more of the following letters:

| Letter | Meaning |
|--|--|
| **R** | Read-only |
| **W** | Write-only |
| **RW** | Read/write |
| **C** | Combined write allowed |
| **H** | Cacheable |
| **F** | Prefetchable |
| **D** | Card decode addressing is 32-bit, instead of 24-bit |

If both **R** and **W** are specified or if neither is specified, read/write is assumed.

*size*  
Specifies the number of bytes required in the memory range as a 32-bit hexadecimal value.

*min*  
Specifies the lowest possible starting address of the device memory range as a 64-bit hexadecimal value.

*max*  
Specifies the highest possible ending address of the memory range as a 64-bit hexadecimal value.

*align-mask*  
Optionally specifies a 64-bitmask that is used in a bitwise AND operation to align the start of the device memory range on an integral (usually 64-bit) address boundary.

If align-mask is omitted, the default memory alignment is on a 4K boundary (FFFFF000).

**IRQConfig**=\[*IRQattrs:*\]*IRQNum*\[**,**_IRQNum_\]...  
*IRQattrs* is omitted if the device uses a bus-relative, edge-triggered IRQ. Otherwise, specify **L** to indicate a level-triggered IRQ and **LS** if the device can share the IRQ lines listed in this entry.

*IRQNum* specifies one or more bus-relative IRQs the device can use as decimal numbers, each separated from the next by a comma (,).

**PcCardConfig**=_ConfigIndex_\[**:**\[*MemoryCardBase1*\]\[**:**_MemoryCardBase2_\]\]\[**(**_attrs_**)**\]  
Configures CardBus registers and/or creates up to two permanent memory windows that map to the attribute space of the device. A driver can use the memory windows to access the attribute space from an ISR. Specify all numeric values in hexadecimal format.

The elements of a **PcCardConfig** entry are as follows:

*ConfigIndex*  
Specifies the 8-bit PCMCIA configuration index for a device on a PCMCIA bus.

*MemoryCardBase1*  
Optionally specifies a 32-bit base address for a first memory window.

*MemoryCardBase2*  
Optionally specifies a 32-bit base address for a second memory window.

*attrs*  
Optionally specifies one or more attributes for the device, separated by spaces. An invalid attribute specifier invalidates the whole **PcCardConfig** entry. If more than one specifier for a particular attribute is provided, the attributes are applied to individual I/O or memory windows for the device. If only one specifier is provided, then that attribute is applied to all windows (see the following example).

Specifically, if multiple specifiers are provided, the first specifier found reading from left to right will be applied to the first window, and the next specifier applied to the second window. A maximum of two I/O windows and two memory windows may be controlled by a single **PcCardConfig** entry. If the device has more than two memory windows, then a second **PcCardConfig** entry must be included.

The attributes include:

| Attribute | Description |
|--|--|
| **W** | 16-bit I/O data path.<br><br>The default is 8-bit if the INF specifies a **LogConfig** directive. If no **LogConfig** directive is specified, the driver uses 16-bit I/O. |
| **S**_n_ | ~IOCS16 source.<br><br>If _n_ is 0, ~IOCS16 is based on the value of the datasize bit. If n is 1, ~IOCS16 is based on the ~IOIS16 signal from the device. The default is **S**1. |
| **Z**_n_ | I/O 8-bit, zero wait state.<br><br>If _n_ is 1, 8-bit I/O accesses occur with zero additional wait states. If _n_ is 0, access occurs with additional wait states. This flag has no meaning for 16-bit I/O. The default is **Z**0. |
| **Xl**_n_ | I/O wait states.<br><br>If n is 1, 16-bit system accesses occur with one additional wait state. The default is **Xl**1. |
| **M** | 16-bit memory data path. The default is 8-bit. |
| **M8** | 8-bit memory data path. |
| **XM**_n_ | Memory wait states, where n can be 0, 1, 2 or 3.<br><br>This value determines the number of additional wait states for 16-bit accesses to a memory window. The default is **XM**3. |
| **A** | Memory range to be mapped as Attribute memory. |
| **C** | Memory range to be mapped as Common Memory (default). |

For example, an attrs value of (WB CA M XM1 XI0) translates to the following:

```console
1st I/O window is 16-bit

2nd I/O window 8-bit

1st memory window is common

2nd memory window is attribute

Memory is 16-bit

One wait state on memory windows

Zero wait states on I/O windows
```

**MfCardConfig**=_ConfigRegBase_**:**_ConfigOptions_\[**:**_IoResourceIndex_\]\[**(**_attrs_**)**\]...  
Specifies the attribute-memory location of the set of configuration registers for one function of a multifunction device, as follows:

*ConfigRegBase*  
Specifies the attribute offset of the configuration registers for this function of the multifunction device.

*ConfigOptions*  
Specifies the 8-bit PCMCIA configuration option register.

*IoResourceIndex*  
Specifies the index to the **IOConfig** entry for the bus driver to use in programming the configuration I/O base and limit registers. This index is zero-based, that is, zero designates the initial **IOConfig** entry in this *log-config-section*.

*attrs*  
If set to the letter **A**, directs the PCMCIA bus driver to turn on audio enable in the configuration and status registers.

Each **MfCardConfig** entry supplies information about a single function of the multifunction device. When a set of **LogConfig** directives each reference a discrete *log-config-section* in the INF's [***DDInstall*.LogConfigOverride**](inf-ddinstall-logconfigoverride-section.md) section, each *log-config-section* must have its entries, including **MfCardConfig** entries, listed in the same order.

## Remarks

A **LogConfig** directive can be specified under any per-manufacturer, per-models [**INF *DDInstall* section**](inf-ddinstall-section.md) or [**INF *DDInstall*.LogConfigOverride section**](inf-ddinstall-logconfigoverride-section.md).

An INF for a non-PnP device that supports several alternative logical configurations typically defines a set of *log-config-sections* under a *DDInstall* section. Each *log-config-section* specifies a discrete set of logical configuration resources. It also includes a **ConfigPriority** entry, which ranks each logical configuration according to its effects on device and driver performance, ease of initialization, and so forth.

For PnP devices, the PnP manager assigns a set of logical hardware resources to each PnP device. That is, the PnP manager queries the system bus drivers, receives their reports of per-device I/O bus configuration resources in use, and assigns per-device sets of logical hardware resources to achieve the best system-wide balance in the usage of all such resources.

As a result, the **LogConfig** directive under a *DDInstall* section is ignored for PnP devices,. To override the resources reported by the bus for a PnP device, include the **LogConfig** directive under a [***DDInstall*.LogConfigOverride**](inf-ddinstall-logconfigoverride-section.md) section. In this case, the resources specified in the *log-config-section* is used instead of those reported by the bus.

Platform extensions can be added to a *DDInstall* section that contains a **LogConfig** directive, or to a [***DDInstall*.LogConfigOverride**](inf-ddinstall-logconfigoverride-section.md) section, to specify platform-specific or OS-specific logical configurations. For more information, see [Creating an INF File](overview-of-inf-files.md).

A given *log-config-section* name must be unique to the INF file, but it can be referenced by **LogConfig** directives in other INF *DDInstall* sections for the same devices. Each INF-writer-created section name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

Only one **ConfigPriority** entry can be used in each *log-config-section*. There can be more than one of each of the other entries, depending on the hardware resource requirements of the device.

One or more **MfCardConfig=** entries can appear only in a *log-config-section* that is referenced by a **LogConfig** directive in the _DDInstall_**.LogConfigOverride** section of an INF for a multifunction device. For more information about INF files for multifunction devices, see [Supporting Multifunction Devices](../multifunction/index.md).

### LogConfig-Referenced Section Entries and Values

From a *log-config-section*, the system installer builds binary logical configuration records and stores them in the registry.

An INF file can contain any number of per-device *log-config-sections*. However, each such section must contain complete information for installing one device. In general, the INF should specify the entries in each of its *log-config-sections* in the same order. The INF should specify each set of entries in the order best suited to how the driver initializes its device.

If more than one *log-config-section* is present for a given device, only one of these INF sections is used during installation. Such an INF file partially controls which such section is used with the **ConfigPriority** value that it supplies in each such *log-config-section*. That is, the system installers attempt to honor any configuration priorities in an INF file, but might select a lower ranked logical configuration if a conflict with an already installed device is found.

During installation, one and only one resource from each entry in a given *log-config-section* is selected and assigned to a particular device. If a particular device needs more than one resource of the same type, a set of entries of that type must be used in its *log-config-sections*.

For example, to ensure two I/O port ranges for a particular device, two **IOConfig=** entries must be specified in the *log-config-section* for that device. On the other hand, if a device requires no IRQ, its INF can omit the **IRQConfig** entry from the *log-config-sections*.

## Examples

This example shows some valid **PcCardConfig** entries for a PCMCIA device.

```inf
PcCardConfig=0:E0000:F0000(W)
PcCardConfig=0:E0000(M)
PcCardConfig=0::(W)
PcCardConfig=0(W)
```

This example shows a Type 1 I/O range specification in an **IOConfig** entry. It specifies an I/O port region, eight bytes in size, which can start at 1F8, 2F8, or 3F8.

```inf
IOConfig=1F8-1FF, 2F8-2FF, 3F8-3FF
```

By contrast, this example shows a Type 2 I/O range specification in an **IOConfig** entry. It specifies an I/O port region, eight bytes in size, which can start at 300, 308, 310, 318, 320, or 328.

```inf
IOConfig=8@300-32F%FF8
```

This example shows a set of **IOConfig** entries for a four-port device, each specifying an I/O port range that is offset by 0x400 bytes from the next.

```inf
IoConfig=0x200-0x21f
IoConfig=0x600-0x61f
IoConfig=0xA00-0xA1f
IoConfig=0xE00-0xE1f
```

The next two examples show typical **MemConfig** entries.

This example specifies a memory region of 32K bytes that can start at either C0000 or D0000.

```inf
MemConfig=C0000-C7FFF, D0000-D7FFF
```

This example specifies a memory region of 32k bytes starting on 64K boundaries.

```inf
MemConfig=8000@C0000-D7FFF%F0000
```

This example shows how the system HDC class INF file sets up several *log-config-sections* for generic ESDI hard disk controllers and uses a [***DDInstall*.LogConfigOverride**](inf-ddinstall-logconfigoverride-section.md) section for a particular IDE controller.

```inf
[MS_HDC] ; per-manufacturer Models section
%FujitsuIdePccard.DeviceDesc% = 
          atapi_fujitsu_Inst, PCMCIA\FUJITSU-IDE-PC_CARD-DDF2
%*PNP0600.DeviceDesc% = atapi_Inst, *PNP0600 ; generic ESDI HDCs

; ... other manufacturers' Models sections omitted

[atapi_Inst]
CopyFiles = @atapi.sys
LogConfig = esdilc1, esdilc2, esdilc3, esdilc4

; ... [atapi_Inst.Services] + service/EventLog-install omitted here

[esdilc1]
ConfigPriority=HARDWIRED
IOConfig=1f0-1f7(3ff::)
IoConfig=3f6-3f6(3ff::)
IRQConfig=14

[esdilc2]
ConfigPriority=HARDWIRED
IOConfig=170-177(3ff::)
IoConfig=376-376(3ff::)
IRQConfig=15

[esdilc3]
ConfigPriority=HARDWIRED
IOConfig=1e8-1ef(3ff::)
IoConfig=3ee-3ee(3ff::)
IRQConfig=11

[esdilc4]
; ...

[atapi_fujitsu_Inst.LogConfigOverride]
LogConfig = fujitsu.LogConfig0

[fujitsu.LogConfig0]
ConfigPriority=NORMAL
IOConfig=10@100-400%fff0
IRQConfig=14,15,5,7,9,11,12,3
PcCardConfig=1:0:0(W)
```

For some examples of how **MfCardConfig** entries are used, see [Supporting PC Cards That Have Incomplete Configuration Register Addresses](../multifunction/supporting-pc-cards-that-have-incomplete-configuration-register-addres.md).

## See also

[***DDInstall***](inf-ddinstall-section.md)

[***DDInstall*.FactDef**](inf-ddinstall-factdef-section.md)
