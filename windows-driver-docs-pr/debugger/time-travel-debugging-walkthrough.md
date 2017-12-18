---
title: Time Travel Debugging - Sample App Walkthrough
description: This section contains a walk through of a small C++ app. 
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>


# ![Small time travel logo showing clock](images/ttd-time-travel-debugging-logo.png) Time Travel Debugging - Sample App Walkthrough


This lab introduces Time Travel Debugging (TTD), using a small sample program with a code flaw. TTD is used to debug, identify and root cause the issue. Although the issue in this small program is easy to find, the general procedure can be used on more complex code. This general procedure can be summarized as follows.

1. Capture a time travel trace of the failed program.
2. Use the dx command to determine the exception event stored in the recording. 
3. Use time travel to postion the trace at the exception event.
4. From that point in the trace single step backwards until the faulting code in question comes into scope.
5. With the faulting code in scope, look at the local values and develop a hypothesis of a variable that may contain an incorrect value.
6. Determine the memory address of the variable with the incorrect value.
7. Set a memory access (ba) breakpoint on address of the suspect variable.
8. Use g- to run back to point of memory access of the suspect variable.
9. See if that location, or a few instructions before, is the point of the code flaw. If so, you are done.
If some other variable sets the value in the first variable, set another break on access breakpoint on the second variable. 
10. Use g- to run back to point of memory access on the second suspect variable. See if that location or a few instructions before contains the code flaw. If so, you are done.
11. Repeat this process walking back until the code that set the incorrect value that caused the error is located.
 
Although the general techniques included in this procedure apply to a broad set of code issues, there are unique code issues that will require a unique approach. The techniques illustrated in the walkthrough should serve to expand your debugging tool set and will illustrate some of what is possible with a TTD trace.


## <span id="Lab_objectives"></span><span id="lab_objectives"></span><span id="LAB_OBJECTIVES"></span>Lab objectives

After completing this lab, you will be able to use the general procedure with a time travel trace to locate issues in code. 


## <span id="Lab_setup"></span><span id="lab_setup"></span><span id="LAB_SETUP"></span>Lab setup

You will need the following hardware to be able to complete the lab.

-   A laptop or desktop computer (host) running Windows 10 

You will need the following software to be able to complete the lab.

-   The WinDbg Preview. For information on installing WinDbg Preview, see [WinDbg Preview - Installation](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/windbg-install-preview)
-   Visual Studio to build the sample C++ code. 

The lab has the following three sections.

