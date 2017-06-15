---
title: Handling Transaction Operations
author: windows-driver-content
description: Handling Transaction Operations
MS-HAID:
- 'ktm\_dg\_3892cd69-c851-4e00-8bc1-eb31f2ea1124.xml'
- 'kernel.handling\_transaction\_operations'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9b82e9d6-3db2-4806-a087-1c9622dc04e2
keywords: ["transactions WDK KTM , handling operations", "handling transaction operations WDK KTM", "transactions WDK KTM , committing transactions", "committing transactions WDK KTM", "transactions WDK KTM , rolling back transactions", "rolling back transactions WDK KTM", "transactions WDK KTM , recovering transactions", "recovering transactions WDK KTM"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20Transaction%20Operations%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


