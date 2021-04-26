---
title: Using Virtual Clock Values
description: Using Virtual Clock Values
keywords: ["virtual clock values WDK KTM", "Kernel Transaction Manager WDK , virtual clock values", "KTM WDK , virtual clock values", "transactions WDK KTM , virtual clock values"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using Virtual Clock Values


KTM provides a virtual clock for each transaction manager object. When a resource manager calls [**ZwCreateTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreatetransactionmanager), KTM sets the object's virtual clock value to 1. KTM increments the virtual clock value every time that a commit operation begins. Whenever KTM writes to its log stream, it includes the current virtual clock value in the log record.

When a resource manager calls [**ZwRecoverTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrecovertransactionmanager), KTM reads log stream records up to the end of the stream, and it sets the transaction manager object's virtual clock value to the last value that it finds in the object's log stream.

When a resource manager calls [**ZwRollforwardTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollforwardtransactionmanager), KTM reads log stream records up to the specified clock value, and it sets the transaction manager object's virtual clock value to the specified clock value.

KTM enables resource managers and superior transaction managers to modify a transaction manager object's virtual clock value, but they typically do not have to modify the clock value.

### When to Modify Virtual Clock Values

Typically, your transaction processing system (TPS) does not have to modify virtual clock values unless the components in your TPS are trying to synchronize multiple log streams.

For example, suppose that your TPS contains multiple resource managers that communicate with each other during pre-prepare/prepare/commit sequences. Also suppose that each resource manager creates a transaction manager object that has a unique log stream. To make sure that KTM restores the state of all resource managers to the same point in time during a recovery operation, these resource managers might use the following steps:

-   When one resource manager communicates with another, it passes the most recent virtual clock value that it has received from either KTM or yet another resource manager.

-   Whenever a resource manager calls a KTM routine that accepts a virtual clock value (see the following section in this topic), it passes the highest clock value that it has received from KTM or another resource manager.

-   Each resource manager writes virtual clock values into its log stream and uses those values when it performs rollback or recovery operations.

These steps cause the virtual clock values that KTM stores for each transaction manager object to almost or exactly match. Therefore, when a recovery operation causes KTM to read its log streams, or when a rollback operation causes the resource managers to read their log streams, the recovery or rollback is based on synchronized log streams.

### How to Modify Virtual Clock Values

Resource managers can modify the virtual clock value by passing a new value to [**ZwPrePrepareComplete**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntprepreparecomplete), [**ZwPrepareComplete**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntpreparecomplete), [**ZwCommitComplete**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcommitcomplete), [**ZwRollbackComplete**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollbackcomplete), [**ZwReadOnlyEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntreadonlyenlistment), or [**ZwSinglePhaseReject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntsinglephasereject).

[Superior transaction managers](creating-a-superior-transaction-manager.md) can modify the virtual clock value by passing a new value to [**ZwPrePrepareEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntpreprepareenlistment), [**ZwPrepareEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntprepareenlistment), [**ZwCommitEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcommitenlistment), or [**ZwReadOnlyEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntreadonlyenlistment).

In addition, a resource manager or superior transaction manager that uses a [**ResourceManagerNotification**](/windows-hardware/drivers/ddi/wdm/nc-wdm-ptm_rm_notification) callback routine can modify the virtual clock value that the callback routine receives. KTM then saves the updated value.

If a resource manager or superior transaction manager passes a new clock value to KTM, KTM saves the new value only if it is greater than the current clock value. Otherwise, KTM keeps the current clock value.

Resource managers and superior transaction managers can obtain a transaction manager object's virtual clock value by calling the [**ZwQueryInformationTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationtransactionmanager) routine.

 

