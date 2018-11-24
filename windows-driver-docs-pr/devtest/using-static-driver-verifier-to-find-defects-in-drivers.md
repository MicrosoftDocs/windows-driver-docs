---
title: Using Static Driver Verifier to Find Defects in Windows Drivers
description: Static Driver Verifier (SDV) uses a set of interface rules and a model of the operating system to determine if the driver interacts correctly with the Windows operating system.
ms.assetid: 94D4104C-66ED-4C1E-8EE1-4C669EB4EAAD
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Static Driver Verifier to Find Defects in Windows Drivers


Static Driver Verifier (SDV) uses a set of interface rules and a model of the operating system to determine if the driver interacts correctly with the Windows operating system. SDV finds defects in driver code that could point to potential bugs in drivers.

SDV can analyze kernel-mode drivers that conform to one of the following driver models: WDM, KMDF, NDIS, or Storport. For more information, see [Supported Drivers](supported-drivers.md) and [Determining if Static Driver Verifier supports your driver or library](determining-if-static-driver-verifier-supports-your-driver-or-library.md).  Additionally, SDV provides limited support (a severely restricted rule set focused on general errors such as null dereferences) for drivers that do not follow the above driver models.

### <span id="preparing_your_source_code"></span><span id="PREPARING_YOUR_SOURCE_CODE"></span>

| Preparing your source code |
|----------------------------|
|                            |

Use the following steps to prepare your code for analysis.

