---
title: Determining the current task offload settings
description: This section describes how to determine the current task offload settings for protocol drivers
ms.assetid: cd2f9b9f-f455-405d-8775-9a437e628476
keywords:
- task offload WDK TCP/IP transport , current settings
- current task load settings WDK TCP/IP offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining the Current Task Offload Settings


A protocol driver can determine the current task offload encapsulation settings of an underlying miniport adapter by issuing an [OID\_OFFLOAD\_ENCAPSULATION](https://msdn.microsoft.com/library/windows/hardware/ff569762) OID query request.




For more information about issuing an OID request, see [Generating OID Requests from an NDIS Protocol Driver](generating-oid-requests-from-an-ndis-protocol-driver.md).

 

 





