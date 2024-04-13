---
title: Configuring Object Reference Tracing
description: Configuring Object Reference Tracing
keywords: ["Object Reference Tracing, configuration"]
ms.date: 01/26/2021
---

# Configuring Object Reference Tracing


You can use Gflags to enable, disable, and configure the Object Reference Tracing feature of Windows. Object Reference Tracing records sequential stack traces whenever an object reference counter is incremented or decremented. The traces can help you to detect object reference errors, including double-dereferencing, failure to reference, and failure to dereference objects. This feature is supported only in Windows Vista and later versions of Windows. For detailed information about this feature, see [Object Reference Tracing](object-reference-tracing.md).

**To enable Object Reference Tracing**

1.  In the Gflags dialog box, select the **System Registry** tab or the **Kernel Flags** tab.

2.  In the Object Reference Tracing section, select **Enable**.

    You must limit the trace to objects with specified pool tags, to objects created by a specified process, or both.

3.  To limit the trace to objects with a particular pool tag, type the pool tag name. To list multiple pool tags, use semicolons (;) to separate the pool tags. When you list multiple pool tags, the trace includes objects with any of the specified pool tags. Pool tags are case sensitive. Use the [!pool](../debuggercmds/-pool.md) and [!poolfind](../debuggercmds/-poolfind.md) debugger commands to determine pool names.

    For example, Fred;Tag1.

4.  To limit the trace to objects that are created by a particular process, type the image name of the process. You can specify only one image file name.

    When you specify both pool tags and a process, the trace includes objects that are created by the process that have any of the specified pool tags.

5.  To retain the trace after the trace object is destroyed, select **Permanent**.

    When you select **Permanent**, the trace is retained until you disable object reference tracing, or shut down or restart Windows.

6.  Click **Apply** or **OK**.

The following screen shot shows Object Reference Tracing enabled on the **Kernel Flags** tab.

:::image type="content" source="images/gflags-obj.png" alt-text="Screenshot of object reference tracing enabled on the Kernel Flags tab in Gflags dialog box.":::

This trace will include only objects that were created by the notepad.exe process that have the pool tag **Fred** or **Tag1**. Because this is a run time (kernel flags) setting, the trace starts immediately. If it were a registry setting, you would have to restart Windows to start the trace.

**To disable Object Reference Tracing**

1.  In the Gflags dialog box, select the **System Registry** tab or the **Kernel Flags** tab. Object Reference Tracing will appear on the latter tab only in Windows Vista and later versions of Windows.

2.  In the Object Reference Tracing section, clear the **Enable** check box.

 

 