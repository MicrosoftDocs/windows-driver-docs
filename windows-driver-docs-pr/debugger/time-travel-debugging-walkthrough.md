---
title: Time Travel Debugging - Sample App Walkthrough
description: This section contains a walk through of a small C++ app. 
ms.author: windowsdriverdev
ms.date: 12/11/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>


# ![Small time travel logo showing clock](images/ttd-time-travel-debugging-logo.png) Time Travel Debugging - Sample App Walkthrough


This lab introduces Time Travel Debugging (TTD), using a small sample program with a code flaw. TTD is used to debug and identify and root cause the issue. Although the issue in this small program is easy to find, the general procedure can be used on more complex code. This general procedure can be sumarized as follows.

1. Capture a time travel trace of the failed program.
2. Use the dx command to determine the exception event stored in the recording. 
3. Step back in the trace to the exception event.
4. From that point single step backwards until the faulting code in question comes into scope.
5. With the faulting code in scope, look at the local values and develop a hypthesis of a variable that may contain an incorrect value.
6. Determine the memory address of the variable with the incorrect value.
7. Set a memory access (ba) breakpoint on address of the suspect variable.
8. Use g- to run back to point of memory access of the suspect variable.
9. See if that location or a few instructions before is the point of the code flaw. If so, you are done.
If some other variable sets the value in the first variable, set another break on access breakpoint on the second variable. 
10. Use g- to run back to point of memory access on the second suspect variable. See if that location or a few instructions before contains the code flaw. If so, you are done.
11. Repeat this process walking back until the code that created the error, by settng the incorrect value is located.
 

## <span id="Lab_objectives"></span><span id="lab_objectives"></span><span id="LAB_OBJECTIVES"></span>Lab objectives

After completing this lab you will be able to use the general procedure with a time travel trace to locate issues in code. 

## <span id="Lab_setup"></span><span id="lab_setup"></span><span id="LAB_SETUP"></span>Lab setup


You will need the following hardware to be able to complete the lab.

-   A laptop or desktop computer (host) running Windows 10 

You will need the following software to be able to complete the lab.

-   The WinDbg Preview. For information on installing WinDbg Preview, see [WinDbg Preview - Installation](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/windbg-install-preview)
-   Visual Studio to build the sample C++ code 

The lab has the following eleven sections.

-   [Section 1: Build the sample code](#build)
-   [Section 2: Record a trace of the sample "DisplayText" code](#record)
-   [Section 3: Analyze the trace file recording to indentify the code issue](#analyze)


## <span id="build"></span>Section 1: Build the sample code

*In Section 1, you will build the sampe code using Visual Studio.*

The PCs in this lab need to be configured to use an Ethernet network connection for kernel debugging.


## <span id="record"></span>Section 2: Record a trace of the sample "DisplayText" cod

*In Section 2, you will record a trace of the sample "DisplayText" app*

The PCs in this lab need to be configured to use an Ethernet network connection for kernel debugging.



## <span id="analyze"></span>Section 3: Analyze the trace file recording to indentify the code issue

*In Section 3, you will analyze the trace file recording to indentify the code issue.*

The PCs in this lab need to be configured to use an Ethernet network connection for kernel debugging.

1. Capture a time travel trace of the failed program.
2. Use the dx command to determine the exception event stored in the recording. 
3. Step back in the trace to the exception event.
4. From that point single step backwards until the faulting code in question comes into scope.
5. With the faulting code in scope, look at the local values and develop a hypthesis of a variable that may contain an incorrect value.
6. Determine the memory address of the variable with the incorrect value.
7. Set a memory access (ba) breakpoint on address of the suspect variable.
8. Use g- to run back to point of memory access of the suspect variable.
9. See if that location or a few instructions before is the point of the code flaw. If so, you are done.
If some other variable sets the value in the first variable, set another break on access breakpoint on the second variable. 
10. Use g- to run back to point of memory access on the second suspect variable. See if that location or a few instructions before contains the code flaw. If so, you are done.
11. Repeat this process walking back until the code that created the error, by settng the incorrect value is located.

---

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




