---
title: Installing a Test Certificate on a Test Computer
description: Installing a Test Certificate on a Test Computer
ms.assetid: b28bd334-cd75-4ea1-8f1b-d9cd5b417b53
keywords: ["test certificates WDK", "installing test certificates WDK", "test signing driver packages WDK , installing test certificates", "certificate stores WDK"]
---

# Installing a Test Certificate on a Test Computer


The [test certificates](test-certificates.md) that are used to embed signatures in driver files and to sign a [driver package's](driver-packages.md) [catalog file](catalog-files.md) must be added to the [Trusted Root Certification Authorities certificate store](trusted-root-certification-authorities-certificate-store.md) and the [Trusted Publishers certificate store](trusted-publishers-certificate-store.md). You can manually add a test certificate to these certificate stores by using the [**CertMgr**](https://msdn.microsoft.com/library/windows/hardware/ff543411) tool, as described in [Using CertMgr to Install Test Certificates on a Test Computer](using-certmgr-to-install-test-certificates-on-a-test-computer.md).

You can also configure the default domain policy to automatically deploy a test certificate on computers in a domain, as described in [Deploying a Test Certificate by Using the Default Domain Policy](deploying-a-test-certificate-by-using-the-default-domain-policy.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installing%20a%20Test%20Certificate%20on%20a%20Test%20Computer%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




