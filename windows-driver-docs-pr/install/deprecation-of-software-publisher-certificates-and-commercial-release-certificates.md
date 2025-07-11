---
title: Certificate Deprecation - Publisher and Commercial
description: Learn about certificate deprecation for software publisher certificates, commercial release certificates, and commercial test certificates.
keywords:
- Trusted Root Certification Authorities certificate store WDK
- Trusted Publishers certificate store WDK
ms.date: 07/11/2025
---

# Deprecation of software publisher certificates, commercial release certificates, and commercial test certificates

> [!CAUTION] 
> Most cross-certificates expired in July 2021. You can't use code-signing certificates that chain with expired cross-certificates to create new kernel mode digital signatures for any version of Windows.

The [Microsoft Trusted Root Program](/security/trusted-root/program-requirements) no longer supports root certificates that have kernel mode signing capabilities.

For policy requirements, see [Windows 10 kernel mode code signing requirements]
(/security/trusted-root/program-requirements#f-windows-10-kernel-mode-code-signing-kmcs-requirements).

Existing [cross-signed root certificates](cross-certificates-for-kernel-mode-code-signing.md) with kernel-mode code-signing capabilities continue to work until expiration. All software publisher certificates, commercial release certificates, and commercial test certificates that chain back to these root certificates also become invalid on the same schedule.

To get your driver signed, first [Register for the Windows Hardware Dev Center program](../dashboard/hardware-program-register.md).

## Frequently asked questions

* [How can I find the expiration schedule of the trusted cross-certificates?](#how-can-i-find-the-expiration-schedule-of-the-trusted-cross-certificates)

* [Are there alternatives to cross-signed certificates for testing drivers?](#are-there-alternatives-to-cross-signed-certificates-for-testing-drivers)

* [How are my existing signed driver packages affected?](#how-are-my-existing-signed-driver-packages-affected)

* [Is there a way to run production driver packages without exposing it to Microsoft?](#is-microsoft-the-sole-provider-of-production-kernel-mode-code-signatures)

* [Does every new production version of a driver package require a Microsoft signature?](#does-every-new-production-version-of-a-driver-package-require-a-microsoft-signature)

* [Can I sign nondriver code with existing certificates issued by a third party?](#can-i-sign-non-driver-code-with-existing-certificates-issued-by-a-third-party)

* [Can I continue to use EV certificate for signing submissions to Hardware Dev Center?](#can-i-continue-to-use-ev-certificate-for-signing-submissions-to-hardware-dev-center)

* [How do I know if scheduled expirations can affect my signing certificate?](#how-do-i-know-if-scheduled-expirations-can-affect-my-signing-certificate)

* [How can I automate Microsoft Test Signing to work with my organization's build processes?](#how-can-i-automate-microsoft-test-signing-to-work-with-my-organizations-build-processes)

* [Is Microsoft the sole provider of production kernel-mode code signatures?](#is-microsoft-the-sole-provider-of-production-kernel-mode-code-signatures)

* [How can I have my drivers run in Windows XP when Hardware Dev Center doesn't provide driver signing?](#how-can-i-have-my-drivers-run-in-windows-xp-when-hardware-dev-center-doesnt-provide-driver-signing)

* [How do production signing options differ by Windows version?](#how-do-production-signing-options-differ-by-windows-version)

### How can I find the expiration schedule of the trusted cross-certificates?

All cross-signed trusted root certificates are now expired.

### Are there alternatives to cross-signed certificates for testing drivers?

The following procedures are available. For all methods, the [TESTSIGNING boot option](the-testsigning-boot-configuration-option.md) must be enabled.

* [MakeCert test certificate process](makecert-test-certificate.md)
* [Windows Hardware Quality Labs (WHQL) test signature program](whql-test-signature-program.md)
* [Enterprise CA test certificate](enterprise-ca-test-certificate.md)

For testing drivers at boot, see [How to install a test-signed driver required for Windows setup and boot](how-to-install-test-signed-driver-for-setup-and-boot.md).

For more information, see the [Introduction to signing drivers during development and test](introduction-to-test-signing.md).

### How are my existing signed driver packages affected?

As long as driver packages are timestamped before the expiration date of the leaf-signing certificate, the packages continue working.

### Is there a way to run production driver packages without exposing it to Microsoft?

No, all production driver packages must be submitted to, and signed by Microsoft. 

### Does every new production version of a driver package require a Microsoft signature?

Yes, every time a Production level driver package is rebuilt, Microsoft must sign the package.

### Can I sign nondriver code with existing certificates issued by a third party?

Yes, these certificates continue to work until they expire. Code signed by using these certificates runs only in user mode unless it has a valid Microsoft signature.

### Can I continue to use EV certificate for signing submissions to Hardware Dev Center?

Yes, extended validation (EV) certificates continue to work until they expire. If you sign a kernel-mode driver with an EV certificate after the issuing cross-certificate expires, the resulting driver doesn't load, run, or install.

### How do I know if scheduled expirations can affect my signing certificate?

If your cross certificate chain ends in `Microsoft Code Verification Root`, your signing certificate is affected. 

To view the cross certificate chain, run the `signtool verify /v /kp <mydriver.sys>` command. For example:

:::image type="content" source="images/signtoolcrosssigexample.png" border="false" alt-text="Screenshot that shows output from the sign tool command that identifies a cross-certificate chain.":::

### How can I automate Microsoft Test Signing to work with my organization's build processes?

Your build processes can call the [Hardware Dev Center API](../dashboard/dashboard-api.md). 

For samples that show usage, see the [Surface Dev Center Manager (SDCM)](https://github.com/Microsoft/SDCM) repository on GitHub.

### Is Microsoft the sole provider of production kernel-mode code signatures?

Yes.

### How can I have my drivers run in Windows XP when Hardware Dev Center doesn't provide driver signing?

Drivers can still be signed with a third-party issued code-signing certificate. However, the certificate that signed the driver must be imported into the `Local Computer Trusted Publishers` certificate store on the target computer. For more information, see [Trusted publishers certificate store](trusted-publishers-certificate-store.md).

### How do production signing options differ by Windows version?

[!include[Warning about deprecation of cross signing for driver signing](../includes/cross-signing-deprecation-warning.md)]

If your driver runs on Windows 7, 8, or 8.1, your driver must be signed through the Windows Hardware Compatibility Program. To get started, see [Create a new hardware submission](../dashboard/hardware-submission-create.md).

Starting in Windows 10, use either Windows Hardware Compatibility Program (WHCP) or [attestation signing](../dashboard/code-signing-attestation.md).

If you have challenges signing your driver with WHCP, report the specifics using one of the following options:

* Use the Microsoft Collaborate portal available through the [Microsoft Partner Center Dashboard](https://partner.microsoft.com/dashboard/collaborate) and create a feedback bug.

* Go to [Windows developer support](https://developer.microsoft.com/windows/support) and select the **Contact us** tab. In the **Technical support** box, next to **Driver Development and Testing/Certification**, select **Submit an incident**.

## Related articles

* [Register for the Hardware Program](../dashboard/hardware-program-register.md)
