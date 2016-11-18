---
title: Understanding the Source Code Pane
description: Understanding the Source Code Pane
ms.assetid: 70be3322-fdbc-4d7e-880d-dcbc0fecc39f
keywords: ["Static Driver Verifier Report WDK , Source Code pane", "Source Code pane WDK Static Driver Verifier"]
---

# Understanding the Source Code Pane


The **Source Code** pane displays all of the source code files that are involved in detecting a rule violation, including SDV operating system model code (sdv-harness.c file), SDV rule code (\*.slic files), and the driver's source code.

The following screen shot shows an example **Source Code** pane.

![screen shot of the source code pane in the defect viewer](images/sdv-sourcecode.png)

Unlike the [Trace Tree pane](trace-tree-pane.md), the **Source Code** pane displays the entire file—not just the executed code elements—and it displays each source file on a separate tab. This arrangement makes it easy to determine the origin of the code elements in the trace. Source code files that are not involved in the rule violation do not appear in the **Source Code** pane, even if they are in the driver's sources directory.

SDV coordinates the display in the **Source Code** pane with the display in the **Trace Tree** pane and the [State pane](state-pane.md). As you step through the source code elements in the **Trace Tree** pane, SDV automatically highlights the line of code in the **Source Code** pane that contains the element and displays the values of variables at the corresponding point in the **State** pane.

Similarly, when you select a line of *executed* code in the **Source Code** pane, the highlight in the **Trace Tree** pane moves to the corresponding action elements from that line of code. Because the **Trace Tree** pane displays only code that is executed in the path to the rule violation, when you select a line of *unexecuted* code in the **Source Code** pane, the highlight in the **Trace Tree** pane moves to the top node (*main*).

The **Source Code** pane is a component of the Defect Viewer.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Understanding%20the%20Source%20Code%20Pane%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




