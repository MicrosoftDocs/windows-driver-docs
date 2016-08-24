---
title: Mediums and Categories
author: windows-driver-content
description: Mediums and Categories
MS-HAID:
- 'vidcapds\_7b441ff1-7cfc-42e9-89f9-603f64584fe7.xml'
- 'stream.mediums\_and\_categories'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2bc83ce6-7f79-44e7-a0fb-7b9f56771730
keywords: ["video capture WDK AVStream , mediums", "capturing video WDK AVStream , mediums", "video capture WDK AVStream , stream categories", "capturing video WDK AVStream , stream categories", "identifying pin primary purpose", "stream categories WDK video capture", "mediums WDK video capture", "pin connections WDK video capture"]
---

# Mediums and Categories


Traditionally, Microsoft DirectShow streams have been identified solely by their [Media Type](http://go.microsoft.com/fwlink/p/?linkid=51458). While this is sufficient for rendering simple filter graphs, more complex graphs and graphs that reflect a hardware topology require additional information for correct graph building. To enable filter graph building to correctly identify and connect pins, video capture minidrivers specify stream categories that their pins belong to, as well as mediums.

Stream categories are a method to identify the primary purpose of a pin. For example, a capture filter could have two output pins with identical MediaTypes supported on each pin. In the case where the filter gives priority to one of the pins, the higher-priority pin could be assigned to the capture stream category (PINNAME\_VIDEO\_CAPTURE), and the lower-priority pin to the preview stream category (PINNAME\_VIDEO\_PREVIEW).

Mediums are a method to ensure connectivity between two pins on separate filters, such as the analog audio output pin on a TV tuner filter (to support TV audio), and TV Audio input pin on a TV Audio filter. One way to think of a medium is that it identifies a wire between the output pin of one filter and the input pin of another filter.

The DirectShow graph builder interfaces, **IFilterMapper2** and **ICaptureGraphBuilder**, use these methods to construct filter graphs based on both mediums and stream categories.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Mediums%20and%20Categories%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


