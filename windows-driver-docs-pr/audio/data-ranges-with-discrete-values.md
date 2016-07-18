---
title: Data Ranges with Discrete Values
description: Data Ranges with Discrete Values
ms.assetid: 330edd60-0469-4351-bfb1-29b29e133c1a
keywords: ["data-intersection handlers WDK audio , discrete value data ranges", "discrete value data ranges WDK audio", "data ranges WDK audio , discrete values"]
---

# Data Ranges with Discrete Values


## <span id="data_ranges_with_discrete_values"></span><span id="DATA_RANGES_WITH_DISCRETE_VALUES"></span>


If your audio device supports sample frequencies of 11, 22, and 44 kHz, for example, you can specify all three frequencies as a range of 11 to 44 kHz in a single [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) structure. This technique has the benefit of being concise. A potential disadvantage is that a buggy data-intersection handler might choose an invalid parameter value (for example, 27 kHz) that falls within the range. In this case, the adapter driver has no option but to fail the **NewStream** call (for example, see [**IMiniportWavePci::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536735)) that attempts to create a pin with the invalid format.

Another approach is to provide a list of data ranges in which each data range specifies a discrete value rather than a range of values for each parameter. For example, instead of providing a single data range to specify a range of sample frequencies from 11 to 44 kHz, the data-range array can contain three separate elements for 11, 22, and 44 kHz. In each of these elements, the maximum and minimum sample frequencies are set to the same value (11, 22, or 44 kHz). The benefit of this approach is that it eliminates any ambiguity about the precise values that are supported. Also, if one discrete value is preferred over another, the data range containing this value can be moved to a position in the array that is ahead of the data range containing the other value. A minor disadvantage of discrete values is that they can increase the size of the data-range array.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Data%20Ranges%20with%20Discrete%20Values%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


