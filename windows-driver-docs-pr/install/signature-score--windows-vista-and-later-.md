---
title: Signature Score
description: Signature Score
keywords:
- signature score WDK device installations
ms.date: 12/03/2021
---

# Signature Score

This page describes the signature score for [driver packages](driver-packages.md). Signature score is one of three scores comprised in a driver package rank. Information on this page applies only to Windows Vista and later versions of the operating system.

A driver package rank is formatted as 0x*SSGGTHHH*, where the value of 0x*SS*000000 is the signature score, the value of 0x00*GG*0000 is the [feature score](feature-score--windows-vista-and-later-.md), and the value of 0x0000*THHH* is the [identifier score](identifier-score--windows-vista-and-later-.md).

The signature score ranks a driver package according to how the driver package is signed, as follows:

-   Windows assigns the best signature score (lowest signature score value) to driver packages that have a trusted signature. This includes the following:

    -   Premium WHQL signatures and standard WHQL signatures.
    -   Signatures for inbox driver packages.
    -   Windows Sustained Engineering (Windows SE) signatures.
    -   A third-party signature using Authenticode technology.  Valid third-party signature types include the following:
        -   Drivers signed by using a code signing certificate from an Enterprise Certificate Authority (CA).
        -   Drivers signed by using a code signing certificate issued by a Class 3 CA.
        -   Drivers signed by using a code signing certificate created by the [**MakeCert Tool**](../devtest/makecert.md).
-   Windows assigns the second best signature score to [driver packages](driver-packages.md) that do not have a valid signature, but the driver package is installed by an [**INF *DDInstall* section**](inf-ddinstall-section.md) that has an **.nt** platform extension.

    For more information about the **.nt** extension, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

-   Windows assigns the third best signature score to driver packages that do not have a valid signature, and the driver package is not installed by an INF *DDInstall* section that has an **.nt** platform extension.

-   Windows assigns the fourth and worst signature score (highest signature score value) to driver packages that are not signed or whose signing state is unknown.

For more information about driver ranking, see [How Windows Ranks Drivers](how-setup-ranks-drivers--windows-vista-and-later-.md).

 

