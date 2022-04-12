---
title: System-defined device properties
description: Learn more about system-defined device properties.
keywords:
- device properties WDK device installations , system-defined
ms.date: 04/12/2022
---

# System-defined device properties

In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) supports system-defined properties that characterize the configuration or operation of device instances, [device setup classes](./overview-of-device-setup-classes.md), [device interface classes](./overview-of-device-interface-classes.md), and device interfaces. Each property is represented by a [property key](property-keys.md), which is a GUID value that identifies a property category and a property identifier. The system-defined property key categories are reserved for system use only.

The following system-defined device property keys are defined in *Devpkey.h*:

- The DEVPKEY_NAME property key that represents the name of a component. Use the value of the DEVPKEY_NAME property to identify the component to an end-user. Windows supports the DEVPKEY_NAME property for [**device instances**](./devpkey-name--device-instance-.md), [**device setup classes**](./devpkey-name--device-setup-class-.md), and [**device interfaces**](./devpkey-name--device-interface-.md).

- Property keys that represent the [device instance properties that correspond to the SPDRP_Xxx identifiers](/previous-versions/ff541334(v=vs.85)). (The SPDRP_*Xxx* identifiers are defined in *Setupapi.h*.)

- Property keys that represent the device instance properties that do not have corresponding SPDRP_*Xxx* identifiers. This includes the following:

    [Device status and problem properties](./retrieving-the-status-and-problem-code-for-a-device-instance.md)

    [Device relations properties](retrieving-device-relations.md), including the parent device, child devices, and sibling devices

    [Device driver properties](accessing-device-driver-properties.md)

    [Device driver package properties](/previous-versions/ff541200(v=vs.85))

    [Miscellaneous other device properties](/previous-versions/ff549289(v=vs.85))

- Property keys that represent [device setup class properties](accessing-device-setup-class-properties.md) that correspond to the SPCRP_Xxx identifiers. (The SPCRP_Xxx identifiers are defined in *Setupapi.h*.)

- Property keys that represent device setup class properties that do not have corresponding SPCRP_Xxx identifiers.

- Property keys that represent [device interface class properties](accessing-device-interface-class-properties.md).

- Property keys that represent [device interface properties](accessing-device-interface-properties.md).

For information about how to create custom device properties, see [Creating custom device properties](creating-custom-device-properties.md).
