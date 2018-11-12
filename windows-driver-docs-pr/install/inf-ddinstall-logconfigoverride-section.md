---
title: INF DDInstall.LogConfigOverride Section
description: DDInstall.LogConfigOverride sections are used to create an override configuration to override hardware resource requirements.
ms.assetid: 7ee8d221-7cdb-4373-aa8b-2d5164f6a636
keywords:
- INF DDInstall.LogConfigOverride Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DDInstall.LogConfigOverride Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF DDInstall.LogConfigOverride Section


**Note**  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

<em>DDInstall</em>**.LogConfigOverride** sections are used to create an [override configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#logical-configuration-types-for-resource-requirements-lists), which overrides the hardware resource requirements that a Plug and Play device's bus driver reports.

```cpp
[install-section-name.LogConfigOverride] |
[install-section-name.nt.LogConfigOverride] |
[install-section-name.ntx86.LogConfigOverride] |
[install-section-name.ntarm.LogConfigOverride] | (Windows 8 and later versions of Windows)
[install-section-name.ntarm64.LogConfigOverride] | (Windows 10 version 1709 and later versions of Windows)
[install-section-name.ntia64.LogConfigOverride] |  (Windows XP and later versions of Windows)
[install-section-name.ntamd64.LogConfigOverride]  (Windows XP and later versions of Windows)
 
LogConfig=log-config-section[,log-config-section]...] 
```

## Entries


The section entries and values that are used with <em>DDInstall</em>**.LogConfigOverride** sections are specified within *log-config-sections* referenced by [**INF LogConfig directives**](inf-logconfig-directive.md).

Remarks
-------

The configuration data that is specified in a *log-config-section* for a Plug and Play device is a preferred hardware resource configuration, but is not an absolute requirement. Some or all of the specified hardware resource configuration data might not be accepted by the device's underlying bus driver. In this situation, the device driver is assigned the hardware resources that were originally reported by the bus driver.

Examples
--------

The following example shows a <em>DDInstall</em>**.LogConfigOverride** section and a corresponding *log-config-section* for a PCMCIA device.

```cpp
[XYZDevice.LogConfigOverride]
LogConfig = XYZDevice.Override0

[XYZDevice.Override0]
IOConfig=2f8-2ff
IOConfig=20@100-FFFF%FFE0
IRQConfig=3,4,5,7,9,10,11
MemConfig=4000@0-FFFFFFFF%FFFFC000
PcCardConfig=41:100000(W)
```

For more information about the hardware resource configuration data values that are specified in a *log-config-section*, see [**INF LogConfig Directive**](inf-logconfig-directive.md).

## See also


[***DDInstall***](inf-ddinstall-section.md)

 

 






