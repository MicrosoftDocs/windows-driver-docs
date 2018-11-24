---
title: One-to-Many ID Mapping
description: One-to-Many ID Mapping
ms.assetid: 395d3f20-7410-496b-9ec3-1052cd731ae3
keywords:
- mapping network component IDs
- ID mapping WDK netmap.inf
- one-to-many ID mapping WDK networking
- preupgrade IDs WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# One-to-Many ID Mapping





**Note**  Vendor-supplied network upgrades are not supported in Microsoft Windows XP (SP1 and later), Microsoft Windows Server 2003, and later operating systems.

 

A one-to-many ID mapping maps a single preupgrade ID that represents more than one network adapter. The only way to differentiate the adapters associated with a single preupgrade ID is to inspect the values under the registry key that contains the parameter values for the network adapter instance.

An entry in an **OemAdapters** or **OemAsyncAdapters** section that specifies a one-to-many ID mapping has the following format:

*preupgrade-ID* = *mapping-method-number*, *section-name*

where:

*mapping-method-number* must be 0

*section-name* specifies a section in the netmap.inf file that contains the mapping information

The netmap.inf file section specified by *section-name* contains the following entries:

**ValueName = "**<em>Name</em>**"**

Specifies the value that NetSetup reads under the registry key that contains the parameter values for the network adapter instance. *Name* identifies a particular network adapter.

**ValueType =** *Type*

Specifies the registry value type for *ValueName*. *Type* is an integer that corresponds to a specific registry type.

*ValueName*= *postupgrade-ID*

*ValueName* is the value that NetSetup reads under the registry key that contains the parameter values for the network adapter instance. *postupgrade-ID* is the Windows 2000 or later device ID for the adapter. One *ValueName* entry should be provided for each adapter type that will be upgraded. If *ValueName* is set to the keyword **ValueNotPresent** and if NetSetup finds no parameters values for the adapter instance, NetSetup uses the *postuprgrade-ID* associated with **ValueNotPresent** for the adapter.

The following example shows a one-to-many device ID mapping:

```cpp
[OemAdapters]
DATAFIREU=0, DATAFIREU

[DATAFIREU]
ValueName  = "BoardType"
ValueType  = 1
DataFireIsaU = "DATAFIRE - ISA1U"
DataFireIsa1ST= "DATAFIRE - ISA1ST"
DataFireIsa4ST= "DATAFIRE - ISA4ST"
DataFireIsaGeneric = "ValueNotPresent"
```

The **OemAdapters** section in the above example contains a single entry that identifies the preupgrade device ID of the network adapter as DATAFIREU and specifies that the **DATAFIREU** section of the netmap.inf file contains the mapping information for this adapter.

The DATAFIREU section contains the following information:

-   The **ValueName** entry directs NetSetup to look for the **BoardType** value under the **Parameters** key of the network adapter instance.

-   The **ValueType** entry, which is set to 1, specifies that the **BoardType** value is a DWORD.

-   Each remaining value specifies a preupgrade device ID and a corresponding Windows 2000 or later ID. For example, the ID for the DataFireIsaU board type is DATAFIRE - ISA1U. The **ValueNotPresent** keyword can be specified instead of a preupgrade ID.

NetSetup performs a one-to-many ID mapping as follows:

1.  NetSetup reads the specified ValueName under the registry key that contains the parameter values for the network adapter instance.

2.  NetSetup attempts to match the ValueName with one of the ValueNames listed in the specified section of the netmap.inf file. If no ValueName is listed under the registry key, NetSetup attempts to find the ValueNotPresent keyword in the specified section of the netmap.inf file.

3.  If NetSetup finds a match, it installs the network adapter, using the INF file that has the same name as the mapped Windows 2000 or later ID.

If the registry keys or values for an adapter instance are identical for different adapter types, it is not possible to map a single preupgrade device ID to more than one Windows 2000 or later device ID without first modifying these registry keys or values.

The most effective way of handling this situation is as follows:

1.  The network migration DLL's [**PreUpgradeInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff562439) function modifies the registry so that the registry contains unique values for each instance of the network adapter. These unique values should indicate the adapter type.

2.  The **PreUpgradeInitialize** function sets the NUA\_REQUEST\_ABORT\_UPGRADE flag, which causes NetSetup to display a message that prompts the user to restart winnt32.exe and abort the upgrade.

3.  The user aborts the upgrade and then restarts winnt32.exe. The network migration DLL can now use the unique values to map the single preupgrade device ID to more than one Windows 2000 or later device ID.

 

 





