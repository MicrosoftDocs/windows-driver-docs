---
title: Enabling and Disabling Task Offload Services
description: A protocol driver can enable or disable task offload services for an underlying miniport adapter by issuing an OID_OFFLOAD_ENCAPSULATION OID set request.
ms.assetid: cc803af4-d4ed-4b51-9e0e-77443e0eb023
keywords:
- task offload WDK TCP/IP transport , enabling services
- task offload WDK TCP/IP transport , disabling services
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling and Disabling Task Offload Services


A protocol driver can enable or disable task offload services for an underlying miniport adapter by issuing an [OID\_OFFLOAD\_ENCAPSULATION](https://msdn.microsoft.com/library/windows/hardware/ff569762) OID set request. This OID request sets the required encapsulation type and tells the miniport driver to activate all of the available task offload services.




Before issuing the [OID\_OFFLOAD\_ENCAPSULATION](https://msdn.microsoft.com/library/windows/hardware/ff569762) OID set request, the protocol driver should make sure that the underlying miniport adapter supports the required encapsulation type. There are two ways to do this:

-   Check the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure that the protocol driver received in its [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function.
-   Issue an [OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569805) query request.

If the miniport driver supports any task offload type that supports the requested encapsulation type, the miniport driver must return NDIS\_STATUS\_SUCCESS in response to the [OID\_OFFLOAD\_ENCAPSULATION](https://msdn.microsoft.com/library/windows/hardware/ff569762) set request. Otherwise, the miniport driver should return NDIS\_STATUS\_INVALID\_PARAMETER.

 

 





