---
title: Constructing a Package-Aware Driver with Updated Core Drivers
description: Constructing a Package-Aware Driver with Updated Core Drivers
ms.assetid: 801ac83c-a04a-4a3f-81a9-24010a390ee5
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




