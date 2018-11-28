---
title: Control Nodes
description: Control Nodes
ms.assetid: e1ab522e-089e-4508-aef4-5b2a65f50bb5
keywords:
- broadcast receiver topology WDK BDA
- receiver topology WDK BDA
- Broadcast Driver Architecture WDK AVStream , broadcast receiver topology
- BDA WDK AVStream , receiver topology
- control nodes WDK BDA
- nodes WDK BDA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Control Nodes





The following figure shows an example of one possible functional topology that receives digital broadcast content. It illustrates the operations necessary to:

-   tune and demodulate the signal.

-   capture and demultiplex the signal.

-   obtain electronic program guide (EPG) information.

-   obtain audio and video content.

-   obtain IP data.

![diagram illustrating receiver topology](images/rcvrtopl.png)

Note that some functions in receiver topology that acquire content, such as the tuner, are always associated with hardware. Other functions, such as content stream demultiplexing, can be performed with hardware or software components. Still others, such as the transport information filter (TIF) and network provider filter, are always software components.

The blocks in the preceding figure correspond to BDA control nodes. Each control node combines network and program-specific parameter data with the input signal, or signal component, using a standard algorithm. The result produces a new signal component that is useful to the control nodes connected immediately downstream.

 

 




