---
title: Non-WAN-Specific Extensions for TAPI Over Connection-Oriented NDIS
description: Non-WAN-Specific Extensions to Support Telephonic Services Over Connection-Oriented NDIS
ms.assetid: be677971-8c4a-435a-81b1-ff1ad9d849b4
keywords:
- CoNDIS WAN drivers WDK networking , TAPI services
- telephonic services WDK WAN , non-WAN-specific extensions
- CoNDIS TAPI WDK networking , non-WAN-specific extensions
- NDIS/TAPI translation OIDs WDK networking
- connection-oriented NDIS WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Non-WAN-Specific Extensions to Support Telephonic Services Over Connection-Oriented NDIS





This topic describes non-WAN-specific extensions for TAPI support over connection-oriented NDIS. These extensions are the NDIS/TAPI translation OIDs. These extensions allow non-WAN-specific call managers and integrated miniport call manager (MCM) drivers to translate TAPI parameters to NDIS parameters or TAPI parameters to NDIS parameters. These extensions allow call managers and MCMs that support ATM, for example, to provide TAPI access over connection-oriented media. For information about WAN-specific extensions for TAPI support over connection-oriented NDIS, see [CoNDIS WAN Operations that Support Telephonic Services](condis-wan-operations-that-support-telephonic-services.md).

The NDIS/TAPI translation OIDs should not be used for call managers or MCMs that respectively register CO\_ADDRESS\_FAMILY\_TAPI\_PROXY with [**NdisCmRegisterAddressFamilyEx**](https://msdn.microsoft.com/library/windows/hardware/ff561685) or [**NdisMCmRegisterAddressFamilyEx**](https://msdn.microsoft.com/library/windows/hardware/ff563554). Instead, such call managers and MCMs, as well as their TAPI clients, should encapsulate TAPI parameters inside connection-oriented structures, as described in [CoNDIS WAN Operations that Support Telephonic Services](condis-wan-operations-that-support-telephonic-services.md).

The NDIS/TAPI translation OIDs are as follows:

-   [OID\_CO\_TAPI\_TRANSLATE\_TAPI\_CALLPARAMS](https://msdn.microsoft.com/library/windows/hardware/ff569100)

    This OID requests a call manager or MCM to translate TAPI call parameters supplied by the client to NDIS call parameters. The client typically uses the NDIS call parameters returned by the call manager or MCM as an input (formatted as a [**CO\_CALL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff545384) structure) to [**NdisClMakeCall**](https://msdn.microsoft.com/library/windows/hardware/ff561635). The client uses **NdisClMakeCall** to initiate a connection-oriented call.

-   [OID\_CO\_TAPI\_TRANSLATE\_NDIS\_CALLPARAMS](https://msdn.microsoft.com/library/windows/hardware/ff569099)

    This OID requests a call manager or MCM to translate NDIS call parameters for an incoming call (passed in a CO\_CALL\_PARAMETERS structure to the client's [**ProtocolClIncomingCall**](https://msdn.microsoft.com/library/windows/hardware/ff570228) function) to TAPI call parameters. The client uses the translated TAPI call parameters returned by the call manager or MCM to determine whether to accept or reject the incoming call.

-   [OID\_CO\_TAPI\_TRANSLATE\_SAP](https://msdn.microsoft.com/library/windows/hardware/ff569101)

    This OID requests a call manager or MCM to prepare one or more NDIS SAPs from TAPI call parameters that are supplied by the client. The client typically uses an NDIS SAP returned by the call manager or MCM as an input (formatted as a [**CO\_SAP**](https://msdn.microsoft.com/library/windows/hardware/ff545392) structure) to [**NdisClRegisterSap**](https://msdn.microsoft.com/library/windows/hardware/ff561648), with which the client registers a SAP on which to receive incoming calls.

 

 





