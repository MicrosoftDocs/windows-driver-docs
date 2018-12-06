---
title: Cross-Certificates for Kernel Mode Code Signing
description: This information describes how to obtain and use cross-certificates for code-signing kernel-mode binary files for Microsoft Windows.
ms.assetid: 0A1364BF-04DA-4F1C-803A-18FE2A5EF390
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Cross-Certificates for Kernel Mode Code Signing


This information describes how to obtain and use cross-certificates for code-signing kernel-mode binary files for Microsoft Windows.

**Note**  Please also review Microsoft Security Advisory ([2880823](https://technet.microsoft.com/library/security/2880823)) "Deprecation of SHA-1 Hashing Algorithm for Microsoft Root Certificate Program" which describes a policy change wherein Microsoft will no longer allow root certificate authorities to issue X.509 certificates using the SHA-1 hashing algorithm for the purposes of SSL and code signing after January 1, 2016.

 

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
    1.  Click the Start button, type “mmc” in the search box, and press return. If a User Account Control dialog box appears, click Yes.
    2.  From the MMC File menu, select Add/Remove Snap-in, …
    3.  Select the Certificates snap-in and click Add.
    4.  Select My user account and click Finish.
    5.  Select the Certificates snap-in again and click Add.
    6.  Select Computer account and click Next.
    7.  Select Local computer and click Finish.

2.  Locate your SPC in the certificate store, and then double-click it. Your certificate is listed in one of the following two locations, depending on how the certificate was installed.
    -   The Current User, Personal, Certificates store, or
    -   The Local Computer, Personal, Certificates store

3.  In the **Certificate** dialog box, click on the **Certification Path** tab, and then select the top-most certificate in the certification path. This is the CA that is the issuing root authority for your SPC.
4.  View the root authority certificate by clicking the **View Certificate** button, and then click the **Details** tab of the new **Certificate** dialog box.
5.  Find the **Issuer** and **Thumbprint** for this certificate. Then locate the corresponding entry for this CA in the list below.
6.  Download the related cross-certificate for the CA and use this cross-certificate together with your SPC when digitally signing kernel-mode code

## Cross-Certificate List


The following list contains all of the CAs that are currently supported by Microsoft for issuing SPCs for code-signing kernel-mode code.

|                              CA                              |                 Root certificate thumbprint                 |                        Download link                        |
| :----------------------------------------------------------: | :---------------------------------------------------------: | :---------------------------------------------------------: |
| Certum Trusted Network CA                                    | 55 43 55 15 fd d2 48 65 75 fd c5 cf 3b ad 00 c9 13 12 3d 03 | [Download](http://go.microsoft.com/fwlink/p/?linkid=321770) |
| DigiCert Assured ID Root CA                                  | ba 3e a5 4d 72 c1 45 d3 7c 25 5e 1e a4 0a fb c6 33 48 b9 6e | [Download](http://go.microsoft.com/fwlink/p/?linkid=321771) |
| DigiCert Global Root CA                                      | c9 83 39 19 f1 f3 6a 63 48 11 1e 93 02 6f d4 0e b9 6f bc 34 | [Download](http://go.microsoft.com/fwlink/p/?linkid=321772) |
| DigiCert High Assurance EV Root CA                           | 2f 25 13 af 39 92 db 0a 3f 79 70 9f f8 14 3b 3f 7b d2 d1 43 | [Download](http://go.microsoft.com/fwlink/p/?linkid=321773) |
| Entrust.net Certification Authority (2048)                   | 00 a3 e6 00 9e aa 73 9b 3d ee f4 b5 06 64 9d 8a 1a 7a d3 3a | [Download](http://go.microsoft.com/fwlink/p/?linkid=321774) |
| Entrust Root Certification Authority – G2                    | ‎d8 fc 24 87 48 58 5e 17 3e fb fb 30 75 c4 b4 d6 0f 9d 8d 08 | [Download](http://go.microsoft.com/fwlink/p/?LinkId=624811) |
| GeoTrust Primary Certification Authority                     | e8 6e 80 82 99 0e 3d fa ed 81 6d 9e b1 72 0f 91 a4 f1 a1 85 | [Download](http://go.microsoft.com/fwlink/p/?linkid=321775) |
| GeoTrust Primary Certification Authority – G3                | b2 bb bd fa c8 f1 a8 ad 58 95 cd 49 38 4b 22 ca 19 db 2d 1f | [Download](http://go.microsoft.com/fwlink/p/?linkid=321776) |
| GlobalSign Root CA                                           | cc 1d ee bf 6d 55 c2 c9 06 1b a1 6f 10 a0 bf a6 97 9a 4a 32 | [Download](http://go.microsoft.com/fwlink/p/?linkid=321777) |
| Go Daddy Root Certificate Authority – G2                     | 84 2c 5c b3 4b 73 bb c5 ed 85 64 bd ed a7 86 96 7d 7b 42 ef | [Download](http://go.microsoft.com/fwlink/p/?linkid=321778) |
| NetLock Arany (Class Gold)                                   | 89 4f 1d 28 97 aa 4c 07 4d cd 85 c5 fc 09 ee 73 b9 51 04 d8 | [Download](http://go.microsoft.com/fwlink/p/?linkid=321779) |
| NetLock Platina (Class Platinum)                             | 97 dd 74 97 16 20 57 29 41 dc 80 0c 2f d8 0a 48 07 7d 10 b0 | [Download](http://go.microsoft.com/fwlink/p/?linkid=321780) |
| Security Communication RootCA1                               | 41 f2 8c e5 6f d8 b9 cb 46 7f b5 03 2a 3c ae 1c dc 9d 86 48 | [Download](http://go.microsoft.com/fwlink/p/?linkid=321781) |
| Starfield Root Certificate Authority – G2                    | 40 c2 0a 9a 33 fa d0 36 ac bf e8 2d 6c bb ee 1b 42 9b 86 de | [Download](http://go.microsoft.com/fwlink/p/?linkid=321782) |
| StartCom Certification Authority                             | e6 06 9e 04 8d ea 8d 81 7a fc 41 88 b1 be f1 d8 88 d0 af 17 | [Download](http://go.microsoft.com/fwlink/p/?linkid=321783) |
| TC TrustCenter Class 2 CA II                                 | 42 62 ff 7d 89 70 66 aa e7 75 80 d3 3a d2 88 03 f9 a1 1a 62 | [Download](http://go.microsoft.com/fwlink/p/?linkid=321784) |
| Thawte Primary Root CA                                       | 55 38 e9 fe c1 40 30 b7 40 15 23 49 e1 15 a1 16 5d 29 07 4a | [Download](http://go.microsoft.com/fwlink/p/?linkid=321785) |
| Thawte Primary Root CA – G3                                  | ba 57 ca 5e 78 dd 2d 1d 74 76 ae be e9 95 3e 39 6f d0 55 46 | [Download](http://go.microsoft.com/fwlink/p/?linkid=321786) |
| VeriSign Class 3 Public Primary Certification Authority – G5 | 57 53 4c cc 33 91 4c 41 f7 0e 2c bb 21 03 a1 db 18 81 7d 8b | [Download](http://go.microsoft.com/fwlink/p/?linkid=321787) |
| VeriSign Universal Root Certification Authority              | 9e d8 cd 56 01 f0 10 56 51 eb bb 3f 57 f0 31 82 e5 fa 7e 01 | [Download](http://go.microsoft.com/fwlink/p/?linkid=321788) |

## New Cross-Certificate List


The following list contains several new CAs that are currently supported by Microsoft for issuing SPCs for code-signing kernel-mode code.


|                              CA                              |                 Root certificate thumbprint                 |                        Download link                        |
| :----------------------------------------------------------: | :---------------------------------------------------------: | :---------------------------------------------------------: |
| AddTrust External CA Root                                    | a7 5a c6 57 aa 7a 4c df e5 f9 de 39 3e 69 ef ca b6 59 d2 50 | [Download](http://go.microsoft.com/fwlink/p/?linkid=321790) |
| GoDaddy Class 2 Certification Authority                      | d9 61 24 72 ef 0f 27 87 e2 b2 d9 e0 63 a0 6b 32 fa 5e 33 3d | [Download](http://go.microsoft.com/fwlink/p/?linkid=321791) |
| Starfield Class 2 Certification Authority                    | f8 fc 7f 3c dd 51 76 ad d2 7c f9 7f 73 96 59 09 46 6d 9a 22 | [Download](http://go.microsoft.com/fwlink/p/?linkid=321792) |
| UTN-USERFirst-Object                                         | ae 1e 25 26 01 30 a3 0b 1b c2 20 29 35 65 3b e5 a7 23 be f5 | [Download](http://go.microsoft.com/fwlink/p/?linkid=321793) |
 

 





