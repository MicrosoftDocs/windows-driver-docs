---
title: Testing BDA Drivers Using BDA Filters
description: Testing BDA Drivers Using BDA Filters
ms.assetid: 136810b7-9378-482b-8e21-a7eae0142909
keywords:
- Broadcast Driver Architecture WDK AVStream , testing drivers
- BDA WDK AVStream , testing drivers
- testing drivers WDK , BDA
- DirectShow filters WDK AVStream
- Graph Editor WDK BDA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Testing BDA Drivers Using BDA Filters





You can use the DirectShow Filter Graph Editor (*Graphedt.exe*) to insert a DirectShow filter instance of your BDA component in a filter graph so that you can test your component. You can obtain the Graph Editor from the Microsoft Windows Driver Kit (WDK).

You can use the Graph Editor to perform rudimentary tests of a BDA component, such as, connecting pins that are exposed by a filter instance of the component to other pins of filter types in the graph.

To use the Graph Editor to thoroughly test functionality of your BDA component, you must build a filter graph that starts with a BDA network provider filter, contains a filter instance of your BDA component, and is rendered, at least, through a demultiplexer filter (packet identifier (PID) filter) to a transport information filter (TIF). The biggest problem with using the Graph Editor is that there is no dedicated application to submit requests via the **ITuner** interface that the network provider filter implements. However, the network provider filter has associated property pages that provide some limited ability to exercise the **ITuner** interface.

 

 




