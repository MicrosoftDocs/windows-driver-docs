---
title: Checked Build Breakpoints and Messages
description: Checked Build Breakpoints and Messages
ms.assetid: 99b27487-eb95-4303-bad6-0b7ed8b450f0
keywords: ["breakpoints WDK", "checked builds WDK , breakpoints", "checked builds WDK , messages", "messages WDK checked builds"]
---

# Checked Build Breakpoints and Messages


## <span id="ddk_checked_build_breakpoints_and_messages_tools"></span><span id="DDK_CHECKED_BUILD_BREAKPOINTS_AND_MESSAGES_TOOLS"></span>


This topic contains a list and explanation of some of the common breakpoints and [**DbgPrint**](https://msdn.microsoft.com/library/windows/hardware/ff543632) messages that a driver might encounter in the checked build.

<span id="____DPC_routine___1_sec_---_This_is_not_a_break_in_KeUpdateSystemTime"></span><span id="____dpc_routine___1_sec_---_this_is_not_a_break_in_keupdatesystemtime"></span><span id="____DPC_ROUTINE___1_SEC_---_THIS_IS_NOT_A_BREAK_IN_KEUPDATESYSTEMTIME"></span>**\*\*\* DPC routine &gt; 1 sec --- This is not a break in KeUpdateSystemTime**  
This message appears just before a breakpoint is issued. It indicates that the active driver spent more than one second in a DPC routine.

<span id="____isr_at_0x_________________nnnnnnnn_________________took_over_.5_second"></span><span id="____ISR_AT_0X_________________NNNNNNNN_________________TOOK_OVER_.5_SECOND"></span>**\*\*\* ISR at 0x** *nnnnnnnn* **took over .5 second**  
This message appears just before a breakpoint is issued. It indicates that the interrupt service routine with entry point 0x*nnnnnnnn* executed for more than 500ms.

<span id="IOINIT__Built-in_driver__________________xxxxxx_________________failed_to_initialize___0xnnnnnnnn"></span><span id="ioinit__built-in_driver__________________xxxxxx_________________failed_to_initialize___0xnnnnnnnn"></span><span id="IOINIT__BUILT-IN_DRIVER__________________XXXXXX_________________FAILED_TO_INITIALIZE___0XNNNNNNNN"></span>**IOINIT: Built-in driver** *xxxxxx* **failed to initialize − 0x***nnnnnnnn*  
The boot start driver named *xxxxxx* returned a failure status 0x*nnnnnnnn* from its **DriverEntry** entry point.

<span id="IOINIT__Built-in_driver__________________xxxxxx_________________took__________________y.z________________s_to_initialize"></span><span id="ioinit__built-in_driver__________________xxxxxx_________________took__________________y.z________________s_to_initialize"></span><span id="IOINIT__BUILT-IN_DRIVER__________________XXXXXX_________________TOOK__________________Y.Z________________S_TO_INITIALIZE"></span>**IOINIT: Built-in driver** *xxxxxx* **took** *y.z* **s to initialize**  
The boot start driver named *xxxxxx* executed for *y.z* seconds (which is longer than the expected maximum time of 5 seconds) in its **DriverEntry** entry point.

<span id="IOINIT__Built-in_driver__________________xxxxxx_________________took__________________y.z________________s_to_fail_initialization"></span><span id="ioinit__built-in_driver__________________xxxxxx_________________took__________________y.z________________s_to_fail_initialization"></span><span id="IOINIT__BUILT-IN_DRIVER__________________XXXXXX_________________TOOK__________________Y.Z________________S_TO_FAIL_INITIALIZATION"></span>**IOINIT: Built-in driver** *xxxxxx* **took** *y.z* **s to fail initialization**  
The boot start driver named *xxxxxx* executed for *y.z* seconds (which is longer than the expected maximum time of 5 seconds) in its **DriverEntry** entry point.

<span id="ioload__driver__________________xxxxxx_________________took__________________y.z________________s_to_initialize"></span><span id="IOLOAD__DRIVER__________________XXXXXX_________________TOOK__________________Y.Z________________S_TO_INITIALIZE"></span>**IOLOAD: Driver** *xxxxxx* **took** *y.z* **s to initialize**  
The driver named *xxxxxx* executed for *y.z* seconds (which is longer than the expected maximum time of 5 seconds) in its **DriverEntry** entry point.

<span id="ioload__driver__________________xxxxxx_________________took__________________y.z________________s_to_fail_initialization"></span><span id="IOLOAD__DRIVER__________________XXXXXX_________________TOOK__________________Y.Z________________S_TO_FAIL_INITIALIZATION"></span>**IOLOAD: Driver** *xxxxxx* **took** *y.z* **s to fail initialization**  
The driver named *xxxxxx* executed for *y.z* seconds (which is longer than the expected maximum time of 5 seconds) in its **DriverEntry** entry point.

<span id="IopLoadDriver__A_PnP_driver__________________xxxxxx_________________does_not_support_DriverUnload_routine"></span><span id="ioploaddriver__a_pnp_driver__________________xxxxxx_________________does_not_support_driverunload_routine"></span><span id="IOPLOADDRIVER__A_PNP_DRIVER__________________XXXXXX_________________DOES_NOT_SUPPORT_DRIVERUNLOAD_ROUTINE"></span>**IopLoadDriver: A PnP driver** *xxxxxx* **does not support DriverUnload routine**  
The driver named *xxxxxx* supports IRP\_MJ\_PNP, but did not specify an unload routine in **DriverEntry**.

<span id="DO_DEVICE_INITIALIZING_flag_not_cleared_on_DO_0x_________________nnnnnnnn"></span><span id="do_device_initializing_flag_not_cleared_on_do_0x_________________nnnnnnnn"></span><span id="DO_DEVICE_INITIALIZING_FLAG_NOT_CLEARED_ON_DO_0X_________________NNNNNNNN"></span>**DO\_DEVICE\_INITIALIZING flag not cleared on DO 0x** *nnnnnnnn*  
The device object at address 0x*nnnnnnnn* was created outside of **DriverEntry**, but the DO\_DEVICE\_INITIALIZING bit was not cleared before returning to the system.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Checked%20Build%20Breakpoints%20and%20Messages%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




