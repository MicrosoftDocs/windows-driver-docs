---
title: Signing a Catalog File with a Commercial Release Certificate
description: Signing a Catalog File with a Commercial Release Certificate
ms.assetid: 362b0c79-50b9-4749-80e2-62601d76e9e3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Signing a Catalog File with a Commercial Release Certificate


Use the following [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) command to sign the [catalog file](catalog-files.md) of a kernel-mode [driver package](driver-packages.md) with a [commercial release certificate](commercial-release-certificate.md).

**Note**  For 32-bit versions of Windows Vista and later versions of Windows, only a commercial release certificate can be used to sign kernel-mode drivers to be released on these Windows versions.

 

```cpp
SignTool sign /v /s CertificateStore /n CertificateName /t http://timestamp.verisign.com/scripts/timstamp.dll CatalogFileName.cat
```

Where:

-   The **sign** command configures SignTool to sign the catalog file *CatalogFileName.cat*.

-   The **/v** verbose option configures SignTool to print execution and warning messages.

-   The **/s** *CertificateStore* option specifies the name of the certificate store that contains the *CertificateName* certificate. Follow the instructions of the certification authority (CA) that issued the certificate on how to install the certificate in the system certificate stores.

-   The **/n** *CertificateName* option specifies the name of the certificate in the *CertificateStore* certificate store.

-   The **/t**  *http://timestamp.verisign.com/scripts/timstamp.dll* option supplies the URL to the publicly-available time-stamp server that VeriSign provides.

-   *CatalogFileName.cat* is the name of the catalog file.

 

 





