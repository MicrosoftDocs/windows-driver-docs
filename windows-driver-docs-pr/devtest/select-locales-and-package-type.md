---
title: Select locales and package type in the Device Metadata Authoring Wizard
description: Select locales and package type in the Device Metadata Authoring Wizard
ms.assetid: 02227FAB-A37F-4B20-AD52-E071C19E8743
keywords: ["Select locales and package type in the Device Metadata Authoring Wizard"]
---

# Select locales and package type in the Device Metadata Authoring Wizard


To begin, select the appropriate locale or locales of your metadata package, as well as your package type (Windows 7 or Windows 8).

### <span id="To_set_locale_and_package_type"></span><span id="to_set_locale_and_package_type"></span><span id="TO_SET_LOCALE_AND_PACKAGE_TYPE"></span>To set locale and package type

1.  Click the **Package Definition** tab.
2.  Under **Available locales**, select the ones that you want to associate with the metadata package.
    **Note**  
    This step is required for all metadata packages.

    For Windows 7 packages, the tool creates multiple single-locale device metadata packages. For Windows 8, it creates a single metadata package containing multiple locales.

     

3.  Under **Locale Default**, do one of the following:
    -   If you want the package to appear in a specific language when a package isn't available for a locale, select the desired language.
        **Note**  You can only specify one metadata package as the Local Default package.

         

    -   If you don't want the package to appear in a specific language when a locale-specific package isn't available, select **No default**.

4.  At the bottom of the screen, select one or both of the following options:
    -   Select **Windows 8 Package (multiple locales per package)** if the following criteria apply to you:
        -   You can use the default device information in Windows 7 **Devices and Printers** in **Control Panel** in any display language (for example, English resources for all display languages).
        -   You want to reduce the number of device metadata packages.
    -   Select **Windows 7 style device metadata package (single locale per package)** if the following criteria apply to you:
        -   You can't include another language's information in a given language’s metadata package.
        -   You want to differentiate the device information per locale in **Devices and Printers** in **Control Panel**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\dma]:%20Select%20locales%20and%20package%20type%20in%20the%20Device%20Metadata%20Authoring%20Wizard%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




