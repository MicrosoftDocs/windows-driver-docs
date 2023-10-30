---
title: Kernel Extended Attributes
description: Filter Manager and Minifilter Driver Architecture
keywords:
- Extended , File Attributes
- Kernel EA
- Extended Attributes
- $Kernel
ms.date: 08/09/2023
---
# Kernel Extended Attributes

Starting in Windows 8, NTFS supports Kernel Extended Attributes (Kernel EAs). Verifying an image's signature is an expensive operation. Storing information about whether a previously validated binary has been changed reduces the number of instances where an image has to undergo a full signature check. Using Kernel EAs for this reason boosts the performance of image file signature validation.

EAs with the name prefix ``$Kernel`` can only be modified from kernel mode. Any EA that begins with this string is considered a Kernel EA. Before retrieving the necessary update sequence number (USN), it's recommended to first issue **FSCTL_WRITE_USN_CLOSE_RECORD** to commit any pending USN Journal updates on the file that may have occurred earlier. Otherwise, the **FileUSN** value may change shortly after setting the Kernel EA.

It's recommended that a Kernel EA contains at least the following information:

- USN UsnJournalID

  - The **UsnJournalID** field is a GUID that identifies the current incarnation of USN Journal File. The USN Journal can be deleted and created from user mode per volume. Each time the USN Journal is created a new **UsnJournalID** GUID is generated. With this field, you can tell if there was a period of time where the USN Journal was disabled and can revalidate.
    - This value can be retrieved using [FSCTL_QUERY_USN_JOURNAL](/windows/win32/api/winioctl/ni-winioctl-fsctl_query_usn_journal).
- USN FileUSN
  - The **FileUSN** value contains the USN ID of the last change that was made to the file and is tracked inside the Master File Table (MFT) record for the given file.
    - When the USN Journal is deleted, **FileUSN** is reset to zero.

This information, along with any other a given usage might need, is then set on the file as a Kernel EA.

## Setting a Kernel Extended Attribute

In order to set a Kernel EA, it must begin with the prefix ``"$Kernel."`` followed by a valid EA name string. An attempt to set a Kernel EA from user mode is silently ignored. The request returns **STATUS_SUCCESS** but no actual EA modification is made. Calling an API like [ZwSetEaFile](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwseteafile) or [FltSetEaFile](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltseteafile) to set a Kernel EA from kernel mode isn't sufficient because SMB supports the setting of EAs across the network and those requests are issued from kernel mode on the server.

To set a Kernel EA, the caller must also set the **IRP_MN_KERNEL_CALL** value in the MinorFunction field of the IRP (I/O request packet). Since the only way to set this field is by generating a custom IRP, the routine [FsRtlSetKernelEaFile](/previous-versions/mt807493(v=vs.85)) has been exported from the FsRtl package as a support function to set up a Kernel EA.

Starting in Windows 10 version 1803, user EAs and kernel EAs can be intermixed. Setting a kernel EA doesn't generate a USN_REASON_EA_CHANGE record to the USN Journal. The system does generate USN_REASON_EA_CHANGE when any user EAs are set.

## Querying an Extended Attribute

Querying the EAs on a file from user mode returns both normal and Kernel EAs. They're returned to user mode to minimize any application compatibility issues. The normal [ZwQueryEaFile](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwqueryeafile) and [FltQueryEaFile](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltqueryeafile) operations return both normal and kernel EAs from both user and kernel modes.

When only a **FileObject** is available, using [FsRtlQueryKernelEaFile](/previous-versions/mt807492(v=vs.85)) may be more convenient for use to query for Kernel EAs from kernel mode.

## Querying Update Sequence Number Journal Information

The [FSCTL_QUERY_USN_JOURNAL](/windows/win32/api/winioctl/ni-winioctl-fsctl_query_usn_journal) operation requires **SE_MANAGE_VOLUME_PRIVILEGE** even when issued from kernel mode unless the **IRP_MN_KERNEL_CALL** value was set in the MinorFunction field of the IRP. The routine **FsRtlKernelFsControlFile** has been exported from the FsRtl package in the Kernel to easily allow kernel mode components to issue this USN request.

**NOTE** Starting with Windows 10, version 1703 and later this operation no longer requires SE_MANAGE_VOLUME_PRIVILEGE.

## Auto-Deletion of Kernel Extended Attributes

Simply rescanning a file because the USN ID of the file changed can be expensive as there are many benign reasons a USN update may be posted to the file. To simplify this, an auto delete of Kernel EAs feature was added to NTFS.

Because not all Kernel EAs may want to be deleted in this scenario, an extended EA prefix name is used. If a Kernel EA begins with:  ``"$Kernel.Purge."`` then if any of the following USN reasons are written to the USN journal, NTFS deletes all kernel EAs that exist on that file that conforms to the given naming syntax:
  
- USN_REASON_DATA_OVERWRITE
- USN_REASON_DATA_EXTEND
- USN_REASON_DATA_TRUNCATION
- USN_REASON_REPARSE_POINT_CHANGE

This delete of Kernel EAs is successful even in low memory situations.

## Remarks

User-mode components can't tamper with kernel EAs. Kernel EAs can exist in the same file as a normal EA.

## See Also

[FltQueryEaFile](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltqueryeafile)  
[FltSetEaFile](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltseteafile)  
[FSCTL_QUERY_USN_JOURNAL](/windows/win32/api/winioctl/ni-winioctl-fsctl_query_usn_journal)  
[FsRtlQueryKernelEaFile](/previous-versions/mt807492(v=vs.85))
[FsRtlSetKernelEaFile](/previous-versions/mt807493(v=vs.85))  
[ZwQueryEaFile](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwqueryeafile)  
[ZwSetEaFile](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwseteafile)
