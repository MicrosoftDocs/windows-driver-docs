---
title: Metadata field L2 identifiers
author: windows-driver-content
description: This section describes metadata field L2 identifiers for Windows Filtering Platform callout drivers.
ms.assetid: 4A03C593-3760-48F0-A082-A9D1AD90EAD6
keywords:
- Metadata field L2 identifiers network drivers
ms.author: windowsdriverdev
ms.date: 11/09/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")