---
title: Boot Parameters to Manipulate Memory
description: Boot Parameters to Manipulate Memory
ms.assetid: 04504216-20b5-4c65-a1e2-6eec7480ce17
keywords: ["memory-related boot options WDK", "boot parameters WDK", "boot entry parameters WDK", "manipulating memory WDK boot parameters", "low-memory environments WDK boot parameters", "simulating low-memory environments WDK boot parameters", "memory WDK boot parameters"]
---

# Boot Parameters to Manipulate Memory


## <span id="ddk_boot_parameters_to_manipulate_memory_tools"></span><span id="DDK_BOOT_PARAMETERS_TO_MANIPULATE_MEMORY_TOOLS"></span>


You can simulate a low-memory environment for testing without changing the amount of physical memory on the computer. Instead, you can limit the memory available to the operating system by using **truncatememory** or **removememory** options with the [**BCDedit /set**](https://msdn.microsoft.com/library/windows/hardware/ff542202) command.

The **/maxmem** parameter specifies the maximum amount of memory available to Windows. It is calibrated in megabytes (MB). Set the value to any amount less than the actual physical memory on the computer.

The **/maxmem** parameter actually determines the largest memory address available to Windows. Due to gaps in the mapping of physical memory, Windows might receive somewhat less memory than the value of **/maxmem**. For more precision, use **/burnmemory**.

The **truncatememory** or **removememory** options are available in Windows 7 and later. The **truncatememory** option disregards all memory at or above the specified physical address. The **removememory** option reduces memory available to Windows by the specified amount (measured in MB). Both options reduce memory, but the **removememory** option is better at restricting the operating system to use the specified memory while accounting for memory gaps.

### <span id="boot_parameters_to_test_in_a_low_memory_environment_in_windows_vista_a"></span><span id="BOOT_PARAMETERS_TO_TEST_IN_A_LOW_MEMORY_ENVIRONMENT_IN_WINDOWS_VISTA_A"></span>Boot Parameters to Test in a Low-memory Environment in Windows

To simulate a low-memory environment, use the [**BCDedit /set**](https://msdn.microsoft.com/library/windows/hardware/ff542202) command and the **removememory** option to modify a boot entry. Set the value of **removememory** to the amount of physical memory on the system minus the desired memory size for this test.

For example, to limit the memory of a computer with 2 GB of physical memory to a maximum of 512 MB of available memory, set the value of the **removememory** parameter to 1536 (2 GB (2048 MB) - 512 MB = 1536 MB).

The following example shows a BCDEdit command used to remove 1536 MB of memory from the total available to the system for the specified boot entry.

```
bcdedit /set {18b123cd-2bf6-11db-bfae-00e018e2b8db} removememory 1536
```

You can also use the **truncatememory** option with the **bcdedit /set** command to achieve the same result. When you use this option, Windows ignores all memory at or above the specified physical address. Specify the *address* in bytes. For example, the following command sets the physical address limit at 1 GB for the specified boot entry. You can specify the address in decimal (1073741824) or hexadecimal (0x40000000).

```
bcdedit /set {18b123cd-2bf6-11db-bfae-00e018e2b8db} truncatememory Ox40000000
```

Because the **removememory** option makes more efficient use of system memory, its use is recommended instead of **truncatememory**.

When you are finished testing, you can remove the **removememory** and **truncatememory** boot entry options using the [**BCDEdit /deletevalue**](https://msdn.microsoft.com/library/windows/hardware/jj856916) command.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Boot%20Parameters%20to%20Manipulate%20Memory%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




