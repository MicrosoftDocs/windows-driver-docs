---
title: Pausing a Driver Stack
description: Pausing a Driver Stack
keywords:
- driver stacks WDK networking , pausing
- pausing driver stacks WDK networking
ms.date: 04/20/2017
---

# Pausing a Driver Stack





NDIS pauses a driver stack to complete operations such as inserting a filter module or adding a binding. In general, a driver stack pause operation proceeds as follows:

1.  NDIS sends a PnP pause event to the protocol driver.

    The binding enters the Pausing state. After all outstanding send requests are complete, the protocol driver completes the PnP event. The binding is in the Paused state.

2.  NDIS pauses all the filter modules, beginning at the top of the stack and progressing down to the miniport driver.

    After NDIS calls the filter driver's [*FilterPause*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_pause) function, the filter module enters the Pausing state. After NDIS returns all outstanding receive indications, and all outstanding send operations are complete, the filter module enters the Paused state.

3.  NDIS pauses the miniport adapter.

    After NDIS calls the miniport driver's [*MiniportPause*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pause) function, the miniport adapter enters the Pausing state. After NDIS returns all outstanding receive indications, the miniport adapter enters the Paused state.

**Note**  NDIS drivers cannot fail a pause request. You should log any errors that occur.

 

 

