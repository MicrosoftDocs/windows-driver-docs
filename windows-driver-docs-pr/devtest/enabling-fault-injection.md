---
title: Enabling Fault Injection
description: Enabling Fault Injection
ms.assetid: 451a5e9e-bc5c-4148-b475-7f38c535cf6a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling Fault Injection


The WdfTester tool provides a WMI interface to configure DDI fault injection for a specific driver. A script (WdftesterScript.wsf) is provided that uses this WMI interface to configure fault injection. You can either write your own script or use the provided script to enable fault injection. You can run a script (WdftesterScript.wsf) from a Command Prompt window to register, configure, and unregister a driver. The script also has a command line option called **runtest**.

### <span id="what_the_runtest_option_does"></span><span id="WHAT_THE_RUNTEST_OPTION_DOES"></span>What the runtest option does

The **runtest** option executes simple disable and enable operations on a driver. This option demonstrates how to use the tool. At first, the script disables the specified driver and then enables it. This allows WdfTester to monitor all the DDI calls made during the disable and enable operations. The script uses one of the WMI interfaces to obtain the list of DDIs that were called during this period. The script determines which of these DDIs could be failed (only those that return NTSTATUS). The script then calls another WMI interface to configure WdfTester to fail the first DDI in the list. The script disables and enables the driver, which causes the DDI to fail and fire a WMI event. The script is already waiting on the WMI fail event for the DDI. If the event is received successfully and the failure hasn't caused the computer to become unresponsive or to cause a bug check (as determined by the driver developer or tester) the test is considered successful. The script then repeats these steps for next DDI in the list.

**Note**   The **runtest** option requires that you copy the [DevCon](devcon.md) (Devcon.exe) tool and place it in the same directory as other Wdftester files. The Devcon.exe application is located in the *%WDKRoot%*\\tools\\*&lt;platform&gt;* directory.

 

**The runtest option:**

1.  Registers your driver with WdfTester. If you have not installed your driver, you must install it before you use runtest.

2.  Enables Driver Verifier for this driver (computers running Windows Vista or later do not require a restart).

3.  Disables the driver by using the Devcon application.

4.  Enables the driver by using the Devcon application.

5.  Retrieves the names of the functions that were called during the enable and disable operations and identifies those functions that return NTSTATUS and that could be failed.

6.  Starts asynchronous WMI Event notification.

7.  For each DDI that could be failed from the list obtained in step 5:
    1.  Configures the function for failure.
    2.  Disables and then enables the driver by using Devcon.exe. This operation calls the function, and WdfTester fails the function call.
    3.  Waits on the WMI event to fire.
    4.  If the WMI event is fired, the **runtest** option repeats step 7 for the next function in the list.

8.  Unregisters the driver.

 

 





