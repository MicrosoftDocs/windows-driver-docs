Creating a Driver From Existing Source Files
====================================================================================================================

The WDK is integrated with Microsoft Visual Studio, and uses the same compiler and build tools that you use to build Visual Studio solutions and projects. [MSBuild](http://go.microsoft.com/fwlink/p/?linkid=262804) replaces the Windows Build Utility (Build.exe) that was used in versions of the WDK prior to Windows Driver Kit (WDK) 8.

To convert a driver that was created with a previous version of the WDK, create a new Windows driver solution in Visual Studio using one of the provided Windows driver templates. If you start with a template for your driver model, the structure of the project will be in place and the correct platform tool set will be selected. You can then add your source files to the solution. For information about selecting templates, see [Creating a New Device Function Driver](creating_a_new_driver.md), [Creating a New Filter Driver](creating_a_new_filter_driver.md), or [Creating a New Software Driver](creating_a_new_software_driver.md).

<span id="related_topics"></span>Related topics
-----------------------------------------------

* [WDK and the Visual Studio build environment](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh454286)
* [ProjectUpgradeTool](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Dn265174)
* [MSBuild](http://go.microsoft.com/fwlink/p/?linkid=262804)
* [Walkthrough: Using MSBuild](http://go.microsoft.com/fwlink/p/?linkid=262807)
* [Creating a New Device Function Driver](creating_a_new_driver.md)
* [Creating a New Filter Driver](creating_a_new_filter_driver.md)
* [Creating a New Software Driver](creating_a_new_software_driver.md)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Creating%20a%20Driver%20From%20Existing%20Source%20Files%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


