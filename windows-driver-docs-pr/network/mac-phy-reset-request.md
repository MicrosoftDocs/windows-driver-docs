---
title: MAC/PHY Reset Request
description: MAC/PHY Reset Request
ms.assetid: 2d1f6e72-c577-4e0f-97fe-bb81f4d62c1e
keywords:
- MAC/PHY reset WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MAC/PHY Reset Request


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When a method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) is made, the miniport driver must validate parameters for the reset request. If the data is valid, the miniport driver must initiate the reset operation and do one of the following:

Wait for the reset operation to complete before the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function returns.

Initiate the reset operation and return NDIS\_STATUS\_PENDING from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function. After the reset operation completes, the driver must call [**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622) to complete the method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) and confirm the completion of the reset operation. For more information about this procedure, see [MAC/PHY Reset Confirmation](mac-phy-reset-confirmation.md).

 

 





