---
Description: This topic includes a detailed walkthrough of how to use WinUSB Functions to communicate with a USB device that is using Winusb.sys as its function driver.
title: How to Access a USB Device by Using WinUSB Functions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to Access a USB Device by Using WinUSB Functions


**Summary**

-   Opening the device and obtaining WinUSB handle.
-   Getting information about the device, configuration, and interface settings of all interfaces,, and their endpoints.
-   Reading and writing data to bulk and interrupt endpoints.

**Important APIs**

-   [SetupAPI Functions](https://msdn.microsoft.com/library/windows/hardware/ff550855)
-   [WinUSB Functions](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb)

This topic includes a detailed walkthrough of how to use [WinUSB Functions](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb) to communicate with a USB device that is using Winusb.sys as its function driver.

If you are using Microsoft Visual Studio 2013, create your skeleton app by using the WinUSB template. In that case, skip steps 1 through 3 and proceed from step 4 in this topic. The template opens a file handle to the device and obtains the WinUSB handle required for subsequent operations. That handle is stored in the app-defined DEVICE\_DATA structure in device.h.

For more information about the template, see Write a Windows desktop app based on the WinUSB template.

**Note**  WinUSB functions require Windows XP or later. You can use these functions in your C/C++ application to communicate with your USB device. Microsoft does not provide a managed API for WinUSB.

## <a href="" id="pre"></a>Prerequisites


The following items apply to this walkthrough:

-   This information applies to Windows 8.1, Windows 8, Windows 7, Windows Server 2008, Windows Vista versions of Windows.
-   You have installed Winusb.sys as the device's function driver. For more information about this process, see [WinUSB (Winusb.sys) Installation](winusb-installation.md).
-   The examples in this topic are based on the [OSR USB FX2 Learning Kit device](http://www.osronline.com/). You can use these examples to extend the procedures to other USB devices.

## <a href="" id="setup"></a>Step 1: Create a skeleton app based on the WinUSB template


To access a USB device, start by creating a skeleton app based on the WinUSB template included in the integrated environment of Windows Driver Kit (WDK) (with Debugging Tools for Windows) and Microsoft Visual Studio.You can use the template as a starting point.

For information about the template code, how to create, build, deploy, and debug the skeleton app, see [Write a Windows desktop app based on the WinUSB template](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md).

The template enumerates devices by using [SetupAPI](https://msdn.microsoft.com/library/windows/hardware/ff550855) routines, opens a file handle for the device, and creates a WinUSB interface handle required for subsequent tasks. For example code that gets the device handle and opens the device, see [Template code discussion](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md).

## <a href="" id="query"></a>Step 2: Query the Device for USB Descriptors


Next, query the device for USB-specific information such as device speed, interface descriptors, related endpoints, and their pipes. The procedure is similar to the one that USB device drivers use. However, the application completes device queries by calling [**WinUsb\_GetDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff540257).

The following list shows the WinUSB functions that you can call to get USB-specific information:

-   Additional device information.

    Call [**WinUsb\_QueryDeviceInformation**](https://msdn.microsoft.com/library/windows/hardware/ff540290) to request information from the device descriptors for the device. To get the device's speed, set DEVICE\_SPEED (0x01) in the *InformationType* parameter. The function returns LowSpeed (0x01) or HighSpeed (0x03).

-   Interface descriptors

    Call [**WinUsb\_QueryInterfaceSettings**](https://msdn.microsoft.com/library/windows/hardware/ff540292) and pass the device's interface handles to obtain the corresponding interface descriptors. The WinUSB interface handle corresponds to the first interface. Some USB devices, such as the OSR Fx2 device, support only one interface without any alternative setting. Therefore, for these devices the *AlternateSettingNumber* parameter is set to zero and the function is called only one time. **WinUsb\_QueryInterfaceSettings** fills the caller-allocated [**USB\_INTERFACE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff540065) structure (passed in the *UsbAltInterfaceDescriptor* parameter) with information about the interface. For example, the number of endpoints in the interface is set in the **bNumEndpoints** member of **USB\_INTERFACE\_DESCRIPTOR**.

    For devices that support multiple interfaces, call [**WinUsb\_GetAssociatedInterface**](https://msdn.microsoft.com/library/windows/hardware/ff540245) to obtain interface handles for associated interfaces by specifying the alternative settings in the *AssociatedInterfaceIndex* parameter.

-   Endpoints

    Call [**WinUsb\_QueryPipe**](https://msdn.microsoft.com/library/windows/hardware/ff540293) to obtain information about each endpoint on each interface. **WinUsb\_QueryPipe** populates the caller-allocated [**WINUSB\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540285) structure with information about the specified endpoint's pipe. The endpoints' pipes are identified by a zero-based index, and must be less than the value in the **bNumEndpoints** member of the interface descriptor that is retrieved in the previous call to [**WinUsb\_QueryInterfaceSettings**](https://msdn.microsoft.com/library/windows/hardware/ff540292). The OSR Fx2 device has one interface that has three endpoints. For this device, the function's *AlternateInterfaceNumber* parameter is set to 0, and the value of the *PipeIndex* parameter varies from 0 to 2.

    To determine the pipe type, examine the [**WINUSB\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540285) structure's **PipeInfo** member. This member is set to one of the [**USBD\_PIPE\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff539119) enumeration values: UsbdPipeTypeControl, UsbdPipeTypeIsochronous, UsbdPipeTypeBulk, or UsbdPipeTypeInterrupt. The OSR USB FX2 device supports an interrupt pipe, a bulk-in pipe, and a bulk-out pipe, so **PipeInfo** is set to either UsbdPipeTypeInterrupt or UsbdPipeTypeBulk. The UsbdPipeTypeBulk value identifies bulk pipes, but does not provide the pipe's direction. The direction information is encoded in the high bit of the pipe address, which is stored in the **WINUSB\_PIPE\_INFORMATION** structure's **PipeId** member. The simplest way to determine the direction of the pipe is to pass the **PipeId** value to one of the following macros from Usb100.h:

    -   The `USB_ENDPOINT_DIRECTION_IN (PipeId)` macro returns **TRUE** if the direction is in.
    -   The `USB_ENDPOINT_DIRECTION_OUT(PipeId)` macro returns **TRUE** if the direction is out.

    The application uses the **PipeId** value to identify which pipe to use for data transfer in calls to WinUSB functions, such as [**WinUsb\_ReadPipe**](https://msdn.microsoft.com/library/windows/hardware/ff540297) (described in the "Issue I/O Requests" section of this topic), so the example stores all three **PipeId** values for later use.

The following example code gets the speed of the device that is specified by the WinUSB interface handle.

```ManagedCPlusPlus
BOOL GetUSBDeviceSpeed(WINUSB_INTERFACE_HANDLE hDeviceHandle, UCHAR* pDeviceSpeed)
{
    if (!pDeviceSpeed || hDeviceHandle==INVALID_HANDLE_VALUE)
    {
        return FALSE;
    }

    BOOL bResult = TRUE;

    ULONG length = sizeof(UCHAR);

    bResult = WinUsb_QueryDeviceInformation(hDeviceHandle, DEVICE_SPEED, &length, pDeviceSpeed);
    if(!bResult)
    {
        printf("Error getting device speed: %d.\n", GetLastError());
        goto done;
    }

    if(*pDeviceSpeed == LowSpeed)
    {
        printf("Device speed: %d (Low speed).\n", *pDeviceSpeed);
        goto done;
    }
    if(*pDeviceSpeed == FullSpeed)
    {
        printf("Device speed: %d (Full speed).\n", *pDeviceSpeed);
        goto done;
    }
    if(*pDeviceSpeed == HighSpeed)
    {
        printf("Device speed: %d (High speed).\n", *pDeviceSpeed);
        goto done;
    }

done:
    return bResult;
}
```

The following example code queries the various descriptors for the USB device that is specified by the WinUSB interface handle. The example function retrieves the types of supported endpoints and their pipe identifiers. The example stores all three PipeId values for later use.

```ManagedCPlusPlus
struct PIPE_ID
{
    UCHAR  PipeInId;
    UCHAR  PipeOutId;
};

BOOL QueryDeviceEndpoints (WINUSB_INTERFACE_HANDLE hDeviceHandle, PIPE_ID* pipeid)
{
    if (hDeviceHandle==INVALID_HANDLE_VALUE)
    {
        return FALSE;
    }

    BOOL bResult = TRUE;

    USB_INTERFACE_DESCRIPTOR InterfaceDescriptor;
    ZeroMemory(&InterfaceDescriptor, sizeof(USB_INTERFACE_DESCRIPTOR));

    WINUSB_PIPE_INFORMATION  Pipe;
    ZeroMemory(&Pipe, sizeof(WINUSB_PIPE_INFORMATION));

    
    bResult = WinUsb_QueryInterfaceSettings(hDeviceHandle, 0, &InterfaceDescriptor);

    if (bResult)
    {
        for (int index = 0; index < InterfaceDescriptor.bNumEndpoints; index++)
        {
            bResult = WinUsb_QueryPipe(hDeviceHandle, 0, index, &Pipe);

            if (bResult)
            {
                if (Pipe.PipeType == UsbdPipeTypeControl)
                {
                    printf("Endpoint index: %d Pipe type: Control Pipe ID: %d.\n", index, Pipe.PipeType, Pipe.PipeId);
                }
                if (Pipe.PipeType == UsbdPipeTypeIsochronous)
                {
                    printf("Endpoint index: %d Pipe type: Isochronous Pipe ID: %d.\n", index, Pipe.PipeType, Pipe.PipeId);
                }
                if (Pipe.PipeType == UsbdPipeTypeBulk)
                {
                    if (USB_ENDPOINT_DIRECTION_IN(Pipe.PipeId))
                    {
                        printf("Endpoint index: %d Pipe type: Bulk Pipe ID: %c.\n", index, Pipe.PipeType, Pipe.PipeId);
                        pipeid->PipeInId = Pipe.PipeId;
                    }
                    if (USB_ENDPOINT_DIRECTION_OUT(Pipe.PipeId))
                    {
                        printf("Endpoint index: %d Pipe type: Bulk Pipe ID: %c.\n", index, Pipe.PipeType, Pipe.PipeId);
                        pipeid->PipeOutId = Pipe.PipeId;
                    }

                }
                if (Pipe.PipeType == UsbdPipeTypeInterrupt)
                {
                    printf("Endpoint index: %d Pipe type: Interrupt Pipe ID: %d.\n", index, Pipe.PipeType, Pipe.PipeId);
                }
            }
            else
            {
                continue;
            }
        }
    }

done:
    return bResult;
}
```

## <a href="" id="control"></a>Step 3: Send Control Transfer to the Default Endpoint


Next, communicate with the device by issuing control request to the default endpoint.

All USB devices have a default endpoint in addition to the endpoints that are associated with interfaces. The primary purpose of the default endpoint is to provide the host with information that it can use to configure the device. However, devices can also use the default endpoint for device-specific purposes. For example, the OSR USB FX2 device uses the default endpoint to control the light bar and seven-segment digital display.

Control commands consist of an 8-byte setup packet, which includes a request code that specifies the particular request, and an optional data buffer. The request codes and buffer formats are vendor defined. In this example, the application sends data to the device to control the light bar. The code to set the light bar is 0xD8, which is defined for convenience as SET\_BARGRAPH\_DISPLAY. For this request, the device requires a 1-byte data buffer that specifies which elements should be lit by setting the appropriate bits.

The application can set this through the user interface (UI), such as by providing a set of eight check box controls to specify which elements of the light bar should be lit. The specified elements correspond to the appropriate bits in the buffer. To avoid UI code, the example code in this section sets the bits so that alternate lights get lit up.

**Use the following steps to issue a control request.**

1.  Allocate a 1-byte data buffer and load the data into the buffer that specifies the elements that should be lit by setting the appropriate bits.
2.  Construct a setup packet in a caller-allocated [**WINUSB\_SETUP\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff540313) structure. Initialize the members to represent the request type and data as follows:
    -   The **RequestType** member specifies request direction. It is set to 0, which indicates host-to-device data transfer. For device-to-host transfers, set RequestType to 1.
    -   The **Request** member is set to the vendor-defined code for this request, 0xD8. It is defined for convenience as SET\_BARGRAPH\_DISPLAY.
    -   The **Length** member is set to the size of the data buffer.
    -   The **Index** and **Value** members are not required for this request, so they are set to zero.

3.  Call [**WinUsb\_ControlTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff540219) to transmit the request to the default endpoint by passing the device's WinUSB interface handle, the setup packet, and the data buffer. The function receives the number of bytes that were transferred to the device in the *LengthTransferred* parameter.

The following code example sends a control request to the specified USB device to control the lights on the light bar.

```ManagedCPlusPlus
BOOL SendDatatoDefaultEndpoint(WINUSB_INTERFACE_HANDLE hDeviceHandle)
{
    if (hDeviceHandle==INVALID_HANDLE_VALUE)
    {
        return FALSE;
    }

    BOOL bResult = TRUE;

    
    UCHAR bars = 0;

    WINUSB_SETUP_PACKET SetupPacket;
    ZeroMemory(&SetupPacket, sizeof(WINUSB_SETUP_PACKET));
    ULONG cbSent = 0;

    //Set bits to light alternate bars
    for (short i = 0; i < 7; i+= 2)
    {
        bars += 1 << i;
    }

    //Create the setup packet
    SetupPacket.RequestType = 0;
    SetupPacket.Request = 0xD8;
    SetupPacket.Value = 0;
    SetupPacket.Index = 0; 
    SetupPacket.Length = sizeof(UCHAR);

    bResult = WinUsb_ControlTransfer(hDeviceHandle, SetupPacket, &bars, sizeof(UCHAR), &cbSent, 0);
    if(!bResult)
    {
        goto done;
    }

    printf("Data sent: %d \nActual data transferred: %d.\n", sizeof(bars), cbSent);


done:
    return bResult;

}
```

## <a href="" id="io"></a>Step 4: Issue I/O Requests


Next, send data to the device's bulk-in and bulk-out endpoints that can be used for read and write requests, respectively. On the OSR USB FX2 device, these two endpoints are configured for loopback, so the device moves data from the bulk-in endpoint to the bulk-out endpoint. It does not change the value of the data or add any new data. For loopback configuration, a read request reads the data that was sent by the most recent write request. WinUSB provides the following functions for sending write and read requests:

-   [**WinUsb\_WritePipe**](https://msdn.microsoft.com/library/windows/hardware/ff540322)
-   [**WinUsb\_ReadPipe**](https://msdn.microsoft.com/library/windows/hardware/ff540297)

**To send a write request**

1.  Allocate a buffer and fill it with the data that you want to write to the device. There is no limitation on the buffer size if the application does not set RAW\_IO as the pipe's policy type. WinUSB divides the buffer into appropriately sized chunks, if necessary. If RAW\_IO is set, the size of the buffer is limited by the maximum transfer size supported by WinUSB.
2.  Call [**WinUsb\_WritePipe**](https://msdn.microsoft.com/library/windows/hardware/ff540322) to write the buffer to the device. Pass the WinUSB interface handle for the device, the pipe identifier for the bulk-out pipe (as described in the [Query the Device for USB Descriptors](#query) section of this topic), and the buffer. The function returns the number of bytes that are actually written to the device in the *bytesWritten* parameter. The *Overlapped* parameter is set to **NULL** to request a synchronous operation. To perform an asynchronous write request, set *Overlapped* to a pointer to an **OVERLAPPED** structure.

Write requests that contain zero-length data are forwarded down the USB stack. If the transfer length is greater than a maximum transfer length, WinUSB divides the request into smaller requests of maximum transfer length and submits them serially.
The following code example allocates a string and sends it to the bulk-out endpoint of the device.

```ManagedCPlusPlus
BOOL WriteToBulkEndpoint(WINUSB_INTERFACE_HANDLE hDeviceHandle, UCHAR* pID, ULONG* pcbWritten)
{
    if (hDeviceHandle==INVALID_HANDLE_VALUE || !pID || !pcbWritten)
    {
        return FALSE;
    }

    BOOL bResult = TRUE;

    UCHAR szBuffer[] = "Hello World";
    ULONG cbSize = strlen(szBuffer);
    ULONG cbSent = 0;

    bResult = WinUsb_WritePipe(hDeviceHandle, *pID, szBuffer, cbSize, &cbSent, 0);
    if(!bResult)
    {
        goto done;
    }

    printf("Wrote to pipe %d: %s \nActual data transferred: %d.\n", *pID, szBuffer, cbSent);
    *pcbWritten = cbSent;


done:
    return bResult;

}
```

**To send a read request**

-   Call [**WinUsb\_ReadPipe**](https://msdn.microsoft.com/library/windows/hardware/ff540297) to read data from the bulk-in endpoint of the device. Pass the WinUSB interface handle of the device, the pipe identifier for the bulk-in endpoint, and an appropriately sized empty buffer. When the function returns, the buffer contains the data that was read from the device. The number of bytes that were read is returned in the function's *bytesRead* parameter. For read requests, the buffer must be a multiple of the maximum packet size.

Zero-length read requests complete immediately with success and are not sent down the stack. If the transfer length is greater than a maximum transfer length, WinUSB divides the request into smaller requests of maximum transfer length and submits them serially. If the transfer length is not a multiple of the endpoint's **MaxPacketSize**, WinUSB increases the size of the transfer to the next multiple of MaxPacketSize. If a device returns more data than was requested, WinUSB saves the excess data. If data remains from a previous read request, WinUSB copies it to the beginning of the next read request and completes the request, if necessary.
The following code example reads data from the bulk-in endpoint of the device.

```ManagedCPlusPlus
BOOL ReadFromBulkEndpoint(WINUSB_INTERFACE_HANDLE hDeviceHandle, UCHAR* pID, ULONG cbSize)
{
    if (hDeviceHandle==INVALID_HANDLE_VALUE)
    {
        return FALSE;
    }

    BOOL bResult = TRUE;

    UCHAR* szBuffer = (UCHAR*)LocalAlloc(LPTR, sizeof(UCHAR)*cbSize);
    
    ULONG cbRead = 0;

    bResult = WinUsb_ReadPipe(hDeviceHandle, *pID, szBuffer, cbSize, &cbRead, 0);
    if(!bResult)
    {
        goto done;
    }

    printf("Read from pipe %d: %s \nActual data read: %d.\n", *pID, szBuffer, cbRead);


done:
    LocalFree(szBuffer);
    return bResult;

}
```

## Step 5: Release the Device Handles


After you have completed all the required calls to the device, release the file handle and the WinUSB interface handle for the device. For this, call the following functions:

-   **CloseHandle** to release the handle that was created by **CreateFile**, as described in the step 1.
-   [**WinUsb\_Free**](https://msdn.microsoft.com/library/windows/hardware/ff540233) to release the WinUSB interface handle for the device, which is returned by [**WinUsb\_Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff540277).

## Step 6: Implement Main


The following code example shows the main function of your console application.

```ManagedCPlusPlus
int _tmain(int argc, _TCHAR* argv[])
{

    GUID guidDeviceInterface = OSR_DEVICE_INTERFACE; //in the INF file

    BOOL bResult = TRUE;

    PIPE_ID PipeID;

    HANDLE hDeviceHandle = INVALID_HANDLE_VALUE;
    WINUSB_INTERFACE_HANDLE hWinUSBHandle = INVALID_HANDLE_VALUE;
    
    UCHAR DeviceSpeed;
    ULONG cbSize = 0;

    bResult = GetDeviceHandle(guidDeviceInterface, &hDeviceHandle);
    if(!bResult)
    {
        goto done;
    }

    bResult = GetWinUSBHandle(hDeviceHandle, &hWinUSBHandle);
    if(!bResult)
    {
        goto done;
    }

    bResult = GetUSBDeviceSpeed(hWinUSBHandle, &DeviceSpeed);
    if(!bResult)
    {
        goto done;
    }

    bResult = QueryDeviceEndpoints(hWinUSBHandle, &PipeID);
    if(!bResult)
    {
        goto done;
    }

    bResult = SendDatatoDefaultEndpoint(hWinUSBHandle);
    if(!bResult)
    {
        goto done;
    }

    bResult = WriteToBulkEndpoint(hWinUSBHandle, &PipeID.PipeOutId, &cbSize);
    if(!bResult)
    {
        goto done;
    }

    bResult = ReadFromBulkEndpoint(hWinUSBHandle, &PipeID.PipeInId, cbSize);
    if(!bResult)
    {
        goto done;
    }


    system("PAUSE");

done:
    CloseHandle(hDeviceHandle);
    WinUsb_Free(hWinUSBHandle);

    return 0;
}
```

## Next steps


If your device supports isochronous endpoints, you can use [WinUSB Functions](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb) to send transfers. This feature is only supported in Windows 8.1.

For more information, see [Send USB isochronous transfers from a WinUSB desktop app](getting-set-up-to-use-windows-devices-usb.md).

## Related topics
[WinUSB](winusb.md)  
[WinUSB Architecture and Modules](winusb-architecture.md)  
[WinUSB (Winusb.sys) Installation](winusb-installation.md)  
[WinUSB Functions for Pipe Policy Modification](winusb-functions-for-pipe-policy-modification.md)  
[WinUSB Power Management](winusb-power-management.md)  
[WinUSB Functions](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb)  
[Write a Windows desktop app based on the WinUSB template](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md)  



