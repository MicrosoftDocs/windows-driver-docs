---
title: XPSDrv Installation
author: windows-driver-content
description: XPSDrv Installation
ms.assetid: 0b5ef114-2862-46f9-bd32-ae09fa4e6a92
keywords:
- XPSDrv printer drivers WDK , installing
- INF files WDK print , XPSDrv printer drivers
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# XPSDrv Installation


To be properly installed by the spooler, XPSDrv drivers must include the following:

-   The [**CopyFiles**](https://msdn.microsoft.com/library/windows/hardware/ff546346) directive of the driver INF file must reference the [filter pipeline configuration file](filter-pipeline-configuration-file.md).

-   The Needs directive must reference Xpsdrv.oem. For more information about the Needs directive, see [**INF DDInstall Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) and [Source Media for INFs](https://msdn.microsoft.com/library/windows/hardware/ff552302).

-   If the configuration module is based on Unidrv, the Needs directive must reference Unidrv.oem and Xpsgpd.oem. Likewise, if the XPSDrv driver configuration module is based on PScript5, the Needs directive must reference Pscript.oem and Xpsppd.oem.

The following code example illustrates an INF file with the preceding changes.

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20XPSDrv%20Installation%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


