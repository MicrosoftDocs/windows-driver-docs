---
title: Implementing a UI for Configuring sAPOs
description: Implementing a UI for Configuring sAPOs
ms.assetid: 52ce61fd-e5cf-4c84-885e-e46c7bfdad4a
---

# Implementing a UI for Configuring sAPOs


After you develop custom sAPOs, you must implement a user interface to configure the various system effects features that you have provided. The default Windows Vista user interface for system effects is implemented as a property page on a property sheet.

A property sheet is a window that allows the user to view and edit the properties of an item. A property sheet contains one or more overlapping child windows called property pages, each containing control windows for setting a group of related properties. Each page has a tab that the user can select to bring the page to the foreground of the property sheet.

You have the following two options for implementing your user interface.

-   If you wrap the system-supplied sAPOs with your custom sAPOs you will not be able to configure your custom features using the Windows Vista property page. In order to provide a way to configure your custom features, you have to replace the Windows Vista default property page. See the [Replacing the Default Property Page](replacing-the-default-property-page.md) topic for information about how to do this.

-   If you replace the system-supplied sAPOs with ones that you developed, you must provide a separate UI for configuring your sAPOs. See the [Custom UI Design Information](custom-ui-design-information.md) topic for details about how to do this.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Implementing%20a%20UI%20for%20Configuring%20sAPOs%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




