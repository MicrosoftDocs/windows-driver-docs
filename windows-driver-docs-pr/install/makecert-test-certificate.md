---
title: MakeCert Test Certificate
description: MakeCert Test Certificate
ms.assetid: 17f63c42-a563-4a57-a3be-ac3b2e97ee3b
keywords:
- MakeCert test certificates WDK
- digital certificates WDK
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MakeCert Test Certificate


A MakeCert test certificate is an [X.509 digital certificate](digital-certificates.md) that is created by using the command-line [CryptoAPI](http://go.microsoft.com/fwlink/p/?linkid=136391) [**MakeCert**](https://msdn.microsoft.com/library/windows/hardware/ff548309) tool. A MakeCert test certificate is a self-signed root certificate that can be used to test-sign a [driver package's](driver-packages.md) [catalog file](catalog-files.md) or to test-sign a driver file by embedding a signature in the driver file.

To create a MakeCert test certificate, use the [**MakeCert**](https://msdn.microsoft.com/library/windows/hardware/ff548309) tool as follows:

```
MakeCert -r -pe -ss TestCertStoreName -n "CN=CertName" CertFileName.cer
```

Where:

-   The **-r** option specifies that the certificate is self-signed, that is, the certificate is a root certificate.

-   The **-pe** option specifies that the private key that is associated with the certificate can be exported.

-   The **-ss**  *TestCertStoreName* option specifies the name of the certificate store that contains the test certificate.

-   The **-n** ***"*CN=***CertName****"*** option specifies a name for the certificate that can be used with the [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) tool to identify the certificate. We recommend that you use a certificate name that clearly identifies the certificate as a test certificate, for example, "WDK Driver Testing Cert - for in-house use only." If the certificate name is not supplied, the default name of the certificate is "Joe's Software Emporium."

-   *CertFilename.cer* is the file name that contains a copy of the test certificate. The certificate file is used to add the certificate to the Trusted Root Certification Authorities certificate store and the Trusted Publishers certificate stores.

The certificate store that contains the test certificate is added to the list of certificate stores that Windows manages for the user account on the development computer on which the certificate store was created.

A developer has to create only one MakeCert test certificate to sign all [driver packages](driver-packages.md) on a development computer.

In the following example, the MakeCert command generates a test certificate named "Contoso.com(Test)", installs the test certificate in the *PrivateCertStore* certificate store, and creates the *Testcert.cer* file that contains a copy of the test certificate.

```
MakeCert -r -pe -ss PrivateCertStore -n "CN=Contoso.com(Test)" testcert.cer
```

### <a href="" id="installing-a-makecert-test-certificate"></a> Installing a MakeCert test certificate

To test-sign a [catalog file](catalog-files.md) or embed a signature in a driver file, the MakeCert test certificate can be in the Personal certificate store ("my" store), or some other custom certificate store, of the local computer that signs the software. However, to verify a test signature, the corresponding test certificate must be installed in the [Trusted Root Certification Authorities certificate store](trusted-root-certification-authorities-certificate-store.md) of the local computer that you use to verify the signature.

Use the [**CertMgr**](https://msdn.microsoft.com/library/windows/hardware/ff543411) tool, as follows, to install a test certificate in the Trusted Root Certification Authorities certificate store of the local computer that you use to sign drivers:

```
CertMgr /add CertFileName.cer /s /r localMachine root
```

Before you can install a [driver package](driver-packages.md) that is signed by a MakeCert test certificate, the test certificate must be installed in the Trusted Root Certification Authorities certificate store and the [Trusted Publishers certificate store](trusted-publishers-certificate-store.md) of the test computer. For information about how to install a MakeCert test certificate on a test computer, see [Installing a Test Certificate on a Test Computer](installing-a-test-certificate-on-a-test-computer.md).

 

 





