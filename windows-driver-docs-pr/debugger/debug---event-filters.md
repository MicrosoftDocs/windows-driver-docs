---
title: Debug Event Filters
description: Debug Event Filters
ms.assetid: ffa1241a-8a75-44ac-94b7-608393cf4138
keywords: ["Debug Event Filters", "exceptions, Debug Event Filters", "events, Debug Event Filters"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debug | Event Filters


## <span id="ddk_debug_event_filters_dbg"></span><span id="DDK_DEBUG_EVENT_FILTERS_DBG"></span>


Click **Event Filters** on the **Debug** menu to open the **Event Filters** dialog box. In this dialog box, you can configure the break status and handling status of exceptions and events.

### <span id="dialog_box"></span><span id="DIALOG_BOX"></span>Dialog Box

The **Event Filters** dialog box lists all events that the debugger recognizes. You may add numbered exceptions to the list that will then be displayed.

To change the break status for an event, select the event and then click one of the **Execution** option buttons (**Enabled**, **Disabled**, **Output**, or **Ignore**).

To change the handling status for an event, select the event and then click one of the **Continue** option buttons (**Handled** or **Not Handled**).

To add a new numbered exception, click **Add**. When the **Exception Filter** dialog box appears, enter the exception code, click the appropriate button for the break status and handling status, and then click **OK**.

To remove a numbered exception, select the exception and then click **Remove**. You cannot remove the standard events.

When you set the status for the **Load module** or **Unload module** events, you can limit this status to a specific module. Click **Argument**, enter the name of the module or the base address of the module in the **Filter Argument** dialog box, and then click **OK**. You can use [wildcards](string-wildcard-syntax.md) when you specify the base address. If you do not specify a module, the break occurs when any module is loaded or unloaded.

When you set the status for the **Debuggee output** event, you can limit this status to a specific output pattern. Click **Argument**, enter the output pattern in the **Filter Argument** dialog box, and then click **OK**. If you do not specify an output pattern, the break occurs for any output.

If you want to set automatic commands that are executed if the event breaks into the debugger, select the event and then click **Commands**. The **Filter Command** dialog box will appear. Enter any commands that you want into the **Command** or **Second-chance Command** box. Separate multiple commands by using semicolons and do not enclose these commands in quotation marks.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about break status and handling status, all event codes, the default status for all events, and other methods of controlling this status, see [Controlling Exceptions and Events](controlling-exceptions-and-events.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debug%20|%20Event%20Filters%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




