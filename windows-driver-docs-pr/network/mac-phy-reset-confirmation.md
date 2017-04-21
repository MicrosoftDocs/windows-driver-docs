---
title: MAC/PHY Reset Confirmation
description: MAC/PHY Reset Confirmation
ms.assetid: 2fd93b09-94b2-437f-bf4c-97c12123b806
keywords:
- MAC/PHY reset WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MAC/PHY Reset Confirmation


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

If the miniport driver returned NDIS\_STATUS\_PENDING from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function when the method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) was made, the miniport driver completes the method request when the reset operation is complete by calling [**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622). The miniport driver confirms the completion of the reset operation by returning a [**DOT11\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff548782) structure in the following way:

-   Format the **InformationBuffer** member of the *OidRequest* parameter as a [**DOT11\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff548782) structure.

    The miniport driver sets the **uStatusType** member of the DOT11\_STATUS\_INDICATION structure to NDIS\_STATUS\_DOT11\_RESET\_CONFIRM.

    The miniport driver sets the **ndisStatus** member of the [**DOT11\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff548782) structure to NDIS\_STATUS\_SUCCESS if the reset operation completed successfully. If the reset operation failed, the miniport driver sets this member to the appropriate NDIS\_STATUS value.

-   Set the value of the **BytesRead** and **BytesWritten** members of the *OidRequest* parameter to the size of the DOT11\_RESET\_REQUEST structure. For more information about this structure, see [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409).

 

 





