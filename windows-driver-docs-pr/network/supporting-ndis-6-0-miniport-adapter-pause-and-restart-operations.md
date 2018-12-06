---
title: Supporting NDIS 6.0 Miniport Adapter Pause and Restart Operations
description: Supporting NDIS 6.0 Miniport Adapter Pause and Restart Operations
ms.assetid: 88b9fe8f-2bdd-44e0-bcb9-58c815a68cce
keywords:
- miniport adapters WDK networking , pause and restart operations
- adapters WDK networking , pause and restart operations
- porting miniport drivers WDK networking , adapters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting NDIS 6.0 Miniport Adapter Pause and Restart Operations





The miniport adapter pause and restart capabilities are new features that are introduced in NDIS 6.0.

NDIS calls a miniport driver's [*MiniportPause*](https://msdn.microsoft.com/library/windows/hardware/ff559418) function to stop data flow before performing a Plug and Play operation, such as adding or removing a filter driver or binding or unbinding a protocol driver. The miniport adapter remains in the *Pausing* state until the pause operation has completed.

NDIS calls the miniport driver's [**MiniportRestart**](https://msdn.microsoft.com/library/windows/hardware/ff559435) function to return the miniport adapter to the *Running* state.

For more information about pause and restart operations, see [Driver Stack Management](driver-stack-management.md).

 

 





