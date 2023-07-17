---
title: INF DDInstall.LogConfigOverride section
description: DDInstall.LogConfigOverride sections are used to create an override configuration to override hardware resource requirements.
keywords:
- INF DDInstall.LogConfigOverride Section Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF DDInstall.LogConfigOverride Section
api_type:
- NA
ms.date: 06/02/2022
---

# INF DDInstall.LogConfigOverride section

> [!CAUTION]
> Starting with Windows 11 version 22H2, a driver package using this section will no longer be able to receive a signature from Hardware Developer Center.
 
> [!CAUTION]
> If you are building a universal or Windows Driver package, this section is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md) and [Getting Started with Windows Drivers](../develop/getting-started-with-windows-drivers.md).

_DDInstall_.**LogConfigOverride** sections are used to create an [override configuration](../kernel/hardware-resources.md#logical-configuration-types-for-resource-requirements-lists), which overrides the hardware resource requirements that a Plug and Play device's bus driver reports.

```inf
[install-section-name.LogConfigOverride] |
[install-section-name.nt.LogConfigOverride] |
[install-section-name.ntx86.LogConfigOverride] |
[install-section-name.ntia64.LogConfigOverride] | (Windows XP and later versions of Windows)
[install-section-name.ntamd64.LogConfigOverride] | (Windows XP and later versions of Windows)
[install-section-name.ntarm.LogConfigOverride] | (Windows 8 and later versions of Windows)
[install-section-name.ntarm64.LogConfigOverride] (Windows 10 version 1709 and later versions of Windows)
 
LogConfig=log-config-section[,log-config-section]...] 
```

## Entries

The section entries and values that are used with _DDInstall_.**LogConfigOverride** sections are specified within *log-config-section*s referenced by [**INF LogConfig directives**](inf-logconfig-directive.md).

## Remarks

The configuration data that is specified in a _log-config-section_ for a Plug and Play device is a preferred hardware resource configuration, but is not an absolute requirement. Some or all of the specified hardware resource configuration data might not be accepted by the device's underlying bus driver. In this situation, the device driver is assigned the hardware resources that were originally reported by the bus driver.

## Examples

The following example shows a _DDInstall_.**LogConfigOverride** section and a corresponding _log-config-section_ for a PCMCIA device.

```inf
[XYZDevice.LogConfigOverride]
LogConfig = XYZDevice.Override0

[XYZDevice.Override0]
IOConfig=2f8-2ff
IOConfig=20@100-FFFF%FFE0
IRQConfig=3,4,5,7,9,10,11
MemConfig=4000@0-FFFFFFFF%FFFFC000
PcCardConfig=41:100000(W)
```

For more information about the hardware resource configuration data values that are specified in a _log-config-section_, see [**INF LogConfig Directive**](inf-logconfig-directive.md).

## See also

[**_DDInstall_**](inf-ddinstall-section.md)
