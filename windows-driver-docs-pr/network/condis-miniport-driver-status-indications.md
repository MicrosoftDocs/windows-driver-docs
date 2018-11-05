---
title: CoNDIS Miniport Driver Status Indications
description: CoNDIS Miniport Driver Status Indications
ms.assetid: 1f1174ba-8b0a-4d43-96c9-2d92f50a22c4
keywords:
- miniport drivers WDK networking , CoNDIS
- NDIS miniport drivers WDK , CoNDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CoNDIS Miniport Driver Status Indications





Miniport drivers call the [**NdisMCoIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563562) function to report a change in the status of a miniport adapter. The miniport driver passes **NdisMCoIndicateStatusEx** a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure that contains the status information.

The status indication includes information to identify the type of status and a reason for the status change.

The miniport driver should set the **SourceHandle** member of the NDIS\_STATUS\_INDICATION structure to the handle that NDIS passed to the *MiniportAdapterHandle* parameter of the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function. If the status indication is associated with an OID request, the miniport driver can set the **DestinationHandle** and **RequestId** members of NDIS\_STATUS\_INDICATION so that NDIS can provide the status indication to a specific protocol binding. For more information about OID requests, see [CoNDIS Miniport Driver OID Requests](condis-miniport-driver-oid-requests.md).

 

 





