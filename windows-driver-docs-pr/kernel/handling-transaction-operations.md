---
title: Handling Transaction Operations
description: Handling Transaction Operations
ms.assetid: 9b82e9d6-3db2-4806-a087-1c9622dc04e2
keywords: ["transactions WDK KTM , handling operations", "handling transaction operations WDK KTM", "transactions WDK KTM , committing transactions", "committing transactions WDK KTM", "transactions WDK KTM , rolling back transactions", "rolling back transactions WDK KTM", "transactions WDK KTM , recovering transactions", "recovering transactions WDK KTM"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling Transaction Operations


Resource managers must handle three transaction operations: *commit*, *rollback*, and *recovery*.

To *commit a transaction*, a resource manager makes all changes to a transaction's data permanent and visible to other transactions.

To *roll back a transaction*, a resource manager removes all changes to a transaction's data. The resource manager must restore the data to the state that it was in before the transaction was created.

To *recover a transaction*, a resource manager restores a transaction's data to a known good state after a system crash or another unexpected event.

This section contains the following topics:

[Handling Commit Operations](handling-commit-operations.md)

[Handling Rollback Operations](handling-rollback-operations.md)

[Handling Recovery Operations](handling-recovery-operations.md)

 

 




