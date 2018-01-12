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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20DUAL_OPLOCK_KEY_ECP_CONTEXT%20structure%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





