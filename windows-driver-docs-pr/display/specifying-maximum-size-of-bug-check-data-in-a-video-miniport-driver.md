---
title: The Max Size of Bug-check Data in a Video Miniport Driver
description: Specifying Maximum Size of Bug-check Data in a Video Miniport Driver
keywords:
- BugcheckDataSize
- video miniport driver bug-check data WDK DirectX 9.0
- bug-check data size WDK DirectX 9.0
ms.date: 12/06/2018
ms.custom: seodec18
---

# The Max Size of Bug-check Data in a Video Miniport Driver


**This topic applies only to Microsoft Windows XP with Service Pack 1 (SP1) and later.**

A video miniport driver must set the value for the *BugcheckDataSize* parameter of the **VideoPortRegisterBugcheckCallback** function to be no greater than 0x0F20 (4000) bytes for Windows XP SP1 and Microsoft Windows Server 2003 releases. In Windows Server 2003 and later releases, the maximum value for *BugcheckDataSize* is the MAX\_SECONDARY\_DUMP\_SIZE constant. The value of this constant might change in releases later than Windows Server 2003.

The Windows XP SP1 DDK documentation incorrectly specified the maximum value for *BugcheckDataSize*.

 

 





