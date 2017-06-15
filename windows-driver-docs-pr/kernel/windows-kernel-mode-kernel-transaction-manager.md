---
title: Windows Kernel-Mode Kernel Transaction Manager
author: windows-driver-content
description: Windows Kernel-Mode Kernel Transaction Manager
MS-HAID:
- 'tranmanager\_0dbe1e99-f577-4d81-9473-ad0be7a30f66.xml'
- 'kernel.windows\_kernel\_mode\_kernel\_transaction\_manager'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 43bf96ed-8be8-4670-a310-99cd7c7f9073
---

# Windows Kernel-Mode Kernel Transaction Manager


When you are dealing with multiple reads and writes on one or more data stores, and the operations must all atomically succeed or fail to preserve the integrity of the data, you might want to group the operations together as a single transaction. If all of the operations within the transaction succeed, the transaction can be committed so that all the changes persist as an atomic unit. If a failure occurs, the transaction can be rolled back so that the data stores are restored to their original state.

The kernel transaction manager (KTM) is the Windows kernel-mode component that implements transaction processing in kernel mode. KTM allows kernel mode components, such as drivers, to perform transactions. In addition, KTM is the platform on which user-mode [Transactional NTFS (TxF)](http://go.microsoft.com/fwlink/p/?linkid=131245) is based.

For information about how to use KTM in kernel-mode components, see [Kernel Transaction Manager](using-kernel-transaction-manager.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Windows%20Kernel-Mode%20Kernel%20Transaction%20Manager%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


