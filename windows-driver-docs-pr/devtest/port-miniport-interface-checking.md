---
title: Port/Miniport Interface Checking
description: Port/Miniport interface checking
keywords:
- Port/Miniport interface checking
ms.date: 09/14/2017
---

# Port/miniport interface checking

Port/miniport interface checking enables Driver Verifier to inspect the DDI interface between PortCls.sys and its audio miniport drivers, along with ks.sys and its AVStream miniport drivers. See [Rules for AVStream drivers](./rules-for-avstream-drivers.md) and [Rules for audio drivers](./rules-for-audio-drivers.md)

### Activating this option:

You can activate port/miniport interface checking for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting driver verifier options](./selecting-driver-verifier-options.md). You must restart the computer to activate or deactivate the port/miniport interface checking option.

* **At the command line**

    At the command line, the port miniport interface checking is represented by **0x0x00010000 (Bit 16)**. For example:
    
    `verifier /flags 0x00010000 /driver MyDriver.sys`

    The feature will be active after the next boot.

* **Using Driver Verifier Manager**

1. Start Driver Verifier Manager. Type Verifier in a Command Prompt window.
2. Select Create custom settings (for code developers) and then click Next.
3. Select(check) Port miniport interface checking.
4. Restart the computer.
