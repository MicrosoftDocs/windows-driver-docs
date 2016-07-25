---
title: Installing a New Bus Driver
description: Installing a New Bus Driver
ms.assetid: 449c0c08-c995-4e23-a770-a567bd48966c
---

# Installing a New Bus Driver


New vendor bus drivers should comply with the following guidelines for reporting the bus type and device IDs, and, possibly, for creating a new [device setup class](device-setup-classes.md) for the child devices on the bus. These guidelines apply to a new vendor bus if the configuration or operation of the bus and its child devices differ significantly from other buses. In those cases, new vendor bus drivers should do the following to ensure that the bus and its child devices are not unintentionally and inappropriately grouped with other buses and child devices:

1.  Use a unique GUID to identify the bus type. A bus driver reports the bus type of a child device (represented as a physical device object ([*PDO*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdo)) in response to an [**IRP\_MN\_QUERY\_BUS\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff551654) request for the child device. In response to such a request, the bus driver returns a pointer to a [**PNP\_BUS\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff559608) structure that returns the GUID in the **PNP\_BUS\_INFORMATION.BusTypeGuid** member. In addition, the bus driver should set **PNP\_BUS\_INFORMATION.LegacyBusType** to **PNPBus**, and **PNP\_BUS\_INFORMATION.BusNumber** to an appropriate custom value.

2.  [Use custom hardware IDs](using-custom-hardware-ids-and-compatible-ids.md) to uniquely identify the bus [*enumerator*](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-enumerator) and the child devices of the bus.

3.  If the child devices of the bus do not belong to an existing [device setup class](device-setup-classes.md), [install a new device setup class for the child devices of the bus](installing-a-new-device-setup-class-for-a-bus.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installing%20a%20New%20Bus%20Driver%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




