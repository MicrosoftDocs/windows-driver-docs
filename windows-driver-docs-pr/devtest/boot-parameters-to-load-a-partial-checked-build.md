---
title: Boot Parameters to Load a Partial Checked Build
description: Boot Parameters to Load a Partial Checked Build
ms.assetid: 701a3258-d659-49a7-8e0d-52adc556a289
keywords: ["partial checked build boot options WDK", "boot parameters WDK", "boot entry parameters WDK", "loading partial checked builds WDK boot options"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20%20%20%20%20%20%20%20%20%20%20%20Boot%20Parameters%20to%20Load%20a%20Partial%20Checked%20Build%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




