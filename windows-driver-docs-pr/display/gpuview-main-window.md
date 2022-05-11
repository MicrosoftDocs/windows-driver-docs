---
title: GPUView Main Window
description: The following figure shows a screen shot of what first appears when GPUView is loaded after it has parsed the event file. 
ms.date: 05/10/2022
---

# GPUView Main Window

The following figure shows a screen shot of what first appears when GPUView is loaded after it has parsed the event file. During the parsing process, there are a number of events that GPUView understands, which it converts into logical objects that it displays in its client area. 

Because GPUView is a specialized tool that understands graphics operations, the client area is used to show the work as it progresses through time. 

Logically, the passage of time is displayed from left to right. Items that perform some operation in time are displayed along the timeline in rows or workflow queues.

![GPUView Display](\Image\gpuview-merged.png)
The following sections describe the GPUView display.

## Application Title Bar
The title bar displays three things: 

- The name of the file that GPUView is currently viewing 
- The unit of time for the start of the viewport area 
- The duration of time for the viewport area 

## Application Menu
Standard Windows menu that is covered in the GPUView Menu Options section.

## Timeline Ruler
The gray region represents the timeline for the current viewport area. The text in the upper left-hand side represents the time offset into the event file. The number in the parentheses is the unit of measurement. As you zoom in or out, the units change.

## GPU Hardware Queue
The blue region immediately below the Timeline Ruler is the GPU Hardware Queue Area. This is the area where GPUView displays information that represents the actual work done by the video hardware. As you zoom into smaller increments of time, the data view becomes more meaningful. Also, there will be one GPU Hardware Queue for each video adapter you have in the system. In this example, there is one adapter.

## Flip Queue
The Yellow region immediately below the GPU Hardware Queue is the display Flip Queue Area. The Flip Queue provides information that pertains to what is displayed on the monitor. Video adapters can drive multiple monitors and in this example, the event trace file that GPUView is viewing has two monitors. 

The Timeline Ruler, GPU Hardware Queue, and associated Flip Queues are part of what GPUView considers static client area. This area does not scroll. All the remaining area below is tied to the virtual scroll bar and is known as the Processes Workflow Area. 

## Idle - Process
The first green region is a process workflow that directly relates to CPU idle time. When GPUView parses the event file, it determines how many processors there are and determines when these processes are idle. Thus the Idle process shows you when work is not being done on the corresponding CPU. In the diagram above, you can see that the file that the events were generated on was a dual-core machine.

## All Remaining Processes
All the remaining green process regions show processes with the associated threads and video context queues. The items displayed in the process areas represent work being performed in that process on its threads. 

## The Status Bar
Finally, across the bottom of the application there is a status bar that provides specific details about the parse event file. There are eight fields. From left to right, the fields are the following:

- The Windows build upon which the event file was captured 
- The count of processors on that machine 
- The number of lost events during the time the event file was captured 
- The number of lost buffers 
- The pointer size 
- The client view display level summary-of-gpuview-controls.md
- The time in the file that corresponds to the mouse position (when the Track Mouse Cursor option is enabled) 
- The time length of the mouse selection 

## User Input - Common Actions on Main Window
Scrolling, zooming, and clicking are typically the actions performed on the main window. For more information about keyboard and mouse input functionality, see [Summary of GPUView Controls](summary-of-gpuview-controls.md).

 
