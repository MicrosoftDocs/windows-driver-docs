---
title: Boot Parameters to Load a Partial Checked Build
description: Boot Parameters to Load a Partial Checked Build
ms.assetid: 701a3258-d659-49a7-8e0d-52adc556a289
keywords:
- partial checked build boot options WDK
- boot parameters WDK
- boot entry parameters WDK
- loading partial checked builds WDK boot options
ms.date: 04/20/2017
ms.localizationpriority: medium
---

#  Boot Parameters to Load a Partial Checked Build


## <span id="ddk_boot_parameters_to_load_a_partial_checked_build_tools"></span><span id="DDK_BOOT_PARAMETERS_TO_LOAD_A_PARTIAL_CHECKED_BUILD_TOOLS"></span>


A *partial checked build* contains checked build versions of the kernel and HAL and a free build of the remainder of the operating system. For details, see [Installing Just the Checked Operating System and HAL (For Windows Vista and Later)](installing-just-the-checked-operating-system-and-hal--for-windows-vist.md).

### <span id="configuring_a_partial_checked_build_in_windows_vista_and_later"></span><span id="CONFIGURING_A_PARTIAL_CHECKED_BUILD_IN_WINDOWS_VISTA_AND_LATER"></span>Configuring a Partial Checked Build in Windows

To configure a partial checked build use the [**BCDedit /set**](https://msdn.microsoft.com/library/windows/hardware/ff542202) command and the **kernel** and **hal** options.

The following commands configure a boot entry to use the checked versions of the kernel and hardware abstraction layer (HAL).

```
bcdedit /set {18b123cd-2bf6-11db-bfae-00e018e2b8db} kernel ntoskrnl.chk
```

```
bcdedit /set {18b123cd-2bf6-11db-bfae-00e018e2b8db} hal halacpi.chk
```

To view the results of the commands, type **bcdedit /enum**. The **/enum** option lists all of the boot entries. The boot entry that has been modified to use the checked versions of the kernel and HAL has also been configured for kernel debugging over a serial connection.

```
## Windows Boot Loader
-------------------
identifier              {18b123cd-2bf6-11db-bfae-00e018e2b8db}
device                  partition=C:
path                    \Windows\system32\winload.exe
description             PartialCheckedBuild
locale                  en-US
inherit                 {bootloadersettings}
debugtype               serial
debugport               1
baudrate                115200
osdevice                partition=C:
systemroot              \Windows
kernel                  ntoskrnl.chk
hal                     halacpi.chk
resumeobject            {d7094401-2641-11db-baba-00e018e2b8db}
nx                      OptIn
debug                   Yes
```

 

 





