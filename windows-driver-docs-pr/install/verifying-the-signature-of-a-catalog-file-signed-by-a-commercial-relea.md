---
title: Verify Catalog File Signed by Commercial Certificate
description: Verifying the Signature of a Catalog File Signed by a Commercial Release Certificate
ms.assetid: 153bb1e7-009d-4ef8-b5d7-a9e6eecf65bf
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Verifying the Signature of a Catalog File Signed by a Commercial Release Certificate


To verify that a [catalog file](catalog-files.md) is signed by a valid [commercial release certificate](commercial-release-certificate.md), use the following [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) command:

```cpp
SignTool verify /v /pa CatalogFileName.cat
```

To verify that a file that is listed in a [driver package's](driver-packages.md) catalog file is signed by a valid commercial release certificate, use the following SignTool command:

```cpp
SignTool verify /v /pa /c CatalogFileName.cat DriverFileName
```

Where:

-   The **verify** command configures SignTool to verify the signature of the driver package's catalog file *CatalogFileName.cat* or the driver file *DriverFileName*.

-   The **/v** option configures SignTool to print execution and warning messages.

-   The **/pa** option configures SignTool to verify that the signature of the catalog file or driver file complies with the PnP driver installation requirements.

-   *CatalogFileName.cat* is the name of the catalog file for a driver package.

-   *The* ***/c*** *CatalogFileName.cat* option specifies a catalog file that includes an entry for the file *DriverFileName*.

-   *DriverFileName* specifies the name of a file that has an entry in the catalog file *CatalogFileName.cat*.

 

 





