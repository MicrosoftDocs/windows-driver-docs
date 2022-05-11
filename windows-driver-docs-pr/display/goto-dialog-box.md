---
title: Goto Dialog Box
description: "The Goto dialog box is a navigational helper."
ms.date: 05/10/2022
---

# Goto Dialog Box  

The **Goto** dialog box is a navigational helper. When sharing ETL files, a user might have already isolated the problem area. The **Goto** dialog box helps set up the main viewing area around the known problematic region. All times in this dialog box are in base measurement units; therefore, 10,000,000 is equal to one second. 

The following figure shows the **Goto** dialog box when the **Duration** check box is selected.

In the preceding figure, the **Start** value is used for the left side of the main window. The **Duration** value corresponds to the amount of time that the main window displays from the **Start** location.

The following figure shows the **Goto** dialog box when the **Duration** check box is cleared.

In the preceding figure, the **Start** value is used for the left side of the main window. The difference between the **Start** and **end** values corresponds to the amount of time for which the main window is displayed. 

Note  If the **Duration** check box is cleared, the view and the operation of the **Goto** dialog box changes from the "**Goto** dialog box with **Duration** selected" figure to the "**Goto** dialog box with **Duration** cleared" figure.

If you know that the problematic area is 1 second long and 8.5 seconds into the file, you would set **Start** to 85,000,000, clear **Use 64 ms Duration**, and set the **Duration** text box to 10,000,000. These settings provide you with one second of time. Alternatively, you can clear the **Duration** check box and type both the **Start** and **end** times in the **Start** and **end** text boxes, respectively. 

The **Save** button records the current view so that you can **Restore** the view later. 

The **Restore** button applies the previously saved values. 

The **Goto** button applies the view changes and exits the dialog box. 

