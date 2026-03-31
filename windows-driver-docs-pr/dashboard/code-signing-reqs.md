---
title: Driver Code Signing Requirements
description: This article describes requirements for code signing your driver.
ms.date: 05/29/2025
ms.topic: best-practice
---

# Driver code signing requirements

You must sign your drivers with a certificate before you submit them to the hardware dashboard. Your organization can associate any number of certificates with its dashboard account, and each one of your submissions must be signed with any one of those certificates. Whether you have extended validation (EV) or standard certificates, there's no restriction on the number of certificates associated with your organization.

This article provides general information on the types of code signing available for your drivers, and the associated requirements for those drivers.

For more extensive information on driver signing requirements, see:

- [Driver signing changes in Windows 10](https://techcommunity.microsoft.com/blog/windowshardwarecertification/driver-signing-changes-in-windows-10/364859)

- [Driver signing changes in Windows 10, version 1607](https://techcommunity.microsoft.com/blog/windowshardwarecertification/driver-signing-changes-in-windows-10-version-1607/364894)

- [Update on Sysdev EV Certificate requirement](https://techcommunity.microsoft.com/blog/windowshardwarecertification/update-on-sysdev-ev-certificate-requirement/364879)

## Where to get EV code signing certificates

You can purchase EV code signing certificates from one of the following certificate authorities:

- [Certum EV code signing certificate](https://shop.certum.eu/certum-ev-code-sigining.html)

- [DigiCert EV code signing certificate](https://www.digicert.com/signing/code-signing-certificates)

- [GlobalSign EV code signing certificate](https://go.microsoft.com/fwlink/p/?LinkId=620888)

- [IdenTrust EV code signing certificate](https://www.identrust.com/digital-certificates/trustid-ev-code-signing)

- [Sectigo (formerly Comodo) EV code signing certificate](https://www.sectigo.com/ssl-certificates-tls/code-signing)

- [SSL.com EV code signing certificate](https://www.ssl.com/certificates/ev-code-signing/)

## EV certificate signed drivers

To submit binaries for attestation signing, your Hardware Dev Center dashboard account must have at least one EV certificate associated with it. This requirement is also true if you want to submit binaries for Windows Hardware Lab Kit certification.

The following rules apply:

- Your registered EV certificate must be valid at the time of submission.

- Although Microsoft strongly recommends that you sign individual submissions with an EV certificate, you can sign submissions with an Authenticode signing certificate. The Authenticode certificate must be registered to your Partner Center account.

- All certificates must be SHA-2, and signed with the `/fd sha256` SignTool command line switch.

If you already have an approved EV certificate from a certificate authority, you can use it to establish a Partner Center account. If you don't have an EV certificate, choose [one the certificate authorities](#where-to-get-ev-code-signing-certificates) and follow their directions for purchase.

After the certificate authority verifies your contact information and your certificate purchase is approved, follow their directions to retrieve the certificate.
