---
title: Handling the Port Deactivation PnP Event
description: Handling the Port Deactivation PnP Event
ms.assetid: 0e3b10a7-5ab5-48e1-a5cc-c7bc6ce26410
keywords:
- ports WDK NDIS , PnP event notifications
- NDIS ports WDK , PnP event notifications
- PnP event notifications WDK NDIS ports
- deactivation PnP events WDK NDIS ports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling the Port Deactivation PnP Event





Overlying drivers must handle the **NetEventPortDeactivation** PnP event when a miniport driver deactivates an NDIS port. To notify overlying drivers about port deactivation events, NDIS propagates the port deactivation PnP event from the underlying miniport driver.

Before a protocol driver completes the handling of a port deactivation PnP event, it must ensure that all outstanding OID requests and send requests that are associated with the port have completed. After the protocol driver completes the PnP event, the driver must ensure that it does not issue any OID requests or send requests for that port.

Miniport drivers specify the **NetEventPortDeactivation** PnP event code in the [**NET\_PNP\_EVENT\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff568752) structure that the *NetPnPEvent* parameter points to in the call to the [**NdisMNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff563616) function to report that some ports have been deactivated. The miniport driver specifies an array of NDIS\_PORT\_NUMBER values to list the deactivated ports. For more information about the array of port numbers, see [Deactivating NDIS Ports](deactivating-an-ndis-port.md).

 

 





