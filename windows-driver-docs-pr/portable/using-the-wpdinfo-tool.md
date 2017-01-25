---
Description: Using the WpdInfo Tool
MS-HAID: 'wpddk.using\_the\_wpdinfo\_tool'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Using the WpdInfo Tool
---

# Using the WpdInfo Tool


The *WpdInfo.exe* tool is a Windows-based application that you can use to test the functionality in your driver. You can use this tool to perform the following tasks:

-   Open or close a device
-   Create or delete an object on the device
-   Create, save, or delete an object resource
-   Send a command to the device
-   View the supported device commands
-   View the supported device content types
-   View the supported events
-   View the supported properties
-   View the attributes of a given resource
-   View the attributes of a given property
-   Perform bulk property operations
-   Open or close a device service
-   Invoke a method on a device service

When you start the tool, it prompts you to choose one of the available WPD devices.

![wpdinfo device selection](images/wpdinfo1.png)

After you choose a device, a connection is established and the WpdInfo application windows are initialized. The upper-left frame of the main window displays the hierarchy of supported objects. The upper-right frame displays resource data that is associated with the object that is currently selected. The lower-middle pane displays the properties that are supported by the object. The pane at the bottom of the window displays any error information returned by the driver during a given operation.

![wpdinfo default screens](images/wpdinfo2.png)

You can right-click a given object, resource, or property to display a menu of options that apply to the selected element. For example, you can right-click an object that appears in the upper-left pane to delete it, operate on its resources, view associated properties and so on.

![wpdinfo options](images/wpdinfo3.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Using%20the%20WpdInfo%20Tool%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



