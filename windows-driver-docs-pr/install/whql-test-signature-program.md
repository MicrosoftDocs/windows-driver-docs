---
title: WHQL Test Signature Program
description: WHQL test signature program
author: mhopkins-msft
ms.date: 09/12/2024
ms.author: mhopkins
keywords:
- driver signing WDK , WHQL digital signatures
- signing drivers WDK , WHQL digital signatures
- digital signatures WDK , WHQL
- signatures WDK , WHQL
- test signing drivers WDK , WHQL digital signatures
- WHQL digital signatures WDK
---

# WHQL test signature program

The Windows Hardware Quality Labs (WHQL) test signature program supports test-signing of drivers to be submitted for a [WHQL release signature](whql-release-signature.md). Independent hardware vendors (IHVs) participating in this program can submit [driver packages](driver-packages.md) to be test-signed.

Install a driver from a WHQL test-signed driver package by following these steps:

1. Disable secure boot on the computer. For instructions, see [Disable secure boot](#disable-secure-boot).

1. Set the [testsigning boot configuration option](the-testsigning-boot-configuration-option.md) on the test computer. See [Set the testsigning boot configuration option](#set-the-testsigning-boot-configuration-option).

1. Reboot the computer. Once rebooted, system displays a watermark in the bottom right corner of the screen indicating test mode, the Windows edition, and Windows build information.

1. Install the Hardware Developer Center (HDC) test-signed driver.

For information about how to obtain a WHQL test signature, send email to <winqual@microsoft.com> and include "Test Signature" in the subject line.

## Disable secure boot

1. Suspend BitLocker on the boot disk. BitLocker needs to be suspended before disabling secure boot in [UEFI](../bringup/uefi-in-windows.md). For more information, see [Suspend BitLocker protection for non-Microsoft software updates](/troubleshoot/windows-client/windows-security/suspend-bitlocker-protection-non-microsoft-updates).

1. Disable secure boot to install the WHQL test certificate. For more information, see [Disabling Secure Boot](/windows-hardware/manufacture/desktop/disabling-secure-boot).

## Set the testsigning boot configuration option

The Microsoft Test Root Authority is accepted when test-signing is enabled. Set the [testsigning boot configuration option](the-testsigning-boot-configuration-option.md) on the computer in which the test-signed driver package is to be installed. The test-signing option is enabled by following these steps:

1. Open an elevated command prompt window. To open an elevated command prompt window, create a desktop shortcut to cmd.exe, select, and hold (or right-click) the cmd.exe shortcut, and select **Run as administrator**.

1. In the elevated command prompt window, run the following commands to configure for test signed drivers and [reboot](/windows-server/administration/windows-commands/shutdown) the system:

   ```cmd
   bcdedit /set testsigning on
   shutdown /r /t 00
   ```
