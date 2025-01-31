---
title: Windows Driver Signing Tutorial
description: Provides an overview and details the steps to sign driver binaries for Windows.
ms.date: 01/31/2025
ai-usage: ai-assisted
---

# Windows driver signing tutorial

This tutorial provides an overview and details the steps to sign driver binaries for Windows in one consolidated location. The following subtopics describe the process:

- [Test Signing](test-signing.md)
- [Release Signing](release-signing.md)
- [Troubleshooting Driver Signing Installation](troubleshooting-driver-signing-installation.md)

## Overview

Windows requires all software running in kernel mode, including drivers, to be digitally signed in order to be loaded.

[Certify your driver with Microsoft](/windows-hardware/test/hlk/) and Microsoft provides a signature for it. When your driver package passes the certification tests, [Windows Hardware Quality Labs (WHQL)](./whql-release-signature.md) can sign it. If WHQL signs your driver package, you can distribute it through the Windows Update program or other Microsoft-supported distribution mechanisms.

> [!NOTE]
> The mandatory kernel-mode code-signing policy applies to all kernel-mode software for x64-based systems that are running on Windows Vista and later versions of Windows. However, Microsoft encourages publishers to digitally sign all kernel-mode software, including device drivers (user-mode drivers included) for 32-bit systems as well. Windows Vista and later versions of Windows, verify kernel-mode signatures on 32-bit systems. Software to support protected media content must be digitally signed even if it's 32-bit.

### User-Mode Driver Signing

User-mode drivers don't require digital signing but we recommend it for security purposes. Starting with Windows 8, there might be scenarios where signing is required, but signing isn't universally applicable.

- Microsoft recommends signing user-mode drivers to ensure integrity and security.
- Signing helps verify the vendor's identity and the integrity of the driver package.

User-mode drivers, like the printer driver install and work on an x64-based computer. A dialog appears to the user during installation asking for approval to install the driver. These driver packages must be signed for installation to proceed.

These resources describe driver signing in greater detail:

- The main [Driver Signing](driver-signing.md) article

- The subtopic "How to Release Sign a Kernel Module" in the [Kernel-Mode Code Signing Walkthrough](/previous-versions/windows/hardware/design/dn653569(v=vs.85)) describes what you should know about signing kernel-mode code. The information in the document also applies to signing user-mode drivers.

- The *selfsign_readme.htm* file located in the *selfsign* directory in your Windows Driver Kit (WDK) installation.
