---
title: Indicating CoNDIS WAN Miniport Driver Status
description: Indicating CoNDIS WAN Miniport Driver Status
ms.assetid: c12492d7-e25d-4c80-8f2d-1e89931577ed
keywords:
- CoNDIS WAN drivers WDK networking , status
- status indications WDK networking , CoNDIS WAN miniport drivers
- NDIS_STATUS_WAN_CO_LINKPARAMS
- NDIS_STATUS_WAN_CO_FRAGMENT
- indications WDK CoNDIS WAN
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Indicating CoNDIS WAN Miniport Driver Status





A CoNDIS WAN miniport driver calls [**NdisMCoIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563562) to indicate status changes up to bound protocol drivers. For more information about indicating status from a CoNDIS miniport driver or MCM, see [Indicating Miniport Driver Status](indicating-miniport-driver-status.md).

Bound protocol drivers can ignore these status indications. However, processing these indications typically results in improved performance for protocol drivers and the miniport driver.

The NDISWAN intermediate driver forwards status indications to NDIS. NDIS calls the [**ProtocolCoStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff570258) functions of bound protocol drivers or a configuration manager. These protocol drivers or configuration manager can log these indications and possibly take corrective action, if necessary.

For a CoNDIS WAN miniport driver, a call to [**NdisMCoIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563562) is the same as in any CoNDIS miniport driver, except that the CoNDIS WAN miniport driver indicates a WAN-specific status for each virtual connection (VC) on the miniport driver's NIC. The miniport driver calls **NdisMCoIndicateStatusEx** with an explicit VC handle to indicate these changes up to a protocol driver that shares this VC. If the driver specifies a **NULL***NdisVcHandle*, the status pertains to a general change in the state of the NIC.

Each status indication provides two basic pieces of information:

-   A status code that specifies the general status. There are a limited number of defined general status codes; this list is subject to future expansion.

-   A buffer that contains the status information. This status information can be specific to a NIC, or, for a CoNDIS WAN miniport driver, specific to a VC on a NIC. For example, a buffer might contain the new transmit speed of an X.25 connection, which recently decreased by a factor of two.

The CoNDIS WAN VC status indications are:

-   NDIS\_STATUS\_WAN\_CO\_LINKPARAMS

    A CoNDIS WAN miniport driver calls [**NdisMCoIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563562) to indicate that the parameters for a particular VC that is active on the NIC have changed. In this call, the miniport driver passes the handle to the VC in the *NdisVcHandle* parameter, NDIS\_STATUS\_WAN\_CO\_LINKPARAMS in the *GeneralStatus* parameter, and a pointer to a [**WAN\_CO\_LINKPARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff565819) structure in the *StatusBuffer* parameter. WAN\_CO\_LINKPARAMS describes new parameters for the VC.

-   NDIS\_STATUS\_WAN\_CO\_FRAGMENT

    A CoNDIS WAN miniport driver calls **NdisMCoIndicateStatusEx** to indicate that it has received a partial packet from the endpoint of a VC. In this call, the miniport driver passes the handle to the VC in the *NdisVcHandle* parameter, NDIS\_STATUS\_WAN\_CO\_FRAGMENT in the *GeneralStatus* parameter, and a pointer to an [**NDIS\_WAN\_CO\_FRAGMENT**](https://msdn.microsoft.com/library/windows/hardware/ff559030) structure in the *StatusBuffer* parameter. NDIS\_WAN\_CO\_FRAGMENT describes the reason that the partial packet was received.

    After this indication occurs, a connection-oriented client should send frames to the connection-oriented client at the other end of the VC. These frames will notify the opposite endpoint of the partial-packet situation, so that the opposite endpoint is not required to wait for a time-out to occur.

    NDISWAN monitors dropped packets by counting the number of fragment indications on each VC.

 

 





