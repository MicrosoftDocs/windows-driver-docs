---
title: WdfTester Installation
description: WdfTester Installation
ms.assetid: 39645ca4-3f4e-4a1f-bf62-7b44856ce58e
---

# WdfTester Installation


Before you can run the WdfTester tool on your driver, you must first copy the WdfTester files to a working directory and run an installation script.

**To install WdfTester**

1.  Copy the following list of files from the WDK (*%WDKRoot%*\\tools\\*&lt;platform&gt;*) to a local folder that contains a copy of your driver binary.
    Wdftester.sys
    Wdftester.inf
    Wdftester.ctl
    Wdftester.tmf
    WdftesterScript.wsf
2.  Open a Command Prompt window (be sure to **Run as Administrator** on Windows Vista), and then type the following command:cscript WdfTesterScript.wsf install

    This command installs the Wdftester.sys driver and starts the service.

3.  Press Enter.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20WdfTester%20Installation%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




