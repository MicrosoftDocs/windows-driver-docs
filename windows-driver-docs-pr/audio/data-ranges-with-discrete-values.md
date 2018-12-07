---
title: Data Ranges with Discrete Values
description: Data Ranges with Discrete Values
ms.assetid: 330edd60-0469-4351-bfb1-29b29e133c1a
keywords:
- data-intersection handlers WDK audio , discrete value data ranges
- discrete value data ranges WDK audio
- data ranges WDK audio , discrete values
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Data Ranges with Discrete Values


## <span id="data_ranges_with_discrete_values"></span><span id="DATA_RANGES_WITH_DISCRETE_VALUES"></span>


If your audio device supports sample frequencies of 11, 22, and 44 kHz, for example, you can specify all three frequencies as a range of 11 to 44 kHz in a single [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) structure. This technique has the benefit of being concise. A potential disadvantage is that a buggy data-intersection handler might choose an invalid parameter value (for example, 27 kHz) that falls within the range. In this case, the adapter driver has no option but to fail the **NewStream** call (for example, see [**IMiniportWavePci::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536735)) that attempts to create a pin with the invalid format.

Another approach is to provide a list of data ranges in which each data range specifies a discrete value rather than a range of values for each parameter. For example, instead of providing a single data range to specify a range of sample frequencies from 11 to 44 kHz, the data-range array can contain three separate elements for 11, 22, and 44 kHz. In each of these elements, the maximum and minimum sample frequencies are set to the same value (11, 22, or 44 kHz). The benefit of this approach is that it eliminates any ambiguity about the precise values that are supported. Also, if one discrete value is preferred over another, the data range containing this value can be moved to a position in the array that is ahead of the data range containing the other value. A minor disadvantage of discrete values is that they can increase the size of the data-range array.

 

 




