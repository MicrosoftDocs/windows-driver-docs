---
title: Verifying the SPC Signature of a Catalog File
description: Verifying the SPC Signature of a Catalog File
ms.assetid: 57bc65fe-1c31-4ebb-a1bc-e1fe275f8d10
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Verifying the SPC Signature of a Catalog File


To verify that a [catalog file](catalog-files.md) is signed by a valid [Software Publisher Certificate (SPC)](software-publisher-certificate.md) and corresponding cross-certificate, use the following [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) command:

```cpp
SignTool verify /v /kp CatalogFileName.cat 
```

To verify that a file that is listed in a [driver package's](driver-packages.md) [catalog file](catalog-files.md) is signed by a [Software Publisher Certificate (SPC)](software-publisher-certificate.md) and corresponding cross-certificate, use the following SignTool command:

```cpp
SignTool verify /v /kp /c CatalogFileName.cat DriverFileName
```

Where:

-   The **verify** command configures SignTool to verify the signature of the [driver package's](driver-packages.md) catalog file *CatalogFileName.cat* or the driver file *DriverFileName*.

-   The **/v** option configures SignTool to print execution and warning messages.

-   The **/kp** option configures SignTool to verify that the signature of the file complies with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) and the [PnP device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md) of Windows Vista and later versions of Windows.

-   *CatalogFileName.cat* is the name of the catalog file for a driver package.

-   *The* ***/c*** *CatalogFileName.cat* option specifies a catalog file that includes an entry for the file *DriverFileName*.

-   *DriverFileName* is the name of a file that has an entry in the catalog file *CatalogFileName.cat*.

For example, the following command verifies that *Tstamd64.cat* has a digital signature that complies with the kernel-mode code signing policy and the PnP device installation signing requirements for Windows Vista and later versions of Windows. In this example, *Tstam64.cat* is in the same directory in which the command is run.

```cpp
SignTool verify /kp tstamd64.cat
```

In the next example, the following command verifies that *Toastpkg.inf*, which has an entry in the catalog file *Tstamd64.cat*, has a digital signature that complies with the kernel-mode code signing policy and the PnP device installation signing requirements of Windows Vista and later versions of Windows. In this example, *Tstam64.cat* and *Toastpkg.inf* are in the same directory in which the command is run.

```cpp
SignTool verify /kp /c tstamd64.cat toastpkg.inf
```

 

 





