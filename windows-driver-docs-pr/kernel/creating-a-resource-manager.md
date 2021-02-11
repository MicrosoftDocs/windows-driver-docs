---
title: Creating a Resource Manager
description: Creating a Resource Manager
keywords: ["resource managers WDK KTM , creating resource managers", "enlistments WDK KTM , read-only enlistments", "read-only enlistments WDK KTM", "resource managers WDK KTM , volatile resource managers", "volatile resource managers WDK KTM", "resource managers WDK KTM , adding to a TPS", "transaction processing systems WDK KTM , adding resource managers", "TPS WDK KTM , adding resource managers"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Creating a Resource Manager


[*Resource managers*](transaction-processing-terms.md#ktm-term-resource-manager) maintain each transaction's data and log the transaction's operations. If a transaction processing system (TPS) has multiple resource managers, each resource manager can participate in each transaction's commit, rollback, and recovery operations.

Each resource manager must export an interface that transactional clients can use to access the database or other resource that the resource manager maintains.

Typically, a kernel-mode resource manager must perform the following tasks in the listed order:

1.  Create a log stream.

    Resource managers can use the [Common Log File System](introduction-to-the-common-log-file-system.md) (CLFS), or some other logging capability, to maintain their log streams. A call to [**ClfsCreateLogFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatelogfile) creates a CLFS log stream. The resource manager must use the log stream to record any information that it requires to commit, roll back, or recover transactions. In addition, KTM uses the log stream to record any internal state changes that might be necessary to recover transactions.

2.  Create a transaction manager object.

    A call to [**ZwCreateTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreatetransactionmanager) creates a transaction manager object and connects the resource manager to an additional CLFS log stream that the resource manager specifies.

3.  Recover the transaction manager state.

    A call to [**ZwRecoverTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrecovertransactionmanager) reads the transaction manager object's log stream (which KTM maintains) and determines whether the TPS was shut down before all transactions were completed (for example, because the system crashed). KTM restores its internal state based on information in the log stream.

4.  Create a resource manager object.

    A call to [**ZwCreateResourceManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreateresourcemanager) creates a resource manager object and associates it with the previously created transaction manager object.

5.  Recover the resource manager state.

    A call to [**ZwRecoverResourceManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrecoverresourcemanager) causes KTM to send the resource manager TRANSACTION\_NOTIFY\_RECOVER notifications for any transactions that were in progress the last time that the resource manager shut down. For information about how the resource manager should respond to these notifications, see [Handling Recovery Operations](handling-recovery-operations.md).

6.  Receive transactions from clients.

    Typically, a client creates a transaction object and uses the resource manager's client interface to pass the transaction object's GUID to the resource manager. For example, the resource manager might provide a *CreateDataObject* routine that is similar to the one that the [Understanding TPS Components](understanding-tps-components.md) topic describes.

7.  Enlist in each transaction.

    A call to [**ZwOpenTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopentransaction) opens a handle to the transaction object, and then a call to [**ZwCreateEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreateenlistment) creates an enlistment for the transaction. The enlistment enables the resource manager to receive a specified set of [transaction notifications](transaction-notifications.md).

8.  Enable reception of transaction notifications.

    The resource manager can call [**ZwGetNotificationResourceManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntgetnotificationresourcemanager) to obtain notifications synchronously, or it can call [**TmEnableCallbacks**](/windows-hardware/drivers/ddi/wdm/nf-wdm-tmenablecallbacks) to register a *ResourceManagerNotification* callback routine that KTM calls whenever a notification is available.

9.  Service resource access requests from clients, but do not make the changes permanent.

    After a client has created a transaction object, it typically calls the resource manager's interface to access the resource manager's resource. For example, a resource manager for a database might receive requests to read from and write to the database.

    The resource manager must record the results of the read and write operations in a [CLFS log stream](using-log-streams-with-ktm.md) or other logging capability until it receives a notification that the transaction's operations will be committed, rolled back, or recovered.

10. Commit or roll back client operations.

    Eventually, the resource manager receives a notification to begin committing or rolling back the operations that the client has performed. In response, the resource manager must either make the client operations permanent or discard them. For more information about how to handle commit and rollback notifications, see [Handling Transaction Operations](handling-transaction-operations.md).

    Occasionally, a resource manager might have to try to force KTM to quickly provide a commit or rollback notification, perhaps because the resource manager has determined that a device was surprise-removed. In such a case, the resource manager can call [**TmRequestOutcomeEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-tmrequestoutcomeenlistment).

11. Close the enlistment object handle.

    After the resource manager has finished processing the transaction, it must call [**ZwClose**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose) to close the enlistment object's handle

12. Close the resource manager object handle and the transaction manager object handle.

    Before the resource manager unloads, it must call [**ZwClose**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose) to close the resource manager object's handle and the transaction manager object's handle.

Steps 1 through 5 must be performed in your resource manager's initialization code. For example, if your resource manager is a kernel-mode driver, the initialization code is the driver's [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine.

Steps 6 through 11 are typically performed in code that responds to requests from transactional clients.

Step 12 must be performed in your resource manager's final clean-up code, such as a kernel-mode driver's [*Unload*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) routine.

## <a href="" id="kernel-creating-a-read-only-enlistment"></a> Creating a Read-Only Enlistment


A *read-only enlistment* is an enlistment that does not receive any notifications from KTM. A resource manager can make any enlistment read-only by calling [**ZwReadOnlyEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntreadonlyenlistment). This call causes KTM to stop delivering notifications to the resource manager.

After your resource manager has called [**ZwCreateEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreateenlistment), it can call **ZwReadOnlyEnlistment** at any time up to the point at which it would ordinarily call [**ZwPrepareComplete**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntpreparecomplete).

There are two reasons why you might want your resource manager to call **ZwReadOnlyEnlistment**.

-   Your resource manager has been participating in a transaction and, at some point before it receives a TRANSACTION\_NOTIFY\_COMMIT notification, the resource manager determines that it no longer has to participate in the transaction's commit operation.

    For example, when the resource manager receives a TRANSACTION\_NOTIFY\_PREPARE notification, it might determine that none of the transaction's operations have changed the resource manager's database. The resource manager can call **ZwReadOnlyEnlistment** instead of **ZwPrepareComplete** to remove itself from the transaction.

-   Your resource manager never participates in any transaction's commit operation.

    For example, your resource manager might monitor data that the client sends, without modifying any stored database. In this case, your resource manager might call **ZwReadOnlyEnlistment** immediately after it has called **ZwCreateEnlistment**. In addition, you might choose to make such a resource manager *volatile*, as described in the next section of this topic.

After a resource manager has called **ZwReadOnlyEnlistment**, it can call [**ZwClose**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose) to close the enlistment handle.

## <a href="" id="kernel-creating-a-volatile-resource-manager"></a> Creating a Volatile-Resource Manager


A *volatile-resource manager* is a resource manager that does not maintain durable data. For example, you might create a volatile-resource manager to monitor data that the client sends, if the resource manager does not modify a durably stored database. Volatile-resource managers typically do not log transaction activity and therefore cannot perform recovery or rollback operations.

A volatile-resource manager must set the RESOURCE\_MANAGER\_VOLATILE flag when it calls [**ZwCreateResourceManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreateresourcemanager). If this flag is set, KTM does not log any information about the resource manager in the log stream of the associated transaction manager object.

Your resource manager can also set a TRANSACTION\_MANAGER\_VOLATILE flag when it calls [**ZwCreateTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreatetransactionmanager). If this flag is set, KTM does not create a log stream for the transaction manager object. In addition, any additional resource managers that are connected to the transaction manager object must also be volatile and set the RESOURCE\_MANAGER\_VOLATILE flag.

## Adding a Resource Manager to an Existing TPS


If you have to add an additional resource manager to an existing TPS, you have two choices:

-   Your new resource manager calls [**ZwCreateTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreatetransactionmanager) to create its own transaction manager object.

    Use this choice if your resource manager does not communicate with other resource managers in the TPS.

-   Your new resource manager calls [**ZwOpenTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopentransactionmanager) to connect to an existing transaction manager object.

    Use this choice if your resource manager must communicate with other resource managers in the TPS. The resource manager that calls **ZwCreateTransactionManager** must share the transaction manager object's GUID, log stream name, or object name so that other resource managers can call **ZwOpenTransactionManager**. These other resource managers can call [**ZwQueryInformationTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationtransactionmanager) to obtain additional information about the transaction manager object.

After you have added your resource manager to the TPS, clients that are aware of your resource manager can call the resource manager's client interface.

 

