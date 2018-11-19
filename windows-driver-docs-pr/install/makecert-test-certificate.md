---
title: MakeCert Test Certificate
description: MakeCert Test Certificate
ms.assetid: 17f63c42-a563-4a57-a3be-ac3b2e97ee3b
keywords:
- MakeCert test certificates WDK
- digital certificates WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MakeCert Test Certificate


A MakeCert test certificate is an [X.509 digital certificate](digital-certificates.md) that is created by using the [**MakeCert**](https://msdn.microsoft.com/library/windows/hardware/ff548309) tool. A MakeCert test certificate is a self-signed root certificate that can be used to test-sign a [driver package's](driver-packages.md) [catalog file](catalog-files.md) or to test-sign a driver file by embedding a signature in the driver file.

To learn more about creating a MakeCert test certificate, see [**Creating Test Certificates**](creating-test-certificates.md).

## Installing a MakeCert test certificate

To test-sign a [catalog file](catalog-files.md) or embed a signature in a driver file, the MakeCert test certificate can be in the Personal certificate store ("my" store), or some other custom certificate store, of the local computer that signs the software. However, to verify a test signature, the corresponding test certificate must be installed in the [Trusted Root Certification Authorities certificate store](trusted-root-certification-authorities-certificate-store.md) of the local computer that you use to verify the signature.

Use the [**CertMgr**](../devtest/certmgr.md) tool, as follows, to install a test certificate in the Trusted Root Certification Authorities certificate store of the local computer that you use to sign drivers:

```cpp
CertMgr /add CertFileName.cer /s /r localMachine root
```

Before you can install a [driver package](driver-packages.md) that is signed by a MakeCert test certificate, the test certificate must be installed in the Trusted Root Certification Authorities certificate store and the [Trusted Publishers certificate store](trusted-publishers-certificate-store.md) of the test computer. For information about how to install a MakeCert test certificate on a test computer, see [Installing a Test Certificate on a Test Computer](installing-a-test-certificate-on-a-test-computer.md).

 

 





