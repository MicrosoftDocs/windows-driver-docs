---
title: Cross-Certificates for Kernel Mode Code Signing
description: This information describes how to obtain and use cross-certificates for code-signing kernel-mode binary files for Microsoft Windows.
ms.date: 04/20/2017
---

# Cross-Certificates for Kernel Mode Code Signing


This information describes how to obtain and use cross-certificates for code-signing kernel-mode binary files for Microsoft Windows.

> [!NOTE]
> Please review Microsoft Security Advisory ([2880823](/security-updates/SecurityAdvisories/2016/2880823)) "Deprecation of SHA-1 Hashing Algorithm for Microsoft Root Certificate Program" which describes a policy change wherein Microsoft will no longer allow root certificate authorities to issue X.509 certificates using the SHA-1 hashing algorithm for the purposes of SSL and code signing after January 1, 2016.

> [!NOTE]
> The [Microsoft Trusted Root Program](/security/trusted-root/program-requirements) no longer supports root certificates that have kernel mode signing capabilities. For more info, see [Deprecation of Software Publisher Certificates, Commercial Release Certificates, and Commercial Test Certificates](deprecation-of-software-publisher-certificates-and-commercial-release-certificates.md).

## Cross-Certificates Overview


A cross-certificate is a digital certificate issued by one Certificate Authority (CA) that is used to sign the public key for the root certificate of another Certificate Authority. Cross-certificates provide a means to create a chain of trust from a single, trusted, root CA to multiple other CAs.

In Windows, cross-certificates:

-   Allow the operating system kernel to have a single trusted Microsoft root authority.
-   Extend the chain of trust to multiple commercial CAs that issue Software Publisher Certificates (SPCs), which are used for code-signing software for distribution, installation, and loading on Windows

The cross-certificates that are provided here are used with the Windows Driver Kit (WDK) code-signing tools for properly signing kernel-mode software. Digitally signing kernel-mode software is similar to code-signing any software that is published for Windows. Cross-certificates are added to the digital signature by the developer or software publisher when signing the kernel-mode software. The cross-certificate itself is added by the code-signing tools to the digital signature of the binary file or catalog.

See [Authenticode Signing of Third-party CSPs](authenticode-signing-of-csps.md) for more information about how to use cross-certificates to sign third-party Cryptographic Service Providers (CSPs).

## Selecting the Correct Cross-certificate


Microsoft provides a specific cross-certificate for each CA that issues SPCs for code-signing kernel-mode code. The list below has a link to the correct cross-certificate for the root authority that issued your SPC.

Follow the steps below to identify your CA, and then download the related cross-certificate.

1.  Open the Microsoft Management Console (MMC) and add the Certificates snap-in:
    1.  Select the Start button, type “mmc” in the search box, and select mmc from the search results. If a User Account Control dialog box appears, select Yes.
    2.  From the MMC File menu, select Add/Remove Snap-in, …
    3.  Select the Certificates snap-in and select Add.
    4.  Select My user account and select Finish.
    5.  Select the Certificates snap-in again and select Add.
    6.  Select Computer account and select Next.
    7.  Select Local computer and select Finish.

2.  Locate your SPC in the certificate store, and then double-click it. Your certificate is listed in one of the following two locations, depending on how the certificate was installed.
    -   The Current User, Personal, Certificates store, or
    -   The Local Computer, Personal, Certificates store

3.  In the **Certificate** dialog box, select the **Certification Path** tab, and then select the top-most certificate in the certification path. This is the CA that is the issuing root authority for your SPC.
4.  View the root authority certificate by selecting the **View Certificate** button, and then select the **Details** tab of the new **Certificate** dialog box.
5.  Find the **Issuer** and **Thumbprint** for this certificate. Then locate the corresponding entry for this CA in the list below.
6.  Download the related cross-certificate for the CA and use this cross-certificate together with your SPC when digitally signing kernel-mode code

## Cross-Certificate List


The following list contains several new CAs that are currently supported by Microsoft for issuing SPCs for code-signing kernel-mode code.


|                              CA                              |                 Root certificate thumbprint                 |Expiration date|                         Download link                        |
| :----------------------------------------------------------: | :---------------------------------------------------------: | :-----------: | :---------------------------------------------------------: |
| AddTrust External CA Root                                    | a7 5a c6 57 aa 7a 4c df e5 f9 de 39 3e 69 ef ca b6 59 d2 50 | 2023/08/15    | [Download](https://go.microsoft.com/fwlink/p/?linkid=321790) |
| GoDaddy Class 2 Certification Authority                      | d9 61 24 72 ef 0f 27 87 e2 b2 d9 e0 63 a0 6b 32 fa 5e 33 3d | 2023/08/27    | [Download](https://go.microsoft.com/fwlink/p/?linkid=321791) |
| Starfield Class 2 Certification Authority                    | f8 fc 7f 3c dd 51 76 ad d2 7c f9 7f 73 96 59 09 46 6d 9a 22 | 2023/08/27    | [Download](https://go.microsoft.com/fwlink/p/?linkid=321792) |
| UTN-USERFirst-Object                                         | ae 1e 25 26 01 30 a3 0b 1b c2 20 29 35 65 3b e5 a7 23 be f5 | 2023/08/15    | [Download](https://go.microsoft.com/fwlink/p/?linkid=321793) |
 

