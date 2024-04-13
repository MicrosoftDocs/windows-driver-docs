---
title: Opening and Closing a Parallel Port
description: Opening and Closing a Parallel Port
keywords:
- parallel ports WDK , opening
- parallel ports WDK , closing
- parallel ports WDK , sharing
ms.date: 03/03/2023
---

# Opening and Closing a Parallel Port





Clients can share a parallel port. A client must open a file on a parallel port before the client can use other I/O requests or use the [parallel port callback routines](/windows-hardware/drivers/ddi/index). A client must not attempt to communicate with a parallel port after the client has closed its file on the port.

Note that in a Plug and Play environment, a device can be removed or added whenever there are no open files on it. In general, every time a parallel port is added, Plug and Play assigns a different location and resources.

 

