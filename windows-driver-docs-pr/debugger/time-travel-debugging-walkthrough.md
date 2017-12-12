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


This lab introduces  Time Travel Debugging, using a small code sample with a code flaw. TTD is used to debug and identify the issue. Although the issue in teh code is easy to find, the general procedure can be used on more complex code. The general procedure can be sumarized as follows.

1. Capture a time travel trace of the failed program.
2. Use the dx command to determine the exception event. 
3. Step back in the trace and to the exception event.
4. Single step until teh code in question comes into scope.
5. Look at the local values and develop a hypthesis of a variable that may have an incorrect value.
6. Determine memory address of the variable with the incorrect value.
7. Seta memory access ba breakpoint on address of the suspect variable.
8. Use g- to run back to point of memory access.
9. See if that location or a few instructions before is the point of teh code flaw. If so, you are done.
If some other variable seems to set the value in teh first variable, set another break on access breakpoint on that variable 
10. Use g- to run back to point of memory access on the second suspect variable.
11. Repeat this process walking back until the code that made the error is located.
 


## <span id="Lab_objectives"></span><span id="lab_objectives"></span><span id="LAB_OBJECTIVES"></span>Lab objectives

After completing this lab you will be able to use the general procedure with a time travel trace to locate issues in code. 

## <span id="Lab_setup"></span><span id="lab_setup"></span><span id="LAB_SETUP"></span>Lab setup


You will need the following hardware to be able to complete the lab.

-   A laptop or desktop computer (host) running Windows 10

You will need the following software to be able to complete the lab.

-   Visual Studio to build the code 
-   The sample echo driver for Windows 10

The lab has the following eleven sections.

-   [Section 1: Connect to a kernel mode WinDbg session](#connectto)
-   [Section 2: Kernel mode debugging commands and techniques](#kernelmodedebuggingcommandsandtechniques)
-   [Section 3: Download and build the KMDF Universal Echo Driver](#download)
-   [Section 4: Install the KMDF Echo driver sample on the target system](#install)
-   [Section 5: Use WinDbg to display information about the driver](#usewindbgtodisplayinformation)
-   [Section 6: Display Plug and Play device tree information](#displayingtheplugandplaydevicetree)
-   [Section 7: Work with breakpoints and source code](#workingwithbreakpoints)
-   [Section 8: View variables and call stacks](#viewingvariables)
-   [Section 9: Display processes and threads](#displayingprocessesandthreads)
-   [Section 10: IRQL, Registers and Ending the WinDbg session](#irqlregistersmemory)
-   [Section 11: Windows debugging resources](#windowsdebuggingresources)

## <span id="CONNECTTO"></span>Section 1: Connect to a kernel mode WinDbg session


*In Section 1, you will configure network debugging on the host and target system.*

The PCs in this lab need to be configured to use an Ethernet network connection for kernel debugging.

This lab uses two PCs. Windows debugger runs on the *host* system and the KMDF Echo driver runs on the *target* system.

The "&lt;-Host" on the left is connected using a cross over ethernet cable to the "-&gt;Target" on the right.

---

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




