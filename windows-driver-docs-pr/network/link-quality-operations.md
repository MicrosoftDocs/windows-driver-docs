---
title: Link Quality Operations
description: Link Quality Operations
ms.assetid: a649114f-39d9-4cb1-9190-985dc7967268
keywords:
- network operations WDK Native 802.11 , link quality operations
- link quality operations WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Link Quality Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Link quality is a metric that defines the throughput quality over the data link between the 802.11 station and an access point (AP) or peer station. The 802.11 station measures the link quality as a value ranging from zero through 100, with 100 indicating the highest link quality.

This range of values is divided into 5 groups: \[0-19\], \[20-39\], \[40-59\], \[60-79\], and \[80-100\].

The link quality measurement is specific to the implementation by the independent hardware vendor (IHV). It is recommended that the 802.11 station represent the link quality value as the percentage of the highest possible throughput over the data link to the AP or peer station.

When measuring the link quality to an associated AP or peer station, the 802.11 station must use the following guidelines:

-   The 802.11 station measures link quality during periodic sampling periods. The length and intervals of the sampling periods are specific to the IHV implementation.

-   During the sampling period, the 802.11 station must measure the link quality to the associated AP or one peer station. If the 802.11 station is connected to an independent basic service set (IBSS) network, the station must determine the link quality for each associated peer station during different sampling periods.

    **Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).

     

-   The link quality must have a value of 100 when the 802.11 station can communicate with the AP or peer station during the sampling period at the highest possible throughput. A link quality of 100 is defined when all of the following occur during the sampling period:
    1.  A unicast data packet is transmitted or received at the highest PHY data rate.
    2.  Packets are sent without any retransmission.
    3.  Packets are received without frame check sequence (FCS) errors.
    4.  The 802.11 station does not perform any transmit deferrals due to a busy media.
-   The link quality must have a value of zero if the 802.11 station cannot transmit to or receive from the associated AP or peer station during the sampling period.

The miniport driver reports link quality through any of the following:

<a href="" id="--------ndis-status-dot11-link-qualitystatus-indications"></a>[NDIS\_STATUS\_DOT11\_LINK\_QUALITY](https://msdn.microsoft.com/library/windows/hardware/ff567344) **Status Indications**  
The miniport driver makes the Native 802.11 NDIS\_STATUS\_DOT11\_LINK\_QUALITY indication whenever the 802.11 station determines the link quality to an associated AP or peer station has changed significantly since the last NDIS\_STATUS\_DOT11\_LINK\_QUALITY indication.

The determination for when to make this indication is specific to the IHV implementation. However, the miniport driver should implement some threshold mechanism to avoid making frequent indications.

The miniport driver should make an [NDIS\_STATUS\_DOT11\_LINK\_QUALITY](https://msdn.microsoft.com/library/windows/hardware/ff567344) indication whenever the link quality changes from one group to another. For example, the driver should make this indication if the link quality changes from a value of 39 to 45. Once again, the miniport driver must avoid making frequent indications and must implement a damping algorithm to avoid thrashing when the link quality quickly changes groups.

If the 802.11 station is connected to an IBSS network, the miniport driver must make NDIS\_STATUS\_DOT11\_LINK\_QUALITY indications so that the operating system can determine the overall quality of the IBSS network. The algorithm for calculating the link quality for each associate peer station is specific to the implementation of the IHV.

**Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).

 

For more information about Native 802.11 indications, see [Native 802.11 Status Indications](native-802-11-status-indications.md).

<a href="" id="oid-dot11-enum-bss-listquery-requests"></a>[OID\_DOT11\_ENUM\_BSS\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569360) **Query Requests**  
The miniport driver returns the link quality of each AP or peer station detected during the last scan operation when the OID\_DOT11\_ENUM\_BSS\_LIST object identifier (OID) is queried. The driver returns the link quality through the **uLinkQuality** member of each [**DOT11\_BSS\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff547665) structure that represents an AP or peer station detected by the 802.11 station.

For the currently associated AP or peer stations detected during the scan operation, the miniport driver must determine the link quality value using the same criteria that was used to make an [NDIS\_STATUS\_DOT11\_LINK\_QUALITY](https://msdn.microsoft.com/library/windows/hardware/ff567344) indication.

For each AP or peer station that the 802.11 station is not associated with, the determination of the link quality value is specific to the implementation of the IHV.

For more information about scan operations, see [Native 802.11 Scan Operations](native-802-11-scan-operations.md).

 

 





