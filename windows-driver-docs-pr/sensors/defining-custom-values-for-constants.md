---
title: Defining custom values for sensor constants
description: Defining custom values for sensor constants
ms.assetid: 0ed635c2-117d-4a49-a565-31e5a0a9861d
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Defining custom values for sensor constants


You can define custom values for categories, sensor types, data fields, properties, and events.

## Guidelines for Custom Values

Avoid defining new constants if a set of platform-defined constants will work. Study and understand the categories, types, data fields, properties, and events described in the [Constants](https://msdn.microsoft.com/library/windows/hardware/ff545409) reference section and decide whether your sensor driver fits into the platform framework.

If you choose to define custom values, follow these guidelines:

-   Generate new PROPERTYKEYs. Do not reuse GUIDs from platform-defined constants and do not base your new GUIDs on platform-defined base values.

-   Use identical GUIDs for new sensor data types in the same sensor category. To make each data type unique, increment the PID part of the property key.

-   Use identical GUIDs for new sensor properties that you define for your sensor. To make each property unique, increment the PID part of the property key.

-   Use identical GUIDs for new sensor event type that you define for your sensor. To make each event type unique, increment the PID part of the property key.

-   Create unique constants. To avoid conflicts between constant names, begin each custom name with a value that helps make the name unique, both within the sensor code and across other implementations. For example, a company named Fabrikam could begin each constant definition with `FABRIKAM_`.

-   Document and publish the values. If you want developers to be able to access the data from your sensor through the Windows Sensor API or Location API, you must document your custom values and publish the constants, for example by providing a header file. If your sensor is part of a proprietary system, publishing the custom values is not required.

## Example

The following code example shows how to define custom values for sensor constants. The example creates a new category, sensor type, and data types for a sample sensor that provides the current local time. You can imagine such a sensor receiving time information from a reference clock through satellite or other radio transmissions.

```cpp
// Define a sensor ID.
// {0D77BEE3-7169-42bf-8379-28F9A9B59A57}
DEFINE_GUID(SAMPLE_SENSOR_TIME_ID,
0xd77bee3, 0x7169, 0x42bf, 0x83, 0x79, 0x28, 0xf9, 0xa9, 0xb5, 0x9a, 0x57);

// Define a custom category.
// {062A5C3B-44C1-4ad1-8EFC-0F65B2E4AD48}
DEFINE_GUID(SAMPLE_SENSOR_CATEGORY_DATE_TIME,
0x62a5c3b, 0x44c1, 0x4ad1, 0x8e, 0xfc, 0xf, 0x65, 0xb2, 0xe4, 0xad, 0x48);

// Define a custom type.
// {5F199A84-409F-4e35-B2DD-F9C79F5318A0}
DEFINE_GUID(SAMPLE_SENSOR_TYPE_TIME,
0x5f199a84, 0x409f, 0x4e35, 0xb2, 0xdd, 0xf9, 0xc7, 0x9f, 0x53, 0x18, 0xa0);

// Time/Date sensor fields.
// Because these are related, each field uses the same GUID, but changes the PID.
// {340946F2-9A77-42b0-8176-57D4DF00E5CA}
DEFINE_PROPERTYKEY(SAMPLE_SENSOR_DATA_TYPE_HOUR,
0x340946f2, 0x9a77, 0x42b0, 0x81, 0x76, 0x57, 0xd4, 0xdf, 0x0, 0xe5, 0xca, PID_FIRST_USABLE); // PID = 2

DEFINE_PROPERTYKEY(SAMPLE_SENSOR_DATA_TYPE_MINUTE,
0x340946f2, 0x9a77, 0x42b0, 0x81, 0x76, 0x57, 0xd4, 0xdf, 0x0, 0xe5, 0xca, PID_FIRST_USABLE + 1); // PID = 3

DEFINE_PROPERTYKEY(SAMPLE_SENSOR_DATA_TYPE_SECOND,
0x340946f2, 0x9a77, 0x42b0, 0x81, 0x76, 0x57, 0xd4, 0xdf, 0x0, 0xe5, 0xca, PID_FIRST_USABLE + 2); // PID = 4
```

## Using the DEFINE\_PROPERTYKEY Macro

To use the DEFINE\_PROPERTYKEY macro, use one of the following two options:

-   Include Initguid.h in your project. In this case, the macro defines the property key for you. This approach works in most cases, but can cause naming collisions in large, complex projects.

-   Do not include Initguid.h. Instead, compile your definitions into a static library file that has the .lib file name extension. In this case, the macro declares the names for your property keys for the compiler. However, you have to reference the .lib file in your linker settings. This approach works best in large projects that use multiple modules.

Using the macro without including Initguid.h and without referencing a library file will cause the LNK2001 error.

## Related topics
[The Sensors Geolocation Driver Sample](https://msdn.microsoft.com/library/windows/hardware/hh768273)



