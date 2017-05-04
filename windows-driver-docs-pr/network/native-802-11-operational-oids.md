---
title: Native 802.11 Operational OIDs
description: This section describes Native 802.11 Operational OIDs and their characteristics.
keywords: ["Native 802.11 Operational OIDs", "Native 802.11 WLAN Operational OIDs", "WDK Native 802.11 Operational OIDs", "Native 802.11 Operational object identifiers"]
ms.assetid: F2443987-F018-49C3-844A-AEF665513A4E
ms.author: windowsdriverdev
ms.date: 04/25/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 Operational OIDs

>[!IMPORTANT]
> The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

The Native 802.11 Operational object identifiers (OIDs) query and set the configuration and operation of the 802.11 station. These OIDs are applicable to miniport drivers that support any of the Native 802.11 operation modes. For more information about these operation modes, see [Native 802.11 Operation Modes](native-802-11-operation-modes.md).

>[!NOTE]
> For the Windows Vista operating system, only the Extensible Station (ExtSTA) operation mode is supported.
 
In the following table, these abbreviations are used to specify the requirements for Native 802.11 Operational OID query (Q), set (S), and NDIS 6.0 method (M) requests:

- R   
Indicates that support for the object is required. The miniport driver must not fail set or query requests for the object by returning NDIS_STATUS_NOT_SUPPORTED from its [MiniportOidRequest](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.
- O   
Indicates that support for the object is optional. The miniport driver can either support query or set requests for the object, or the driver can fail the request by returning NDIS_STATUS_NOT_SUPPORTED from its [MiniportOidRequest](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.
- X   
Indicates that the specified state of a Native 802.11 operating mode supports a set request for the object. If the miniport driver is not in the specified state, the miniport driver must fail the set request by returning NDIS_STATUS_INVALID_STATE from its [MiniportOidRequest](https://msdn.microsoft.com/library/windows/hardware/ff559416) function. 

For more information about Native 802.11 operation modes, see [Native 802.11 Operation Modes](native-802-11-operation-modes.md). For more information about Native 802.11 operating states, see [Native 802.11 Operating States](native-802-11-operating-states.md).

| Name                                                                                                      | Q | S | M | ExtSTA INIT| ExtSTA OP|
|---                                                                                                        |---|---|---|---         |---       |
| [OID_DOT11_ATIM_WINDOW](https://msdn.microsoft.com/library/windows/hardware/ff569105)                     | O | O |   | X          |          |
| [OID_DOT11_CURRENT_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff569125)                 | O |   |   |            |          |
| [OID_DOT11_CURRENT_OPERATION_MODE](https://msdn.microsoft.com/library/windows/hardware/ff569132)          | R | R |   | X          |          |
| [OID_DOT11_CURRENT_OPTIONAL_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569133)     | O |   |   |            |          |
| [OID_DOT11_DATA_RATE_MAPPING_TABLE](https://msdn.microsoft.com/library/windows/hardware/ff569139)         | O |   |   |            |          |
| [OID_DOT11_MAXIMUM_LIST_SIZE](https://msdn.microsoft.com/library/windows/hardware/ff569382)               | O |   |   |            |          |
| [OID_DOT11_MPDU_MAX_LENGTH](https://msdn.microsoft.com/library/windows/hardware/ff569387)                 | O |   |   |            |          |
| [OID_DOT11_MULTICAST_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569388)                  | R | R |   |            |          |
| [OID_DOT11_NIC_POWER_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569392)                 | R | R |   | X          |          |
| [OID_DOT11_NIC_SPECIFIC_EXTENSION](https://msdn.microsoft.com/library/windows/hardware/ff569393)          |   |   | O | X          | X        |
| [OID_DOT11_OPERATION_MODE_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569396)       | O |   |   |            |          |
| [OID_DOT11_OPTIONAL_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569397)             | O |   |   |            |          |
| [OID_DOT11_PERMANENT_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff569399)               | O |   |   |            |          |
| [OID_DOT11_RECV_SENSITIVITY_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569407)           | O |   |   |            |          |
| [OID_DOT11_RESET_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409)                   |   |   | R | X          | X        |
| [OID_DOT11_RF_USAGE](https://msdn.microsoft.com/library/windows/hardware/ff569410)                        | O |   |   |            |          |
| [OID_DOT11_SCAN_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413)                    |   | R |   | X          | X        |
| [OID_DOT11_SUPPORTED_DATA_RATES_VALUE](https://msdn.microsoft.com/library/windows/hardware/ff569422)      | O |   |   |            |          |
| [OID_DOT11_SUPPORTED_PHY_TYPES](https://msdn.microsoft.com/library/windows/hardware/ff569426)             | O |   |   |            |          |
| [OID_DOT11_SUPPORTED_POWER_LEVELS](https://msdn.microsoft.com/library/windows/hardware/ff569427)          | O |   |   |            |          |
| [OID_DOT11_SUPPORTED_RX_ANTENNA](https://msdn.microsoft.com/library/windows/hardware/ff569428)            | O |   |   |            |          |
| [OID_DOT11_SUPPORTED_TX_ANTENNA](https://msdn.microsoft.com/library/windows/hardware/ff569429)            | O |   |   |            |          |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")