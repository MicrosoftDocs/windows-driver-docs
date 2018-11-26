---
title: How to run Code Analysis for drivers
description: Code Analysis for Drivers provides information about possible defects in the source code. You can run code analysis manually, and you can also run code analysis automatically with each build.
ms.assetid: BDD4EC2C-FB23-44BE-9A52-F98774AC7268
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to run Code Analysis for drivers


Code Analysis for Drivers provides information about possible defects in the source code. You can run code analysis manually, and you can also run code analysis automatically with each build.

In this topic:

-   [Running code analysis](#running-code-analysis)
-   [Viewing the code analysis results](#viewing-the-code-analysis-results)
-   [Suppressing the report of defects](#suppressing-the-report-of-defects)
-   [Changing stack usage limits for warning C6262 for kernel-mode drivers](#changing-stack-usage-limits-for-warning-c6262-for-kernel-mode-drivers)
-   [Related topics](#related-topics)

## Running code analysis


**To run code analysis on driver source code manually**

1.  In Visual Studio, select the driver project file or solution and select the project configuration and platform to analyze.
2.  From the **Analyze** or **Build** menu, click **Run Code Analysis on Solution**.

**To run code analysis on driver source code automatically with each build**

1.  In Visual Studio, right-click the driver project or solution in **Solution Explorer** and click **Properties**.
2.  In the properties dialog box for the project, click **Code Analysis**.
3.  In the **Code Analysis for C/C++ Properties** page, select the project configuration and platform that you want to analyze (for example, Windows 8 and Win32).
4.  Select **Enable Code Analysis for C/C++ on Build**.
5.  Under Rule set, select **Microsoft Driver Recommended Rules**. This is the default rule set for drivers.
6.  In the **Build** menu, click **Build Solution**.

## Viewing the code analysis results


If possible defects are found in the source code, the **Code Analysis Results** window displays the code analysis warning number and the line number in the source file where the defect occurs.

**To view defects**

1.  In the **Code Analysis Results** window, click the line number and a description of the defect is displayed in the **Code Analysis Results** window.

    The Code window displays the source code and indicates where the defect occurs.

2.  To find out more about a particular warning, click the Warning in the **Code Analysis Results** window.

**To view the code analysis log file associated with a build**

1.  Navigate to the directory for your build configuration and platform (for example, \\Windows7Release\\x64).
2.  If you use the recommended rules, the log file is called vc.\*codeanalysis.xml. If you are creating a driver for Windows Server 2012, this file is used to create the Driver Verification log.

## Suppressing the report of defects


In some cases, you might want to suppress the report of a particular warning messages; for example, if the warning is primarily informational and you know the cause of the error.

**To suppress warning messages**

1.  To remove an instance of a reported defect, select the line number and warning in the **Code Analysis Results** window.
2.  In the expanded description of the warning, click **Actions** &gt; **Suppress Message** &gt; **In source**.

    A pragma warning directive with the suppress specifier suppresses the warning only for the line of code that immediately follows the \#pragma warning statement.

    ```
    #pragma warning(suppress: 6014)
    ```

## Changing stack usage limits for warning C6262 for kernel-mode drivers


In user-mode and kernel-mode code, stack space is limited, and failure to commit a page of stack causes a stack overflow exception. High stack usage is particularly a concern in kernel mode because the total stack space available is only 12 KB. Kernel-mode code should aggressively limit stack use.

The Code Analysis tool issues warning [C6262](http://go.microsoft.com/fwlink/p/?linkid=321750) if more than 1 KB of stack space is used locally in a function. If you want to investigate functions that might potentially be resource intensive, you can customize or lower the stack threshold limit used by [C6262](http://go.microsoft.com/fwlink/p/?linkid=321750). If you lower the stack threshold limit, the Code Analysis tool can potentially find more problems. You can then choose to address those stack usage issues. For example, you could lower the threshold to 400 bytes, to see if other functions are using resources.

**To customize the stacksize limit for C6262**

1. Open the Visual Studio project file (.vcxproj) for your kernel-mode driver (or component) in Notepad or another text editor.
2. Add a new **&lt;ItemDefinitionGroup&gt;** for the compiler **&lt;ClCompile&gt;**.
3. Add the **&lt;PREfastAdditionalOptions&gt;** element and set the **stacksize**<em>&lt;bytes&gt;</em>. The default value is **stacksize1024**.
   ```XML
     <ItemDefinitionGroup>
       <ClCompile>



      <!-- Change stack depth for C6262 from 1024 to 400 -->
      <PREfastAdditionalOptions>stacksize400</PREfastAdditionalOptions>

    </ClCompile>
  </ItemDefinitionGroup>


```


4.  Save the project file. Start Visual Studio, load the updated driver project, and run code analysis.

    To revert to the default of 1 KB, undo the changes you made to the project file, or change the stack size value to **stacksize1024**.

## Related topics


[Code Analysis for Drivers Warnings](prefast-for-drivers-warnings.md)










