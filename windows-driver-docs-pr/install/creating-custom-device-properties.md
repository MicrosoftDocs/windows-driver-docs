---
title: Creating Custom Device Properties
description: Creating Custom Device Properties
ms.assetid: e18fcbe8-6083-451e-b1be-5a543b61c627
keywords:
- device properties WDK device installations , creating custom
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Custom Device Properties


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) supports creation of custom device property categories for device instances, [device setup classes](device-setup-classes.md), device interface classes, and device interfaces. A custom property can be accessed by calling the appropriate [SetupAPI property function](https://msdn.microsoft.com/library/windows/hardware/ff541483). A custom device property can also be modified by using an [**INF AddProperty directive**](inf-addproperty-directive.md) or an [**INF DelProperty directive**](inf-delproperty-directive.md).

For more information about custom device properties, see the following topics:

[Creating Custom Device Property Categories](#creating-custom-device-property-categories)

[Using the SetupAPI Property Functions to Access Custom Device Properties](#using-the-setupapi-property-functions-to-access-custom-device-properti)

[Using the INF AddProperty Directive or the INF DelProperty Directive to Modify a Custom Device Property](#using-the-inf-addproperty-directive-or-the-inf-delproperty-directive-t)

### <a href="" id="creating-custom-device-property-categories"></a> Creating Custom Device Property Categories

A custom device property category is a logically-related collection of custom device properties. To programmatically create a custom device property category, use the [**DEFINE_DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff541072) macro to create the property keys that represent the properties in the property category, as follows:

-   Create a unique GUID value that represents the property category and set the GUID value of each property key to this unique GUID value. For information about how to create a new GUID value, see [Defining and Exporting New GUIDs](https://msdn.microsoft.com/library/windows/hardware/ff542998).

    **Note**  The system-defined property categories are reserved for operating system use only.

     

-   Set the property identifier of each property key to an integer value that is unique within the property category and that is greater than or equal to two.

You can also create a custom device property category for a device instance by using an [**INF AddProperty directive**](inf-addproperty-directive.md).

### <a href="" id="using-the-setupapi-property-functions-to-access-custom-device-properti"></a> Using the SetupAPI Property Functions to Access Custom Device Properties

Access custom device properties in the same manner as described in [Using SetupAPI to Access Device Properties (Windows Vista and Later)](using-setupapi-to-access-device-properties--windows-vista-and-later-.md). The following additional considerations apply when you access custom device properties:

-   The **SetupDiGetXxxPropertyKeys** and **SetupDiGetXxxPropertyKeysEx** functions retrieve the system-defined device property keys and custom device property keys that represent properties that are set for a component.

-   The **SetupDiSetXxxProperty** functions set a custom device property for a component. Windows internally associates the custom device property key, the property data type, and the property value. If a custom device property with the same property key is already set, the **SetupDiSetXxxProperty** function overwrites the property value and property data type that is associated with the property.

-   The **SetupDiGetXxxProperty** functions retrieve a custom device property that is set for a component. The **SetupDiGetXxxProperty** function retrieves the property value and the property data type that were set when the property was set.

### <a href="" id="using-the-inf-addproperty-directive-or-the-inf-delproperty-directive-t"></a> Using the INF AddProperty Directive or the INF DelProperty Directive to Modify a Custom Device Property

To modify a custom device property by using an [**INF AddProperty directive**](inf-addproperty-directive.md), include an AddProperty directive in the section that installs the component and supply the following entries for the property:

-   The *property-category-guid* entry that represents the custom device property category

-   A property identifier entry that identifies the property within the custom device property category

-   The *value* entry of a new device property or the *value* entry that modifies an existing device property value

Use the [**INF DelProperty directive**](inf-delproperty-directive.md) to delete a custom device property.

For more information about how to use these directives, see the [Using the INF AddProperty Directive and the INF DelProperty Directive](using-the-inf-addproperty-directive-and-the-inf-delproperty-directive.md).

 

 





