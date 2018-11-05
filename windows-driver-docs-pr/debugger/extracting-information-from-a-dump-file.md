---
title: Extracting Information from a Dump File
description: Extracting Information from a Dump File
ms.assetid: abde266e-e3ab-4e5e-ac6d-a27933f3d1a9
keywords: ["extracting information from a dump file", "dump file, extracting various information", "machine name (determining from a dump file)", "computer name (determining from a dump file)", "IP address (determining from a dump file)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Extracting Information from a Dump File


## <span id="ddk_extracting_information_from_a_dump_file_dbg"></span><span id="DDK_EXTRACTING_INFORMATION_FROM_A_DUMP_FILE_DBG"></span>


Certain kinds of information, such as the name of the target computer, are easily available during live debugging. When debugging a dump file it takes a little more work to determine this information.

### <span id="finding_the_computer_name_in_a_kernel_mode_dump_file"></span><span id="FINDING_THE_COMPUTER_NAME_IN_A_KERNEL_MODE_DUMP_FILE"></span>Finding the Computer Name in a Kernel-Mode Dump File

If you need to determine the name of the computer on which the crash dump was made, you can use the [**!peb**](-peb.md) extension and look for the value of COMPUTERNAME it its output.

Or you can use the following command:

```dbgcmd
0: kd> x srv!SrvComputerName
be8ce2e8  srv!SrvComputerName  = _UNICODE_STRING "AIGM-MYCOMP-PUB01"
```

### <span id="finding_the_ip_address_in_a_kernel_mode_dump_file"></span><span id="FINDING_THE_IP_ADDRESS_IN_A_KERNEL_MODE_DUMP_FILE"></span>Finding the IP Address in a Kernel-Mode Dump File

To determine the IP address of the computer on which the crash dump was made, find a thread stack that shows some send/receive network activity. Open one of the send packets or receive packets. The IP address will be visible in that packet.

### <span id="finding_the_process_id_in_a_user_mode_dump_file"></span><span id="FINDING_THE_PROCESS_ID_IN_A_USER_MODE_DUMP_FILE"></span>Finding the Process ID in a User-Mode Dump File

To determine the process ID of the target application from a user-mode dump file, use the [**| (Process Status)**](---process-status-.md) command. This will display all the processes being debugged at the time the dump was written. The process marked with a period (**.**) is the current process. Its process ID is given in hexadecimal after the **id:** notation.

 

 





