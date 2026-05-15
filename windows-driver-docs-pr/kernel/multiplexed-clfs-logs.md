---
title: Multiplexed CLFS Logs
description: Multiplexed CLFS logs
keywords: ["Common Log File System WDK kernel , multiplexed logs", "CLFS WDK kernel , multiplexed logs", "multiplexed logs WDK CLFS", "stable storage WDK CLFS", "storage WDK CLFS"]
ms.date: 09/19/2025
ms.topic: concept-article
---

# Multiplexed CLFS logs

A *multiplexed log* serves as stable storage for several streams. A *dedicated log* serves as stable storage for a single stream. This article discusses multiplexed logs. For information about dedicated logs, see [Dedicated CLFS logs](dedicated-clfs-logs.md).

Each stream of a multiplexed log provides its clients with the illusion that their stream is the entire log. A client, in this context, is a driver, a thread, or some other unit of software that writes to and reads from a Common Log File System (CLFS) log. It's possible for a single stream to have several clients. Each client would have its own [**LOG_FILE_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_object) structure, which represents an open instance of the stream.

Consider the case of a multiplexed log that has two streams, each of which has one client. You can use the following procedure to create the log, the streams, and the client marshalling areas.

1. On behalf of client 1, call [**ClfsCreateLogFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatelogfile) to obtain a pointer to a **LOG_FILE_OBJECT** structure. Set the *puszLogFileName* parameter to a string of the form "log:&lt;log name&gt;::&lt;stream name&gt;" where &lt;log name&gt; is a valid path on the underlying file system, and &lt;stream name&gt; is the name that you chose to give to the stream used by client 1. For example, you could set *puszLogFileName* to "log:c:\\ClfsLogs\\myLog::Stream1". In that case, CLFS would create the base log file myLog.blf in the c:\\ClfsLogs directory, and Stream1 would be the name of the stream used by client 1.

    It's the form of the string passed in *puszLogFileName* that determines whether CLFS creates a dedicated or multiplexed log. If the string has a double colon (::) after the path name, then CLFS creates a multiplexed log.

1. On behalf of client 2, call [**ClfsCreateLogFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatelogfile) to obtain a pointer to a **LOG_FILE_OBJECT** structure. Set the *puszLogFileName* parameter to a string of the form "log:&lt;log name&gt;::&lt;stream name&gt;" where &lt;log name&gt; is the same path name you used for client 1, and &lt;stream name&gt; is the name that you chose to give to the stream used by client 2. For example, you could set *puszLogFileName* to "log:c:\\ClfsLogs\\myLog::Stream2".

1. Pass one of the **LOG_FILE_OBJECT** pointers you obtained from **ClfsCreateLogFile** to [**ClfsAddLogContainer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsaddlogcontainer) to create a container (contiguous physical extent) on stable storage that holds log records. Specify the size of the container (that will be rounded up to a multiple of 1 megabyte) by setting the *pcbContainer* parameter. Set the *puszContainerPath* parameter to specify a path name for the container. The path name can be absolute or relative to the directory that contains the base log file.

    You can create additional containers for your log by calling **ClfsAddLogContainer** again. All containers for a given log must be the same size. As an alternative to calling **ClfsAddLogContainer** several times, you can call [**ClfsAddLogContainerSet**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsaddlogcontainerset) to create several containers simultaneously. Your set of containers serve as stable storage for log records written by both client 1 and client 2.

1. Pass the **LOG_FILE_OBJECT** pointer you obtained on behalf of client 1 to [**ClfsCreateMarshallingArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatemarshallingarea) to obtain a pointer to a marshalling area that client 1 can use to read and write log records. Specify the size of the log I/O blocks that the marshalling area uses by setting the *cbMarshallingBuffer* parameter. There are several other parameters you can use to set various properties of the marshalling area.

    If client 1 needs additional marshalling areas, pass the same **LOG_FILE_OBJECT** pointer to **ClfsCreateMarshallingArea** again, once for each additional marshalling area that client 1 needs.

1. Pass the **LOG_FILE_OBJECT** pointer you obtained on behalf of client 2 to **ClfsCreateMarshallingArea** to obtain a marshalling area that client 2 can use to read and write log records. Specify the size of the log I/O blocks that the marshalling area uses by setting the *cbMarshallingBuffer* parameter. There are several other parameters you can use to set various properties of the marshalling area.

    If client 2 needs additional marshalling areas, pass the same **LOG_FILE_OBJECT** pointer to **ClfsCreateMarshallingArea** again, once for each additional marshalling area that client 2 needs.

Now that clients 1 and 2 each have a **LOG_FILE_OBJECT** and one or more marshalling areas, they can each write records to their own streams (by way of the marshalling areas associated with those streams) by calling the following functions.

[**ClfsReserveAndAppendLog**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreserveandappendlog)

[**ClfsReserveAndAppendLogAligned**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreserveandappendlogaligned)

[**ClfsWriteRestartArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfswriterestartarea)

All log records written by clients 1 and 2 go to the same log; that is, to the same set of physical containers on stable storage. CLFS multiplexes the log records written by the two clients and keeps track of which records belong to each stream.

As client 1 writes records to its stream, it gets back an increasing sequence of log sequence numbers (LSNs) that identify those records. Similarly, client 2 gets its own sequence of LSNs. The LSNs that belong to a particular stream can be compared to determine the order in which the corresponding records were written. However, an LSN that belongs to one stream can't be compared to an LSN that belongs to another stream.

CLFS maintains a base LSN and a last LSN for every stream, including streams that share a multiplexed log. Each stream has an active portion that begins with the record pointed to by the base LSN and ends with the record pointed to by the last LSN. A container in a multiplexed log on stable storage can't be recycled until the base LSNs of all the log's streams advance beyond any records stored in that container.

## See also

[**ClfsAddLogContainer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsaddlogcontainer)

[**ClfsAddLogContainerSet**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsaddlogcontainerset)

[**ClfsCreateLogFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatelogfile)

[**ClfsCreateMarshallingArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatemarshallingarea)

[**ClfsReserveAndAppendLog**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreserveandappendlog)

[**ClfsReserveAndAppendLogAligned**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreserveandappendlogaligned)

[**ClfsWriteRestartArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfswriterestartarea)

[Dedicated CLFS logs](dedicated-clfs-logs.md)

[**LOG_FILE_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_object)
