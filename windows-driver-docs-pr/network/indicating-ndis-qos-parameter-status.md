---
title: Indicating NDIS QoS Parameter Status
description: Indicating NDIS QoS Parameter Status
ms.assetid: 7E896BC3-839F-4119-BF79-A7BB4CA61CDA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Indicating NDIS QoS Parameter Status


A miniport driver that supports NDIS Quality of Service (QoS) for the IEEE 802.1 Data Center Bridging (DCB) interface must issue NDIS status indications whenever one of the following events occurs:

-   The driver's operational NDIS QoS parameters are either resolved for the first time or change later.

    For more information about how to issue this type of NDIS status indication, see [Indicating Changes to the Operational NDIS QoS Parameters](indicating-changes-to-the-operational-ndis-qos-parameters.md).

-   The driver's remote NDIS QoS parameters are either received from a data-link peer for the first time or change later.

    For more information about how to issue this type of NDIS status indication, see [Indicating Changes to the Remote NDIS QoS Parameters](indicating-changes-to-the-remote-ndis-qos-parameters.md).

For more information about operational and remote NDIS QoS parameters, see [Overview of NDIS QoS Parameters](overview-of-ndis-qos-parameters.md).

 

 





