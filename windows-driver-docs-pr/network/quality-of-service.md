---
title: Quality of Service
description: Quality of Service
ms.assetid: e7a4413c-633b-4634-a647-c84b8c97cbea
keywords:
- connection-oriented NDIS WDK , quality of service
- CoNDIS WDK networking , quality of service
- quality of service WDK CoNDIS
- QoS WDK CoNDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Quality of Service





The originator of a call on an SVC can specify *quality of service* (QoS) parameters for the call that specify performance parameters for the call. Depending on the signaling protocol that is being used, a call manager or MCM driver that is setting up an outgoing or incoming call can negotiate the QoS with a network entity such as a network switch or a remote client. If allowed by the signaling protocol, a connection-oriented client might also request a change of QoS when determining whether to accept an incoming call.

The QoS parameters for a call are specified as call parameters in a [**CO\_CALL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff545384) structure. CO\_CALL\_PARAMETERS points to two other structures:

-   [**CO\_CALL\_MANAGER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff545381), which specifies call manager parameters that a call manager or MCM driver use to set up a call.

-   [**CO\_MEDIA\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff545388), which specifies media parameters that a miniport driver or MCM driver use to activate a VC.

Both CO\_CALL\_MANAGER\_PARAMETERS and CO\_MEDIA\_PARAMETERS contain generic parameters (flags) that apply to all drivers that use the parameters. Each of these structures also points to a [**CO\_SPECIFIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff545396) structure that specifies call manager-specific parameters (when pointed to by a CO\_CALL\_MANAGER\_PARAMETERS structure) or media-specific parameters (when pointed to by a CO\_MEDIA\_PARAMETERS structure).

For more information about QoS operations, see [Client-Initiated Request to Change Call Parameters](client-initiated-request-to-change-call-parameters.md) and [Incoming Request to Change Call Parameters](incoming-request-to-change-call-parameters.md).

 

 





