---
title: Creating a Superior Transaction Manager
description: Creating a Superior Transaction Manager
ms.assetid: 6f6bf61a-fe53-47b5-9559-f76334969af8
keywords: ["transaction managers WDK KTM", "superior transaction managers WDK KTM", "enlistments WDK KTM , superior enlistments", "superior enlistments WDK KTM", "enlistments WDK KTM , subordinate enlistments", "subordinate enlistments WDK KTM"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Creating a Superior Transaction Manager


In KTM, a *superior transaction manager* is a resource manager that creates superior enlistments for the transactions that it participates in. A *superior enlistment* is an enlistment that grants the resource manager the ability to coordinate the [commit operation](handling-commit-operations.md) for the enlistment's transaction. In other words, either a transactional client or the superior transaction manager can start the pre-prepare/prepare/commit sequence for the transaction.

After a resource manager has created a superior enlistment for a transaction, KTM rejects all calls to [**ZwCommitTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566420) for the transaction. Therefore, transactional clients cannot commit such a transaction. Instead, the resource manager that created the superior enlistment must call [**ZwPrePrepareEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567044), [**ZwPrepareEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567039), and [**ZwCommitEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff566419).

### When to Create a Superior Transaction Manager

Suppose that you want to integrate a transaction processing system (TPS) component with KTM, but the component contains its own non-KTM transaction management capabilities that clients can call. In such a situation, you might have to create a superior transaction manager.

For example, suppose that your component provides its own interfaces that clients use to create and commit transactions. Because your component's clients do not call KTM to create or commit transactions, your component must become a superior transaction manager when you integrate it into a KTM-based TPS.

### How to Create a Superior Transaction Manager

If you want your component to be a superior transaction manager, it must do the following:

1.  Call [**ZwCreateResourceManager**](https://msdn.microsoft.com/library/windows/hardware/ff566427) to register as a resource manager.

2.  Call [**ZwCreateTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566429) every time that a client of your component creates a transaction by using your component's client interface.

3.  Call [**ZwCreateEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff566422), setting the ENLISTMENT\_SUPERIOR flag, and specifying both the ENLISTMENT\_SUPERIOR\_RIGHTS and ENLISTMENT\_SUBORDINATE\_RIGHTS access flags.

4.  Call [**ZwPrePrepareEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567044), [**ZwPrepareEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567039), and [**ZwCommitEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff566419) when your component's client calls your component's client interface to commit the transaction.

KTM permits only one superior enlistment per transaction. Other resource managers can create additional enlistments. These enlistments are called *subordinate enlistments* because they cannot initiate the commit operation.

To roll back a superior enlistment, your superior transaction manager calls [**ZwRollbackEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567083).

To recover a superior enlistment, your superior transaction manager calls [**ZwRecoverEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567075).

When a superior transaction manager commits, rolls back, or recovers a transaction, KTM sends [transaction notifications](transaction-notifications.md) to all subordinate enlistments so that they can participate.

A TPS that includes a superior transaction manager cannot use [single-phase commit operations](handling-commit-operations.md#single-phase-commit-operations).

During a recovery operation, if KTM cannot determine the outcome of a transaction, it sends a TRANSACTION\_NOTIFY\_RECOVER\_QUERY notification to the superior transaction manager. In response, the superior transaction manager must call **ZwCommitEnlistment** if the transaction can be committed or **ZwRollbackEnlistment** if the transaction should be rolled back. If the superior transaction manager cannot determine the outcome of a transaction, it should not respond to the TRANSACTION\_NOTIFY\_RECOVER\_QUERY notification until it can determine an outcome.

 

 




