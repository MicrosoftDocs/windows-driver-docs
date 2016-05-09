---
title: When the FilterUnloadCallback Routine Is Called
description: When the FilterUnloadCallback Routine Is Called
ms.assetid: 22a3a73e-28be-4483-a7a6-73525e74503d
keywords: ["FilterUnloadCallback", "non-mandatory unload WDK file system minifilter", "mandatory unload WDK file system minifilter"]
---

# When the FilterUnloadCallback Routine Is Called


## <span id="ddk_when_the_filterunloadcallback_routine_is_called_if"></span><span id="DDK_WHEN_THE_FILTERUNLOADCALLBACK_ROUTINE_IS_CALLED_IF"></span>


The filter manager calls a minifilter driver's [**FilterUnloadCallback**](https://msdn.microsoft.com/library/windows/hardware/ff551085) routine before unloading the minifilter driver in one of the following ways:

-   *Non-mandatory unload*. This type of unload occurs when a user-mode application has called [**FilterUnload**](https://msdn.microsoft.com/library/windows/hardware/ff541516) or a kernel-mode driver has called [**FltUnloadFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544602). It also occurs when you type **fltmc unload** at the command prompt.

-   *Mandatory unload*. This type of unload occurs when you issue a service stop request by typing **sc stop** or **net stop** at the command prompt. (For more information about the **sc stop** and **net stop** commands, click **Help and Support** on the Start menu.) It also occurs when a user-mode application calls the Microsoft Win32 **ControlService** function, passing the SERVICE\_CONTROL\_STOP control code as the *dwControl* parameter. (For more information about Win32 service functions, see the Microsoft Windows SDK documentation.)

For a non-mandatory unload, if the minifilter driver's *FilterUnloadCallback* routine returns an error or warning NTSTATUS value, such as STATUS\_FLT\_DO\_NOT\_DETACH, the filter manager does not unload the minifilter driver.

For a mandatory unload, the filter manager unloads the minifilter driver after the minifilter driver's *FilterUnloadCallback* routine is called, even if the *FilterUnloadCallback* routine returns an error or warning NTSTATUS value, such as STATUS\_FLT\_DO\_NOT\_DETACH.

To disable mandatory unloading for a minifilter driver, the minifilter driver sets the FLTFL\_REGISTRATION\_DO\_NOT\_SUPPORT\_SERVICE\_STOP flag in the **Flags** member of the [**FLT\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff544811) structure that the minifilter driver passes as a parameter to [**FltRegisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544305) in its **DriverEntry** routine. When this flag is set, the filter manager normally processes non-mandatory unload requests. However, mandatory unload requests will fail. The filter manager does not call the minifilter driver's *FilterUnloadCallback* routine for failed unload requests.

Note that if a minifilter driver's **DriverEntry** routine returns a warning or error NTSTATUS value, the *FilterUnloadCallback* routine is not called; the filter manager simply unloads the minifilter driver.

The *FilterUnloadCallback* routine is not called at system shutdown time. A minifilter driver that must perform shutdown processing should register a preoperation callback routine for IRP\_MJ\_SHUTDOWN operations.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20When%20the%20FilterUnloadCallback%20Routine%20Is%20Called%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




