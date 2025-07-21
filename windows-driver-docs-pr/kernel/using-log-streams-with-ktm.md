---
title: Using Log Streams with KTM
description: Using Log Streams with KTM
keywords: ["log streams WDK KTM", "Kernel Transaction Manager WDK , log streams", "KTM WDK , log streams", "Common Log File System WDK kernel , KTM log streams", "CLFS WDK kernel , KTM log streams", "transaction managers WDK KTM , log streams", "resource managers WDK KTM , log streams"]
ms.date: 07/18/2025
ms.topic: how-to
---

# Using Log Streams with the Kernel Transaction Manager (KTM)

KTM-based transaction processing systems (TPSs) should log transaction activity by using the [Common Log File System](introduction-to-the-common-log-file-system.md) (CLFS). KTM creates a log stream for each transaction manager object. Each resource manager should create its own log stream.

## Creating Log Streams for Transaction Manager Objects

When your resource manager calls [**ZwCreateTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreatetransactionmanager), you must specify the name of a CLFS log stream. If the specified stream doesn't exist, KTM creates it. If the stream already exists, **ZwCreateTransactionManager** reopens it. KTM assigns this log stream to the transaction manager object.

KTM uses the transaction manager object's log stream to record internal state information about the transaction manager object and the following objects associated with it:

- All associated resource manager objects
- All associated transaction objects
- All associated enlistment objects

If transactional operations are interrupted before they're complete, KTM can use the information in the log to determine whether to commit or roll back the transactions.

KTM doesn't record the transaction data that resource managers receive from or send to clients. Resource managers must use their own log streams to record this information.

Resource managers can call [**ZwQueryInformationTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationtransactionmanager) to get information about a transaction manager object's log stream, such as the log stream's path name or the GUID that KTM assigns to the stream.

## Creating Log Streams for Resource Managers

In its initialization code, each resource manager should call [**ClfsCreateLogFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatelogfile) to create its own log stream. Each resource manager should use its stream to record all the information about transactions that it requires to commit, roll back, or recover the transaction's data.

KTM and all resource managers of a TPS can use a single log file, but each TPS component must use a different stream within the log file. For information about how to specify individual streams within a log file, see [**ClfsCreateLogFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatelogfile).

Periodically, KTM creates a [restart area](reading-restart-records-from-a-clfs-stream.md) in the transaction manager's log stream. When KTM performs a recovery operation, it reads the last restart area to recover the state of objects that were open before the system shutdown. Similarly, your resource manager should periodically create restart areas in its log stream. For example, your resource manager might create a restart area every time that a transactional operation is completed.

For more information about restart areas in CLFS log streams, see [Reading Restart Records from a CLFS Stream](reading-restart-records-from-a-clfs-stream.md). Also, see the [**ClfsWriteRestartArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfswriterestartarea), [**ClfsReadRestartArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreadrestartarea), and [**ClfsReadPreviousRestartArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreadpreviousrestartarea) routines.

## Using Log Streams for Recovery

After your resource manager calls **ZwCreateTransactionManager**, it must call [**ZwRecoverTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrecovertransactionmanager). The **ZwRecoverTransactionManager** routine reads the transaction manager object's log stream to recover the state of the TPS to a known good point. If the computer shuts down properly (or doesn't shut down), the log stream contains minimal information after the resource manager was last loaded. If a system crash occurs, the log stream contains enough recovery information to restore all the transactions to a known state.

After your resource manager calls [**ZwCreateResourceManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreateresourcemanager), it must call [**ZwRecoverResourceManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrecoverresourcemanager). The **ZwRecoverResourceManager** routine tries to recover the transactions that are associated with each of the resource manager's enlistments. For more information about how to recover a resource manager's transactions, see [Handling Recovery Operations](handling-recovery-operations.md).

## Storing Transaction Data

Resource managers that use CLFS log streams should store transaction data in [CLFS marshaling areas](clfs-marshalling-areas.md). CLFS periodically moves the data from the log stream's marshaling area to a permanent storage medium. To log an operation that modifies data, a resource manager might take the following steps:

1. Copy the original data, before the write operation modifies it, to the marshaling area.

1. Perform the operation on a copy of the data without modifying the database's permanent storage medium.

1. Copy the new data to the marshaling area.

If the resource manager receives a rollback notification, it can restore the original data from the log stream. If it receives a commit notification, the resource manager can copy the modified data from the log stream to the database's permanent storage medium.

Resource managers can also use the [**ZwSetInformationEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntsetinformationenlistment) routine to store recovery information in an enlistment object. KTM saves this information in its log stream and reads it from the log stream during recovery operations. Therefore, a resource manager can obtain this recovery information at any time by calling [**ZwQueryInformationEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationenlistment).
