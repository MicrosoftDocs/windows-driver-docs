---
title: Viewing a Thread
description: Understanding the thread execution display of GPUView is critical to see where threads are active and where they perform video-specific functionality. 
ms.date: 05/10/2022
---

# Viewing a Thread

Understanding the thread execution display of GPUView is critical to see where threads are active and where they perform video-specific functionality. 

The following diagram is a screen shot of a fraction of a millisecond worth of time showing only the active threads that span two processes—the System process and the GPUView idle process. In this view, there are three threads shown.

![GPUView idle process](\Image\viewing-a-thread01.png) 

With each thread, the name is on the left-hand side, and a gray rectangular area on the right-hand side is where the Execution Intervals are shown. This entire area is known as the Thread Area.

## Thread Name

![Thread Name](\Image\viewing-a-thread02.png)

In the red ellipse in the preceding graphic, the thread ID appears in the parentheses followed by the module and function that spawned the thread. In this case, thread 432 created by dxgmms1.sys at offset 0x37DC0. If symbols are loaded, GPUView shows the symbolic name rather than the offset number. 

## Thread Execution Area

![Thread Execution Area](\Image\viewing-a-thread03.png)

The gray area to the right of the name, the Thread Execution Area, represents time when a thread could run. In this case, the thread did run twice during this time period.

## Thread Execution Interval

![Thread Execution Area](\Image\viewing-a-thread04.png)

In this case, the white rectangles represent when the thread actually ran. This diagram shows two Thread Execution Intervals.

## Details Text

![Details Text](\Image\viewing-a-thread05.png)

On the right-hand side just above the Thread Execution Area, details are provided regarding the thread's execution. The first number is the number of Execution Intervals during this time period. The second number, labeled iTime, is the amount of time DPCs ran on this thread. The third item is the total Execution Interval time, and the last item is the percentage of the viewport time that the thread ran.

## Details of the Execution Interval

![Details of the Execution Interval](\Image\viewing-a-thread06.png)

## Background Color

GPUView color-codes the background color of the Execution Interval to show the processor relationship. In the case of the preceding diagram, the Idle process has two threads, indicating that it is a dual-core machine. One processor was assigned the color white and the other bright green. As thread switches occur, GPUView paints the background with the processor information showing that when the system thread ran, it ran on the first processor. 

GPUView currently displays eight unique processor colors and supports up to 32 unique processors. 

## Thread Priority

The number displayed at the start of every Execution Interval is the thread's priority.

## Hardware or DPC Interruptions

Hardware Interrupts or Deferred Procedure Calls can run on any thread at any point in time. GPUView displays this information as crosshatched time in the Execution Interval. Hardware interruptions are shown in red crosshatches and DPCs are shown in blue.

![Hardware or DPC Interruptions](\Image\viewing-a-thread07.png)

In the preceding diagram, a DPC ran on the first idle core and, shortly thereafter, a hardware interruption occurred on the second idle core.

## Nested Execution Profiling

With some APIs, GPUView will show time spent in particular functions. This is known as Nested Execution in the Execution Interval. A significant portion of the video kernel logs events that denote when the thread has entered or left a particular routine.

![Nested Execution Profiling](\Image\viewing-a-thread08.png)

In the preceding diagram, the leftmost arrow points to Nested Execution time that is blue. Blue is a reserved color that denotes video kernel code. The second arrow points to Nested Execution time that is red. Red is reserved as video driver kernel code time. 

## Stack Walk Dots

![Stack Walk Dots](\Image\viewing-a-thread09.png)

If stack walking is enabled for the trace, GPUView shows them as dots just below the Execution Interval. In the preceding diagram, there are three Stack Walk dots for the two intervals.

## Non-Execution Time

If a thread is created or destroyed within the viewport time, GPUView will show the non-existence via a horizontal line. In the following diagram, the Viewport start time is represented by the vertical line just to the right of the thread name. The horizontal line, referenced by the red arrow, between it and the Execution Area represents time when the thread did not exist.

![Non-Execution Time](\Image\viewing-a-thread10.png)