---
title: Querying a Miniport Driver Directly From User Mode
description: Querying a Miniport Driver Directly From User Mode
keywords:
- user-mode driver queries WDK networking
ms.date: 04/20/2017
---

# Querying a Miniport Driver Directly From User Mode





An application can use [**IOCTL\_NDIS\_QUERY\_GLOBAL\_STATS**](/previous-versions/windows/hardware/network/ff548975(v=vs.85)) to directly query information from a miniport driver's NIC. In this operation, the application can use any query OID that the miniport driver supports.

 

