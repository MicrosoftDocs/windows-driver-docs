---
title: Framework Object Properties
description: Framework Object Properties
keywords:
- framework objects WDK KMDF , properties
- properties WDK KMDF
- get method WDK KMDF
- set method WDK KMDF
ms.date: 04/20/2017
---

# Framework Object Properties





Most framework objects contain sets of properties. Properties represent information that is available to a driver. From the driver's perspective, some properties are read-only and some are read/write.

For each readable property, the framework defines a "get" [method](framework-object-methods.md) that a driver can call to retrieve the property's value. Each "get" method returns the current value of the property.

For each writable property, the framework defines a "set" method that a driver can call to modify the property's value. The driver supplies the property's new value as an input parameter to the "set" method.

For example, the framework device object defines two methods, [**WdfDeviceGetDeviceState**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegetdevicestate) and [**WdfDeviceSetDeviceState**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetdevicestate), that a driver can call to get or set a device's Plug and Play (PnP) state.

 

