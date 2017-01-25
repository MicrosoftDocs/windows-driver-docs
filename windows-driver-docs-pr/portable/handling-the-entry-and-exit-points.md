---
Description: Handling the Entry and Exit Points
MS-HAID: 'wpddk.handling\_the\_entry\_and\_exit\_points'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Handling the Entry and Exit Points
---

# Handling the Entry and Exit Points


Each time a device is loaded in a driver's host process, the user-mode driver framework (UMDF) adds a device object. And, each time the framework adds an object, it calls methods in the **IDriverEntry** interface. These methods are found in the CDriver class. The following table describes the methods that are found in this class.

| Method                           | Description                            |
|----------------------------------|----------------------------------------|
| **IDriverEntry::OnDeinitialize** | Performs necessary cleanup operations. |
| **IDriverEntry::OnDeviceAdd**    | Adds a new device to the system.       |
| **IDriverEntry::OnInitialize**   | Handles driver initialization.         |

 

In the WpdHelloWorldDriver, the **OnDeviceAdd** method is the only method that does meaningful work; the **OnInitialize** method simply returns S\_OK and the **OnDeinitialize** method returns no value.

The code for the **OnDeviceAdd** method completes the following steps:

1.  Creates a device callback object.
2.  Creates a WDF device.
3.  Creates the WpdBaseDriver object and assigns it to the WDF device object.
4.  Creates a queue callback object.
5.  Creates the default queue.

CDriver also implements **IObjectCleanup::OnCleanup**, which contains code to release a reference to the WpdBaseDriver object that is held by the WDF device object during **OnDeviceAdd**.

For more information about each interface and its methods, see the [UMDF](http://go.microsoft.com/fwlink/p/?linkid=153678) documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Handling%20the%20Entry%20and%20Exit%20Points%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