-   [Section 1: Build the sample code](#build)
-   [Section 2: Record a trace of the "DisplayText" sample](#record)
-   [Section 3: Analyze the trace file recording to identify the code issue](#analyze)


## <span id="build"></span>Section 1: Build the sample code

*In Section 1, you will build the sample code using Visual Studio.*

**Create the sample app in in Visual Studio**

1.  In Microsoft Visual Studio, click **File** &gt; **New** &gt; **Project/Solution...** and click on the Visual **C++** templates. 
    
    Select the Win32 Console Application.

    Provide a project name of *DisplayText* and click on **OK**.

    The default settings are fine for our purposes, so click on **Finish**, to accept the defaults.

2. Paste in the following text to the DisplayText.cpp Window.

```
// DisplayText.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <array>
#include <stdio.h>
#include <string.h>

int DetermineStringSize()
{
       printf("Determining String Size \n");
       // ToDo Implement String size - for now all supported strings are 15.
       int buffsize = 15;
       int WideCharBuffSize = 4;
       int CharBuffSizeFactor = 2;
       int NarrowCharBuffSize = WideCharBuffSize/CharBuffSizeFactor;
       char NotNull = ' ';
       char VeryNull = NULL;
       char ExtraSpace = NotNull;
       return buffsize;
}

int DisplayText()
{
                printf("Displaying Text \n");
                wchar_t const* const message = L"Message text to display goes here";
                size_t size = DetermineStringSize();
                wchar_t* buffer = NULL;
                wcscpy_s(buffer, size, message);
                return 0;
}


int main()
{
    printf("Calling Displaying Text \n");
    DisplayText();
                return 0;
}

```

3.  In Visual Studio, click **Build** &gt; **Build Solution**.

    If all goes well, the build windows should display a message indicating that the build succeeded.

4.  **Locate the built sample app files**

    In the Solution Explorer, right click on the *DisplayText* project and select **Open Folder in File explorer**.
    
    Navigate to the Debug folder that contains the complied exe and symbol pdb file for the sample. For example, you would navigate to *C:\Projects\DisplayText\Debug*, if that's the folder that your projects are stored in. 

5. **Run the sample app with the code flaw**

    Click on the exe file to run the sample app.


    ![Faulting app dialog box](images/ttd-time-travel-walkthrough-faulting-app-dialog-box.png) 


    Click on **Retry**, to see if our app will make any forward progress.

    If this dialog box appears, select **Close program**


   ![Faulting app dialog box](images/ttd-time-travel-walkthrough-program-not-working-dialog-box.png) 
    
    
    In the next section of the walkthrough, we will record the execution of the sample app to see if we can determine why this exception is occurring. 


## <span id="record"></span>Section 2: Record a trace of the "DisplayText" sample

*In Section 2, you will record a trace of the misbehaving sample "DisplayText" app*

To launch the sample app and record a TTD trace, follow these steps. For general information about recording TTD traces, see [Time Travel Debugging - Record a trace](time-travel-debugging-record.md)

1. Run WinDbg Preview as an Administrator, so as to be able to record time travel traces.

2. In WinDbg Preview, select **File** > **Start debugging** > **Launch executable (advanced)**.

3. Enter the path to the user mode executable that you wish to record or select **Browse** to navigate to the executable. For information about working with the Launch Executable menu in WinDbg Preview, see [WinDbg Preview - Start a user-mode session](windbg-user-mode-preview.md).


    ![Screen shot of WinDbg Preview showing start recording checkbox in launch executable (advanced) screen](images/ttd-time-travel-walkthrough-recording-app.png)


4. Check the **Record process with Time Travel Debugging** box to record a trace when the executable is launched. 

5. Click **OK** to launch the executable and start recording. 

6. The recording dialog appears indicating the trace is being recorded. Shortly after that, the application crashes.

7. Click on **Retry**, to allow the code to try and run.

8. The program crashes and the trace file will be closed and written out to disk. 

   ![Screen shot of WinDbg Preview showing output with 10/16 keyframes indexed](images/ttd-time-travel-walkthrough-windbg-indexed-frames.png)

9. The debugger will automatically index the trace file. Indexing allows for more accurate and faster memory value look ups. This indexing process will take longer for larger trace files.

    ```
    0:000> !index
    Indexed 10/15 keyframes
    Indexed 15/15 keyframes
    Successfully created the index in 525ms.
     ```
   
   > [!NOTE]
   > A keyframe is a location in a trace used for indexing. Keyframes are generated automatically. Larger traces will contain more keyframes. 
   >   
 
10. At this point you are at the beginning of the trace file and are ready to travel forward and backward in time.

   Now that you have a recorded a TTD trace, you can replay the trace back or work with the trace file, for example sharing it with a co-worker. For more information about working with trace files, see [Time Travel Debugging - Working with Trace Files](time-travel-debugging-trace-file-information.md)

In the next section of this lab we will analyze the trace file to locate the issue with our code.


## <span id="analyze"></span>Section 3: Analyze the trace file recording to identify the code issue

*In Section 3, you will analyze the trace file recording to identify the code issue.*

**Configure the WinDbg Environment**

1.  Add your local symbol location to the symbol path and reload the symbols, by typing the following commands.

    ```
    .sympath+ C:\Projects\DisplayText\Debug
    .reload /f
    ```

2.  Add your local code location to the source path by typing the following command.

    ```
    .srcpath C:\Projects\DisplayText\DisplayText
    ```

3.  On the WinDbg Preview ribbon, select **Source** and **Open Source File**. Locate the DisplayText.cpp file and open it.

**Examine the exception**

1. When the trace file was loaded is displays information that exception occurred. 

    ```
    (2b2c.2bbc): Break instruction exception - code 80000003 (first/second chance not available)
    Time Travel Position: 15:0
    eax=662ea6e0 ebx=00000000 ecx=76f566ac edx=68fa4afc esi=68fa137c edi=0116b000
    eip=76f566ac esp=012ff668 ebp=012ff8b8 iopl=0         nv up ei pl nz na po nc
    cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00000202
    ntdll!LdrpInitializeProcess+0x1d1c:
    76f566ac 83bdbcfeffff00  cmp     dword ptr [ebp-144h],0 ss:002b:012ff774=00000000
    ```
2. Use the dx command to list all of the events in the recording. The exception event is listed in the events.

    ```
    0:000> dx -r1 @$curprocess.TTD.Events
    ...
    [0x2c]           : Module Loaded at position: 9967:0
    [0x2d]           : Exception at 9BDC:0
    [0x2e]           : Thread terminated at 9C43:0
    ...
    ```

3. Click on the Exception event to display information about that TTD event. 

    ```
    0:000> dx -r1 @$curprocess.TTD.Events[45]
    @$curprocess.TTD.Events[45]                 : Exception at 9E0D:0
    Type             : Exception
    Position         : 9E0D:0 [Time Travel]
    Exception        : Exception of type Hardware at PC: 0XC42142
    ```

4. Click on the link to time travel to that position.

    ```
    0:000> dx -r1 @$curprocess.TTD.Events[45]
    @$curprocess.TTD.Events[45]                 : Exception at 9E0D:0
    Type             : Exception
    Position         : 9E0D:0 [Time Travel]
    Exception        : Exception of type Hardware at PC: 0XC42142
    ```



**Examine the exception**

1.  Use the **dv** command to display the current local variables in memory.

    ```
    0:000> dv
      _Expr_val = 0n0
    destination = 0x00000000 ""
    size_in_elements = 0xf
    source = 0x00d475d0 "Message text to display goes here"
    available = 0xcccccccc
    destination_it = 0xcccccccc "--- memory read error at address 0xcccccccc ---"
    source_it = 0xcccccccc "--- memory read error at address 0xcccccccc ---"
    ```

    The output shows that there is likely a problem with the destination_it and source\_it.

2. Looking at our code, it looks like the exception may be caused by the bad parameters being passed to the wcscpy_s in this line of code.

    ```
    wcscpy_s(buffer, size, message);
    ```

3. To investigate further we will set a breakpoint by clicking on the wcscpy_s line in the source window.

  ![Screen shot of source Window showing breakpoint set on wcscpy_s](images/ttd-time-travel-walkthrough-source-window-breakpoint.png)


4. Use g- to travel back until the breakpoint is hit.

   ```
   Breakpoint 0 hit
   Time Travel Position: 5B:AF
   eax=0000000f ebx=00c20000 ecx=00000000 edx=00000000 esi=013a1046 edi=00effa60
   eip=013a17c1 esp=00eff970 ebp=00effa60 iopl=0         nv up ei pl nz na po nc
   cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00000202
   DisplayText!DisplayText+0x41:
   013a17c1 8bf4            mov     esi,esp
   ```


5. Use the **dv** command to display the current local variables in memory.

   ```
   0:000> dv
         buffer = 0x00000000 ""
           size = 0xf
        message = 0x00d475d0 "Message text to display goes here"
 
   ```

7. Looking at the value of *size* it is 0xf - 15 and our string looks to be 32 in length, so this looks like the reason that the wscpy is failing. But how did *size* get set to 15? To answer that question, we will set an break on memory access breakpoint. 

    > [!NOTE]
    > In this very small sample it would be pretty easy to just look in the code, but if there are hundreds of lines of code and dozens of subroutines the techniques described here can be used to decrease the time necessary to locate the issue.


**TTD and breakpoints**

Using breakpoints is a common approach to pause code execution at some event of interest.  Unique to TTD, you can set a breakpoint and travel back in time until that breakpoint is hit after the trace has been recorded. The ability to examine the process state after an issue has happened, to determine the best location for a breakpoint, enables additional debugging workflows unique to TTD. 

**Setting memory access breakpoints**

You can set breakpoints that fire when a memory location is accessed. Use the **ba** (break on access) command, with the following syntax.

```
ba <access> <size> <address> {options}
```

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>e</p></td>
<td align="left"><p>execute (when CPU fetches an instruction from the address)</p></td>
</tr>
<tr class="even">
<td align="left"><p>r</p></td>
<td align="left"><p>read/write (when CPU reads or writes to the address)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>w</p></td>
<td align="left"><p>write (when the CPU writes to the address)</p></td>
</tr>
</tbody>
</table>

 
Note that you can only set four data breakpoints at any given time and it is up to you to make sure that you are aligning your data correctly or you won’t trigger the breakpoint (words must end in addresses divisible by 2, dwords must be divisible by 4, and quadwords by 0 or 8).


**Setting the break on access breakpoint for the size variable**    

1.  Use the **dx** command to examine the symbols associated with *size*. 

    ```
    0:000> dx &size
    0053fdd4          size = 0xf
    ```

    In this trace *size* is located in memory at 0053fdd4. 


2.  First clear the existing breakpoints, then set the memory access breakpoint with the **ba** command using the address we want to monitor. Lastly use **bl** to list the breakpoints to confirm they are set as intended.

    ```
    0:000> bc *
    0:000> ba w4 0053fdd4
    0:000> bl
      0 e Disable Clear  0053fdd4 w 4 0001 (0001)  0:**** 
    ```

3.  Use g- command to travel back in time until the breakpoint is hit.

    ```
    0:000> g-
    Breakpoint 0 hit
    Time Travel Position: 5B:92
    eax=0000000f ebx=003db000 ecx=00000000 edx=00cc1a6c esi=00d41046 edi=0053fde8
    eip=00d4174a esp=0053fcf8 ebp=0053fde8 iopl=0         nv up ei pl nz ac pe nc
    cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00000216
    DisplayText!DisplayText+0x3a:
    00d4174a c745e000000000  mov     dword ptr [ebp-20h],0 ss:002b:0053fdc8=cccccccc
    ```

5. Use the **dv** command to display the current local variables in memory.

   ```
   0:000> dv
         buffer = 0x00000000 ""
           size = 0xf
        message = 0x00d475d0 "Message text to display goes here"
 
   ```

4. Single step backwards until the faulting code in question comes into scope. In this case, we can use p- command to travel back one step as the breakpoint leaves us one step after the code of interest has executed.

    ```
    0:000> p-
    Time Travel Position: 5B:91
    eax=0000000f ebx=003db000 ecx=00000000 edx=00cc1a6c esi=00d41046 edi=0053fde8
    eip=00d41747 esp=0053fcf8 ebp=0053fde8 iopl=0         nv up ei pl nz ac pe nc
    cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00000216
    DisplayText!DisplayText+0x37:
    00d41747 8945ec          mov     dword ptr [ebp-14h],eax ss:002b:0053fdd4=cccccccc
    ```

7. Use the source window to examine the line of code that we have hit.

    ```
    size_t size = DetermineStringSize();
    ```
    In this line of code we see that *size* is set by calling DetermineStringSize(). 

8.  We will use a similar approach to find the address of the DisplayText!DetermineStringSize function, and set a breakpoint on memory access. Because the function will just be read from memory for execution, we need to set a r - read breakpoint.

    ```
    0:000> dx &DisplayText!DetermineStringSize
    00d41f60          DisplayText!DetermineStringSize (void)
    0:000> bc * 
    0:000> ba r4 00d41f60
    0:000> bl
     0 e Disable Clear  00d41f60 r 4 0001 (0001)  0:**** DisplayText!DetermineStringSize
    ```

9.  Use g- command to travel back in time until the breakpoint is hit.

    ```
    0:000> g-
    Breakpoint 0 hit
    Time Travel Position: 5B:92
    eax=0000000f ebx=003db000 ecx=00000000 edx=00cc1a6c esi=00d41046 edi=0053fde8
    eip=00d4174a esp=0053fcf8 ebp=0053fde8 iopl=0         nv up ei pl nz ac pe nc
    cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00000216
    DisplayText!DisplayText+0x3a:
    00d4174a c745e000000000  mov     dword ptr [ebp-20h],0 ss:002b:0053fdc8=cccccccc
    ``'

9. As the DetermineStringSize function is not large, we could just look at the code to find the issue. If this was a large function, we could look at the last line of code that returns the final value to see how that value is set.

    ```
    return buffsize;
    ```
    
    This is where the incorrect value of 0xf is returned, but how did buffsize get set to the incorrect value? We can set another breakpoint to find out.

8.  Use the **dx** command to examine  *buffsize*. 

    ```
    0:000> dx &buffsize
    0053fde0          buffsize = 0n13923792
    ```

    In this trace, *buffsize* is located in memory at 0053fdd4. 


9.  Set the breakpoint with the **ba** command using the address we now want to monitor. 

    ```
    bc *
    ba w4 0053fde0 
    ```
           

10. Use g- to run back to point of memory access of the suspect buffsize variable.

   ```
   0:000> g-
   Breakpoint 0 hit
   Time Travel Position: 5B:9C
   eax=cccccccc ebx=002b1000 ecx=00000000 edx=68d51a6c esi=013a1046 edi=001bf7d8
   eip=013a1735 esp=001bf6b8 ebp=001bf7d8 iopl=0         nv up ei pl nz na po nc
   cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00000202
   DisplayText!DetermineStringSize+0x25:
   013a1735 c745ec04000000  mov     dword ptr [ebp-14h],4 ss:002b:001bf7c4=cccccccc
   ```
      

11. It looks like we have found the root cause. The ToDo comment indicates that the string size has not been implemented and 15 (0xf) is always returned.

   ```
   // ToDo Implement String size - for now all supported strings are 15.
      int buffsize = 15;
   ```

**Summary**      

In this very small sample the issue could have been determined by looking at the few lines of code, but in larger programs the techniques presented here can be used to decrease the time necessary to locate an issue. 

Once a trace is recorded, the trace and repro steps can be shared, and the issue will be reproducible on demand.  


---

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

[Time Travel Debugging - Recording](time-travel-debugging-record.md)

[Time Travel Debugging - Replay a trace](time-travel-debugging-replay.md)

[Time Travel Debugging - Working with trace files](time-travel-debugging-trace-file-information.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




