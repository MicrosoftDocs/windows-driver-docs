---
title: Signing a Catalog File with a Commercial Release Certificate
description: Signing a Catalog File with a Commercial Release Certificate
ms.assetid: 362b0c79-50b9-4749-80e2-62601d76e9e3
---

# Signing a Catalog File with a Commercial Release Certificate


Use the following [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) command to sign the [catalog file](catalog-files.md) of a kernel-mode [driver package](driver-packages.md) with a [commercial release certificate](commercial-release-certificate.md).

**Note**  For 32-bit versions of Windows Vista and later versions of Windows, only a commercial release certificate can be used to sign kernel-mode drivers to be released on these Windows versions.

 

```
SignTool sign /v /s CertificateStore /n CertificateName /t http://timestamp.verisign.com/scripts/timstamp.dll CatalogFileName.cat
```

Where:

-   The **sign** command configures SignTool to sign the catalog file *CatalogFileName.cat*.

-   The **/v** verbose option configures SignTool to print execution and warning messages.

-   The **/s** *CertificateStore* option specifies the name of the certificate store that contains the *CertificateName* certificate. Follow the instructions of the certification authority (CA) that issued the certificate on how to install the certificate in the system certificate stores.

-   The **/n** *CertificateName* option specifies the name of the certificate in the *CertificateStore* certificate store.

-   The **/t**  *http://timestamp.verisign.com/scripts/timstamp.dll* option supplies the URL to the publicly-available time-stamp server that VeriSign provides.

-   *CatalogFileName.cat* is the name of the catalog file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Signing%20a%20Catalog%20File%20with%20a%20Commercial%20Release%20Certificate%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




