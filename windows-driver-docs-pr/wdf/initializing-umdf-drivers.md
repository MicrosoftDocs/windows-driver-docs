---
title: Initializing UMDF Drivers
description: Initializing UMDF Drivers
ms.assetid: b21ec019-1a80-4219-8aa8-3545ec3383b9
keywords:
- User-Mode Driver Framework WDK , initializing drivers
- UMDF WDK , initializing drivers
- user-mode drivers WDK UMDF , initializing
- initializing drivers WDK UMDF
- reflectors WDK UMDF
- loading reflectors WDK UMDF
- driver host process WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing UMDF Drivers


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

Before a UMDF driver for a device is initialized, the driver manager and the reflector are loaded by the operating system and the driver host process is created. To ensure that a device starts successfully, the driver manager is loaded and fully initialized by the time the reflector initializes.

When the device is installed, the Plug and Play (PnP) subsystem loads the reflector, if not already loaded. The reflector then contacts the driver manager to create the driver host process. The framework within the newly created driver host process then calls the [**IDriverEntry::OnInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff554900) method to initialize the UMDF driver, if not already initialized.

The framework adds a new device object for each device loaded in the driver host process. The following sections show an overview and provide details on how the framework adds a new device:

-   [Adding a Device Overview](adding-a-device-overview.md)
-   [Adding a Device](adding-a-device.md)

 

 





