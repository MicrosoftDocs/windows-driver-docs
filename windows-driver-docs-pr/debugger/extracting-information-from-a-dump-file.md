---
title: Extracting Information from a Dump File
description: Extracting Information from a Dump File
ms.assetid: abde266e-e3ab-4e5e-ac6d-a27933f3d1a9
keywords: ["extracting information from a dump file", "dump file, extracting various information", "machine name (determining from a dump file)", "computer name (determining from a dump file)", "IP address (determining from a dump file)"]
---

# Extracting Information from a Dump File


## <span id="ddk_extracting_information_from_a_dump_file_dbg"></span><span id="DDK_EXTRACTING_INFORMATION_FROM_A_DUMP_FILE_DBG"></span>


Certain kinds of information, such as the name of the target computer, are easily available during live debugging. When debugging a dump file it takes a little more work to determine this information.

### <span id="finding_the_computer_name_in_a_kernel_mode_dump_file"></span><span id="FINDING_THE_COMPUTER_NAME_IN_A_KERNEL_MODE_DUMP_FILE"></span>Finding the Computer Name in a Kernel-Mode Dump File

If you need to determine the name of the computer on which the crash dump was made, you can use the [**!peb**](https://msdn.microsoft.com/library/windows/hardware/ff564670) extension and look for the value of COMPUTERNAME it its output.

Or you can use the following command:

``` syntax
0: kd> x srv!SrvComputerName
be8ce2e8  srv!SrvComputerName  = _UNICODE_STRING "AIGM-MYCOMP-PUB01"
```

### <span id="finding_the_ip_address_in_a_kernel_mode_dump_file"></span><span id="FINDING_THE_IP_ADDRESS_IN_A_KERNEL_MODE_DUMP_FILE"></span>Finding the IP Address in a Kernel-Mode Dump File

To determine the IP address of the computer on which the crash dump was made, find a thread stack that shows some send/receive network activity. Open one of the send packets or receive packets. The IP address will be visible in that packet.

### <span id="finding_the_process_id_in_a_user_mode_dump_file"></span><span id="FINDING_THE_PROCESS_ID_IN_A_USER_MODE_DUMP_FILE"></span>Finding the Process ID in a User-Mode Dump File

To determine the process ID of the target application from a user-mode dump file, use the [**| (Process Status)**](https://msdn.microsoft.com/library/windows/hardware/ff566242) command. This will display all the processes being debugged at the time the dump was written. The process marked with a period (**.**) is the current process. Its process ID is given in hexadecimal after the **id:** notation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Extracting%20Information%20from%20a%20Dump%20File%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




