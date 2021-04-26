---
title: Installing a Test Certificate on a Test Computer
description: Installing a Test Certificate on a Test Computer
keywords:
- test certificates WDK
- installing test certificates WDK
- test signing driver packages WDK , installing test certificates
- certificate stores WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a Test Certificate on a Test Computer


The [test certificates](./makecert-test-certificate.md) that are used to embed signatures in driver files and to sign a [driver package's](driver-packages.md) [catalog file](catalog-files.md) must be added to the [Trusted Root Certification Authorities certificate store](trusted-root-certification-authorities-certificate-store.md) and the [Trusted Publishers certificate store](trusted-publishers-certificate-store.md). You can manually add a test certificate to these certificate stores by using the [**CertMgr**](../devtest/certmgr.md) tool, as described in [Using CertMgr to Install Test Certificates on a Test Computer](using-certmgr-to-install-test-certificates-on-a-test-computer.md).

You can also configure the default domain policy to automatically deploy a test certificate on computers in a domain, as described in [Deploying a Test Certificate by Using the Default Domain Policy](deploying-a-test-certificate-by-using-the-default-domain-policy.md).

 

