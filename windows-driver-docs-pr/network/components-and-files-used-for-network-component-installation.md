---
title: Components and Files Used for Network Component Installation
description: Components and Files Used for Network Component Installation
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
ms.date: 01/16/2019
---

# Components and Files Used for Network Component Installation

The following components and files are used to install network drivers:

-   One or more information (INF) files

-   A required class installer and optional co-installer for miniport drivers

-   INetCfg for protocol and filter drivers

-   An optional notify object

In addition to one or more of the above components, a vendor also optionally supplies the following files:

-   One or more device driver image (.sys) files and driver library (.dll) files

-   A driver catalog file

-   A text-mode setup information file (txtsetup.oem)

## INF files

Each network component must have an information (INF) file that the network class installer uses to install the component. Network INF files are based on the common INF file format. For more information about the INF file format, see [INF File Sections and Directives](../install/index.md).

For detailed information about creating INF files for network components, see [Creating Network INF Files](creating-network-inf-files.md).

Starting with Windows OS build version 25319, you can create a network driver package that can be executed from the [Driver Store](../develop/run-from-driver-store.md). An INF that is using 'run from Driver Store' means that the INF uses [**DIRID 13**](../install/using-dirids.md) to specify the location for [driver package](../install/driver-packages.md) files on install.

You can't install a driver package through the network configuration interfaces and use the driver store feature on older Windows versions. To successfully install the driver package in this scenario, you need to have a minimum OS build number of 25319.


To use DIRID 13, include the following section in the INF file:

```cpp
[Standard.NT$ARCH$.10.0...25319]
%NDISPROT_Desc%=Install, MS_NDISPROT
```

To use DIRID 12, include the following section in the INF file:

```cpp
[Standard.NT$ARCH$]
%NDISPROT_Desc%=Install_NC, MS_NDISPROT
```

To allow your driver to install using DIRID 12 or DIRID 13 depending on the OS build number that the driver is being installed on, include both sections in the INF file. For an example INF file that installs differently depending on the OS build number, see [NDIS Protocol Driver INF File sample](https://github.com/microsoft/Windows-driver-samples/blob/develop/network/ndis/ndisprot/6x/sys/630/ndisprot630.inf).

## INetCfg

Currently, NDIS protocol and filter drivers are installed by calling into the `INetCfg` family of [Network Configuration Interfaces](/previous-versions/windows/hardware/network/ff559080(v=vs.85)). For example, to install or remove network components, a driver writer calls into the [INetCfgClassSetup](/previous-versions/windows/hardware/network/ff547709(v=vs.85)) interface. 

Driver writers can either call into this interface programmatically or they can use [netcfg.exe](/windows-server/administration/windows-commands/netcfg), which calls `INetCfg` on their behalf.

For more information about protocol driver installation, see [NDIS protocol driver installation](ndis-protocol-driver-installation.md).

For more information about filter driver installation, see [NDIS Filter Driver Installation](ndis-filter-driver-installation.md).

## Notify object

A software component, such as a network protocol, client, or service, can have a *notify object*. A notify object can display a user interface, notify the component of binding events so that the component can exercise some control over the binding process, and conditionally install or remove software components. For more information about notify objects, see [Notify Objects for Network Components](notify-objects-for-network-components.md).

A network adapter cannot have a notify object. It can have co-installers. For more information about co-installers, see [Writing a Co-installer](../install/writing-a-co-installer.md).

If you want to create a driver package that can be executed from the [Driver Store](../install/driver-store.md), you can't install it with notify objects on older Windows versions. To successfully install the driver package in this scenario, you need to have a minimum OS build number of 25341. 

## Vendor-supplied files

A vendor supplies one or more drivers for the device, which typically consists of a driver image (.sys) file and a driver library (.dll) file. A vendor may also supply an optional driver *catalog file*. A vendor gets a digital signature by submitting its driver package to the Windows Hardware Quality Lab (WHQL) for testing and signing. WHQL returns the package with a catalog (.cat) file. The vendor must list the catalog file in the INF file for the device.

An optional text-mode setup information file (txtsetup.oem) may also be supplied by the vendor. If a network device is required to boot the machine, the driver or drivers for the device must be included in the operating system kit or the vendor of such a device must provide a txtsetup.oem file. The txtsetup.oem file contains information that is used by the system setup components to install the device during text-mode setup.

 

