---
title: Handling Recovery Operations
author: windows-driver-content
description: Handling Recovery Operations
MS-HAID:
- 'ktm\_dg\_20d1705b-fcfe-43a5-ae2b-bb38e3c86954.xml'
- 'kernel.handling\_recovery\_operations'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 35149bb9-fd48-44d3-a9fd-0e631aa0e853
keywords: ["transactions WDK KTM , recovering transactions", "recovering transactions WDK KTM", "transaction processing systems WDK KTM , recovering transactions", "TPS WDK KTM , recovering transactions", "log streams WDK KTM , recovering transactions", "virtual clock values WDK KTM , recovering transactions"]
---

# Handling Recovery Operations


In a *recovery* operation, a transaction processing system (TPS) tries to recover its state from the information that is in [log streams](using-log-streams-with-ktm.md). After a recovery operation is complete, all transactions should be in a committed or rolled back state, and all resource data should be in a known good state.

Sometimes a TPS stops before all its transactions have finished. For example, the operating system might crash. Therefore, resource managers must initiate recovery operations whenever they start to run. The recovery operation tries to determine whether any transactions are incomplete. If incomplete transactions are found in the log, the recovery operation tries to commit or roll back those transactions.

For a KTM-based TPS, each recovery operation consists of two steps. The first step involves recovering information from the transaction manager object's log stream. The second step involves recovering information from the resource manager's log stream.

A TPS can recover to the end of all log streams or, if its resource managers maintain [virtual clock values](using-virtual-clock-values.md), it can recover up to a specified clock value.

### Recovering Information from a Transaction Manager Object's Log Stream

Immediately after a resource manager calls [**ZwCreateTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff566430) or [**ZwOpenTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff567035), it must call [**ZwRecoverTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff567079). The **ZwRecoverTransactionManager** routine reads the log stream that belongs to the transaction manager object. This routine reconstructs the state of the transaction manager object (including all transactions, enlistments, and resource managers) from the recovery information that is in the log stream, beginning at the last [restart area](reading-restart-records-from-a-clfs-stream.md) that KTM created and ending at the stream's end.

To recover from the last restart area up to a specified virtual clock value, the resource manager can call [**ZwRollforwardTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff567089) instead of **ZwRecoverTransactionManager**.

### Recovering Information from a Resource Manager's Log Stream

Immediately after a resource manager calls [**ZwCreateResourceManager**](https://msdn.microsoft.com/library/windows/hardware/ff566427) or [**ZwOpenResourceManager**](https://msdn.microsoft.com/library/windows/hardware/ff567026), it must call [**ZwRecoverResourceManager**](https://msdn.microsoft.com/library/windows/hardware/ff567078). The **ZwRecoverResourceManager** routine tries to recover the transactions that are associated with each of the resource manager's enlistments.

When a resource manager calls **ZwRecoverResourceManager**, KTM sends TRANSACTION\_NOTIFY\_RECOVER [notifications](transaction-notifications.md) for each of the resource manager's enlistments. The resource manager must call [**ZwRecoverEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567075) every time that it receives one of the TRANSACTION\_NOTIFY\_RECOVER notifications.

When the resource manager calls **ZwRecoverEnlistment**, KTM sends one of the following notifications:

-   TRANSACTION\_NOTIFY\_COMMIT

    The resource manager must use information in its log stream to commit the transaction and then must call [**ZwCommitComplete**](https://msdn.microsoft.com/library/windows/hardware/ff566418).

-   TRANSACTION\_NOTIFY\_ROLLBACK

    The resource manager must use information in its log stream to roll back the transaction and then must call [**ZwRollbackComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567081).

-   TRANSACTION\_NOTIFY\_INDOUBT

    KTM has not determined the state of the transaction and will send a commit or rollback notification later.

Typically, KTM sends a TRANSACTION\_NOTIFY\_COMMIT notification if it determines that all resource managers called [**ZwPrepareComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567037) before the TPS stopped and restarted. KTM sends a TRANSACTION\_NOTIFY\_ROLLBACK notification if it determines that one or more resource managers did not call **ZwPrepareComplete**.

After KTM has sent a TRANSACTION\_NOTIFY\_RECOVER notification for each enlistment, it sends a TRANSACTION\_NOTIFY\_LAST\_RECOVER notification.

If your resource manager called **ZwRollforwardTransactionManager** instead of **ZwRecoverTransactionManager**, it must recover only up to the virtual clock value that it specified to **ZwRollforwardTransactionManager**.

Resource managers can call [**ZwSetInformationEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567094) to set customized recovery information. KTM saves this information and writes it to the log stream, but KTM does not try to interpret the information. The resource manager can retrieve the recovery information at any time by calling [**ZwQueryInformationEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567051).

[Superior transaction managers](creating-a-superior-transaction-manager.md) sometimes receive TRANSACTION\_NOTIFY\_RECOVER\_QUERY notifications during a recover operation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20Recovery%20Operations%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


