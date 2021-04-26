---
title: Using CertMgr to Install Test Certificates on a Test Computer
description: Using CertMgr to Install Test Certificates on a Test Computer
keywords:
- Certmgr Tool
- Certificate Manager tool WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using CertMgr to Install Test Certificates on a Test Computer


To install test certificates on a test computer by using [**CertMgr**](../devtest/certmgr.md), follow these steps:

1.  Copy the certificate (*.cer*) file, which was used to [test-sign](test-signing-driver-packages.md) drivers, to the test computer. You can copy the certificate file to any directory on the test computer.

2.  Use [**CertMgr**](../devtest/certmgr.md) commands to add the certificate to the [Trusted Root Certification Authorities certificate store](trusted-root-certification-authorities-certificate-store.md) and the [Trusted Publishers certificate store](trusted-publishers-certificate-store.md).

The following CertMgr command adds the certificate in the certificate file *CertificateFileName.cer* to the Trusted Root Certification Authorities certificate store on the test computer:

```cpp
CertMgr.exe /add CertificateFileName.cer /s /r localMachine root /all
```

The following CertMgr command adds the certificate in the certificate file *CertificateFileName.cer* to the Trusted Publishers certificate store on the test computer:

```cpp
CertMgr.exe /add CertificateFileName.cer /s /r localMachine trustedpublisher
```

 

