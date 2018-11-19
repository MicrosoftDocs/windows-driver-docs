---
title: BCDEdit /set
description: The BCDEdit /set command sets a boot entry option value in the Windows boot configuration data store (BCD) for Windows 7, Windows Server 2008, Windows 8, Windows 8.1,Windows 10, Windows Server 2012, and Windows Server 2012 R2.
ms.assetid: e66d9c55-9a44-4de2-a1a4-634c7d550735
ms.date: 07/09/2018
keywords: ["BCDEdit /set Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /set
api_type:
- NA
ms.localizationpriority: medium
---

# BCDEdit /set

The **BCDEdit /set** command sets a boot entry option value in the Windows boot configuration data store (BCD) for Windows 7, Windows Server 2008, Windows 8, Windows 8.1,Windows 10, Windows Server 2012, and Windows Server 2012 R2. Use the **BCDEdit /set** command to configure specific boot entry elements, such as kernel debugger settings, memory options, or options that enable test-signed kernel-mode code or load alternate hardware abstraction layer (HAL) and kernel files. To remove a boot entry option, use the [**BCDEdit /deletevalue**](bcdedit--deletevalue.md) command.

> [!CAUTION]
> Administrative privileges are required to use BCDEdit to modify BCD. Changing some boot entry options using the **BCDEdit /set** command could render your computer inoperable. As an alternative, use the System Configuration utility (MSConfig.exe) to change boot settings.

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

```syntax
bcdedit  /set [{ID}] datatype value
```

## Parameters

\[**{ID}**\]  
The **{ID}** is the GUID that is associated with the boot entry. If you do not specify an **{ID}**, the command modifies the current operating system boot entry. If a boot entry is specified, the GUID associated with the boot entry must be enclosed in braces **{ }**. To view the GUID identifiers for all of the active boot entries, use the **bcdedit /enum** command. The identifier for the current boot entry is **{current}**. For more information about this option, use the following command: **bcdedit /? ID**

> [!NOTE]
> If you are using [Windows PowerShell](http://go.microsoft.com/fwlink/p/?linkid=108518), you must use quotes around the boot entry identifier, for example: **"{49916baf-0e08-11db-9af4-000bdbd316a0}"** or **"{current}"**.

*datatype* *value*  

The following list shows some useful *datatypes* and their associated *values*.

**bootlog** \[ **yes** | **no** \]  
Enables the system initialization log. This log is stored in the Ntbtlog.txt file in the %WINDIR% directory. It includes a list of loaded and unloaded drivers in text format.

**bootmenupolicy** \[ **Legacy** | **Standard** \]  
Defines the type of boot menu the system will use. ForWindows 10, Windows 8.1, Windows 8 and Windows RT the default is **Standard**. For Windows Server 2012 R2, Windows Server 2012, the default is **Legacy**. When **Legacy** is selected, the Advanced options menu (**F8**) is available. When **Standard** is selected, the boot menu appears but only under certain conditions: for example, if there is a startup failure, if you are booting up from a repair disk or installation media, if you have configured multiple boot entries, or if you manually configured the computer to use Advanced startup. When **Standard** is selected, the **F8** key is ignored during boot. Windows 8 PCs start up quickly so there isn't enough time to press **F8**. For more information, see [Windows Startup Settings (including safe mode)](http://go.microsoft.com/fwlink/p/?linkid=313921).

> [!NOTE]
> The option is available starting with Windows 8 and Windows Server 2012. You can also use the **onetimeadvancedoptions** to use the Advanced options (**F8**) menu (**Legacy**) one time on the next boot.

**bootstatuspolicy** *policy*

Controls the boot status policy. The boot status *policy* can be one of the following:

- `DisplayAllFailures`: Displays all errors if there is a failed boot, failed shutdown, or failed checkpoint. The computer will fail over to the Windows recovery environment on reboot.

- `IgnoreAllFailures`: Ignore errors if there is a failed boot, failed shutdown, or failed checkpoint. The computer will attempt to boot normally after an error occurs.

- `IgnoreShutdownFailures`: Only ignore errors if there is a failed shutdown. If there is a failed shutdown, the computer does not automatically fail over to the Windows recovery environment on reboot. This is the default setting for Windows 8.

- `IgnoreBootFailures`: Only ignore errors if there is a failed boot. If there is a failed boot, the computer does not automatically fail over to the Windows recovery environment on reboot.

- `IgnoreCheckpointFailures`: Only ignore errors if there is a failed checkpoint. If there is a failed checkpoint, the computer does not automatically fail over to the Windows recovery environment on reboot. The option is available starting with Windows 8 and Windows Server 2012.

- `DisplayShutdownFailures`: Displays errors if there is a failed shutdown. If there is a failed shutdown, the computer will fail over to the Windows recovery environment on reboot. Ignores boot failures and failed checkpoints. The option is available starting with Windows 8 and Windows Server 2012.

- `DisplayBootFailures`: Displays errors if there is a failed boot. If there is a failed boot, the computer will fail over to the Windows recovery environment on reboot. Ignores shutdown failures and failed checkpoints. The option is available starting with Windows 8 and Windows Server 2012.

- `DisplayCheckpointFailures`: Displays errors if there is a failed checkpoint. If there is a failed checkpoint, the computer will fail over to the Windows recovery environment on reboot. Ignores boot and shutdown failures. The option is available starting with Windows 8 and Windows Server 2012.

**bootux** \[ **disabled** | **basic** | **standard** \]  
Controls the boot screen animation. The possible values are disabled, basic, and standard.

> [!NOTE]
> Not supported in Windows 8 and Windows Server 2012.

**disabledynamictick** \[ **yes** | **no** \]  
Enables and disables dynamic timer tick feature. The option is available starting with Windows 8 and Windows Server 2012.

> [!NOTE]
> This option should only be used for debugging.

**disableelamdrivers** \[ **yes** | **no** \]  
Controls the loading of Early Launch Antimalware (ELAM) drivers. The OS loader removes this entry for security reasons. This option can only be triggered by using the F8 menu. Someone must be physically present (at the computer) to trigger this option.

> [!NOTE]
> This option should only be used for debugging. The option is available starting with Windows 8 and Windows Server 2012.

**forcelegacyplatform** \[ **yes** | **no** \]  
Forces the OS to assume the presence of legacy PC devices like CMOS and keyboard controllers.

> [!NOTE]
> This option should only be used for debugging. The option is available starting with Windows 8 and Windows Server 2012.

**groupsize** *maxsize*
Sets the maximum number of logical processors in a single processor group, where *maxsize* is any power of 2 between 1 and 64 inclusive. By default, processor groups have a maximum size of 64 logical processors. You can use this boot configuration setting to override the size and makeup of a computer's processor groups for testing purposes. [Processor groups](http://go.microsoft.com/fwlink/p/?linkid=155063) provide support for computers with greater than 64 logical processors. This boot option is available on 64-bit versions of Windows 7 and Windows Server 2008 R2 and later versions. This boot option has no effect on the 32-bit versions of Windows 7.

Use the **groupsize** option if you want to force multiple groups and the computer has 64 or fewer active logical processors. For more information about using this option, see [Boot Parameters to Test Drivers for Multiple Processor Group Support](https://msdn.microsoft.com/library/windows/hardware/ff542298).

**groupaware** \[ **on** | **off** \]  
Forces drivers to be aware of multiple groups in a multiple processor group environment. Use this option to help expose cross-group incompatibilities in drivers and components. [Processor groups](http://go.microsoft.com/fwlink/p/?linkid=155063) provide support for computers with greater than 64 logical processors. This boot option is available on 64-bit versions of Windows 7 and Windows Server 2008 R2 and later versions. This boot option has no effect on the 32-bit versions of Windows 7. You can use the **groupaware** option and the **groupsize** option to test driver compatibility to function with multiple groups when computer has 64 or fewer active logical processors.

The **groupaware on** setting ensures that processes are started in a group other than group 0. This increases the chances of cross-group interaction between drivers and components. The option also modifies the behavior of the legacy functions, **KeSetTargetProcessorDpc**, **KeSetSystemAffinityThreadEx**, and **KeRevertToUserAffinityThreadEx**, so that they always operate on the highest numbered group that contains active logical processors. Drivers that call any of these legacy functions should be changed to call their group-aware counterparts (**KeSetTargetProcessorDpcEx**, **KeSetSystemGroupAffinityThread**, and **KeRevertToUserGroupAffinityThread**).

For more information about using this option, see [Boot Parameters to Test Drivers for Multiple Processor Group Support](https://msdn.microsoft.com/library/windows/hardware/ff542298).

**hal** *file*
Directs the operating system loader to load an alternate HAL file. The specified file must be located in the %SystemRoot%\\system32 directory.

**hypervisorbusparams** *Bus.Device.Function*  
Defines the PCI bus, device, and function numbers of the debugging device. For example, 1.5.0 describes the debugging device on bus 1, device 5, function 0. Use this option when you are using either a 1394 cable, or a USB 2.0 or USB 3.0 debug cable for debugging.

**hypervisordebug** \[ **On** | **Off** \]  
Controls whether the hypervisor debugger is enabled.

**Serial**  
Specifies a serial connection for debugging. When the **Serial** option is specified, you also set the **hypervisordebugport** and **hypervisorbaudrate** options.

``` syntax
bcdedit /set hypervisordebugtype serial
bcdedit /set hypervisordebugport 1
bcdedit /set hypervisorbaudrate 115200
bcdedit /set hypervisordebug on
bcdedit /set hypervisorlaunchtype auto
```

**1394**  
Specifies an IEEE 1394 (FireWire) connection for debugging. When this option is used, the **hypervisorchannel** option should also be set.

**Net**  
Specifies an Ethernet network connection for debugging. When this option is used, the **hypervisorhostip** option must be also be set.

**hypervisorhostip** *IP address*
(Only used when the **hypervisordebugtype** is **Net**.) For debugging hypervisor over a network connection, specifies the IPv4 address of the host debugger. For information about debugging Hyper-V, see [Create a Virtual Machine with Hyper-V](https://docs.microsoft.com/virtualization/hyper-v-on-windows/quick-start/quick-create-virtual-machine).

> [!NOTE]
> The option is available starting in Windows 8 and Windows Server 2012.

**hypervisorhostport** \[ *port* \]  
(Only used when the **hypervisordebugtype** is **Net**.) For network debugging, specifies the port to communicate with on the host debugger. Should be 49152 or higher.

> [!NOTE]
> The option is available starting in Windows 8 and Windows Server 2012.

**hypervisordhcp** \[ **yes** | **no** \]  
Controls use of DHCP by the network debugger used with the hypervisor. Setting this to **no** forces the use of Automatic Private IP Addressing (APIPA) to obtain a local link IP address.

> [!NOTE]
> The option is available starting in Windows 8 and Windows Server 2012.

**hypervisoriommupolicy** \[ **default** | **enable** | **disable**\]  
Controls whether the hypervisor uses an Input Output Memory Management Unit (IOMMU).

> [!NOTE]
> The option is available starting in Windows 8 and Windows Server 2012.

**hypervisorlaunchtype** \[ **Off** | **Auto** \]  
Controls the hypervisor launch options. If you are setting up a debugger to debug Hyper-V on a target computer, set this option to **Auto** on the target computer. For more information, see [Create a Virtual Machine with Hyper-V](https://docs.microsoft.com/virtualization/hyper-v-on-windows/quick-start/quick-create-virtual-machine).

**hypervisorloadoptions NOFORCESNOOP** \[ **Yes** | **No** \]  
Specifies whether the hypervisor should enforce snoop control on system IOMMUs.

**hypervisornumproc** *number*  
Specifies the total number of logical processors that can be started in the hypervisor.

> [!NOTE]
> The option is available starting in Windows 8 and Windows Server 2012.

**hypervisorrootproc** *number*  
Specifies the maximum number of virtual processors in the root partition and limits the number of post-split Non-Uniform Memory Architecture (NUMA) nodes which can have logical processors started in the hypervisor.

> [!NOTE]
> The option is available starting in Windows 8 and Windows Server 2012.

**hypervisorrootprocpernode** *number*  
Specifies the total number of virtual processors in the root partition that can be started within a pre-split Non-Uniform Memory Architecture (NUMA) node.

> [!NOTE]
> The option is available starting in Windows 8 and Windows Server 2012.

**hypervisorusekey** \[ *key* \]  
(Only used when the **hypervisordebugtype** is **Net**.) For network debugging specifies the key with which to encrypt the connection. \[0-9\] and \[a-z\] allowed only.

> [!NOTE]
> The option is available starting in Windows 8 and Windows Server 2012.

**hypervisoruselargevtlb** \[ **yes** | **no**
Increases virtual Translation Lookaside Buffer (TLB) size.

> [!NOTE]
> The option is available starting in Windows 8 and Windows Server 2012.

**increaseuserva** *Megabytes*
Specifies the amount of memory, in megabytes, for user-mode virtual address space.

On 32-bit editions of Windows, applications have 4 gigabyte (GB) of virtual address space available. The virtual address space is divided so that 2 GB is available to the application and the other 2 GB is available only to the system.

The 4-gigabyte tuning feature, enabled with the **increaseuserva** option, allows you to increase the virtual address space that is available to the application up to 3 GB, which reduces the amount available to the system to between 1 and 2 GB. The **BCEdit /set increaseuserva** *Megabytes* command can specify any value between 2048 (2 GB) and 3072 (3 GB) megabytes in decimal notation. Windows uses the remaining address space (4 GB minus the specified amount) as its kernel-mode address space.

See [4-Gigabyte Tuning (Windows)](https://docs.microsoft.com/windows/desktop/Memory/4-gigabyte-tuning) for additional information about this feature.

**kernel** *file*
Directs the operating system loader to load an alternate kernel. The specified file must be located in the %SystemRoot%\\system32 directory.

**loadoptions busparams**=*Bus.Device.Function*
Specifies the target controller when multiple controllers exist. This syntax is appropriate when using either a 1394 cable or a USB 2.0 debug cable for debugging. *Bus* specifies the bus number, *Device* specifies the device number, and *Function* specifies the function number.

> [!NOTE]
> For 1394 debugging, the bus parameters must be specified in decimal, regardless of which version of Windows is being configured. The format of the bus parameters used for USB 2.0 debugging depends on the Windows version. In Windows Server 2008, the USB 2.0 bus parameters must be specified in hexadecimal. In Windows 7 and Windows Server 2008 R2 and later versions of Windows, the USB 2.0 bus parameters must be specified in decimal.

**maxgroup** \[ **on** | **off** \]  
Maximizes the number of groups created in a processor group configuration.

The **maxgroup on** setting assigns NUMA nodes to groups in a manner that maximizes the number of groups for a particular computer. The number of groups created is either the number of NUMA nodes the computer has, or the maximum number of groups supported by this version of Windows, whichever is smaller. The default behavior (**maxgroup off)** is to pack the NUMA nodes tightly into as few groups as possible.

Use this option if you want to use multiple groups, the computer has 64 or fewer active logical processors, and the computer already has multiple NUMA nodes. This option can also be used to alter the default group configuration of a computer that has more than 64 logical processors.

[Processor groups](https://docs.microsoft.com/windows/desktop/ProcThread/processor-groups) provide support for computers with greater than 64 logical processors. This option is available on 64-bit versions of Windows 7 and Windows Server 2008 R2 and later versions. This boot option has no effect on the 32-bit versions of Windows 7.

For more information about using this option, see [Boot Parameters to Test Drivers for Multiple Processor Group Support](boot-parameters-to-test-drivers-for-multiple-processor-group-support.md).

**nointegritychecks** \[ **on** | **off** \]
Disables integrity checks. Cannot be set when secure boot is enabled. This value is ignored by Windows 7 and Windows 8.

**nolowmem** \[ **on** | **off** \]
Controls the use of low memory. When **nolowmem on** is specified, this option loads the operating system, device drivers, and all applications into addresses above the 4 GB boundary, and directs Windows to allocate all memory pools at addresses above the 4 GB boundary. Note that the **nolowmem** option is ignored in Windows 8, Windows Server 2012, and later versions of Windows.

**novesa** \[ **on** | **off** \]
Indicates whether the VGA driver should avoid VESA BIOS calls. The option is ignored in Windows 8 and Windows Server 2012.

**novga** \[ **on** | **off** \]
Disables the use of VGA modes in the OS. The option is available starting in Windows 8 and Windows Server 2012.

**nx** \[**Optin |OptOut | AlwaysOn |AlwaysOff**\]  
Enables, disables, and configures Data Execution Prevention (DEP), a set of hardware and software technologies designed to prevent harmful code from running in protected memory locations. For information about DEP settings, see [Data Execution Prevention](https://docs.microsoft.com/windows/desktop/Memory/data-execution-prevention).

**Optin**  
Enables DEP only for operating system components, including the Windows kernel and drivers. Administrators can enable DEP on selected executable files by using the Application Compatibility Toolkit (ACT).

**Optout**  
Enables DEP for the operating system and all processes, including the Windows kernel and drivers. However, administrators can disable DEP on selected executable files by using **System** in **Control Panel**.

**AlwaysOn**  
Enables DEP for the operating system and all processes, including the Windows kernel and drivers. All attempts to disable DEP are ignored.

**AlwaysOff**  
Disables DEP. Attempts to enable DEP selectively are ignored.

On Windows Vista, this parameter also disables Physical Address Extension (PAE). This parameter does not disable PAE on Windows Server 2008.

**onecpu** \[ **on** | **off** \]  
Forces only the boot CPU to be used in a computer that has more than one logical processor.

For example, the following command configures the current operating system loader to use one processor.

```syntax
bcdedit /set onecpu on
```

**onetimeadvancedoptions** \[ **on** | **off** \]  
Controls whether the system boots to the legacy menu (F8 menu) on the next boot.

> [!NOTE]
> The option is available starting in Windows 8 and Windows Server 2012.

```syntax
bcdedit /set {current} onetimeadvancedoptions on
```

**pae** \[ **Default** | **ForceEnable** | **ForceDisable** \]  
Enables or disables Physical Address Extension (PAE). When PAE is enabled, the system loads the PAE version of the Windows kernel.

The **pae** parameter is valid only on boot entries for 32-bit versions of Windows that run on computers with x86-based and x64-based processors. On 32-bit versions of Windows (prior to Windows 8) , PAE is disabled by default. However, Windows automatically enables PAE when the computer is configured for hot-add memory devices in memory ranges beyond the 4 GB region, as defined by the Static Resource Affinity Table (SRAT). *Hot-add memory* supports memory devices that you can add without rebooting or turning off the computer. In this case, because PAE must be enabled when the system starts, it is enabled automatically so that the system can immediately address extended memory that is added between restarts. Hot-add memory is supported only on Windows Server 2008, Datacenter Edition; Windows Server 2008 for Itanium-Based Systems; and on the datacenter and enterprise editions of all later versions of Windows Server. Moreover, for versions of Windows prior to Windows Server 2008, hot-add memory is supported only on computers with an ACPI BIOS, an x86 processor, and specialized hardware. For Windows Server 2008 and later versions of Windows Server, it is supported for all processor architectures.

On a computer that supports hardware-enabled Data Execution Prevention (DEP) and is running a 32-bit version of the Windows operating system that supports DEP, PAE is automatically enabled when DEP is enabled and, on all 32-bit versions of the Windows operating system, except Windows Server 2003 with SP1, PAE is disabled when you disable DEP. To enable PAE when DEP is disabled, you must enable PAE explicitly, by using **/set nx AlwaysOff** and **/set pae ForceEnable**. For more information about DEP, see [Boot Parameters to Configure DEP and PAE](https://msdn.microsoft.com/library/windows/hardware/ff542275).

For more information about using the **pae** parameter and the other parameters that affect PAE configuration, see [Boot Parameters to Configure DEP and PAE](https://msdn.microsoft.com/library/windows/hardware/ff542275).

**pciexpress** \[ **default** | **forcedisable**\]  
Enables or disables PCI Express functionality. If the computer platform supports the PCI Express features and the ACPI \_OSC method grants control of the features to the operating system, Windows enables the advanced features through the PCI Express Native Control feature (this is the default). Use the **forcedisable** option to override the advanced PCI Express features and use legacy PCI Express behavior. For more information, see [Enabling PCI Express Native Control in Windows](https://msdn.microsoft.com/library/windows/hardware/gg487424.aspx).

**quietboot** \[ **on** | **off** \]  
Controls the display of a high-resolution bitmap in place of the Windows boot screen display and animation. In operating systems prior to Windows Vista, the **/noguiboot** serves a similar function.

> [!NOTE]
> Do not use the **quietboot** option in Windows 8 as it will prevent the display of bug check data in addition to all boot graphics.

**removememory** *Megabytes*
Removes memory from the total available memory that the operating system can use.

For example, the following command removes 256 MB of memory from the total available to the operating system associated with the specified boot entry.

``` syntax
bcdedit /set {49916baf-0e08-11db-9af4-000bdbd316a0} removememory 256
```

**sos** \[ **on** | **off** \]  
Controls the display of the names of the drivers as they load during the boot process. Use **sos on** to display the names. Use **sos off** to suppress the display.

**testsigning** \[ **on** | **off** \]  
Controls whether Windows 10, Windows 8.1, Windows 8, Windows 7, Windows Server 2008, or Windows Vista will load any type of test-signed kernel-mode code. This option is not set by default, which means test-signed kernel-mode drivers on 64-bit versions of Windows 10, Windows 8.1, Windows 8, Windows 7, Windows Server 2008, and Windows Vista will not load by default. After you run the BCDEdit command, restart the computer so that the change takes effect. For more information, see [Introduction to Test-Signing](https://msdn.microsoft.com/library/windows/hardware/ff547660).

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

**tpmbootentropy** \[ **default** | **ForceEnable** | **ForceDisable**\]  
Determines whether entropy is gathered from the trusted platform module (TPM) to help seed the random number generator in the operating system.

**truncatememory** *address*
Limits the amount of physical memory available to Windows. When you use this option, Windows ignores all memory at or above the specified physical address. Specify the *address* in bytes.

For example, the following command sets the physical address limit at 1 GB. You can specify the address in decimal (1073741824) or hexadecimal (0x40000000).

``` syntax
bcdedit /set {49916baf-0e08-11db-9af4-000bdbd316a0} truncatememory 0x40000000
```

**tscsyncpolicy** \[ **Default** | **Legacy** | **Enhanced** \]  
Controls the times stamp counter synchronization policy. This option should only be used for debugging.

> [!NOTE]
> The option is available starting in Windows 8 and Windows Server 2012.

**usefirmwarepcisettings** \[ **yes** | **no** \]  
Enables or disables the use of BIOS-configured peripheral component interconnect (PCI) resources.

**useplatformclock** \[ **yes** | **no** \]  
Forces the use of the platform clock as the system's performance counter.

> [!NOTE]
> This option should only be used for debugging.

**uselegacyapicmode** \[ **yes** | **no** \]  
Used to force legacy APIC mode, even if the processors and chipset support extended APIC mode.

**useplatformtick** \[ **yes** | **no** \]  
Forces the clock to be backed by a platform source, no synthetic timers are allowed. The option is available starting in Windows 8 and Windows Server 2012.

> [!NOTE]
> This option should only be used for debugging.

**vga** \[ **on** | **off** \]  
Forces the use of a safe resolution. For example, on a computer running Windows 7, this option forces the use of 640x480 resolution. On a computer running Windows 8, this option forces the use of 800x600 resolution if it is available, or 640x480 if not.

**xsavedisable** \[ **0** | **1** \]  
When set to a value other than zero (0), disables XSAVE processor functionality in the kernel.

**x2apicpolicy** \[ **enable** | **disable** \]  
Enables or disables the use of extended APIC mode, if supported. The system defaults to using extended APIC mode if it is available.

### Comments

For more information about specific BCD elements and boot options, you can use the commands **BCDEdit /? OSLOADER** and **BCDEdit /? TYPES OSLOADER**.

To view the current boot entries and their settings, use the **bcdedit /enum** command. This command displays the active boot entries and their associated globally unique identifiers (GUID). Use the identifiers with the **/set** command to configure options for a specific boot entry.

To delete a boot option value that you have set, use the **/deletevalue** option. The syntax for the command is as follows:

**bcdedit** /**deletevalue** \[**{ID}**\] *datatatype*

For example, if you change the processor group option, **groupsize**, to a new value for testing purposes, you can revert to the default value of 64 by typing the following command and then restarting the computer.

``` syntax
bcdedit /deletevalue groupsize
```

Any change to a boot option requires a restart to take effect. For information about commonly used BCDEdit commands, see [Boot Configuration Data Editor Frequently Asked Questions](http://go.microsoft.com/fwlink/p/?linkid=155086).

## Requirements

|||
|----|----|
|Minimum supported client|Windows Vista|
|Minimum supported server|Windows Server 2008|
|||

## See also

- [BCDEdit /deletevalue](bcdedit--deletevalue.md)
