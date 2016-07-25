---
title: Creating Test Certificates
description: Creating Test Certificates
ms.assetid: 4e6daa96-029c-4e1c-b483-b900cb836858
---

# Creating Test Certificates


Test-signing requires a test certificate. After a test certificate is generated, it can be used to test-sign multiple drivers or [driver packages](driver-packages.md). For more information, see [Test Certificates](test-certificates.md).

This topic describes how to use the [**MakeCert**](https://msdn.microsoft.com/library/windows/hardware/ff548309) tool to create test certificates. In most development environments, test certificates generated through MakeCert should be sufficient to test the installation and loading of test-signed drivers or driver packages. For more information about this type of test certificate, see [MakeCert Test Certificate](makecert-test-certificate.md).

The following command-line example uses MakeCert to complete the following tasks:

-   Create a self-signed test certificate named *Contoso.com(Test)*. This certificate uses the same name for the subject name and the certificate authority (CA).

-   Put a copy of the certificate in an output file that is named *ContosoTest.cer*.

-   Put a copy of the certificate in a certificate store that is named *PrivateCertStore*. Putting the test certificate in *PrivateCertStore* keeps it separate from other certificates that may be on the system.

Use the following MakeCert command to create the *Contoso.com(Test)* certificate:

```
makecert -r -pe -ss PrivateCertStore -n CN=Contoso.com(Test) ContosoTest.cer
```

Where:

-   The **-r** option creates a self-signed certificate with the same issuer and subject name.

-   The **-pe** option specifies that the private key that is associated with the certificate can be exported.

-   The **-ss** option specifies the name of the certificate store that contains the test certificate (*PrivateCertStore*).

-   The **-n CN=** option specifies the name of the certificate, Contoso.com(Test). This name is used with the [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) tool to identify the certificate.

-   *ContosoTest.cer* is the file name that contains a copy of the test certificate, Contoso.com(Test). The certificate file is used to add the certificate to the Trusted Root Certification Authorities certificate store and the Trusted Publishers certificate store.

For more information about the MakeCert tool and its command-line arguments, see [**MakeCert**](https://msdn.microsoft.com/library/windows/hardware/ff548309).

Also, refer to the readme file *Selfsign\_readme.htm* and the script file *Selfsign\_example.cmd*, which are located in the *src\\general\\build\\driversigning* directory of the Windows Driver Kit (WDK). The script file *Selfsign\_example.cmd* includes a documented example of how to use MakeCert to create a test certificate.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Creating%20Test%20Certificates%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




