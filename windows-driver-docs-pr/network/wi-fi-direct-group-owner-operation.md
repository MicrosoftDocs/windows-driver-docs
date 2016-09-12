---
title: Wi-Fi Direct Group Owner Operation
description: A Wi-Fi Direct Role port is configured in operation mode DOT11\_OPERATION\_MODE\_WFD\_GROUP\_OWNER before it can function as a Group Owner.
ms.assetid: C58718A7-3C28-4087-9A73-6FC9CAD7575F
---

# Wi-Fi Direct Group Owner Operation


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

A Wi-Fi Direct Role port is configured in operation mode [**DOT11\_OPERATION\_MODE\_WFD\_GROUP\_OWNER**](https://msdn.microsoft.com/library/windows/hardware/ff547678) before it can function as a Group Owner. Once the operation mode is configured, the port should perform similar to **DOT11\_OPERATION\_MODE\_EXTENSIBLE\_AP**. It should follow the guidelines for the Extensible Access Point mode for starting and stopping the AP and for handling client associations and data packets. Except for the OIDs, NDIS\_STATUS\_INDICATION and Data Type exceptions listed in [Wi-Fi Direct Reference Tables](wi-fi-direct-reference-tables.md), it should handle all the OIDs and NDIS\_STATUS\_INDICATIONS and Data Types that a miniport driver is expected to support in Extensible Access Point mode. It should also continue to support the Wi-Fi Direct OIDs listed in Wi-Fi Direct Reference Tables.

**See Also:**

[OID\_DOT11\_WFD\_DESIRED\_GROUP\_ID](https://msdn.microsoft.com/library/windows/hardware/hh451791)

[OID\_DOT11\_WFD\_START\_GO\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh451809)

[OID\_DOT11\_WFD\_GROUP\_START\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451800)

[**DOT11\_INCOMING\_ASSOC\_DECISION\_V2**](https://msdn.microsoft.com/library/windows/hardware/hh406480)

[NDIS\_STATUS\_DOT11\_WFD\_GROUP\_OPERATING\_CHANNEL](https://msdn.microsoft.com/library/windows/hardware/hh464153)

 

 





