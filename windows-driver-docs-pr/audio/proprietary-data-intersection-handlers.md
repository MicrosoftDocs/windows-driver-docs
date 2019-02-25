---
title: Proprietary Data-Intersection Handlers
description: Proprietary Data-Intersection Handlers
ms.assetid: 8ed497d3-2344-4979-9859-e66a4713e6c5
keywords:
- data-intersection handlers WDK audio , proprietary
- proprietary data-intersection handlers WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Proprietary Data-Intersection Handlers


## <span id="proprietary_data_intersection_handlers"></span><span id="PROPRIETARY_DATA_INTERSECTION_HANDLERS"></span>


You can overcome the limitations of the default data-intersection handler by writing a proprietary handler for your adapter. A proprietary handler is implemented as the [**IMiniport::DataRangeIntersection**](https://msdn.microsoft.com/library/windows/hardware/ff536764) method on a miniport driver object. See the sample adapter drivers in the Microsoft Windows Driver Kit (WDK) for examples of **DataRangeIntersection** methods.

A proprietary data-intersection handler can compensate for nonstandard hardware features that cannot be adequately specified in the [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) structure. For example, the AC97 sample adapter driver in the WDK manages hardware that can support two or more audio channels during playback, but cannot support mono. The sample's [**DataRangeIntersection**](https://msdn.microsoft.com/library/windows/hardware/ff536764) method determines whether the data range for the other filter's source pin is limited to mono (that is, **MaximumChannels** &lt; 2). If so, it fails the call by returning STATUS\_NO\_MATCH.

A proprietary data-intersection handler has the option of handling data intersections on some of its pins and allowing the port driver's default data-intersection handler to handle data intersections on the other pins.

The remainder of this section presents guidelines for implementing proprietary data-intersection handlers.

 

 




