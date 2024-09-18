---
title: Cross-Certificates for Kernel Mode Code Signing
description: This information describes cross-certificates which are now deprecated for driver signing on Microsoft Windows.
ms.date: 09/17/2024
ai-usage: ai-assisted
---

# Cross-Certificates for Kernel Mode Code Signing

[!include[Warning about deprecation of cross signing for driver signing](../includes/cross-signing-deprecation-warning.md)]

## Cross-Certificates Overview

A cross-certificate is a digital certificate issued by one Certificate Authority (CA) that establishes a trust relationship with another CA by allowing the public key of the other CA's root certificate to be trusted. This process is known as cross-signing, where the CA's certificate is signed by another CA to create multiple valid trust paths.


## Related info

* [Deprecation of Software Publisher Certificates, Commercial Release Certificates, and Commercial Test Certificates](deprecation-of-software-publisher-certificates-and-commercial-release-certificates.md)
* [Authenticode Signing of Third-party CSPs](authenticode-signing-of-csps.md)
