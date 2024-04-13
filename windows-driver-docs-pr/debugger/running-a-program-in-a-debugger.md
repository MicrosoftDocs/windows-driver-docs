---
title: Running a Program in a Debugger
description: Running a Program in a Debugger
keywords: ["GFlags, running a program in a debugger"]
ms.date: 05/23/2017
---

# Running a Program in a Debugger


## <span id="ddk_running_a_program_in_a_debugger_dtools"></span><span id="DDK_RUNNING_A_PROGRAM_IN_A_DEBUGGER_DTOOLS"></span>


This feature configures the program so that it always runs in a debugger with the specified options. This setting is saved in the registry. It affects all new instances of the program and remains effective until you change it.

**To run a program in a debugger**

1.  Click the **Image File** tab.

2.  In the **Image** box, type the name of an executable file or DLL, including the file name extension,and then press the TAB key.

    This activates the check boxes on the **Image File** tab.

3.  Click the **Debugger** check box to select it.

    The following screen shot shows the **Debugger** check box on the **Image File** tab in Windows Vista.

    :::image type="content" source="images/gflags-debugger.png" alt-text="Screenshot of the Debugger check box on the Image File tab in Windows Vista.":::

4.  In the **Debugger** box, type the command to run the debugger, including the path (optional) and name of the debugger and parameters. For example, **ntsd -d -g -G -x** or **c:\\debuggers\\cdb.exe -g -G**.

5.  Click **Apply**.

 

 