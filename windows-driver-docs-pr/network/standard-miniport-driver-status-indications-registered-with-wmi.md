---
title: Standard Miniport Driver Status Indications Registered with WMI
description: Standard Miniport Driver Status Indications Registered with WMI
ms.assetid: afebd0a2-c811-4534-9320-02b9292ba81b
keywords:
- status indications WDK networking , WMI
- WMI WDK networking , status indications
- Windows Management Instrumentation WDK networking , status indications
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standard Miniport Driver Status Indications Registered with WMI





NDIS automatically registers GUIDs with WMI for the NDIS status indications that miniport drivers indicate with the [**NdisMIndicateStatusEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismindicatestatusex) or [**NdisMCoIndicateStatusEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismcoindicatestatusex) function. For a list of general status indications, see [Status Indications](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_netvista/).

If a WMI client registers with WMI to receive an NDIS WMI event, NDIS translates the corresponding NDIS status indication to the WMI event and reports the event to all of the WMI clients that registered for the event.

NDIS drivers can also generate custom status indications. For more information about custom status indications and WMI, see [Customized OIDs and Status Indications](customized-oids-and-status-indications.md).

 

 





