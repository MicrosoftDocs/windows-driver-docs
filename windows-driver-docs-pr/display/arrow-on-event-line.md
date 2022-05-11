---
title: Arrow on Event Line
description: "When events are selected in different dialogs, a line is drawn in GPUView's main window to denote the position of the event."
ms.date: 05/10/2022
---

# Arrow on Event Line  

When events are selected in different dialogs, a line is drawn in GPUView's main window to denote the position of the event. If that event is known to have run on a particular thread, GPUView draws an arrow just above the thread to help direct the user's eye to the correct thread. The following diagram illustrates this point.  

If the event has no clear owner, no arrow appears on the line.   

There are also two navigation arrows that point either up or down if the thread is visible in the viewport but scrolled out of view. The following image shows a black arrow pointing up. The arrow is drawn on the Event Line at the top of the scrollable area.   

Likewise, if the thread is visible, but below the client area of the window, GPUView draws a black arrow pointing down (as in the following diagram).  

If the event is known to have an owner but the current viewing level makes it so the thread is not visible, GPUView draws a circle on the Event Line at the junction of the scrollable and nonscrollable areas, as in the following diagram.  

In the case where a circle is drawn on the Event Line, adjusting the viewing level eventually brings the thread into view.

