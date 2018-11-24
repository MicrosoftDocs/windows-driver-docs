---
title: Power-Down and Removal Sequence for a Function or Filter Driver
description: Power-Down and Removal Sequence for a Function or Filter Driver
ms.assetid: E5A22C91-5967-42D6-A991-42B46C72ED82
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Power-Down and Removal Sequence for a Function or Filter Driver


The following figure shows the order in which the framework calls a KMDF function or filter driver's event callback functions when powering down and removing the device. The sequence starts at the top of the figure with an operational device that is in the working power state (D0):

![power-down and removal sequence for a function or filter driver](images/fdo-fido-powerdown3.png)

As the figure shows, the KMDF power-down and removal sequence involves calling the corresponding "undo" callbacks in the reverse order in which the framework called the functions that are involved in making the device operational. The framework deletes the device object after it deletes the device object context area.

 

 





