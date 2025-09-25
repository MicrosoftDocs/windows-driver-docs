---
title: CLFS Support for Archiving
description: CLFS support for archiving
keywords: ["Common Log File System WDK kernel , archiving", "CLFS WDK kernel , archiving", "archiving WDK CLFS", "non-ephemeral logs WDK CLFS", "archive tail WDK CLFS"]
ms.date: 09/19/2025
ms.topic: concept-article
---

# CLFS support for archiving

Common Log File System (CLFS) supports archiving for dedicated logs by maintaining an archive tail. When you call [**ClfsCreateLogFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatelogfile) to create a dedicated log, you can set the FILE_ATTRIBUTE_ARCHIVE flag of the *fFlagsAndAttributes* parameter to specify that CLFS should maintain an archive tail for the log. A log for which CLFS maintains an archive tail is called a *non-ephemeral log*.

Suppose you're performing transactions on a database and each transaction has several updates described by log records. After a particular transaction has committed and been written to stable storage, you might not need the log records that describe that transaction anymore. That is, the log records wouldn't be needed during restart recovery if there's a system failure. However, if the stable storage medium that holds the database fails and the database hasn't been recently archived on a different medium, the database updates could be lost.

The preceding paragraph describes archiving database records, but in other scenarios you might want to archive log records. In either case, archiving is the responsibility of the clients (your software). You can keep track of the archiving you've done by setting the log's archive tail. The archive tail is the log sequence number (LSN) of the oldest record for which archiving hasn't yet been completed.

A non-ephemeral log actually has two tails: one marked by the base LSN and one marked by the archive tail. You can position the two tails as you see fit by calling [**ClfsAdvanceLogBase**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsadvancelogbase) (or [**ClfsWriteRestartArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfswriterestartarea)), and [**ClfsSetArchiveTail**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfssetarchivetail). Typically the base LSN points to the oldest record that would still be needed for transaction rollback or restart recovery, and the archive tail points to the oldest record for which archiving hasn't been performed. The archive tail might be less than the base LSN or it might be greater than the base LSN.

The base LSN and the archive tail are important when you call [**ClfsReadNextLogRecord**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreadnextlogrecord) repeatedly to read a chain of records linked by previous LSNs, undo-next LSNs, or user LSNs. **ClfsReadNextLogRecord** doesn't read a record whose LSN is less than both the archive tail and the base LSN. It will, however, read a record whose LSN is between the archive tail and the base LSN. For more information about following record chains, see [Reading Data Records from a CLFS Stream](reading-data-records-from-a-clfs-stream.md).

## See also

[**ClfsAdvanceLogBase**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsadvancelogbase)

[**ClfsCreateLogFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatelogfile)

[**ClfsReadNextLogRecord**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreadnextlogrecord)

[**ClfsSetArchiveTail**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfssetarchivetail)

[**ClfsWriteRestartArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfswriterestartarea)

[Reading Data Records from a CLFS Stream](reading-data-records-from-a-clfs-stream.md)
