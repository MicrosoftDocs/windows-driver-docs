---
title: OID_GEN_RECEIVE_SCALE_PARAMETERS_V2
description: This topic describes OID_GEN_RECEIVE_SCALE_PARAMETERS_V2
keywords: OID_GEN_RECEIVE_SCALE_PARAMETERS_V2, OID_GEN_RECEIVE_SCALE_PARAMETERS_V2 RSSv2
ms.date: 10/11/2017
ms.localizationpriority: medium
---

# OID_GEN_RECEIVE_SCALE_PARAMETERS_V2

[!include[RSSv2 Beta Prerelease](../includes/rssv2-beta-prerelease.md)]

The OID_GEN_RECEIVE_SCALE_PARAMETERS_V2 OID is sent to [RSSv2](receive-side-scaling-version-2-rssv2-.md)-capable miniport drivers to set run-time parameters, other than the indirection table, for a scaling entity. OID_GEN_RECEIVE_SCALE_PARAMETERS_V2 replaces the [OID_GEN_RECEIVE_SCALE_PARAMETERS](oid-gen-receive-scale-parameters.md) OID from RSSv1 and is not visible to NDIS Light Weight Filters (LWFs) before NDIS 6.80. This OID is a Regular OID and can be issued as a Query or Set request. It is issued at IRQL == PASSIVE_LEVEL. It can target a given VPort, when the *NDIS_OID_REQUEST_FLAGS_VPORT_ID_VALID* flag is set at NIC switch creation. Otherwise, it targets the physical NIC in the Native RSS case.

As a Query, NDIS and overlying drivers can use OID_GEN_RECEIVE_SCALE_PARAMETERS_V2 to query the RSS parameters of a NIC. NDIS returns an [NDIS_RECEIVE_SCALE_PARAMETERS_V2](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_parameters_v2) structure that defines the current RSS parameters.

As a Set, the purpose of this OID is to perform the following actions:

- Initially configure the scaling entity (a miniport adapter in Native RSS mode or a VPort in VMQ mode).
- Enable or disable RSS.
- When in RSS mode, perform non-timing-critical management functions such as changing the hash key, hash type and hash function, number of queues, or number of indirection table entries for the scaling entity.

## Remarks

Enabling RSS and setting RSS parameters can be performed in one step.. After the upper layer enables RSS using this OID, the initial state of the scaling entity is as follows:

- The primary processor becomes *inactive*.
- The default processor becomes *active*.
- All the ITEs become *active*.
- The miniport driver starts calculation of the RSS hash, setting of the corresponding OOB for all packets, and directing packets to a processor specified by the indirection table entry or default processor parameter.

After RSS is enabled, the upper layer issues the [OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES](oid-gen-rss-set-indirection-table-entries.md) OID to move ITEs to different processors. In RSSv2, the **DefaultQueue** and **PrimaryProcessor** are also moved to a different processor using OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES.

During the process of disabling RSS, the upper layer will point all ITEs to the primary processor before invoking this OID to turn RSS off. After this point, receive traffic should target the primary processor. However, miniport drivers should not expect the disabling of RSS before VPort deletion. The upper layer can set the receive filter on the VPort to zero, thus ensuring that no receive traffic is flowing through the VPort, then proceed to delete the VPort without disabling RSS.

The upper layer will ensure that important invariants are not violated before performing management functions. For example:

- Before changing the number of queues, the upper layer will ensure that the indirection table does not reference more processors than configured for a VPort.
Before changing the number of indirection table entries for VMMQ-RESTRICTED adapters, the upper layer will ensure that the content of the indirection table is normalized to the power of 2.

### Error conditions and status codes

This OID returns the following status codes when an error occurs:

| Status code | Error condition |
| --- | --- |
| NDIS_STATUS_INVALID_LENGTH | The OID was malformed. |
| NDIS_STATUS_NO_QUEUES | The number of queues is being changed when RSS is enabled, but the current indirection table references more processors than the new number of queues. |
| NDIS_STATUS_INVALID_DATA | <ul><li>The indirection table is being reduced in size, but does not contain a power-of-two repeat pattern.</li><li>During an RSS state transition (to *on* or *off*), a processor from a steering parameter that becomes *active* does not belong to the adapter's RSS processor set. Note that *inactive* steering parameters are only tracking writes to the processor and are not enforced. Enforcement happens during RSS state transition when the parameter becomes *active*.</li></ul> |
| NDIS_STATUS_INVALID_PARAMETER | Other fields, either in the header or the OID itself, contain invalid values. |

## Requirements

**Version**: Windows 10, version 1709
**Header**: Ntddndis.h (include Ndis.h)

## See also

- [Receive Side Scaling Version 2 (RSSv2)](receive-side-scaling-version-2-rssv2-.md)
- [OID_GEN_RECEIVE_SCALE_PARAMETERS](oid-gen-receive-scale-parameters.md)
- [NDIS_RECEIVE_SCALE_PARAMETERS_V2](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_parameters_v2)
- [OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES](oid-gen-rss-set-indirection-table-entries.md)
