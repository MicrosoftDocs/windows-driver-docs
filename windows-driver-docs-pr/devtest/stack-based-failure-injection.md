---
title: Stack Based Failure Injection
description: The Stack Based Failure Injection option injects resource failures in kernel mode drivers.
ms.assetid: B5C06413-81FB-46DA-B053-80ED347DA3EB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stack Based Failure Injection


**Note**  The instructions to enable this feature only apply to the WDK for Windows 8. For Windows 8.1, this feature has been integrated into Driver Verifier. On computers running Windows 8.1, use the [Systematic low resources simulation](systematic-low-resource-simulation.md) option.

 

The Stack Based Failure Injection option injects resource failures in kernel mode drivers. This option uses a special driver, KmAutoFail.sys, in conjunction with [Driver Verifier](driver-verifier.md) to penetrate driver error handling paths. Testing these paths has historically been very difficult. The Stack Based Failure Injection option injects resource failures in a predictable manner, which makes the issues it finds reproducible. Because the error paths are easy to reproduce, it also makes it easy to verify fixes to these issues.

To help you determine the root cause of the error, a debugger extension is provided that can tell you exactly which failures have been injected and in what order.

When the Stack Based Failure Injection option is enabled on a specific driver, it intercepts some calls from that driver to the kernel and Ndis.sys. Stack Based Failure Injection looks at the call stack—specifically, at the portion of the call stack that comes from the driver it is enabled on. If this is the first time it has ever seen that stack, it will fail the call according to the semantics of that call. Otherwise, if it has seen that call before, it will pass it through untouched. Stack Based Failure Injection contains logic to deal with the fact that a driver can be loaded and unloaded multiple times. It will recognize that a call stack is the same even if the driver is reloaded into a different memory location.

## <span id="Activating_this_option"></span><span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating this option


