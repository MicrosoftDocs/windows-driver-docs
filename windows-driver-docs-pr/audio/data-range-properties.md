---
title: Data-Range Properties
description: Data-Range Properties
ms.assetid: 84bdd151-a034-445e-9f6d-19940e32b2c1
keywords: ["data-intersection handlers WDK audio , data-range properties", "data ranges WDK audio , properties"]
---

# Data-Range Properties


## <span id="data_range_properties"></span><span id="DATA_RANGE_PROPERTIES"></span>


Data ranges are used not only for data intersection, but can be accessed as device properties as well (see [Pin Data-Range and Intersection Properties](pin-data-range-and-intersection-properties.md)). For this reason, an adapter driver whose data-intersection handler takes care of all format negotiations on its pins should still include a complete set of data ranges. The data ranges should reflect as closely as possible the data-format preferences that are embodied in the adapter's data-intersection handler.

A pin's data ranges can be accessed through the following properties:

[**KSPROPERTY\_PIN\_DATARANGES**](https://msdn.microsoft.com/library/windows/hardware/ff565199)

[**KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES**](https://msdn.microsoft.com/library/windows/hardware/ff565195)

These two properties designate the pin's static data ranges and constrained data ranges, respectively.

Constrained data ranges provide more accurate information about the current capabilities of a device because they are dynamically updated to account for any on-board resources that have already been allocated for other purposes. By comparison, static data ranges might inaccurately report hardware capabilities that depend on resources that are no longer available.

In the current PortCls implementation, the default data-intersection handlers in the port drivers use only an adapter's static data ranges.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Data-Range%20Properties%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




