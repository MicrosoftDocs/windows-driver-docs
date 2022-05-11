---
title: GPU Hardware Queue
description: This topic provides information about what the user views when looking at the GPU Hardware Queue. 
ms.date: 05/10/2022
---

# GPU Hardware Queue

This topic provides information about what the user views when looking at the GPU Hardware Queue. This first diagram is a simple zoomed-in view of the GPU Hardware Queue.

![](\Image\gpu-hardware-queue01.png)

The GPU Hardware Queue represents workflow on the hardware. In these workflow queues, the item on the bottom of the stack of rectangles represents the work that is currently executing. The rectangles stacked above it represent work that is in waiting.

![](\Image\gpu-hardware-queue02.png)

In the preceding diagram, the DMA packet inside the red ellipse represents the work that the hardware was executing, and the DMA packet in the black ellipse represents the second packet of two that the video scheduler placed down on the hardware. They are packets in waiting.

![](\Image\gpu-hardware-queue03.png)

Notice that the end of a rectangle does not mean the end of the functional lifetime of the object. Here, inside the red ellipse, when the hardware finished with the present packet (item on the bottom), the DMA packet in waiting now transitions into the DMA packet being processed by the hardware. At this transition point, the topmost DMA packet in waiting advances (down) one step closer to actually running on the hardware.

Zooming out just a little bit and left-clicking the top DMA packet produces the following diagram.

![](\Image\gpu-hardware-queue04.png)

This DMA packet was selected by left-clicking it. Notice that the packet has three transitional points while it is in the queue. The entire time span of this object is considered time in the hardware queue, but only the last section (rightmost where it is on the bottom of the stack) is counted as execution time on the hardware. 

The color coding is also important. The color for each DMA packet corresponds to a particular Context CPU Queue in a particular Process. 

![](\Image\gpu-hardware-queue05.png)

Zooming out a little from the previous diagram, the associated process is (6584) SchBillboard.exe. It has the matching color and matching selection in process Context CPU Queue. 

There is also the text in the upper right-hand corner of the GPU Hardware Queue area. It can be seen in the following diagram. 

![](\Image\gpu-hardware-queue06.png)

The first item is the count of DMA packets that received execution time on the hardware. The second value is the time of these executing packets. The third is the percentage of the viewport area where DMA packets were executing on the hardware. 

## Types of DMA Packets

![](\Image\gpu-hardware-queue07.png)

Four types of DMA packets are found in the GPU Hardware Queue. 

The most common are Standard DMA Packets and Present Packets. Both of these packets represent client requests on the hardware. 

The two types of DMA packets that are less common are Paging Packets and Preemption Packets. Paging Packets are always red and Preemption Packets are always black. Both these packets are placed in the GPU Hardware Queue on behalf of the video scheduler. Paging Packets occur when data needed for processing needs to be pre-fetched. Preemption Packets are generated when the scheduler determines that it needs to abort the current work flow to provide some higher-priority content. 

## Selectable Areas

All DMA Packets are selectable via a left mouse click. All selectable items show this capability through changing the mouse pointer into the hand icon. When a DMA Packet is selected, the **Object Details** dialog is launched containing information about the particular DMA packet selected. 

