---
title: Deprecation of Software Publisher Certificates, Commercial Release and Test Certificates
description: Deprecation of Software Publisher Certificates, Commercial Release Certificates, and Commercial Test Certificates
keywords:
- Trusted Root Certification Authorities certificate store WDK
- Trusted Publishers certificate store WDK
ms.date: 09/22/2021
ms.localizationpriority: medium
---

# Deprecation of Software Publisher Certificates, Commercial Release Certificates, and Commercial Test Certificates

> [!CAUTION] 
> The majority of cross-certificates expired in July 2021.
> You cannot use code signing certificates that chain to expired cross-certificates to create new kernel mode digital signatures for any version of Windows.

The [Microsoft Trusted Root Program](/security/trusted-root/program-requirements) no longer supports root certificates that have kernel mode signing capabilities.

For policy requirements, see [Windows 10 Kernel Mode Code Signing Requirements](/security/trusted-root/program-requirements#f-windows-10-kernel-mode-code-signing-kmcs-requirements).

Existing [cross-signed root certificates](cross-certificates-for-kernel-mode-code-signing.md) with kernel mode code signing capabilities will continue working until expiration. All software publisher certificates, commercial release certificates, and commercial test certificates that chain back to these root certificates also become invalid on the same schedule.

To get your driver signed, first [Register for the Windows Hardware Dev Center program](../dashboard/register-for-the-hardware-program.md).

## Frequently asked questions

* [What is the expiration schedule of the trusted cross-certificates?](#what-is-the-expiration-schedule-of-the-trusted-cross-certificates)
* [What alternatives to cross signed certificates are available for testing drivers?](#what-alternatives-to-cross-signed-certificates-are-available-for-testing-drivers)
* [What will happen to my existing signed driver packages?](#what-will-happen-to-my-existing-signed-driver-packages)
* [Is there a way to run production driver packages without exposing it to Microsoft?](#is-there-a-way-to-run-production-driver-packages-without-exposing-it-to-microsoft)
* [Does every new version of my driver package need to be resubmitted to Hardware Dev Center?](#does-every-new-production-version-of-a-driver-package-need-to-be-signed-by-microsoft)
* [Will we continue to be able to sign non-driver code with our existing 3rd party issued certificates after 2021?](#will-we-continue-to-be-able-to-sign-non-driver-code-with-our-existing-3rd-party-issued-certificates-after-2021)
* [Will I be able to continue using my EV certificate for signing submissions to Hardware Dev Center?](#will-i-be-able-to-continue-using-my-ev-certificate-for-signing-submissions-to-hardware-dev-center)
* [How do I know if my signing certificate will be impacted by these expirations?](#how-do-i-know-if-my-signing-certificate-will-be-impacted-by-these-expirations)
* [How can we automate Microsoft Test Signing to work with our build processes?](#how-can-we-automate-microsoft-test-signing-to-work-with-our-build-processes)
* [Starting in 2021, will Microsoft be the sole provider of production kernel mode code signatures?](#starting-in-2021-will-microsoft-be-the-sole-provider-of-production-kernel-mode-code-signatures)
* [Hardware Dev Center doesn't provide driver signing for Windows XP, how can I have my drivers run in XP?](#hardware-dev-center-doesnt-provide-driver-signing-for-windows-xp-how-can-i-have-my-drivers-run-in-xp)
* [How do production signing options differ by Windows version?](#how-do-production-signing-options-differ-by-windows-version)

### What is the expiration schedule of the trusted cross-certificates?

The majority of cross-signed root certificates expired in 2021, according to the following schedule:

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

### What alternatives to cross-signed certificates are available for testing drivers?

For all options below, the [TESTSIGNING boot option](the-testsigning-boot-configuration-option.md) must be enabled.

- [MakeCert Process](makecert-test-certificate.md)
- [WHQL Test Signature Program](whql-test-signature-program.md)
- [Enterprise CA Process](enterprise-ca-test-certificate.md)

For testing drivers at boot, see [How to Install a Test-signed Driver Required for Windows Setup and Boot](how-to-install-test-signed-driver-for-setup-and-boot.md).

For more info, see [Signing drivers during development and test](./introduction-to-test-signing.md).

### What will happen to my existing signed driver packages? 

As long as driver packages are timestamped before the expiration date of the leaf signing certificate, they will continue working.

### Is there a way to run production driver packages without exposing it to Microsoft? 

No, all production driver packages must be submitted to, and signed by Microsoft. 

### Does every new Production version of a driver package need to be signed by Microsoft?

Yes, every time a Production level driver package is rebuilt, it must be signed by Microsoft.

### Will we continue to be able to sign non-driver code with our existing 3rd party issued certificates after 2021?

Yes, these certificates will continue to work until they expire. Code which is signed using these certificates will only be able to run in user mode, and will not be allowed to run in the kernel, unless it has a valid Microsoft signature.

### Will I be able to continue using my EV certificate for signing submissions to Hardware Dev Center?  

Yes, EV certificates will continue to work until they expire. If you sign a kernel-mode driver with an EV certificate after the expiration of the cross-certificate that issued that EV certificate, the resulting driver will not load, run, or install.

### How do I know if my signing certificate will be impacted by these expirations? 

If your Cross Certificate Chain ends in `Microsoft Code Verification Root`, your signing certificate is affected. 

To view the cross certificate chain, run `signtool verify /v /kp <mydriver.sys>`. For example:

![[Finding Cross Certificate Chain.]](images/signtoolcrosssigexample.png)

### How can we automate Microsoft Test Signing to work with our build processes?

Your build processes can call the [Hardware Dev Center API](../dashboard/dashboard-api.md). 

For samples that show usage, see the [Surface Dev Center Manager](https://github.com/Microsoft/SDCM) repository.

### Starting in 2021, will Microsoft be the sole provider of production kernel mode code signatures? 

Yes.

### Hardware Dev Center doesn't provide driver signing for Windows XP, how can I have my drivers run in XP?

Drivers can still be signed with a 3rd party issued code signing certificate. However, the certificate that signed the driver must be imported into the `Local Computer Trusted Publishers` certificate store on the target computer. See [Trusted Publishers Certificate Store](trusted-publishers-certificate-store.md) for more information.

### How do production signing options differ by Windows version?

> [!WARNING]
> Cross-signing is no longer accepted for driver signing. Using cross certificates to sign kernel-mode drivers is a violation of the Microsoft Trusted Root Program (TRP) policy.
> Certificates in violation of Microsoft TRP policies will be revoked by the CA.

If your driver runs on Windows 7, 8, or 8.1, your driver must be signed through the Windows Hardware Compatibility Program. To get started, see [Create a new hardware submission](../dashboard/create-a-new-hardware-submission.md).

For Windows 10, use either WHCP or [attestation signing](../dashboard/attestation-signing-a-kernel-driver-for-public-release.md).

If you have challenges signing your driver with WHCP, please report the specifics using one of the following:

* Use the Microsoft Collaborate portal, available through the [Microsoft Partner Center Dashboard](https://partner.microsoft.com/dashboard/collaborate), to create a feedback bug.
* Go to [Windows hardware engineering support](https://developer.microsoft.com/windows/hardware/support), select the **Contact us** tab, and in the **Developer support topic** dropdown, select **HLK/HCK**. Then select **Submit an incident**.

## Related information

* [Register for the Hardware Program](../dashboard/register-for-the-hardware-program.md)
