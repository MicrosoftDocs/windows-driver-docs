---
title: Kernel Extended Attributes
description: Filter Manager and Minifilter Driver Architecture
keywords:
- Extended , File Attributes
- Kernel EA
- Extended Attributes
- $Kernel
ms.date: 04/20/2017
ms.localizationpriority: medium
---
# Kernel Extended Attributes
Kernel Extended Attributes (Kernel EA's) are a feature added to NTFS in Windows 8 as a way to boost the performance of image file signature validation.  It is an expensive operation to verify an images signature. Therefore, storing information about whether a binary, which has previously been validated, has been changed or not would reduce the number of instances where an image would have to undergo a full signature check.


## Overview
EA's with the name prefix ``$Kernel`` can only be modified from kernel mode. Any EA that begins with this string is considered a Kernel EA. Before retrieving the necessary update sequence number (USN), it is recommended that **FSCTL_WRITE_USN_CLOSE_RECORD** be issued first as this will commit any pending USN Journal updates on the file that may have occurred earlier. Without this, the **FileUSN** value may change shortly after setting of the Kernel EA.

It is recommended that a Kernel EA contains at least the following information:
- USN UsnJournalID
  - The **UsnJournalID** field is a GUID that identifies the current incarnation of USN Journal File.  The USN Journal can be deleted and created from user mode per volume.  Each time the USN Journal is created a new **UsnJournalID** GUID will be generated.  With this field, you can tell if there was a period of time where the USN Journal was disabled and can revalidate.
    - This value can be retrieved using [FSCTL_QUERY_USN_JOURNAL](https://msdn.microsoft.com/library/windows/desktop/aa364583).
- USN FileUSN
  - The **FileUSN** value contains the USN ID of the last change that was made to the file and is tracked inside the Master File Table (MFT) record for the given file.
    - When the USN Journal is deleted, **FileUSN** is reset to zero.

This information, along with any other a given usage might need, is then set on the file as a Kernel EA.


## Setting a Kernel Extended Attribute
In order to set a Kernel EA, it must begin with the prefix ``"$Kernel."`` and be trailed by a valid EA name string. An attempt to set a Kernel EA from user mode will be silently ignored.  The request will return **STATUS_SUCCESS** but no actual EA modification will be made. To set a Kernel EA calling an API like [ZwSetEaFile](https://msdn.microsoft.com/library/windows/hardware/ff961908) or [FltSetEaFile](https://msdn.microsoft.com/library/windows/hardware/ff544500) from kernel mode is not sufficient.  This is because SMB supports the setting of EA’s across the network and those requests will be issued from kernel mode on the server.  

To set a Kernel EA the caller must also set the **IRP_MN_KERNEL_CALL** value in the MinorFunction field of the IRP (I/O request packet). Since the only way to set this field is by generating a custom IRP, the routine [FsRtlSetKernelEaFile](https://msdn.microsoft.com/library/windows/hardware/mt807493) has been exported from the FsRtl package as a support function to set up a Kernel EA.

You may not intermix the setting of normal and kernel EA’s in the same call to [FsRtlSetKernelEaFile](https://msdn.microsoft.com/library/windows/hardware/mt807493).  If you do this the operation will be failed with **STATUS_INTERMIXED_KERNEL_EA_OPERATION**.    Setting a Kernel EA will not generate a **USN_REASON_EA_CHANGE** record to the USN Journal; as a consequence, kernel EA's and regular EA's cannot be used in the same operation.  


## Querying an Extended Attribute
Querying the EA’s on a file from user mode will return both normal and Kernel EA’s. They are returned to user mode to minimize any application compatibility issues. The normal [ZwQueryEaFile](https://msdn.microsoft.com/library/windows/hardware/ff961907) and [FltQueryEaFile](https://msdn.microsoft.com/library/windows/hardware/ff543435) operations will return both normal and kernel EA's from both user and kernel modes.

When only a **FileObject** is available, using [FsRtlQueryKernelEaFile](https://msdn.microsoft.com/library/windows/hardware/mt807492) may be more convenient for use to query for Kernel EA's from kernel mode.


## Querying Update Sequence Number Journal Information
The [FSCTL_QUERY_USN_JOURNAL](https://msdn.microsoft.com/library/windows/desktop/aa364583) operation requires **SE_MANAGE_VOLUME_PRIVILEGE** even when issued from kernel mode unless the **IRP_MN_KERNEL_CALL** value was set in the MinorFunction field of the IRP. The routine **FsRtlKernelFsControlFile** has been exported from the FsRtl package in the Kernel to easily allow kernel mode components to issue this USN request.

**NOTE** Starting with Windows 10, version 1703 and later this operation no longer requires SE_MANAGE_VOLUME_PRIVILEGE.  

## Auto-Deletion of Kernel Extended Attributes
Simply rescanning a file because the USN ID of the file changed can be expensive as there are many benign reasons a USN update may be posted to the file.  To simplify this, an auto delete of Kernel EA’s feature was added to NTFS.

Because not all Kernel EA’s may want to be deleted in this scenario, an extended EA prefix name is used.  If a Kernel EA begins with:  ``"$Kernel.Purge."`` then if any of the following USN reasons are written to the USN journal, NTFS will delete all kernel EAs that exist on that file that conforms to the given naming syntax:  
- USN_REASON_DATA_OVERWRITE
- USN_REASON_DATA_EXTEND
- USN_REASON_DATA_TRUNCATION
- USN_REASON_REPARSE_POINT_CHANGE

This delete of Kernel EA’s will be successful even in low memory situations.

## Remarks
- Kernel EA's cannot be tampered with by user mode components.
- Kernel EA’s can exist in the same file as a normal EA.


## See Also
[FltQueryEaFile](https://msdn.microsoft.com/library/windows/hardware/ff543435)  
[FltSetEaFile](https://msdn.microsoft.com/library/windows/hardware/ff544500)  
[FSCTL_QUERY_USN_JOURNAL](https://msdn.microsoft.com/library/windows/desktop/aa364583)  
[FsRtlQueryKernelEaFile](https://msdn.microsoft.com/library/windows/hardware/mt807492)      
[FsRtlSetKernelEaFile](https://msdn.microsoft.com/library/windows/hardware/mt807493)  
[ZwQueryEaFile](https://msdn.microsoft.com/library/windows/hardware/ff961907)  
[ZwSetEaFile](https://msdn.microsoft.com/library/windows/hardware/ff961908)  
