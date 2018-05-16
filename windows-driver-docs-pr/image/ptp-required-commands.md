---
title: PTP Required Commands
author: windows-driver-content
description: PTP Required Commands
ms.assetid: 98f4be09-0f13-45a1-b28a-c027e57c0dd7
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PTP Required Commands


## <a href="" id="ddk-ptp-required-commands-si"></a>


PTP drivers must support commands marked as mandatory in the *Conformance Section* (chapter 14) of the PIMA15740 specification. The only exception is that the **GetNumObjects** command is not used. In other words, if a device is compliant with the PIMA15740 specification, it will work with Microsoft Windows Me, Windows XP, and later.

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

 

 




