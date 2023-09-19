---
title: Cross-Certificates for Kernel Mode Code Signing
description: This information describes cross-certificates which are now deprecated for driver signing on Microsoft Windows.
ms.date: 09/19/2023
---

# Cross-Certificates for Kernel Mode Code Signing

[!include[Warning about deprecation of cross signing for driver signing](../includes/cross-signing-deprecation-warning.md)]

## Cross-Certificates Overview

A cross-certificate is a digital certificate issued by one Certificate Authority (CA) that is used to sign the public key for the root certificate of another Certificate Authority. Cross-certificates provide a means to create a chain of trust from a single, trusted, root CA to multiple other CAs.

## Cross-Certificate List

The following table lists CAs that are no longer supported by Microsoft for issuing SPCs for code-signing kernel-mode code.

|                              CA                              |                 Root certificate thumbprint                 |Expiration date|
| :----------------------------------------------------------: | :---------------------------------------------------------: | :-----------: |
| AddTrust External CA Root                                    | a7 5a c6 57 aa 7a 4c df e5 f9 de 39 3e 69 ef ca b6 59 d2 50 | 2023/08/15    |
| GoDaddy Class 2 Certification Authority                      | d9 61 24 72 ef 0f 27 87 e2 b2 d9 e0 63 a0 6b 32 fa 5e 33 3d | 2023/08/27    |
| Starfield Class 2 Certification Authority                    | f8 fc 7f 3c dd 51 76 ad d2 7c f9 7f 73 96 59 09 46 6d 9a 22 | 2023/08/27    |
| UTN-USERFirst-Object                                         | ae 1e 25 26 01 30 a3 0b 1b c2 20 29 35 65 3b e5 a7 23 be f5 | 2023/08/15    |

## Related info

* [Deprecation of Software Publisher Certificates, Commercial Release Certificates, and Commercial Test Certificates](deprecation-of-software-publisher-certificates-and-commercial-release-certificates.md)
* [Authenticode Signing of Third-party CSPs](authenticode-signing-of-csps.md)
