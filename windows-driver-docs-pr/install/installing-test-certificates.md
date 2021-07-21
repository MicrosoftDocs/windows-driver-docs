---
title: Installing Test Certificates
description: Installing Test Certificates
ms.date: 07/20/2020
ms.localizationpriority: medium
---

# Installing Test Certificates


To successfully install a test-signed [driver package](driver-packages.md) on a test computer, the computer must be able to verify the signature. To do that, the test computer must have the certificate for the certificate authority (CA) that issued the package's test certificate installed in the computer's Trusted Root Certification Authorities certificate store

The CA certificate must be added to the Trusted Root Certification Authorities certificate store only once. Once added, it can then be used to verify the signature of all drivers or driver packages, which were digitally signed with the certificate, before the driver package is installed on the computer.

The simplest way to add a test certificate to the Trusted Root Certification Authorities certificate store is through the [**CertMgr**](../devtest/certmgr.md) tool. This topic will describe the procedure for installing the test certificate, Contoso.com(test). This certificate is stored within the *ContosoTest.cer* file. For more information about how this certificate was created, see [Creating Test Certificates](creating-test-certificates.md).

The following command-line uses Certmgr.exe to install, or add, the Contoso.com(test) certificate to the test computer's Trusted Root Certification Authorities certificate store:

```cpp
certmgr /add ContosoTest.cer /s /r localMachine root
```

Where:

-   The /add option specifies that the certificate in the *ContosoTest.cer* file is to be added to the specified certificate store.

-   The **/s** option specifies that the certificate is to be added to a system store.

-   The /r option specifies the system store location, which is either *currentUser* or *localMachine*.

-   *Root* specifies the name of the destination store for the local computer, which is either ***root*** to specify the Trusted Root Certification Authorities certificate store or ***trustedpublisher*** to specify the Trusted Publishers certificate store.

A successful run produces the following output:

```cmd
certmgr /add ContosoTest.cer /s /r localMachine root
CertMgr Succeeded
```

After the certificate is copied to the Trusted Root Certification Authorities certificate store (the local machine's root store, *not* the user store), you can view it through the Microsoft Management Console (MMC) Certificates snap-in, as described in [Viewing Test Certificates](viewing-test-certificates.md).

The following screenshot shows the Contoso.com(Test) certificate in the Trusted Root Certification Authorities certificate store.

![screen shot of the trusted root certification authorities certificate store in the mmc certificates snap-in.](images/certstore2.png)

You can also view the certificate at the command prompt:

```cmd
certutil -store root | findstr Contoso
certutil -store root <SHA-1 id of certificate>
```

Or, from PowerShell:

```cmd
Get-ChildItem -path cert: \LocalMachine\My | findstr Contoso
```

The Certmgr.exe tool is part of the Windows SDK and is typically installed to `C:\Program Files (x86)\Windows Kits\10\bin\<build>\x86\certmgr.exe`.

For more information about CertMgr and its command-line arguments, see [**CertMgr**](../devtest/certmgr.md).

For more information about how to install test certificates, see [Installing a Test Certificate on a Test Computer](installing-a-test-certificate-on-a-test-computer.md).

 