You can activate the Stack Based Failure Injection feature for one or more drivers when you are [Deploying a Driver to a Test Computer](https://msdn.microsoft.com/windows-drivers/develop/deploying_a_driver_to_a_test_computer). You can select the Stack Based Failure Injection option when you configure the [Driver Verifier Properties for Driver Package Projects](https://msdn.microsoft.com/windows-drivers/develop/driver_verifier_properties_for__driver_projects). You must restart the computer to activate or deactivate the Stack Based Failure Injection option. You can also run a test utility to enable Driver Verifier and this feature on the test computer.

**Important**  When you activate Stack Based Failure Injection on the test computer, make sure do not also select [Low Resources Simulation](low-resources-simulation.md).

 

-   **Using Driver Verifier Property page**

    1.  Open the property pages for your driver package. Right-click the driver package project in **Solution Explorer** and select **Properties**.
    2.  In the property pages for the driver package, click **Configuration Properties**, click **Driver Install**, and then click **Driver Verifier**.
    3.  Select **Enable Driver Verifier**. When you enable Driver Verifier on the test computer, you can choose to enable Driver Verifier for all drivers on the computer, for the driver project only, or for a list of specified drivers.
    4.  Under **Stack Based Failure Injector**, select (check) Stack Based Failure Injection.
    5.  Click **Apply** or **OK**.
    6.  See [Deploying a Driver to a Test Computer](https://msdn.microsoft.com/windows-drivers/develop/deploying_a_driver_to_a_test_computer) for more information. The test computer must restart to activate this option.
-   **Using the Enable and Disable Driver Verifier test**

    1.  You can also enable Driver Verifier by running a utility test. Follow the instructions described in [How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime). Under the **All Tests\\Driver Verifier** test category, select the **Enable Driver Verifier (possible reboot required)** and **Disable Driver Verifier (possible reboot required)** tests.
    2.  Select the Driver Verifier options by clicking on the name of the **Enable Driver Verifier (possible reboot required)** test in the **Driver Test Group** window.
    3.  Select (check) Stack Based Failure Injection.
    4.  After you add these tests to a test group you can save the test group. To enable the Stack Based Failure Injection, run the **Enable Driver Verifier (possible reboot required)** test on the computer you have configured for testing.

        To deactivate Driver Verifier, run the **Disable Driver Verifier (possible reboot required)** test.

## <span id="Using_the_Stack_Based_Failure_Injection_option"></span><span id="using_the_stack_based_failure_injection_option"></span><span id="USING_THE_STACK_BASED_FAILURE_INJECTION_OPTION"></span>Using the Stack Based Failure Injection option


One important consideration when testing with Stack Based Failure Injection is that most bugs that it finds will result in a bug check. This could prove somewhat painful if your driver is a boot-loaded driver. Because of this, we will automatically disable Stack Based Failure Injection if Driver Verifier is disabled. This means that you can disable Stack Based Failure Injection at boot time from the debugger by disabling Driver Verifier using the command **!verifier –disable**.

If it is possible, for your initial tests with Stack Based Failure Injection, set up your driver so that it is not loaded at boot time. You can then run some simple load and unload tests. Many of the bugs found by Stack Based Failure Injection occur during initialization or cleanup. Repeatedly loading and unloading your driver is a good way to find these.

After making any fixes necessary to get the load unload tests to succeed, you can move on to IOCTL-based testing, full functional testing, and finally stress testing. In general, if you follow this test progression, you will not uncover many new issues during stress testing because most of the code paths will have already been executed before this.

## <span id="Using_the_Stack_Based_Failure_Injection__SBFI__debugger_extension"></span><span id="using_the_stack_based_failure_injection__sbfi__debugger_extension"></span><span id="USING_THE_STACK_BASED_FAILURE_INJECTION__SBFI__DEBUGGER_EXTENSION"></span>Using the Stack Based Failure Injection (SBFI) debugger extension


Most of the issues found with Stack Based Failure Injection result in bug checks. To help determine the cause of these code bugs, the WDK provides the Stack Based Failure Injection debugger extension and the necessary symbols. The installation procedure will install both on your debugger system. The default location is C:\\Program Files (x86)\\Windows Kits\\8.0\\Debuggers\\*&lt;arch&gt;*.

**To run the debugger extension**

- From the debugger command prompt, type the following command: **!**<em>&lt;path&gt;\\</em>**kmautofaildbg.dll.autofail**. For example, assuming debugger extensions are installed at c:\\dbgext and that kmautofail.pdb is in the symbol path, you would enter the following command:

  ```
  !c:\dbgext\kmautofaildbg.dll.autofail
  ```

This will dump information to your debugger showing the call stacks from the most recent failures injected. Each entry looks something like the following, taken from a real test run. In the following example, Stack Based Failure Injection is enabled on Mydriver.sys

```
Sequence: 2, Test Number: 0, Process ID: 0, Thread ID: 0
                 IRQ Level: 2, HASH: 0xea98a56083aae93c
 0xfffff8800129ed83 kmautofail!ShimHookExAllocatePoolWithTag+0x37
 0xfffff88003c77566 mydriver!AddDestination+0x66
 0xfffff88003c5eeb2 mydriver!ProcessPacketDestination+0x82
 0xfffff88003c7db82 mydriver!ProcessPacketSource+0x8b2
 0xfffff88003c5d0d8 mydriver!ForwardPackets+0xb8
 0xfffff88003c81102 mydriver!RoutePackets+0x142
 0xfffff88003c83826 mydriver!RouteNetBufferLists+0x306
 0xfffff88003c59a76 mydriver!DeviceSendPackets+0x156
 0xfffff88003c59754 mydriver!ProcessingComplete+0x4a4
 0xfffff88001b69b81 systemdriver2!ProcessEvent+0x1a1
 0xfffff88001b3edc4 systemdriver1!CallChildDriver+0x20
 0xfffff88001b3fc0a systemdriver1!ProcessEvent+0x3e
 0xfffff800c3ea6eb9 nt!KiRetireDpcList+0x209
 0xfffff800c3ea869a nt!KiIdleLoop+0x5a
```

At the top of the output, the sequence number counts the number of faults that are injected. This example shows the second fault injected during this test run. The process ID is 0, so this was the system process. IRQL is 2, so this is called at dispatch level.

From the stack, KmAutoFail is the Stack Based Failure Injection driver. The KmAutoFail function name indicates what function call from Mydriver.sys was intercepted and fault injected. Here, the function that failed was [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520). All functions in KmAutoFail that intercept calls to Ntoskrnl.sys or Ndis.sys use this naming convention. Next, we see the call stack with the driver being tested (Mydriver.sys). This is the portion of the call stack that is used to determine the uniqueness of the stack. Thus each entry dumped by the debugger extension will be unique in this portion of the call stack. The rest of the call stack indicates who called the driver. The main importance of this is whether the driver is called from user mode (by means of an IOCTL) or from a kernel-mode driver.

Note that if a driver has returned failure from its [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, a reload attempt will normally take place at a different memory location. In that case, the call stack from the earlier location will probably contain “garbage” rather than stack information from the driver. But this is not a problem; it tells you that the driver correctly handled that injected fault.

This next entry shows a call to the driver by means of an IOCTL from user mode. Note the process ID and the IRQ level. Since Mydriver.sys is an NDIS filter driver, the IOCTL came through Ndis.sys. Note that nt!NtDeviceIoControlFile is on the stack. Any test that you run on your driver that uses IOCTLs will go through this function.

```
Sequence: 5, Test Number: 0, Process ID: 2052, Thread ID: 4588
                 IRQ Level: 0, HASH: 0xecd4650e9c25ee4
 0xfffff8800129ed83 kmautofail!ShimHookExAllocatePoolWithTag+0x37
 0xfffff88003c6fb39 mydriver!SendMultipleOids+0x41
 0xfffff88003c7157b mydriver!PvtDisconnect+0x437
 0xfffff88003c71069 mydriver!NicDisconnect+0xd9
 0xfffff88003ca3538 mydriver!NicControl+0x10c
 0xfffff88003c99625 mydriver!DeviceControl+0x4c5
 0xfffff88001559d93 NDIS!ndisDummyIrpHandler+0x73
 0xfffff88001559339 NDIS!ndisDeviceControlIrpHandler+0xc9
 0xfffff800c445cc96 nt!IovCallDriver+0x3e6
 0xfffff800c42735ae nt!IopXxxControlFile+0x7cc
 0xfffff800c4274836 nt!NtDeviceIoControlFile+0x56
 0xfffff800c3e74753 nt!KiSystemServiceCopyEnd+0x13
```

## <span id="Analyzing_the_results_of_Stack_Based_Failure_Injection"></span><span id="analyzing_the_results_of_stack_based_failure_injection"></span><span id="ANALYZING_THE_RESULTS_OF_STACK_BASED_FAILURE_INJECTION"></span>Analyzing the results of Stack Based Failure Injection


You are running your tests on your driver, and suddenly you hit a problem. Most likely this was a bug check, but it could also because the computer became unresponsive. How do you find the cause? Assuming it is a bug check, first use the extension above to find the list of injected failures, then use the debugger command: **!analyze –v**.

The most common bug check is caused by not checking for the success of an allocation. In this case, the stack from the bug check analysis is probably almost identical to that of the last failure injected. At some point after the failed allocation (often the very next line), the driver will access the null pointer. This type of bug is very easy to fix. Sometimes the failing allocation is one or two up the list, but this type is still very easy to find and fix.

The second most common bug check occurs during cleanup. In this case, the driver probably detected the allocation failure and jumped to cleanup; but during cleanup, the driver did not check the pointer and once again accessed a null pointer. A closely related case is where cleanup can be called twice. If the cleanup does not set the pointer to a structure to null after it frees it, the second time the cleanup function is called it will try to free the structure a second time, resulting in a bug check.

Errors that cause the computer to become unresponsive are more difficult to diagnose, but the procedure to debug them is similar. These errors are often caused by reference count or spin lock issues. Fortunately, [Driver Verifier](driver-verifier.md) will catch many spin lock issues before they would lead to problems. In these cases, break into the debugger and use the debugger extension to dump the list of faults that have been injected by Stack Based Failure Injection. A quick look at the code around the latest failures might show a reference count that is taken before the failure but not released after. If not, look for a thread in your driver that is waiting on a spin lock, or for any reference count that is obviously wrong.

 

 





