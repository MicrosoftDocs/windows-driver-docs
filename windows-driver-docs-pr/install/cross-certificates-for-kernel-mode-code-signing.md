---
title: Cross-Certificates for Kernel Mode Code Signing
description: This information describes cross-certificates which are now deprecated for driver signing on Microsoft Windows.
ms.date: 09/19/2023
---

# Cross-Certificates for Kernel Mode Code Signing

[!include[Warning about deprecation of cross signing for driver signing](../includes/cross-signing-deprecation-warning.md)]

## Cross-Certificates Overview

A cross-certificate is a digital certificate issued by one Certificate Authority (CA) that is used to sign the public key for the root certificate of another Certificate Authority. Cross-certificates provide a means to create a chain of trust from a single, trusted, root CA to multiple other CAs.

## Related info

* [Deprecation of Software Publisher Certificates, Commercial Release Certificates, and Commercial Test Certificates](deprecation-of-software-publisher-certificates-and-commercial-release-certificates.md)
* [Authenticode Signing of Third-party CSPs](authenticode-signing-of-csps.md)
