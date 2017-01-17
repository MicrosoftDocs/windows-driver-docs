---
Description: Initializing the Driver
MS-HAID: 'wpddk.initializing\_the\_driver'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Initializing the Driver
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Initializing%20the%20Driver%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



