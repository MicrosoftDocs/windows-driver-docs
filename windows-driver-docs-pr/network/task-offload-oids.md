---
title: Task offload OIDs
description: This topic describes Task offload OIDs 
ms.assetid: 0d7eab31-d5c9-4264-9598-c72e19e1d86b
keywords:
- Task offload OIDs, task offload NDIS OIDs, task offload OIDs WDK, task offload OIDs networking
ms.date: 11/06/2017
ms.localizationpriority: medium
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

