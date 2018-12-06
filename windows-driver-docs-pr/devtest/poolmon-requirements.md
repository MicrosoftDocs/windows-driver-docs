---
title: PoolMon Requirements
description: PoolMon Requirements
ms.assetid: 5ee1ed1c-5392-4ce4-8edb-e600b93f82d7
keywords:
- PoolMon WDK , requirements
- Memory Pool Monitor WDK , requirements
- PoolMon WDK , displays
- Memory Pool Monitor WDK , displays
- files WDK PoolMon
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PoolMon Requirements


## <span id="ddk_poolmon_requirements_tools"></span><span id="DDK_POOLMON_REQUIREMENTS_TOOLS"></span>


PoolMon requires the following system configuration, permissions, and files.

### <span id="System_Requirements"></span><span id="system_requirements"></span><span id="SYSTEM_REQUIREMENTS"></span>System Requirements

The version of PoolMon included in the Windows Driver Kit (WDK) and described in this document runs only on Microsoft Windows XP and later versions of Windows.

### <span id="Pool_Tagging_Requirement"></span><span id="pool_tagging_requirement"></span><span id="POOL_TAGGING_REQUIREMENT"></span>Pool Tagging Requirement

Before running any version of PoolMon on Windows XP or earlier versions of Windows, you must enable pool tagging. Pool tagging is permanently enabled on Windows Server 2003 and later versions of Windows.

The pool tagging feature collects and calculates statistics about pool memory sorted by the tag value of the allocation.

To enable pool tagging, use GFlags, a tool included in Debugging Tools for Windows. Open the **Global Flags** dialog box, check the **Enable Pool Tagging** check box, and then restart the computer.

### <span id="Requirements_for_Terminal_Services_Session_Pool_Monitoring"></span><span id="requirements_for_terminal_services_session_pool_monitoring"></span><span id="REQUIREMENTS_FOR_TERMINAL_SERVICES_SESSION_POOL_MONITORING"></span>Requirements for Terminal Services Session Pool Monitoring

PoolMon displays allocations from the Terminal Services session pools only on Windows Server 2003 and later versions of Windows.

Windows allocates memory from Terminal Services session pools only when the computer is configured as a Terminal Server. On Terminal Servers, the kernel-mode portions of the Win32 subsystem allocate memory from the session pools. Otherwise, Windows allocates pool memory for Terminal Services from the system pool.

### <span id="Requirements_for_Generating_a_Local_Tag_File"></span><span id="requirements_for_generating_a_local_tag_file"></span><span id="REQUIREMENTS_FOR_GENERATING_A_LOCAL_TAG_FILE"></span>Requirements for Generating a Local Tag File

The **/c** parameter, which creates a localtag.txt file of pool tags used by drivers on the local machine, is supported only on 32-bit versions of Windows.

### <span id="Display_Requirements"></span><span id="display_requirements"></span><span id="DISPLAY_REQUIREMENTS"></span>Display Requirements

To see the entire PoolMon display, the Command Prompt window size must be at least 80 characters wide (width=80) and at least 53 rows high (height=53), and the Command Prompt window buffer must be at least 500 characters wide (width=500) and at least 2000 rows high (height=2000). Otherwise, the display might be truncated.

### <span id="Required_Files"></span><span id="required_files"></span><span id="REQUIRED_FILES"></span>Required Files

poolmon.exe

msdis130.dll

msvcp70.dll

msvcr70.dll

pooltag.txt

 

 





