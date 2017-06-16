---
title: Creating a Transactional Client
author: windows-driver-content
description: Creating a Transactional Client
ms.assetid: 75d4758b-dfba-431b-9bfa-9dcb98c2a7cc
keywords: ["transactional clients WDK KTM", "transactional clients WDK KTM , creating transactional clients"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Creating a Transactional Client


A [*transactional client*](transaction-processing-terms.md#ktm-term-transactional-client) is a transaction processing system (TPS) component that uses a resource manager's exported interface to access a resource, such as a database, that the resource manager supports.

Typically, the client creates a transaction, performs a set of database operations, and then commits the transaction to make the operations permanent. If the client encounters an error, it can roll back the transaction to remove the transaction's operations instead of committing the transaction.

Typically, a transactional client that uses kernel-mode KTM must perform the following tasks for each transaction:

1.  Create a transaction object.

    A call to [**ZwCreateTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566429) creates a transaction object, provides an object handle, and assigns an object identifier (a GUID) that the client can pass to the resource manager to identify the transaction.

2.  Obtain the transaction object's identifier.

    The client can call [**ZwQueryInformationTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567057) to obtain the object identifier.

3.  Pass the transaction object's identifier to a resource manager.

    The client typically calls the resource manager's exported interface to open a communication path to the resource manager and to associate the path with the transaction. For example, the resource manager might provide a *CreateDataObject* routine that is similar to the one that the [Understanding TPS Components](understanding-tps-components.md) topic describes.

4.  Perform operations to be included in the transaction.

    Typically, the client calls the resource manager's interface to access the resource manager's resource. For example, the client of a database manager might read from and write to the database.

5.  Commit or roll back the transaction.

    If all the resource operations succeed, the client must call [**ZwCommitTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566420) to make the operations permanent. If an operation fails, the client must call [**ZwRollbackTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567086) instead of **ZwCommitTransaction**. For example, if the client of a database manager determines that one of a series of write operations failed, the client must call **ZwRollbackTransaction** so that none of the write operations become permanent.

    Clients can call **ZwCommitTransaction** and **ZwRollbackTransaction** either synchronously or asynchronously. If clients call these routines synchronously, the routines do not return until the commit or rollback operation is complete.

    For more information about how to commit and roll back transactions, see [Handling Transaction Operations](handling-transaction-operations.md).

6.  Close the transaction object handle.

    After the client has finished processing the transaction, it must call [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417) to close the transaction object's handle

A TPS might include more than one resource manager. If a client's transaction includes operations on multiple resources, such as two databases that two resource managers support, the client typically does the following:

1.  Creates a single transaction object for each transaction.

2.  Passes the transaction object's identifier to each resource manager.

3.  Performs operations on each database by calling each resource manager's interface.

4.  Commits the transaction if all operations completed without errors, or rolls back the transaction if an error was detected.

If your TPS includes a *superior transaction manager*, transactional clients typically do not call KTM. For more information about superior transaction managers and their clients, see [Creating a Superior Transaction Manager](creating-a-superior-transaction-manager.md).

Transactional clients can call [**ZwSetInformationTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567104) to set transaction-specific information. For example, a client can set a time-out value for the transaction or supply a descriptive character string. Clients can call [**ZwQueryInformationTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567057) to retrieve information about a transaction. For example, a client can call this routine to determine whether a transaction has been committed or rolled back.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Creating%20a%20Transactional%20Client%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


