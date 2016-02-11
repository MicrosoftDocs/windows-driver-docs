
# Creating a log file for the code analysis tool

The Windows Server 2012 [Hardware Certification Program](http://go.microsoft.com/fwlink/p/?linkid=227016) requires a Driver Verification Log (DVL) for all applicable driver submissions. You must run the Code Analysis tool prior to creating a DVL for your driver. The DVL contains a summary of the results from the Code Analysis and Static Driver Verifier log files. The log files do not contain source code information.

![](common/wedge.gif)**To run code analysis on the driver**

1.  In Microsoft Visual Studio Ultimate 2012, select the driver project file and then right-click to open the project properties. Select **Windows 8 Release** as the **Configuration** and **x64** as the **Platform**.
2.  From the **Analyze** or **Build** menu, click **Run Code Analysis on Solution**.
3.  If errors or warnings are found, use the **Code Analysis Report** window to investigate the cause of the errors. Use the warning messages to fix those problems. For more information about the Code Analysis tool, see [How to run Code Analysis for drivers](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh454219) and [Analyzing C/C++ Code Quality by Using Code Analysis](http://go.microsoft.com/fwlink/p/?linkid=226836).

The Code Analysis tool for drivers writes the results to the file vc.nativecodeanalysis.all.xml in the build configuration and platform sub-directory of your project, for example, \\Windows 8Release\\x64.

<span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks
-------------------------------------------------------------------------------------

Code Analysis for Drivers is a compile-time static verification tool that detects basic coding errors in C and C++ programs and includes a specialized module that is designed to detect errors in (primarily) kernel-mode driver code. In previous versions of the WDK, the driver-specific module for code analysis was part of a stand-alone tool called PREfast for Drivers (PFD).

You can also run the Code Analysis tool from a Visual Studio Command Prompt window. Set up the environment by running one of the following batch files.

``` syntax
"C:\Program Files\Microsoft Visual Studio 11.0\VC\vcvarsall.bat" x64
```

-Or-

``` syntax
"C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\vcvarsall.bat" x64
```

Run the Code Analysis tool.

``` syntax
msbuild.exe <vcxprojectfile> /p:Configuration="Win8 Release" /P:Platform=x64 /target:clean
msbuild.exe <vcxprojectfile> /p:Configuration="Win8 Release" /P:Platform=x64 /P:RunCodeAnalysisOnce=True
```

For the most up-to-date information about the requirements for the Driver Verification Log, refer to the WDK Release Notes.

<span id="related_topics"></span>Related topics
-----------------------------------------------

* [Creating a driver verification log](creating_a_driver_verification_log.md)
* [Creating a log file for Static Driver Verifier](creating_a_log_file_for_static_driver_verifier.md)
* [Code Analysis for Drivers](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh454182)
* [Hardware Certification Program](http://go.microsoft.com/fwlink/p/?linkid=227016)
* [Analyzing C/C++ Code Quality by Using Code Analysis](http://go.microsoft.com/fwlink/p/?linkid=226836)
* [How to run Code Analysis for drivers](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh454219)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Creating%20a%20log%20file%20for%20the%20code%20analysis%20tool%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


