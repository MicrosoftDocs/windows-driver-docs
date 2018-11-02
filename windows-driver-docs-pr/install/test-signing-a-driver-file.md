---
title: Test-Signing a Driver File
description: Test-Signing a Driver File
ms.assetid: 3d73d632-e910-43e7-a8fd-c78a11df0206
keywords:
- test signing driver packages WDK , driver files
- test signing driver packages WDK , embedding signatures
- embedded signatures in driver files WDK
- signatures WDK , embedded
- digital signatures WDK , embedded
- MakeCert test certificates WDK
- test signing driver files WDK
- commercial test certificates WDK
- Enterprise CA test certificates WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Test-Signing a Driver File


Use [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) to embed a signature in a driver file as described in the following topics:

[Using a MakeCert Test Certificate or a Commercial Test Certificate to Embed a Test Signature in a Driver File](#using-a-makecert-test-certificate-or-a-commercial-test-certificate-to-)

[Using an Enterprise CA Test Certificate to Embed a Test Signature in a Driver File](#using-an-enterprise-ca-test-certificate-to-embed-a-test-signature-in-a)

### <a href="" id="using-a-makecert-test-certificate-or-a-commercial-test-certificate-to-"></a> Using a MakeCert Test Certificate or a Commercial Test Certificate to Embed a Test Signature in a Driver File

Use the following SignTool command to embed a signature in a driver file by using a [MakeCert test certificate](makecert-test-certificate.md) or a [commercial test certificate](commercial-test-certificate.md).

```cpp
SignTool sign /v /s TestCertStoreName /n TestCertName /t http://timestamp.verisign.com/scripts/timstamp.dll DriverFileName.sys
```

Where:

-   The sign command configures SignTool to embed a signature in the driver file DriverFileName.sys.

-   The **/v** verbose option configures SignTool to print execution and warning messages.

-   The **/s** *TestCertStoreName* option supplies the name of the test certificate store that contains the test certificate named *TestCertName*.

-   The **/n** *TestCertName* option supplies the name of the test certificate that is installed in the certificate store named *TestCertStoreName*. The test certificate can be either a MakeCert test certificate or a commercial test certificate.

-   The **/t** *http://timestamp.verisign.com/scripts/timstamp.dll* option supplies the URL to the publicly-available time-stamp server that VeriSign provides.

-   *DriverFileName.sys* is the name of the driver file.

The following command shows how to use SignTool to test-sign a driver file. This example embeds a signature in *Toaster.sys*, which is in the *amd64* subdirectory under the directory in which the command is run. The test certificate is named "contoso.com(test)" and it is installed in the certificate store named "PrivateCertStore."

```cpp
SignTool sign /v /s PrivateCertStore /n contoso.com(test) /t http://timestamp.verisign.com/scripts/timstamp.dll amd64\toaster.sys
```

### <a href="" id="using-an-enterprise-ca-test-certificate-to-embed-a-test-signature-in-a"></a>**Using an Enterprise CA Test Certificate to Embed a Test Signature in a Driver File**

The following SignTool command assumes that an Enterprise CA issues the test certificate that you use to test-sign a [driver package](driver-packages.md). If the [Enterprise CA test certificate](enterprise-ca-test-certificate.md) is the only test certificate that is present in your certificate stores, you can use the following command where you specify only the **/a** option and the name of the driver file. In this situation, SignTool will locate and use your Enterprise CA test certificate by default.

If you have created or obtained other test certificates in addition to an Enterprise CA test certificate, you must use the SignTool options **/s** and **/n** to specify the name of the test certificate store and the name of the test certificate that is installed in the test certificate store.

```cpp
SignTool sign /v /a /t http://timestamp.verisign.com/scripts/timstamp.dll DriverFileName.sys
```

 

 





