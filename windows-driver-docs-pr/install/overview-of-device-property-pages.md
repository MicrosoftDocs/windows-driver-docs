---
title: Overview of Device Property Pages
description: Overview of Device Property Pages
ms.assetid: b117721a-db32-4144-b0ae-5a0fca40f9db
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Device Property Pages


A *device property page* is a window that allows the user to view and edit the properties for a device. For most devices, the operating system provides standard device property pages that allow the user to view and edit a common set of parameters for that device. For more information about how property pages are displayed for a device, see [How Device Property Pages are Displayed](how-device-property-pages-are-displayed.md).

Independent hardware vendors (IHVs) typically provide custom device property pages that allow the user to view and edit additional and proprietary properties for a device. These properties are specific to each device that the IHV supplies. These properties might include default playback volume for a CD drive or speaker volume for a modem.

An IHV creates a custom device property page by using a property page provider. A property page provider can be one of the following:

<a href="" id="class-installers-and-co-installers"></a>**Class Installers and Co-installers**  
A co-installer or class installer can provide one or more custom device property pages by supporting the DIF_ADDPROPERTYPAGE_ADVANCED device installation function (DIF) code.

<a href="" id="property-page-extension-dll"></a>**Property Page Extension DLL**  
A dynamic-link library (DLL) that provides one or more custom device property pages is referred to as a *property page extension DLL*. This type of provider supports custom property pages by implementing the **AddPropSheetPageProc**, **ExtensionPropSheetPageProc**, and other property sheet callback functions.

For more information about these functions, see the Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0.

An IHV should supply a provider of custom device property pages in its driver package if its device or device class has any individual properties that a user can set.

**Note**  In versions of Windows earlier than Windows 2000, users set such information in Control Panel. Driver software that is written for Windows 2000 and later versions of Windows should provide property pages instead.

 

For more information about property page providers, see [Types of Device Property Page Providers](types-of-device-property-page-providers.md).

The Windows SDK for Windows 7 and .NET Framework 4.0 documentation provides comprehensive guidance about property pages and the Microsoft Win32 functions that manipulate them. For more information about property pages and property sheets, see [Property Sheet](http://go.microsoft.com/fwlink/p/?linkid=180781) in the Windows SDK for Windows 7 and .NET Framework 4.0 documentation.

 

 





