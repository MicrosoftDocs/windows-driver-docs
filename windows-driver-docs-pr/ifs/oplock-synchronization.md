---
title: Oplock synchronization
description: Describes how filters and file systems handle oplock synchronization
ms.date: 01/08/2021
---

# Oplock synchronization

Filters and file systems that request [exclusive opportunistic locks](oplock-overview.md) (oplocks) must synchronize calls into the system-supplied oplock package. In particular, calls to oplock FSCTRL routines (to establish oplocks), must be synchronized against calls to oplock check-break routines. A list of both sets of routines include:

* Oplock FSCTRL routines:

  * Minifilters: [**FltOplockFsctrl**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockfsctrl), [**FltOplockFsctrlEx**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockfsctrlex)
  * Legacy filters and file systems: [**FsRtlOplockFsctrl**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockfsctrl), [**FsRtlOplockFsctrlEx**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockfsctrlex), [**FsRtlUpperOplockFsctrl**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlupperoplockfsctrl)

* Oplock check-break routines:

  * Minifilters: [**FltCheckOplock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcheckoplock),  [**FltCheckOplockEx**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcheckoplockex)
  * Legacy filters and file systems: [**FsRtlCheckOplock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlcheckoplock), [**FsRtlCheckOplockEx**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlcheckoplockex), [**FsRtlCheckOplockEx2**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlcheckoplockex2), [**FsRtlOplockBreakH**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockbreakh)

When processing an oplock request, filters and file systems must ensure the following:

* I/O that might break an oplock cannot occur in parallel with processing the request.
* Oplock requests cannot happen concurrently with oplock break acknowledgements.

IRP calls that request the creation of exclusive oplocks for the same file control block (FCB) are:

* [IRP_MJ_CREATE](irp-mj-create.md) with the FILE_OPEN_REQUIRING_OPLOCK bit set in Create.Options
* [IRP_MJ_FILE_SYSTEM_CONTROL](irp-mj-file-system-control.md) with oplock controls

The following are some examples of oplock synchronization:

* When processing an oplock request, a file system would acquire some resource exclusively, call [**FsRtlOplockFsctrlEx**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockfsctrlex), and release the resource.

* When processing an oplock break acknowledgment, the file system would acquire that same resource shared, call [**FsRtlOplockFsctrlEx**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockfsctrlex), and release the resource.

* When performing I/O, the file system would acquire that same resource shared, call [**FsRtlCheckOplockEx2**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlcheckoplockex2), perform the I/O, and release the resource.

  Upper file systems should ensure that they synchronize between calls of [**FsRtlCheckUpperOplock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlcheckupperoplock) and [**FsRtlUpperOplockFsctrl**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlupperoplockfsctrl) in a similar fashion.
