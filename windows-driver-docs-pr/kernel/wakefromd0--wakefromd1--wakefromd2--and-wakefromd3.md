---
title: WakeFromD0, WakeFromD1, WakeFromD2, and WakeFromD3
description: WakeFromD0, WakeFromD1, WakeFromD2, and WakeFromD3
keywords: ["WakeFromD0", "WakeFromD1", "WakeFromD2", "WakeFromD3"]
ms.date: 06/16/2017
---

# WakeFromD0, WakeFromD1, WakeFromD2, and WakeFromD3





Each of these [**DEVICE\_CAPABILITIES**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_capabilities) structure members indicates whether the device can awaken in response to an external signal that arrives when the device is in the specified state.

For a device that supports all four device power states (D0, D1, D2, D3) but can awaken only from states D0 and D1, the **WakeFromD0** and **WakeFromD1** bits are set, and the **WakeFromD2** and **WakeFromD3** bits are clear.

 

