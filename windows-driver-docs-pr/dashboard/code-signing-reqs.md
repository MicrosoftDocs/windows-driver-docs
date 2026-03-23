---
title: Driver code signing requirements
description: Driver code signing requirements
ms.date: 05/29/2025
ms.topic: best-practice
---

# Driver code signing requirements

Your drivers must be signed with a certificate before you submit them to the hardware dashboard. Your organization can associate any number of certificates with its dashboard account, and each one of your submissions must be signed with any one of those certificates. There's no restriction on the number of certificates (both extended validation (EV) and Standard) associated with your organization.

This article provides general information on the types of code signing available for your drivers, and the associated requirements for those drivers.

For more extensive information on driver signing requirements see the following pages:

- [Driver Signing Changes in Windows 10](https://techcommunity.microsoft.com/blog/windowshardwarecertification/driver-signing-changes-in-windows-10/364859)
- [Driver Signing changes in Windows 10, version 1607](https://techcommunity.microsoft.com/blog/windowshardwarecertification/driver-signing-changes-in-windows-10-version-1607/364894)
- [Update on Sysdev EV Certificate requirement](https://techcommunity.microsoft.com/blog/windowshardwarecertification/update-on-sysdev-ev-certificate-requirement/364879)

## Where to get EV code signing certificates

EV Code signing certificates can be purchased from one of the following certificate authorities:

- [Certum EV code signing certificate](https://shop.certum.eu/certum-ev-code-sigining.html)
- [DigiCert EV code signing certificate](https://www.digicert.com/signing/code-signing-certificates)
- [GlobalSign EV code signing certificate](https://go.microsoft.com/fwlink/p/?LinkId=620888)
- [IdenTrust EV code signing certificate](https://www.identrust.com/digital-certificates/trustid-ev-code-signing)
- [Sectigo (formerly Comodo) EV code signing certificate](https://www.sectigo.com/ssl-certificates-tls/code-signing)
- [SSL.com EV code signing certificate](https://www.ssl.com/certificates/ev-code-signing/)

## EV certificate signed drivers

Your Hardware Dev Center dashboard account must have at least one EV certificate associated with it to submit binaries for attestation signing or to submit binaries for HLK certification.

The following rules apply:

- Your registered EV certificate must be valid at the time of submission.
- While Microsoft strongly recommends that you sign individual submissions with an EV certificate, you can alternatively sign submissions with an Authenticode signing certificate that is also registered to your Partner Center account.
- All certificates must be SHA2 and signed with the `/fd sha256` SignTool command line switch.

If you already have an approved EV certificate from a certificate authority, you can use it to establish a Partner Center account. If you don't have an EV certificate, choose [one the certificate authorities](#where-to-get-ev-code-signing-certificates) and follow their directions for purchase.

Once the certificate authority verifies your contact information and your certificate purchase is approved, follow their directions to retrieve the certificate.
