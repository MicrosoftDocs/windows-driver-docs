---
title: Boot Parameters to Manipulate Memory
description: Boot Parameters to Manipulate Memory
keywords:
- memory-related boot options WDK
- boot parameters WDK
- boot entry parameters WDK
- manipulating memory WDK boot parameters
- low-memory environments WDK boot parameters
- simulating low-memory environments WDK boot parameters
- memory WDK boot parameters
ms.date: 07/19/2024
ms.topic: reference
---

# Boot Parameters to Manipulate Memory

You can simulate a low-memory environment for testing without changing the amount of physical memory on the computer. Instead, you can limit the memory available to the operating system by using **truncatememory** or **removememory** options with the [**BCDedit /set**](./bcdedit--set.md) command.

The **truncatememory** or **removememory** options are available in Windows 7 and later.

- The **truncatememory** option disregards all memory at or above the specified physical address.

- The **removememory** option reduces memory available to Windows by the specified amount (measured in MB). Both options reduce memory, but the **removememory** option is better at restricting the operating system to use the specified memory while accounting for memory gaps. Because of this, the use of **removememory** is recommended.

## Boot Parameters to Simulate a Low Memory Environment in Windows

To simulate a low memory environment, use the [**BCDedit /set**](./bcdedit--set.md) command and the **removememory** option to modify a boot entry. Set the value of **removememory** to the amount of physical memory on the system minus the desired memory size for this test.

For example, to limit the memory of a computer with 2 GB of physical memory to a maximum of 512 MB of available memory, set the value of the **removememory** parameter to 1536 (2 GB (2048 MB) - 512 MB = 1536 MB).

The following example shows a BCDEdit command used to remove 1536 MB of memory from the total available to the system for the specified boot entry.

In this example `bcdedit /enum`  was used to determine the BCD data store GUID is `{18b123cd-2bf6-11db-bfae-00e018e2b8db}`. For information on specifying a specific boot entry, or working with the default boot entry, see [Editing Boot Options](editing-boot-options.md).

```txt
bcdedit /set {18b123cd-2bf6-11db-bfae-00e018e2b8db} removememory 1536
```

You can also use the **truncatememory** option with the **bcdedit /set** command to achieve the same result. When you use this option, Windows ignores all memory at or above the specified physical address. Specify the *address* in bytes. For example, the following command sets the physical address limit at 1 GB for the specified boot entry. You can specify the address in decimal (1073741824) or hexadecimal (0x40000000).

```txt
bcdedit /set {18b123cd-2bf6-11db-bfae-00e018e2b8db} truncatememory 0x40000000
```

After rebooting, use a utility such as [systeminfo](/windows-server/administration/windows-commands/systeminfo) to confirm the amount of available memory.

When you are finished testing, you can remove the **removememory** and **truncatememory** boot entry options using the [**BCDEdit /deletevalue**](./bcdedit--deletevalue.md) command.

## Related topics

- [Editing Boot Options](editing-boot-options.md)
- [Using Boot Parameters](using-boot-parameters.md)
- [BCD Edit Options Reference](bcd-boot-options-reference.md)
