---
title: Context CPU Queue
description: The following is a zoomed-in screen shot that shows the GPU Hardware Queue along with the Context CPU Queues of four processes.
ms.date: 05/10/2022
---

# Context CPU Queue

The following is a zoomed-in screen shot that shows the GPU Hardware Queue along with the Context CPU Queues of four processes.

![Context CPU Queues of four processes](\Image\context-cpu-queues01.png) 

The association between the Context CPU Queue items and the items in the GPU Hardware Queue is one of the most fundamental relationships in GPUView. In the preceding diagram, the leftmost red arrow points to the Context CPU Queue color key. The bottom red arrow points to a corresponding data item in the Context CPU Queue and the uppermost red arrow points to a DMA Packet in the GPU Hardware Queue that came from the Dwm.exe process's Context CPU Queue. At any moment in time, you can see what application (Process) has work down on the GPU by looking at the color of the blocks in the GPU Hardware Queue. 

Because Windows virtualizes the video hardware, the work that is performed in the Context CPU Queue represents the graphics workload queued to the hardware, but not actually being processed by the hardware. The following diagram may help with seeing the relationship between the Context CPU Queue and the GPU Hardware Queue. 

![Context CPU Queue and the GPU Hardware Queue](\Image\context-cpu-queues02.png) 

Here, the application submitted work for the GPU at the point of the leftmost red arrow. Already in the queue were two other work items, denoted by the leftmost light blue arrows. Looking above in the GPU Hardware Queue, you see that some other processes had work down on the GPU, and it is not until much later that you finally see the first two work items for the application run in the GPU Hardware Queue (light blue arrows in the GPU Hardware Queue). Eventually, the highlighted work item (Queue Packet) makes it into the GPU Hardware Queue (denoted by the black arrow) and shortly thereafter runs to completion (two yellow arrows). Just after that, the application finally sees the work as being done (rightmost red arrow). Even through the Work Item (Queue Packet) took only 1.5 milliseconds to execute on the hardware, it had to wait for its turn on this very busy machine. To the application, it took about 28 milliseconds from the time it was submitted to the time it was completed.

## Details of the Context GPU Queue

The layout of the Context CPU Queue is similar to the layout of the GPU Hardware Queue.

![Context CPU Queue and the GPU Hardware Queue](\Image\context-cpu-queues03.png)

## Color Key
The leftmost rectangle shows the color key for all work items (Queue Packets) in the Context CPU Queue. This color key helps when identifying where the GPU Hardware Queue is spending its time.

## Context Queue Area
The gray area denotes the Context Queue Area.

## Context CPU Queue Text
The text above the Context Queue Area provides details about the work being performed in the Context and associated work in the GPU Hardware Queue. The first number is the count of items that actually ran in the Context CPU Queue during the given viewport time. (Note that it is a count of the number of items in the bottom row of the Context CPU Queue). After that is the amount of time that these work items (Queue Packets) spent executing in the GPU Hardware Queue and the associated percentage of the Viewport. Following that is the same calculation for the Context CPU Queue items.

## Context CPU Queue Items
The solid-color rectangles in the Context CPU Queue represent standard Queue Packets. This is work for the GPU. The crosshatched rectangles are present packets and the rectangles with diagonal lines represent Present Token Packets.

## Flip Surface
In the Context CPU Queue associated with the Dwm.exe process, GPUView provides the Flip Surface address in the Present Packet rectangles. The first number is the Flip Queue. The second number is the address of the surface that will be flipped. This number can typically be found in the DMA Packet that finished just before the Present Packet was issued.

## Note about Queues
The Queues, as seen by GPUView, are stacks of work queued up and waiting to be executed. In the display, the item on the bottom of the stack (bottom row) is the item that is actually being worked on at that specific moment in time. The next item waiting to be worked on is stacked on top of the one that is executing. A transition point is the moment that one work item finishes and the one in waiting now becomes the next one worked on. These transition points give a stair step look to the queue as work is performed and packets are completed. The newest items added to the queue always get placed on top. 