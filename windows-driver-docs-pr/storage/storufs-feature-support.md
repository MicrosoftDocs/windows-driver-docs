---
title: Features supported by StorUFS
description: Overview of Features supported by StorUFS
ms.date: 11/13/2023
---

# Features supported by StorUFS

The Microsoft Universal Flash Storage (UFS) driver (*storufs.sys*) is the system-supplied storage miniport driver that provides access to UFS devices. It's available starting in Windows 10. The following sections outline the support provided by **StorUFS** for Windows 10 and later versions.

## List of SCSI commands that StorUFS supports

* INQUIRY
* READ (10)
* REPORT LUNS
* REQUEST SENSE
* SEND DIAGNOSTIC
* START STOP UNIT
* TEST UNIT READY
* UNMAP
* WRITE (10)
* WRITE BUFFER

## List of supported UFS commands from initiator device driver to target device

* NOP_OUT        (0x00)
* UPIU_COMMAND   (0x01)
* DATA_OUT       (0x02)
* TASK_MAN_REQ   (0x04)
* QUERY_REQ      (0x16)
* NOP_IN         (0x20)
* RESPONSE       (0x21)
* DATA_IN        (0x22)
* TASK_MAN_RESP  (0x24)
* QUERY_RESP     (0x36)

## List of features that UFS driver supports

* Boot from UFS
* Replay Protected Memory Block (RPMB)
* Host performance boost (HPB)*
* Write booster**
* Runtime power management
* Firmware upgrade
* Command queue mgmt
* Inline Crypto Engine (ICE) support

\* *Write booster feature currently supported on UFS 3.1+ Intel platforms.*

\** *HPB feature is currently supported on UFS 3.1+ Samsung platforms.*
