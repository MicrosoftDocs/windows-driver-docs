---
title: Overview of Device and Driver Installation
description: Overview of Device and Driver Installation
keywords:
- Device setup WDK device installations , about device installations
- device installations WDK , about device installations
- installing devices WDK , about device installations
ms.date: 10/16/2019
ms.localizationpriority: High
---

# Overview of Device and Driver Installation

The Windows operating system installs devices when the system restarts or when a user plugs in (or manually installs) a Plug and Play (PnP) device.

Specifically, Windows enumerates the devices that are present in the system and loads and calls the drivers for each device.

Drivers such as the ACPI driver and other PnP [bus drivers](../kernel/bus-drivers.md) help Windows determine which devices are present.

## In this section


-   [Step 1: The New Device is Identified](step-1--the-new-device-is-identified.md)
-   [Step 2: A Driver for the Device is Selected](step-2--a-driver-for-the-device-is-selected.md)
-   [Step 3: The Driver for the Device is Installed](step-3--the-driver-for-the-device-is-installed.md)
-   [Overview of the Driver Selection Process](overview-of-the-driver-selection-process.md)
