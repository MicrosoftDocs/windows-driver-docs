---
title: WDF verification
description: WDF verification for Driver Verifier
ms.assetid: 9ee72369-878f-4710-a38b-1c93042178bd
keywords:
- WDF verification for Driver Verifier
ms.date: 
ms.localizationpriority: medium
---

# WDF Verification

WDF Verification checks if a kernel-mode driver is following the [Kernel-Mode Driver Framework (KMDF) requirements](https://docs.microsoft.com/windows-hardware/drivers/wdf/using-the-framework-to-develop-a-driver) properly.  

Failing this verification check will cause [bug check 0x10D: WDF_VIOLATION](https://docs.microsoft.com/windows-hardware/drivers/debugger/bug-check-0x10d---wdf-violation). 


### Activating this option:

You can activate port/miniport interface checking for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting driver verifier options](https://docs.microsoft.com/windows-hardware/drivers/devtest/selecting-driver-verifier-options). You must restart the computer to activate or deactivate the port/miniport interface checking option.

* **At the command line**

    At the command line, the port miniport interface checking is represented by **0x00100000**. For example:
    
    `verifier /flags 0x00100000 /driver MyDriver.sys`

    The feature will be active after the next boot.

* **Using Driver Verifier Manager**

1. Start Driver Verifier Manager. Type Verifier in a Command Prompt window.
2. Select Create custom settings (for code developers) and then click Next.
3. Select(check) Port miniport interface checking.
4. Restart the computer.
