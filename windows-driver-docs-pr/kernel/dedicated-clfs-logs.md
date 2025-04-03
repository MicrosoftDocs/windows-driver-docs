---
title: Dedicated CLFS Logs
description: Dedicated CLFS logs
keywords: ["Common Log File System WDK kernel , dedicated logs", "CLFS WDK kernel , dedicated logs", "dedicated logs WDK CLFS", "stable storage WDK CLFS", "storage WDK CLFS"]
ms.date: 04/03/2025
---

# Dedicated CLFS logs

A Common Log File System (CLFS) log can be either dedicated or multiplexed. A *dedicated log* serves as stable storage for a single stream. A *multiplexed log* serves as stable storage for several streams. This article discusses dedicated logs. For information about multiplexed logs, see [Multiplexed CLFS Logs](multiplexed-clfs-logs.md).

To create a dedicated log, perform the following steps.

1. Call [**ClfsCreateLogFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatelogfile) to obtain a pointer to a [**LOG_FILE_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_object) structure. Set the *puszLogFileName* parameter to a string of the form "log:*&lt;log name&gt;*" where *&lt;log name&gt;* is a valid path on the underlying file system. For example, if you set *puszLogFileName* to "log:c:\\ClfsLogs\\myLog", the base log file myLog.blf would be created in the c:\\ClfsLogs directory. The c:\\ClfsLogs directory would also serve as the default location for containers that you add to the log later.

   It's the form of the string passed in *puszLogFileName* that determines whether CLFS creates a dedicated or multiplexed log. If the string has a double colon (::) after the log name, then CLFS creates a multiplexed log. In the example given here, "log:c\\ClfsLogs\\myLog" has no double colon, so CLFS creates a dedicated log.

   The **LOG_FILE_OBJECT** pointer returned by **ClfsCreateLogFile** represents an open instance of the dedicated log's one and only stream.

1. Pass the **LOG_FILE_OBJECT** pointer you obtained from **ClfsCreateLogFile** to [**ClfsAddLogContainer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsaddlogcontainer) to create a container (contiguous physical extent) on stable storage holds log records. Specify the size of the container (which will be rounded up to a multiple of 512 kilobytes) by setting the *pcbContainer* parameter. Set the *puszContainerPath* parameter to specify a path name for the container. The path name can be absolute or relative to the directory that contains the base log file.

   You can create more containers for your log by calling **ClfsAddLogContainer** again. All containers for a given log must be the same size. As an alternative to calling **ClfsAddLogContainer** several times, you can call [**ClfsAddLogContainerSet**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsaddlogcontainerset) to create several containers simultaneously.

1. Pass the **LOG_FILE_OBJECT** pointer you obtained from **ClfsCreateLogFile** to [**ClfsCreateMarshallingArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatemarshallingarea) to obtain a pointer to a marshalling area that you can use to read and write log records to your stream. Specify the size of the log I/O blocks that the marshalling area uses by setting the *cbMarshallingBuffer* parameter. There are several other parameters you can use to set various properties of the marshalling area.

If you need more marshalling areas, pass the same **LOG_FILE_OBJECT** pointer to **ClfsCreateMarshallingArea** again, once for each extra marshalling area that you need.

Now that you have one or more marshalling areas associated with your stream, you can write records to those marshalling areas by calling the following functions.

[**ClfsReserveAndAppendLog**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreserveandappendlog)

[**ClfsReserveAndAppendLogAligned**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreserveandappendlogaligned)

[**ClfsWriteRestartArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfswriterestartarea)

Each time you write a record, you get back a log sequence number (LSN) that identifies the record. The LSN assigned to a record is always greater than the LSN assigned to the previously written record, regardless of which marshalling area was used to write the record.

## See also

[**ClfsAddLogContainer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsaddlogcontainer)

[**ClfsAddLogContainerSet**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsaddlogcontainerset)

[**ClfsCreateLogFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatelogfile)

[**ClfsCreateMarshallingArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatemarshallingarea)

[**ClfsReserveAndAppendLog**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreserveandappendlog)

[**ClfsReserveAndAppendLogAligned**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreserveandappendlogaligned)

[**ClfsWriteRestartArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfswriterestartarea)

[**LOG_FILE_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_object)

[Multiplexed CLFS Logs](multiplexed-clfs-logs.md)
