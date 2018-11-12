---
title: Analyzing a Capture Stall
description: Analyzing a Capture Stall
ms.assetid: 9a88deba-374c-4ccc-8bb8-18e3b4124158
keywords: ["kernel streaming debugging, blah"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Analyzing a Capture Stall


The following is an artificially created scenario that simulates a capture stall. This is a particularly valuable scenario since similar situations frequently occur in stress testing. The scenario is as follows:

The Windows recording component Sndrec32 is recording from the primary capture device, in this case a Creative SBLive wave device. For a period of time, it records normally; however, the graph stalls at 8.50 seconds because we have explicitly caused portcls not to complete capture IRPs for purposes of this test.

The application shows running, but the stream position is not advancing. Position is halted at 8.50 seconds.

Since the primary capture device on this machine is a PCI sound card, first use the [**!ks.pciaudio**](-ks-pciaudio.md) command to try and determine a starting point. Use a flag value of 1 to request a display of all running streams:

```dbgcmd
kd> !pciaudio 1

1 Audio FDOs found:
 Functional Device 8121c030 [\Driver\emu10k]
        Wave Cyclic Streams:
            Pin 812567c0 RUN [emu10k1m!CMiniportWaveCyclicStreamSBLive ff9ec7f8] 
```

In this case, there is only one PCI audio device and it is serviced by the Intel emu10k driver (\\Driver\\emu10k). This driver currently has a single running stream (0x812567C0). Now you can use [**!ks.graph**](-ks-graph.md) to view the kernel graph. Set *Level* and *Flags* both to 7 to obtain maximum detail on the stall:

```dbgcmd
kd> !graph 812567c0 7 7
Attempting a graph build on 812567c0...  Please be patient...
Graph With Starting Point 812567c0:
"emu10k" Filter ff9ebb98, Child Factories 5
    Output Factory 0:
        Pin 812567c0 (File 811c6630, -> "splitter" 811df960) Irps(q/p) = 8, 0
 Queued: 81255418 811df008 81252008 81255280 81250b30 ffa1fe70 81252e70 ffa01d98 
```

The above shows the details for factory 0. The emu10k output pin 0x812567C0 is connected to the splitter input pin 0x811DF960. There are eight IRPs queued to emu10k's output pin. The output from [**!ks.graph**](-ks-graph.md) continues as follows:

```dbgcmd
"splitter" Filter ffb18890, Child Factories 2
    Output Factory 0:
        Pin 811df430 (File ffa55f90) Irps(q/p) = 10, 0
 Queued: ffadd008 ffa73b00 ffa1e998 811de310 ffa54370 ffaaf008 811dee70 81250e70 811de580 811de8c0 
```

There are ten IRPs queued to splitter's output pin.

```dbgcmd
    Input Factory 1:
        Pin 811df960 (File 81187820, <- "emu10k" 812567c0) Irps(q/p) = 0, 8
            Pending: 81255418 811df008 81252008 81255280 81250b30 ffa1fe70 81252e70 ffa01d98 
```

Splitter's input pin has no queued IRPs; however, it is waiting for the eight from emu10k to enter the queue.

```dbgcmd
Analyzing a Hung Graph From 812567c0:

Suspect Filters (For a Hung Graph):
 "emu10k" Filter ff9ebb98 or class "PortCls Wave Cyclic" is suspect.
        Reasons For This Analysis:
            - No critical pin has less than 8 queued Irps
            - Downstream "splitter" pin 811df960 is starved
        Irps to check:
 81255418 811df008 81252008 81255280 81250b30 ffa1fe70 81252e70 ffa01d98
```

From this information, the analyzer suggests that either emu10k or WaveCyclic may be at fault. It also provides a list of the suspect IRPs; these are the IRPs that are queued to emu10k's input pin. If any of those IRPs were to complete, splitter would copy data and complete an IRP and the graph would progress. For some reason, emu10k is not completing those capture Irps.

 

 





