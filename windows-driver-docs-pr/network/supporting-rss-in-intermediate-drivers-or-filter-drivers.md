---
title: Supporting RSS in Intermediate Drivers or Filter Drivers
description: Supporting RSS in Intermediate Drivers or Filter Drivers
ms.assetid: 5e1bfbb0-0b7a-4a9d-a228-4089f7208880
keywords:
- receive-side scaling WDK networking , intermediate drivers
- RSS WDK networking , intermediate drivers
- receive-side scaling WDK networking , filter drivers
- RSS WDK networking , filter drivers
- filter drivers WDK RSS
- intermediate drivers WDK RSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting RSS in Intermediate Drivers or Filter Drivers





All intermediate drivers and filter drivers should, at a minimum, pass on OID requests, other requests, and status indications. Intermediate drivers or filter drivers should provide additional driver-specific support for receive side scaling (RSS) if the driver does any of the following:

-   Originates send requests.

-   Originates receive indications.

-   Queues send requests or receive indications for later processing.

Filter drivers that bypass send and receive processing do not have to do anything additional to support RSS. For more information about bypassing send or receive requests in a filter driver, see [Data Bypass Mode](data-bypass-mode.md).

A QoS scheduler is an example of a filter driver that should support RSS. Such a driver queues send packets for sending at an appropriate time. The filter driver should use the same CPU that the protocol driver uses for a given connection.

An intermediate driver or filter driver that does not support RSS can intercept the RSS OID requests and disable RSS by reporting that RSS is not supported.

A filter driver or intermediate driver that supports RSS can use the information from the RSS OIDs to assign connections to the same CPUs the protocol driver and miniport driver are using.

For more information about the RSS OIDs, see [RSS Configuration](rss-configuration.md).

 

 





