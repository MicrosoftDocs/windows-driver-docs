---
title: Understanding TPS Components
description: Understanding TPS Components
ms.assetid: 4bc962fa-8c05-4b0f-b634-9c0f435907b7
keywords: ["transaction processing systems WDK KTM , components", "TPS WDK KTM , components", "transaction processing systems WDK KTM , scenarios", "TPS WDK KTM , scenarios", "resource managers WDK KTM , in a TPS"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Understanding TPS Components


Any [*transaction processing system*](transaction-processing-terms.md#ktm-term-transaction-processing-system) (TPS) that uses the Kernel Transaction Manager (KTM) and the [Common Log File System](using-common-log-file-system.md) (CLFS) should contain the following important components:

-   A [*transaction manager*](transaction-processing-terms.md#ktm-term-transaction-manager) (KTM)

    KTM tracks the state of each transaction and coordinates recovery operations after a system crash.

-   One or more [*resource managers*](transaction-processing-terms.md#ktm-term-resource-manager)

    Resource managers, which you provide, manage the data that is associated with each transaction.

-   One or more CLFS [*log streams*](transaction-processing-terms.md#ktm-term-log-stream)

    The transaction manager and resource managers use CLFS log streams to record information that can be used to commit, roll back, or recover a transaction.

-   One or more [*transactional clients*](transaction-processing-terms.md#ktm-term-transactional-client)

    Typically, each transactional client of your TPS can create a transaction, perform operations on data within the context of the transaction, and then initiate either a commit or rollback operation for the transaction.

This topic introduces you to a [simple TPS](#simple-tps) with one resource manager, a more complex TPS that contains [multiple resource managers](#multiple-resource-managers-in-a-tps), and some [other TPS scenarios](#other-tps-scenarios).

The [Using KTM](using-ktm.md) section provides detailed information about how to use KTM to create TPS components.

### Simple TPS

A simple TPS might consist of KTM, one resource manager, and CLFS. Transactional clients can communicate with the resource manager by an interface that the resource manager provides.

For example, suppose that you want to create a database management system. You want your system's clients to access the database by opening a handle to a database object, performing read and write operations on the object, and then closing the object handle.

Now suppose that you want sets of read and write operations to occur atomically so that other users of the system see only the final result. You can achieve that goal by designing a TPS that enables clients to bind sets of database operations to a transaction.

Your system should include a resource manager that manages the data in the database in response to read and write requests from clients. This resource manager could export an application programming interface (API) that enables clients to associate a transaction with a set of read and write operations.

When your resource manager is loaded, it must register itself with KTM by calling [**ZwCreateTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff566430) and [**ZwCreateResourceManager**](https://msdn.microsoft.com/library/windows/hardware/ff566427). Then, the resource manager can participate in transactions.

You might want your resource manager to support a set of functions that enable clients to create data objects, read and write data that is associated with the data objects, and close the data objects. The following pseudocode shows an example code sequence from a client.

```cpp
CreateDataObject (IN TransactionID, OUT DataHandle);
ReadData (IN DataHandle, OUT Data);
WriteData (IN DataHandle, IN Data);
WriteData (IN DataHandle, IN Data);
WriteData (IN DataHandle, IN Data);
CloseDataObject (IN DataHandle);
```

Before a client can call your resource manager's *CreateDataObject* routine, the client must create a transaction object by calling KTM's [**ZwCreateTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566429) routine and obtain the transaction object's identifier by calling [**ZwQueryInformationTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567057).

When the client calls your resource manager's *CreateDataObject* routine, the client passes the transaction object's identifier to the resource manager. The resource manager can call [**ZwOpenTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567033) to obtain a handle to the transaction object, and then it can call [**ZwCreateEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff566422) to register its participation in the transaction.

At this point, the client can start performing operations on the data object. Because the client provided a transaction identifier when it created the data object, the resource manager can assign all the read and write operations to the transaction.

Your resource manager must record all the results of data operations that the client specifies without making the results permanent. Typically, the resource manager uses CLFS to record the operation results in a transaction log stream.

When the client has finished calling the resource manager to perform transactional operations, it calls KTM's [**ZwCommitTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566420) routine. At this point, KTM [notifies](transaction-notifications.md) the resource manager that it should make the operations permanent. The resource manager then moves the operation results from the log stream to the data's permanent storage medium. Finally, the resource manager calls [**ZwCommitComplete**](https://msdn.microsoft.com/library/windows/hardware/ff566418) to inform KTM that the commit operation is complete.

What happens if your resource manager reports an error for one of the client's calls to *ReadData* or *WriteData*? The client can call [**ZwRollbackTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567086) to roll back the transaction. As a result of that call, KTM notifies the resource manager that it should restore the data to its original state. Then, the client can either create a new transaction for the same operations, or it can choose to not continue.

The following pseudocode shows an example of a more detailed sequence of a client's transactional operations.

```cpp
    ZwCreateTransaction (&TransactionHandle, ...);
    ZwQueryInformationTransaction (TransactionHandle, ...);
    CreateDataObject (TransactionID, &DataHandle);
    Status = ReadData (DataHandle, &Data1);
    if (Status == Error) goto ErrorRollback;
    Status = WriteData (DataHandle, Data2);
    if (Status == Error) goto ErrorRollback;
    Status = WriteData (DataHandle, Data3);
    if (Status == Error) goto ErrorRollback;
    Status = WriteData (DataHandle, Data4);
    if (Status == Error) goto ErrorRollback;
    ZwCommitTransaction (TransactionHandle, ...);
    goto Leave;
ErrorRollback:
    ZwRollbackTransaction (TransactionHandle, ...);
Leave:
    ZwClose (TransactionHandle);
    return;
```

What happens if the system crashes after the transaction is created but before it is committed or rolled back? Every time that your resource manager loads, it should call [**ZwRecoverTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff567079) and [**ZwRecoverResourceManager**](https://msdn.microsoft.com/library/windows/hardware/ff567078). Calling **ZwRecoverTransactionManager** causes KTM to open its log stream and read the transaction history. Calling **ZwRecoverResourceManager** causes KTM to notify the resource manager of any enlisted transactions that were in progress before the crash and which transactions the resource manager must therefore recover.

If a transactional client called [**ZwCommitTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566420) for a transaction before the crash, and began to handle commit operations for the transaction, the resource manager must be able to restore the transaction's state to the point immediately prior to the crash. If the client was not ready to commit the transaction before the crash, the resource manager can discard the data and roll back the transaction.

For more information about how to write transactional clients, see [Creating a Transactional Client](creating-a-transactional-client.md).

For more information about how to write resource managers, see [Creating a Resource Manager](creating-a-resource-manager.md).

### Multiple Resource Managers in a TPS

Now suppose that your TPS enables clients to modify information in two separate databases within a single transaction, so that the transaction succeeds only if the modifications of both databases succeed.

In this case, your TPS can have two resource managers, one for each database. Each resource manager can export an API that clients can use to access the resource manager's database.

The following pseudocode shows how a client might create a single transaction that contains operations on two databases that two resource managers support.

In this example, the client reads data from the first database and writes it to the second database. Then, the client reads data from the second database and writes it to the first database. (The first resource manager exports functions that begin with **Rm1**, and the second resource manager exports functions that begin with **Rm2**.)

```cpp
    ZwCreateTransaction (&TransactionHandle, ...);
    ZwQueryInformationTransaction (TransactionHandle, ...);
    Rm1CreateDataObject (TransactionID, &Rm1DataHandle);
    Rm2CreateDataObject (TransactionID, &Rm2DataHandle);
    Status = Rm1ReadData (Rm1DataHandle, &Rm1Data);
    if (Status == Error) goto ErrorRollback;
    Status = Rm2WriteData (Rm2DataHandle, Rm1Data);
    if (Status == Error) goto ErrorRollback;
    Status = Rm2ReadData (Rm2DataHandle, &Rm2Data);
    if (Status == Error) goto ErrorRollback;
    Status = Rm1WriteData (Rm1DataHandle, Rm2Data);
    if (Status == Error) goto ErrorRollback;
    ZwCommitTransaction (TransactionHandle, ...);
    goto Leave;
ErrorRollback:
    ZwRollbackTransaction (TransactionHandle, ...);
Leave:
    ZwClose (TransactionHandle);
    return;
```

Because the client passes the same transaction identifier to both resource managers, both resource managers can call [**ZwOpenTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567033) and [**ZwCreateEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff566422) to enlist in the transaction. When the client eventually calls [**ZwCommitTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566420), KTM [notifies](transaction-notifications.md) each resource manager that the manager should make the operations permanent, and each resource manager calls [**ZwCommitComplete**](https://msdn.microsoft.com/library/windows/hardware/ff566418) when it has finished.

### Other TPS Scenarios

KTM supports other TPS scenarios. For example, the following scenarios describe components that a TPS might contain:

-   One resource manager that manages multiple databases.

    The resource manager's API could enable clients to open and access more than one database at a time, and the client could combine accesses to multiple databases in a single transaction.

-   One resource manager with an API that clients call, and additional resource managers with APIs that the first resource manager calls.

    The client communicates only with the first resource manager. When that resource manager processes requests from a client, it can access the additional resource managers, as needed, to process the client's requests. For example, a resource manager manages a client-accessible database that requires backup or data verification operations from a second resource manager that is not available to clients.

-   An existing client and resource manager that do not use KTM, integrated with an additional set of resource managers that do use KTM.

    In this case, you typically have to modify the existing resource manager so that it becomes a [superior transaction manager](creating-a-superior-transaction-manager.md) that communicates with KTM.

 

 




