---
title: Combining Nodes in a Filter
description: Combining Nodes in a Filter
ms.assetid: ebceb42a-966d-4c03-b4f5-8666284fc871
keywords:
- control nodes WDK BDA
- nodes WDK BDA
- combining nodes in filters WDK BDA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Combining Nodes in a Filter





The following figure of a sample DirectShow filter graph shows one possible way in which the control nodes can be represented as filters in a filter graph. The network provider is always its own filter and precedes all other filters. In this sample, because the tuner and demodulator nodes are combined on the same circuit card, they appear as one filter. The capture filter follows the tuner/demodulator filter. For all of these filters so far, the actual internal and external connections in the filter match the control nodes. The next filter downstream is the MPEG-2 transport stream demultiplexer, which is represented by a single filter that exposes the packet identifier (PID) filters as shown in the figure in the [Control Nodes](control-nodes.md) section. The actual MPEG-2 transport stream demultiplexer filter reproduces the topology as many times as necessary to handle all the elementary streams.

![diagram illustrating a directshow filter graph with a tuner and demodulator combined in one filter](images/smpdshw1.png)

 

 




