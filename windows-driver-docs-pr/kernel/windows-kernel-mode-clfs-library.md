---
title: Windows Kernel-Mode CLFS Library
description: Windows Kernel-Mode CLFS Library
ms.date: 10/17/2018
---

# Windows Kernel-Mode CLFS Library


Windows provides a transactional logging system for system files. This system is called the Common Log File System (CLFS). For more information about CLFS, see [Common Log File System](introduction-to-the-common-log-file-system.md).

Routines that provide a direct interface for CLFS are prefixed with the letters "**Clfs**"; for a list of CLFS library routines, see [Common Log File System (CLFS) Library Routines](/windows-hardware/drivers/ddi/index). CLFS also provides a list of routines that you can implement to manage a CLFS; for more information on CLFS management, see [CLFS Management Library Routines](/windows-hardware/drivers/ddi/index).

CLFS is a technology that is related to transacted file systems; for more information about transactions, see [Windows Kernel-Mode Transaction Manager](windows-kernel-mode-kernel-transaction-manager.md).

 

