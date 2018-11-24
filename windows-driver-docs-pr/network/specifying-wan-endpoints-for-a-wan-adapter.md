---
title: Specifying WAN Endpoints for a WAN Adapter
description: Specifying WAN Endpoints for a WAN Adapter
ms.assetid: e6dd12c3-03e3-4f7d-8ad7-2511bf46c4f8
keywords:
- add-registry-sections WDK networking , WAN adapter endpoints
- WAN adapter endpoints WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying WAN Endpoints for a WAN Adapter





A INF file for a WAN adapter must add a **WanEndpoints** value to the instance key for the adapter. **WanEndpoints** is a REG\_DWORD value that specifies the number of endpoints (also known as channels, circuits or bearer channels) that are supported by the WAN adapter. For example, the **WanEndpoints** value for a *basic rate interface* (BRI) ISDN adapter is 2, whereas the **WanEndpoints** value for a *primary rate interface* (PRI) ISDN adapter is typically 23.

**Note**   ISDN drivers are deprecated in Windows 8.1, Windows Server 2012 R2, and later.

 

The following is an example of an *add-registry-section* that adds a **WanEndpoints** value of 2 for a BRI ISDN adapter:

```INF
[a1.reg]
HKR,, WanEndpoints, 0x00010001, 2
```

 

 





