---
title: About sensor parameter types
description: About sensor parameter types
ms.date: 11/30/2022
---

# About sensor parameter types

You should understand how the sensor class extension uses some data types as method parameters. The following table describes these data types.

| Type | Parameter names | Meaning |
|---|---|---|
| [IWDFFile](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdffile) | pClientFile | This UMDF COM interface represents a file object that the platform associates with a client application. Although sensor method calls always supply this type as a valid interface pointer, it is intended to be used as an ID for the application. The address that the pointer contains is a unique number that can identify the client application. Be aware that this value is distinct from the address of the pointer itself. Do not use the address-of operator (&) to retrieve an ID. Use the pointer itself.</br></br>If you choose to use this pointer to access the underlying object, remember to call AddRef through the pointer initially, and to call Release when you have finished. |
| **LPWSTR** | pwszSensorID | This string is a unique ID that is provided by the driver for a particular sensor. This ID must be unique for each sensor on a particular device. |
| [IPortableDeviceValues](/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevalues) | ppDataValues</br></br>ppPropertyValues</br></br>pPropertiesToSet</br></br>ppResults | This WPD interface provides a convenient way to create a property bag of name/value pairs. **PROPERTYKEY**s represent names and **PROPVARIANT**s represent values. The DDI uses this interface both to set and retrieve sets of values, or for a single value.</br></br>You can retrieve this interface from a method or, if a new object is required, by calling CoCreateInstance with **CLSID_PortableDeviceValues**. |
| [IPortableDeviceValuesCollection](/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevaluescollection) | pEventCollection</br></br>ppSensorObjectCollection | This WPD interface contains a collection of [IPortableDeviceValues](/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevalues) objects. DDI methods that use this interface enable you to provide several sets of data at the same time, such as multiple events or information about multiple sensors.</br></br>You can retrieve this interface from a method or, if a new object is required, by calling CoCreateInstance with **CLSID_PortableDeviceValuesCollection**. |
| [IPortableDeviceKeyCollection](/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicekeycollection) | pDataFields</br></br>pProperties</br></br>ppSupportedDataFields</br></br>ppSupportedProperties | This WPD interface contains a collection of **PROPERTYKEY**s. These keys represent property names that can be stored by [IPortableDeviceValues](/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevalues). The DDI uses this collection object both for setting and retrieving sets of property names, or a single name.</br></br>You can retrieve this interface from a method or, if a new object is required, by calling CoCreateInstance with **CLSID_PortableDeviceKeyCollection**. |
