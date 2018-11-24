---
title: Components and Files Used for Network Component Installation
description: Components and Files Used for Network Component Installation
ms.assetid: be056ff1-0b92-4e81-a506-7750012aad4e
keywords:
- installing network components WDK , components and files used
- network component installations WDK , components and files used
- components WDK network installations
- class installers WDK networking
- co-installers WDK networking
- network migration DLL WDK
- text-mode setup WDK networking
- driver image files WDK networking
- driver library files WDK networking
- migration DLL WDK networking
- vendor-supplied installation files WDK networking
- files WDK network component installs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Components and Files Used for Network Component Installation





The following components and files are used to install network drivers:

-   A required class installer and optional co-installer

-   One or more information (INF) files

-   An optional notify object

In addition to one or more of the above components, a vendor also supplies the following files:

-   One or more device driver image (.sys) files and driver library (.dll) files

-   An optional driver catalog file

-   An optional text-mode setup information file (txtsetup.oem)

### Class installer and co-installer

Network components are installed by the network class installer or by a custom class installer created by the vendor. A *class installer* is a dynamic-link library (DLL) that installs, configures, or removes devices of a particular class in the system. For more information about class installers, see [Writing Class Installers and Co-Installers](https://msdn.microsoft.com/library/windows/hardware/ff819060).

If the network class installer does not provide all the features that a vendor requires, a vendor can customize the installation process by writing a device *co-installer*. A *co-installer* is a Win32 DLL that assists in device installation. Co-installers are called by the system Device Installer as "helpers" or filters for Class Installers. For more information about co-installers, see [Writing a Co-installer](https://msdn.microsoft.com/library/windows/hardware/ff554011).

### INF files

Each network component must have an information (INF) file that the network class installer uses to install the component. Network INF files are based on the common INF file format. For more information about the INF file format, see [INF File Sections and Directives](https://msdn.microsoft.com/library/windows/hardware/ff547433).

For detailed information about creating INF files for network components, see [Creating Network INF Files](creating-network-inf-files.md).

### Notify object

A software component, such as a network protocol, client, or service, can have a *notify object*. A notify object can display a user interface, notify the component of binding events so that the component can exercise some control over the binding process, and conditionally install or remove software components. For more information about notify objects, see [Notify Objects for Network Components](notify-objects-for-network-components.md).

A network adapter cannot have a notify object. It can have co-installers. For more information about co-installers, see [Writing a Co-installer](https://msdn.microsoft.com/library/windows/hardware/ff554011).

### Vendor-supplied files

A vendor supplies one or more drivers for the device, which typically consists of a driver image (.sys) file and a driver library (.dll) file. A vendor may also supply an optional driver *catalog file*. A vendor gets a digital signature by submitting its driver package to the Windows Hardware Quality Lab (WHQL) for testing and signing. WHQL returns the package with a catalog (.cat) file. The vendor must list the catalog file in the INF file for the device.

An optional text-mode setup information file (txtsetup.oem) may also be supplied by the vendor. If a network device is required to boot the machine, the driver or drivers for the device must be included in the operating system kit or the vendor of such a device must provide a txtsetup.oem file. The txtsetup.oem file contains information that is used by the system setup components to install the device during text-mode setup.

 

 





