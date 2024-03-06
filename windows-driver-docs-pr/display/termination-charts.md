---
title: Termination Charts
description: The Termination Charts are both adapter- and process-specific.
ms.date: 05/10/2022
---

# Termination Charts

The Termination Charts are both adapter- and process-specific. They show memory that is submitted for discarding. It basically adds up the amount of memory waiting to be discarded. The color key shows Local, System, and DMA buffer memory. The following diagrams show these charts.

:::image type="content" source="images/adapter-level.png" alt-text="Diagram that shows the adapter level Termination Chart.":::

Note that the Termination Charts at the adapter level are displayed in their own blue gradient area just above the associated adapter.

:::image type="content" source="images/process-level.png" alt-text="Diagram that shows the process level Termination Chart.":::

In the case of the process Termination Chart, the chart is shown between the Context CPU Queue and the first thread.

The reason why these charts look more like bar charts is that the value represents the amount of memory waiting to be discarded, and the work performed to discard the memory usually consumes all of it. Thus, we get a count, followed by no count which bounces between zero and some number.
