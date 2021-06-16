---
title: Deprecation of Software Publisher Certificates, Commercial Release Certificates, and Commercial Test Certificates
description: Deprecation of Software Publisher Certificates, Commercial Release Certificates, and Commercial Test Certificates
keywords:
- Trusted Root Certification Authorities certificate store WDK
- Trusted Publishers certificate store WDK
ms.date: 08/01/2019
ms.localizationpriority: medium
---

# Deprecation of Software Publisher Certificates, Commercial Release Certificates, and Commercial Test Certificates

The [Microsoft Trusted Root Program](/security/trusted-root/program-requirements) no longer supports root certificates that have kernel mode signing capabilities.

For policy requirements, see [Windows 10 Kernel Mode Code Signing Requirements](/security/trusted-root/program-requirements#f-windows-10-kernel-mode-code-signing-kmcs-requirements).

Existing [cross-signed root certificates](cross-certificates-for-kernel-mode-code-signing.md) with kernel mode code signing capabilities will continue working until expiration.
As a result, all [software publisher certificates](software-publisher-certificate.md), [commercial release certificates](commercial-release-certificate.md), and [commercial test certificates](commercial-test-certificate.md) that chain back to these root certificates also become invalid on the same schedule.  To get your driver signed, first [Register for the Windows Hardware Dev Center program](../dashboard/register-for-the-hardware-program.md).

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
* [Will I be able to continue signing drivers if my certificate chains to a cross-cert that expires after 2021?](#will-i-be-able-to-continue-signing-drivers-with-a-certificate-that-chains-to-a-cross-cert-that-expires-after-july-1-2021)

### What is the expiration schedule of the trusted cross-certificates?

The majority of cross-signed root certificates will expire in 2021, according to the following schedule:

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

|Driver runs on| Drivers signed before July 1 2021 by| Driver signed on or after July 1 2021 by |
| - | - | - |
|Windows Server 2008 and later, Windows 7, Windows 8| WHQL or cross-signed drivers| WHQL or drivers cross-signed before July 1 2021|
|Windows 10| WHQL or attested | WHQL or attested |

If you have challenges signing your driver with WHQL, please report the specifics using one of the following:

* Use the Microsoft Collaborate portal, available through the [Microsoft Partner Center Dashboard](https://partner.microsoft.com/dashboard/collaborate), to create a feedback bug.
* Go to [Windows hardware engineering support](https://developer.microsoft.com/windows/hardware/support), select the **Contact us** tab, and in the **Developer support topic** dropdown, select **HLK/HCK**. Then select **Submit an incident**.

### Will I be able to continue signing drivers with a certificate that chains to a cross-cert that expires after July 1, 2021?

No, kernel-mode drivers must be signed with a WHQL signature after July 1st, 2021. You cannot use a certificate that chains to a cross-cert that expires after July 1, 2021 to sign kernel-mode drivers. Using these certificates to sign kernel-mode drivers after this date is a violation of the Microsoft Trusted Root Program (TRP) policy. Certificates in violation of Microsoft TRP policies will be revoked by the CA. Additional certificates may be present on the kernel-mode driver, however Windows ignores those signatures for the purpose of validating the driver.

## Related information

* [Register for the Hardware Program](../dashboard/register-for-the-hardware-program.md)
* [Software Publisher Certificate](software-publisher-certificate.md)
* [Commercial Release Certificate](commercial-release-certificate.md)
* [Commercial Test Certificate](commercial-test-certificate.md)
