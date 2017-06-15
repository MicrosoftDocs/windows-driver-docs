---
title: Creating a Superior Transaction Manager
author: windows-driver-content
description: Creating a Superior Transaction Manager
MS-HAID:
- 'ktm\_dg\_f862958e-bbef-4210-bce8-505a861d7a75.xml'
- 'kernel.creating\_a\_superior\_transaction\_manager'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6f6bf61a-fe53-47b5-9559-f76334969af8
keywords: ["transaction managers WDK KTM", "superior transaction managers WDK KTM", "enlistments WDK KTM , superior enlistments", "superior enlistments WDK KTM", "enlistments WDK KTM , subordinate enlistments", "subordinate enlistments WDK KTM"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Creating%20a%20Superior%20Transaction%20Manager%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


