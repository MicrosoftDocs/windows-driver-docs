---
title: Installing Test Certificates
description: Installing Test Certificates
ms.assetid: 4c306390-32cc-4c7a-9f61-48e8af385a6d
---

# Installing Test Certificates


To successfully install a test-signed [driver package](driver-packages.md) on a test computer, the computer must be able to verify the signature. To do that, the test computer must have the certificate for the certificate authority (CA) that issued the package's test certificate installed in the computer's Trusted Root Certification Authorities certificate store

The CA certificate must be added to the Trusted Root Certification Authorities certificate store only once. Once added, it can then be used to verify the signature of all drivers or driver packages, which were digitally signed with the certificate, before the driver package is installed on the computer.

The simplest way to add a test certificate to the Trusted Root Certification Authorities certificate store is through the [**CertMgr**](https://msdn.microsoft.com/library/windows/hardware/ff543411) tool. This topic will describe the procedure for installing the test certificate, Contoso.com(test). This certificate is stored within the *ContosoTest.cer* file. For more information about how this certificate was created, see [Creating Test Certificates](creating-test-certificates.md).

The following command-line uses Certmgr.exe to install, or add, the Contoso.com(test) certificate to the test computer's Trusted Root Certification Authorities certificate store:

```
certmgr.exe /add ContosoTest.cer /s /r localMachine root
```

Where:

-   The /add option specifies that the certificate in the *ContosoTest.cer* file is to be added to the specified certificate store.

-   The **/s** option specifies that the certificate is to be added to a system store.

-   The /r option specifies the system store location, which is either *currentUser* or *localMachine*.

-   *Root* specifies the name of the destination store for the local computer, which is either ***root*** to specify the Trusted Root Certification Authorities certificate store or ***trustedpublisher*** to specify the Trusted Publishers certificate store.

After the certificate is copied to the Trusted Root Certification Authorities certificate store, you can view it through the Microsoft Management Console (MMC) Certificates snap-in, as described in [Viewing Test Certificates](viewing-test-certificates.md).

The following screen shot shows the Contoso.com(Test) certificate in the Trusted Root Certification Authorities certificate store.

![screen shot of the trusted root certification authorities certificate store in the mmc certificates snap-in](images/certstore2.png)

For more information about CertMgr and its command-line arguments, see [**CertMgr**](https://msdn.microsoft.com/library/windows/hardware/ff543411).

For more information about how to install test certificates, see [Installing a Test Certificate on a Test Computer](installing-a-test-certificate-on-a-test-computer.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installing%20Test%20Certificates%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




