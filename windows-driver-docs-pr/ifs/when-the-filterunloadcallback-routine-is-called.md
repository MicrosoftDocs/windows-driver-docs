---
title: When the FilterUnloadCallback Routine Is Called
description: When the FilterUnloadCallback Routine Is Called
keywords:
- FilterUnloadCallback
- non-mandatory unload WDK file system minifilter
- mandatory unload WDK file system minifilter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# When the FilterUnloadCallback Routine Is Called


## <span id="ddk_when_the_filterunloadcallback_routine_is_called_if"></span><span id="DDK_WHEN_THE_FILTERUNLOADCALLBACK_ROUTINE_IS_CALLED_IF"></span>


The filter manager calls a minifilter driver's [**FilterUnloadCallback**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_filter_unload_callback) routine before unloading the minifilter driver in one of the following ways:

-   *Non-mandatory unload*. This type of unload occurs when a user-mode application has called [**FilterUnload**](/windows/win32/api/fltuser/nf-fltuser-filterunload) or a kernel-mode driver has called [**FltUnloadFilter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltunloadfilter). It also occurs when you type **fltmc unload** at the command prompt.

-   *Mandatory unload*. This type of unload occurs when you issue a service stop request by typing **sc stop** or **net stop** at the command prompt. (For more information about the **sc stop** and **net stop** commands, click **Help and Support** on the Start menu.) It also occurs when a user-mode application calls the Microsoft Win32 **ControlService** function, passing the SERVICE\_CONTROL\_STOP control code as the *dwControl* parameter. (For more information about Win32 service functions, see the Microsoft Windows SDK documentation.)

For a non-mandatory unload, if the minifilter driver's *FilterUnloadCallback* routine returns an error or warning NTSTATUS value, such as STATUS\_FLT\_DO\_NOT\_DETACH, the filter manager does not unload the minifilter driver.

For a mandatory unload, the filter manager unloads the minifilter driver after the minifilter driver's *FilterUnloadCallback* routine is called, even if the *FilterUnloadCallback* routine returns an error or warning NTSTATUS value, such as STATUS\_FLT\_DO\_NOT\_DETACH.

To disable mandatory unloading for a minifilter driver, the minifilter driver sets the FLTFL\_REGISTRATION\_DO\_NOT\_SUPPORT\_SERVICE\_STOP flag in the **Flags** member of the [**FLT\_REGISTRATION**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_registration) structure that the minifilter driver passes as a parameter to [**FltRegisterFilter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltregisterfilter) in its **DriverEntry** routine. When this flag is set, the filter manager normally processes non-mandatory unload requests. However, mandatory unload requests will fail. The filter manager does not call the minifilter driver's *FilterUnloadCallback* routine for failed unload requests.

Note that if a minifilter driver's **DriverEntry** routine returns a warning or error NTSTATUS value, the *FilterUnloadCallback* routine is not called; the filter manager simply unloads the minifilter driver.

The *FilterUnloadCallback* routine is not called at system shutdown time. A minifilter driver that must perform shutdown processing should register a preoperation callback routine for IRP\_MJ\_SHUTDOWN operations.

 

