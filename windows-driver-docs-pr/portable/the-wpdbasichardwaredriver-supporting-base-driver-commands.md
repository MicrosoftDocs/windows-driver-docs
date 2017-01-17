---
Description: 'Supporting the Base-Driver Commands'
MS-HAID: 'wpddk.the\_wpdbasichardwaredriver\_supporting\_base\_driver\_commands'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Supporting the Base-Driver Commands'
---

# Supporting the Base-Driver Commands


The base driver module for the sample (*WpdBaseDriver.cpp*) processes a single command (WPD\_COMMAND\_COMMON\_GET\_OBJECT\_IDS\_FROM\_ PERSISTENT\_UNIQUE\_IDS). However, this module is also the starting point for all command processing in the sample driver. This means that all commands are first processed by the **WpdBaseDriver::DispatchMessage** method. This method examines the category of a given command and then forwards it to the enumeration-, property-, or capability-command handler.

The one change that occurred in the **WpdBaseDriver::DispatchMessage** method was that the code that checks for resource-related commands was removed. Because the sample driver does not support resources, it was no longer necessary to process related commands; any application that sends non-implemented commands receives the E\_NOTIMPL error.

The information in the following table describes the command that is supported by the base driver module, together with the handler for the command.

| Command                                                               | Handler                              | Description                                                                                                              |
|-----------------------------------------------------------------------|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| WPD\_COMMAND\_COMMON\_GET\_OBJECT\_IDS\_FROM\_PERSISTENT\_UNIQUE\_IDS | OnGetOjectIDsFromPersistentUniqueIDs | Issued when an application attempts to retrieve the object identifier that matches a given persistent-unique identifier. |

 

## <span id="related_topics"></span>Related topics


****
[The WpdBasicHardwareDriverSample](the-wpdbasichardwaredriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Supporting%20the%20Base-Driver%20Commands%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




