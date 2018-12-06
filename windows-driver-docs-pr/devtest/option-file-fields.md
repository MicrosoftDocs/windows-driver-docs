---
title: Option File Fields
description: Option File Fields
ms.assetid: 5ca79c91-5d19-4393-aa5e-be3d47e62967
keywords:
- options files WDK Static Driver Verifier
- fields WDK Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Option File Fields


An SDV Options file contains the SDV settings. Some of these settings you can change. Other settings are reserved by SDV.

The fields in the options file that you can change include the following:

<span id="SDV_SlamConfig_Maximum_Driver_Size"></span><span id="sdv_slamconfig_maximum_driver_size"></span><span id="SDV_SLAMCONFIG_MAXIMUM_DRIVER_SIZE"></span>**SDV\_SlamConfig\_Maximum\_Driver\_Size**  
Specifies the maximum size of a driver that SDV will support (in terms of lines of code). The default value is 100K lines of code.

<span id="SDV_SlamConfig_Timeout"></span><span id="sdv_slamconfig_timeout"></span><span id="SDV_SLAMCONFIG_TIMEOUT"></span>**SDV\_SlamConfig\_Timeout**  
Limits the time SDV can spend verifying each rule. The value of this entry is an integer that represents a number of seconds. The minimum value is 10, the maximum value is 86400, and the default value is 3000 (50 minutes).

If SDV exceeds the per-rule time limit while verifying a rule, it terminates the verification and reports a **Timeout** in the [command-line output](command-line-output.md) and in Static Driver Verifier under the Results section on the **Main** tab.

<span id="SDV_SlamConfig_Spaceout"></span><span id="sdv_slamconfig_spaceout"></span><span id="SDV_SLAMCONFIG_SPACEOUT"></span>**SDV\_SlamConfig\_Spaceout**  
Limits the amount of virtual memory that SDV can consume when verifying each rule. The value of this entry is an integer in megabyte (MB) units. The minimum value is 100, and the default value is 2500 MB (2.5 GB.)

If SDV exceeds the virtual memory limit while verifying a rule, it terminates the verification and reports a **Spaceout** in the [command-line output](command-line-output.md) and in Static Driver Verifier under the Results section on the **Main** tab.

If SDV reports a **Spaceout**, consider increasing the value of **SDV\_SlamConfig\_Spaceout**, stopping all other processes on the computer while SDV is running, or moving SDV to a computer with more memory. The optimal value for a system is approximately 200 MB less than the amount of physical memory on the system.

<span id="SDV_SlamConfig_NumberOfThreads"></span><span id="sdv_slamconfig_numberofthreads"></span><span id="SDV_SLAMCONFIG_NUMBEROFTHREADS"></span>**SDV\_SlamConfig\_NumberOfThreads**  
Sets the number of threads to use during a verification. If the value is 0, this limits the number of threads to the number of processors on the computer (this includes hyper-threaded processors). If the value is set to a number greater than 0, the value specifies the number of threads that SDV can use during the verification. Increasing the number of threads might increase the run time performance of SDV, but it might also increase the number of time outs that occur. The default value is 0. If you are running SDV on a multiprocessor computer that uses the default value, SDV will automatically take advantage of the additional processors.

 

 





