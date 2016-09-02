---
title: Wi-Fi Direct Client Operation
description: A Wi-Fi Direct Role port is configured in operation mode DOT11\_OPERATION\_MODE\_WFD\_CLIENT before it can function as a Client.
ms.assetid: 5DE4D86F-7EE0-4BB0-87AC-36E99CE3D209
---

# Wi-Fi Direct Client Operation


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

A Wi-Fi Direct Role port is configured in operation mode [**DOT11\_OPERATION\_MODE\_WFD\_CLIENT**](https://msdn.microsoft.com/library/windows/hardware/ff547678) before it can function as a Client. Once the operation mode is configured, the port should perform similar to **DOT11\_OPERATION\_MODE\_EXTENSIBLE\_STATION**. It should follow the guidelines for the Extensible Station mode for association, disassociation and roaming and handling of data packets. Except for the OIDs, NDIS\_STATUS\_INDICATION and Data Type exceptions listed in [Wi-Fi Direct Reference Tables](wi-fi-direct-reference-tables.md), it should handle all the OIDs and NDIS\_STATUS\_INDICATIONS and Data Types that a miniport driver is expected to support in Extensible Station mode. It should also continue to support the Wi-Fi Direct OIDs listed in Wi-Fi Direct Reference Tables.OID\_DOT11\_WFD\_GROUP\_JOIN\_PARAMETERS

**See Also:**

[OID\_DOT11\_WFD\_DESIRED\_GROUP\_ID](https://msdn.microsoft.com/library/windows/hardware/hh451791)

[OID\_DOT11\_WFD\_CONNECT\_TO\_GROUP\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh464154)

[OID\_DOT11\_WFD\_DISCONNECT\_FROM\_GROUP\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh451794)

[OID\_DOT11\_WFD\_GROUP\_JOIN\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh464155)

[NDIS\_STATUS\_DOT11\_WFD\_GROUP\_OPERATING\_CHANNEL](https://msdn.microsoft.com/library/windows/hardware/hh464153)

 

 





