---
title: Implementing a UI for Configuring sAPOs
description: Implementing a UI for Configuring sAPOs
ms.assetid: 52ce61fd-e5cf-4c84-885e-e46c7bfdad4a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementing a UI for Configuring sAPOs


After you develop custom sAPOs, you must implement a user interface to configure the various system effects features that you have provided. The default Windows Vista user interface for system effects is implemented as a property page on a property sheet.

A property sheet is a window that allows the user to view and edit the properties of an item. A property sheet contains one or more overlapping child windows called property pages, each containing control windows for setting a group of related properties. Each page has a tab that the user can select to bring the page to the foreground of the property sheet.

You have the following two options for implementing your user interface.

-   If you wrap the system-supplied sAPOs with your custom sAPOs you will not be able to configure your custom features using the Windows Vista property page. In order to provide a way to configure your custom features, you have to replace the Windows Vista default property page. See the [Replacing the Default Property Page](replacing-the-default-property-page.md) topic for information about how to do this.

-   If you replace the system-supplied sAPOs with ones that you developed, you must provide a separate UI for configuring your sAPOs. See the [Custom UI Design Information](custom-ui-design-information.md) topic for details about how to do this.

 

 




