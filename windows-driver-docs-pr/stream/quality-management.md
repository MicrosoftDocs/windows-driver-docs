---
title: Quality Management
author: windows-driver-content
description: Quality Management
ms.assetid: 359e6e12-903f-4037-8f35-b090ce41f770
keywords:
- quality management WDK kernel streaming
- KSPROPERTY_STREAM_QUALITY
- KSQUALITY_MANAGER
- notifications WDK kernel streaming
- complaints WDK kernel streaming
- kernel streaming WDK , quality management
- KS WDK , quality management
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Quality Management


## <a href="" id="ddk-quality-management-ksg"></a>


The kernel streaming architecture provides optional support for quality management. This mechanism adjusts flow control to match resource constraints and determines degradation needs in a filter graph. Quality management notifications are sent through a kernel-mode proxy.

Pins that report quality management problems support the [**KSPROPERTY\_STREAM\_QUALITY**](https://msdn.microsoft.com/library/windows/hardware/ff565750) property. This is an optional write-only property that the pin can set to the handle and context parameter of a QM complaint sink. To do this, the pin provides a structure of type [**KSQUALITY\_MANAGER**](https://msdn.microsoft.com/library/windows/hardware/ff566730) that contains this information. The pin connection in turn uses this information to notify the quality manager of problems using [**KSQUALITY**](https://msdn.microsoft.com/library/windows/hardware/ff566728) structures with the given context parameter.

To allow user-mode clients to submit quality management complaints, a minidriver supports properties in [KSPROPSETID\_Quality](https://msdn.microsoft.com/library/windows/hardware/ff566587).

If the pin allows degradation strategies, the minidriver supports the [**KSPROPERTY\_STREAM\_DEGRADATION**](https://msdn.microsoft.com/library/windows/hardware/ff565690) property.

For more information, see [**KSDEGRADE**](https://msdn.microsoft.com/library/windows/hardware/ff561671) and [**KSDEGRADE\_STANDARD**](https://msdn.microsoft.com/library/windows/hardware/ff561673).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Quality%20Management%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


