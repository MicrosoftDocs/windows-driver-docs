---
title: Metadata field L2 identifiers
description: This section describes metadata field L2 identifiers for Windows Filtering Platform callout drivers.
ms.assetid: 4A03C593-3760-48F0-A082-A9D1AD90EAD6
keywords:
- Metadata field L2 identifiers network drivers
ms.date: 11/09/2017
ms.localizationpriority: medium
---

# Metadata field L2 identifiers

Windows 8 and Windows Server 2012 introduce metadata field L2 identifiers.

The metadata field L2 identifiers are each represented by a bit field. These identifiers are defined as follows:

| Metadata field identifier | Description |
| --- | --- |
| FWPS_L2_METADATA_FIELD_ETHERNET_MAC_HEADER_SIZE | The size, in bytes, of the MAC header. |
| FWPS_L2_METADATA_FIELD_VSWITCH_DESTINATION_PORT_ID | The identifier for the destination port on the virtual switch. |
| FWPS_L2_METADATA_FIELD_VSWITCH_PACKET_CONTEXT | A **HANDLE** to the virtual switch packet context. |
| FWPS_L2_METADATA_FIELD_VSWITCH_SOURCE_NIC_INDEX | The index for the source NIC on the virtual switch. |
| FWPS_L2_METADATA_FIELD_VSWITCH_SOURCE_PORT_ID | The identifier for the source port on the virtual switch. |
| FWPS_L2_METADATA_FIELD_WIFI_OPERATION_MODE | The current Native 802.11 operation mode. |

## Related topics

[Metadata field identifiers](metadata-field-identifiers.md)

[Metadata fields at each filtering layer](metadata-fields-at-each-filtering-layer.md)

[FWPS_INCOMING_METADATA_VALUES0](https://msdn.microsoft.com/library/windows/hardware/ff552397)

