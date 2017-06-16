---
title: Multiplexed CLFS Logs
author: windows-driver-content
description: Multiplexed CLFS Logs
ms.assetid: bbea9bdc-8bb8-4455-89c4-4735bad85ba0
keywords: ["Common Log File System WDK kernel , multiplexed logs", "CLFS WDK kernel , multiplexed logs", "multiplexed logs WDK CLFS", "stable storage WDK CLFS", "storage WDK CLFS"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Multiplexed CLFS Logs


## <a href="" id="ddk-introduction-to-wmi-kg"></a>


A *multiplexed log* serves as stable storage for several streams. A *dedicated log* serves as stable storage for a single stream. This topic discusses multiplexed logs. For information about dedicated logs, see [Dedicated CLFS Logs](dedicated-clfs-logs.md).

Each stream of a multiplexed log provides its clients with the illusion that their stream is the entire log. A client, in this context, is a driver, a thread, or some other unit of software that writes to and reads from a Common Log File System (CLFS) log. It is possible for a single stream to have several clients. Each client would have its own [**LOG\_FILE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff554316) structure, which represents an open instance of the stream.

Consider the case of a multiplexed log that has two streams, each of which has one client. You can use the following procedure to create the log, the streams, and the client marshalling areas.

1.  On behalf of client 1, call [**ClfsCreateLogFile**](https://msdn.microsoft.com/library/windows/hardware/ff540792) to obtain a pointer to a **LOG\_FILE\_OBJECT** structure. Set the *puszLogFileName* parameter to a string of the form "log:&lt;log name&gt;::&lt;stream name&gt;" where &lt;log name&gt; is a valid path on the underlying file system, and &lt;stream name&gt; is the name that you have chosen to give to the stream that will be used by client 1. For example, you could set *puszLogFileName* to "log:c:\\ClfsLogs\\myLog::Stream1". In that case, CLFS would create the base log file myLog.blf in the c:\\ClfsLogs directory, and Stream1 would be the name of the stream used by client 1.

    **Note**  It is the form of the string passed in *puszLogFileName* that determines whether CLFS creates a dedicated or multiplexed log. If the string has a double colon (::) after the path name, then CLFS creates a multiplexed log.

     

2.  On behalf of client 2, call [**ClfsCreateLogFile**](https://msdn.microsoft.com/library/windows/hardware/ff540792) to obtain a pointer to a **LOG\_FILE\_OBJECT** structure. Set the *puszLogFileName* parameter to a string of the form "log:&lt;log name&gt;::&lt;stream name&gt;" where &lt;log name&gt; is the same path name you used for client 1, and &lt;stream name&gt; is the name that you have chosen to give to the stream that will be used by client 2. For example, you could set *puszLogFileName* to "log:c:\\ClfsLogs\\myLog::Stream2".

3.  Pass one of the **LOG\_FILE\_OBJECT** pointers you obtained from **ClfsCreateLogFile** to [**ClfsAddLogContainer**](https://msdn.microsoft.com/library/windows/hardware/ff540768) to create a container (contiguous physical extent) on stable storage that will hold log records. Specify the size of the container (which will be rounded up to a multiple of 1 megabyte) by setting the *pcbContainer* parameter. Set the *puszContainerPath* parameter to specify a path name for the container. The path name can be absolute or relative to the directory that contains the base log file.

    You can create additional containers for your log by calling **ClfsAddLogContainer** again. Note that all containers for a given log must be the same size. As an alternative to calling **ClfsAddLogContainer** several times, you can call [**ClfsAddLogContainerSet**](https://msdn.microsoft.com/library/windows/hardware/ff540770) to create several containers simultaneously. Note that your set of containers will serve as stable storage for log records written by both client 1 and client 2.

4.  Pass the **LOG\_FILE\_OBJECT** pointer you obtained on behalf of client 1 to [**ClfsCreateMarshallingArea**](https://msdn.microsoft.com/library/windows/hardware/ff541520) to obtain a pointer to a marshalling area that client 1 can use to read and write log records. Specify the size of the log I/O blocks that the marshalling area will use by setting the *cbMarshallingBuffer* parameter. There are several other parameters you can use to set various properties of the marshalling area.

    If client 1 needs additional marshalling areas, pass the same **LOG\_FILE\_OBJECT** pointer to **ClfsCreateMarshallingArea** again, once for each additional marshalling area that client 1 needs.

5.  Pass the **LOG\_FILE\_OBJECT** pointer you obtained on behalf of client 2 to **ClfsCreateMarshallingArea** to obtain a marshalling area that client 2 can use to read and write log records. Specify the size of the log I/O blocks that the marshalling area will use by setting the *cbMarshallingBuffer* parameter.

    **Note**  There are several other parameters you can use to set various properties of the marshalling area.

     

    If client 2 needs additional marshalling areas, pass the same **LOG\_FILE\_OBJECT** pointer to **ClfsCreateMarshallingArea** again, once for each additional marshalling area that client 2 needs.

Now that clients 1 and 2 each have a **LOG\_FILE\_OBJECT** and one or more marshalling areas, they can each write records to their own streams (by way of the marshalling areas associated with those streams) by calling the following functions.

[**ClfsReserveAndAppendLog**](https://msdn.microsoft.com/library/windows/hardware/ff541723)

[**ClfsReserveAndAppendLogAligned**](https://msdn.microsoft.com/library/windows/hardware/ff541726)

[**ClfsWriteRestartArea**](https://msdn.microsoft.com/library/windows/hardware/ff541770)

All log records written by clients 1 and 2 go to the same log; that is, to the same set of physical containers on stable storage. CLFS multiplexes the log records written by the two clients and keeps track of which records belong to each stream.

As client 1 writes records to its stream, it gets back an increasing sequence of log sequence numbers (LSNs) that identify those records. Similarly, client 2 gets its own sequence of LSNs. The LSNs that belong to a particular stream can be compared to determine the order in which the corresponding records were written. However, an LSN that belongs to one stream cannot be compared to an LSN that belongs to another stream.

CLFS maintains a base LSN and a last LSN for every stream, including streams that share a multiplexed log. Each stream has an active portion that begins with the record pointed to by the base LSN and ends with the record pointed to by the last LSN. Note that a container in a multiplexed log on stable storage cannot be recycled until the base LSNs of all the log's streams have advanced beyond any records stored in that container.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Multiplexed%20CLFS%20Logs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


