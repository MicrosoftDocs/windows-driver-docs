---
title: Getting Started with Windows Drivers
description: Windows Drivers allow you to create one driver that will run on all Windows variants.
ms.date: 05/16/2022
---

# Getting Started with 'Windows Drivers'

When you write a driver to run on the Windows operating system, you have two basic choices. You can write a *Windows Desktop driver*, which *only* runs on Windows Desktop editions. Or, you can meet a few extra requirements and write a *Windows Driver*, which runs on both Desktop and non-Desktop variants of Windows. The *Windows Driver* classification extends and replaces the older *Universal Driver* classification.

The following additional requirements apply to Windows Drivers:

- Compliant with [DCH Design Principles](dch-principles-best-practices.md).
- Follow the principles of [Driver Package Isolation](driver-isolation.md).
- Follow [API Layering Requirements](api-layering.md).
- Certified with [Windows Hardware Compatibility Program Certification Process](/windows-hardware/design/compatibility/whcp-certification-process) using the [Hardware Lab Kit](/windows-hardware/test/hlk/). WHCP Certification Process requirements apply to both KMDF and UMDF drivers.

The following table summarizes the distinctions between the two classifications:

|     Feature                                                         |Windows Drivers|Windows Desktop Drivers |
| --------------------------------------------------------------------|:-------------:|:----------------------:|
| Runs on Windows Desktop                                              | Yes           | Yes                    |
| Runs on non-Desktop variants of Windows                              | Yes           | No                     |
| Must be certified with WHCP                                         | Yes           | No                     |
| WDK & HLK are primary vehicles for developing and certifying drivers| Yes           | Yes                    |
| Adhere to stricter reliability and serviceability requirements (e.g. driver package isolation)     | Yes           | No                     |

While it's not required for a driver running only on Windows Desktop to meet the additional requirements for a Windows Driver, doing so enhances driver serviceability and reliability, and also prepares the driver for possible future certification on non-Desktop variants of Windows.
