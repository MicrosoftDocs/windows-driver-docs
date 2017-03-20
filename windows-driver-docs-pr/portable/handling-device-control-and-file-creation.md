---
Description: Handling Device Control and File Creation
MS-HAID: 'wpddk.handling\_device\_control\_and\_file\_creation'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Handling Device Control and File Creation
---

# Handling Device Control and File Creation


Each time a Windows-based application calls the **DeviceIoControl** Win32 function, the user-mode driver framework (UMDF) notifies the driver by calling one of the methods in the **IQueueCallbackDeviceIlControl** interface. Each time a Windows-based application calls the **CreateFile** Win32 function, UMDF notifies the driver by calling a method in the **IQueueCallbackCreate** interface. All this functionality is found in the sample driver's *Queue.cpp* and *Queue.h* modules.

The following table describes the methods that are found in these modules.

| Method                                               | Description                                                                                                   |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **IObjectCleanup::OnCleanup**                        | Releases the reference to the client context map that is assigned by **OnCreateFile** to the WDF file object. |
| **IQueueCallbackCreate::OnCreateFile**               | Opens the device as a result of an application that calls the Win32 **CreateFile** function.                  |
| **IQueueCallbackDeviceIoControl::OnDeviceIoControl** | Performs a device operation as a result of an application that calls the **DeviceIOControl** function.        |

 

Refer to the [UMDF](http://go.microsoft.com/fwlink/p/?linkid=153678) documentation for a description of each interface and its methods.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Handling%20Device%20Control%20and%20File%20Creation%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



