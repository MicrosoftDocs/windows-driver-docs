---
title: Understanding the Trace Tree Pane
description: Understanding the Trace Tree Pane
ms.assetid: 98640d7e-29fc-4397-ac6b-47f4e17f88a1
keywords: ["Static Driver Verifier Report WDK , Trace Tree pane", "Trace Tree pane WDK Static Driver Verifier"]
---

# Understanding the Trace Tree Pane


The **Trace Tree** pane is the focus of the Defect Viewer. Typically, you step through the code in the **Trace Tree** pane, while watching its effect on the code in the **Source Code** pane and on the values in the **State** pane.

The **Trace Tree** pane is organized into a hierarchical structure with a series of expandable and collapsible nodes. The hierarchy indicates the code elements that caused other elements to be executed. This format helps you to interpret each code branch and to display and hide code sections easily as you step through the trace.

The following screen shot shows an example **Trace Tree** pane.

![screen shot of the trace tree pane in the defect viewer](images/sdv-tracetree.png)

Each code element in the **Trace Tree** pane is preceded by its line number in the source file. This numbering helps you find the code element in the Source Tree window and in the source file.

Some lines of code in the **Source Code** pane correspond to more than one element in the **Trace Tree** pane. This situation occurs when the line of code causes more than one action. For example, if a function call parameter is an IRQL, the line of code that includes the function call might also include a call to find the current IRQL, such as:

```
IoReleaseCancelSpinLock(KeGetCurrentIrql());
```

In this situation, the **Trace Tree** pane would include a critical element for the [**KeGetCurrentIrql**](https://msdn.microsoft.com/library/windows/hardware/ff552054) function call, a few calls to the SDV operating system model to randomly generate an IRQL, and then a call to [**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550) with the returned IRQL.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Understanding%20the%20Trace%20Tree%20Pane%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




