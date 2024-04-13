---
title: Power-Down and Removal Sequence for a Function or Filter Driver
description: Power-Down and Removal Sequence for a Function or Filter Driver
ms.date: 04/20/2017
---

# Power-Down and Removal Sequence for a Function or Filter Driver


The following figure shows the order in which the framework calls a KMDF function or filter driver's event callback functions when powering down and removing the device. The sequence starts at the top of the figure with an operational device that is in the working power state (D0):

:::image type="content" source="images/fdo-fido-powerdown3.png" alt-text="Flowchart showing the power-down and removal sequence for a KMDF function or filter driver.":::

As the figure shows, the KMDF power-down and removal sequence involves calling the corresponding "undo" callbacks in the reverse order in which the framework called the functions that are involved in making the device operational. The framework deletes the device object after it deletes the device object context area.

 

 





