---
title: Debug Event Filters
description: Debug Event Filters
ms.assetid: ffa1241a-8a75-44ac-94b7-608393cf4138
keywords: ["Debug Event Filters", "exceptions, Debug Event Filters", "events, Debug Event Filters"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
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

 

 





