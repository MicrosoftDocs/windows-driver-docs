---
title: MB Signal Strength Operations
description: MB Signal Strength Operations
ms.assetid: 489299d0-29c5-4885-ae68-f3d0f42bd201
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB Signal Strength Operations


This topic describes the operations to report signal strength.

These operations require access to the network provider, but not to the Subscriber Identity Module (SIM card).

Be aware that in case of GSM-based devices, miniport drivers should send signal strength notifications only after the miniport driver has successfully registered with a network provider. For CDMA-based devices, miniport drivers can send signal strength notifications before the miniport driver has successfully registered with a network provider.

For more information about signal strength operations, see [OID\_WWAN\_SIGNAL\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569836).

 

 





