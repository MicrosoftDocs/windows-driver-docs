Analyzing a Driver Using Code Analysis and Verification Tools
==============================================================================================================================================

Code analysis and verification tools can help improve the stability and reliability of your driver by systematically analyzing the source code. The code analysis and verification tools can detect errors that are missed by the compiler and by conventional runtime testing. Additionally they can determine whether the driver correctly interacts with the Windows operating system kernel. Using Microsoft Visual Studio Ultimate 2012 and the Windows Driver Kit (WDK), you can configure the code analysis and verification tools to run as part of the build process, or you can schedule the tools to analyze your driver at a predetermined time.

<span id="C_C___Code_Analysis_Tool_for_Windows_Drivers"></span><span id="c_c___code_analysis_tool_for_windows_drivers"></span><span id="C_C___CODE_ANALYSIS_TOOL_FOR_WINDOWS_DRIVERS"></span>C/C++ Code Analysis Tool for Windows Drivers
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Windows 8 release of the WDK provides enhancements to the C/C++ Code Analysis tool included with Visual Studio. Specifically, the WDK provides a specialized driver module that is designed to detect errors in kernel-mode driver code. This driver module is integrated into the C/C++ Code Analysis tool.

**When to use:** You can run the C/C++ Code Analysis tool for drivers very early in the development cycle, as soon as the code compiles correctly.

For information about the Code Analysis tool in Visual Studio, see:

-   [Analyzing Application Quality using Code Analysis](http://go.microsoft.com/fwlink/p/?linkid=226836)
-   [Code Analysis for Drivers](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh454182)
-   [How to run Code Analysis for drivers](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh454219)
-   [Using SAL Annotations to Reduce C/C++ Code Defects](http://go.microsoft.com/fwlink/p/?linkid=247283)
-   [SAL 2.0 Annotations for Windows Drivers](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh454237)

**Note**  In previous versions of the WDK, the driver-specific module for code analysis was part of a standalone tool called PREfast for Drivers (PFD). PREfast for Drivers was also integrated into the WDK Build environment, as part of Microsoft Automated Code Review (OACR).

 

<span id="Static_Driver_Verifier"></span><span id="static_driver_verifier"></span><span id="STATIC_DRIVER_VERIFIER"></span>Static Driver Verifier
-------------------------------------------------------------------------------------------------------------------------------------------------

Static Driver Verifier (SDV) is a static verification tool that systematically analyzes the source code of Windows kernel-mode drivers. SDV determines whether the driver correctly interacts with the Windows operating system kernel. SDV can be launched from the **Driver** menu in Visual Studio or from the **Visual Studio Command Prompt** window.

**When to use:** Run Static Driver Verifier early in the development cycle on drivers that compile correctly. Run Static Driver Verifier before you begin the test cycle.

For information about Static Driver Verifier, see:

-   Overview: [Static Driver Verifier](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff552808)
-   How to: [Using Static Driver Verifier to find defects in drivers](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh454281)

**Note**  In previous versions of the WDK, Static Driver Verifier was a stand-alone tool that you launched from a WDK Build Environment window.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Analyzing%20a%20Driver%20Using%20Code%20Analysis%20and%20Verification%20Tools%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


