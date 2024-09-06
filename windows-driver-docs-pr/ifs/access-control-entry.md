---
title: Access Control Entry
description: Access Control Entry
keywords:
- security descriptors WDK file systems , access control entry
- descriptors WDK file systems , access control entry
- access control entry WDK file systems
- ACE WDK file systems
- security identifiers WDK file systems
- SIDs WDK file systems
ms.date: 09/05/2024
---

# Access Control Entry

An [access control entry](ace.md) (ACE) describes access rights associated with a particular security identifier (SID). The OS evaluates ACEs to compute the effective access granted to a particular program based on its credentials. For example, when a user signs in the computer and then executes a program, the program uses the credentials associated with that particular user's account.

When a program attempts to open an object, Windows compares the credentials associated with the program against the security controls associated with the object. The security reference monitor then uses the ACE information to determine if the program should be allowed or denied access to the given object. It's the ACE that determines the behavior of the security subsystem.

The following figure illustrates the access control entry.

:::image type="content" source="images/fssecurity-04.png" alt-text="Diagram illustrating the access control entry.":::

The security subsystem uses several types of ACES, including the following types. The **Type** member of the ACE structure controls the interpretation of the ACE. The defined types are:

- **ACCESS_ALLOWED_ACE_TYPE**—this type indicates that the ACE specifies access rights that granted to the specific SID.

- **ACCESS_DENIED_ACE_TYPE** indicates that the ACE specifies access rights that are to be denied to the specific SID.

- **SYSTEM_AUDIT_ACE_TYPE** indicates that the ACE specifies auditing behavior.

- **SYSTEM_ALARM_ACE_TYPE** indicates that the ACE specifies alarm behavior.

- **ACCESS_ALLOWED_COMPOUND_ACE_TYPE** indicates that the ACE is tied to a particular server and the entity it's impersonating.

The ACCESS_*XXX* types are used to control programmatic access to an object. The SYSTEM_*XXX* types are used to control the audit and alarm behavior of the security subsystem when the object is accessed. The actual behavior of the security subsystem is computed by combining the information for some or all of the ACEs associated with the object.

A driver can construct an ACE of **ACCESS_ALLOWED_ACE_TYPE** using the [**RtlAddAccessAllowedAce**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-rtladdaccessallowedace) routine. To add the other types of ACE entries, driver writers must construct their own functions because the WDK doesn't provide other support routines.
