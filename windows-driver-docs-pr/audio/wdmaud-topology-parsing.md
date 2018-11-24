---
title: WDMAud Topology Parsing
description: WDMAud Topology Parsing
ms.assetid: 8aa3e2e8-c9a2-4c3e-94b1-44a0dc218bf3
keywords:
- WDMAud topology parsing WDK audio
- topology parsing WDK audio
- source mixer lines WDK audio
- destination mixer lines WDK audio
- parsing destination mixer lines
- virtual sum WDK audio
- translating nodes WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDMAud Topology Parsing


## <span id="wdmaud_topology_parsing"></span><span id="WDMAUD_TOPOLOGY_PARSING"></span>


The [WDMAud system driver](user-mode-wdm-audio-components.md#wdmaud_system_driver) parses destination mixer lines first before parsing the source mixer lines. The order in which WDMAud parses the destination lines is the reverse of that in which SysAudio discovers the lines. For example, the higher numbered pins are parsed first. Parsing starts at the immediate parent of the pin and moves in the upstream direction. Each node is translated according to these rules until the parser detects one of the following terminating conditions:

-   The current node being parsed is a SUM node.

-   The current node is a MUX node.

-   The current node has multiple parents.

SUM and MUX nodes are the *classic terminators* of the destination line. A SUM node does not generate any controls. A MUX node generates a MUX control in the destination line that contains references to each of the source lines controlled by the MUX.

If multiple parents are discovered, parsing is immediately terminated. The mixer-line driver interprets this condition as a "virtual sum" that is formed by tying multiple inputs together.

The name of the destination line comes from the name returned from the [**KSPROPERTY\_PIN\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff565203) property on that pin.

After all destination line controls have been translated, WDMAud begins translating the source lines. Again, the order in which WDMAud parses these lines is the reverse of the order in which SysAudio queries them. Also, the direction in which source lines are parsed is opposite to that in which destination lines are parsed. WDMAud parses each line starting from the pin and proceeding in the downstream direction until it detects one of the following terminating conditions:

-   The parser finds a destination line.

-   The current node being translated belongs to a destination line.

-   The current node is a SUM node.

-   The current node is a MUX node.

When a MUX is encountered during parsing of a source line that belongs to a destination line, it is translated into a control. However, it is used only as a placeholder to update the line numbers in the MUX stored in the destination line later. The final line numbers are not yet available at this point, so a placeholder is required.

Both a MUX and a SUM node terminate a source line; therefore, any nodes between a SUM or MUX and another SUM or MUX are not translated.

## <span id="Notes"></span><span id="notes"></span><span id="NOTES"></span>Notes


1.  The line names in the MUX are derived from the pin name for the line, except when the line feeding into a MUX is from a SUM or MUX node. In that case, the name of the line is the name of the MUX or SUM node. When the mixer driver discovers this, it builds a virtual mixer line with the name of the SUM or MUX node and then translates all the controls between the SUM or MUX and the MUX.

2.  A *split* in the topology is a case where a node has more than a single child. This is useful when a single pin routes to two separate destinations but shares some common controls, such as volume or a mute. Any time a split is encountered, the WDMAud driver creates a new line and duplicates all the controls parsed up to the split. This happens unconditionally whenever a split is encountered, even after encountering a SUM node that terminates a source line.

 

 




