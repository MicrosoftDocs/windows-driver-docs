---
title: XPSDrv Installation
description: XPSDrv Installation
keywords:
- XPSDrv printer drivers WDK , installing
- INF files WDK print , XPSDrv printer drivers
ms.date: 05/08/2023
---

# XPSDrv Installation

[!include[Print Support Apps](../includes/print-support-apps.md)]

To be properly installed by the spooler, XPSDrv drivers must include the following:

- The [**CopyFiles**](../install/inf-copyfiles-directive.md) directive of the driver INF file must reference the [filter pipeline configuration file](filter-pipeline-configuration-file.md).

- The Needs directive must reference Xpsdrv.oem. For more information about the Needs directive, see [**INF DDInstall Section**](../install/inf-ddinstall-section.md).

- If the configuration module is based on Unidrv, the Needs directive must reference Unidrv.oem and Xpsgpd.oem. Likewise, if the XPSDrv driver configuration module is based on PScript5, the Needs directive must reference Pscript.oem and Xpsppd.oem.

The following code example illustrates an INF file with the preceding changes.

```inf
[Version]
Signature="$Windows NT$"
Provider=%MS%
Class=Printer
ClassGUID={4D36E979-E325-11CE-BFC1-08002BE10318}
CatalogFile=ntprint.cat
DriverVer=10/11/2005,6.0.5242.0
PnpLockdown=1

[Manufacturer]
%MS% = Microsoft,NTamd64

[Microsoft.NTamd64]
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
