---
title: Capturing Extensions
description: Capturing Extensions
ms.assetid: A8C2E550-4B1F-4DDB-B97F-1F7B6B74F5E7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Capturing Extensions


A Hyper-V extensible switch capturing extension inspects packet traffic, object identifier (OID) requests, and NDIS status indications. This type of extension cannot modify or drop packets, or exclude packets from being delivered to extensible switch ports. However, capturing extensions can originate packet traffic, such as packets that contain traffic statistics that the extension sends to a host application.

Capturing extensions are invoked at the start of the ingress data path and at the end of the egress data path. For more information about these data paths, see [Hyper-V Extensible Switch Data Path](hyper-v-extensible-switch-data-path.md).

A capturing extension has the following requirements and restrictions:

-   A capturing extension must be developed as an NDIS filter driver that supports the extensible switch interface.

    For more information about filter drivers, see [NDIS Filter Drivers](ndis-filter-drivers2.md).

    For more information on how to write a capturing extension, see [Writing Hyper-V Extensible Switch Extensions](writing-hyper-v-extensible-switch-extensions.md).

-   A capturing extension provides the same functionality as a standard NDIS monitoring filter driver. However, the INF file for a capturing extension must install it as a modifying filter driver.

    For more information about modifying filter drivers, see [Types of Filter Drivers](types-of-filter-drivers.md).

    For more information about the INF requirements for modifying filter drivers, see [Configuring an INF File for a Modifying Filter Driver](configuring-an-inf-file-for-a-modifying-filter-driver.md).

-   A capturing extension can monitor packets over the ingress and egress extensible switch data path. However, this type of extension must always call [**NdisFSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562616) to forward the packets to underlying drivers in the extensible switch driver stack and not complete them.

-   A capturing extension must not modify the data within the packets nor add port destinations to the out-of-band (OOB) data of the packet. The extension must not exempt the delivery of the packet to any extensible switch port.

-   A capturing extension can originate packets. For example, the extension may originate packets in order to report traffic conditions to a remote monitoring application.

    For more information on originating packets by an extension, see [Originating Packet Traffic](originating-packet-traffic.md).

    **Note**  As with other extensions, the capturing extension can only originate packet traffic in the extensible switch ingress data path.

     

-   A capturing extension can monitor packets, OID requests, and NDIS status indications that are issued over the extensible switch driver stack. However, this type of extension must forward packets, OID requests, and NDIS status indications through the extensible switch driver stack. The extension must not modify the data within the packets, OID requests, or NDIS status indications that it monitors.

-   The **FilterClass** value in the INF file for the extension must be set to **ms\_switch\_capture**. For more information, see [INF Requirements for Hyper-V Extensible Switch Extensions](inf-requirements-for-hyper-v-extensions.md).

-   Any number of capturing extensions can be bound to an extensible switch instance. By default, multiple capturing extensions are ordered based on when they were installed. For example, multiple capturing extensions are layered in the extensible switch driver stack with the most recently installed extension layered above other capturing extensions in the stack.

    Once bound to an extensible switch instance, the layering of capturing extensions in the extensible switch driver stack can be reordered. For more information, see [Reordering Hyper-V Extensible Switch Extensions](reordering-hyper-v-extensibility-switch-extensions.md).

 

 





