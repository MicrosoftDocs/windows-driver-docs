---
title: Using ks.graph
description: Using ks.graph
ms.assetid: 05dcd5d3-fac6-4af5-8149-955435fb016f
keywords: ["kernel streaming debugging, displaying a graph"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using !ks.graph


The [**!ks.graph**](-ks-graph.md) command is one of most powerful extension commands in the kernel streaming extension module. This command displays a picture of an entire graph in kernel mode from any given starting point.

Before running [**!ks.graph**](-ks-graph.md), you may want to enable all library extensions that are capable of being active. To do this, issue a [**!ks.libexts enableall**](-ks-libexts.md) command. The output of **!ks.graph** will be a textual description of the kernel mode graph in topologically sorted order. Here is an example:

```dbgcmd
kd> !graph ffa0c6d4 7
Attempting a graph build on ffa0c6d4...  Please be patient...
Graph With Starting Point ffa0c6d4:
"usbaudio" Filter ffaaa768, Child Factories 2
    Output Factory 0:
        Pin ffb1caf0 (File 811deeb8, -> "splitter" ffa8b008) Irps(q/p) = 7, 1
```

This example displays a capture graph in which two Sndrec32.exe's are capturing from a Telex USB Microphone. Each individual record begins with a name (usbaudio, in the above section) and shows the filter address (0xFFAAA768) and quantity of child pin factories (2) on the filter.

Below each entry, each factory is enumerated and lists the address of each pin instance (0xFFB1CAF0), the file object (0x811DEEB8) corresponding to each instance, the direction of the connection, the destination of that connection, and the address of the destination pin (0xFFA8B008). The number of queued (7) and pending IRPs (1) for each pin is also displayed.

Connections which have forward direction symbols (-&gt;) indicate that the pin is an output pin and is connected to an input pin. Connections which have reverse direction symbols (&lt;-), on the other hand, are input pins and show the origination of the connection. The output continues as follows:

```dbgcmd
"splitter" Filter ffa0c660, Child Factories 2
    Output Factory 0:
        Pin 81250008 (File ffb10028, -> "kmixer" 8123c000) Irps(q/p) = 3, 0
        Pin 811df9c0 (File ffaaf2f0, -> "kmixer" 81236000) Irps(q/p) = 3, 0
    Input Factory 1:
        Pin ffa8b008 (File ffb26d68, <- "usbaudio" ffb1caf0) Irps(q/p) = 1, 7
"kmixer" Filter ffa65b70, Child Factories 4
    Input Factory 2:
        Pin 81236000 (File ffaaf7d0, <- "splitter" 811df9c0) Irps(q/p) = 0, 0
    Output Factory 3:
        Pin 81252d00 (File 811df1d8) Irps(q/p) = 10, 0
"kmixer" Filter ffb03808, Child Factories 4
    Input Factory 2:
        Pin 8123c000 (File ffb10130, <- "splitter" 81250008) Irps(q/p) = 0, 0
    Output Factory 3:
        Pin ffa1e9c0 (File 81253468) Irps(q/p) = 10, 0
```

In order to follow the graph, use the following procedure:

**To follow this graph:**

1.  Find the pin of interest. Consider 0xFFB1CAF0, usbaudio's output pin (factory 0).

2.  Find the connected pin. In this example, this is splitter pin 0xFFA8B008.

3.  Look at the connection direction and visually move that way looking for the filter name. (Remember, the list is topologically sorted.) In this example, the right-pointing arrow indicates that we need to look below this entry in the list to find the corresponding pin. The splitter filter 0xFFA0C660 is immediately below.

4.  Find the destination pin address in the filter pin instance list. In this case, this address is 0xFFA8B008.

The To follow this graph: command can also be used to analyze stalled graphs from any given starting point. To do this, specify 4 in the *Flags* parameter:

```dbgcmd
kd> !graph 812567c0 7 4

Attempting a graph build on 812567c0...  Please be patient...

Graph With Starting Point 812567c0:

"emu10k" Filter ff9ebb98, Child Factories 5
    Output Factory 0:
        Pin 812567c0 (File 811c6630, -> "splitter" 811df960) Irps(q/p) = 8, 0
"splitter" Filter ffb18890, Child Factories 2
    Output Factory 0:
        Pin 811df430 (File ffa55f90) Irps(q/p) = 10, 0
    Input Factory 1:
        Pin 811df960 (File 81187820, <- "emu10k" 812567c0) Irps(q/p) = 0, 8

Analyzing a Hung Graph From 812567c0:

Suspect Filters (For a Hung Graph):
    "emu10k" Filter ff9ebb98 or class "PortCls Wave Cyclic" is suspect.
        Reasons For This Analysis:
            - No critical pin has less than 8 queued Irps
            - Downstream "splitter" pin 811df960 is starved
        Irps to check:
            81255418 811df008 81252008 81255280 81250b30 ffa1fe70 81252e70 ffa01d98

NOTE: The above is based on heuristic analysis.  It is not designed to be a
      replacement for an actual developer looking at this particular hang!  The
      filters listed as suspects may or may not be the actual cause of the
      stall!
```

For such output, look at the "suspects" list. These suspect filters are those that are in the critical path of progress being made in the graph. Begin debugging from that point based on the reasons that the analyzer has produced for the stall.

**Note**   This functionality should only be used on stalled graphs! The analyzer has no way of knowing how long the graph has been in this state. Breaking into the debugger and analyzing a running graph as a stalled graph still displays a suspect filter.

 

 

 





