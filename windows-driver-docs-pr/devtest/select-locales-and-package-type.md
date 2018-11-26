---
title: Select locales and package type in the Device Metadata Authoring Wizard
description: Select locales and package type in the Device Metadata Authoring Wizard
ms.assetid: 02227FAB-A37F-4B20-AD52-E071C19E8743
keywords:
- Select locales and package type in the Device Metadata Authoring Wizard
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Select locales and package type in the Device Metadata Authoring Wizard


To begin, select the appropriate locale or locales of your metadata package, as well as your package type (Windows 7 or Windows 8).

### <span id="To_set_locale_and_package_type"></span><span id="to_set_locale_and_package_type"></span><span id="TO_SET_LOCALE_AND_PACKAGE_TYPE"></span>To set locale and package type

1.  Click the **Package Definition** tab.
2.  Under **Available locales**, select the ones that you want to associate with the metadata package.
    **Note**  
    This step is required for all metadata packages.

    For Windows 7 packages, the tool creates multiple single-locale device metadata packages. For Windows 8, it creates a single metadata package containing multiple locales.



3.  Under **Locale Default**, do one of the following:
    -   If you want the package to appear in a specific language when a package isn't available for a locale, select the desired language.
        **Note**  You can only specify one metadata package as the Local Default package.




-   If you don't want the package to appear in a specific language when a locale-specific package isn't available, select **No default**.


4.  At the bottom of the screen, select one or both of the following options:
    -   Select **Windows 8 Package (multiple locales per package)** if the following criteria apply to you:
        -   You can use the default device information in Windows 7 **Devices and Printers** in **Control Panel** in any display language (for example, English resources for all display languages).
        -   You want to reduce the number of device metadata packages.
    -   Select **Windows 7 style device metadata package (single locale per package)** if the following criteria apply to you:
        -   You can't include another language's information in a given language’s metadata package.
        -   You want to differentiate the device information per locale in **Devices and Printers** in **Control Panel**.









