---
Description: Initializing the Driver
title: Initializing the Driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing the Driver


The initialization functions, **WpdBaseDriver::Initialize** and **WpdBaseDriver::Uninitialize** are empty in the WpdHelloWorldDriver sample. The **Initialize** function simply returns S\_OK and the **Uninitialize** function does nothing.

The following excerpt from the sample driver contains the code for **WpdBaseDriver::Initialize** and **WpdBaseDriver::Uninitialize**.

```ManagedCPlusPlus
/**
 * This method is called to initialize the driver object.
 * This is where the driver would set up its I/O libraries
 * and so on.
 */
HRESULT WpdBaseDriver::Initialize()
{

    return S_OK;
}

/**
 * This method is called to uninitialize the driver object.
 * In a real driver, this is where the driver would clean up
 * any resources held by this driver.
 */
VOID WpdBaseDriver::Uninitialize()
{
}
```

If you wanted to port this sample to support an actual device—for example, a Bluetooth-enabled mobile phone—you would add functionality in the **Initialize** function to initialize the driver's I/O library. which issues the device commands. In the case of the mobile phone, this library might include commands to enumerate a phone book, or to set or retrieve files in the phone's storage. At a bare minimum, the **Initialize** function would establish the device's network address. The **WPDBaseDriver::Uninitialize** function would perform any required cleanup.

 

 




