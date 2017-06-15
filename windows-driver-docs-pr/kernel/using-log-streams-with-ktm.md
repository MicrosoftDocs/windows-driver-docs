---
title: Using Log Streams with KTM
author: windows-driver-content
description: Using Log Streams with KTM
MS-HAID:
- 'ktm\_dg\_7eec4c22-7af0-493e-b86d-074655d59c5d.xml'
- 'kernel.using\_log\_streams\_with\_ktm'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d7ad0e16-d1f2-4c41-b647-95b5445c2708
keywords: ["log streams WDK KTM", "Kernel Transaction Manager WDK , log streams", "KTM WDK , log streams", "Common Log File System WDK kernel , KTM log streams", "CLFS WDK kernel , KTM log streams", "transaction managers WDK KTM , log streams", "resource managers WDK KTM , log streams"]
---

# Using Log Streams with KTM


KTM-based transaction processing systems (TPSs) should log transaction activity by using the [Common Log File System](using-common-log-file-system.md) (CLFS). KTM creates a log stream for each transaction manager object. Each resource manager should create its own log stream.

### Creating Log Streams for Transaction Manager Objects

When your resource manager calls [**ZwCreateTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff566430), you must specify the name of a CLFS log stream. If the specified stream does not exist, KTM creates it. If the stream already exists, **ZwCreateTransactionManager** reopens it. KTM assigns this log stream to the transaction manager object.

KTM uses the transaction manager object's log stream to record internal state information about the transaction manager object and all resource manager objects, transaction objects, and enlistment objects that are associated with the transaction manager object. If transactional operations are interrupted before they are complete, KTM can use the information in the log to determine whether to commit or roll back the transactions.

KTM does not record the transaction data that resource managers receive from or send to clients. Resource managers must use their own log streams to record this information.

Resource managers can call [**ZwQueryInformationTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff567058) to obtain information about a transaction manager object's log stream, such as the log stream's path name or the GUID that KTM assigns to the stream.

### Creating Log Streams for Resource Managers

In its initialization code, each resource manager should call [**ClfsCreateLogFile**](https://msdn.microsoft.com/library/windows/hardware/ff540792) to create its own log stream. Each resource manager should use its stream to record all the information about transactions that it requires to commit, roll back, or recover the transaction's data.

KTM and all resource managers of a TPS can use a single log file, but each TPS component must use a different stream within the log file. For information about how to specify individual streams within a log file, see [**ClfsCreateLogFile**](https://msdn.microsoft.com/library/windows/hardware/ff540792).

Periodically, KTM creates a [restart area](reading-restart-records-from-a-clfs-stream.md) in the transaction manager's log stream. When KTM performs a recovery operation, it reads the last restart area to recover the state of objects that were open before the system shut down. Similarly, your resource manager should periodically create restart areas in its log stream. For example, your resource manager might create a restart area every time that a transactional operation is completed.

For more information about restart areas in CLFS log streams, see [Reading Restart Records from a CLFS Stream](reading-restart-records-from-a-clfs-stream.md). Also, see the [**ClfsWriteRestartArea**](https://msdn.microsoft.com/library/windows/hardware/ff541770), [**ClfsReadRestartArea**](https://msdn.microsoft.com/library/windows/hardware/ff541709), and [**ClfsReadPreviousRestartArea**](https://msdn.microsoft.com/library/windows/hardware/ff541699) routines.

### Using Log Streams for Recovery

After your resource manager calls **ZwCreateTransactionManager**, it must call [**ZwRecoverTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff567079). The **ZwRecoverTransactionManager** routine reads the transaction manager object's log stream to recover the state of the TPS to a known good point. If the computer shut down properly—or did not shut down—after the resource manager was last loaded, the log stream contains minimal information. If a system crash has occurred, the log stream contains enough recovery information to restore all the transactions to a known state.

After your resource manager calls [**ZwCreateResourceManager**](https://msdn.microsoft.com/library/windows/hardware/ff566427), it must call [**ZwRecoverResourceManager**](https://msdn.microsoft.com/library/windows/hardware/ff567078). The **ZwRecoverResourceManager** routine tries to recover the transactions that are associated with each of the resource manager's enlistments. For more information about how to recover a resource manager's transactions, see [Handling Recovery Operations](handling-recovery-operations.md).

### Storing Transaction Data

Resource managers that use CLFS log streams should store transaction data in [CLFS marshalling areas](clfs-marshalling-areas.md). CLFS periodically moves the data from the log stream's marshalling area to a permanent storage medium. To log an operation that modifies data, a resource manager might do the following:

1.  Copy the original data, before the write operation modifies it, to the marshalling area.

2.  Perform the operation on a copy of the data without modifying the database's permanent storage medium.

3.  Copy the new data to the marshalling area.

If the resource manager receives a rollback notification, it can restore the original data from the log stream. If it receives a commit notification, the resource manager can copy the modified data from the log stream to the database's permanent storage medium.

Resource managers can also use the [**ZwSetInformationEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567094) routine to store recovery information in an enlistment object. KTM saves this information in its log stream and reads it from the log stream during recovery operations. Therefore, a resource manager can obtain this recovery information at any time by calling [**ZwQueryInformationEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567051).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20Log%20Streams%20with%20KTM%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


