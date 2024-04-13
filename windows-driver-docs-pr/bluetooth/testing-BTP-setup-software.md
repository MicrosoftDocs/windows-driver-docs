---
title: Bluetooth Test Platform Software Setup
description: How to set up the Microsoft Bluetooth Test Platform software
ms.date: 01/10/2024
---

# Bluetooth Test Platform software setup

1. Download the [BTP setup package](testing-BTP-setup-package.md), which will install all required files to the `C:\BTP` directory.

1. Ensure [Secure boot](/windows-hardware/design/device-experiences/oem-secure-boot) is **disabled**.

1. Ensure BitLocker is **disabled**.

1. If using the Traduci, plug it into the SUT before doing step 5.

1. From an elevated command line on the SUT, navigate to the `C:\BTP` directory and run `ConfigureMachineForBTP.bat` to configure the test machine. A reboot may be required.

1. Refer to [BTP tests](testing-BTP-Tests.md) for running test scripts in the package.
