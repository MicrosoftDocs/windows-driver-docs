---
title: Handling NDIS Ports Status Indications
description: Handling NDIS Ports Status Indications
ms.assetid: ba3794de-b17e-4878-a65e-6c9f5f8ebbbc
keywords:
- ports WDK NDIS , status indications
- NDIS ports WDK , status indications
- status indications WDK networking , NDIS ports
- port states WDK NDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling NDIS Ports Status Indications





If an NDIS port is the source of a status indication, a miniport driver should use the **PortNumber** member in the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure to specify the source port. Miniport drivers never indicate status for inactive ports.

Miniport drivers should use the [**NDIS\_STATUS\_PORT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567415) status indication to indicate changes in the state of an NDIS port. For this status indication, miniport drivers must set the port number in the **PortNumber** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure. The **StatusBuffer** member of the NDIS\_STATUS\_INDICATION structure contains a pointer to an [**NDIS\_PORT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff566800) structure.

 

 





