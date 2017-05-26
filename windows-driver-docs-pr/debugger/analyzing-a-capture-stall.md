---
title: Analyzing a Capture Stall
description: Analyzing a Capture Stall
ms.assetid: 9a88deba-374c-4ccc-8bb8-18e3b4124158
keywords: ["kernel streaming debugging, blah"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Analyzing a Capture Stall


The following is an artificially created scenario that simulates a capture stall. This is a particularly valuable scenario since similar situations frequently occur in stress testing. The scenario is as follows:

The Windows recording component Sndrec32 is recording from the primary capture device, in this case a Creative SBLive wave device. For a period of time, it records normally; however, the graph stalls at 8.50 seconds because we have explicitly caused portcls not to complete capture IRPs for purposes of this test.

The application shows running, but the stream position is not advancing. Position is halted at 8.50 seconds.

Since the primary capture device on this machine is a PCI sound card, first use the [**!ks.pciaudio**](-ks-pciaudio.md) command to try and determine a starting point. Use a flag value of 1 to request a display of all running streams:

```
kd> !pciaudio 1

1 Audio FDOs found:
 Functional Device 8121c030 [\Driver\emu10k]
        Wave Cyclic Streams:
            Pin 812567c0 RUN [emu10k1m!CMiniportWaveCyclicStreamSBLive ff9ec7f8] 
```

In this case, there is only one PCI audio device and it is serviced by the Intel emu10k driver (\\Driver\\emu10k). This driver currently has a single running stream (0x812567C0). Now you can use [**!ks.graph**](-ks-graph.md) to view the kernel graph. Set *Level* and *Flags* both to 7 to obtain maximum detail on the stall:

```
kd> !graph 812567c0 7 7
Attempting a graph build on 812567c0...  Please be patient...
Graph With Starting Point 812567c0:
"emu10k" Filter ff9ebb98, Child Factories 5
    Output Factory 0:
        Pin 812567c0 (File 811c6630, -> "splitter" 811df960) Irps(q/p) = 8, 0
 Queued: 81255418 811df008 81252008 81255280 81250b30 ffa1fe70 81252e70 ffa01d98 
```

The above shows the details for factory 0. The emu10k output pin 0x812567C0 is connected to the splitter input pin 0x811DF960. There are eight IRPs queued to emu10k's output pin. The output from [**!ks.graph**](-ks-graph.md) continues as follows:

```
"splitter" Filter ffb18890, Child Factories 2
    Output Factory 0:
        Pin 811df430 (File ffa55f90) Irps(q/p) = 10, 0
 Queued: ffadd008 ffa73b00 ffa1e998 811de310 ffa54370 ffaaf008 811dee70 81250e70 811de580 811de8c0 
```

There are ten IRPs queued to splitter's output pin.

```
    Input Factory 1:
        Pin 811df960 (File 81187820, <- "emu10k" 812567c0) Irps(q/p) = 0, 8
            Pending: 81255418 811df008 81252008 81255280 81250b30 ffa1fe70 81252e70 ffa01d98 
```

Splitter's input pin has no queued IRPs; however, it is waiting for the eight from emu10k to enter the queue.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Analyzing%20a%20Capture%20Stall%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




