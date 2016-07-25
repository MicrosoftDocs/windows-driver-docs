---
title: Verifying the SPC Signature of a Catalog File
description: Verifying the SPC Signature of a Catalog File
ms.assetid: 57bc65fe-1c31-4ebb-a1bc-e1fe275f8d10
---

# Verifying the SPC Signature of a Catalog File


To verify that a [catalog file](catalog-files.md) is signed by a valid [Software Publisher Certificate (SPC)](software-publisher-certificate.md) and corresponding cross-certificate, use the following [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) command:

```
SignTool verify /v /kp CatalogFileName.cat 
```

To verify that a file that is listed in a [driver package's](driver-packages.md) [catalog file](catalog-files.md) is signed by a [Software Publisher Certificate (SPC)](software-publisher-certificate.md) and corresponding cross-certificate, use the following SignTool command:

```
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

```
SignTool verify /kp tstamd64.cat
```

In the next example, the following command verifies that *Toastpkg.inf*, which has an entry in the catalog file *Tstamd64.cat*, has a digital signature that complies with the kernel-mode code signing policy and the PnP device installation signing requirements of Windows Vista and later versions of Windows. In this example, *Tstam64.cat* and *Toastpkg.inf* are in the same directory in which the command is run.

```
SignTool verify /kp /c tstamd64.cat toastpkg.inf
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Verifying%20the%20SPC%20Signature%20of%20a%20Catalog%20File%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




