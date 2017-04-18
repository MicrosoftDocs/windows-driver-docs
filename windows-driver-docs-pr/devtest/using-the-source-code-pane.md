---
title: Using the Source Code Pane
description: Using the Source Code Pane
ms.assetid: da8d16cd-583f-42b0-857f-64e5103aa379
keywords: ["Static Driver Verifier Report WDK , Source Code pane", "Source Code pane WDK Static Driver Verifier"]
---

# Using the Source Code Pane


Use the **Source Code** pane to determine the origin of each line of code in the path to a rule violation.

As you step through the code elements in the [Trace Tree pane](trace-tree-pane.md), the cursor in the **Source Code** pane automatically moves to the originating line of code, switching quickly between files as necessary. To determine which file is being displayed, find the file name on the topmost tab in the **Source Code** pane, or use the [color coding](color-coding-in-the-source-code-pane.md) as a visual cue.

To determine the effect of a line of executed driver source code on the state of the verification or on the trace, first click that line of code in the **Source Code** pane so that the code elements from that line are highlighted in the **Trace Tree** pane. Next, use the **Trace Tree** pane to step through the lines of code that follow it, while watching for changing values in the [State Pane](state-pane.md).

To find the functions that SDV is monitoring for the rule and identify actions that might change the values in the [State Pane](state-pane.md), you can read the rule source code (*RuleName*.slic) files in the **Source Code** pane.

You can use the **Source Code** pane to read any file, but the cursor steps through the code line by line; not in the order of execution.

You can also copy the code from any tab of the **Source Code** pane and paste it into an application that supports rich text format (RTF) files, such as Microsoft Word or WordPad. To copy the code, from the **Edit** menu, select **Select All** and then, from the **Edit** menu, select **Copy**. Or, press CTRL+A (select all) and then CTRL+C (copy).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Using%20the%20Source%20Code%20Pane%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




