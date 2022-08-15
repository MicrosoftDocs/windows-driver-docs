---
title: Preloading Driver Packages
description: Preloading Driver Packages
keywords:
- installation applications WDK , preloaded driver packages
- device installation applications WDK , preloaded driver packages
- preloaded driver packages WDK device installations
ms.date: 04/20/2017
---

# Preloading Driver Packages


Plug and Play (PnP) [driver packages](driver-packages.md) can be *preloaded* on a computer as part of a Windows installation or after Windows is installed on a computer. A network administrator can also preload driver packages on a network server that provides the source for driver packages that are installed on network computers. When Windows searches for drivers that match a device, Windows will check whether there are preloaded driver packages that match the device.

How to configure a Windows installation to preload driver packages is outside the scope of this documentation. For information about how to configure a Windows installation to preload driver packages, see [How to Add OEM Plug and Play Drivers to Windows XP](https://go.microsoft.com/fwlink/p/?linkid=3100&ID=314479) and [How to Add OEM Plug and Play Drivers to Windows Installations](/troubleshoot/windows-server/deployment/add-oem-plug-play-drivers).

After Windows is installed, a [driver package](driver-packages.md) can be preloaded in one of the following ways:

1.  To preload a driver package on a local computer, copy the driver package to a package-specific directory on a local computer and concatenate the local directory path of the driver package to the **DevicePath** value entry under the **HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion** subkey of the registry.

2.  To preload a driver package for a computer network, a network administrator can copy the driver package to a shared directory on a network server and concatenate the path of the shared directory to the **DevicePath** value entry in the registry of the network computers that have access to the shared directory.

The **DevicePath** value entry is a [REG_EXPAND_SZ](/windows/desktop/SysInfo/registry-value-types)-typed entry that contains the *%SystemRoot%\\inf* directory path and zero or more directory path entries. The format of the **DevicePath** value entry is the following, where each directory path is either a local directory path or a path of a shared directory on a network server where the preloaded [driver packages](driver-packages.md) are located:

```cpp
%SystemRoot%\inf;DirectoryPath1;DirectoryPath2;...
```

For example, to preload a driver package for a network adapter in the *%SystemRoot%\\Drivers\\NIC* directory on a local computer, an administrator copies the driver package to that directory and concatenates the path of the **DevicePath** value entry, as follows:

```cpp
%SystemRoot%\inf;...;%SystemRoot%\inf\Drivers\NIC
```

For example, to preload a driver package for a network adapter in the shared directory *\\\\DriverPackageServer\\ShareName\\Drivers\\NIC* on a network, a network administrator copies the driver package to the shared directory and concatenates the shared directory path of the **DevicePath** value entry in the registry of the network computers, as follows:

```cpp
%SystemRoot%\inf;...;\\DriverPackageServer\ShareName\Drivers\NIC
```

> [!NOTE]
> Specifying network share in DevicePath in a machine with point and print client connection can result in excessive network share access and printing delays. This is because each time printerdata is changed in the server, the client will iterate through DevicePath directories checking for availability of newer print drivers.
