---
title: Preloading Driver Packages
description: Preloading Driver Packages
ms.assetid: e617764d-0b48-4cd8-aeac-04d6039aba71
keywords: ["installation applications WDK , preloaded driver packages", "device installation applications WDK , preloaded driver packages", "preloaded driver packages WDK device installations"]
---

# Preloading Driver Packages


Plug and Play (PnP) [driver packages](driver-packages.md) can be *preloaded* on a computer as part of a Windows installation or after Windows is installed on a computer. A network administrator can also preload driver packages on a network server that provides the source for driver packages that are installed on network computers. When Windows searches for drivers that match a device, Windows will check whether there are preloaded driver packages that match the device.

How to configure a Windows installation to preload driver packages is outside the scope of this documentation. For information about how to configure a Windows installation to preload driver packages, see [How to Add OEM Plug and Play Drivers to Windows XP](http://go.microsoft.com/fwlink/p/?linkid=3100&amp;ID=314479) and [How to Add OEM Plug and Play Drivers to Windows Installations](http://go.microsoft.com/fwlink/p/?linkid=70235).

After Windows is installed, a [driver package](driver-packages.md) can be preloaded in one of the following ways:

1.  To preload a driver package on a local computer, copy the driver package to a package-specific directory on a local computer and concatenate the local directory path of the driver package to the **DevicePath** value entry under the **HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion** subkey of the registry.

2.  To preload a driver package for a computer network, a network administrator can copy the driver package to a shared directory on a network server and concatenate the path of the shared directory to the **DevicePath** value entry in the registry of the network computers that have access to the shared directory.

The **DevicePath** value entry is a REG\_EXPAND\_SZ-typed entry that contains the *%SystemRoot%\\inf* directory path and zero or more directory path entries. The format of the **DevicePath** value entry is the following, where each directory path is either a local directory path or a path of a shared directory on a network server where the preloaded [driver packages](driver-packages.md) are located:

```
%SystemRoot%\inf;DirectoryPath1;DirectoryPath2;...
```

For example, to preload a driver package for a network adapter in the *%SystemRoot%\\Drivers\\NIC* directory on a local computer, an administrator copies the driver package to that directory and concatenates the path of the **DevicePath** value entry, as follows:

```
%SystemRoot%\inf;...;%SystemRoot%\inf\Drivers\NIC
```

For example, to preload a driver package for a network adapter in the shared directory *\\\\DriverPackageServer\\ShareName\\Drivers\\NIC* on a network, a network administrator copies the driver package to the shared directory and concatenates the shared directory path of the **DevicePath** value entry in the registry of the network computers, as follows:

```
%SystemRoot%\inf;...;\\DriverPackageServer\ShareName\Drivers\NIC
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Preloading%20Driver%20Packages%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




