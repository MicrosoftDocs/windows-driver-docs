---
title: Transaction Processing Terms
description: Before you begin to use KTM, you should know the definitions of the following terms transaction, resource manager, transactional client, transaction manager, log stream, enlistment, and transaction processing system.
Robots: noindex, nofollow
ms.assetid: c8a8806f-a228-4d02-9995-c8cf45e57935
keywords: ["Kernel Transaction Manager WDK , terminology", "KTM WDK , terminology", "transactions WDK KTM , definition", "resource managers WDK KTM , definition", "transactional clients WDK KTM , definition", "transaction managers WDK KTM , definition", "log streams WDK KTM , definition", "enlistments WDK KTM , definition", "transaction processing systems WDK KTM , definition", "TPS WDK KTM , definition", "transactions WDK KTM , terminology", "transaction managers WDK KTM"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Transaction Processing Terms


Before you begin to use KTM, you should know the definitions of the following terms: [transaction](#ktm-term-transaction), [resource manager](#ktm-term-resource-manager), [transactional client](#ktm-term-transactional-client), [transaction manager](#ktm-term-transaction-manager), [log stream](#ktm-term-log-stream), [enlistment](#ktm-term-enlistment), and [transaction processing system](#ktm-term-transaction-processing-system).

<a href="" id="ktm-term-transaction"></a>**transaction**  
A *transaction* is a collection of data operations. All the operations must succeed for the transaction to succeed. If all the operations succeed, the transaction can be *committed* (that is, its results can be made permanent and public). If any operation fails, the transaction must be *rolled back*, (that is, all changes must be removed so that the data is in the same state that it was in before the transaction's operations began).

A transaction's operations are *atomic*, *consistent*, *isolated*, and *durable* (ACID).

-   They are atomic because they must be committed or rolled back as a whole.

-   They are consistent because the operations always produce an accurate result, whether they are committed or rolled back.

-   They are isolated because each transaction's results are not visible to other transactions until the transaction's operations have been committed or rolled back.

-   They are durable because, after the transaction's operations have been committed or rolled back, the results of the operations are permanent.

An example of a transaction is the set of operations that must be performed when you use an automatic teller machine (ATM) to transfer money from your checking account to your savings account. The debit from your checking account and the credit to your savings account must appear to be a single, atomic operation.

An operation that is part of a transaction is also known as a *transacted operation*.

<a href="" id="ktm-term-resource-manager"></a>**resource manager**  
A *resource manager* is a software component that manages data resources that can be updated by transacted operations. For example, if you are designing a database system, you might provide a resource manager that stores and retrieves the database's data. A simple [transaction processing system](#ktm-term-transaction-processing-system) (TPS) might have only one resource manager.

A resource manager typically also provides a public interface that transactional clients can call to access the resource manager's data. For example, the resource manager for a database might provide a set of functions that clients can call to read from and write to the database.

A more complex TPS can have multiple resource managers, each of which manages a separate database or other resource while participating in the system's transactions.

For more information about resource managers, see [Creating a Resource Manager](creating-a-resource-manager.md).

In some cases, one resource manager is *superior* to the other resource managers and can initiate commit operations. In KTM, such resource managers are called [superior transaction managers](creating-a-superior-transaction-manager.md).

<a href="" id="ktm-term-transactional-client"></a>**transactional client**  
A *transactional client* is a software component that accesses a database that a resource manager supports, typically by calling functions that the resource manager exports. The client is responsible for creating transactions, performing a set of operations that a resource manager supports, and then informing the transaction manager (KTM) that the transaction should be either committed or rolled back.

For more information about transactional clients, see [Creating a Transactional Client](creating-a-transactional-client.md).

<a href="" id="ktm-term-transaction-manager"></a>**transaction manager**  
A *transaction manager*, such as KTM, provides the infrastructure that enables transactional clients and resource managers to communicate with each other. It also tracks the state of each transaction (but not the data that clients and resource managers handle).

The transaction manager can also coordinate recovery operations after a system crash.

The transaction manager has no knowledge of the data or operations that make up a transaction. The data and operations are controlled by the clients and resource managers.

KTM provides functions that transactional clients can call. These functions enable clients to create, commit, and roll back transactions.

KTM also provides functions that resource managers can call. These functions enable resource managers to enlist in transactions so that they can receive notifications about transactions. After a resource manager enlists in a transaction, it can receive a notification when a transactional client is ready to commit or roll back the transaction, or when a recovery operation occurs.

<a href="" id="ktm-term-log-stream"></a>**log stream**  
A *log stream* is a recorded history of the events that have happened to transactions. KTM maintains a log stream by using the [Common Log File System](using-common-log-file-system.md) (CLFS). KTM records state changes for each transaction so that it can support rollback and recovery operations when they are necessary.

Resource managers must also use a log stream to record data and operations.

A rollback operation requires KTM and resource managers to restore a transaction and all data to an initial state. KTM and resource managers record the initial state of each transaction in the log streams so that they can fetch it during a rollback operation.

Recovery operations occur after a system crash. When the operating system subsequently restarts, KTM and resource managers can use log stream contents to rebuild a transaction's state to the state that it was in before the crash.

For more information about log streams in KTM, see [Using Log Streams with KTM](using-log-streams-with-ktm.md).

<a href="" id="ktm-term-enlistment"></a>**enlistment**  
An *enlistment* is an association between a resource manager and a transaction. KTM provides a set of functions that resource managers call to create and manage enlistments. After a resource manager creates an enlistment, KTM sends notifications to the resource manager when the transaction's state changes.

<a href="" id="ktm-term-transaction-processing-system"></a>**transaction processing system**  
A *transaction processing system* (TPS) is a collection of a transaction manager, one or more resource managers, one or more log streams, and one or more transactional clients that access the resource managers' resources.

 

 




