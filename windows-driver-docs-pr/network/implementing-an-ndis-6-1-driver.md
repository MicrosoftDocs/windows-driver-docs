---
title: Implementing an NDIS 6.1 Driver
description: Implementing an NDIS 6.1 Driver
ms.assetid: a2b5d722-88b3-4321-9d0d-451f465194d1
keywords:
- NDIS WDK , versions in network drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementing an NDIS 6.1 Driver





An NDIS 6.1 driver must report the correct NDIS version when it registers with NDIS.

You must update the major and minor NDIS version number in the NDIS\_*Xxx*\_DRIVER\_CHARACTERISTICS structure to support NDIS 6.1. The **MajorNdisVersion** member must contain 0x06 and the **MinorNdisVersion** member must contain 0x01. This requirement applies to miniport, protocol, and filter drivers.

 

 





