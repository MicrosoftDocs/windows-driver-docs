---
title: Test-Signing a Catalog File
description: Test-Signing a Catalog File
ms.assetid: a6397f8f-e5f1-4ce2-af7b-a7846fa30bc8
keywords:
- catalog files WDK driver signing , test signing
- test signing catalog files WDK
- test signing driver packages WDK , catalog files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Test-Signing a Catalog File


After you create and verify a [driver package's](driver-packages.md) [catalog file](catalog-files.md), use [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) to test-sign the catalog file as described in the following topics:

[Using a MakeCert Test Certificate or Commercial Test Certificate to Test-Sign a Driver package's Catalog File](#using-a-makecert-test-certificate-or-commercial-test-certificate-to-te)

[Using an Enterprise CA Test Certificate to Test-Sign a Driver package's Catalog File](#using-an-enterprise-ca-test-certificate-to-test-sign-a-driver-package-)

### <a href="" id="using-a-makecert-test-certificate-or-commercial-test-certificate-to-te"></a> Using a MakeCert Test Certificate or Commercial Test Certificate to Test-Sign a Driver Package's Catalog File

Use the following SignTool command to sign a [catalog file](catalog-files.md) by using a [MakeCert test certificate](makecert-test-certificate.md) or a [commercial test certificate](commercial-test-certificate.md):

```cpp
SignTool sign /v /s TestCertStoreName /n TestCertName /t http://timestamp.verisign.com/scripts/timstamp.dll CatalogFileName.cat
```

Where:

-   The **sign** command configures SignTool to sign the [catalog file](catalog-files.md) that is named *CatalogFileName.cat*.

-   The **/v** verbose option configures SignTool to print execution and warning messages.

-   The **/s** *TestCertStoreName* option supplies the name of the test certificate store that contains the test certificate named *TestCertName*.

-   The **/n** *TestCertName* option supplies the name of the test certificate that is installed in the certificate store named *TestCertStoreName*. The test certificate can be either a MakeCert test certificate or a commercial test certificate.

-   The **/t** *http://timestamp.verisign.com/scripts/timstamp.dll* option supplies the URL to the publicly-available time-stamp server that VeriSign provides.

-   *CatalogFileName.cat* is the name of the [catalog file](catalog-files.md).

The following command shows how to use SignTool to test-sign a [driver package's](driver-packages.md) catalog file. This example signs the catalog file *Tstamd64.cat*, which is in the same directory in which the command is run. The test certificate is named "contoso.com(test)," which is installed in the certificate store named "PrivateCertStore."

```cpp
SignTool sign /v /s PrivateCertStore /n contoso.com(test) /t http://timestamp.verisign.com/scripts/timstamp.dll tstamd64.cat
```

### <a href="" id="using-an-enterprise-ca-test-certificate-to-test-sign-a-driver-package-"></a> Using an Enterprise CA Test Certificate to Test-Sign a Driver Package's Catalog File

The following SignTool command assumes that an Enterprise CA issues the test certificate that you use to test-sign a [driver package](driver-packages.md). If the [Enterprise CA test certificate](enterprise-ca-test-certificate.md) is the only test certificate that is present in your certificate stores, you can use the following command where you specify only the **/a** option and the name of the [catalog file](catalog-files.md). In this situation, SignTool will locate and use your Enterprise CA test certificate by default.

If you have created or obtained other test certificates in addition to an Enterprise CA test certificate, you must use the SignTool options **/s** and **/n** to specify the name of the test certificate store and the name of the test certificate that is installed in the test certificate store.

```cpp
SignTool sign /v /a /t http://timestamp.verisign.com/scripts/timstamp.dll CatalogFileName.cat
```

 

 





