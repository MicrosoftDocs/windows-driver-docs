---
title: OPLOCK\_KEY\_ECP\_CONTEXT structure
description: The OPLOCK\_KEY\_ECP\_CONTEXT structure is used to attach an oplock key to a file.
ms.assetid: 029dd105-162a-4674-a3d5-b54a91fa4be2
keywords: ["OPLOCK_KEY_ECP_CONTEXT structure Installable File System Drivers", "POPLOCK_KEY_ECP_CONTEXT structure pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- OPLOCK_KEY_ECP_CONTEXT
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# OPLOCK\_KEY\_ECP\_CONTEXT structure


The OPLOCK\_KEY\_ECP\_CONTEXT structure is used to attach an oplock key to a file.

Syntax
------

```ManagedCPlusPlus
typedef struct _OPLOCK_KEY_ECP_CONTEXT {
  GUID  OplockKey;
  ULONG Reserved;
} OPLOCK_KEY_ECP_CONTEXT, *POPLOCK_KEY_ECP_CONTEXT;
```

Members
-------

**OplockKey**  
A GUID for the oplock key. This GUID is shared among different handles and identifies them as belonging to the same client cache. When two handles share the same oplock key, a request performed on one handle will not break an outstanding oplock on the other handle.

**Reserved**  
Reserved. Must be set to zero.

Remarks
-------

For information about how to use ECPs to associate extra information with a file when the file is created, see [Using Extra Create Parameters with an IRP\_MJ\_CREATE Operation](https://msdn.microsoft.com/library/windows/hardware/ff557261).

The OPLOCK\_KEY\_ECP\_CONTEXT structure is read-only. You should use it to retrieve information about the oplock key ECP only. For more information about this issue, see [System-Defined ECPs](https://msdn.microsoft.com/library/windows/hardware/ff556779).

The oplock key enables an application to open multiple handles to the same stream without breaking the application's own oplock. The oplock break only occurs after the application receives a sharing violation (STATUS\_SHARING\_VIOLATION).

Oplocks are granted on stream handles when a stream is opened. Such a stream handle can be associated with an oplock key. A caller can explicitly provide the oplock key to the [**IoCreateFileEx**](https://msdn.microsoft.com/library/windows/hardware/ff548283) routine to create the stream handle. If the caller does not explicitly specify an oplock key when the caller creates the handle, the operating system treats the handle as having a unique oplock key associated with the handle, so that the handle's key differs from any other key on any other handle. If a file operation is received on a handle other than the one on which the oplock was granted, and the oplock key that is associated with the oplock's handle differs from the key that is associated with the operation's handle, and that operation is incompatible with the currently granted oplock, then that oplock is broken. The oplock breaks even if it is the same process or thread performing the incompatible operation. For example, if a process opens a stream for which an exclusive oplock is granted and the same process then opens the same stream again, by using a different (or no) oplock key, the exclusive oplock is broken immediately.

Oplock keys are associated with handles when the handles are created. You can associate a handle with an oplock key even if no oplocks are granted.

For more information about oplocks and oplock keys, see [Oplock Semantics Overview](https://msdn.microsoft.com/library/windows/hardware/ff551011).

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
<td align="left"><p>This structure is available starting with Windows 7.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include Ntifs.h or Ntddk.h)</td>
</tr>
</tbody>
</table>

## See also


[**IoCreateFileEx**](https://msdn.microsoft.com/library/windows/hardware/ff548283)

 

 






