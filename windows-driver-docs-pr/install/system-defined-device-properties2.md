---
title: System-Defined Device Properties
description: System-Defined Device Properties
ms.assetid: 9d823a9f-0802-4e92-bf94-abb5b0e7b9ee
keywords: ["device properties WDK device installations , system-defined"]
---

# System-Defined Device Properties


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) supports system-defined properties that characterize the configuration or operation of device instances, [device setup classes](device-setup-classes.md), [device interface classes](device-interface-classes.md), and device interfaces. Each property is represented by a [property key](property-keys.md), which is a GUID value that identifies a property category and a property identifier. The system-defined property key categories are reserved for system use only.

The following system-defined device property keys are defined in *Devpkey.h*:

-   The DEVPKEY\_NAME property key that represents the name of a component. Use the value of the DEVPKEY\_NAME property to indentify the component to an end-user. Windows supports the DEVPKEY\_NAME property for [**device instances**](https://msdn.microsoft.com/library/windows/hardware/ff543530), [**device setup classes**](https://msdn.microsoft.com/library/windows/hardware/ff543534), and [**device interfaces**](https://msdn.microsoft.com/library/windows/hardware/ff543533).

-   Property keys that represent the [device instance properties that correspond to the SPDRP\_Xxx identifiers](https://msdn.microsoft.com/library/windows/hardware/ff541334). (The SPDRP\_*Xxx* identifiers are defined in *Setupapi.h*.)

-   Property keys that represent the device instance properties that do not have corresponding SPDRP\_*Xxx* identifiers. This includes the following:

    [Device status and problem properties](https://msdn.microsoft.com/library/windows/hardware/ff542254)

    [Device relations properties](https://msdn.microsoft.com/library/windows/hardware/ff541498), including the parent device, child devices, and sibling devices

    [Device driver properties](https://msdn.microsoft.com/library/windows/hardware/ff541205)

    [Device driver package properties](https://msdn.microsoft.com/library/windows/hardware/ff541200)

    [Miscellaneous other device properties](https://msdn.microsoft.com/library/windows/hardware/ff549289)

-   Property keys that represent [device setup class properties](https://msdn.microsoft.com/library/windows/hardware/ff542239) that correspond to the SPCRP\_Xxx identifiers. (The SPCRP\_Xxx identifiers are defined in *Setupapi.h*.)

-   Property keys that represent device setup class properties that do not have corresponding SPCRP\_Xxx identifiers.

-   Property keys that represent [device interface class properties](https://msdn.microsoft.com/library/windows/hardware/ff541406).

-   Property keys that represent [device interface properties](https://msdn.microsoft.com/library/windows/hardware/ff541409).

For information about how to create custom device properties, see [Creating Custom Device Properties](creating-custom-device-properties.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20System-Defined%20Device%20Properties%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




