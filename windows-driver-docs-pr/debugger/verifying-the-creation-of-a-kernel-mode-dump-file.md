---
title: Verifying the Creation of a Kernel-Mode Dump File
description: Verifying the Creation of a Kernel-Mode Dump File
keywords: ["dump file, verifying kernel-mode dump creation"]
ms.date: 05/23/2017
---

# Verifying the Creation of a Kernel-Mode Dump File


## <span id="ddk_verifying_the_creation_of_a_kernel_mode_dump_file_dbg"></span><span id="DDK_VERIFYING_THE_CREATION_OF_A_KERNEL_MODE_DUMP_FILE_DBG"></span>


If you have a machine that has broken into the debugger, but you are unsure whether the crash dump file was successfully written, execute the following command:

```dbgcmd
dd nt!IopFinalCrashDumpStatus L1
```

This displays the value of the **IopFinalCrashDumpStatus** variable.

If this value equals zero, the process was successful. If it equals -1 (0xFFFFFFFF), the dump process has not started.

Any other value is a status code indicating an error during the dump process.

 

 





