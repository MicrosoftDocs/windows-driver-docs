---
title: Segment Viewer Window
description: The Segment Viewer displays information about the memory layout at a particular instant of time for a particular memory segment.
ms.date: 05/10/2022
---

# Segment Viewer Window

The Segment Viewer displays information about the memory layout at a particular instant of time for a particular memory segment. You can use the Segment Viewer window and its associated functionality in GPUView to view the memory layout and memory placement over time.

The Segment Viewer window can be launched by either pressing the **Segment Viewer** button after bringing up the Object Details of a Standard Dma Packet in the GPU Hardware Queue or by double-clicking the segment in the **Object Viewer Dialog Object** tree control.

A typical screen shot of the Segment Viewer window looks like the following.

:::image type="content" source="images/segment-viewer-window-01.png" alt-text="Screenshot of the Segment Viewer window in GPUView.":::

The area above the virtual scroll bar is a fixed area that is divided into four different sections.

The top section consists of the adapter handle value, the Segment index and attributes, the segment size, and the commit limit values.

The second section is the time location and memory event navigation buttons (arrows). The time value is the instant in the file that represents the information displayed. The buttons with the left- and right-pointing arrows reset the window to the previous or next memory event for that segment.

The third section is a summary section that provides a quick overview of the Allocated, Marked, and Free memory space at the currently viewed moment in time.

The last fixed area section is a continuation of the summary information. It shows the size of the largest free block and the largest free/marked block.

The rest of the window displays information about individual memory allocations on each row.

## Memory View Columns

The Default form of the Segment Viewer's memory rows is 14 columns wide. The main diagram (the preceding graphic) shows only nine of them. A horizontal scroll bar is provided for getting to the rightmost items.

* Change: This column holds either text or a graphic that indicates where the most recent memory operation occurred. If the current view time is next to a memory operation where memory is marked, the column will read marked. If the memory has been discarded, the column will show a left-pointing red triangle. If the item is paged in, the graphic will be a right-pointing yellow triangle, as in the following diagram.

:::image type="content" source="./images/segment-viewer-window-02.png" alt-text="Diagram showing a right-pointing yellow triangle in the Change column.":::

* PID: This column displays the Process ID followed by the process name followed by the Context CPU Queue assigned color.

* Dxg Adapter Allocation: This column displays the Dxgkernel Video Adapter Allocation memory address value.

* Vid MM Global Allocation: This column displays the Video Memory Manager Global Allocation memory address value.

* Placement: This column holds the placement value.

* Preference: This column holds the memory placement preferences.

* Priority: This column holds the Priority flags.

* Segment Offset: This column displays the memory locations offset into the segment.

* Size: This column displays the size of the memory.

* Width: This column displays the memory's width.

* Height: This column displays the memory's height.

* Format: This column displays the format of the memory.

* Locked: This column indicates whether the memory block is locked or not.

* Flags: This column displays the flags of the memory allocation as English words rather than hexadecimal bits.
