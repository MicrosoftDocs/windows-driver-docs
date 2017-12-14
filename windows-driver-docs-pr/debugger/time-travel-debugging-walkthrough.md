---
title: Time Travel Debugging - Sample App Walkthrough
description: This section contains a walk through of a small C++ app. 
ms.author: windowsdriverdev
ms.date: 12/13/2017
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
-   Visual Studio to build the sample C++ code. 

The lab has the following three sections.

-   [Section 1: Build the sample code](#build)
-   [Section 2: Record a trace of the sample "DisplayText" code](#record)
-   [Section 3: Analyze the trace file recording to indentify the code issue](#analyze)


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
                // ToDo Implment String size - for now all supported strings are 15.
                int buffsize = 15;
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
    DisplayText();
                return 0;
}

```

3.  In Visual Studio, click **Build** &gt; **Build Solution**.

    If all goes well, the build windows should display a message indicating that the build succeeded.

4.  **Locate the built sample app files**

    In the Solution Explorer, right click on the *DisplayText* project and select **Open Folder in File explorer**.
    
    Navigate to the Debug folder that contains the complied exe and symbol pdb file for the sample. For example, you would navigate to *C:\Users\UserName\Documents\Visual Studio 2017\Projects\DisplayText\Debug*, if that's the folder that your projects are stored in. 

5. **Run the sample app with the code flaw**

    Click on the exe file to run the sample app.

    ![Screen Shot of faulting app dialog box](images/ttd-time-travel-walkthrough-faulting-app-dialog-box.png) 

    Click on **Ignore**, to see if our app will make any forward progress.
    
    In the next section of the walkthrough, we will record the execution of the sample app to see if we can determine why this exception is occuring. 


## <span id="record"></span>Section 2: Record a trace of the sample "DisplayText" code

*In Section 2, you will record a trace of the misbeavhing sample "DisplayText" app*

To launch the sample app and record a TTD trace, follow these steps. For general information about recording TTD traces, see [Time Travel Debugging - Record a trace](time-travel-debugging-record.md)

1. In WinDbg Preview, select **File** > **Start debugging** > **Launch executable (advanced)**.

2. Enter the path to the user mode executable that you wish to record or select **Browse** to navigate to the executable. For information about working with the Launch Executable menu in WinDbg Preview, see [WinDbg Preview - Start a user-mode session](windbg-user-mode-preview.md).


    ![Screen shot of WinDbg Preview showing start recording checkbox in launch executable (advanced) screen](images/ttd-time-travel-walkthrough-recording-app.png)

3. Check the **Record process with Time Travel Debugging** box to record a trace when the executable is launched. 

4. Click **OK** to launch the executable and start recording. 

5. The recording dialog appears indicating the trace is being recorded. Shortly after that, the application crashes.

6. Click on **Retry**, to allow the exception handling code to run.

7. The program crashes and the trace file will be closed and written out to disk. 

   ![Screen shot of WinDbg Preview showing output with 16/16 keyframes indexed](images/ttd-time-travel-walkthrough-windbg-indexed-frames.png)

8. The debugger will automatically index the trace file. Indexing allows for more accurate and faster memory value look ups. This indexing process will take longer for larger trace files.

    ```
    0:000> !index
    Indexed 10/15 keyframes
    Indexed 15/15 keyframes
    Successfully created the index in 525ms.
     ```
   
   > [!NOTE]
   > A keyframe is a location in a trace used for indexing. Keyframes are generated automatically. Larger traces will contain more keyframes. 
   >   
 
9. At this point you are at the beginning of the trace file and are ready to travel forward and backward in time.

   Now that you have a recorded a TTD trace, you can replay the trace back or work with the trace file, for example sharing it with a co-worker. For more information about working with trace files, see [Time Travel Debugging - Working with Trace Files](time-travel-debugging-trace-file-information.md)

In the next section of this lab we will analyze the trace file to locate the issue with our code.


## <span id="analyze"></span>Section 3: Analyze the trace file recording to indentify the code issue

*In Section 3, you will analyze the trace file recording to indentify the code issue.*

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

1. When the trace file was loaded is displays information that exception ocurred. 

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

    The output shows that there may be a problem with the destination_it and source\_it.

2.  Use p- command to travel back one step.


    ```

**Set a breakpoint**

    > [!TIP]
    > Using breakpoints is a common approach to pause code execution at some event of interest.  Unique to TTD, you can set a breakpoint and travel back in time until that breakpoint is hit after the trace has been recorded. The ability to examine the process state after an issue has happened, to determine the best location for a breakpoint, enables additional debugging workflows. 


**Note**  
**Setting memory access breakpoints**

You can also set breakpoints that fire when a memory location is accessed. Use the **ba** (break on access) command, with the following syntax.

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


4.  Altough we could look in code, We will use the **x** command to examine the symbols associated with the display text program to determine the function name to use for the breakpoint. 

    ```
    x DisplayText!Disp*
    00d41710          DisplayText!DisplayText (void)
    ```

    The output above shows that **DisplayText** method for our DisplayText program is located at 00d41710. 

    Alternatively, we could review the source code to locate the desired function name for our breakpoint.

5.  Set the breakpoint with the **ba** command using the address we want to monitor. 

    ```
    ba w8 00d41710 
    ```
     

6.  List the current breakpoints to confirm that the breakpoint was set by typing the **bl** command.

    ```
    0: kd> bl
    1 e fffff801`0bf9b1c0     0001 (0001) ECHO!EchoEvtDeviceAdd
    ```

    The "e" in the output shown above indicates that the breakpoint number 1 is enabled to fire.


7.  Restart code execution on the target system by typing the **go** command **g**.

12. Step through the code line-by-line by typing the **p** command or pressing F10 until you reach the following end of the [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine. The Brace character “}” will be highlighted as shown.

7.  When the test app runs, the I/O routine in the driver will be called. This will cause the breakpoint to fire, and execution of the driver code on the target system will halt.

    ```
    Breakpoint 2 hit
    ECHO!EchoEvtIoWrite:
    fffff801`0bf95810 4c89442418      mov     qword ptr [rsp+18h],r8
    ```
`

3. Step back in the trace to the exception event.

   ```

   ```
      

4. From that point single step backwards until the faulting code in question comes into scope.

   ```

   ```
      

5. With the faulting code in scope, look at the local values and develop a hypthesis of a variable that may contain an incorrect value.

   ```

   ```
      

6. Determine the memory address of the variable with the incorrect value.

   ```

   ```
      

7. Set a memory access (ba) breakpoint on address of the suspect variable.

   ```

   ```
      

8. Use g- to run back to point of memory access of the suspect variable.

   ```

   ```
      

9. See if that location or a few instructions before is the point of the code flaw. If so, you are done.
If some other variable sets the value in the first variable, set another break on access breakpoint on the second variable. 

   ```

   ```
      

10. Use g- to run back to point of memory access on the second suspect variable. See if that location or a few instructions before contains the code flaw. If so, you are done.

   ```

   ```
      

11. Repeat this process walking back until the code that created the error, by settng the incorrect value is located.


   ```

   ```
      


---

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




