---
title: Processing Classify Callouts
description: Processing Classify Callouts
ms.assetid: 284aeda0-8275-440f-abf4-84a0c61cc4f4
keywords:
- Windows Filtering Platform callout drivers WDK , classify callouts
- callout drivers WDK Windows Filtering Platform , classify callouts
- classifyFn
- classify callouts WDK Windows Filtering Platform
- classify callouts WDK Windows Filtering Platform , about classify callouts
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing Classify Callouts


The filter engine calls a callout's [*classifyFn*](https://msdn.microsoft.com/library/windows/hardware/ff544890) callout function when there is network data to be processed by the callout. This occurs when all the filtering conditions are true for a filter that specifies the callout for the filter's action. If such a filter has no filtering conditions, the filter engine always calls the callout's *classifyFn* callout function.

The filter engine passes several different data items to a callout's *classifyFn* callout function. These data items include fixed data values, metadata values, raw network data, filter information, and any flow context. The particular data items that the filter engine passes to the callout depend on the specific filtering layer and the conditions under which *classifyFn* is called. A *classifyFn* function can use any combination of these data items to make its filtering decisions.

The implementation of a callout's *classifyFn* callout function depends on what the callout is designed to do. The following sections provide examples of some the more typical functions of a callout:

[Using a Callout for Deep Inspection](using-a-callout-for-deep-inspection.md)

[Using a Callout for Deep Inspection of Stream Data](using-a-callout-for-deep-inspection-of-stream-data.md)

[Inspecting Packet and Stream Data](inspecting-packet-and-stream-data.md)

[Modifying Stream Data](modifying-stream-data.md)

[Data Logging](data-logging.md)

[Associating Context with a Data Flow](associating-context-with-a-data-flow.md)

[Processing Classify Callouts Asynchronously](processing-classify-callouts-asynchronously.md)

[Using Bind or Connect Redirection](using-bind-or-connect-redirection.md)

[ALE Endpoint Lifetime Management](ale-endpoint-lifetime-management.md)

[Using Packet Tagging](using-packet-tagging.md)

The actual implementation of a particular callout's *classifyFn* callout function can be based on a combination of these examples.

For callouts that process data at a filtering layer that supports data flows, the callout's *classifyFn* callout function can associate a context with each of the data flows. The *classifyFn* function can use this context to save state information for the next time that it is called by the filter engine for that data flow. For more information about how a callout function can associate a context with a data flow, see [Associating Context with a Data Flow](associating-context-with-a-data-flow.md).

WFP supports asynchronous processing of the *classifyFn* callout function. For more information about asynchronous processing, see [Processing Classify Callouts Asynchronously](processing-classify-callouts-asynchronously.md).

 

 





