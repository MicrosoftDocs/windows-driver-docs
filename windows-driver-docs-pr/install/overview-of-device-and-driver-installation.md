---
title: Overview of Device and Driver Installation
description: Overview of Device and Driver Installation
keywords:
- Device setup WDK device installations , about device installations
- device installations WDK , about device installations
- installing devices WDK , about device installations
ms.date: 11/18/2021
ms.localizationpriority: High
---

# Overview of Device Installation

The Windows operating system automatically installs devices without driver packages installed on them when those devices are reported to the operating system as present devices.  This happens for all present devices when the system is booting and happens when a user plugs in (or manually installs) a Plug and Play (PnP) device. Drivers such as the ACPI driver and other PnP [bus drivers](../kernel/bus-drivers.md) help Windows determine which devices are present.

The following steps go over parts of this process in more detail:

-   [Step 1: The New Device is Identified](step-1--the-new-device-is-identified.md)
-   [Step 2: A Driver for the Device is Selected](step-2--a-driver-for-the-device-is-selected.md)
-   [Step 3: The Driver for the Device is Installed](step-3--the-driver-for-the-device-is-installed.md)
-   [Overview of the Driver Selection Process](overview-of-the-driver-selection-process.md)
