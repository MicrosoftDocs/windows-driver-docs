---
title: Verifying the Signature of a Test-Signed Catalog File
description: Verifying the Signature of a Test-Signed Catalog File
ms.assetid: fa627f5b-977e-49ca-b099-358ed686eef7
keywords:
- verifying test signatures
- checking test signatures
- catalog files WDK driver signing , verifying signatures
- test signing catalog files WDK
- validating test certificates WDK
- test signing driver packages WDK , catalog files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Verifying the Signature of a Test-Signed Catalog File


To verify that a [driver package's](driver-packages.md) [catalog file](catalog-files.md) was signed by a valid [test certificate](test-certificates.md), use the following [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) command:

```cpp
SignTool verify /v /pa CatalogFileName.cat
```

To verify that a file, listed in a [driver package's](driver-packages.md) catalog file, is signed by a test certificate, use the following [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) command:

```cpp
SignTool verify /v /pa /c CatalogFileName.cat DriverFileName
```

Where:

-   The **verify** command configures SignTool to verify the signature of the driver package's catalog file *CatalogFileName.cat* or the driver file *DriverFileName*.

-   The **/v** option configures SignTool to print execution and warning messages.

-   The **/pa** option configures SignTool to verify that the signature of the catalog file or driver file complies with the PnP device installation signing requirements.

-   *CatalogFileName.cat* is the name of the catalog file for a driver package.

-   *The* ***/c*** *CatalogFileName.cat* option specifies a catalog file that includes an entry for the file *DriverFileName*.

-   *DriverFileName* is the name of a file that has an entry in the catalog file *CatalogFileName.cat*.

Be aware that the SignTool **verify** command does not explicitly specify the test certificate that was used to sign the [catalog file](catalog-files.md). For the verify operation to succeed, you must first install the test certificate in the [Trusted Root Certification Authorities certificate store](trusted-root-certification-authorities-certificate-store.md) of the local computer that you use to verify the signature. For more information about how to install the test certificate in the Trusted Root Certification Authorities certificate store of a local computer, see [Installing a Test Certificate on a Test Computer](installing-a-test-certificate-on-a-test-computer.md). The installation procedure is the same on both the signing computer and a test computer.

For example, the following command verifies that *Tstamd64.cat* has a test signature that complies with the PnP device installation signing requirements of Windows Vista and later versions of Windows. In this example, *Tstam64.cat* is in the same directory in which the command is run.

```cpp
SignTool verify /v /pa tstamd64.cat
```

 

 





