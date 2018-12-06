---
title: Boot Parameters to Test Drivers for Multiple Processor Group Support
description: Boot Parameters to Test Drivers for Multiple Processor Group Support
ms.assetid: 8ce311d6-a182-4d04-a453-81f6abe2043b
ms.date: 05/08/2018
ms.localizationpriority: medium
---

# Boot Parameters to Test Drivers for Multiple Processor Group Support


Windows 7 and Windows Server 2008 R2 provide support for computers with more than 64 processors. This support is made possible by introducing [Processor groups](http://go.microsoft.com/fwlink/p/?linkid=155063). For testing purposes, you can configure any computer that has multiple logical processors to have multiple processor groups by limiting the group size. This means you can test drivers and components for multiple processor group compatibility on computers that have 64 or fewer logical processors.

**Note**   The concept of *processor groups*, introduced with Windows 7, allows existing APIs and DDIs to continue to work on computers with more than 64 logical processors. Typically, a group's processors are represented by an affinity mask, which is 64 bits long. Any computer with more than 64 logical processors will necessarily have more than one group.
When a process is created, the process is assigned to a specific group. By default, threads of the process can run on all logical processors of the same group, although the thread affinity can be explicitly changed. Calls to any API or DDI that takes an affinity mask or processor number as an argument, but not a group number, is limited to affecting or reporting on those processors in the calling thread's group. The same is true of APIs or DDIs that return an affinity mask or processor number, like **GetSystemInfo**.

Starting with Windows 7, an application or driver can make use of functions that extend the legacy APIs. These new group-aware functions accept a group number argument to unambiguously qualify a processor number or affinity mask, and therefore can manipulate processors outside of the calling thread's group. The interaction between drivers and components running in different groups within a computer introduces the potential for bugs when legacy APIs or DDIs are involved. You can use the legacy non-group-aware APIs on Windows 7 and Windows Server 2008 R2. However, driver requirements are more stringent. For functional correctness of drivers on computers that have more than one processor group, you must replace any DDI that either accepts a processor number or mask as a parameter without an accompanying processor group or returns a processor number or mask without an accompanying processor group. These legacy non-group-aware DDIs can perform erratically on a computer that has multiple process groups because the inferred group may be different than what the calling thread intended. Therefore, drivers that use these legacy DDIs and are targeted for Windows Server 2008 R2 must be updated to use the new extended versions of the interfaces. Drivers that do not call any functions that use processor affinity masks or processor numbers will operate correctly, regardless of the number of processors. Drivers that call the new DDIs can run on previous versions of Windows by including the procgrp.h header, calling [**WdmlibProcgrpInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff565629), and linking against the [Processor Group Compatibility Library](https://msdn.microsoft.com/library/windows/hardware/ff559909) (procgrp.lib).

For more information on the new group-aware APIs and DDIs, download the white paper [Supporting System that Have More than 64 Logical Processors: Guideline for Developers](http://go.microsoft.com/fwlink/p/?linkid=147914).

 

To help identify potential processor group-related problems in drivers and components, you can use the [**BCDEdit /set**](https://msdn.microsoft.com/library/windows/hardware/ff542202) options. The two BCD boot configuration settings, **groupsize** and **maxgroup**, can configure any computer that has multiple logical processors to support multiple processor groups. The **groupaware** option modifies the behavior of certain DDIs and manipulates the group environment for testing purposes.

### <span id="create_multiple_processor_groups_by_changing_the_group_size"></span><span id="CREATE_MULTIPLE_PROCESSOR_GROUPS_BY_CHANGING_THE_GROUP_SIZE"></span>Create Multiple Processor Groups by Changing the Group Size

The **groupsize** option specifies the maximum number of logical processors in a group. By default, the **groupsize** option is not set, and any computer with 64 or fewer logical processors has one group, which is group 0.

**Note**   A physical processor, or processor package, can have one or more cores, or processor units, each of which can contain one or more logical processors. The operating system considers a logical processor as one logical computing engine.

 

To create multiple processor groups, run [**BCDEdit /set**](https://msdn.microsoft.com/library/windows/hardware/ff542202) in an elevated Command Prompt window and specify a new *maxsize* value for **groupsize** that is less than the total number of logical processors. Note that the group size setting is for testing and you should not configure shipping systems with this setting. The *maxsize* value can be set to any power of 2 between 1 and 64 inclusive. The command uses the following syntax:

```
bcdedit.exe /set groupsize maxsize
```

For example, the following command sets the maximum number of processors in a group to 2.

```
bcdedit.exe /set groupsize 2
```

If a non-NUMA computer has 8 logical processors, setting the **groupsize** to 2 creates 4 processor groups with 2 logical processors each.

Group 0: 1 NUMA node containing 1 package of 2 logical processors

Group 1: 1 NUMA node containing 1 package of 2 logical processors

Group 2: 1 NUMA node containing 1 package of 2 logical processors

Group 3: 1 NUMA node containing 1 package of 2 logical processors

By design, a non-NUMA computer is considered to have one NUMA node. Because NUMA nodes cannot span groups, the system creates a node for each group after you restart the computer.

If **groupsize** is set to a value less than the number of logical processors in a physical processor package (socket), the system redefines its concept of a package upon restart such that the package does not span a group. This means that more packages than that are actually present are reported by processor topology APIs. This also means that the Windows (package-level) processor licensing limits might prevent some processor packages from starting when **groupsize** is set.

A processor package can span groups if it has multiple NUMA nodes defined within it and the system assigns these nodes to different groups.

Windows limits the number of groups supported. This number could change with new versions of Windows or in service pack releases. Drivers or components should not depend on the number of groups Windows supports as being constant. The limit on the number of groups could restrict the number of logical processors allowed to start when small values are used for the **groupsize** boot option.

To remove the **groupsize** setting you used for testing and return to the default setting of 64 logical processors per group, use the following BCDEdit command.

```
bcdedit.exe /deletevalue groupsize
```

This command is the equivalent of setting **groupsize** to 64.

### <span id="maximize_the_number_of_processor_groups"></span><span id="MAXIMIZE_THE_NUMBER_OF_PROCESSOR_GROUPS"></span>Maximize the Number of Processor Groups

The **maxgroup** option is another way to create processor groups on a computer with multiple logical processors and NUMA nodes. The **maxgroup** boot option has no effect on non-NUMA computers.

To maximize the number of groups, run the [**BCDEdit /set**](https://msdn.microsoft.com/library/windows/hardware/ff542202) command in an elevated Command Prompt window. The command uses the following syntax:

```
bcdedit.exe /set maxgroup on
```

For example, consider a computer that has 2 NUMA nodes, 1 processor package per node, and 4 processor cores per package, for a total of 8 logical processors.

The default group configuration is:

Group 0: 8 logical processors, 2 packages, 2 NUMA nodes

If you enter a **bcdedt.exe /set maxgroup on** command followed by a restart, the command yields the following group configuration:

Group 0: 4 logical processors, 1 package, 1 NUMA node

Group 1: 4 logical processors, 1 package, 1 NUMA node

Note that NUMA nodes are assigned to groups in a manner that maximizes the number of groups.

To change back to the default the setting, use the following **BCDEdit** command.

```
bcdedit.exe /set maxgroup off
```

### <span id="test_multiple_group_compatibility_by_setting_the_group_aware_boot_opti"></span><span id="TEST_MULTIPLE_GROUP_COMPATIBILITY_BY_SETTING_THE_GROUP_AWARE_BOOT_OPTI"></span>Test Multiple-Group Compatibility by Setting the Group Aware Boot Option

Windows 7 and Windows Server 2008 R2 have introduced a new BCD option (**groupaware**) that forces drivers and components to be aware of multiple groups in a multiple processor group environment. The **groupaware** option changes the behavior of a set of device driver functions to help expose cross-group incompatibilities in drivers and components. You can use the **groupaware** boot option along with the **groupsize** and **maxgroup** options to test driver compatibility with multiple groups when a computer has 64 or fewer active logical processors.

When the **groupaware** boot option is set, the operating system ensures that processes are started in a group other than group 0. This increases the chances of cross-group interaction between drivers and components. The option also modifies the behavior of the legacy functions that are not group-aware, **KeSetTargetProcessorDpc**, **KeSetSystemAffinityThreadEx**, and **KeRevertToUserAffinityThreadEx**, so that they always operate on the highest numbered group that contains active logical processors. Drivers that call any of these legacy functions should be changed to call their group-aware counterparts (**KeSetTargetProcessorDpcEx**, **KeSetSystemGroupAffinityThread**, and **KeRevertToUserGroupAffinityThread**),

To test for compatibility, use the following [**BCDEdit /set**](https://msdn.microsoft.com/library/windows/hardware/ff542202) command.

```
bcdedit.exe /set groupaware on
```

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Legacy non-group aware functions</th>
<th align="left">Windows 7 group-aware replacement</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>KeSetTargetProcessorDpc</p></td>
<td align="left"><p>KeSetTargetProcessorDpcEx</p></td>
</tr>
<tr class="even">
<td align="left"><p>KeSetSystemAffinityThreadEx</p></td>
<td align="left"><p>KeSetSystemGroupAffinityThread</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KeRevertToUserAffinityThreadEx</p></td>
<td align="left"><p>KeRevertToUserGroupAffinityThread</p></td>
</tr>
</tbody>
</table>

 

To reset the computer to the default setting, use the following **BCDEdit** command.

```
bcdedit.exe /set groupaware off
```

 

 





