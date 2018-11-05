---
title: Restarting a Driver Stack
description: Restarting a Driver Stack
ms.assetid: 5c9138f8-4a29-4740-b085-efe24d950fba
keywords:
- driver stacks WDK networking , restarting
- restarting driver stacks WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Restarting a Driver Stack





NDIS restarts a driver stack after operations such as inserting a filter module or adding a binding. A driver stack restart operation proceeds as follows:

1.  NDIS restarts the miniport adapter.

    After NDIS calls the miniport driver's [**MiniportRestart**](https://msdn.microsoft.com/library/windows/hardware/ff559435) function, the miniport adapter enters the Restarting state. The miniport driver prepares to resume send and receive operations. If the preparation fails, the miniport adapter returns to the Paused state. After the driver is ready to resume send and receive operations, the miniport adapter enters the Running state.

2.  NDIS restarts the filter modules, beginning at the bottom of the driver stack and progressing up to the protocol driver.

    After NDIS calls a filter driver's [**FilterRestart**](https://msdn.microsoft.com/library/windows/hardware/ff549962) function, the filter module enters the Restarting state. The filter driver prepares to resume send and receive operations. If the preparation fails, the module returns to the Paused state. After the driver is ready to resume send and receive operations, the filter module enters the Running state.

3.  NDIS sends a PnP restart event to the protocol driver.

    The binding enters the Restarting state. The protocol driver prepares to resume send and receive operations. If the preparation fails, the binding returns to the Paused state. After the protocol driver is ready to resume send and receive operations, the binding enters the Running state.

 

 





