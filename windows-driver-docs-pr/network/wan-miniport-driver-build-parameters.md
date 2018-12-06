---
title: WAN Miniport Driver Build Parameters
description: WAN Miniport Driver Build Parameters
ms.assetid: 8e494bd2-c499-48bf-8574-7e8df05be4c8
keywords:
- WAN miniport drivers WDK networking , building
- CoNDIS WAN drivers WDK networking , building
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WAN Miniport Driver Build Parameters





This topics provides some information about defining build parameters for NDIS and CoNDIS WAN miniport drivers.

Add the following line to your Sources file before building to identify your driver as a miniport driver.

```Text
C_DEFINES=/DNDIS_MINIPORT_DRIVER
```

If you are writing an NDIS WAN miniport driver that supports connections through TAPI, you must add the following line to your Sources file before building to identify the TAPI version that your driver supports.

```Text
C_DEFINES=-DNDIS_TAPI_CURRENT_VERSION=0x00010003
```

If you are writing a CoNDIS WAN miniport driver that is an integrated miniport call manager (MCM) and that supports the CoNDIS address family type CO\_ADDRESS\_FAMILY\_TAPI\_PROXY, you must add the following line to your sources file before building to identify the TAPI version that your driver supports.

```Text
C_DEFINES=-DNDIS_TAPI_CURRENT_VERSION=0x00030000
```

For WAN miniport drivers, the include paths should include Ndiswan.h as well as Ndis.h.

If the WAN miniport driver supports connections through TAPI, the driver should also include Ndistapi.h.

 

 





