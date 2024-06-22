---
title: Getting Started with Windows Drivers
description: Windows Drivers allow you to create one driver that will run on all Windows variants.
ms.date: 06/21/2024
---

# Getting Started with 'Windows Drivers'

When you write a driver to run on the Windows operating system, you have three choices. You can write a *Desktop driver*, which *only* runs on Windows Desktop editions. Or, if your driver passes `infverif /u` and [ApiValidator](validating-windows-drivers#apivalidator), you can write a [*Universal Driver*](../install/using-a-universal-inf-file.md). If your driver passes `infverif /w`, which adds [Driver Package Isolation](../develop/driver-isolation.md), you can write a *Windows Driver*, which runs on both Desktop and non-Desktop variants of Windows. For info on configuring your build settings, see [Target Platforms](./target-platforms.md).

The following additional requirements apply to Windows Drivers:

- Compliant with [DCH Design Principles](dch-principles-best-practices.md).
- Follow the principles of [Driver Package Isolation](driver-isolation.md).
- Follow [API Layering Requirements](api-layering.md).

While it's not required for a driver running only on Windows Desktop to meet the additional requirements for a Universal Driver or Windows Driver, doing so enhances driver serviceability and reliability, and also prepares the driver for possible future certification on non-Desktop variants of Windows.
