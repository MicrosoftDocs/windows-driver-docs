---
title: Other Visual Items of the Segment Viewer Window
description: When the Segment Viewer window is invoked from pressing the Segment Viewer button in the Object Details dialog that is displayed. 
ms.date: 05/10/2022
---

# Other Visual Items of the Segment Viewer Window

## Finding Standard Dma Packet Memory

When the Segment Viewer window is invoked from pressing the **Segment Viewer** button in the **Object Details** dialog that is displayed when you click on a Standard Dma Packet in the GPU Hardware Queue, it will highlight with a yellow background the memory addresses in the segment that match the memory addresses displayed in the **Object Details** dialog. 

The following two diagrams illustrate this association. Notice that the **Vid MM Global Allocation** field of the Segment Viewer window matches an entry in the second column of the **Object Details** dialog. To help the user see exactly what memory is referenced by the Standard DMA packet, the rows are highlighted with a yellow background.

The following two diagrams show this relationship. The first one is a clip of the **Object Details** dialog. 

![Object Details Merged.et](.\images\object-details-merged.png) 

The next is a clip of the Segment Viewer window.

![Segment Viewer](.\images\segment-viewer.png)

## Empty Memory Space
 
If a block of the Segment address space does not contain video content, it is known as empty space. The Segment Viewer window shows this empty space using gray crosshatches, as shown in the following diagram.

![Empty Memory Space](.\images\empty-memory-space01.png)
