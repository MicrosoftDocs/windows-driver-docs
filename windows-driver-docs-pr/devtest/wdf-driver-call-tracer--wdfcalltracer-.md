---
title: WDF Driver Call Tracer (WdfCallTracer)
description: WDF Driver Call Tracer (WdfCallTracer)
ms.assetid: 67ad4b5e-9117-435e-bd81-90069a806d3c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDF Driver Call Tracer (WdfCallTracer)


You can use WdfCallTracer to trace and view driver communication with framework in real time. WdfCallTracer is the name of a functionality and not a separate executable file (There is no separate binary for this.).

Using this functionality, you can view the DDI and event calls in real time.

The following procedure shows you how to can configure WdfTester by using the driver communication for the KMDF Static Bus Driver Sample (Statbus.sys available in the WDK). Currently only the DDI calls can be viewed.

**To set up WDF Driver Call Tracer and build the sample driver**

1.  Install [WdfTester Installation](wdftester-installation.md).

2.  Build the KMDF static bus driver sample (Statbus.sys). The KMDF sample is located in the *%WDKRoot%*\\src\\general\\toaster\\toastDrv\\kmdf\\bus\\static directory.

3.  Copy the bus driver sample to the directory that contains the WdfTester files that you installed. Load the driver by following the instructions for the KMDF Toaster samples. Use [DevCon](devcon.md) (Devcon.exe) or the **Add New Hardware Wizard**.

Use the following procedure to configure TraceView so that you can view the DDI and event calls in real time

**To create a new log session in TraceView**

1.  Start TraceView.exe (*%WDKRoot%*\\tools\\*&lt;platform&gt;*).

2.  From the **File** menu, click **Create New Log Session**.

3.  In the **Create New Log Session** dialog box, click **Add Provider**.

4.  In the **Provider Control GUID Setup** dialog box, click **CTL (Control GUID) File**.

5.  Click the **Browse** button, and select Wdftester.ctl file from the directory that contains WdfTester files and your driver.

6.  Click **OK**.

7.  In the **Format Information Source Select** dialog box, click **Select TMF Files**, and click **OK**.

8.  In the **Trace Format Information Setup** dialog box, click **Add,** and then browse to the directory where the WdfTester files are located.

9.  Click Wdftester.tmf, click **Open** to select the file, and then click **Done**.

10. Click **Next** in the **Create New Log Session** dialog box, and then click **Finish**.

Now you are ready to register the driver and enable tracing so that you can view the driver communication.

**To register the KMDF driver and enable tracing**

1.  Open a Command Prompt window and change to the directory where you installed the Wdftester files.

2.  Register the KMDF driver (in this example, Statbus.sys) by using the WdftesterScript.wsf script.
    ```
    cscript WdftesterScript.wsf register statbus.sys
    ```

3.  Enable the driver from Device Manager, or plug in your hardware. If your driver was already enabled, use Device Manager to disable it, and then enable it again.

You should now see driver communication in the TraceView application.

 

 





