---
Description: The easiest way to write a Windows desktop app that communicates with a USB device, is by using the C/C++ WinUSB template.
title: Write a Windows desktop app based on the WinUSB template
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Write a Windows desktop app based on the WinUSB template


**Important APIs**

-   [SetupAPI Functions](https://msdn.microsoft.com/library/windows/hardware/ff550855)
-   [WinUSB Functions](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb)

The easiest way to write a Windows desktop app that communicates with a USB device, is by using the C/C++ WinUSB template. For this template, you need an integrated environment with the Windows Driver Kit (WDK) (with Debugging Tools for Windows) and Microsoft Visual Studio (Professional or Ultimate). You can use the template as a starting point.

## Prerequisites


-   To set up the integrated development environment, first install Microsoft Visual Studio Ultimate 2012 or Microsoft Visual Studio Professional 2012 and then install the WDK. You can find information about how to get Visual Studio and the WDK [here](http://go.microsoft.com/fwlink/p/?linkid=239721).
-   Debugging Tools for Windows is included when you install the WDK. For more information, see [Download and Install Debugging Tools for Windows](http://go.microsoft.com/fwlink/p/?linkid=235427).

## Creating a WinUSB application


To create an application from the template:

1.  Open Microsoft Visual Studio. On the **File** menu, choose **New** &gt; **Project**. The **New Project** dialog box opens, as shown in the following screen shot.
2.  In the **New Project** dialog box, in the left pane, locate and select **USB**.
3.  In the middle pane, select **WinUSB application.**
4.  In the **Name** field, if you want, change the project name. In this topic, we'll use the default name.
5.  In the **Location** field, enter the directory where you want to create the new project.
6.  Check **Create directory for solution**. Click **OK**.

    ![winusb template in visual studio](images/winusb-template.png)

    Visual Studio creates two projects and a solution. You can see the solution, the two projects, and the files that belong to each project in the **Solution Explorer** window, as shown in the following screen shot. (If the **Solution Explorer** window is not visible, choose **Solution Explorer** from the **View** menu.) The solution contains a C++ application project named USB Application1 and a driver package project named USB Application1 Package. If you want to look at the application source code, you can open any of the files that appear under **Source Files**.

    ![winusb template solution explorer](images/winusb-template1.png)

    The USB Application1 project has source files for the application.

    The USB Application1 Package project contains an INF file that is used to install Microsoft-provided Winusb.sys driver as the device driver.

7.  In the INF file, USBApplication1.inf, locate these lines:

    `%DeviceName% =USB_Install, USB\VID_vvvv&PID_pppp`

8.  Replace VID\_vvvv&PID\_pppp with the hardware ID for your device. Get the hardware ID from Device Manager. In Device Manager, view the device properties. On the **Details** tab, view the **Hardware Ids** property value.
9.  In the **Solution Explorer** window, right-click **Solution 'USB Application1' (2 projects)**, and choose **Configuration Manager**. Choose a configuration and platform for both the application project and the package project. In this exercise, we choose Win8.1 Debug and x64, as shown in the following screen shot.

    ![winusb application template](images/winusb-template2.png)

## Building, deploying and debugging the project


So far in this exercise, you've used Visual Studio to build your projects. Next you need to configure the device to which the device is connected. The template requires that the Winusb driver is installed as the driver for your device.

Your testing and debugging environment can have:

-   Two computer setup: the host computer and the target computer. You develop and build your project in Visual Studio on the host computer. The debugger runs on the host computer and is available in the Visual Studio user interface. When you test and debug the application, it driver runs on the target computer.

-   Single computer setup: Your target and host run on one computer. You develop and build your project in Visual Studio, and run the debugger and the application.

You can deploy, install, load, and debug your application and the driver by following these steps:

-   **Two computer setup**

    1.  Provision your target computer by following the instructions in [Provision a computer for driver deployment and testing](https://msdn.microsoft.com/library/windows/hardware/dn745909).
        **Note**  
        Provisioning creates a user on the target machine named, WDKRemoteUser. After provisioning is complete you will see the user switch to WDKRemoteUser. 
    2.  On the host computer, open your solution in Visual Studio.
    3.  In main.cpp add this line before the OpenDevice call.

        `system ("pause")`

        The line causes the application to pause when launched. This is useful in remote debugging.

    4.  In pch.h, include this line:

        `#include <cstdlib>`

        This include statement is required for the system() call in the preceding step.

    5.  In the **Solution Explorer** window, right-click USB Application1 Package, and choose **Properties**.
    6.  In the **USB Application1 Package Property Pages** window, in the left pane, navigate to **Configuration Properties &gt; Driver Install &gt; Deployment**, as shown in the following screen shot.
    7.  Check **Enable deployment**, and check **Remove previous driver versions before deployment**.
    8.  For **Remote Computer Name**, select the name of the computer that you configured for testing and debugging. In this exercise, we use a computer named dbg-target.
    9.  Select **Install and Verify**. Click **OK**.

        ![winusb template](images/winusb-template4.png)

    10. In the property page, navigate to **Configuration Properties &gt; Debugging**, and select **Debugging Tools for Windows – Remote Debugger**, as shown in the following screen shot.

        ![winusb template debug setting](images/winusb-template5.png)

    11. Select **Build Solution** from the **Build** menu. Visual Studio displays build progress in the **Output** window. (If the **Output** window is not visible, choose **Output** from the **View** menu.) In this exercise, we've build the project for an x-64 system running Windows 8.1.

On the target computer, you will see driver install scripts running. The driver files are copied to the %Systemdrive%\\drivertest\\drivers folder on the target computer. Verify that the .inf, .cat, test cert, and .sys files, and any other necessary files, are present %systemdrive%\\drivertest\\drivers folder. The device must appear in Device Manager without errors.

On the host computer, you will see this message in the **Output** window.

```syntax
Deploying driver files for project 
"<path>\visual studio 12\Projects\USB Application1\USB Application1 Package\USB Application1 Package.vcxproj".  
Deployment may take a few minutes...
========== Build: 1 succeeded, 0 failed, 1 up-to-date, 0 skipped ==========
```

**To debug the application**

1.  On the host computer, navigate to **x64 &gt; Win8.1Debug** in the solution folder.
2.  Copy the application executable, UsbApplication1.exe to the target computer.
3.  On the target computer launch the application.
4.  On the host computer, from the **Debug** menu, select **Attach to process**.
5.  In the window, select **Windows User Mode Debugger** (Debugging Tools for Windows) as the transport and the name of the target computer, in this case dbg-target, as the qualifier as shown in this image.

    ![winusb template debug setting](images/winusb-template6.png)

6.  Select the application from the list of **Available Processes** and click **Attach**. You can now debug using **Immediate Window** or by using the options in **Debug** menu.

The preceding instructions debug the application by using **Debugging Tools for Windows – Remote Debugger**. If you want to use the **Remote Windows Debugger** (the debugger that is included with Visual Studio), then follow these instructions:

1.  On the target computer, add msvsmon.exe to the list of apps allowed through Firewall.
2.  Launch Visual Studio Remote Debugging Monitor located in C:\\DriverTest\\msvsmon\\msvsmon.exe.
3.  Create a working folder, such as, C:\\remotetemp.
4.  Copy the application executable, UsbApplication1.exe to the working folder on the target computer.
5.  On the host computer, in Visual Studio, right-click the **USB Application1 Package** project, and select **Unload Project**.
6.  Right-click the **USB Application1** project, in project properties expand the **Configuration Properties** node and click **Debugging**.
7.  Change **Debugger to launch** to **Remote Windows Debugger**.
8.  Change the project settings to run the executable on a remote computer by following the instructions given in [Remote Debugging of a Project Built Locally](https://msdn.microsoft.com/library/vstudio/8x6by8d2.aspx). Make sure that **Working Directory** and **Remote Command** properties reflect the folder on the target computer.
9.  To debug the application, in the **Build** menu, select **Start Debugging**, or press **F5.**

-   **Single computer setup:**

    1.  To build your application and the driver installation package, choose **Build Solution** from the **Build** menu. Visual Studio displays build progress in the **Output** window, as shown in the following screen shot. (If the **Output** window is not visible, choose **Output** from the **View** menu.) In this exercise, we've build the project for an x-64 system running Windows 8.1.
    2.  To see the built driver package, navigate in Windows Explorer to your USB Application1 folder, and then navigate to **x64 &gt; Win8.1Debug &gt; USB Application1 Package**. The driver package contains several files: USBApplication1.inf is an information file that Windows uses when you install the driver, usbapplication1.cat is a catalog file that the installer uses to verify the test signature for the driver package. The other file is a co-installer for the Windows Driver Frameworks (WDF). These files are shown in the following screen shot.

        ![winusb application template](images/winusb-template3.png)

        **Note**  There is no driver file included in the package. That is because the INF file references the in-box driver, Winusb.sys, found in Windows\\System32 folder.
    3.  Manually install the driver. In Device Manager, update the driver by specifying the INF in the package. Point to the driver package located in the solution folder, shown in the preceding section.
    4.  Right-click the **USB Application1** project, in project properties expand the **Configuration Properties** node and click **Debugging**.
    5.  Change **Debugger to launch** to **Local Windows Debugger**.
    6.  7.  Right-click the USB Application1 Package project, and select **Unload Project**.
    8.  To debug the application, in the **Build** menu, select **Start Debugging**, or press **F5**.

## Template code discussion


The template is a starting point for your desktop application. The USB Application1 project has source files device.cpp and main.cpp.

The main.cpp file contains the application entry point, \_tmain. The device.cpp contains all helper functions that open and close the handle to the device.

The template also has a header file named device.h. This file contains definitions for the device interface GUID (discussed later) and a DEVICE\_DATA structure that stores information obtained by the application. For example, it stores the WinUSB interface handle obtained by OpenDevice and used in subsequent operations.

```cpp
typedef struct _DEVICE_DATA {

    BOOL                    HandlesOpen;
    WINUSB_INTERFACE_HANDLE WinusbHandle;
    HANDLE                  DeviceHandle;
    TCHAR                   DevicePath[MAX_PATH];

} DEVICE_DATA, *PDEVICE_DATA;
```

### <a href="" id="deviceinstance"></a>Getting the instance path for the device - see RetrieveDevicePath in device.cpp

To access a USB device, the application creates a valid file handle for the device by calling **CreateFile**. For that call, the application must obtain the device path instance. To obtain the device path, the app uses [SetupAPI](https://msdn.microsoft.com/library/windows/hardware/ff550855) routines and specifies the device interface GUID in the INF file that was used to install Winusb.sys. Device.h declares a GUID constant named GUID\_DEVINTERFACE\_USBApplication1. By using those routines, the application enumerates all devices in the specified device interface class and retrieves the device path of the device.

```cpp
HRESULT
RetrieveDevicePath(
    _Out_bytecap_(BufLen) LPTSTR DevicePath,
    _In_                  ULONG  BufLen,
    _Out_opt_             PBOOL  FailureDeviceNotFound
    )
/*++

Routine description:

    Retrieve the device path that can be used to open the WinUSB-based device.

    If multiple devices have the same device interface GUID, there is no
    guarantee of which one will be returned.

Arguments:

    DevicePath - On successful return, the path of the device (use with CreateFile).

    BufLen - The size of DevicePath&#39;s buffer, in bytes

    FailureDeviceNotFound - TRUE when failure is returned due to no devices
        found with the correct device interface (device not connected, driver
        not installed, or device is disabled in Device Manager); FALSE
        otherwise.

Return value:

    HRESULT

--*/
{
    BOOL                             bResult = FALSE;
    HDEVINFO                         deviceInfo;
    SP_DEVICE_INTERFACE_DATA         interfaceData;
    PSP_DEVICE_INTERFACE_DETAIL_DATA detailData = NULL;
    ULONG                            length;
    ULONG                            requiredLength=0;
    HRESULT                          hr;

    if (NULL != FailureDeviceNotFound) {

        *FailureDeviceNotFound = FALSE;
    }

    //
    // Enumerate all devices exposing the interface
    //
    deviceInfo = SetupDiGetClassDevs(&GUID_DEVINTERFACE_USBApplication1,
                                     NULL,
                                     NULL,
                                     DIGCF_PRESENT | DIGCF_DEVICEINTERFACE);

    if (deviceInfo == INVALID_HANDLE_VALUE) {

        hr = HRESULT_FROM_WIN32(GetLastError());
        return hr;
    }

    interfaceData.cbSize = sizeof(SP_DEVICE_INTERFACE_DATA);

    //
    // Get the first interface (index 0) in the result set
    //
    bResult = SetupDiEnumDeviceInterfaces(deviceInfo,
                                          NULL,
                                          &GUID_DEVINTERFACE_USBApplication1,
                                          0,
                                          &interfaceData);

    if (FALSE == bResult) {

        //
        // We would see this error if no devices were found
        //
        if (ERROR_NO_MORE_ITEMS == GetLastError() &&
            NULL != FailureDeviceNotFound) {

            *FailureDeviceNotFound = TRUE;
        }

        hr = HRESULT_FROM_WIN32(GetLastError());
        SetupDiDestroyDeviceInfoList(deviceInfo);
        return hr;
    }

    //
    // Get the size of the path string
    // We expect to get a failure with insufficient buffer
    //
    bResult = SetupDiGetDeviceInterfaceDetail(deviceInfo,
                                              &interfaceData,
                                              NULL,
                                              0,
                                              &requiredLength,
                                              NULL);

    if (FALSE == bResult && ERROR_INSUFFICIENT_BUFFER != GetLastError()) {

        hr = HRESULT_FROM_WIN32(GetLastError());
        SetupDiDestroyDeviceInfoList(deviceInfo);
        return hr;
    }

    //
    // Allocate temporary space for SetupDi structure
    //
    detailData = (PSP_DEVICE_INTERFACE_DETAIL_DATA)
        LocalAlloc(LMEM_FIXED, requiredLength);

    if (NULL == detailData)
    {
        hr = E_OUTOFMEMORY;
        SetupDiDestroyDeviceInfoList(deviceInfo);
        return hr;
    }

    detailData->cbSize = sizeof(SP_DEVICE_INTERFACE_DETAIL_DATA);
    length = requiredLength;

    //
    // Get the interface&#39;s path string
    //
    bResult = SetupDiGetDeviceInterfaceDetail(deviceInfo,
                                              &interfaceData,
                                              detailData,
                                              length,
                                              &requiredLength,
                                              NULL);

    if(FALSE == bResult)
    {
        hr = HRESULT_FROM_WIN32(GetLastError());
        LocalFree(detailData);
        SetupDiDestroyDeviceInfoList(deviceInfo);
        return hr;
    }

    //
    // Give path to the caller. SetupDiGetDeviceInterfaceDetail ensured
    // DevicePath is NULL-terminated.
    //
    hr = StringCbCopy(DevicePath,
                      BufLen,
                      detailData->DevicePath);

    LocalFree(detailData);
    SetupDiDestroyDeviceInfoList(deviceInfo);

    return hr;
}
```

In the preceding function, the application gets the device path by calling these routines:

1.  [**SetupDiGetClassDevs**](https://msdn.microsoft.com/library/windows/hardware/ff551072) to get a handle to the *device information set*, an array that contains information about all installed devices that matched the specified device interface class, GUID\_DEVINTERFACE\_USBApplication1. Each element in the array called a *device interface* corresponds to a device that is installed and registered with the system. The device interface class is identified by passing the device interface GUID that you defined in the INF file. The function returns an HDEVINFO handle to the device information set.
2.  [**SetupDiEnumDeviceInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff551015) to enumerate the device interfaces in the device information set and obtain information about your device interface.

    This call requires the following items:

    -   An initialized caller-allocated [**SP\_DEVICE\_INTERFACE\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552342) structure that has its **cbSize** member set to the size of the structure.
    -   The HDEVINFO handle from step 1.
    -   The device interface GUID that you defined in the INF file.

    [**SetupDiEnumDeviceInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff551015) looks up the device information set array for the specified index of the device interface and fills the initialized [**SP\_DEVICE\_INTERFACE\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552342) structure with basic data about the interface.

    **Note**   To enumerate all the device interfaces in the device information set, call [**SetupDiEnumDeviceInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff551015) in a loop until the function returns **FALSE** and the error code for the failure is ERROR\_NO\_MORE\_ITEMS. The ERROR\_NO\_MORE\_ITEMS error code can be retrieved by calling **GetLastError**. With each iteration, increment the member index.

    Alternately, you can call [**SetupDiEnumDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff551010) that enumerates the device information set and returns information about device interface elements, specified by the index, in a caller-allocated [**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure. You can then pass a reference to this structure in the *DeviceInfoData* parameter of the [**SetupDiEnumDeviceInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff551015) function.

3.  [**SetupDiGetDeviceInterfaceDetail**](https://msdn.microsoft.com/library/windows/hardware/ff551120) to get detailed data for the device interface. The information is returned in a [**SP\_DEVICE\_INTERFACE\_DETAIL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552343) structure. Because the size of the **SP\_DEVICE\_INTERFACE\_DETAIL\_DATA** structure varies, **SetupDiGetDeviceInterfaceDetail** is called twice. The first call gets the buffer size to allocate for the **SP\_DEVICE\_INTERFACE\_DETAIL\_DATA** structure. The second call fills the allocated buffer with detailed information about the interface.
    1.  Calls [**SetupDiGetDeviceInterfaceDetail**](https://msdn.microsoft.com/library/windows/hardware/ff551120) with *DeviceInterfaceDetailData* parameter set to **NULL**. The function returns the correct buffer size in the *requiredlength* parameter. This call fails with the ERROR\_INSUFFICIENT\_BUFFER error code. This error code is expected.
    2.  Allocates memory for a [**SP\_DEVICE\_INTERFACE\_DETAIL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552343) structure based on the correct buffer size that is retrieved in the *requiredlength* parameter.
    3.  Calls [**SetupDiGetDeviceInterfaceDetail**](https://msdn.microsoft.com/library/windows/hardware/ff551120) again and passes it a reference to the initialized structure in the *DeviceInterfaceDetailData* parameter. When the function returns, the structure is filled with detailed information about the interface. The device path is in the [**SP\_DEVICE\_INTERFACE\_DETAIL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552343) structure's **DevicePath** member.

### <a href="" id="filehandle"></a>Creating a file handle for the device - see OpenDevice in device.cpp

To interact with the device, the needs a WinUSB interface handle to the first (default) interface on the device. The template code obtains the file handle and the WinUSB interface handle and stores them in the DEVICE\_DATA structure.

```cpp
HRESULT
OpenDevice(
    _Out_     PDEVICE_DATA DeviceData,
    _Out_opt_ PBOOL        FailureDeviceNotFound
    )
/*++

Routine description:

    Open all needed handles to interact with the device.

    If the device has multiple USB interfaces, this function grants access to
    only the first interface.

    If multiple devices have the same device interface GUID, there is no
    guarantee of which one will be returned.

Arguments:

    DeviceData - Struct filled in by this function. The caller should use the
        WinusbHandle to interact with the device, and must pass the struct to
        CloseDevice when finished.

    FailureDeviceNotFound - TRUE when failure is returned due to no devices
        found with the correct device interface (device not connected, driver
        not installed, or device is disabled in Device Manager); FALSE
        otherwise.

Return value:

    HRESULT

--*/
{
    HRESULT hr = S_OK;
    BOOL    bResult;

    DeviceData->HandlesOpen = FALSE;

    hr = RetrieveDevicePath(DeviceData->DevicePath,
                            sizeof(DeviceData->DevicePath),
                            FailureDeviceNotFound);

    if (FAILED(hr)) {

        return hr;
    }

    DeviceData->DeviceHandle = CreateFile(DeviceData->DevicePath,
                                          GENERIC_WRITE | GENERIC_READ,
                                          FILE_SHARE_WRITE | FILE_SHARE_READ,
                                          NULL,
                                          OPEN_EXISTING,
                                          FILE_ATTRIBUTE_NORMAL | FILE_FLAG_OVERLAPPED,
                                          NULL);

    if (INVALID_HANDLE_VALUE == DeviceData->DeviceHandle) {

        hr = HRESULT_FROM_WIN32(GetLastError());
        return hr;
    }

    bResult = WinUsb_Initialize(DeviceData->DeviceHandle,
                                &DeviceData->WinusbHandle);

    if (FALSE == bResult) {

        hr = HRESULT_FROM_WIN32(GetLastError());
        CloseHandle(DeviceData->DeviceHandle);
        return hr;
    }

    DeviceData->HandlesOpen = TRUE;
    return hr;
}
```

1.  The app calls **CreateFile** to create a file handle for the device by specifying the device path retrieved earlier. It uses the FILE\_FLAG\_OVERLAPPED flag because WinUSB depends on this setting.
2.  By using the file handle for the device, the app creates a WinUSB interface handle. [WinUSB Functions](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb) use this handle to identify the target device instead of the file handle. To obtain a WinUSB interface handle, the app calls [**WinUsb\_Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff540277) by passing the file handle. Use the received handle in the subsequent calls to get information from the device, and to send I/O requests to the device.

### Release the device handles - see CloseDevice in device.cpp

The template code implements code to release the file handle and the WinUSB interface handle for the device.

-   **CloseHandle** to release the handle that was created by **CreateFile**, as described in the [Create a File Handle for the Device](#filehandle) section of this walkthrough.
-   [**WinUsb\_Free**](https://msdn.microsoft.com/library/windows/hardware/ff540233) to release the WinUSB interface handle for the device, which is returned by [**WinUsb\_Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff540277).

```cpp
VOID
CloseDevice(
    _Inout_ PDEVICE_DATA DeviceData
    )
/*++

Routine description:

    Perform required cleanup when the device is no longer needed.

    If OpenDevice failed, do nothing.

Arguments:

    DeviceData - Struct filled in by OpenDevice

Return value:

    None

--*/
{
    if (FALSE == DeviceData->HandlesOpen) {

        //
        // Called on an uninitialized DeviceData
        //
        return;
    }

    WinUsb_Free(DeviceData->WinusbHandle);
    CloseHandle(DeviceData->DeviceHandle);
    DeviceData->HandlesOpen = FALSE;

    return;
}
```

## Next steps


Next, read these topics to send get device information and send data transfers to the device:

-   [Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md)

    Learn about querying the device for USB-specific information such as device speed, interface descriptors, related endpoints, and their pipes.

-   [Send USB isochronous transfers from a WinUSB desktop app](getting-set-up-to-use-windows-devices-usb.md)

    Transfer data to and from isochronous endpoints of a USB device.

## Related topics
[Windows desktop app for a USB device](windows-desktop-app-for-a-usb-device.md)  
[Provision a computer for driver deployment and testing](https://msdn.microsoft.com/library/windows/hardware/dn745909)  



