---
title: Task offload OIDs
author: windows-driver-content
description: This topic describes Task offload OIDs 
ms.assetid: 0d7eab31-d5c9-4264-9598-c72e19e1d86b
keywords:
- Task offload OIDs, task offload NDIS OIDs, task offload OIDs WDK, task offload OIDs networking
ms.author: windowsdriverdev
ms.date: 11/06/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Task offload OIDs

The following table summarizes the OIDs that support TCP/IP task offload operations. For more info about such operations, see [TCP/IP Task Offload](task-offload.md).-ndis-status-dot11-wfd-group-operating-channel.md

In this table, M indicates an OID is mandatory, while O indicates it is optional.

| Length | Query | Set | Name |
| --- | --- | --- | --- |
| Arr |   | M | [OID_TCP_TASK_IPSEC_ADD_SA](oid-tcp-task-ipsec-add-sa.md) |
| Arr |   | M | [OID_TCP_TASK_IPSEC_ADD_UDPESP_SA](oid-tcp-task-ipsec-add-udpesp-sa.md) |
| 4 |   | M | [OID_TCP_TASK_IPSEC_DELETE_SA](oid-tcp-task-ipsec-delete-sa.md) |
| 4 |   | M | [OID_TCP_TASK_IPSEC_DELETE_UDPESP_SA](oid-tcp-task-ipsec-delete-udpesp-sa.md) |
| Arr | M | M | [OID_TCP_TASK_OFFLOAD](oid-tcp-task-offload.md) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")