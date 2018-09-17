---
title: Protocol Driver Synchronous OID Requests
description: This topic describes miniport adapter Synchronous OID requests
ms.assetid: 34B88444-DDF1-4AEA-8277-3EA87CA7004A
keywords: Protocol driver Synchronous OID Requests Interface, Protocol driverSynchronous OID call, Protocol driverWDK Synchronous OIDs, Protocol driverSynchronous OID request
ms.author: windowsdriverdev
ms.date: 09/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Protocol Driver Synchronous OID Requests

To support the Synchronous OID request path, protocol drivers call the [**NdisSynchronousOidRequest**](https://msdn.microsoft.com/library/windows/hardware/BF539DDA-59ED-4010-88BC-3C7D8DC475EF) function to issue a Synchronous OID.

For protocol drivers, the *Synchronous OID request interface* differs from the Regular and Direct OID request interfaces in that protocol drivers do not have to implement an asynchronous *complete* callback function. This is because of the synchronous nature of the path. For more info about the differences between Regular, Direct, and Synchronous OIDs in general, see [Synchronous OID Request Interface in NDIS 6.80](synchronous-oid-request-interface-in-ndis-6-80.md).

> [!NOTE]
> NDIS 6.80 supports specific OIDs for use with the Synchronous OID request interface. OIDs that existed before NDIS 6.80 and some NDIS 6.80 OIDs are not supported. To determine if an OID can be used in the Synchronous OID request interface, see the OID reference page.

To support the Synchronous OID request interface, use the documentation for the standard OID request interface. The following table shows the relationship between the functions in the Synchronous OID request interface and the standard OID request interface.

| Synchronous OID function | Standard OID function |
| --- | --- |
| [*NdisSynchronousOidRequest*](https://msdn.microsoft.com/library/windows/hardware/BF539DDA-59ED-4010-88BC-3C7D8DC475EF) | [*NdisOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff563710) |

