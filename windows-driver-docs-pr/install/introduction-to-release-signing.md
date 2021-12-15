---
title: Introduction to Release-Signing
description: Introduction to Release-Signing
ms.date: 04/20/2017
---

# Introduction to Release-Signing


[Driver packages](driver-packages.md) should be release-signed for the following reasons:

-   To ensure the authenticity, integrity, and reliability of driver packages.

    Windows uses digital signatures to verify the identity of the publisher and to verify that the driver has not been altered since it was published.

-   To provide the best user experience by facilitating automatic driver installation.

    If a driver is not signed, the [Plug and Play (PnP) driver installation policy](digital-signatures-and-pnp-device-installation--windows-vista-and-late.md) requires that a system administrator manually authorize the installation of an unsigned driver, adding an extra step to the installation process. This extra step can be potentially confusing and bothersome to the average user.

-   To run kernel-mode drivers on 64-bit versions of Windows Vista and later versions of Windows.

    The [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) for 64-bit versions of Windows Vista and later requires that kernel-mode drivers be signed in order for the operating system to load the driver.

-   To play back certain types of next-generation premium content, all kernel-mode components in Windows Vista and later versions of Windows must be signed. In addition, all the user-mode and kernel-mode components in the Protected Media Path (PMP) must comply with PMP signing policy. For information about PMP signing policy, see the white paper [Code-signing for Protected Media Components in Windows Vista](/windows-hardware/test/hlk/).

The [Hardware Certification Kit (HCK)](/previous-versions/windows/hardware/hck/jj124227(v=vs.85)) has [test categories](/windows-hardware/test/hlk/) for a variety of device types. If a test category for the device type is included in this list, the driver publisher should obtain a [WHQL release signature](whql-release-signature.md) for the driver package.

**Note**  On Windows Server 2003, Windows XP, and Windows 2000, the INF file from the WHQL-signed [driver package](driver-packages.md) must use a [device setup class](./overview-of-device-setup-classes.md) that is defined in *%SystemRoot%/inf/Certclas.inf*. Otherwise, Windows treats the driver package as unsigned.

 

If a driver package is digitally-signed by WHQL, it can be distributed through the Windows Update program or other Microsoft-supported distribution mechanisms. WHQL signs the driver package [catalog file](catalog-files.md), but does not embed signatures in driver files. If a driver is a *boot-start driver* for 64-bit processors, the driver publisher must also [embed a signature](embedded-signatures-in-a-driver-file.md) in the kernel-mode driver files before submitting the driver package to WHQL.

If the [Hardware Certification Kit (HCK)](/previous-versions/windows/hardware/hck/jj124227(v=vs.85)) does not have a [test category](/windows-hardware/test/hlk/) for your device type, you must use the following types of digital signatures to [release-sign](/windows-hardware/drivers/install/deprecation-of-software-publisher-certificates-and-commercial-release-certificates) driver packages on Windows Vista and later versions of Windows:

-   To comply with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) of 64-bit versions of Windows Vista and later versions of Windows, you must use a [Software Publisher Certificate (SPC)](/windows-hardware/drivers/install/deprecation-of-software-publisher-certificates-and-commercial-release-certificates) to sign a kernel-mode driver package. For non-*boot-start drivers*, you only have to sign the driver package's [catalog file](catalog-files.md). For a boot-start driver, you must embed an SPC signature in a kernel-mode driver file and, optionally, also sign the driver package's catalog file.

-   To comply with the [PnP device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md) of 32-bit versions of Windows Vista and later versions of Windows, you can use either an SPC or a [commercial release certificate](/windows-hardware/drivers/install/deprecation-of-software-publisher-certificates-and-commercial-release-certificates) to sign a kernel-mode driver package's catalog file. These latter two signature types verify the authenticity and integrity of a driver, but unlike a WHQL release signature, do not verify the reliability of the driver.

An SPC and a commercial release certificate are collectively referred to as [release certificates](release-certificates.md) and a signature generated with a release certificate is referred to as a *release signature*.

For more information about the release-signing requirements and procedures, see [Release-Signing Driver Packages](/windows-hardware/drivers/install/deprecation-of-software-publisher-certificates-and-commercial-release-certificates).

**Note**  To understand the steps that are involved in release-signing driver packages, see [How to Release-Sign a Driver Package](how-to-release-sign-a-driver-package.md). This topic provides a summary of the release-signing process, and steps through many examples of release-signing by using the *ToastPkg* sample driver package within the Windows Driver Kit (WDK).

