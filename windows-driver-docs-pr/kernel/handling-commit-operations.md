---
title: Handling Commit Operations
description: Handling Commit Operations
ms.assetid: 4885476e-ce68-4674-b8a5-8a317f33cd5b
keywords: ["transactions WDK KTM , committing transactions", "committing transactions WDK KTM", "resource managers WDK KTM , committing transactions", "single-phase commit WDK KTM , multi-phase commit WDK KTM", "pre-prepare phase WDK KTM", "prepare phase WDK KTM", "commit phase WDK KTM"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling Commit Operations


There are two types of commit operations: *single-phase commit* and *multi-phase commit*. A single-phase commit operation consists of a single notification that resource managers must respond to, while a multi-phase commit operation includes additional notifications for preparation steps.

A single-phase commit operation is simpler to implement. It is appropriate for transaction processing systems (TPSs) that have one of the following characteristics:

-   A single resource manager.

-   Multiple resource managers, all but one of which are [read-only](creating-a-resource-manager.md#kernel-creating-a-read-only-enlistment) and do not participate in the commit operation.

A multi-phase commit operation is necessary if multiple resource managers participate in the commit operation.

### Single-Phase Commit Operations

If you want your TPS to support single-phase commit operations, one (and only one) resource manager must register to receive TRANSACTION\_NOTIFY\_SINGLE\_PHASE\_COMMIT [notifications](transaction-notifications.md) for its enlistments. All other resource managers must be [read-only](creating-a-resource-manager.md#kernel-creating-a-read-only-enlistment).

A TPS that includes a [superior transaction manager](creating-a-superior-transaction-manager.md) cannot use single-phase commit.

If a resource manager has registered to receive TRANSACTION\_NOTIFY\_SINGLE\_PHASE\_COMMIT notifications, KTM sends this kind of notification when a transactional client calls [**ZwCommitTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566420).

When the resource manager receives a TRANSACTION\_NOTIFY\_SINGLE\_PHASE\_COMMIT notification for a transaction, it can either commit the transaction or reject single-phase commit.

To commit the transaction, the resource manager must do the following:

1.  Flush any data that it is holding in a non-permanent cache (in-memory storage), such as the [CLFS marshalling area](clfs-marshalling-areas.md) for a [CLFS log stream](using-log-streams-with-ktm.md).

    The resource manager must move the data from the cache to a durable storage medium. For example, a resource manager that is using CLFS can call [**ClfsFlushBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff541544).

2.  Make all data changes permanent and public (that is, visible outside the resource manager's scope).

3.  Call [**ZwCommitComplete**](https://msdn.microsoft.com/library/windows/hardware/ff566418).

After calling **ZwCommitComplete**, the resource manager should call [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417) to close the enlistment handle.

To reject a single-phase commit operation for the transaction, the resource manager can call [**ZwSinglePhaseReject**](https://msdn.microsoft.com/library/windows/hardware/ff567113). If the resource manager calls **ZwSinglePhaseReject**, KTM immediately changes the commit operation from single-phase to multi-phase.

If other resource managers enlist in the same transaction, they must be [read-only](creating-a-resource-manager.md#kernel-creating-a-read-only-enlistment). However, they must register to receive the TRANSACTION\_NOTIFY\_RM\_DISCONNECTED notification, which they receive if the resource manager that is handling the single-phase commit operation closes the enlistment handle without indicating that it has committed or rolled back the transaction.

### Multi-Phase Commit Operations

A multi-phase commit operation begins when one of the following events happens:

-   A transactional client calls [**ZwCommitTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566420), and no resource managers have registered to receive TRANSACTION\_NOTIFY\_SINGLE\_PHASE\_COMMIT notifications.

-   A resource manager calls [**ZwSinglePhaseReject**](https://msdn.microsoft.com/library/windows/hardware/ff567113) after it has received a TRANSACTION\_NOTIFY\_SINGLE\_PHASE\_COMMIT notification.

-   A [superior transaction manager](creating-a-superior-transaction-manager.md) calls [**ZwPrePrepareEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567044).

Multi-phase commit operations consist of three sequential phases: *pre-prepare*, *prepare*, and *commit*.

**Pre-Prepare Phase**

The pre-prepare phase (also known as *phase zero*) of the commit operation begins when KTM sends a TRANSACTION\_NOTIFY\_PREPREPARE notification to all resource managers. KTM sends this notification if no resource managers support a single-phase commit operation for the transaction, or if a superior transaction manager calls [**ZwPrePrepareEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567044).

When each resource manager receives the TRANSACTION\_NOTIFY\_PREPREPARE notification, it must do the following:

1.  Flush any data that it is holding in a non-permanent cache (in-memory storage), such as the [CLFS marshalling area](clfs-marshalling-areas.md) for a [CLFS log stream](using-log-streams-with-ktm.md).

    The resource manager must move the data from the cache to a durable storage medium. For example, a resource manager that is using CLFS can call [**ClfsFlushBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff541544).

2.  Call [**ZwPrePrepareComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567040).

After a resource manager has called **ZwPreprepareComplete**, it can continue to receive and service client requests. But the resource manager must treat all data modifications as cache pass-through operations that are immediately written to a durable storage medium.

If a resource manager encounters an error while it is processing a TRANSACTION\_NOTIFY\_PREPREPARE notification, it should call [**ZwRollbackEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567083) to roll back the transaction.

**Prepare Phase**

The prepare phase (also known as *phase one*) of the commit operation begins when KTM sends a TRANSACTION\_NOTIFY\_PREPARE notification to all resource managers. KTM sends this notification after TRANSACTION\_NOTIFY\_PREPREPARE if no resource managers support single-phase commit or if a superior transaction manager calls [**ZwPrepareEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567039).

When each resource manager receives the TRANSACTION\_NOTIFY\_PREPARE notification, it must do the following:

1.  Stop servicing client requests and report any client subsequent requests as client errors.

2.  Make sure that all data has been moved to durable storage.

3.  Call [**ZwPrepareComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567037).

If a resource manager encounters an error while it is processing a TRANSACTION\_NOTIFY\_PREPARE notification, it should call [**ZwRollbackEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567083) to roll back the transaction. However, the resource manager cannot roll back the transaction after it has called **ZwPrepareComplete**.

**Commit Phase**

The commit phase (also known as *phase two*) of the commit operation begins when KTM sends a TRANSACTION\_NOTIFY\_COMMIT notification to all resource managers. KTM sends this notification after TRANSACTION\_NOTIFY\_PREPARE if no resource managers support single-phase commit or if a superior transaction manager calls [**ZwCommitEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff566419).

When each resource manager receives the TRANSACTION\_NOTIFY\_COMMIT notification, it must do the following:

1.  Make all data changes permanent and public (that is, visible to other transactions).

    Typically, a resource manager makes changes permanent and public by copying the transaction's saved data from the log stream to the database's public, permanent storage. For more information about how to use log streams, see [Using Log Streams with KTM](using-log-streams-with-ktm.md).

2.  Call [**ZwCommitComplete**](https://msdn.microsoft.com/library/windows/hardware/ff566418).

After the resource manager calls **ZwCommitComplete**, it should call [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417) to close the enlistment handle.

If a resource manager encounters an error while it is processing a TRANSACTION\_NOTIFY\_COMMIT notification, it should shut itself down. The next time that the operating system reloads the resource manager, the resource manager's [recovery process](handling-recovery-operations.md) should restore the transaction to a state that was known to be good before the error occurred.

 

 




