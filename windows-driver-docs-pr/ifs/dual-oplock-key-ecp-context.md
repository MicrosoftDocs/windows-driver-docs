---
title: DUAL\_OPLOCK\_KEY\_ECP\_CONTEXT structure
description: The DUAL\_OPLOCK\_KEY\_ECP\_CONTEXT structure contains the extra create parameter context for a dual oplock key. Oplocks keys for both a target and a parent file object can be set in this structure.
ms.assetid: 7E337D2F-7292-4D18-B750-8361A83C8B1F
keywords: ["DUAL_OPLOCK_KEY_ECP_CONTEXT structure Installable File System Drivers", "PDUAL_OPLOCK_KEY_ECP_CONTEXT structure pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- DUAL_OPLOCK_KEY_ECP_CONTEXT
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# DUAL\_OPLOCK\_KEY\_ECP\_CONTEXT structure


The **DUAL\_OPLOCK\_KEY\_ECP\_CONTEXT** structure contains the extra create parameter context for a dual oplock key. Oplocks keys for both a target and a parent file object can be set in this structure.

Syntax
------

```ManagedCPlusPlus
typedef struct _DUAL_OPLOCK_KEY_ECP_CONTEXT {
  GUID    ParentOplockKey;
  GUID    TargetOplockKey;
  BOOLEAN ParentOplockKeySet;
  BOOLEAN TargetOplockKeySet;
} DUAL_OPLOCK_KEY_ECP_CONTEXT, *PDUAL_OPLOCK_KEY_ECP_CONTEXT;
```

Members
-------

**ParentOplockKey**  
A **GUID** representing the parent oplock key value.

**TargetOplockKey**  
A **GUID** representing the target oplock key value.

**ParentOplockKeySet**  
Set to TRUE if **ParentOplockKey** contains a valid GUID for the parent's oplock key.

**TargetOplockKeySet**  
Set to TRUE if **TargetOplockKey** contains a valid GUID for the target's oplock key.

Remarks
-------

The **DUAL\_OPLOCK\_KEY\_ECP\_CONTEXT** structure provides dual oplock keys to allow oplock requests on files and directories. Like the [**OPLOCK\_KEY\_ECP\_CONTEXT**](oplock-key-ecp-context.md) structure, **DUAL\_OPLOCK\_KEY\_ECP\_CONTEXT** is set in an extra create parameter list ([**ECP\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff540148)) and later associated with a file object during processing of [**IRP\_MJ\_CREATE**](irp-mj-create.md) by a file system or file system filter driver.

The value **GUID\_ECP\_DUAL\_OPLOCK\_KEY** is used when calling support routines such as [**FsRtlAllocateExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff545609), [**FsRtlInitializeExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff546113), or [**FltRemoveExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff544339).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>This structure is available starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include Ntifs.h)</td>
</tr>
</tbody>
</table>

## See also


[**ECP\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff540148)

[**IO\_DRIVER\_CREATE\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff548565)

[**IoCreateFileEx**](https://msdn.microsoft.com/library/windows/hardware/ff548283)

[**IRP\_MJ\_CREATE**](irp-mj-create.md)

[**OPLOCK\_KEY\_ECP\_CONTEXT**](oplock-key-ecp-context.md)

[Oplock Semantics](https://msdn.microsoft.com/library/windows/hardware/ff551007)

 

 






