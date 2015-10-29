Creating a log file for Static Driver Verifier
========================================================================================================================

The Windows Server 2012 [Hardware Certification Program](http://go.microsoft.com/fwlink/p/?linkid=227016) requires a Driver Verification Log (DVL) for all applicable driver submissions. You must run [Static Driver Verifier](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff552808) (SDV) prior to creating a DVL for your driver. The DVL contains a summary of the results from the Code Analysis and Static Driver Verifier log files. The log files do not contain source code information.

For best results, run the Code Analysis tool before you run Static Driver Verifier.

![](../common/wedge.gif)**To create a log file for Static Driver Verifier**

1.  In Microsoft Visual Studio Ultimate 2012, select the driver project file and then right-click to open the project properties. Select **Windows 8 Release** as the **Configuration** and **x64** as the **Platform**.
2.  If you have already run the Code Analysis tool, follow these instructions for [running Static Driver Verifier](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh454281#running_static_driver_verifier#running_static_driver_verifier). For more information about using SDV, see Using Static Driver Verifier to Find Defects in Drivers
3.  If SDV finds defects in your driver, click the defect in the Results pane to view a trace of the code path that led to the rule violation. Fix any defects found in the driver and run SDV again.

Static Driver Verifier writes the results to the file SDV.DVL.xml in the SDV sub-directory of your project, for example, \\myDriverProject\\SDV.

<span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks
-------------------------------------------------------------------------------------

For the most up-to-date information about Static Driver Verifier and the Driver Verification Log, refer to the WDK Release Notes. The Release Notes are available on the [Windows Driver Kit (WDK) download page](http://go.microsoft.com/fwlink/p/?linkid=254897).

**Important**   Timeouts, spaceouts, and other non-successful results in the DVL file are acceptable for certification submission. This will not cause the Static Tools test in HCK to fail. For HCK 2.0, the Static Tools Test only requires the presence of DVL file to show Code Analysis and SDV had been run, and does not require all rules to pass.

 

You can also run Static Driver Verifier from a Visual Studio Command Prompt window. Set up the environment by running one of the following batch files.

``` syntax
"C:\Program Files\Microsoft Visual Studio 11.0\VC\vcvarsall.bat" x64
```

-Or-

``` syntax
"C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\vcvarsall.bat" x64
```

Run Static Driver Verifier.

``` syntax
msbuild.exe <vcxprojectfile> /p:Configuration="Win8 Release" /p:Platform=x64 /target:sdv /p:inputs="/clean"
msbuild.exe <vcxprojectfile> /p:Configuration="Win8 Release" /p:Platform=x64 /target:sdv /p:inputs="/check:default.sdv"
```

<span id="related_topics"></span>Related topics
-----------------------------------------------

* [Creating a driver verification log](creating_a_driver_verification_log.md)
* [Static Driver Verifier](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff552808)
* [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh454281)
* [Hardware Certification Program](http://go.microsoft.com/fwlink/p/?linkid=227016)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Creating%20a%20log%20file%20for%20Static%20Driver%20Verifier%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


