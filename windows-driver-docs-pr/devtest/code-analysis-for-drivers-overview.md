---
title: Code Analysis for drivers overview
description: The Windows Driver Kit provides a driver-specific extension to the Code Analysis tool in Microsoft Visual Studio Ultimate 2012.
ms.assetid: 2A780608-F386-4838-A4EB-022C2F0EED3B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Code Analysis for drivers overview


The Windows Driver Kit provides a driver-specific extension to the [Code Analysis tool](http://go.microsoft.com/fwlink/p/?linkid=226836) in Microsoft Visual Studio. The Code Analysis for Drivers includes rules that apply only to drivers, particularly kernel-mode drivers. Code Analysis for Drivers can detect potential errors in your code as soon as the code can be compiled.

## <span id="How_the_Code_Analysis_tool_works"></span><span id="how_the_code_analysis_tool_works"></span><span id="HOW_THE_CODE_ANALYSIS_TOOL_WORKS"></span>How the Code Analysis tool works


The Code Analysis tool intercepts the build utility's call to the standard compiler, Cl.exe and, instead, runs a CL intercept compiler that analyzes the driver source code and creates a log file of error and warning messages. You can run the Code Analysis tool by itself, or you can configure the Code Analysis tool to run when you build your driver. When you run the Code Analysis tool by itself (**Analyze &gt; Run Code Analysis on Solution**) the results appear in the Code Analysis Report window. When you run the Code Analysis tool as part of the build, the CL intercept compiler creates a log file of error and warning messages and then it calls the standard version of Cl.exe to produce the build output. The resulting object files are the same as those produced by a standard build command.

When the intercepting compiler runs, Code Analysis for Drivers examines each function in the code independently and then simulates the execution of all possible paths through the code, looking for common driver errors and unwise coding practices. The Code Analysis tool runs relatively quickly, even on larger drivers, and the report that it generates precisely identifies the line of driver code with the suspected error.

## <span id="The_types_of_errors_Code_Analysis_can_detect"></span><span id="the_types_of_errors_code_analysis_can_detect"></span><span id="THE_TYPES_OF_ERRORS_CODE_ANALYSIS_CAN_DETECT"></span>The types of errors Code Analysis can detect


Code Analysis can detect several types of errors, including errors in the following categories:

-   **Memory:** Potential memory leaks, dereferenced **NULL** pointers, access to uninitialized memory, excessive use of the kernel-mode stack, and improper use of pool tags.

-   **Resources:** Failure to release resources such as locks, resources that should be held when calling some functions, and resources that should not be held when calling other functions.

-   **Function use:** Potentially incorrect use of certain functions, function arguments that appear incorrect, possible argument type mismatches for functions that do not strictly check types, possible use of certain obsolete functions, and function calls at a potentially incorrect IRQL.

-   **Floating-point state:** Failure to protect the floating-point hardware state in a driver and attempting to restore the floating-point state after saving it at a different IRQL.

-   **Precedence rules:** Code that might not behave as the programmer intended because of the precedence rules of C programming.

-   **Kernel-mode coding practices:** Coding practices that can cause errors, such as modifying an opaque memory descriptor list (MDL) structure, failing to examine the value of a variable set by a called function, and using C/C++ string manipulation functions rather than the safe string functions defined in Ntstrsafe.h.

-   **Driver-specific coding practices:** Specific operations that are often a source of errors in kernel-mode drivers. For example, copying a whole I/O request packet (IRP) without modifying members and saving a pointer to a string or structure argument instead of copying an argument in a [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine.

## <span id="Code_Analysis_warnings"></span><span id="code_analysis_warnings"></span><span id="CODE_ANALYSIS_WARNINGS"></span>Code Analysis warnings


The Code Analysis tool uses a rule-based model to identify errors in the program or driver code. Each rule is associated with a warning that is reported if the Code Analysis tool detects a violation of the rule. For detailed information about the driver-specific warnings, see [Code Analysis for Drivers Warnings](prefast-for-drivers-warnings.md). For information about the core set of warnings that the Code Analysis tool in Visual Studio reports, see [Code Analysis Warnings](http://go.microsoft.com/fwlink/p/?linkid=226853).

## <span id="Annotations"></span><span id="annotations"></span><span id="ANNOTATIONS"></span>Annotations


One of the important capabilities that the Code Analysis tool provides is the ability to annotate function descriptions and some other entities in the source code of the driver. The Code Analysis tool has an intra-functional scope; that is, it analyzes the interactions between functions. The objective of the annotations is to provide a more complete expression of the contract between the called and calling functions, so that the Code Analysis tool can check that the contract is met. Another goal of the annotations is that they inform whoever reads the code how the function should be used and what results can be expected. The annotations declare the contract of the interface and do not attempt to describe how that contract is achieved. In many cases, the results from running the Code Analysis tool reflect the absence of an appropriate annotation, and by adding the annotation, both the warning about the missing annotation is suppressed, and additional checks are enabled. For more information, see [SAL 2.0 Annotations for Windows Drivers](sal-2-annotations-for-windows-drivers.md). More information about SAL 2.0, see [Using SAL Annotations to Reduce C/C++ Code Defects](http://go.microsoft.com/fwlink/p/?linkid=247283). SAL 2.0 replaces SAL 1.0. SAL 2.0 should be used with the WDK for Windows 8. If you need information about SAL 1.0 for drivers, refer to the PREfast for Drivers Annotations documentation that shipped with the WDK for Windows 7.

## <span id="Interpreting_the_result"></span><span id="interpreting_the_result"></span><span id="INTERPRETING_THE_RESULT"></span>Interpreting the result


Code Analysis for Drivers is easy to run and it runs quickly, even on very large drivers and programs. The work for the developer is in examining the output, analyzing the errors that the Code Analysis tool detected, and distinguishing real coding errors from valid code that the Code Analysis tool misinterpreted.

For a comprehensive reference that describes each warning that the Code Analysis tool might detect, see [Code Analysis for Drivers Warnings](prefast-for-drivers-warnings.md). For information about the core set of warnings that the Code Analysis tool in Visual Studio reports, see [Code Analysis Warnings](http://go.microsoft.com/fwlink/p/?linkid=226853).

Resolving a code analysis warning typically involves either updating the source code when appropriate, or adding an annotation to clarify the function contract. Adding an annotation allows the analyzer to enforce the contract for all future callers, and it also improves readability.

If the **Code Analysis Results** shows errors that you determine, after careful examination, are invalid and cannot be avoided even with the use of annotations, you can choose to exclude or suppress these warnings. For more information, see [How to run Code Analysis for drivers](how-to-run-code-analysis-for-drivers.md).

## <span id="related_topics"></span>Related topics


[How to run Code Analysis for drivers](how-to-run-code-analysis-for-drivers.md)

[Code Analysis tool in Visual Studio](http://go.microsoft.com/fwlink/p/?linkid=226836)

[Code Analysis for Drivers Warnings](prefast-for-drivers-warnings.md)

[Code Analysis Warnings](http://go.microsoft.com/fwlink/p/?linkid=226853)

[SAL 2.0 Annotations for Windows Drivers](sal-2-annotations-for-windows-drivers.md)

 

 






