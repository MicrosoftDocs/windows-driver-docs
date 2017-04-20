---
title: TAEF Timeouts
description: TAEF Timeouts
ms.assetid: 43FE81A2-71DF-4e3a-998E-1B1F8C1398AC
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# TAEF Timeouts


TAEF time-outs are specified in the following format: *\[Day.\]Hour\[:Minute\[:Second\[.FractionalSeconds\]\]\]*.

For example:

*0:0:0.5*  
Specifies a .5 second time-out.

<span id="0_0_45"></span>*0:0:45*  
Specifies a 45 seconds time-out.

<span id="0_20_or_0_20_0"></span><span id="0_20_OR_0_20_0"></span>*0:20* or *0:20:0*  
Specifies a 20 minute time-out.

<span id="5_or_5_0_or_5_0_0"></span><span id="5_OR_5_0_OR_5_0_0"></span>*5* or *5:0* or *5:0:0*  
Specifies a 5 hour time-out.

<span id="1.2_or_1.2_0_or_1.2_0_0"></span><span id="1.2_OR_1.2_0_OR_1.2_0_0"></span>*1.2* or *1.2:0* or *1.2:0:0*  
Specifies a 1 day and 2 hour time-out.

## <span id="Session_Time-outs"></span><span id="session_time-outs"></span><span id="SESSION_TIME-OUTS"></span>Session Time-outs


Session time-outs can be specified for the entire execution of Te.exe when you use the **/sessionTimeout** option. If the time-out expires, the test session will be gracefully stopped, and the [process exit code](exit-codes-for-taef.md) will signify that a time-out occurred.

<span id="te.exe_test1.dll__sessionTimeout_0_20"></span><span id="te.exe_test1.dll__sessiontimeout_0_20"></span><span id="TE.EXE_TEST1.DLL__SESSIONTIMEOUT_0_20"></span>te.exe test1.dll /sessionTimeout:0:20  
The entire test session will time out after 20 minutes.

## <span id="Test_Time-outs"></span><span id="test_time-outs"></span><span id="TEST_TIME-OUTS"></span>Test Time-outs


Test time-outs can be specified by applying time-out metadata to a given test assembly, class or method.

Additionally, time-out metadata values can be overridden at runtime when you use the /testTimeout option. If specified, /testTimeout sets a global test time-out for the entire execution of Te.exe.

**Note:** Test time-outs will be ignored when used in conjunction with [/inproc](te-exe-command-line-parameters.md#inproc).

<span id="te.exe_test1.dll__testTimeout_0_0_45"></span><span id="te.exe_test1.dll__testtimeout_0_0_45"></span><span id="TE.EXE_TEST1.DLL__TESTTIMEOUT_0_0_45"></span>te.exe test1.dll /testTimeout:0:0:45  
Every test and setup/cleanup method will time out after 45 seconds.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20TAEF%20Timeouts%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




