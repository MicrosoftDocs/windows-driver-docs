---
title: Debugging a Dual-Boot Machine
description: Debugging a Dual-Boot Machine
keywords: ["dual-boot machines"]
ms.date: 05/23/2017
---

# Debugging a Dual-Boot Machine


## <span id="ddk_debugging_dual_boot_machines_dbg"></span><span id="DDK_DEBUGGING_DUAL_BOOT_MACHINES_DBG"></span>


How should you respond when the alternate operating system does not start on a dual-boot machine?

First, check that the boot options point to the correct path for the other operating system. See [Getting Set Up for Debugging](getting-set-up-for-debugging.md) for details.

On an x86 computer, you should also verify that boosect.ini exists. This file contains the boot record for the other operating system. To unhide this file, use the **attrib -r -s -h boosect.ini** command.

 

 