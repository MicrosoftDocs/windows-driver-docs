---
title: Access Control Entry (ACE)
description: ACE
keywords: ["access control entry WDK file systems", "ACE WDK file systems"]
ms.date: 03/13/2023
ms.topic: reference
---

# Access control entry (ACE)

An ACE is an access control entry in an access-control list (ACL).

The following values are the currently defined ACE types.

| Value | Meaning |
| ----- | ------- |
| ACCESS_ALLOWED_ACE | Grants specified rights to a user or group. This ACE is stored in a discretionary ACL (DACL). |
| ACCESS_DENIED_ACE  | Denies specified rights to a user or group. This ACE is stored in a DACL. |
| SYSTEM_AUDIT_ACE   | Specifies what types of access cause system-level audits. This ACE is stored in a system ACL (SACL). |

A fourth ACE structure, SYSTEM_ALARM_ACE, isn't currently supported.

 An ACL contains a list of zero or more ACEs. Each ACE controls or monitors access to an object by a specified trustee. Specifically, an ACE:

* Defines access to an object for a specific user or group, or
* Defines the types of access that generate system-administration messages or alarms for a specific user or group.

A security identifier (SID) identifies the user or group.

Each ACE starts with an [**ACE_HEADER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_ace_header) structure. The format of the data following the header varies according to the ACE type specified in the header. This structure must be aligned on a 32-bit boundary.

Requirements: ntifs.h (include ntifs.h)

## Related articles

[**ACCESS_ALLOWED_ACE**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_access_allowed_ace)

[**ACCESS_DENIED_ACE**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_access_denied_ace)

[**ACE_HEADER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_ace_header)

[**ACL**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_acl)

[**RtlAddAccessAllowedAce**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-rtladdaccessallowedace)

[**RtlGetAce**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-rtlgetace)

[**SID**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_sid)

[**SYSTEM_ALARM_ACE**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_system_alarm_ace)

[**SYSTEM_AUDIT_ACE**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_system_audit_ace)
