---
title: Types of Device Property Page Providers
description: Types of Device Property Page Providers
ms.date: 03/11/2022
---

# Types of Device Property Page Providers

You can supply custom device property pages by using the following types of property page providers:

-   **Property Page Extension DLL.**

    A DLL that provides one or more custom device property pages is referred to as a *property page extension DLL*. This type of provider supports custom property pages by implementing the **AddPropSheetPageProc, ExtensionPropSheetPageProc**, and other property sheet callback functions. For more information about these functions, see the Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0 documentation.

    This type of provider is installed by specifying an **EnumPropPages32** entry in the *add-registry-section* of an [**INF AddReg directive**](inf-addreg-directive.md). This directive is specified within a [**INF *DDInstall* section**](inf-ddinstall-section.md).

    The AC97 sample audio driver supports this type of device property page provider. It is located in the *src\\audio\\ac97* subdirectory of the WDK.

    For more information about the requirements for this type of provider, see [Specific Requirements for Device Property Page Providers (Property Page Extension DLLs)](specific-requirements-for-device-property-page-providers--property-pag.md).

    **Note**  Unless your [driver package](driver-packages.md) requires a class installer or co-installer, it is more efficient to support custom device property pages by using a property page extension DLL.

-   **Class Installers and Co-installers.**

    A [co-installer](writing-a-co-installer.md) can provide one or more custom device property pages by supporting the [**DIF_ADDPROPERTYPAGE_ADVANCED**](./dif-addpropertypage-advanced.md) device installation function (DIF) code. When an installer that supplies property pages handles a **DIF_ADDPROPERTYPAGE_ADVANCED** request, it sets the address of a dialog box procedure for the property page.

    The co-installer that is part of the Toaster sample in the Windows Driver Kit (WDK) supports this type of device property page provider. It is located in the *src\\general\\toaster\\classinstaller* subdirectory of the WDK.

    For more information about the requirements for this type of provider, see [Specific Requirements for Device Property Page Providers (Co-Installers)](specific-requirements-for-device-property-page-providers--class-instal.md).

    **Note**  While it is possible to provide a device property page via a class installer or co-installer, it is not recommended. Class installers and co-installers are deprecated.

All types of device property page providers must follow the guidelines described in [General Requirements for Device Property Page Providers](general-requirements-for-device-property-page-providers.md).

 

