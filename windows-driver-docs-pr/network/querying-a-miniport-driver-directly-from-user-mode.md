---
title: Querying a Miniport Driver Directly From User Mode
description: Querying a Miniport Driver Directly From User Mode
ms.assetid: e0d153bf-0e50-47bc-b4e2-10f04c532b99
keywords: ["user-mode driver queries WDK networking"]
---

# Querying a Miniport Driver Directly From User Mode


## <a href="" id="ddk-querying-a-miniport-driver-directly-from-user-mode-ng"></a>


An application can use [**IOCTL\_NDIS\_QUERY\_GLOBAL\_STATS**](https://msdn.microsoft.com/library/windows/hardware/ff548975) to directly query information from a miniport driver's NIC. In this operation, the application can use any query OID that the miniport driver supports.

 

 





