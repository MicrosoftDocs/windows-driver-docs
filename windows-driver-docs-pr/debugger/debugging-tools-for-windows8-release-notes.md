---
title: Debugging Tools For Windows8 Release Notes
description: Debugging Tools For Windows8 Release Notes
ms.assetid: 15776778-691F-4F76-92CE-2DB266AD31E8
---

# Debugging Tools For Windows8 Release Notes


## <span id="Channel_number_for_1394_debugging_in_Visual_Studio"></span><span id="channel_number_for_1394_debugging_in_visual_studio"></span><span id="CHANNEL_NUMBER_FOR_1394_DEBUGGING_IN_VISUAL_STUDIO"></span>Channel number for 1394 debugging in Visual Studio


If you use Microsoft Visual Studio to perform kernel-mode debugging over a 1394 cable, set the channel to a decimal integer between 1 and 62 inclusive. Do not set the channel to 0 when you first set up debugging. Because the default channel value is 0, the software assumes there is no change and does not update the settings. If you must use channel 0, first use an alternate channel (1 through 62) and then switch to channel 0.

## <span id="Inline_function_debugging_is_on_by_default"></span><span id="inline_function_debugging_is_on_by_default"></span><span id="INLINE_FUNCTION_DEBUGGING_IS_ON_BY_DEFAULT"></span>Inline function debugging is on by default


In Windows 8, debugging of inline functions is turned on by default. The command **.inline 0** turns off inline function debugging, and the command **.inline 1** turns on inline function debugging.

## <span id="Invalid_port_number_in_configuration_page_for_network_debugging"></span><span id="invalid_port_number_in_configuration_page_for_network_debugging"></span><span id="INVALID_PORT_NUMBER_IN_CONFIGURATION_PAGE_FOR_NETWORK_DEBUGGING"></span>Invalid port number in configuration page for network debugging


**Issue:** If an invalid port number is entered in the configuration page for kernel-mode network debugging, the configuration succeeds but the debugger on the host computer cannot connect to the target computer.

**Workaround:** Make sure the port number is valid. Valid port numbers range from 49152–65535. Also, your company might have restrictions on which ports can be used for network debugging. To ensure that a valid port number is entered, please check your internal IP Security Policy.

## <span id="use_of_.remote_tool_in_command_line"></span><span id="USE_OF_.REMOTE_TOOL_IN_COMMAND_LINE"></span>Use of .remote tool in command line


**Issue:** The use of **.remote** tool in the command line crashes the interface as it creates old style remote.exe using npipe.

**Workaround:** Use the **.server** command instead.

## <span id="Design_features_for_Visual_Studio"></span><span id="design_features_for_visual_studio"></span><span id="DESIGN_FEATURES_FOR_VISUAL_STUDIO"></span>Design features for Visual Studio


-   Automatic provisioning of a machine includes both user mode and kernel mode bootstrapping, regardless of which one is chosen. This requires two restarts for provisioning and takes between 8–20 minutes.
-   Support for attaching only one process at a time.
-   During a debugging session in Windows Debugger Extension for Visual Studio, exceptions are managed using the command line.

## <span id="Global_design_features"></span><span id="global_design_features"></span><span id="GLOBAL_DESIGN_FEATURES"></span>Global design features


-   User must run in an elevated context in order to install the USB 3.0 XHCI filter driver. If the user is not running elevated, the PnP manager returns an error message that does not inform the user that elevation is the problem.
-   If kernel debugging is enabled, the device used for kernel debugging should not be removed from the system while the device is still turned on. If the device is removed, the system will hang and will need to be restarted.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Tools%20For%20Windows8%20Release%20Notes%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




