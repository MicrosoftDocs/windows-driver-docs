---
title: PNPCPU General Commands
description: PNPCPU General Commands
ms.assetid: 8b98149c-6c5a-4c1f-b988-dce86bdc3e29
keywords:
- PNPCPU WDK , commands
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PNPCPU General Commands


The following syntax is common for all PNPCPU operations.

```
pnpcpu.exe -operation
```

### <span id="parameters"></span><span id="PARAMETERS"></span>Parameters

<span id="-install"></span><span id="-INSTALL"></span>**-install**  
Installs the tool on the local computer.

<span id="-uninstall"></span><span id="-UNINSTALL"></span>**-uninstall**  
Removes the tool from the local computer, and returns the computer to the state it was in before running **-install**.

This includes clearing all processor error codes that could be observed after the **-install** command was run and the system was restarted.

<span id="-add"></span><span id="-ADD"></span>**-add**  
Performs a hot-add operation on every logical processor in the system, up to the maximum supported by the license.

<span id="-__or_-help"></span><span id="-__OR_-HELP"></span>**-?** or **-help**  
Displays usage information similar to this documentation.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

There are no further optional parameters for any of the commands listed.

 

 





