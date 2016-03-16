---
title: Determining Why the Reflector Terminated the Host Process
description: This topic describes how you can analyze why the reflector terminated the driver host process (WUDFHost.exe).
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: c80b117b-597a-494a-bc28-5a918d2a9279
keywords: ["debugging scenarios WDK UMDF reflector terminates the host process", "UMDF WDK debugging scenarios reflector terminates the host process", "UMDF WDK reflector terminates the host process"]
---

# Determining Why the Reflector Terminated the Host Process


This topic describes how you can analyze why the reflector terminated the driver host process (WUDFHost.exe).

The most common reason for the reflector to terminate the host process is the expiration of UMDF [host process timeouts](how-umdf-enforces-time-outs.md).

## <a href="" id="post-mortem-analysis-using-dump-files"></a>Using Dump Files


For many crashes, dump file details are sufficient to determine why the termination occurred. To review dump file information, follow these steps:

1.  Locate the latest .dmp file in the %windir%\\system32\\LogFiles\\WUDF directory.

    **Note**  Starting in UMDF 2.15, the log directory is *%ProgramData%*\\Microsoft\\WDF.

     

2.  Load the latest .dmp file into the debugger by using the following command:
    <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>WinDbg -z &lt;path to the .dmp file&gt;</code></pre></td>
    </tr>
    </tbody>
    </table>

3.  Look at the state of the threads at the time of termination.

## <a href="" id="live-debugging"></a>Using the Debugger


In other cases, you might need to attach to a live kernel-mode target to determine why the reflector terminated the host process. To set up your debugging session, follow the steps described in [How to Enable Debugging of a UMDF Driver](enabling-a-debugger.md#kd).

Once you have established a connection, display the outstanding IRPs by using the [**!wdfkd.wdfumirps**](https://msdn.microsoft.com/library/windows/hardware/dn265384) UMDF debugger extension ([**!wudfext.umirps**](https://msdn.microsoft.com/library/windows/hardware/ff566197) for UMDF version 1).

-   If a PnP IRP or a power IRP is pending, determine why the driver causes the IRP to hang by examining threads in the host process.

    You can use the [**!process**](https://msdn.microsoft.com/library/windows/hardware/ff564717) extension to examine the threads running in the host process. The **0x1f** flags value shows you the stack trace for each thread.

    **!process** *&lt;process addr&gt;* **0x1f**

-   If your driver has not completed a canceled IRP quickly, determine which IRP was canceled and why it has not completed.
-   If a cleanup or close IRP is pending, determine why the IRP is taking a long time to process.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Determining%20Why%20the%20Reflector%20Terminated%20the%20Host%20Process%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




