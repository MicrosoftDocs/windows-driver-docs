---
title: Transaction Notifications
description: Transaction Notifications
ms.assetid: 62169b56-e70f-4d32-a051-a7fd947dbc64
keywords: ["notifications WDK KTM", "transactions WDK KTM , notifications", "resource managers WDK KTM , notifications", "Kernel Transaction Manager WDK , notifications", "KTM WDK , notifications", "superior transaction managers WDK KTM"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Transaction Notifications


KTM provides a notification queue for each resource manager. KTM delivers notifications to a resource manager by putting them in the resource manager's queue.

A resource manager can retrieve notifications from its queue either synchronously or asynchronously.

-   To retrieve notifications synchronously, the resource manager can repeatedly call [**ZwGetNotificationResourceManager**](https://msdn.microsoft.com/library/windows/hardware/ff566467).

-   To receive notifications asynchronously, the resource manager can call [**TmEnableCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff564676) to set up a callback routine. KTM calls the callback routine every time that it puts a notification in the resource manager's queue.

When a resource manager calls [**ZwCreateEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff566422) to create an enlistment for a transaction, the resource manager specifies the types of notifications that it should receive. Resource managers receive only notifications that they register to receive.

The notification constants are defined in Ktmtypes.h. Notification constant names have a format of TRANSACTION\_NOTIFY\_*Xxx*.

The rest of this topic lists all the notification constants that Ktmtypes.h defines and divides them into three groups:

-   Notifications that resource managers can receive

-   Notifications that superior transaction managers can receive

-   Notification constants that are defined but currently not used

### <a href="" id="notifications-for-resource-managers"></a> Notifications for Resource Managers

All resource managers must register to receive TRANSACTION\_NOTIFY\_PREPREPARE, TRANSACTION\_NOTIFY\_PREPARE, and TRANSACTION\_NOTIFY\_COMMIT notifications, even if they subsequently call [**ZwReadOnlyEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567074) to mark an enlistment as read-only.

Resource managers can support TRANSACTION\_NOTIFY\_SINGLE\_PHASE\_COMMIT, but they must also support the multi-phase pre-prepare, prepare, and commit notifications.

The following list contains all the notifications that resource managers can receive:

<a href="" id="transaction-notify-preprepare"></a>TRANSACTION\_NOTIFY\_PREPREPARE  
**When sent**: A client calls [**ZwCommitTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566420) and no resource manager supports single-phase commit, or if a [superior transaction manager](creating-a-superior-transaction-manager.md) calls [**ZwPrePrepareEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567044).

**Received by**: Resource managers.

**Recipient's required action**: Perform pre-prepare operations and then call [**ZwPrePrepareComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567040). (For more information about pre-prepare operations, see [Handling Commit Operations](handling-commit-operations.md).)

**Restrictions:** The resource manager must also support TRANSACTION\_NOTIFY\_PREPARE and TRANSACTION\_NOTIFY\_COMMIT.

<a href="" id="transaction-notify-prepare"></a>TRANSACTION\_NOTIFY\_PREPARE  
**When sent**: After TRANSACTION\_NOTIFY\_PREPREPARE if a client calls [**ZwCommitTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566420) and no resource manager supports single-phase commit, or if a superior transaction manager calls [**ZwPrepareEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567039).

**Received by**: Resource managers.

**Recipient's required action:** Perform prepare operations and then call [**ZwPrepareComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567037). (For more information about prepare operations, see [Handling Commit Operations](handling-commit-operations.md).)

**Restrictions:** The resource manager must also support TRANSACTION\_NOTIFY\_PREPREPARE and TRANSACTION\_NOTIFY\_COMMIT.

<a href="" id="transaction-notify-commit"></a>TRANSACTION\_NOTIFY\_COMMIT  
**When sent**: After TRANSACTION\_NOTIFY\_PREPARE if a client calls [**ZwCommitTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566420) and no resource manager supports single-phase commit, or if a superior transaction manager calls [**ZwCommitEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff566419).

**Received by**: Resource managers.

**Recipient's required action**: Perform commit operations and then call [**ZwCommitComplete**](https://msdn.microsoft.com/library/windows/hardware/ff566418). (For more information about commit operations, see [Handling Commit Operations](handling-commit-operations.md).)

**Restrictions:** The resource manager must also support TRANSACTION\_NOTIFY\_PREPREPARE and TRANSACTION\_NOTIFY\_PREPARE.

<a href="" id="transaction-notify-single-phase-commit"></a>TRANSACTION\_NOTIFY\_SINGLE\_PHASE\_COMMIT  
**When sent**: A client calls [**ZwCommitTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566420) and a resource manager supports single-phase commit operations.

**Received by**: Resource managers.

**Recipient's required action**: Either commit the transaction or call [**ZwSinglePhaseReject**](https://msdn.microsoft.com/library/windows/hardware/ff567113). (For more information about single-phase commit operations, see [Handling Commit Operations](handling-commit-operations.md).)

**Restrictions:** The resource manager must also support TRANSACTION\_NOTIFY\_PREPREPARE, TRANSACTION\_NOTIFY\_PREPARE, and TRANSACTION\_NOTIFY\_COMMIT.

<a href="" id="transaction-notify-rollback"></a>TRANSACTION\_NOTIFY\_ROLLBACK  
**When sent**: A client calls [**ZwRollbackTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567086), a superior transaction manager calls [**ZwRollbackEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567083), or KTM detects an error (such as a failed write to the log stream).

**Received by**: Both resource managers and superior transaction managers.

**Recipient's required action**: Perform any operations that are needed to roll back the transaction's data, and then call [**ZwRollbackComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567081). (For more information about rollback operations, see [Handling Rollback Operations](handling-rollback-operations.md).)

**Restrictions:** All resource managers and superior transaction managers must support TRANSACTION\_NOTIFY\_ROLLBACK.

<a href="" id="transaction-notify-recover"></a>TRANSACTION\_NOTIFY\_RECOVER  
**When sent**: A resource manager calls [**ZwRecoverResourceManager**](https://msdn.microsoft.com/library/windows/hardware/ff567078).

**Received by**: Resource managers.

**Recipient's required action**: The resource manager must call [**ZwRecoverEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567075). (For more information about recovery operations, see [Handling Recovery Operations](handling-recovery-operations.md).)

**Restrictions:** None.

<a href="" id="transaction-notify-last-recover"></a>TRANSACTION\_NOTIFY\_LAST\_RECOVER  
**When sent**: After KTM has sent the last TRANSACTION\_NOTIFY\_RECOVER for a resource manager's enlistments.

**Received by**: Resource managers.

**Recipient's required action**: End the recovery operation. (For more information about recovery operations, see [Handling Recovery Operations](handling-recovery-operations.md).)

**Restrictions:** None.

<a href="" id="transaction-notify-indoubt"></a>TRANSACTION\_NOTIFY\_INDOUBT  
**When sent**: After a resource manager calls [**ZwRecoverEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567075), if KTM cannot determine whether the transaction should be committed or rolled back (typically because the TPS has a superior transaction manager that is unavailable).

Received by: Resource managers.

**Recipient's required action**: Do nothing until KTM sends TRANSACTION\_NOTIFY\_COMMIT or TRANSACTION\_NOTIFY\_ROLLBACK.

**Restrictions:** None.

<a href="" id="transaction-notify-rm-disconnected"></a>TRANSACTION\_NOTIFY\_RM\_DISCONNECTED  
**When sent**: The resource manager that is handling a single-phase commit operation closes the enlistment handle without indicating that it has committed or rolled back the transaction.

**Received by**: Resource managers and superior transaction managers that have enlistments for the transaction.

**Recipient's required action**: Transaction-specific cleanup operations. Typically, this notification is useful to read-only resource managers.

**Restrictions:** None.

### <a href="" id="notifications-for-superior-transaction-managers"></a> Notifications for Superior Transaction Managers

[Superior transaction managers](creating-a-superior-transaction-manager.md) can receive the following notifications:

<a href="" id="transaction-notify-rollback"></a>TRANSACTION\_NOTIFY\_ROLLBACK  
See earlier description.

<a href="" id="transaction-notify-rm-disconnected"></a>TRANSACTION\_NOTIFY\_RM\_DISCONNECTED  
See earlier description.

<a href="" id="transaction-notify-preprepare-complete"></a>TRANSACTION\_NOTIFY\_PREPREPARE\_COMPLETE  
**When sent**: After all resource managers have received TRANSACTION\_NOTIFY\_PREPREPARE and responded by calling [**ZwPrePrepareComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567040).

**Received by**: Superior transaction managers.

**Recipient's required action**: The superior transaction manager should call [**ZwPrepareEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567039).

<a href="" id="transaction-notify-prepare-complete"></a>TRANSACTION\_NOTIFY\_PREPARE\_COMPLETE  
**When sent**: After all resource managers have received TRANSACTION\_NOTIFY\_PREPARE and responded by calling [**ZwPrepareComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567037).

**Received by**: Superior transaction managers.

**Recipient's required action**: The superior transaction manager should call [**ZwCommitEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff566419).

<a href="" id="transaction-notify-commit-complete"></a>TRANSACTION\_NOTIFY\_COMMIT\_COMPLETE  
**When sent**: After all resource managers have received TRANSACTION\_NOTIFY\_COMMIT and responded by calling [**ZwCommitComplete**](https://msdn.microsoft.com/library/windows/hardware/ff566418).

**Received by**: Superior transaction managers.

**Recipient's required action**: Transaction cleanup operations.

<a href="" id="transaction-notify-rollback-complete"></a>TRANSACTION\_NOTIFY\_ROLLBACK\_COMPLETE  
**When sent**: After all resource managers have received TRANSACTION\_NOTIFY\_ROLLBACK and responded by calling [**ZwRollbackComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567081).

**Received by**: Superior transaction managers.

**Recipient's required action**: Transaction cleanup operations.

<a href="" id="transaction-notify-recover-query"></a>TRANSACTION\_NOTIFY\_RECOVER\_QUERY  
**When sent**: A superior transaction manager calls [**ZwRecoverResourceManager**](https://msdn.microsoft.com/library/windows/hardware/ff567078).

**Received by**: Superior transaction managers.

**Recipient's required action**: The superior transaction manager must call either [**ZwCommitEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff566419) or [**ZwRollbackEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567083) for the enlistment.

<a href="" id="transaction-notify-commit-request"></a>TRANSACTION\_NOTIFY\_COMMIT\_REQUEST  
**When sent**: A client calls [**ZwCommitTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566420). If a superior transaction manager has registered for this notification for an enlistment, KTM sends TRANSACTION\_NOTIFY\_COMMIT\_REQUEST to the superior transaction manager **instead of** sending TRANSACTION\_NOTIFY\_COMMIT to the resource managers.

**Received by**: Superior transaction managers.

**Recipient's required action**: The superior transaction manager calls [**ZwCommitEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff566419).

<a href="" id="transaction-notify-request-outcome"></a>TRANSACTION\_NOTIFY\_REQUEST\_OUTCOME  
**When sent**: A resource manager calls [**TmRequestOutcomeEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff564727) while the transaction is in its prepared state.

**Received by**: Superior transaction managers.

**Recipient's required action**: The superior transaction manager must call [**ZwCommitEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff566419) or [**ZwRollbackEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567083).

### <a href="" id="unused-notifications"></a> Unused Notifications

The following notifications are defined in Ktmtypes.h, but KTM currently does not support them:

TRANSACTION\_NOTIFY\_DELEGATE\_COMMIT

TRANSACTION\_NOTIFY\_ENLIST\_MASK

TRANSACTION\_NOTIFY\_ENLIST\_PREPREPARE

TRANSACTION\_NOTIFY\_MARSHAL

TRANSACTION\_NOTIFY\_PROMOTE

TRANSACTION\_NOTIFY\_PROMOTE\_NEW

TRANSACTION\_NOTIFY\_PROPAGATE\_PULL

TRANSACTION\_NOTIFY\_PROPAGATE\_PUSH

TRANSACTION\_NOTIFY\_TM\_ONLINE

TRANSACTION\_NOTIFY\_COMMIT\_FINALIZE

 

 




