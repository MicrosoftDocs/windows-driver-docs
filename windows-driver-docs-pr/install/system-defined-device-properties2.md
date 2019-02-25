---
title: System-Defined Device Properties
description: System-Defined Device Properties
ms.assetid: 9d823a9f-0802-4e92-bf94-abb5b0e7b9ee
keywords:
- device properties WDK device installations , system-defined
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# System-Defined Device Properties


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) supports system-defined properties that characterize the configuration or operation of device instances, [device setup classes](device-setup-classes.md), [device interface classes](device-interface-classes.md), and device interfaces. Each property is represented by a [property key](property-keys.md), which is a GUID value that identifies a property category and a property identifier. The system-defined property key categories are reserved for system use only.

The following system-defined device property keys are defined in *Devpkey.h*:

-   The DEVPKEY_NAME property key that represents the name of a component. Use the value of the DEVPKEY_NAME property to indentify the component to an end-user. Windows supports the DEVPKEY_NAME property for [**device instances**](https://msdn.microsoft.com/library/windows/hardware/ff543530), [**device setup classes**](https://msdn.microsoft.com/library/windows/hardware/ff543534), and [**device interfaces**](https://msdn.microsoft.com/library/windows/hardware/ff543533).

-   Property keys that represent the [device instance properties that correspond to the SPDRP_Xxx identifiers](https://msdn.microsoft.com/library/windows/hardware/ff541334). (The SPDRP_*Xxx* identifiers are defined in *Setupapi.h*.)

-   Property keys that represent the device instance properties that do not have corresponding SPDRP_*Xxx* identifiers. This includes the following:

    [Device status and problem properties](https://msdn.microsoft.com/library/windows/hardware/ff542254)

    [Device relations properties](https://msdn.microsoft.com/library/windows/hardware/ff541498), including the parent device, child devices, and sibling devices

    [Device driver properties](https://msdn.microsoft.com/library/windows/hardware/ff541205)

    [Device driver package properties](https://msdn.microsoft.com/library/windows/hardware/ff541200)

    [Miscellaneous other device properties](https://msdn.microsoft.com/library/windows/hardware/ff549289)

-   Property keys that represent [device setup class properties](https://msdn.microsoft.com/library/windows/hardware/ff542239) that correspond to the SPCRP_Xxx identifiers. (The SPCRP_Xxx identifiers are defined in *Setupapi.h*.)

-   Property keys that represent device setup class properties that do not have corresponding SPCRP_Xxx identifiers.

-   Property keys that represent [device interface class properties](https://msdn.microsoft.com/library/windows/hardware/ff541406).

-   Property keys that represent [device interface properties](https://msdn.microsoft.com/library/windows/hardware/ff541409).

For information about how to create custom device properties, see [Creating Custom Device Properties](creating-custom-device-properties.md).

 

 





