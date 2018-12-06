---
title: Mediums and Categories
description: Mediums and Categories
ms.assetid: 2bc83ce6-7f79-44e7-a0fb-7b9f56771730
keywords:
- video capture WDK AVStream , mediums
- capturing video WDK AVStream , mediums
- video capture WDK AVStream , stream categories
- capturing video WDK AVStream , stream categories
- identifying pin primary purpose
- stream categories WDK video capture
- mediums WDK video capture
- pin connections WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mediums and Categories


Traditionally, Microsoft DirectShow streams have been identified solely by their [Media Type](http://go.microsoft.com/fwlink/p/?linkid=51458). While this is sufficient for rendering simple filter graphs, more complex graphs and graphs that reflect a hardware topology require additional information for correct graph building. To enable filter graph building to correctly identify and connect pins, video capture minidrivers specify stream categories that their pins belong to, as well as mediums.

Stream categories are a method to identify the primary purpose of a pin. For example, a capture filter could have two output pins with identical MediaTypes supported on each pin. In the case where the filter gives priority to one of the pins, the higher-priority pin could be assigned to the capture stream category (PINNAME\_VIDEO\_CAPTURE), and the lower-priority pin to the preview stream category (PINNAME\_VIDEO\_PREVIEW).

Mediums are a method to ensure connectivity between two pins on separate filters, such as the analog audio output pin on a TV tuner filter (to support TV audio), and TV Audio input pin on a TV Audio filter. One way to think of a medium is that it identifies a wire between the output pin of one filter and the input pin of another filter.

The DirectShow graph builder interfaces, **IFilterMapper2** and **ICaptureGraphBuilder**, use these methods to construct filter graphs based on both mediums and stream categories.

 

 




