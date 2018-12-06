---
title: XPSDrv Installation
description: XPSDrv Installation
ms.assetid: 0b5ef114-2862-46f9-bd32-ae09fa4e6a92
keywords:
- XPSDrv printer drivers WDK , installing
- INF files WDK print , XPSDrv printer drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# XPSDrv Installation


To be properly installed by the spooler, XPSDrv drivers must include the following:

-   The [**CopyFiles**](https://msdn.microsoft.com/library/windows/hardware/ff546346) directive of the driver INF file must reference the [filter pipeline configuration file](filter-pipeline-configuration-file.md).

-   The Needs directive must reference Xpsdrv.oem. For more information about the Needs directive, see [**INF DDInstall Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) and [Source Media for INFs](https://msdn.microsoft.com/library/windows/hardware/ff552302).

-   If the configuration module is based on Unidrv, the Needs directive must reference Unidrv.oem and Xpsgpd.oem. Likewise, if the XPSDrv driver configuration module is based on PScript5, the Needs directive must reference Pscript.oem and Xpsppd.oem.

The following code example illustrates an INF file with the preceding changes.

```cpp
[Version]
Signature="$Windows NT$"
Provider=%MS%
ClassGUID={4D36E979-E325-11CE-BFC1-08002BE10318}
Class=Printer
CatalogFile=ntprint.cat
DriverVer=10/11/2005,6.0.5242.0

[Manufacturer]
Microsoft

[Microsoft]
"XPSDrv Sample Driver" = INSTALL_XDSMPL_FILTERS

[INSTALL_XDSMPL_FILTERS]
CopyFiles=XPSDrvSample,ConfigPlugin,COLORPROFILES
DriverFile=mxdwdrv.dll
ConfigFile=unidrvui.dll
HelpFile=unidrv.HLP 
DataFile=XDSmpl.GPD
Include=NTPRINT.INF
Needs=UNIDRV.OEM, XPSGPD.OEM, XPSDRV.OEM
ICMProfiles=xdwscRGB.cdmp

[XPSDrvSample]
xdsmpl-pipelineconfig.xml
...
```

 

 




