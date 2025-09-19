---
title: Select Locales and Package Type in the Device Metadata Authoring Wizard
description: Select locales and package type in the Device Metadata Authoring Wizard
keywords:
- Select locales and package type in the Device Metadata Authoring Wizard
ms.date: 06/24/2025
ms.topic: how-to
---

# Select locales and package type in the Device Metadata Authoring Wizard

> [!IMPORTANT]
> Device metadata is deprecated and will be removed in a future release of Windows. For information about the replacement for this functionality, see **[Driver Package Container Metadata](../install/driver-package-container-metadata.md)**.

To begin, select the appropriate locale or locales of your metadata package, as well as your package type (Windows 7 or Windows 8).

## To set locale and package type

1. Click the **Package Definition** tab.
1. Under **Available locales**, select the ones that you want to associate with the metadata package.
    **Note**  
    This step is required for all metadata packages.

    For Windows 7 packages, the tool creates multiple single-locale device metadata packages. For Windows 8, it creates a single metadata package containing multiple locales.

1. Under **Locale Default**, do one of the following:
    - If you want the package to appear in a specific language when a package isn't available for a locale, select the desired language.
        > [!NOTE]
        >  You can only specify one metadata package as the Local Default package.

    - If you don't want the package to appear in a specific language when a locale-specific package isn't available, select **No default**.

1. At the bottom of the screen, select one or both of the following options:
    - Select **Windows 8 Package (multiple locales per package)** if the following criteria apply to you:
        - You can use the default device information in Windows 7 **Devices and Printers** in **Control Panel** in any display language (for example, English resources for all display languages).
        - You want to reduce the number of device metadata packages.
    - Select **Windows 7 style device metadata package (single locale per package)** if the following criteria apply to you:
        - You can't include another language's information in a given language's metadata package.
        - You want to differentiate the device information per locale in **Devices and Printers** in **Control Panel**.
