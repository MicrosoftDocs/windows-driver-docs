Driver Model Settings Properties for Driver Projects
====================================================================================================================================

Sets the basic properties for a kernel-mode or user-mode driver, including the WDF library version and preprocessor definitions.

<span id="Setting_driver_model_properties_for_driver_projects"></span><span id="setting_driver_model_properties_for_driver_projects"></span><span id="SETTING_DRIVER_MODEL_PROPERTIES_FOR_DRIVER_PROJECTS"></span>Setting driver model properties for driver projects
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  Open the property pages for your driver project. Right-click the driver project in **Solution Explorer** and select **Properties**.
2.  In the property pages for the driver project, click **Configuration Properties** and then click **Driver Model Settings**.
3.  Set the properties for the project.

<span id="Type_of_driver"></span><span id="type_of_driver"></span><span id="TYPE_OF_DRIVER"></span>**Type of driver**  
The type of driver when the driver **Configuration type** is **Driver**. Note that this option is available only when projects use the **WindowsKernelModeDriver8.0** toolset.

Possible values are:

**WDM** (including all miniport/port drivers such as NDIS or StorPort).

**KDMF** A KMDF driver.

**Export driver (WDM)** A WDM driver that exports functions which other drivers can call. For more information, see [Creating Export Drivers](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff542891).

<span id="KMDF_Version_Major"></span><span id="kmdf_version_major"></span><span id="KMDF_VERSION_MAJOR"></span>**KMDF Version Major**  
When the type of driver is KMDF, this option specifies the major version of KMDF that will be used when compiling your driver.

The KMDF\_VERSION\_MAJOR entry informs the MSBuild utility that it must link the driver to the KMDF library.

You can build a KMDF driver for an earlier minor version of the library. For example, you could build a driver using KMDF Version Major=1 and KDMDF Version Minor=9 (KMDF Version 1.9) rather than 1.11 so that the driver could be shipped in a package containing an earlier version of the WDF co-installers.

For more information, see [Framework Library Versioning](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff542842).

<span id="KMDF_Version_Minor"></span><span id="kmdf_version_minor"></span><span id="KMDF_VERSION_MINOR"></span>**KMDF Version Minor**  
When the type of driver is KMDF, this option specifies the minor version of KMDF that will be used when compiling your driver.

For more information, see [Framework Library Versioning](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff542842) (11, 9, 7, 5). If you omit the KMDF Version Minor, the most recent minor version is used.

<span id="UMDF_Version_Major"></span><span id="umdf_version_major"></span><span id="UMDF_VERSION_MAJOR"></span>**UMDF Version Major**  
When you have a UMDF driver, this option specifies the major version of UMDF that will be used when compiling your driver. See [UMDF Version History](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff561356). When you have a UMDF driver, the **Configuration type** is **Dynamic Library (.dll)**.

<span id="UMDF_Version_Minor"></span><span id="umdf_version_minor"></span><span id="UMDF_VERSION_MINOR"></span>**UMDF Version Minor**  
When you have a UMDF driver, this option specifies the minor version of UMDF that will be used when compiling your driver (11, 9, 7, 5). If you omit the UMDF Version Minor, the most recent minor version is used.

<span id="Allow_Date__Time__and_Timestamp"></span><span id="allow_date__time__and_timestamp"></span><span id="ALLOW_DATE__TIME__AND_TIMESTAMP"></span>**Allow Date, Time, and Timestamp**  
Defines the standard C/CPP macros for \_\_DATE\_\_, \_\_TIME\_\_, \_\_TIMESTAMP\_\_.

<span id="Override_Target_Configuration_Preprocessor_Definitions"></span><span id="override_target_configuration_preprocessor_definitions"></span><span id="OVERRIDE_TARGET_CONFIGURATION_PREPROCESSOR_DEFINITIONS"></span>**Override Target Configuration Preprocessor Definitions**  
Overrides the default values for preprocessing symbols: \_WIN32\_WINNT, WINVER, WINNT, and NTDDI\_VERSION for your source file. Note that the default values are controlled by the current target configuration.

<span id="related_topics"></span>Related topics
-----------------------------------------------

* [Framework Library Versioning](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff542842)
* [Building and Loading a Framework-based Driver](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff540730)
* [UMDF Version History](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff561356)
* [Building UMDF Drivers](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff540730)
* [Creating Export Drivers](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff542891)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Driver%20Model%20Settings%20Properties%20for%20Driver%20Projects%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


