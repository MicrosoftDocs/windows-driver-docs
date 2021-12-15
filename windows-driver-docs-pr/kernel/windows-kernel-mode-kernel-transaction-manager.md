---
title: Windows Kernel-Mode Kernel Transaction Manager
description: Windows Kernel-Mode Kernel Transaction Manager
ms.date: 10/17/2018
---

# Windows Kernel-Mode Kernel Transaction Manager


When you are dealing with multiple reads and writes on one or more data stores, and the operations must all atomically succeed or fail to preserve the integrity of the data, you might want to group the operations together as a single transaction. If all of the operations within the transaction succeed, the transaction can be committed so that all the changes persist as an atomic unit. If a failure occurs, the transaction can be rolled back so that the data stores are restored to their original state.

The kernel transaction manager (KTM) is the Windows kernel-mode component that implements transaction processing in kernel mode. KTM allows kernel mode components, such as drivers, to perform transactions. In addition, KTM is the platform on which user-mode [Transactional NTFS (TxF)](/windows/win32/fileio/transactional-ntfs-portal) is based.

For information about how to use KTM in kernel-mode components, see [Kernel Transaction Manager](introduction-to-ktm.md).

 

