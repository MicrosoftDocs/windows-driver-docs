---
title: NDIS Management Information and OIDs
description: NDIS Management Information and OIDs
ms.assetid: 5737634e-ee80-44d4-9dc8-c2ef97670809
keywords:
- WMI WDK networking , management information base
- management information base WDK networking
- dynamic configuration information WDK networking
- statistics WDK networking
- management information base WDK networking , objects
- MIBs WDK networking
- object identifiers WDK networking
- OIDs WDK networking , management information base
- operational characteristics WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Management Information and OIDs





Each miniport driver contains its own *management information base (MIB)*, which is an information block in which the driver stores dynamic configuration information and statistical information that a management entity can query or set. An Ethernet multicast address list is an example of configuration information. The number of broadcast packets received is an example of statistical information. Each information element within the MIB is referred to as an *object*. To refer to each such managed object, NDIS defines an *object identifier (OID)*. Therefore, if a management entity wants to query or set a particular managed object, it must provide the specific OID for that object.

The MIB tracks three classes of objects:

-   Objects that are general to all NDIS miniport drivers.

-   Objects that are specific to all NDIS miniport drivers for a given medium type, such as Ethernet.

-   Objects that are specific to a particular vendor implementation.

The *general* and mandatory *media-specific* OIDs are documented in the Network Reference section of the WDK documentation. The implementation-specific OIDs for a particular network interface card (NIC) driver should be listed and described in the documentation that accompanies a given miniport driver.

Objects are classified as *operational characteristics* (for example, multicast address list) or *statistics* (for example, broadcast packets received), and they are also classified as *mandatory* or *optional*. All operational characteristics objects for general or media-specific classes are mandatory, but only some statistics objects are mandatory. All implementation-specific objects are classified as mandatory.

For more information about OID classifications, see [NDIS OIDs](https://msdn.microsoft.com/library/windows/hardware/ff566707).

 

 





