---
title: Trace Tree Pane
description: Trace Tree Pane
ms.assetid: 0035e926-7332-45a6-84ea-8c36bc23c61a
keywords: ["panes WDK Static Driver Verifier", "Static Driver Verifier Report WDK , Trace Tree pane", "Trace Tree pane WDK Static Driver Verifier", "tracing WDK Static Driver Verifier"]
---

# Trace Tree Pane


The **Trace Tree** pane displays a trace of the critical elements of the source code that were executed in the path to the rule violation, as shown in the following screen shot.

![screen shot of the trace tree pane displaying a trace of the critical elements of the source code that were executed in the path to the rule violation](images/sdv-tracetree.png)

These critical elements, such as function calls and assignments, come from all of the source files that were used to detect the rule violation, including SDV operating system model code (sdv-harness.c file), SDV rule source files (\*.slic), and the driver's source code. The code elements appear in the order that they were executed, even if they originated in different files.

SDV coordinates the display in the **Trace Tree** pane with the display in the [Source Code pane](source-code-pane.md) and the [State pane](state-pane.md). As you step through the source code in the **Trace Tree** pane, SDV automatically highlights the corresponding line of code in the **Source Code** pane and displays the values of variables at the corresponding point in the **State** pane.

This section includes:

[Understanding the Trace Tree Pane](understanding-the-trace-tree-pane.md)

[Color Coding in the Trace Tree Pane](color-coding-in-the-trace-tree-pane.md)

[Trace Tree Pane Actions](trace-tree-pane-actions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Trace%20Tree%20Pane%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




