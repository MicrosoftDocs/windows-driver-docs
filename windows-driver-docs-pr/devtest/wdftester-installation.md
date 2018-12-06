---
title: WdfTester Installation
description: WdfTester Installation
ms.assetid: 39645ca4-3f4e-4a1f-bf62-7b44856ce58e
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