1.  **Declare driver-supplied functions by using function role types**

    SDV requires that the functions be declared by using function role type declarations. For example, a [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine must be declared by using the DRIVER\_INITIALIZE function role type:

    ```
    DRIVER_INITIALIZE DriverEntry;
    ```

    After the declaration, you implement (or define) your callback routine as follows:

    ```
    /
    // Driver initialization routine
    //
    NTSTATUS 
      DriverEntry( 
        _In_ struct _DRIVER_OBJECT  *DriverObject,
        _In_ PUNICODE_STRING  RegistryPath 
        )
      {
          // Function body
      }
    ```

    Each supported driver model has a set of function role types for the driver callback functions and dispatch routines. These function role types are declared in the WDK header files. For example, here is the function prototype for the DRIVER\_INITIALIZE role type as it appears in Wdm.h.

    ```
    /
    // Define driver initialization routine type.
    //
    _Function_class_(DRIVER_INITIALIZE)
    _IRQL_requires_same_
    typedef
    NTSTATUS
    DRIVER_INITIALIZE (
        _In_ struct _DRIVER_OBJECT *DriverObject,
        _In_ PUNICODE_STRING RegistryPath
        );

    typedef DRIVER_INITIALIZE *PDRIVER_INITIALIZE;
    ```

    Because the function role types are already defined in the WDK header files, you only need to declare your callback functions to be of that type. In this case, you declare *DriverEntry* to be of type **DRIVER\_INITIALIZE**. For a complete list of the function role types for the driver models, see [Using Function Role Type Declarations](using-function-role-type-declarations.md).

2.  **Run Code Analysis for C/C++**

    To help you determine whether the source code is prepared, run the [Code Analysis tool](http://go.microsoft.com/fwlink/p/?linkid=226836) in Visual Studio. The Code Analysis tool checks for function role type declarations, which SDV requires. The Code Analysis tool can help identify any function declarations that might have been missed or warn you when the parameters of the function definition do not match those in the function role type.

    -   Open your driver project in Visual Studio.
    -   From the **Build** menu, click **Run Code Analysis on Solution**.

    The results are displayed in the **Code Analysis** window. Fix any function declarations that you might have missed. You can also configure the Code Analysis tool so that it runs whenever you build your solution.

    The following table shows some of warnings that the Code Analysis tool might find in your driver code. To run Static Driver Verifier, your driver needs to be free of these defects.

    | Code analysis for C/C++ Warning | Description                                                                                                                         |
    |---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
    | C28101                          | The Drivers module has inferred that the current function is a &lt;function-type&gt; function                                       |
    | C28022                          | The function class(es) on this function do not match the function class(es) on the typedef used to define it.                       |
    | C28023                          | The function being assigned or passed should have a \_Function\_class\_ annotation for at least one of the class(es)                |
    | C28024                          | The function pointer being assigned to is annotated with the function class, which is not contained in the function class(es) list. |
    | C28169                          | The dispatch function &lt;function&gt; does not have any \_Dispatch\_type\_ annotations                                             |
    | C28208                          | Function signature doesn’t match with the function declarations                                                                     |



### <span id="running_static_driver_verifier"></span><span id="RUNNING_STATIC_DRIVER_VERIFIER"></span>

| Running Static Driver Verifier |
|--------------------------------|
|                                |

1.  Open your driver project (.vcxProj) file in Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

    This opens the Static Driver Verifier application, where you can control, configure, and schedule when Static Driver Verifier performs an analysis.

2.  If your driver includes a library, click the **Libraries** tab and click **Add Library** to add the library.

    Browse to the directory of your library source code and select the project file (.vcxProj). Add all of the libraries that your driver includes. The libraries must be added before SDV analyzes your driver. When you start an analysis of your driver, SDV also analyzes the libraries that have not been processed. After a library is processed, it is stored in the global SDV cache. For more information, see [Library Processing in Static Driver Verifier](library-processing-in-static-driver-verifier.md)

3.  Check the configuration settings for Static Driver Verifier. Click the **Configure** tab.

    **Project Configuration** The Project Configuration shows the configuration and platform settings that you selected in Visual Studio.

    **Resources** In most cases, you can use the default settings. If SDV reports Timeout, GiveUp, or Spaceout, you might try adjusting these settings. For more information, see [Recommendations for Troubleshooting Static Driver Verifier](recommendations-for-troubleshooting-static-driver-verifier.md).

    **Schedule** Select a start time for the verification to begin. The default setting is to begin the analysis immediately after you click **Start** on the **Main** tab. Depending upon the size of the driver and its complexity, the static analysis can take a long time to run. You might want to schedule the analysis to begin when it is most convenient for you; for example, at the end of the day.

    **Note**  Be sure to check your computer's power management plan to ensure the computer will not go into a sleep state during the analysis.



4.  Click the **Rules** tab to select which driver API usage rules to verify when you start the analysis.

    Static Driver Verifier detects the type of driver you are analyzing (WDF, WDM, NDIS, or Storport) and selects the default set of rules for your driver type. If this is the first time you are running SDV on your driver, you should run the default rule set.

    For information about the rules, see [DDI Compliance Rules](https://msdn.microsoft.com/library/windows/hardware/ff552840).

5.  Start the static analysis. Click the **Main** tab, and click **Start**. When you click **Start**, a message is displayed to let you know that static analysis is scheduled and that the analysis can take a long time to run. Click **OK** to continue. The analysis begins at the time you scheduled.

### <span id="viewing_and_analyzing_the_results"></span><span id="VIEWING_AND_ANALYZING_THE_RESULTS"></span>

| Viewing and Analyzing the Results |
|-----------------------------------|
|                                   |

As the static analysis proceeds, SDV reports the status of the analysis. When the analysis is complete, SDV reports the results and statistics. If the driver fails to satisfy an API usage rule, the result is reported as a defect.

If any problems were encountered, SDV displays those on the **Warnings** and **Errors** pages. The **Driver Properties** page displays the results of the tests for certain driver properties. The driver properties tests are used to identify driver features to further qualify the analysis. You can use the **Driver Properties** results to confirm the expected properties and supported capabilities of your driver.

To view specific defects in the [Static Driver Verifier Report](static-driver-verifier-report.md), click the Defect in the **Results** pane. This opens the [Trace Viewer](defect-viewer.md), which displays a trace of the code path to the rule violation. For more information, see [Interpreting Static Driver Verifier Results](interpreting-static-driver-verifier-results.md).

**Note**  Static Driver Verifier retains the results and settings from the analysis. To clear the results, click **Clean**.



### <span id="troubleshooting_sdv_results"></span><span id="TROUBLESHOOTING_SDV_RESULTS"></span>Troubleshooting Static Driver Verifier Results

If SDV reports that no defects were found, check the **Main** tab to ensure that entry points are detected. If the driver does not declare functions by using the function role types, SDV will be unable to analyze and find defects in the driver code. For more information, see [Using Function Role Type Declarations](using-function-role-type-declarations.md).

If SDV reports timeouts or fails to return useful results, you might need to change a few SDV configuration options. For more information about how to troubleshoot SDV, see [Recommendations for Troubleshooting Static Driver Verifier](recommendations-for-troubleshooting-static-driver-verifier.md).

## <span id="related_topics"></span>Related topics


[Determining if Static Driver Verifier supports your driver or library](determining-if-static-driver-verifier-supports-your-driver-or-library.md)

[Using Function Role Type Declarations](using-function-role-type-declarations.md)

[Static Driver Verifier Rules](https://msdn.microsoft.com/library/windows/hardware/ff552840)

[Code Analysis tool](http://go.microsoft.com/fwlink/p/?linkid=226836)










