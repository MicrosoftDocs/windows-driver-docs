---
title: About Item Properties
description: About Item Properties
ms.assetid: f8d00e29-ce7d-4949-a713-07755f495d6a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# About Item Properties





Each application item tree contains a collection of item properties. (This property collection is also known as a property stream.) The application item model provides each application with its own copy of the item tree, allowing applications to modify properties independent of each other.

Drivers specify the properties they support and define the initial values of those properties. When an application reads a property, the driver updates any properties that must be refreshed with their current values. For example, if the application is reading the device time, then the driver can ask the device for its current time and update the device time property. When an application writes a new value to the property, the WIA service asks the driver to validate and write this value to the property.

Certain properties are mandatory for some device types. For example, a device with an automatic document feeder (ADF) must support the ADF properties.

**Note**   If you are more familiar with TWAIN than you are with WIA, it may be helpful to know that WIA properties are synonymous with TWAIN capabilities.

 

 

 




