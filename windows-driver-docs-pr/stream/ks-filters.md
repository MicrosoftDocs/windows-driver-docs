---
title: KS Filters
description: KS Filters
ms.assetid: caf46279-17f3-4bb4-8b8a-a1673f9fa28f
keywords:
- filters WDK kernel streaming
- KS filters WDK kernel streaming
- mixers WDK kernel streaming
- kernel streaming WDK , filters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# KS Filters





A filter is a group of nodes that encapsulates a processing task to be performed on the data stream. [Pins](ks-pins.md) serve as input and output conduits on a filter.

A simple filter could contain one data sink pin and one data source pin. The filter receives incoming data on the data sink pin, processes it internally, and writes to the data source pin. In the following figure, the pins are shown as heavy line segments. Internally, the filter connects the data sink pin to an internal processing unit, a *node*, which in turn is connected to the data source pin.

![diagram illustrating a simple ks filter](images/ks01.png)

Another device might combine or split data flows between pins. For example, an audio mixer supports several data sink pins. The mixer combines them into a single stream, and writes that stream to a data source pin. The following illustration shows the data flow.

![diagram illustrating a mixer](images/ks02.png)

The graph describes the internal relationship between the filter's pins. A more complicated filter might encapsulate several nodes that transform data flowing through the filter.

Filters specify internal connections between pins and internal nodes by using the [KSPROPSETID\_Topology](https://msdn.microsoft.com/library/windows/hardware/ff566598) property set.

The [**KSPROPERTY\_TOPOLOGY\_CONNECTIONS**](https://msdn.microsoft.com/library/windows/hardware/ff565802) property queries all connections between nodes of a KS filter. This property returns an array of [**KSTOPOLOGY\_CONNECTION**](https://msdn.microsoft.com/library/windows/hardware/ff567148). Each KSTOPOLOGY\_CONNECTION structure represents a single data-path connection inside a filter. In the mixer diagram above, the sequence of KSTOPOLOGY\_CONNECTION structures could be as follows:

```cpp
//    FromNode,       FromNodePin,     ToNode,        ToNodePin,
{
 {  KSFILTER_NODE,        0,            0,               0     },
 {       0,               1,       KSFILTER_NODE,        1     }
}
```

 

 




