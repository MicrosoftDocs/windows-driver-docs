---
title: Overview of Device Property Pages
description: Overview of Device Property Pages
ms.assetid: b117721a-db32-4144-b0ae-5a0fca40f9db
---

# Overview of Device Property Pages


A *device property page* is a window that allows the user to view and edit the properties for a device. For most devices, the operating system provides standard device property pages that allow the user to view and edit a common set of parameters for that device. For more information about how property pages are displayed for a device, see [How Device Property Pages are Displayed](how-device-property-pages-are-displayed.md).

Independent hardware vendors (IHVs) typically provide custom device property pages that allow the user to view and edit additional and proprietary properties for a device. These properties are specific to each device that the IHV supplies. These properties might include default playback volume for a CD drive or speaker volume for a modem.

An IHV creates a custom device property page by using a property page provider. A property page provider can be one of the following:

<a href="" id="class-installers-and-co-installers"></a>**Class Installers and Co-installers**  
A co-installer or class installer can provide one or more custom device property pages by supporting the DIF\_ADDPROPERTYPAGE\_ADVANCED device installation function (DIF) code.

<a href="" id="property-page-extension-dll"></a>**Property Page Extension DLL**  
A dynamic-link library (DLL) that provides one or more custom device property pages is referred to as a *property page extension DLL*. This type of provider supports custom property pages by implementing the **AddPropSheetPageProc**, **ExtensionPropSheetPageProc**, and other property sheet callback functions.

For more information about these functions, see the Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0.

An IHV should supply a provider of custom device property pages in its driver package if its device or device class has any individual properties that a user can set.

**Note**  In versions of Windows earlier than Windows 2000, users set such information in Control Panel. Driver software that is written for Windows 2000 and later versions of Windows should provide property pages instead.

 

For more information about property page providers, see [Types of Device Property Page Providers](types-of-device-property-page-providers.md).

The Windows SDK for Windows 7 and .NET Framework 4.0 documentation provides comprehensive guidance about property pages and the Microsoft Win32 functions that manipulate them. For more information about property pages and property sheets, see [Property Sheet](http://go.microsoft.com/fwlink/p/?linkid=180781) in the Windows SDK for Windows 7 and .NET Framework 4.0 documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Overview%20of%20Device%20Property%20Pages%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




