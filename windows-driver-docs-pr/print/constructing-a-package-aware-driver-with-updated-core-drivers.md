---
title: Constructing a Package-Aware Driver with Updated Core Drivers
author: windows-driver-content
description: Constructing a Package-Aware Driver with Updated Core Drivers
ms.assetid: 801ac83c-a04a-4a3f-81a9-24010a390ee5
---

# Constructing a Package-Aware Driver with Updated Core Drivers


A package-aware driver ensures that all of the driver components in your package are configured for use during a point-and-print operation. Point and print enables a Windows user to create a connection to a remote printer without providing disks or other installation media. Instead, the print server automatically downloads the print driver package to the client. For more information, see [Point and Print with Driver Packages](point-and-print-with-driver-packages.md).

### Including Updated Core Drivers

The initial Windows Vista release includes only one core driver package. That package contains Ntprint.inf and the XPSDrv, UniDrv, and PostScript core driver components. The core driver package will be updated periodically and made available in major Windows releases, in service packs, and in quick-fix engineering (QFE) packages distributed by Windows Sustained Engineering (SE). This package is typically distributed as a Microsoft standalone update (MSU) package, which must be installed by the Windows MSU installer (Wusa.exe) - not by the PnP installer. For a description of the process for extracting the core driver package from the MSU for use in PnP installs, see [Get the Updated Core Driver Package](getting-the-updated-core-driver-package.md).

In addition, updated core driver packages will be posted on the Microsoft [Connect](http://go.microsoft.com/fwlink/p/?linkid=133880) Web site after major Windows releases and service pack releases, and, from there, they will be available to anyone for redistribution. Typically, the availability of these drivers lags major Windows updates by four to six weeks. The redistribution agreements for using these driver packages will be available from the Microsoft Connect Web site during the process of obtaining the driver package. If a QFE package is available for the core print drivers, you can obtain the QFE package directly from Windows SE and avoid the publishing delay to the Microsoft Connect Web site. You must request the QFE package through your Microsoft technical account manager (TAM), who will require you to sign an additional redistribution agreement. The QFE packages from Windows SE will be identical to those posted on the Microsoft Connect Web site.

If your package-aware driver package must use a version of the core driver package that is newer than the version in the initial Windows Vista release, then you must distribute the required core driver package with your package-aware driver. Note that Windows Vista provides no mechanism to resolve your driver's core driver dependency if the required core driver package is not already in the driver store. In addition, the Plug and Play (PnP) manager provides no information to help the printer installer to determine whether a required core driver package is available before the installation begins. If the required core driver package is not in the driver store, the installation will fail. Thus, if a manufacturer releases a package-aware driver package that requires an updated version of the core driver package, the release must include the required core driver package to ensure that installation succeeds.

**Note**   If possible, avoid making your package-aware driver package dependent on a system-supplied core driver package that is newer than the initial Windows Vista release. Otherwise, you must take additional steps to ensure that your driver package installs properly on Windows Vista releases with older versions of the core driver package.

 

Localized help content is included in the core driver package, but this content will not be updated after the initial Windows Vista release. When selecting a language for a driver package, use the language that is the most likely to be understood by those installing the package. Typically, a manufacturer who wants to ship a single package to cover multiple languages should use English. The choice of a language for the driver package will not impact the localized help content already available on client machines.

The MSU files are specific to the processor architecture (IA64, x86, and x64). Be sure to choose the appropriate architecture for your driver. As an option, you can supply a multi-architecture driver package that bundles together binary driver files for two or more architectures with a common INF file. If you supply a multi-architecture driver package, your release should include a separate core driver package for each architecture supported.

This section discusses the following topics:

[Getting the Updated Core Driver Package](getting-the-updated-core-driver-package.md)

[Bundling the Core Driver with Your Package-Aware Driver](bundling-the-core-driver-with-your-package-aware-driver.md)

[Updating Your Package-Aware Driver's INF](updating-your-package-aware-driver-s-inf.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Constructing%20a%20Package-Aware%20Driver%20with%20Updated%20Core%20Drivers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


