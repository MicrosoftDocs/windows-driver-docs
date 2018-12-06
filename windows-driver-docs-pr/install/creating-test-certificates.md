---
title: Creating Test Certificates
description: Creating Test Certificates
ms.assetid: 4e6daa96-029c-4e1c-b483-b900cb836858
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Test Certificates


Test-signing requires a test certificate. After a test certificate is generated, it can be used to test-sign multiple drivers or [driver packages](driver-packages.md). For more information, see [Test Certificates](test-certificates.md).

This topic describes how to use the [**MakeCert**](https://msdn.microsoft.com/library/windows/hardware/ff548309) tool to create test certificates. In most development environments, test certificates generated through MakeCert should be sufficient to test the installation and loading of test-signed drivers or driver packages. For more information about this type of test certificate, see [MakeCert Test Certificate](makecert-test-certificate.md).

The following command-line example uses MakeCert to complete the following tasks:

-   Create a self-signed test certificate named *Contoso.com(Test)*. This certificate uses the same name for the subject name and the certificate authority (CA).

-   Put a copy of the certificate in an output file that is named *ContosoTest.cer*.

-   Put a copy of the certificate in a certificate store that is named *PrivateCertStore*. Putting the test certificate in *PrivateCertStore* keeps it separate from other certificates that may be on the system.

Use the following MakeCert command to create the *Contoso.com(Test)* certificate:

```cpp
makecert -r -pe -ss PrivateCertStore -n CN=Contoso.com(Test) -eku 1.3.6.1.5.5.7.3.3 ContosoTest.cer
```

Where:

-   The **-r** option creates a self-signed certificate with the same issuer and subject name.

-   The **-pe** option specifies that the private key that is associated with the certificate can be exported.

-   The **-ss** option specifies the name of the certificate store that contains the test certificate (*PrivateCertStore*).

-   The **-n CN=** option specifies the name of the certificate, Contoso.com(Test). This name is used with the [**SignTool**](../devtest/signtool.md) tool to identify the certificate.

-   The EKU option limits the usage of the resulting certificate to code signing.

-   *ContosoTest.cer* is the file name that contains a copy of the test certificate, Contoso.com(Test). The certificate file is used to add the certificate to the Trusted Root Certification Authorities certificate store and the Trusted Publishers certificate store.

The certificate store that contains the test certificate is added to the list of certificate stores that Windows manages for the user account on the development computer on which the certificate store was created.

A developer has to create only one MakeCert test certificate to sign all [driver packages](driver-packages.md) on a development computer.

For more information about the MakeCert tool and its command-line arguments, see [**MakeCert**](https://msdn.microsoft.com/library/windows/hardware/ff548309).

Also refer to the readme file *Selfsign_readme.htm* in the *bin\\selfsign* directory of the Windows Driver Kit (WDK).

 

 





