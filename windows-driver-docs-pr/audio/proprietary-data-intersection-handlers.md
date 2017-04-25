---
title: Proprietary Data-Intersection Handlers
description: Proprietary Data-Intersection Handlers
ms.assetid: 8ed497d3-2344-4979-9859-e66a4713e6c5
keywords:
- data-intersection handlers WDK audio , proprietary
- proprietary data-intersection handlers WDK audio
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Proprietary Data-Intersection Handlers


## <span id="proprietary_data_intersection_handlers"></span><span id="PROPRIETARY_DATA_INTERSECTION_HANDLERS"></span>


You can overcome the limitations of the default data-intersection handler by writing a proprietary handler for your adapter. A proprietary handler is implemented as the [**IMiniport::DataRangeIntersection**](https://msdn.microsoft.com/library/windows/hardware/ff536764) method on a miniport driver object. See the sample adapter drivers in the Microsoft Windows Driver Kit (WDK) for examples of **DataRangeIntersection** methods.

A proprietary data-intersection handler can compensate for nonstandard hardware features that cannot be adequately specified in the [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) structure. For example, the AC97 sample adapter driver in the WDK manages hardware that can support two or more audio channels during playback, but cannot support mono. The sample's [**DataRangeIntersection**](https://msdn.microsoft.com/library/windows/hardware/ff536764) method determines whether the data range for the other filter's source pin is limited to mono (that is, **MaximumChannels** &lt; 2). If so, it fails the call by returning STATUS\_NO\_MATCH.

A proprietary data-intersection handler has the option of handling data intersections on some of its pins and allowing the port driver's default data-intersection handler to handle data intersections on the other pins.

The remainder of this section presents guidelines for implementing proprietary data-intersection handlers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Proprietary%20Data-Intersection%20Handlers%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


