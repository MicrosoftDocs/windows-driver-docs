---
title: Access Control in a Driver
description: Drivers protect themselves from inappropriate access through access control.
keywords:
- security WDK file systems , minimizing threats
- access control WDK file systems
- access validation WDK file systems
- validating security WDK file systems
- checking security
ms.date: 04/20/2017
---

# Access control in a driver

To protect themselves from inappropriate access, most drivers rely upon the default access controls applied by the I/O manager against their device objects. Other mechanisms are available to drivers. Perhaps the simplest for normal drivers is to apply an explicit security descriptor when they install their driver. An example of applying security descriptors to the device object is discussed in a later section.

A driver that implements its own security policy could rely upon the standard Windows APIs for assistance managing security access. In this case, the driver manages the storage of security descriptors and is responsible for invoking the security reference monitor routines to validate security. These include numerous routines, such as the following:

- [**SeAccessCheck**](/windows-hardware/drivers/ddi/wdm/nf-wdm-seaccesscheck)--this routine compares the security descriptor against the security credentials of the caller.

- [**SePrivilegeCheck**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-seprivilegecheck)--this routine determines if the given privileges are enabled for the caller.

- [**SeSinglePrivilegeCheck**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-sesingleprivilegecheck)--this routine determines if a specific privilege is enabled for the caller.

- [**SeAuditingFileOrGlobalEvents**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-seauditingfileorglobalevents)--this routine indicates if the system has enabled auditing.

- [**SeOpenObjectAuditAlarm**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-seopenobjectauditalarm)--this routine audits open object events.

This list is incomplete, but it describes a number of the key functions that can be used within a driver to perform access validation.
