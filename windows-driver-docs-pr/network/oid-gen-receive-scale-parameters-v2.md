---
title: OID_GEN_RECEIVE_SCALE_PARAMETERS_V2
description: This topic describes OID_GEN_RECEIVE_SCALE_PARAMETERS_V2
ms.assetid: 3897A898-2B00-45DF-AC05-7EC719EB7353
keywords: OID_GEN_RECEIVE_SCALE_PARAMETERS_V2, OID_GEN_RECEIVE_SCALE_PARAMETERS_V2 RSSv2
ms.author: windowsdriverdev
ms.date: 10/11/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

[!include[RSSv2 Beta Prerelease](../rssv2-beta-prerelease.md)]

# OID_GEN_RECEIVE_SCALE_PARAMETERS_V2

The OID_GEN_RECEIVE_SCALE_PARAMETERS_V2 OID is sent to RSSv2-capable miniport drivers to set run-time parameters, other than the indirection table, for a scaling entity. OID_GEN_RECEIVE_SCALE_PARAMETERS_V2 replaces the older [OID_GEN_RECEIVE_SCALE_PARAMETERS](oid-gen-receive-scale-parameters.md) OID from RSSv1 and is not visible to NDIS Light Weight Filters (LWFs) before NDIS 6.80. This OID is a Regular OID and can be issued as a Query or Set request. It is issued at IRQL = PASSIVE_LEVEL. It can target a given VPort, when the *NDIS_OID_REQUEST_FLAGS_VPORT_ID_VALID* flag is set at NIC switch creation. Otherwise, it targets the physical NIC in the Native RSS case.

As a Query, NDIS and overlying drivers can use OID_GEN_RECEIVE_SCALE_PARAMETERS_V2 to query the RSS parameters of a NIC. NDIS returns an [NDIS_RECEIVE_SCALE_PARAMETERS_V2](https://msdn.microsoft.com/library/windows/hardware/96EAB6EE-BF9A-46AD-8DED-5D9BD2B6F219) structure that defines the current RSS parameters.

As a Set, the purpose of this OID is to perform the following actions:

- Initially configure the scaling entity (a miniport adapter in Native RSS mode or a VPort in VMQ mode)
- Enable or disable RSS
- When in RSS mode, perform non-timing-critical management functions such as changing the hash key, number of queues, or number of indirection table entries

## Remarks

Enabling RSS and setting RSS parameters can be performed in one step, using the **NDIS_RECEIVE_SCALE_PARAMETERS_V2** structure. After the upper layer enables RSS using this OID, the initial state of the scaling entity is as follows:

- **DefaultProcessor** is the same as **PrimaryProcessor**
- All the indirection table entries (ITEs) also point to the **PrimaryProcessor** (as specified during VPort creation) in VMMQ mode, or to the **BasePRocessor** in Native RSS mode
- Hash is being calculated and set in the corresponding OOB for all packets

After RSS is enabled, the upper layer issues the [OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES](oid-gen-rss-set-indirection-table-entries.md) OID to move ITEs to different processors. In RSSv2, the **DefaultQueue** and **PrimaryProcessor** are also moved to a different processor using OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES.

During the process of disabling RSS, the upper layer will point all ITEs to the primary processor before invoking this OID to turn RSS off. After this point, receive traffic should target the primary processor. However, miniport drivers should not expect the disabling of RSS before VPort deletion. The upper layer can set the receive filter on the VPort to zero, thus ensuring that no receive traffic is flowing through the VPort, then proceed to delete the VPort without disabling RSS.

The upper layer will ensure that important invariants are not violated before performing management functions. For example:

- Before changing the number of queues, the upper layer will ensure that the indirection table does not reference more processors than configured for a VPort.
Before changing the number of indirection table entries for VMMQ-RESTRICTED adapters, the upper layer will ensure that the content of the indirection table is normalized to the power of 2.

## Requirements

| | |
| --- | --- |
| Version | Windows 10, version 1709 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

- [Receive Side Scaling Version 2 (RSSv2)](receive-side-scaling-version-2-rssv2-.md)
- [OID_GEN_RECEIVE_SCALE_PARAMETERS](oid-gen-receive-scale-parameters.md)
- [NDIS_RECEIVE_SCALE_PARAMETERS_V2](https://msdn.microsoft.com/library/windows/hardware/96EAB6EE-BF9A-46AD-8DED-5D9BD2B6F219)
- [OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES](oid-gen-rss-set-indirection-table-entries.md)

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")