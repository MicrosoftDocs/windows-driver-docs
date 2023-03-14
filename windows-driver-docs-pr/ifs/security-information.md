---
title: SECURITY_INFORMATION
description: SECURITY_INFORMATION
ms.date: 03/13/2023
ms.topic: reference
---

# SECURITY_INFORMATION

``` syntax
typedef ULONG SECURITY_INFORMATION, *PSECURITY_INFORMATION;
```

A value of type SECURITY_INFORMATION is used to identify the object-related security information being set or queried. This security information includes:

- The owner of an object
- The primary group of an object
- The discretionary access-control list (DACL) of an object
- The system ACL (SACL) of an object

Each item of security information is designated by a bit flag. The following sections specify the bits.

## DACL_SECURITY_INFORMATION

Indicates that the object's DACL is being set or queried.

For the following items, the DACL is queried:

- IRP_MJ_QUERY_SECURITY
- FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY
- FltQuerySecurityObject
- SeQuerySecurityDescriptorInfo

For the following items, the DACL is set:

- IRP_MJ_SET_SECURITY
- FLT_PARAMETERS for IRP_MJ_SET_SECURITY
- FltSetSecurityObject
- SeSetSecurityDescriptorInfo
- SeSetSecurityDescriptorInfoEx

Requires READ_CONTROL access for:

- IRP_MJ_QUERY_SECURITY
- FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY
- FltQuerySecurityObject
- SeQuerySecurityDescriptorInfo

Requires WRITE_DAC access for:

- IRP_MJ_SET_SECURITY
- FLT_PARAMETERS for IRP_MJ_SET_SECURITY
- FltSetSecurityObject
- SeSetSecurityDescriptorInfo
- SeSetSecurityDescriptorInfoEx

## GROUP_SECURITY_INFORMATION

Indicates that the primary group identifier of the object is being set or queried.

For the following items, the group identifier is queried:

- IRP_MJ_QUERY_SECURITY
- FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY
- FltQuerySecurityObject
- SeQuerySecurityDescriptorInfo
- IRP_MJ_SET_SECURITY
- FLT_PARAMETERS for IRP_MJ_SET_SECURITY

For the following items, the group identifier is set:

- FltSetSecurityObject
- SeSetSecurityDescriptorInfo
- SeSetSecurityDescriptorInfoEx

Requires READ_CONTROL access for:

- IRP_MJ_QUERY_SECURITY
- FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY
- FltQuerySecurityObject
- SeQuerySecurityDescriptorInfo

Requires WRITE_OWNER access for:

- IRP_MJ_SET_SECURITY
- FLT_PARAMETERS for IRP_MJ_SET_SECURITY
- FltSetSecurityObject
- SeSetSecurityDescriptorInfo
- SeSetSecurityDescriptorInfoEx

## OWNER_SECURITY_INFORMATION

Indicates that the owner identifier of the object is being set or queried.

For the following items, the owner identifier is queried:

- IRP_MJ_QUERY_SECURITY
- FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY
- FltQuerySecurityObject
- SeQuerySecurityDescriptorInfo
- IRP_MJ_SET_SECURITY
- FLT_PARAMETERS for IRP_MJ_SET_SECURITY

For the following items, the owner identifier is set:

- FltSetSecurityObject
- SeSetSecurityDescriptorInfo
- SeSetSecurityDescriptorInfoEx

Requires READ_CONTROL access for:

- IRP_MJ_QUERY_SECURITY
- FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY
- FltQuerySecurityObject
- SeQuerySecurityDescriptorInfo

Requires WRITE_OWNER access for:

- IRP_MJ_SET_SECURITY
- FLT_PARAMETERS for IRP_MJ_SET_SECURITY
- FltSetSecurityObject
- SeSetSecurityDescriptorInfo
- SeSetSecurityDescriptorInfoEx

## SACL_SECURITY_INFORMATION

Indicates that the object's SACL is being set or queried.

For the following items, the SACL is queried:

- IRP_MJ_QUERY_SECURITY
- FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY
- FltQuerySecurityObject
- SeQuerySecurityDescriptorInfo
- IRP_MJ_SET_SECURITY
- FLT_PARAMETERS for IRP_MJ_SET_SECURITY

For the following items, the SACL is set:

- FltSetSecurityObject
- SeSetSecurityDescriptorInfo
- SeSetSecurityDescriptorInfoEx

Requires ACCESS_SYSTEM_SECURITY access in all cases.

## PROCESS_TRUST_LABEL_SECURITY_INFORMATION

Reserved.

## Requirements

Wdm.h (include Wdm.h)

## Related articles

[**ACL**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_acl)

[**SECURITY_DESCRIPTOR**](/previous-versions/windows/hardware/drivers/ff556610(v=vs.85))

[**SeQuerySecurityDescriptorInfo**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-sequerysecuritydescriptorinfo)

[**SeSetSecurityDescriptorInfo**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-sesetsecuritydescriptorinfo)

[**SeSetSecurityDescriptorInfoEx**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-sesetsecuritydescriptorinfoex)

[**ZwQuerySecurityObject**](/previous-versions/ff567066(v=vs.85))

[**ZwSetSecurityObject**](/previous-versions/ff567106(v=vs.85))
