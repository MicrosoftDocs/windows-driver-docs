---
title: Creating a Trace Session for a Registered Provider
description: Creating a Trace Session for a Registered Provider
ms.assetid: 3013b5fa-5390-4d46-b138-4ddcda468ddf
keywords: ["registered providers WDK software tracing"]
---

# Creating a Trace Session for a Registered Provider


## <span id="ddk_create_a_trace_session_for_a_registered_provider_tools"></span><span id="DDK_CREATE_A_TRACE_SESSION_FOR_A_REGISTERED_PROVIDER_TOOLS"></span>


To monitor the trace messages of a [registered provider](registered-provider.md), do the following:

1.  [Start TraceView](starting-and-exiting-traceview.md).

2.  On the **File** menu, click **Create New Log Session**.

3.  Click **Add Provider**.

4.  Click **Named Provider**, and then click the ellipsis button (**...**) beside the **Named Provider** text box.

    In the **Named Provider Selection** dialog box, TraceView displays the registered providers in the system.

5.  Select a registered provider, and then click **OK**.

6.  Do one of the following:
    -   To specify one or more TMF files , click **Select TMF Files**, click **OK**, click **Add**, and then browse to and select one or more TMF files from the directory. To select TMF files from another directory, click the **Add** button again. Otherwise, click **Done**.
    -   To direct TraceView to search for the TMF files in a specified directory, click **Set TMF Search Path**, click **OK**, browse to the directory, and then click **OK**.

7.  To add additional providers of any type, click **Add Provider**. This step is optional.

8.  Click **Next**.

9.  [Set basic trace session options](setting-basic-trace-session-options.md), if desired.

10. [Set advanced trace session options](setting-advanced-trace-session-options.md), if desired.

11. Click **Finish**.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

For information about specifying TMF files, see Select TMF Files and Set TMF Search Path.

To set flags and a level for a registered provider, see [Setting Advanced Trace Session Options](setting-advanced-trace-session-options.md).

The "Windows Kernel Trace" provider that appears in the list of named providers is better known as the [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md). You can use the **Named Provider Selection** dialog box to create an NT Kernel Logger trace session, but this dialog box does not allow you to select the kernel components that are traced. Instead, it selects the default components (process, thread, disk, and network). To select the trace components, use the TraceView interface that is customized for NT Kernel Logger trace sessions.

The TMF file for the Windows Kernel Trace, system.tmf, is included in the WDK. Click **Select TMF Files**, click **Add**, navigate to the \\tools\\tracing\\i386 subdirectory, and then select system.tmf.

For more information, see [Creating an NT Kernel Logger trace session](creating-an-nt-kernel-logger-trace-session.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Creating%20a%20Trace%20Session%20for%20a%20Registered%20Provider%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




