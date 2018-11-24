---
title: Porting I/O
description: Porting I/O
ms.assetid: D65B85C4-401F-4143-9626-5C16E24925A0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting I/O


KMDF drivers handle I/O requests by creating one or more queues and associating one or more I/O event callback functions with each queue. To port a WDM driver’s I/O handling code to KMDF:

-   [Port I/O queues](creating-i-o-queues.md).

-   [Port I/O dispatch routines](porting-i-o-dispatch-routines-to-i-o-event-callback-functions.md) to I/O event callbacks.

-   [Revise code that handles completed requests](revise-completed-request-logic.md).

-   [Revise Canceled Request Logic](revise-canceled-request-logic.md).

-   [Revise Forward Request Logic](revise-forward-request-logic.md).

-   [Revise code that issues I/O requests](revise-code-that-issues-i-o-requests.md).

 

 





