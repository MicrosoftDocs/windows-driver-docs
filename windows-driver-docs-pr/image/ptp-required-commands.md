---
title: PTP Required Commands
description: PTP Required Commands
ms.assetid: 98f4be09-0f13-45a1-b28a-c027e57c0dd7
ms.date: 07/18/2018
ms.localizationpriority: medium
---

# PTP Required Commands

PTP drivers must support commands marked as mandatory in the *Conformance Section* (chapter 14) of the PIMA15740 specification. The only exception is that the **GetNumObjects** command is not used.

The full list of required PTP commands is:

0x1001 **GetDeviceInfo**

0x1002 **OpenSession**

0x1003 **CloseSession**

0x1004 **GetStorageIDs**

0x1005 **GetStorageInfo**

0x1007 **GetObjectHandles**

0x1008 **GetObjectInfo**

0x1009 **GetObject**

0x100A **GetThumb**

