---
title: Determining Why the UMDF Driver Fails to Load or the UMDF Device Fails to Start
description: This topic describes troubleshooting steps you can use when a UMDF driver fails to load or an associated device fails to start.
ms.assetid: 366c0ab4-8d06-4dac-a301-f433cf7978bd
keywords: ["debugging scenarios WDK UMDF UMDF driver fails to load", "debugging scenarios WDK UMDF UMDF device fails to start", "UMDF WDK debugging scenarios UMDF driver fails to load", "UMDF WDK debugging scenarios UMDF device fails to start", "UMDF WDK driver not loading scenario", "UMDF WDK device not starting scenario"]
---

# Determining Why the UMDF Driver Fails to Load or the UMDF Device Fails to Start


This topic describes troubleshooting steps you can use when a UMDF driver fails to load or an associated device fails to start.

You can use the following technique with both UMDF version 1 and 2 drivers.

1.  Check setup by ensuring that the following files are correct:
    -   Driver's INF file.

        Use the [ChkINF](https://msdn.microsoft.com/library/windows/hardware/ff543461) tool to validate the driver's INF file.

    -   %windir%\\inf\\setupapi.dev.log (setupapi.log on Windows XP), %windir%\\setupact.log, and %windir%\\temp\\wudf\_update.log files.

2.  If you did not find any setup issues, enable the **HostProcessDbgBreakOnStart** registry entry by using the [WDF Verifier control application](https://msdn.microsoft.com/library/windows/hardware/ff556129) (WdfVerifier.exe). By enabling **HostProcessDbgBreakOnStart**, you will make the driver host process for the device (WUDFHost.exe) break into the debugger shortly after WUDFHost.exe starts but before your driver DLL loads.

    You should enable **HostProcessDbgBreakOnStart** with a user-mode debugger and not a kernel-mode debugger. A kernel-mode debugger, by default, does not receive user-mode module load and unload notifications. Therefore, you will not be able to set deferred breakpoints.

3.  If you do not see a host start, perform the following steps to correctly configure the device:
    1.  Ensure that all the drivers that you install through your INF exist and are copied to the operating system.
    2.  If the reflector (also known as WUDFRd.sys) is not the service on the device, ensure that the driver, which would then be the service, has a service entry (for example, 'sc qc foo') and is set to start automatically.

4.  Ensure that your driver's symbols are in the symbol path (that is, .sympath).

5.  Verify the following items one at a time. In the following steps, assume that your driver is foo.dll:
    1.  Verify that your driver's **DllMain** routine is called (for example, bu Foo!DllMain).
    2.  If your driver DLL does load, for subsequent steps, you can also use the **HostProcessDbgBreakOnDriverLoad** registry entry. Having **HostProcessDbgBreakOnDriverLoad** set causes WUDFHost.exe to break into the debugger after your driver DLL is loaded. **HostProcessDbgBreakOnDriverLoad** can also be used with the kernel-mode debugger because at this point in the driver loading and device starting process you can set breakpoints in your driver code.
    3.  This step applies to UMDF version 1 drivers only. Verify that your driver's **DllGetClassObject** routine is called. Verify that the class identifier (ID) for your driver is correct. Verify that **DllGetClassObject** runs successfully and returns a driver object (for example, bu Foo!DllGetClassObject).

    4.  For UMDF version 1, verify that your driver's [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) method is called. Verify that the method creates a device and returns successfully (for example, bu Foo!CMyDriver::OnDeviceAdd).

        For UMDF version 2, verify that your driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) function is called. Verify that the function creates a device and returns successfully (for example, bu Foo!MyDriverDeviceAdd).

    5.  For UMDF version 1, verify that your driver's [**IPnpCallbackHardware::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556766) or [**IPnpCallback::OnD0Entry**](https://msdn.microsoft.com/library/windows/hardware/ff556799) method is called. Verify that the method returns successfully (for example, bu Foo!CMyDevice::OnPrepareHardware or Foo!CMyDevice::OnD0Entry).

        For UMDF version 2, verify that your driver's [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) or [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) function is called. Verify that the function returns successfully (for example, bu Foo!MyDevicePrepareHardware or Foo!MyDeviceD0Entry).

    6.  If each of the previous operations run successfully but the operation that follows does not run, you should check the following items:
        1.  Verify that every driver above and below your driver in the user-mode stack also successfully performs these operations.
        2.  Verify that the kernel stack below your driver successfully completes the [**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772) and [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) IRPs.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Determining%20Why%20the%20UMDF%20Driver%20Fails%20to%20Load%20or%20the%20UMDF%20Device%20Fails%20to%20Start%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




