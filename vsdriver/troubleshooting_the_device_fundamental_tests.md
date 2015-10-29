Troubleshooting the Device Fundamentals tests using the WDK
===================================================================================================================================

This topic provides suggestions for fixing problems you might encounter when you use the WDK to run the [Device Fundamentals Tests](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/JJ673011). For information about the tests and testing, see [How to select and configure the Device Fundamentals tests](how_to_select_and_configure_the_device_fundamental_tests.md), [How to test a driver at runtime using Visual Studio](testing_a_driver_at_runtime.md), and [How to test a driver at runtime from a Command Prompt](how_to_test_a_driver_at_runtime_from_a_command_prompt.md).

**Note**  For information about troubleshooting the Device.Fundamentals tests using the HCK, see [Troubleshooting Device Fundamentals Reliability Testing by using the Windows HCK](http://go.microsoft.com/fwlink/p/?linkid=288941).

 

-   [Device Fundamentals test fails (general)](#_devfund_device)
-   [Driver Verifier is not enabled](#_defund_verifier)
-   [Test is unresponsive or not running](#_defund_test_hang)
-   [PnP Surprise Remove Device test fails](#_defund_pnp_surprise_remove)

<span id="_devfund_device"></span><span id="_DEVFUND_DEVICE"></span>
--------------------------------------------------------------------

| Problem: Device Fundamentals test fails (general) |
|---------------------------------------------------|

 

**Error condition:**

The test fails or fails to run. For some device types there are specific requirements for running the Device Fundamentals tests. These are the same requirements you need to follow when you use the [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893).

Before you run the following [Device Fundamental tests](how_to_select_and_configure_the_device_fundamental_tests.md), the devices on the test computer must be configured according to the requirements described for the specific device types.

-   PCI Root Port Surprise Remove Test (PCI devices only)
-   Device Path Exerciser Test (Certification)
-   Sleep and PNP (disable and enable) with IO Before and After (Certification)
-   Plug and Play Driver Test (Certification)
-   Concurrent Hardware And Operating System (CHAOS) Test (Certification)
-   Reinstall with IO Before and After (Certification)
-   Device Install Check For File System Consistency (Certification)
-   Device Install Check For Other Device Stability (Certification)

**Solution:**

Information about specific device requirements for testing are described under [Provided WDTF Simple I/O plug-ins](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh781398). The Device Fundamentals tests use the Provided WDTF Simple I/O plug-ins to perform device specific I/O operations to improve the effectiveness of tests. For a description of the type of I/O the plug-ins perform, and to see if there are any special device requirements, use the following links. If there are any specific triage steps that you can follow to help debug and triage test failures those will also be shown for the device type.

-   [Audio devices](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh781398#_audio#_audio)
-   [Bluetooth devices](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh781398#_bluetooth#_bluetooth)
-   [CDROM devices](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh781398#_cdrom#_cdrom)
-   [Disk devices](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh781398#_disk#_disk)
-   [Display devices](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh781398#_display#_display)
-   [GPS devices](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh781398#_gps#_gps)
-   [LAN devices](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh781398#_lan#_lan)
-   [Mobile Broadband devices](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh781398#_mobile_broadband#_mobile_broadband)
-   [Portable devices](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh781398#_portable_devices#_portable_devices)
-   [Smart Card Readers](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh781398#_smartcard#_smartcard)
-   [Sensor devices](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh781398#_sensors#_sensors)
-   [Volume](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh781398#_volume#_volume)
-   [Webcam](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh781398#_webcam#_webcam)
-   [WLAN](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh781398#_wlan#_wlan)
-   [USB Controller and HUB with Mutt](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh781398#_usb_mutt#_usb_mutt)

<span id="_defund_verifier"></span><span id="_DEFUND_VERIFIER"></span>
----------------------------------------------------------------------

| Problem: Driver Verifier is not enabled |
|-----------------------------------------|

 

**Error message:**

"Driver Verifier is not enabled with at least standard settings on all drivers of device(s) under test (including any upper and/or lower filter drivers. Enable Driver Verifier with at least standard settings and re-run the test."

**Solution:**

The Device Fundamental tests you are running require that Driver Verifier monitors the drivers associated with the device you are testing. You have two options.

-   Add the **Enable Driver Verifier** test to the test group and specify the same *DQ* parameter that you specified for the Device Fundamental tests you are running.
-   Use [Driver Verifier](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff545448) (Verifier.exe) to manually enable Driver Verifier on all individual drivers of the device(s) under test. The Driver Verifier standard settings must be used. To determine which drivers require Driver Verifier, open Device Manager (Devmgmt.msc) on the test computer. In Device Manager, right click the device that you are testing and select **Properties**. Click the **Driver** tab and then click **Driver Details** to identify the names of the drivers. For network class devices, Driver Verifier also has to be enabled on Ndis.sys.

<span id="_defund_test_hang"></span><span id="_DEFUND_TEST_HANG"></span>
------------------------------------------------------------------------

| Problem: Test is unresponsive or not running |
|----------------------------------------------|

 

**Error conditon:**

Test is unresponsive (no apparent progress in the test command window) but the system is responsive.

**Solution:**

Run the test with the test system connected to a kernel debugger. Break into the debugger when the test seems to stop making progress. Review threads with high “tick count” (Ticks) and "WDTF" on the stack running in Te.ProcessHost.exe process. If Te.ProcessHost.exe process doesn’t exist, review threads running in Te.exe process.

``` syntax
!process 0 0 Te.ProcessHost.exe 
    PROCESS fffffa80093c6340
    SessionId: 1 Cid: 1320 Peb: 7f6595b3000 ParentCid: 12a0
    DirBase: 21eee000 ObjectTable: fffff8a0035b0a00 HandleCount: 327. 
    Image: TE. ProcessHost.exe
.process /p /r fffffa80093c6340
```

To list all threads running under Te.ProcessHost.exe and look for threads with WDTF\* on the stack

``` syntax
!process fffffa80093c6340 


        THREAD fffffa800b2be8c0  Cid 0964.0eac  Teb: 000007f601ba6000 Win32Thread: 0000000000000000 WAIT: (UserRequest) UserMode Non-Alertable
            fffffa800b2a11d0  SynchronizationEvent
            fffffa800b300640  SynchronizationEvent
        Not impersonating
        DeviceMap                 fffff8a0014b9c80
        Owning Process            fffffa800b302940       Image:         TE.exe
        Attached Process          N/A            Image:         N/A
        Wait Start TickCount      210995         Ticks: 405945 (0:01:45:32.782)
        Context Switch Count      51             IdealProcessor: 2             
        UserTime                  00:00:00.015
        KernelTime                00:00:00.015
        Win32 Start Address WDTFInterfaces!TsSingleWorkerThread (0x000007fe3a567f28)
        Stack Init fffff8800eb5edd0 Current fffff8800eb5dee0
        Base fffff8800eb5f000 Limit fffff8800eb59000 Call 0
        Priority 9 BasePriority 8 UnusualBoost 0 ForegroundBoost 0 IoPriority 2 PagePriority 5
        Kernel stack not resident.
        Child-SP          RetAddr           Call Site
        fffff880`0eb5df20 fffff803`78b27f7c nt!KiSwapContext+0x76
        (Inline Function) --------`-------- nt!KiSwapThread+0xf4 (Inline Function @ fffff803`78b27f7c)
        fffff880`0eb5e060 fffff803`78aaf4ab nt!KiCommitThreadWait+0x23c
        fffff880`0eb5e120 fffff803`78b257a0 nt!KiWaitForAllObjects+0x3bb
        fffff880`0eb5e3c0 fffff803`78ecb3dc nt!KeWaitForMultipleObjects+0x4ae
        fffff880`0eb5e470 fffff803`78ecb853 nt!ObWaitForMultipleObjects+0x29c
        fffff880`0eb5e980 fffff803`78aff053 nt!NtWaitForMultipleObjects+0xe3
        fffff880`0eb5ebd0 000007fe`45d2315b nt!KiSystemServiceCopyEnd+0x13 (TrapFrame @ fffff880`0eb5ec40)
        00000083`7cdef148 000007fe`430912c6 ntdll!ZwWaitForMultipleObjects+0xa
        00000083`7cdef150 000007fe`368641b5 KERNELBASE!WaitForMultipleObjectsEx+0xe5
        00000083`7cdef430 000007fe`3a566793 WDTFAudioSimpleIoAction!CAudioImpl::RunIO+0x3d1
        00000083`7cdef520 000007fe`3a566ea0 WDTFInterfaces!CSimpleIOEx::PerformIO+0x10f
        00000083`7cdef5b0 000007fe`3a56706b WDTFInterfaces!CSimpleIOExWrap::PerformIO+0x28
        00000083`7cdef5e0 000007fe`3a553fe5 WDTFInterfaces!CMTest_Receiver::Run+0x77
        00000083`7cdefe20 000007fe`3a5578ac WDTFInterfaces!CSimpleIO_MTestEx::ActionThread+0x105
        00000083`7cdefeb0 000007fe`3a567f3e WDTFInterfaces!CMTEXThread::ThreadWorker+0xc
        00000083`7cdefee0 000007fe`4319167e WDTFInterfaces!TsSingleWorkerThread+0x16
        00000083`7cdeff20 000007fe`45d3c3f1 KERNEL32!BaseThreadInitThunk+0x1a
        00000083`7cdeff50 00000000`00000000 ntdll!RtlUserThreadStart+0x1d
```

When you are debugging PnP and power management tests that have become unresponsive, you can use the following two kernel debugger commands to help identify any active PnP and Power threads that could be preventing the tests from making progress.

``` syntax
!pnptriage
```

``` syntax
!poaction
```

<span id="_defund_pnp_surprise_remove"></span><span id="_DEFUND_PNP_SURPRISE_REMOVE"></span>
--------------------------------------------------------------------------------------------

| Problem: PnP Surprise Remove Device test fails |
|------------------------------------------------|

 

**Error message:** "Failed to receive IRP\_MN\_REMOVE\_DEVICE after receiving IRP\_MN\_SURPRISE\_REMOVAL"

**Solution:**

The PnP Surprise Remove Device test (see [PnP Tests (Device Fundamentals)](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/JJ673015)) might fail with the following error message when the PnP manager does not send the remove IRP to the test device stack after sending the surprise remove IRP.

``` syntax
"Failed to receive IRP_MN_REMOVE_DEVICE after receiving IRP_MN_SURPRISE_REMOVAL. Ensure that there are no open handles or references to the test device (in user mode or in kernel mode) preventing IRP_MN_REMOVE_DEVICE from being sent. You may need to terminate any processes or services that may have open user mode handles to this device."
```

The PnP manager will not send the [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff551738) request until all outstanding file handles to the device are closed. That is, the PnP manager will not send the **IRP\_MN\_REMOVE\_DEVICE** request until reference count of the PDO reaches zero. See [Handling an IRP\_MN\_SURPRISE\_REMOVAL Request](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff546699) for information on how to properly handle [**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff551760) request.

To help debug this test failure, you should determine how the reference count of the physical device object (PDO) changes. That is, identify which process is changing the reference count and examine what the call stack looks like when the reference count is changed. The following steps can be used for debugging this failure:

1.  If you have not already done so, connect a kernel debugger to the test computer. See [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Dn745909).
2.  Set a [**ba (Break on Access) breakpoint**](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff538165) at the location where the reference count of the PDO of the test device is stored. See [Processor Breakpoints (ba Breakpoints)](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff553451) for more information about access breakpoints. In the following example, the kernel debugger [**!devnode**](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff562345) command is used to obtain information about the devnode for the USBvideo driver. The address of the PDO for this devnode is 0x849e9648.

    ``` syntax
    0: kd> !devnode 0 1 usbvideo
    Dumping IopRootDeviceNode (= 0x848fadd8)
    DevNode 0x849e9448 for PDO 0x849e9648
      InstancePath is "USB\VID_045E&PID_076D&MI_00\7&1243e0b7&0&0000"
      ServiceName is "usbvideo"
      State = DeviceNodeStarted (0x308)
      Previous State = DeviceNodeEnumerateCompletion (0x30d)
    ```

3.  Use the [**!devobj**](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff562349) command on the PDO to display information about the reference count (RefCount) of the PDO.

    ``` syntax
    0: kd> !devobj 0x849e9648
    Device object (849e9648) is for:
     0000004e \Driver\usbccgp DriverObject 8727e120
    Current Irp 00000000 RefCount 0 Type 00000022 Flags 00003040
    Dacl 82910320 DevExt 849e9700 DevObjExt 849e99e0 DevNode 849e9448 
    ExtensionFlags (0x00000800)  DOE_DEFAULT_SD_PRESENT
    Characteristics (0x00000180)  FILE_AUTOGENERATED_DEVICE_NAME, FILE_DEVICE_SECURE_OPEN
    AttachedDevice (Upper) 88310588 \Driver\usbvideo
    Device queue is not busy
    ```

4.  Examine the PDO device object by using the [**dt (Display Type)**](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff542772) kernel debugger command. The **ReferenceCount** shows the number of open handles for the device that are associated with the device object.

    ``` syntax
    0: kd> dt nt!_DEVICE_OBJECT 849e9648  
    …
       +0x002 Size             : 0x398
       +0x004 ReferenceCount   : 0n0
       +0x008 DriverObject     : 0x8727e120 _DRIVER_OBJECT
    ..
    …
    ```

5.  If the reference count is greater than 0 before starting the test:

    -   Set a breakpoint where the PDO gets created.
    -   After the PDO is created, set the break on access (**ba**) breakpoint at the location where the reference count of the PDO is stored.

    For example, the following command sets a [**ba (Break on Access)**](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff538165) breakpoint on the device object (0x849e9648). The breakpoint is set on write access to the **ReferenceCount** (+4 offset) with a size of 4 bytes (the size of **ReferenceCount**).

    ``` syntax
    0: kd> ba w 4 849e9648+4 
    ```

    -   If the reference count of the PDO is equal to 0 before starting the test, it is likely that running the test is what is causing the reference count of the PDO to be greater than zero at the time the test performs the surprise remove of the device. This usually is an indication of the presence of a handle leak(s). Run the **PNP Surprise Remove Device test** from a Command Prompt window or from Visual Studio to reproduce the failure to capture the info needed to troubleshoot the problem. Please see [PnP Tests (Device Fundamentals)](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/JJ673015) and [How to select and configure the Device Fundamentals tests](how_to_select_and_configure_the_device_fundamental_tests.md) for how to run the **PNP Surprise Remove Device test** from Visual Studio.

    **Note**  If you set the *DoConcurrentIO* parameter to "TRUE" it causes the test to open hundreds of file handles to the PDO. It is recommended to reproduce this failure with this parameter set to "False" for the purpose of debugging this test failure.
6.  When the break on access (ba) breakpoint occurs, you can use the [**!thread**](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff565440) and [**k (Display Stack Backtrace)**](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff551943) kernel debugger commands to debug the failure. Because the reference count could change multiple times during the course of running the test, as an option, you can use the *commandString* parameter of the [**ba (Break on Access)**](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff538165) debugger command to get the information you need on each change to the reference count and still continue testing.

    For example, in the following break on access command, the *commandString* consists of a [**!thread**](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff565440) command that will identify the process causing the reference count change, and the **.reload ; k 100** commands that will identify the call stack, a [**!devobj**](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff562349) command to print the reference count on each change, and **g** command to continue after the breakpoint.

    ``` syntax
    0: kd> ba w 4 849e9648+4 "!thread; .thread /p /r; .reload; k 100; !devobj 849e9648; g" 
    ```

### <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example

In the following example, the [**CreateFile function**](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Aa363858) call from a thread running in cscript.exe is causing an increment to the reference count. We are also able to see the full call stack. Capturing all the instances where the reference count is changed while running the test and analyzing these call stacks after can help with identifying the handle leaks.

``` syntax
THREAD 87eb3d40  Cid 1094.1490  Teb: 7f5a8000 Win32Thread: 82da2210 RUNNING on processor 3
Not impersonating
DeviceMap                 a71b3228
Owning Process            88199cc0       Image:         cscript.exe
Attached Process          N/A            Image:         N/A
Wait Start TickCount      1232688        Ticks: 0
Context Switch Count      18             IdealProcessor: 2             
UserTime                  00:00:00.000
KernelTime                00:00:00.000
Win32 Start Address ntdll!TppWorkerThread (0x7710704d)
Stack Init a6ebfde0 Current a6ebfa6c Base a6ec0000 Limit a6ebd000 Call 0
Priority 9 BasePriority 8 UnusualBoost 0 ForegroundBoost 0 IoPriority 2 PagePriority 5
ChildEBP RetAddr  Args to Child              
a6ebfa50 814a73fe f81771f8 814a72e5 8281000e nt!IopCheckDeviceAndDriver+0x61 (FPO: [Non-Fpo]) (CONV: stdcall) [d:\w8rtm\minkernel\ntos\io\iomgr\parse.c @ 182]
a6ebfb70 8149fb76 849e9648 848f9200 87164008 nt!IopParseDevice+0x11d (FPO: [Non-Fpo]) (CONV: stdcall) [d:\w8rtm\minkernel\ntos\io\iomgr\parse.c @ 1634]
…
…
0236f874 7710689d ffffffff 77195ae2 00000000 ntdll!__RtlUserThreadStart+0x4a (FPO: [SEH]) (CONV: stdcall) [d:\w8rtm\minkernel\ntdll\rtlstrt.c @ 1021]
0236f884 00000000 7710704d 0031c540 00000000 ntdll!_RtlUserThreadStart+0x1c (FPO: [Non-Fpo]) (CONV: stdcall) [d:\w8rtm\minkernel\ntdll\rtlstrt.c @ 939]

Implicit thread is now 87eb3d40
Connected to Windows 8 9200 x86 compatible target at (Wed Sep 19 21:04:27.601 2012 (UTC - 7:00)), ptr64 FALSE
Loading Kernel Symbols
...............................................................
................................................................
...............
Loading User Symbols
................................................................
...........................
Loading unloaded module list
.....................
ChildEBP RetAddr  
a6ebfa50 814a73fe nt!IopCheckDeviceAndDriver+0x61 [d:\w8rtm\minkernel\ntos\io\iomgr\parse.c @ 182]
a6ebfb70 8149fb76 nt!IopParseDevice+0x11d [d:\w8rtm\minkernel\ntos\io\iomgr\parse.c @ 1634]
…
…
0236f2d4 6970274e KERNELBASE!CreateFileW+0x61 [d:\w8rtm\minkernel\kernelbase\fileopcr.c @ 1194]
0236f31c 6b6ce0e1 deviceaccess!CDeviceBroker::OpenDeviceFromInterfacePath+0x178 [d:\w8rtm\base\devices\broker\dll\broker.cpp @ 177]
0236f34c 6b6cc5c0 MFCORE!CDevProxy::CreateKsFilter+0x46 [d:\w8rtm\avcore\mf\core\transforms\devproxy\devproxy.cpp @ 2263]
…
…
0236f874 7710689d ntdll!__RtlUserThreadStart+0x4a [d:\w8rtm\minkernel\ntdll\rtlstrt.c @ 1021]
0236f884 00000000 ntdll!_RtlUserThreadStart+0x1c [d:\w8rtm\minkernel\ntdll\rtlstrt.c @ 939]

Device object (849e9648) is for:
 0000004e \Driver\usbccgp DriverObject 8727e120
Current Irp 00000000 RefCount 1 Type 00000022 Flags 00003040
Dacl 82910320 DevExt 849e9700 DevObjExt 849e99e0 DevNode 849e9448 
ExtensionFlags (0x00000800)  DOE_DEFAULT_SD_PRESENT
Characteristics (0x00000180)  FILE_AUTOGENERATED_DEVICE_NAME, FILE_DEVICE_SECURE_OPEN
AttachedDevice (Upper) 88310588 \Driver\usbvideo
Device queue is not busy.
```

<span id="related_topics"></span>Related topics
-----------------------------------------------

* [Device Fundamentals Tests](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/JJ673011)
* [How to How to test a driver at runtime using Visual Studio](testing_a_driver_at_runtime.md)
* [How to How to test a driver at runtime from a Command Prompt](how_to_test_a_driver_at_runtime_from_a_command_prompt.md)
* [How to select and configure the Device Fundamentals tests](how_to_select_and_configure_the_device_fundamental_tests.md)
* [Provided WDTF Simple I/O plug-ins](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh781398)
* [Troubleshooting Device Fundamentals Reliability Testing by using the Windows HCK](http://go.microsoft.com/fwlink/p/?linkid=288941)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Troubleshooting%20the%20Device%20Fundamentals%20tests%20using%20the%20WDK%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


