---
title: CLFS Support for Archiving
author: windows-driver-content
description: CLFS Support for Archiving
MS-HAID:
- 'Clfs\_guide\_2552a2b7-adf9-4735-ab1c-e5b16776df7a.xml'
- 'kernel.clfs\_support\_for\_archiving'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5a07d7d2-4939-48f8-bd4c-855af61034fb
keywords: ["Common Log File System WDK kernel , archiving", "CLFS WDK kernel , archiving", "archiving WDK CLFS", "non-ephemeral logs WDK CLFS", "archive tail WDK CLFS"]
---

# CLFS Support for Archiving


## <a href="" id="ddk-introduction-to-wmi-kg"></a>


Common Log File System (CLFS) supports archiving for dedicated logs by maintaining an archive tail. When you call [**ClfsCreateLogFile**](https://msdn.microsoft.com/library/windows/hardware/ff540792) to create a dedicated log, you can set the FILE\_ATTRIBUTE\_ARCHIVE flag of the *fFlagsAndAttributes* parameter to specify that CLFS should maintain an archive tail for the log. A log for which CLFS maintains an archive tail is called a *non-ephemeral log*.

Suppose you are performing transactions on a database and each transaction has several updates that are described by log records. After a particular transaction has committed and been written to stable storage, you might not need the log records that describe that transaction any more. That is, the log records would not be needed during restart recovery in the event of a system failure. However, if the stable storage medium that holds the database fails and the database has not been recently archived on a different medium, the database updates could be lost.

The preceding paragraph describes archiving database records, but in other scenarios you might want to archive log records. In either case, archiving is the responsibility of the clients (your software). You can keep track of the archiving you have done by setting the log's archive tail. The archive tail is the log sequence number (LSN) of the oldest record for which archiving has not yet been completed.

A non-ephemeral log actually has two tails: one marked by the base LSN and one marked by the archive tail. You can position the two tails as you see fit by calling [**ClfsAdvanceLogBase**](https://msdn.microsoft.com/library/windows/hardware/ff540773) (or [**ClfsWriteRestartArea**](https://msdn.microsoft.com/library/windows/hardware/ff541770)), and [**ClfsSetArchiveTail**](https://msdn.microsoft.com/library/windows/hardware/ff541744). Typically the base LSN points to the oldest record that would still be needed for transaction rollback or restart recovery, and the archive tail points to the oldest record for which archiving has not been performed. Note that the archive tail might be less than the base LSN or it might be greater than the base LSN.

The base LSN and the archive tail are important when you call [**ClfsReadNextLogRecord**](https://msdn.microsoft.com/library/windows/hardware/ff541690) repeatedly to read a chain of records linked by previous LSNs, undo-next LSNs, or user LSNs. **ClfsReadNextLogRecord** will not read a record whose LSN is less than both the archive tail and the base LSN. It will, however, read a record whose LSN is between the archive tail and the base LSN. For more information about following record chains, see [Reading Data Records from a CLFS Stream](reading-data-records-from-a-clfs-stream.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20CLFS%20Support%20for%20Archiving%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


