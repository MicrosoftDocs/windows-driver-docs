---
title: Creating Custom Device Properties
description: Creating Custom Device Properties
keywords:
- device properties WDK device installations , creating custom
ms.date: 04/04/2022
---

# Creating Custom Device Properties

In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) supports creation of custom device property categories for device instances, [device setup classes](./overview-of-device-setup-classes.md), [device interface classes](overview-of-device-interface-classes.md), and device interfaces. A custom property can be accessed by calling the appropriate [property function](accessing-properties.md). A custom device property can also be modified from a [driver package](driver-packages.md) by using an [**INF AddProperty directive**](inf-addproperty-directive.md) or an [**INF DelProperty directive**](inf-delproperty-directive.md).

For more information about custom device properties, see the following sections:

[Creating Custom Device Property Categories](#creating-custom-device-property-categories)

[Using Property Functions to Access Custom Device Properties](#using-property-functions-to-access-custom-device-properties)

[Using the INF AddProperty Directive or the INF DelProperty Directive to Modify a Custom Device Property](#using-the-inf-addproperty-directive-or-the-inf-delproperty-directive-to-modify-a-custom-device-property)

## Creating Custom Device Property Categories

A custom device property category is a logically-related collection of custom device properties. To programmatically create a custom device property category, use the [**DEFINE_DEVPROPKEY**](./define-devpropkey.md) macro to create the property keys that represent the properties in the property category, as follows:

-   Create a unique GUID value that represents the property category and set the GUID value of each property key to this unique GUID value. For information about how to create a new GUID value, see [Defining and Exporting New GUIDs](../kernel/defining-and-exporting-new-guids.md).

    > [!NOTE]
    > The system-defined property categories are reserved for operating system use only.

-   Set the property identifier of each property key to an integer value that is unique within the property category and that is greater than or equal to two.

You can also create a custom device property category for a device instance by using an [**INF AddProperty directive**](inf-addproperty-directive.md).

## Using Property Functions to Access Custom Device Properties

Access custom device properties in the same manner as described in [Accessing Properties)](accessing-properties.md).

## Using the INF AddProperty Directive or the INF DelProperty Directive to Modify a Custom Device Property

To modify a custom device property by using an [**INF AddProperty directive**](inf-addproperty-directive.md), include an AddProperty directive in the section that installs the component and supply the following entries for the property:

-   The *property-category-guid* entry that represents the custom device property category

-   A property identifier entry that identifies the property within the custom device property category

-   The *value* entry of a new device property or the *value* entry that modifies an existing device property value

Use the [**INF DelProperty directive**](inf-delproperty-directive.md) to delete a custom device property.

For more information about how to use these directives, see the [Using the INF AddProperty Directive and the INF DelProperty Directive](using-the-inf-addproperty-directive-and-the-inf-delproperty-directive.md).

 

