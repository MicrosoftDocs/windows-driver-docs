---
title: Microsoft Bluetooth Test Platform Setup
description: How to set up the Microsoft Bluetooth Test Platform Setup 
ms.date: 06/09/2021
---

# Software Setup for BTP

## Software Setup

1. Download the [BTP software package](testing-BTP-software-package.md), which will install all required files to the `C:\BTP` directory.

2. Ensure [Secure boot](/windows-hardware/design/device-experiences/oem-secure-boot) is **disabled**.

3. Ensure BitLocker is **disabled**.

4. If using the Traduci:
    - plug it into the SUT.
    - From an elevated command line on the SUT, navigate to the `C:\BTP` directory and run `ConfigureMachineForBTP.bat` to configure the test machine. A reboot may be required.

6. Refer to [BTP tests](testing-BTP-Tests.md) for running test scripts in the package.
