---
title: Verifying the Signature of a Catalog File Signed by a Commercial Release Certificate
description: Verifying the Signature of a Catalog File Signed by a Commercial Release Certificate
ms.assetid: 153bb1e7-009d-4ef8-b5d7-a9e6eecf65bf
---

# Verifying the Signature of a Catalog File Signed by a Commercial Release Certificate


To verify that a [catalog file](catalog-files.md) is signed by a valid [commercial release certificate](commercial-release-certificate.md), use the following [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) command:

```
SignTool verify /v /pa CatalogFileName.cat
```

To verify that a file that is listed in a [driver package's](driver-packages.md) catalog file is signed by a valid commercial release certificate, use the following SignTool command:

```
SignTool verify /v /pa /c CatalogFileName.cat DriverFileName
```

Where:

-   The **verify** command configures SignTool to verify the signature of the driver package's catalog file *CatalogFileName.cat* or the driver file *DriverFileName*.

-   The **/v** option configures SignTool to print execution and warning messages.

-   The **/pa** option configures SignTool to verify that the signature of the catalog file or driver file complies with the PnP driver installation requirements.

-   *CatalogFileName.cat* is the name of the catalog file for a driver package.

-   *The* ***/c*** *CatalogFileName.cat* option specifies a catalog file that includes an entry for the file *DriverFileName*.

-   *DriverFileName* specifies the name of a file that has an entry in the catalog file *CatalogFileName.cat*.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Verifying%20the%20Signature%20of%20a%20Catalog%20File%20Signed%20by%20a%20Commercial%20Release%20Certificate%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




