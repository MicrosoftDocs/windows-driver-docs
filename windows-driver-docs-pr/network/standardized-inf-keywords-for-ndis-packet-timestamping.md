---
title: Standardized INF keywords for NDIS packet timestamping
description: Standardized INF keywords for NDIS packet timestamping
ms.date: 01/31/2021
ms.localizationpriority: medium
---

# Standardized INF keywords for NDIS packet timestamping

An INF file can define the following standardized INF keywords to enable or disable the timestamping capabilities that the miniport driver and NIC hardware supports.

Miniport drivers can use these keywords to determine the current configuration of the timestamping capabilities. For example, the driver can read these keyword values during initialization to determine which timestamping capabilities are enabled and the driver can therefore use.

[**\*PtpHardwareTimestamp** INF keyword](#ptphardwaretimestamp-inf-keyword)

[**\*SoftwareTimestamp** INF keyword](#softwaretimestamp-inf-keyword)


For more information about standardized INF keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

## \*PtpHardwareTimestamp INF keyword

The **\*PtpHardwareTimestamp** keyword is defined to enable or disable support for hardware timestamping for Precision Time Protocol (PTP) version 2 packets using UDP as the transport.

The default setting for the **\*PtpHardwareTimestamp** keyword is disabled and the miniport driver should disable all types of hardware timestamping support in the NIC hardware by default.

Miniport drivers read the **\*PtpHardwareTimestamp** keyword value to determine if hardware timestamping is currently enabled or disabled. 

If **\*PtpHardwareTimestamp** is enabled, the miniport driver should:

1. Enable the relevant hardware timestamping capabilities in the NIC hardware. 

1. Generate the [**NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG**](ndis-status-timestamp-current-config.md) status indication to report the timestamping capabilities it enabled to NDIS. The driver uses the [**NDIS_TIMESTAMP_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capabilities) structure to specify which capabilities it enabled.
The flags within the **TimestampFlags** field in the **NDIS_TIMESTAMP_CAPABILITIES** structure that correspond to hardware timestamping are `PtpV2OverUdpIPv4EventMsgReceiveHw`, `PtpV2OverUdpIPv4AllMsgReceiveHw`, `PtpV2OverUdpIPv4EventMsgTransmitHw`, `PtpV2OverUdpIPv4AllMsgTransmitHw`, `PtpV2OverUdpIPv6EventMsgReceiveHw`, `PtpV2OverUdpIPv6AllMsgReceiveHw`, `PtpV2OverUdpIPv6EventMsgTransmitHw`, `PtpV2OverUdpIPv6AllMsgTransmitHw`, `AllReceiveHw`, `AllTransmitHw` and `TaggedTransmitHw`. The **CrossTimestamp** field in the **NDIS_TIMESTAMP_CAPABILITIES** structure for the **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indicates if hardware cross timestamping is enabled.

When **\*PtpHardwareTimestamp** is enabled the miniport should turn on some form of capability to generate hardware timestamps for both Rx and Tx for PTP version 2 over UDP. The miniport should also turn on the hardware cross timestamping capability if the hardware supports it.

The specific hardware timestamping capabilities that the miniport driver should enable in hardware depends on the capabilities of the NIC hardware. For example, if the NIC hardware only supports the `PtpV2OverUDPIPv4EventMsgReceiveHw`, `PtpV2OverUDPIPv6EventMsgReceiveHw` and `TaggedTransmitHw` capabilities, then the miniport can turn on these hardware timestamping capabilities if the **\*PtpHardwareTimestamp** keyword is enabled.

If the NIC hardware supports multiple forms of hardware timestamping capabilities that can enable the PTP version 2 over UDP scenario, then the IHV should consider their hardware and issues such as performance impact to decide which capabilities the miniport should turn on. For example, the hardware may be capable of generating timestamps for `AllTransmitHw` and `TaggedTransmitHw`. If turning on `AllTransmitHw` is more expensive than turning on `TaggedTransmitHw`, then the IHV may choose to only turn on the `TaggedTransmitHw` capability for Tx.

In all cases, the miniport driver should accurately report which hardware timestamping capabilities it enabled or disabled using the **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indication.

> [!NOTE]
> PTP over raw Ethernet is not supported. The IHV needs to determine what the most efficient way of handling PTP over raw Ethernet packets when supporting PTP over UDP is enabled.

> [!NOTE]
> No support is needed for PTP version 1. If the NIC hardware also supports PTP version 1, then the IHV needs to determine the most efficient way of handling PTP version 1 packets when supporting PTP version 2.

### INF entries for *PtpHardwareTimestamp

The **\*PtpHardwareTimestamp** INF keyword is an enumeration keyword. Enumeration standardized INF keywords have the following attributes:

SubkeyName: The name of the keyword that you must specify in the INF file.

ParamDesc: The display text that is associated with SubkeyName. 

Value: The enumeration integer value that is associated with each SubkeyName in the list. 

EnumDesc: The display text that is associated with each value that appears in the menu.

Default: The default value for the menu.

The following table describes the possible INF entries for the **\*PtpHardwareTimestamp** INF keyword.

|SubkeyName|ParamDesc|Value|EnumDesc|
|--- |--- |--- |--- |
|***PtpHardwareTimestamp**|PTP Hardware Timestamp|0 (Default)|Disabled|
|||1|Enabled|

> [!NOTE]
> If the miniport driver finds an unsupported value for the **\*PtpHardwareTimestamp** keyword, then it should disable the hardware timestamping capability completely.

## \*SoftwareTimestamp INF keyword

The **\*SoftwareTimestamp** keyword corresponds to the types of software timestamping the miniport driver is capable of. The miniport driver uses the configured value for this keyword to determine which of the supported software timestamping capabilities are currently enabled.

The default setting for the **\*SoftwareTimestamp** keyword is disabled and all types of software timestamping support in the miniport should be disabled by default.

The miniport generates the [**NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG**](ndis-status-timestamp-current-config.md) status indication to inform NDIS of the various timestamping capabilities that are currently enabled.

The flags within the **TimestampFlags** field in the [**NDIS_TIMESTAMP_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capabilities) structure that correspond to software timestamping are `AllReceiveSw`, `AllTransmitSw` and `TaggedTransmitSw`.

If the **\*SoftwareTimestamp** keyword contains a value that indicates that some configuration of software timestamping is enabled, then the miniport should enable the configured software timestamping capabilities and generate a **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indication that accurately reports which software timestamping capabilities have been enabled.

If the miniport does not support any type of software timestamping then the **\*SoftwareTimestamp** keyword should not be included in its INF file.

The **\*SoftwareTimestamp** INF keyword is an enumeration keyword. Enumeration standardized INF keywords have the following attributes:

SubkeyName: The name of the keyword that you must specify in the INF file.

ParamDesc: The display text that is associated with SubkeyName. 

Value: The enumeration integer value that is associated with each SubkeyName in the list. 

EnumDesc: The display text that is associated with each value that appears in the menu.

Default: The default value for the menu.

The following table describes the possible INF entries for the **\*SoftwareTimestamp** INF keyword.

|SubkeyName|ParamDesc|Value|EnumDesc|
|--- |--- |--- |--- |
|***SoftwareTimestamp**|Software Timestamp|0 (Default)|Disabled|
|||1|**RxAll**: This enum value corresponds to the miniport driver capability to generate software timestamps for all packets during Rx.|
|||2|**TxAll**: This enum value corresponds to the miniport driver capability to generate software timestamps for all packets during Tx.|
|||3|**RxAll & TxAll**: This enum value corresponds to the miniport driver capability to generate software timestamps for all packets during Rx and Tx.|
|||4|**TaggedTx**: This enum value corresponds to the miniport driver capability to generate software timestamps for a specific Tx packet when indicated to do so by the operating system.|
|||5|**RxAll & TaggedTx**: This enum value corresponds to the miniport driver capability to generate software timestamps for all packets during Rx and for a specific Tx packet when indicated to do so by the operating system.|

> [!NOTE]
> If the miniport driver finds an unsupported value for the **\*SoftwareTimestamp** keyword, then it should disable the software timestamping capability completely.
