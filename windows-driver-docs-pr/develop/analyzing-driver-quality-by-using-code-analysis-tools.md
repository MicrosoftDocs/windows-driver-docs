---
ms.assetid: 0FEF982B-7FEE-47C8-A906-F881E9D8F3D7
title: Analyzing a Driver Using Code Analysis and Verification Tools
description: Code analysis and verification tools can help improve the stability and reliability of your driver by systematically analyzing the source code.
ms.date: 07/02/2018
ms.localizationpriority: medium
---

# Analyzing a Driver Using Code Analysis and Verification Tools

Code analysis and verification tools can help improve the stability and reliability of your driver by systematically analyzing the source code. The code analysis and verification tools can detect errors that are missed by the compiler and by conventional runtime testing. Additionally they can determine whether the driver correctly interacts with the Windows operating system kernel. Using Microsoft Visual Studio and the Windows Driver Kit (WDK), you can configure the code analysis and verification tools to run as part of the build process, or you can schedule the tools to analyze your driver at a predetermined time.

## <span id="C_C___Code_Analysis_Tool_for_Windows_Drivers"></span><span id="c_c___code_analysis_tool_for_windows_drivers"></span><span id="C_C___CODE_ANALYSIS_TOOL_FOR_WINDOWS_DRIVERS"></span>C/C++ Code Analysis Tool for Windows Drivers


The Windows 8 release of the WDK provides enhancements to the C/C++ Code Analysis tool included with Visual Studio. Specifically, the WDK provides a specialized driver module that is designed to detect errors in kernel-mode driver code. This driver module is integrated into the C/C++ Code Analysis tool.

**When to use:** You can run the C/C++ Code Analysis tool for drivers very early in the development cycle, as soon as the code compiles correctly.

For information about the Code Analysis tool in Visual Studio, see:

-   [Analyzing Application Quality using Code Analysis](http://go.microsoft.com/fwlink/p/?linkid=226836)
-   [Code Analysis for Drivers](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454182)
-   [How to run Code Analysis for drivers](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454219)
-   [Using SAL Annotations to Reduce C/C++ Code Defects](http://go.microsoft.com/fwlink/p/?linkid=247283)
-   [SAL 2.0 Annotations for Windows Drivers](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454237)

**Note**  In previous versions of the WDK, the driver-specific module for code analysis was part of a standalone tool called PREfast for Drivers (PFD). PREfast for Drivers was also integrated into the WDK Build environment, as part of Microsoft Automated Code Review (OACR).

 

## <span id="Static_Driver_Verifier"></span><span id="static_driver_verifier"></span><span id="STATIC_DRIVER_VERIFIER"></span>Static Driver Verifier


Static Driver Verifier (SDV) is a static verification tool that systematically analyzes the source code of Windows kernel-mode drivers. SDV determines whether the driver correctly interacts with the Windows operating system kernel. SDV can be launched from the **Driver** menu in Visual Studio or from the **Visual Studio Command Prompt** window.

**When to use:** Run Static Driver Verifier early in the development cycle on drivers that compile correctly. Run Static Driver Verifier before you begin the test cycle.

For information about Static Driver Verifier, see:

-   Overview: [Static Driver Verifier](https://msdn.microsoft.com/Library/Windows/Hardware/Ff552808)
-   How to: [Using Static Driver Verifier to find defects in drivers](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454281)


 

 

 





