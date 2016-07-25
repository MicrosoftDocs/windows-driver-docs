---
title: INF DDInstall.LogConfigOverride Section
description: DDInstall.LogConfigOverride sections are used to create an override configuration, which overrides the hardware resource requirements that a Plug and Play device's bus driver reports.
ms.assetid: 7ee8d221-7cdb-4373-aa8b-2d5164f6a636
keywords: ["INF DDInstall.LogConfigOverride Section Device and Driver Installation"]
topic_type:
- apiref
api_name:
- INF DDInstall.LogConfigOverride Section
api_type:
- NA
---

# INF DDInstall.LogConfigOverride Section


**Note**  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).

 

*DDInstall***.LogConfigOverride** sections are used to create an [override configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#logical-configuration-types-for-resource-requirements-lists), which overrides the hardware resource requirements that a Plug and Play device's bus driver reports.

``` syntax
[install-section-name.LogConfigOverride] |
[install-section-name.nt.LogConfigOverride] |
[install-section-name.ntx86.LogConfigOverride] |
[install-section-name.ntia64.LogConfigOverride] |  (Windows XP and later versions of Windows)
[install-section-name.ntamd64.LogConfigOverride]  (Windows XP and later versions of Windows)
 
LogConfig=log-config-section[,log-config-section]...] 
```

## Entries


The section entries and values that are used with *DDInstall***.LogConfigOverride** sections are specified within *log-config-sections* referenced by [**INF LogConfig directives**](inf-logconfig-directive.md).

Remarks
-------

The configuration data that is specified in a *log-config-section* for a Plug and Play device is a preferred hardware resource configuration, but is not an absolute requirement. Some or all of the specified hardware resource configuration data might not be accepted by the device's underlying bus driver. In this situation, the device driver is assigned the hardware resources that were originally reported by the bus driver.

Examples
--------

The following example shows a *DDInstall***.LogConfigOverride** section and a corresponding *log-config-section* for a PCMCIA device.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20INF%20DDInstall.LogConfigOverride%20Section%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





