---
title: Object Viewer Dialog Box
description: "The Object Viewer dialog box tracks different objects throughout the life span of the trace file."
ms.date: 05/10/2022
---

# Object Viewer Dialog Box  

The **Object Viewer** dialog box tracks different objects throughout the life span of the trace file. If you want to look up details about a particular object, this is the dialog box to use. 

The **Object Viewer** dialog resembles the **Event Listing** dialog in that it also uses the **Start Time** and **End Time** controls along with the time adjustment buttons. It differs in that rather than tracking events, the **Object Viewer** tracks objects that are created by GPUView when it processes events. These objects include: Adapters, Segments, Global Allocations, Processes, Devices, Contexts, Device Allocations, DMA Packets, and Queue Packets. The following diagram shows a number of these objects.

![object viewer dialog box 1](\Images\object-viewer-dialog-box-1.png)

Many of the objects that are displayed in this dialog have direct equivalents in the GPUView main window. The adapters will map to the GPU Hardware Queue. The Processes map to the process space and the association between processes and Contexts are also shown here. If you navigate into the Context items in the tree view, you will also find all the Queue Packets that are displayed on that Context CPU Queue in the main window.

**Object Tree**  

On the left side of the dialog box is the **Object tree** control. All objects that GPUView tracks should show up in this tree. Note that if the item is selected, the Object Viewer may provide more details about the item in the upper right-hand control. 

**Details Area**  

In the upper-right corner of the dialog box, is the **Details Area** control that contains the details for the object that is highlighted in the **Object tree** control. Any and all basic data that GPUView is aware of regarding the selected object is displayed in the **details area**. The Details Area control supports copy functionality. Therefore, you can select objects in the **Details Area** control, copy them into the clipboard, and paste them in the **Object to locate** control. 

**Object History**  

In the lower right-hand corner is a list that represents the history of an object, if it has some form of history. Events that GPUView logged against a particular object are listed in this list. In the following diagram, a memory block is selected that is known to have history.

![object viewer dialog box 2](\Images\object-viewer-dialog-box-2.png)

The preceding figure shows that all the events in the history list correspond to the single selected allocation from the **Object tree** control.  

The **Verbose History** check box affects the history list. In the preceding figure, the primary events that GPUView allows in the history list with **Verbose History** selected are excessive **DX - Dma Packet** events. 

Also, note that the history of an object can span more than just the time frame of the viewport. In the preceding figure, the events that exist within the viewport time frame are labeled with an asterisk (*). Events that are outside the viewport time period are left blank. 

**Locate Event**  

The **Locate Event** button locates events that you select from the history list in the context of the **Event Listing** dialog box. To view this functionality, select one of the events marked with an asterisk (*) and click the **Locate Event** button. GPUView brings the **Event Listing** dialog box to the foreground and highlights the specific event.  

> [!NOTE]
> When **Locate Event** is active, it does not change the state of the **Event Listing** dialog box. Therefore, if **Locate Event** does not find the event, you should ensure that there are no selections in the **GUID List** control of the **Event Listing** dialog box. Alternatively, you can select the GUID that corresponds to the type of event that you are trying to locate.   

**Object to Locate**  

If you know the value of the object to locate, you can type it into the **Object to locate** edit control and then press the **Locate** button. If GPUView finds the object in the corresponding time period, the object is highlighted in the **Object tree** control, and the object's details are displayed in the **Details Area** control accordingly. 

**Time Controls**  

The **Start Time** and **End Time** controls work just like the other dialog boxes. These times are used to limit the search span for objects.
