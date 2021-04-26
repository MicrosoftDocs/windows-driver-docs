---
title: Handling Recovery Operations
description: Handling Recovery Operations
keywords: ["transactions WDK KTM , recovering transactions", "recovering transactions WDK KTM", "transaction processing systems WDK KTM , recovering transactions", "TPS WDK KTM , recovering transactions", "log streams WDK KTM , recovering transactions", "virtual clock values WDK KTM , recovering transactions"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling Recovery Operations


In a *recovery* operation, a transaction processing system (TPS) tries to recover its state from the information that is in [log streams](using-log-streams-with-ktm.md). After a recovery operation is complete, all transactions should be in a committed or rolled back state, and all resource data should be in a known good state.

Sometimes a TPS stops before all its transactions have finished. For example, the operating system might crash. Therefore, resource managers must initiate recovery operations whenever they start to run. The recovery operation tries to determine whether any transactions are incomplete. If incomplete transactions are found in the log, the recovery operation tries to commit or roll back those transactions.

For a KTM-based TPS, each recovery operation consists of two steps. The first step involves recovering information from the transaction manager object's log stream. The second step involves recovering information from the resource manager's log stream.

A TPS can recover to the end of all log streams or, if its resource managers maintain [virtual clock values](using-virtual-clock-values.md), it can recover up to a specified clock value.

### Recovering Information from a Transaction Manager Object's Log Stream

Immediately after a resource manager calls [**ZwCreateTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreatetransactionmanager) or [**ZwOpenTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopentransactionmanager), it must call [**ZwRecoverTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrecovertransactionmanager). The **ZwRecoverTransactionManager** routine reads the log stream that belongs to the transaction manager object. This routine reconstructs the state of the transaction manager object (including all transactions, enlistments, and resource managers) from the recovery information that is in the log stream, beginning at the last [restart area](reading-restart-records-from-a-clfs-stream.md) that KTM created and ending at the stream's end.

To recover from the last restart area up to a specified virtual clock value, the resource manager can call [**ZwRollforwardTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollforwardtransactionmanager) instead of **ZwRecoverTransactionManager**.

### Recovering Information from a Resource Manager's Log Stream

Immediately after a resource manager calls [**ZwCreateResourceManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreateresourcemanager) or [**ZwOpenResourceManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopenresourcemanager), it must call [**ZwRecoverResourceManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrecoverresourcemanager). The **ZwRecoverResourceManager** routine tries to recover the transactions that are associated with each of the resource manager's enlistments.

When a resource manager calls **ZwRecoverResourceManager**, KTM sends TRANSACTION\_NOTIFY\_RECOVER [notifications](transaction-notifications.md) for each of the resource manager's enlistments. The resource manager must call [**ZwRecoverEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrecoverenlistment) every time that it receives one of the TRANSACTION\_NOTIFY\_RECOVER notifications.

When the resource manager calls **ZwRecoverEnlistment**, KTM sends one of the following notifications:

-   TRANSACTION\_NOTIFY\_COMMIT

    The resource manager must use information in its log stream to commit the transaction and then must call [**ZwCommitComplete**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcommitcomplete).

-   TRANSACTION\_NOTIFY\_ROLLBACK

    The resource manager must use information in its log stream to roll back the transaction and then must call [**ZwRollbackComplete**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollbackcomplete).

-   TRANSACTION\_NOTIFY\_INDOUBT

    KTM has not determined the state of the transaction and will send a commit or rollback notification later.

Typically, KTM sends a TRANSACTION\_NOTIFY\_COMMIT notification if it determines that all resource managers called [**ZwPrepareComplete**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntpreparecomplete) before the TPS stopped and restarted. KTM sends a TRANSACTION\_NOTIFY\_ROLLBACK notification if it determines that one or more resource managers did not call **ZwPrepareComplete**.

After KTM has sent a TRANSACTION\_NOTIFY\_RECOVER notification for each enlistment, it sends a TRANSACTION\_NOTIFY\_LAST\_RECOVER notification.

If your resource manager called **ZwRollforwardTransactionManager** instead of **ZwRecoverTransactionManager**, it must recover only up to the virtual clock value that it specified to **ZwRollforwardTransactionManager**.

Resource managers can call [**ZwSetInformationEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntsetinformationenlistment) to set customized recovery information. KTM saves this information and writes it to the log stream, but KTM does not try to interpret the information. The resource manager can retrieve the recovery information at any time by calling [**ZwQueryInformationEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationenlistment).

[Superior transaction managers](creating-a-superior-transaction-manager.md) sometimes receive TRANSACTION\_NOTIFY\_RECOVER\_QUERY notifications during a recover operation.

 

