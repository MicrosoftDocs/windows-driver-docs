---
title: Option File Fields
description: Option File Fields
ms.assetid: 5ca79c91-5d19-4393-aa5e-be3d47e62967
keywords: ["options files WDK Static Driver Verifier", "fields WDK Static Driver Verifier"]
---

# Option File Fields


An SDV Options file contains the SDV settings. Some of these settings you can change. Other settings are reserved by SDV.

The fields in the options file that you can change include the following:

<span id="SDV_SlamConfig_Maximum_Driver_Size"></span><span id="sdv_slamconfig_maximum_driver_size"></span><span id="SDV_SLAMCONFIG_MAXIMUM_DRIVER_SIZE"></span>**SDV\_SlamConfig\_Maximum\_Driver\_Size**  
Specifies the maximum size of a driver that SDV will support (in terms of lines of code). The default value is 100K lines of code.

<span id="SDV_SlamConfig_Timeout"></span><span id="sdv_slamconfig_timeout"></span><span id="SDV_SLAMCONFIG_TIMEOUT"></span>**SDV\_SlamConfig\_Timeout**  
Limits the time SDV can spend verifying each rule. The value of this entry is an integer that represents a number of seconds. The minimum value is 10, the maximum value is 86400, and the default value is 2000 (33.34 minutes).

If SDV exceeds the per-rule time limit while verifying a rule, it terminates the verification and reports a **Timeout** in the [command-line output](command-line-output.md) and in Static Driver Verifier under the Results section on the **Main** tab.

<span id="SDV_SlamConfig_Spaceout"></span><span id="sdv_slamconfig_spaceout"></span><span id="SDV_SLAMCONFIG_SPACEOUT"></span>**SDV\_SlamConfig\_Spaceout**  
Limits the amount of virtual memory that SDV can consume when verifying each rule. The value of this entry is an integer in megabyte (MB) units. The minimum value is 100, the maximum value is 2000 (2 gigabytes (GB), and the default value is 400.

If SDV exceeds the virtual memory limit while verifying a rule, it terminates the verification and reports a **Spaceout** in the [command-line output](command-line-output.md) and in Static Driver Verifier under the Results section on the **Main** tab.

If SDV reports a **Spaceout**, consider increasing the value of **SDV\_SlamConfig\_Spaceout**, stopping all other processes on the computer while SDV is running, or moving SDV to a computer with more memory. The optimal value for a system is approximately 200 MB less than the amount of physical memory on the system.

<span id="SDV_SlamConfig_NumberOfThreads"></span><span id="sdv_slamconfig_numberofthreads"></span><span id="SDV_SLAMCONFIG_NUMBEROFTHREADS"></span>**SDV\_SlamConfig\_NumberOfThreads**  
Sets the number of threads to use during a verification. If the value is 0, this limits the number of threads to the number of processors on the computer (this includes hyper-threaded processors). If the value is set to a number greater than 0, the value specifies the number of threads that SDV can use during the verification. Increasing the number of threads might increase the run time performance of SDV, but it might also increase the number of time outs that occur. The default value is 0. If you are running SDV on a multiprocessor computer that uses the default value, SDV will automatically take advantage of the additional processors.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Option%20File%20Fields%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




