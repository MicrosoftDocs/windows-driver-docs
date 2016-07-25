---
title: Types of Device Property Page Providers
description: Types of Device Property Page Providers
ms.assetid: b467543e-6907-44e5-b407-637cad7f6d78
---

# Types of Device Property Page Providers


You can supply custom device property pages by using the following types of property page providers:

-   **Class Installers and Co-installers.**

    A [co-installer](writing-a-co-installer.md) can provide one or more custom device property pages by supporting the [**DIF\_ADDPROPERTYPAGE\_ADVANCED**](https://msdn.microsoft.com/library/windows/hardware/ff543656) device installation function (DIF) code. When an installer that supplies property pages handles a **DIF\_ADDPROPERTYPAGE\_ADVANCED** request, it sets the address of a dialog box procedure for the property page.

    The co-installer that is part of the Toaster sample in the Windows Driver Kit (WDK) supports this type of device property page provider. It is located in the *src\\general\\toaster\\classinstaller* subdirectory of the WDK.

    For more information about the requirements for this type of provider, see [Specific Requirements for Device Property Page Providers (Co-Installers)](specific-requirements-for-device-property-page-providers--class-instal.md).

    **Note**  Although you can write a class installer that provides custom device property pages, it is generally better to provide this functionality in a co-installer, together with other device-specific or device-class-specific features.

     

-   **Property Page Extension DLL.**

    A DLL that provides one or more custom device property pages is referred to as a *property page extension DLL*. This type of provider supports custom property pages by implementing the **AddPropSheetPageProc, ExtensionPropSheetPageProc**, and other property sheet callback functions. For more information about these functions, see the Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0 documentation.

    This type of provider is installed by specifying an **EnumPropPages32** entry in the *add-registry-section* of an [**INF AddReg directive**](inf-addreg-directive.md). This directive is specified within a [**INF *DDInstall* section**](inf-ddinstall-section.md).

    The AC97 sample audio driver supports this type of device property page provider. It is located in the *src\\audio\\ac97* subdirectory of the WDK.

    For more information about the requirements for this type of provider, see [Specific Requirements for Device Property Page Providers (Property Page Extension DLLs)](specific-requirements-for-device-property-page-providers--property-pag.md).

    **Note**  Unless your [driver package](driver-packages.md) requires a class installer or co-installer, it is more efficient to support custom device property pages by using a property page extension DLL.

     

All types of device property page providers must follow the guidelines described in [General Requirements for Device Property Page Providers](general-requirements-for-device-property-page-providers.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Types%20of%20Device%20Property%20Page%20Providers%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




