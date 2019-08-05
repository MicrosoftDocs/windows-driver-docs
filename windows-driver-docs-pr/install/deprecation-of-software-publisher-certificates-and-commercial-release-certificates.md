---
title: Deprecation of Software Publisher Certificates and Commercial Release Certificates
description: Deprecation of Software Publisher Certificates and Commercial Release Certificates
ms.assetid: eafa4e20-94c5-49d6-a192-2fc7c9f1e64g
keywords:
- Trusted Root Certification Authorities certificate store WDK
- Trusted Publishers certificate store WDK
ms.date: 08/01/2019
ms.localizationpriority: medium
---

# Deprecation of Software Publisher Certificates and Commercial Release Certificates

The [Microsoft Trusted Root Program](https://docs.microsoft.com/security/trusted-root/program-requirements) no longer provides root certificates that have kernel mode signing capabilities.

For policy requirements, see [Windows 10 Kernel Mode Code Signing Requirements](https://docs.microsoft.com/security/trusted-root/program-requirements#f-windows-10-kernel-mode-code-signing-kmcs-requirements).

Existing root certificates with kernel mode code signing capabilities will continue working until expiration. The majority of these will expire in 2021, according to the following schedule:

|Common Name| Expiration date|
|-----------|---------------|
|VeriSign Class 3 Public Primary Certification Authority - G5		|2/22/2021|
|thawte Primary Root CA		                                        |2/22/2021|
|GeoTrust Primary Certification Authority		                    |2/22/2021|
|GeoTrust Primary Certification Authority - G3		                |2/22/2021|
|thawte Primary Root CA - G3		                                |2/22/2021|
|VeriSign Universal Root Certification Authority		            |2/22/2021|
|TC TrustCenter Class 2 CA II		                                |4/11/2021|
|COMODO RSA Certification Authority		                            |4/11/2021|
|UTN-USERFirst-Object		                                        |4/11/2021|
|DigiCert Assured ID Root CA		                                |4/15/2021|
|DigiCert High Assurance EV Root CA		                            |4/15/2021|
|DigiCert Global Root CA		                                    |4/15/2021|
|Entrust.net Certification Authority (2048)		                    |4/15/2021|
|GlobalSign Root CA		                                            |4/15/2021|
|Go Daddy Root Certificate Authority - G2		                    |4/15/2021|
|Starfield Root Certificate Authority - G2		                    |4/15/2021|
|NetLock Arany (Class Gold) Fotanúsítvány		                    |4/15/2021|
|NetLock Arany (Class Gold) Fotanúsítvány		                    |4/15/2021|
|NetLock Platina (Class Platinum) Fotanúsítvány		                |4/15/2021|
|Security Communication RootCA1		                                |4/15/2021|
|StartCom Certification Authority		                            |4/15/2021|
|Certum Trusted Network CA		                                    |4/15/2021|
|COMODO ECC Certification Authority		                            |4/11/2021|

## Frequently asked questions
* [What alternatives to cross signed certificates are available for testing drivers?](#what-alternatives-to-cross-signed-certificates-are-available-for-testing-drivers)
* [What will happen to my existing signed driver packages?](#what-will-happen-to-my-existing-signed-driver-packages)
* [Is there a way to run production driver packages without exposing it to Microsoft?](#is-there-a-way-to-run-production-driver-packages-without-exposing-it-to-microsoft)
* [Does every new version of my driver package need to be resubmitted to Hardware Dev Center?](#does-every-new-version-of-my-driver-package-need-to-be-resubmitted-to-hardware-dev-center)
* [Will we continue to be able to sign non-driver code with our existing 3rd party issued certificates after 2021?](#will-we-continue-to-be-able-to-sign-non-driver-code-with-our-existing-3rd-party-issued-certificates-after-2021)
* [Will I be able to continue using my EV certificate for signing submissions to Hardware Dev Center?](#will-i-be-able-to-continue-using-my-ev-certificate-for-signing-submissions-to-hardware-dev-center)
* [How do I know if my signing certificate will be impacted by these expirations?](#how-do-i-know-if-my-signing-certificate-will-be-impacted-by-these-expirations)
* [How can we automate Microsoft Test Signing to work with our build processes?](#how-can-we-automate-microsoft-test-signing-to-work-with-our-build-processes)
* [Starting in 2021, will Microsoft be the sole provider of production kernel mode code signatures?](#starting-in-2021,-will-microsoft-be-the-sole-provider-of-production-kernel-mode-code-signatures)
* [Hardware Dev Center doesn't provide driver signing for Windows XP, how can I have my drivers run in XP?](#hardware-dev-center-doesnt-provide-driver-signing-for-windows-xp-how-can-i-have-my-drivers-run-in-xp)

### What alternatives to cross signed certificates are available for testing drivers?

The following alternatives can be used:

- [MakeCert Process](makecert-test-certificate.md)
- [WHQL Test Signature Program](whql-test-signature-program.md)
- [Enterprise CA Process](enterprise-ca-test-certificate.md)

To use these options, you must enable [TESTSIGNING](the-testsigning-boot-configuration-option.md).

### What will happen to my existing signed driver packages? 

As long as driver packages are timestamped before the expiration date of the intermediate certificate, they will continue working.

### Is there a way to run production driver packages without exposing it to Microsoft? 

No, all production driver packages must be submitted to, and signed by Microsoft. 

### Does every new version of my driver package need to be resubmitted to Hardware Dev Center?

Yes, every time a driver package is rebuilt, it must be re-signed by Microsoft

### Will we continue to be able to sign non-driver code with our existing 3rd party issued certificates after 2021?

Yes, these certificates will continue to work until they expire. Code signed by these certificates will only be able to run in user mode, and will not be allowed to run in the kernel, unless it has a valid Microsoft signature.

### Will I be able to continue using my EV certificate for signing submissions to Hardware Dev Center?  

Yes, you can use a valid EV certificate to sign a submission package for Hardware Dev Center, but a driver package signed by an EV certificate no longer validates after the certificate's expiration date. 

### How do I know if my signing certificate will be impacted by these expirations? 

If your Cross Certificate Chain ends in `Microsoft Code Verification Root`, your signing certificate is affected. 

To view the cross certificate chain, run `signtool verify /v /kp <mydriver.sys>`. For example:

![[Finding Cross Certificate Chain]](images/signtoolcrosssigexample.png)

### How can we automate Microsoft Test Signing to work with our build processes?

Your build processes can call the [Hardware Dev Center API](../dashboard/dashboard-api.md). 

For samples that show usage, see the [Surface Dev Center Manager](https://github.com/Microsoft/SDCM) repository.

### Starting in 2021, will Microsoft be the sole provider of production kernel mode code signatures? 

Yes.

### Hardware Dev Center doesn't provide driver signing for Windows XP, how can I have my drivers run in XP?

Drivers can still be signed with a 3rd party issued code signing certificate. However, the certificate that signed the driver must be installed in the `Trusted Publisher` folder on the target computer. 
