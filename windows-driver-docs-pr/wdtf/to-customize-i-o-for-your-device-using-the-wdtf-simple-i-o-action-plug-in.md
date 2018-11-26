---
title: Customize device I/O using a WDTF simple I/O action plug-in
description: To get the most benefit from the Device Fundamental tests and tests you might have written using the Visual Studio test templates, your device should be supported by a Simple I/O plug-in.
ms.assetid: 96BC880B-79DC-4CB1-BD79-87B0A4717634
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to customize I/O for your device using the WDTF Simple I/O Action Plug-in


To get the most benefit from the Device Fundamental tests and tests you might have written using the Visual Studio test templates, your device should be supported by a Simple I/O plug-in. To see if your device type is supported and to determine if there are specific requirements for testing, refer to [Provided WDTF Simple I/O plug-ins](provided-wdtf-simpleio-plug-ins.md). If your device is not supported, you can create a plug-in in Microsoft Visual Studio by using the **WDTF Simple I/O Action Plug-in** template.

### Prerequisites

-   Device under test is installed on the test computer.
-   Driver Package that is test signed and installed on the test computer. To verify that your driver is correctly installed, see [How to test a driver package](https://msdn.microsoft.com/windows-drivers/develop/test_a_driver_package).
-   Test computers that are configured and provisioned for deployment. See [test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime)

Instructions
------------

### <a href="" id="create-a-project-for-a-wdtf-simple-i-o-action-plug-in-"></a>Step 1: Create a project for a WDTF Simple I/O Action plug-in

1. From the **File** menu, click **New &gt; Project**.
2. From the list of installed templates in the **New Project** dialog box, select **Visual C++ &gt; Windows Driver &gt; Tests &gt; WDTF Simple I/O Action Plug-in**.
3. Provide a name for your simple I/O project and a location (or use the defaults).
4. The project template generates a Visual Studio solution. The Solution contains all the files you need to create a simple I/O plug-in for your device. The names of the files take the form WDTF<em>&lt;project&gt;</em>SimpleIoAction\*. The default name for the simple I/O project is DeviceType.
5. The template creates a WDTF Simple I/O Action interface for your project. The interface acts upon an instance of the IWDTFTarget2 interface.
6. Build your WDTF Simple I/O plug-in solution to verify that all the required files are present.
7. Implement a method to set the target and implement the Simple I/O Actions (Open, Close, and RunIO ), by adding code in the implementation file. The name of the file takes the form CWDTF*project*SimpleIoActionImpl.cpp file.

### <a href="" id="implement-the-settarget-method-for-your-device"></a>Step 2: Implement the SetTarget method for your device

- Open the implementation file for your project, for example, CWDTFmyDeviceTypeSimpleIoActionImpl.cpp, and locate the instance of [**IAction::SetTarget**](https://msdn.microsoft.com/library/windows/hardware/ff538790) SetTarget method. This method has a section marked with comments and TODO: that indicates where you should implement code that checks for compatibility with your device.

  The **SetTarget** method is called once by WDTF for each instance. It has two main purposes:

  - So that WDTF can determine if the object supports the device target, pMainTarget
  - So that the CWDTF<em>&lt;project&gt;</em>SimpleIoActionImpl instance can get the necessary information from the target to accomplish the later Open() , Close() , RunIO() method calls.

  The implementation of this method should return E\_NOINTERFACE to indicate that the target is not supported. The method should return S\_OK if the target is supported. If any other failure occurs, the method should return HRESULT to indicate the error.

  ```ManagedCPlusPlus
       
      ////
      // TODO: 1)  Perform your checks to see if your implementation is compatible with the target.
      //       Use the ITarget::GetValue() & ITarget::Eval() method to get the necessary data , info 
      //       to determine that. 
      //       2)  Also get the necessary info and save it in a member variable 
      //       to accomplish the later Open() method call.
  ```

### <a href="" id="implement-simpleioaction-to-open-the-interface"></a>Step 3: Implement SimpleIoAction to open the interface

Next, you need to open the ITarget for testing by implementing the provided Open() method.

This [**Open**](https://msdn.microsoft.com/library/windows/hardware/hh451153) method should attempt to open the target device. If the method is unable to do this, the method should return an HRESULT indicating the failure. This method should fail if the SimpleIO interface is already open (initialized). How you implement this method depends upon your ITarget type and what makes the most sense in your situation. Perhaps this means you should open a handle to it with CreateFile(). Perhaps it means that you initialize a context structure so that you can keep track of an ongoing test case. In the event of an error, the method should ideally use COMReportError () and should provide a description of the error and any information or steps that could help prevent future occurrences.

**Note**  This method should fail if ISimpleIO\_Action is already opened.

 

-   Open the implementation file for your project, for example, CWDTFmyDeviceTypeSimpleIoActionImpl.cpp, and locate the instance of [**Open**](https://msdn.microsoft.com/library/windows/hardware/hh451153) method. This method has a section marked with comments and TODO:

    ```cpp
    //
       //   TODO: Add code for your implementation of Open() here.
       //
       //
       //  To return failure use COMReportError(,,,).  For example the following 
       //  will return E_FAIL as the error code and "My Device error String"  as
       //  the error string.
       //
       //  COMReportError(WDTF, E_FAIL, "My Device error String");
       //
    ```

### <a href="" id="implement-the-simpleioaction-method-to--close-the-interface"></a>Step 4: Implement the SimpleIoAction method to close the interface

This method should close your previously opened test context. You should clear your context even if you must report a failing HRESULT. There are only a few cases where an error that happens when you close actually makes sense. In this method, you should revert whatever operation you performed in Open(). Perhaps this means you should close your previously opened handle with CloseHandle(). In the event of an error, please provide an actionable description for it.

**Note**  This method should fail if the ISimpleIO\_Action is already closed or has never been opened.

 

-   Open the implementation file for your project, for example, CWDTFmyDeviceTypeSimpleIoActionImpl.cpp, and locate the instance of the [**Close**](https://msdn.microsoft.com/library/windows/hardware/hh451151) method. This method has a section marked with comments and TODO:

    ```cpp
    //
       //  //
       //   TODO: Add code for your implementation of Close() here.
       //
       // 
       //
       //  To return failure use COMReportError(,,,).  For example the following 
       //  will return E_FAIL as the error code and "My Device error String"  as
       //  the error string.
       //
       //  COMReportError(WDTF, E_FAIL, "My Device error String");
       //
     
       //
    ```

### <a href="" id="implement-the-simpleioaction-method-to-perform-simple-i-o-operations-"></a>Step 5: Implement the SimpleIoAction method to perform simple I/O operations

This method should perform a small number of input and output operations on the target. The method should then verify that the I/O operations completed correctly. Then, each test can control how long it performs I/O to a device. Each call to the RunIo() method should only perform a small amount of I/O . WDTF will call RunIo() repeatedly in a loop to perform more I/O. In general, try to keep a single RunIo() method call to a few seconds.

**Note**  This method should fail if ISimpleIO\_Action is currently closed.

 

-   Open the implementation file for your project, for example, CWDTFmyDeviceTypeSimpleIoActionImpl.cpp, and locate the instance of the RunIO method. This method has a section marked with comments and TODO:

    ```cpp
    //
       //  //
       //   TODO: Add code for your implmentaiton of RunIO() here.
       //
       // 
       //
       //  To return failure use COMReportError(,,,).  For example the following 
       //  will return E_FAIL as the error code and "My Device error String"  as
       //  the error string.
       //
       //  COMReportError(WDTF, E_FAIL, "My Device error String");
       //
     
       //
    ```

### <a href="" id="build-and-install-the-simple-i-o-action-plugin-"></a>Step 6: Build and install the Simple I/O Action Plugin

If you have not already done so, you will need to configure a computer for testing. For more information, see [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/library/windows/hardware/dn745909) or [Provision a computer for driver deployment and testing (WDK 8)](https://msdn.microsoft.com/library/windows/hardware/dn745909).

1. Build the solution.

   When you build the Simple I/O Action plug-in, two tests are created. These tests install and uninstall the plugin on the test computer. By default, the Simple I/O Action plugin files appear in **Test Group Explorer**, in the test category **My Test Category**.

2. To install the Simple I/O Action Plug-in, run the test named **Register WDTF**<em>&lt;Project&gt;</em>**SimpleIOAction.DLL** on the test computer. For information about selecting and running tests see, [How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime).
3. To verify that your Simple I/O Action Plug-in is installed, run the **Display devices that have WDTF Simple I/O Plug-ins** test on the test computer. Your plugin and device should appear in the results. For more information, see [How to How to determine if a custom WDTF Simple I/O Action Plug-in is required for your device](test-your-device-to-see-if-you-need-to-customize-the-wdtf-simple-i-o-action-plug-in.md).
4. To uninstall the Simple I/O Action Plug-in, run the test named **Un-register WDTF**<em>&lt;Project&gt;</em>**SimpleIOAction.DLL** on the test computer. You can verify that you have uninstalled the plugin by running the **Display devices that have WDTF Simple I/O plug-ins** test.

## Related topics
[Test Authoring and Execution Framework (TAEF)](https://msdn.microsoft.com/library/windows/hardware/hh439725)  
[How to How to determine if a custom WDTF Simple I/O Action Plug-in is required for your device](test-your-device-to-see-if-you-need-to-customize-the-wdtf-simple-i-o-action-plug-in.md)  
[How to How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime)  



