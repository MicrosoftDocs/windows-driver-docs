---
title: Windows Driver Signing Tutorial
description: Provides an overview and details the steps to sign driver binaries for Windows
ms.date: 02/01/2023
---

# Windows Driver Signing Tutorial

This tutorial provides an overview and details the steps to sign driver binaries for Windows in one consolidated location. The following subtopics describe the process:

* [Test Signing](test-signing.md)
* [Release Signing](release-signing.md)
* [Troubleshooting Driver Signing Installation](troubleshooting-driver-signing-installation.md)

## Overview

Starting with Windows Vista, x64-based versions of Windows require all software running in kernel mode, including drivers, to be digitally signed in order to be loaded.

[Certify your driver with Microsoft](/windows-hardware/test/hlk/) and Microsoft will provide a signature for it. When your driver package passes the certification tests, it can be signed by [Windows Hardware Quality Labs (WHQL)](../dashboard/get-started-dashboard-submissions.md). If your driver package is signed by WHQL, it can be distributed through the Windows Update program or other Microsoft-supported distribution mechanisms.

**Note**  The mandatory kernel-mode code-signing policy applies to all kernel-mode software for x64-based systems that are running on Windows Vista and later versions of Windows. However, Microsoft encourages publishers to digitally sign all kernel-mode software, including device drivers (user-mode drivers included) for 32-bit systems as well. Windows Vista and later versions of Windows, verify kernel-mode signatures on 32-bit systems. Software to support protected media content must be digitally signed even if it is 32-bit.

User-mode drivers, like the Printer driver will install and work in an x64-based computer. A dialog will appear to the user during installation asking for approval to install the driver. Beginning in Windows 8 and later versions of Windows, installation will not proceed unless these driver packages are also signed.

The following resources describe Driver Signing in greater detail:

-   The main [Driver Signing](driver-signing.md) topic
-   The subtopic "How to Release Sign a Kernel Module" in the [Kernel-Mode Code Signing Walkthrough](/previous-versions/windows/hardware/design/dn653569(v=vs.85)) describes what you should know about signing kernel-mode code. The information in the document also applies to signing user-mode drivers.
-   The selfsign_readme.htm file in the Windows 7 WDK is located in the WDK install directory, \\WinDDK\\7600.16385.1\\src\\general\\build\\driversigning. This directory also has a command file, selfsign_example.cmd, which can be edited to run the driver signing commands. The selfsign_readme.htm file in the Windows 8.1 WDK is located at C:\\Program Files (x86)\\Windows Kits\\8.1\\bin\\selfsign, and provides links to additional driver signing information.
