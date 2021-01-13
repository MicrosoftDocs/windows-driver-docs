---
title: Standard Miniport Driver Status Indications Registered with WMI
description: Standard Miniport Driver Status Indications Registered with WMI
keywords:
- status indications WDK networking , WMI
- WMI WDK networking , status indications
- Windows Management Instrumentation WDK networking , status indications
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standard Miniport Driver Status Indications Registered with WMI





NDIS automatically registers GUIDs with WMI for the NDIS status indications that miniport drivers indicate with the [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex) or [**NdisMCoIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcoindicatestatusex) function. For a list of general status indications, see [Status Indications](/windows-hardware/drivers/ddi/_netvista/).

If a WMI client registers with WMI to receive an NDIS WMI event, NDIS translates the corresponding NDIS status indication to the WMI event and reports the event to all of the WMI clients that registered for the event.

NDIS drivers can also generate custom status indications. For more information about custom status indications and WMI, see [Customized OIDs and Status Indications](customized-oids-and-status-indications.md).

 

