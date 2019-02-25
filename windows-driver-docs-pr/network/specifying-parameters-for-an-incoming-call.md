---
title: Specifying Parameters for an Incoming Call
description: Specifying Parameters for an Incoming Call
ms.assetid: f1436c05-f475-454c-b68f-e387821834d4
keywords:
- CoNDIS WAN drivers WDK networking , incoming calls
- telephonic services WDK WAN , incoming calls
- CoNDIS TAPI WDK networking , incoming calls
- voice streaming WDK networing , incoming calls
- incoming calls WDK CoNDIS WAN
- calls WDK CoNDIS WAN
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying Parameters for an Incoming Call





When indicating an incoming call with **Ndis(M)CmDispatchIncomingCall**, a call manager or MCM that supports voice streaming must specify the following values in the [**CO\_CALL\_MANAGER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff545381) structure:

-   Maximum transmit SDU size (CallMgrParameters-&gt;Transmit.MaxSduSize)

-   Maximum receive SDU size (CallMgrParameters-&gt;Receive.MaxSduSize)

In addition, a call manager or an MCM must specify the following values in the LINE\_CALL\_INFO structure:

-   **ulMediaMode**

    This field should contain LINEMEDIAMODE\_AUTOMATEDVOICE, which maps to TAPIMEDIAMODE\_AUDIO in TAPI 3.0.

-   **ulCallerIDFlags**

-   **ulCallerIDSize**

-   **ulCallerIDOffset**

-   **ulCallerIDNameSize**

-   **ulCallerIDNameOffset**

-   **ulCalledIDFlags**

-   **ulCalledIDSize**

-   **ulCalledIDOffset**

-   **ulCalledIDNameSize**

-   **ulCalledDNameOffset**

-   **ulCallerIDAddressType**

-   **ulCalledIDAddressType**

A call manager or MCM that supports an address family other than CO\_ADDRESS\_FAMILY\_TAPI\_PROXY specifies the preceding LINE\_CALL\_INFO members when responding to an [OID\_CO\_TAPI\_TRANSLATE\_NDIS\_CALLPARAMS](https://msdn.microsoft.com/library/windows/hardware/ff569099) query.

A call manager or an MCM that supports the CO\_ADDRESS\_FAMILY\_TAPI\_PROXY family specifies the above-listed LINE\_CALL\_INFO members in the media-specific portion of the CO\_CALL\_MANAGER\_PARAMETERS structure that it supplies to **Ndis(M)CmDispatchIncomingCall**.

For a description of the members in the LINE\_CALL\_INFO structure, see the LINECALLINFO structure in the Microsoft Windows SDK documentation.

 

 





