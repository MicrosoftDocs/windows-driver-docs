---
title: Enabling and Disabling Connection Offload Services
description: Enabling and Disabling Connection Offload Services
ms.assetid: 3d353f87-1cd7-483a-b8eb-d45ec3b8f94e
keywords:
- connection offload WDK TCP/IP transport , enabling services
- connection offload WDK TCP/IP transport , disabling services
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling and Disabling Connection Offload Services





Protocol drivers enable connection offload services with an object identifier (OID) request.

**Note**  Enabling or disabling task offload services is different than enabling or disabling connection offload services. Miniport drivers activate all of the available task offload services after a protocol driver specifies an encapsulation type.

 

The TCP/IP transport enables or disables the connection offload capabilities of a network interface card (NIC) by setting the [OID\_TCP\_CONNECTION\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569804) OID. In this set operation, the TCP/IP transport passes the NDIS\_TCP\_CONNECTION\_OFFLOAD\_PARAMETERS structure in the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure. (For information on NDIS\_TCP\_CONNECTION\_OFFLOAD\_PARAMETERS, see [NDIS 6.0 TCP chimney offload documentation](full-tcp-offload.md).)

For more information about configuring connection offload services, see Initializing an Offload Target in the [NDIS 6.0 TCP chimney offload documentation](full-tcp-offload.md).

 

 





