---
Description: Starting in Windows 8.1, the set of WinUSB Functions have APIs that allow a desktop application to transfer data to and from isochronous endpoints of a USB device. For such an application, the Microsoft-provided Winusb.sys must be the device driver.
title: Send USB isochronous transfers from a WinUSB desktop app
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Send USB isochronous transfers from a WinUSB desktop app


**Summary**

-   Brief overview of isochronous transfers.
-   Transfer buffer calculation based on endpoint interval values.
-   Sending transfers that read and write isochronous data by using [WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md).

**Important APIs**

-   [**WinUsb\_QueryPipeEx**](https://msdn.microsoft.com/library/windows/hardware/dn265563)
-   [**WinUsb\_WriteIsochPipeAsap**](https://msdn.microsoft.com/library/windows/hardware/dn265569)
-   [**WinUsb\_ReadIsochPipeAsap**](https://msdn.microsoft.com/library/windows/hardware/dn265565)

Starting in Windows 8.1, the set of [WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md) have APIs that allow a desktop application to transfer data to and from isochronous endpoints of a USB device. For such an application, the Microsoft-provided Winusb.sys must be the device driver.

A USB device can support isochronous endpoints to transfer time-dependent data at a steady rate, such as with audio/video streaming. There is no guaranteed delivery. A good connection shouldn’t drop any packets, it is not normal or expected to lose packets, but the isochronous protocol is tolerant of such losses.

The host controller sends or receives data during reserved periods of time on the bus, are called *bus intervals*. The unit of bus interval depends on the bus speed. For full speed, it's 1-millisecond frames, for high speed and SuperSpeed, it's 250-microseconds microframes.

The host controller polls the device at regular intervals. For read operations, when the endpoint is ready to send data, the device responds by sending data in the bus interval. To write to the device, the host controller sends data.

**How much data can the app send in one service interval**

The term *isochronous packet* in this topic refers to the amount of data that is transferred in one service interval. That value is calculated by the USB driver stack and the app can get the value while querying pipe attributes.

The size of an isochronous packet determines the size of the transfer buffer that the app allocates. The buffer must end at a frame boundary. The total size of the transfer depends on how much data the app wants to send or receive. After the transfer is initiated by the app, the host packetizes the transfer buffer so that in each interval, the host can send or receive the maximum bytes allowed per interval.

For a data transfer, not all bus intervals are used. In this topic, bus intervals that are used are called *service intervals*.

**How to calculate the frame in which data is transmitted**

The app can choose to specify the frame in one of two ways:

-   Automatically. In this mode, the app instructs the USB driver stack to send the transfer in the next appropriate frame. The app must also specify whether the buffer is a continuous stream so that the driver stack can calculate the start frame.
-   Specifying the start frame that is later than the current frame. The app should take into consideration the latency between the time that the app starts the transfer and when the USB driver stack processes it.

**Code example discussion**

The examples in this topic demonstrate the use of these [WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md):

-   [**WinUsb\_QueryPipeEx**](https://msdn.microsoft.com/library/windows/hardware/dn265563)
-   [**WinUsb\_RegisterIsochBuffer**](https://msdn.microsoft.com/library/windows/hardware/dn265566)
-   [**WinUsb\_UnregisterIsochBuffer**](https://msdn.microsoft.com/library/windows/hardware/dn265567)
-   [**WinUsb\_WriteIsochPipeAsap**](https://msdn.microsoft.com/library/windows/hardware/dn265569)
-   [**WinUsb\_ReadIsochPipeAsap**](https://msdn.microsoft.com/library/windows/hardware/dn265565)
-   [**WinUsb\_WriteIsochPipe**](https://msdn.microsoft.com/library/windows/hardware/dn265568)
-   [**WinUsb\_ReadIsochPipe**](https://msdn.microsoft.com/library/windows/hardware/dn265564)
-   [**WinUsb\_GetCurrentFrameNumber**](https://msdn.microsoft.com/library/windows/hardware/dn265549)
-   [**WinUsb\_GetAdjustedFrameNumber**](https://msdn.microsoft.com/library/windows/hardware/dn265548)

In this topic, we'll read and write 30 milliseconds of data in three transfers to a high speed device. The pipe is capable of transferring 1024 bytes in each service interval. Because the polling interval is 1, data is transferred in every microframe of a frame. Total of 30 frames will carry 30\*8\*1024 bytes.

The function calls for sending read and write transfers are similar. The app allocates a transfer buffer big enough to hold all three transfers. The app registers the buffer for a particular pipe by calling [**WinUsb\_RegisterIsochBuffer**](https://msdn.microsoft.com/library/windows/hardware/dn265566). The call returns a registration handle which is used to send the transfer. The buffer is reused for subsequent transfers and offset in the buffer is adjusted to send or receive the next set of data.

All transfers in the example are sent asynchronously. For this, the app allocates an array of [**OVERLAPPED**](https://msdn.microsoft.com/library/windows/desktop/bb773368) structure with three elements, one for each transfer. The app provides events so that it can get notified when transfers complete and retrieve the results of the operation. For this, in each **OVERLAPPED** structure in the array, the app allocates an event and sets the handle in the **hEvent** member.

This image shows three read transfers by using the [**WinUsb\_ReadIsochPipeAsap**](https://msdn.microsoft.com/library/windows/hardware/dn265565) function. The call specifies offset and length of each transfer. The *ContinueStream* parameter value is FALSE to indicate a new stream. After that, the app requests that subsequent transfers are scheduled immediately following the last frame of the previous request to allow for continuous streaming of data. The number of isochronous packets are calculated as packets per frame \* number of frames; 8\*10. For this call, the app need not worry about calculating start frame number.

![winusb function for isochronous read transfer](images/isoch-app-read.png)

This image shows three write transfers by using the [**WinUsb\_WriteIsochPipe**](https://msdn.microsoft.com/library/windows/hardware/dn265568) function. The call specifies offset and length of each transfer. In this case, the app must calculate the frame number in which the host controller can start sending data. On output, the function receives the frame number of the frame that follows the last frame used in the previous transfer. To get the current frame, the app calls [**WinUsb\_GetCurrentFrameNumber**](https://msdn.microsoft.com/library/windows/hardware/dn265549). At this point, the app must make sure that the start frame of the next transfer is later than the current frame, so that the USB driver stack does not drop late packets. To do so, the app calls [**WinUsb\_GetAdjustedFrameNumber**](https://msdn.microsoft.com/library/windows/hardware/dn265548) to get a realistic current frame number (this is later than the received current frame number). To be on the safe side, the app adds five more frames, and then sends the transfer.

![winusb function for isochronous write transfer](images/isoch-app-write.png)

After each transfer completes, the app gets the results of the transfer by calling [**WinUsb\_GetOverlappedResult**](https://msdn.microsoft.com/library/windows/hardware/ff540263). The *bWait* parameter is set to TRUE so that the call does not return until the operation has completed. For read and write transfers, the *lpNumberOfBytesTransferred* parameter is always 0. For a write transfer, the app assumes that if the operation completed successfully, all bytes were transferred. For a read transfer, the **Length** member of each isochronous packet ([**USBD\_ISO\_PACKET\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff539084)), contains the number bytes transferred in that packet, per interval. To get the total length, the app adds all **Length** values.

When finished, the app releases the isochronous buffer handles by calling [**WinUsb\_UnregisterIsochBuffer**](https://msdn.microsoft.com/library/windows/hardware/dn265567).

## Before you start...


Make sure that,

-   The device driver is the Microsoft-provided driver: WinUSB (Winusb.sys). That driver is included in the \\Windows\\System32\\ folder. For more information, see [WinUSB (Winusb.sys) Installation](winusb-installation.md).

-   You have previously obtained a WinUSB interface handle to device by calling [**WinUsb\_Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff540277). All operations are performed by using that handle. Read [How to Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md).

-   The active interface setting has isochronous endpoints. Otherwise, you cannot access the pipes for the target endpoints.

## Step 1: Find the isochronous pipe in the active setting


1.  Get the USB interface that has the isochronous endpoints by calling [**WinUsb\_QueryInterfaceSettings**](https://msdn.microsoft.com/library/windows/hardware/ff540292).
2.  Enumerate the pipes of the interface setting that defines the endpoints.
3.  For each endpoint get the associated pipe properties in a [**WINUSB\_PIPE\_INFORMATION\_EX**](https://msdn.microsoft.com/library/windows/hardware/dn265570) structure by calling [**WinUsb\_QueryPipeEx**](https://msdn.microsoft.com/library/windows/hardware/dn265563). The retrieved **WINUSB\_PIPE\_INFORMATION\_EX** structure that contains information about the isochronous pipe. The structure contains information about the pipe, its type, id, and so on.
4.  Check the structure members to determine whether it's the pipe that must be used for transfers. If it is, store the **PipeId** value. In the template code, add members to the DEVICE\_DATA structure, defined in Device.h.

This example shows how to determine whether the active setting has isochronous endpoints and obtain information about them. In this example the device is a SuperMUTT device. The device has two isochronous endpoints in the default interface, alternate setting 1.

```ManagedCPlusPlus

typedef struct _DEVICE_DATA {

    BOOL                    HandlesOpen;
    WINUSB_INTERFACE_HANDLE WinusbHandle;
    HANDLE                  DeviceHandle;
    TCHAR                   DevicePath[MAX_PATH];
    UCHAR                   IsochOutPipe;
    UCHAR                   IsochInPipe;

} DEVICE_DATA, *PDEVICE_DATA;

HRESULT
       GetIsochPipes(
       _Inout_ PDEVICE_DATA DeviceData
       )
{
       BOOL result;
       USB_INTERFACE_DESCRIPTOR usbInterface;
       WINUSB_PIPE_INFORMATION_EX pipe;
       HRESULT hr = S_OK;
       UCHAR i;

       result = WinUsb_QueryInterfaceSettings(DeviceData->WinusbHandle,
              0,
              &usbInterface);

       if (result == FALSE)
       {
              hr = HRESULT_FROM_WIN32(GetLastError());
              printf(_T("WinUsb_QueryInterfaceSettings failed to get USB interface.\n"));
              CloseHandle(DeviceData->DeviceHandle);
              return hr;
       }

       for (i = 0; i < usbInterface.bNumEndpoints; i++)
       {
              result = WinUsb_QueryPipeEx(
                     DeviceData->WinusbHandle,
                     1,
                     (UCHAR) i,
                     &pipe);

              if (result == FALSE)
              {
                     hr = HRESULT_FROM_WIN32(GetLastError());
                     printf(_T("WinUsb_QueryPipeEx failed to get USB pipe.\n"));
                     CloseHandle(DeviceData->DeviceHandle);
                     return hr;
              }

              if ((pipe.PipeType == UsbdPipeTypeIsochronous) && (!(pipe.PipeId == 0x80)))
              {
                     DeviceData->IsochOutPipe = pipe.PipeId;
              }
              else if (pipe.PipeType == UsbdPipeTypeIsochronous)
              {
                     DeviceData->IsochInPipe = pipe.PipeId;
              }
       }

       return hr;
}
```

The SuperMUTT device defines its isochronous endpoints in the default interface, at setting 1. The preceding code obtains the **PipeId** values and stores them in the DEVICE\_DATA structure.

## Step 2: Get interval information about the isochronous pipe


Next, get more information about the pipe that you obtained in call to [**WinUsb\_QueryPipeEx**](https://msdn.microsoft.com/library/windows/hardware/dn265563).

-   **Transfer size**

    1.  From the retrieved [**WINUSB\_PIPE\_INFORMATION\_EX**](https://msdn.microsoft.com/library/windows/hardware/dn265570) structure, obtain the **MaximumBytesPerInterval** and **Interval** values.
    2.  Depending on the amount of isochronous data you want to send or receive, calculate the transfer size. For example, consider this calculation:

        ` TransferSize = ISOCH_DATA_SIZE_MS * pipeInfoEx.MaximumBytesPerInterval * (8 / pipeInfoEx.Interval);             `

        In the example, transfer size is calculated for 10 milliseconds of isochronous data.

-   **Number of isochronous packets**For example, consider this calculation:

    To calculate the total number of isochronous packets required to hold the entire transfer. This information is required for read transfers and calculated as, `>IsochInTransferSize / pipe.MaximumBytesPerInterval;             `.

This example shows add code to step 1 example and gets the interval values for the isochronous pipes.

```ManagedCPlusPlus

#define ISOCH_DATA_SIZE_MS   10

typedef struct _DEVICE_DATA {

    BOOL                    HandlesOpen;
    WINUSB_INTERFACE_HANDLE WinusbHandle;
    HANDLE                  DeviceHandle;
    TCHAR                   DevicePath[MAX_PATH];
                UCHAR                   IsochOutPipe;
                UCHAR                   IsochInPipe;
                ULONG                   IsochInTransferSize;
                ULONG                   IsochOutTransferSize;
                ULONG                   IsochInPacketCount;

} DEVICE_DATA, *PDEVICE_DATA;


...

if ((pipe.PipeType == UsbdPipeTypeIsochronous) && (!(pipe.PipeId == 0x80)))
{
       DeviceData->IsochOutPipe = pipe.PipeId;

       if ((pipe.MaximumBytesPerInterval == 0) || (pipe.Interval == 0))
       {
         hr = E_INVALIDARG;             
             printf("Isoch Out: MaximumBytesPerInterval or Interval value is 0.\n");
             CloseHandle(DeviceData->DeviceHandle);
             return hr;
       }
       else
       {
             DeviceData->IsochOutTransferSize = 
                 ISOCH_DATA_SIZE_MS * 
                 pipe.MaximumBytesPerInterval *
                 (8 / pipe.Interval);
       }
}
else if (pipe.PipeType == UsbdPipeTypeIsochronous)
{
       DeviceData->IsochInPipe = pipe.PipeId;

       if (pipe.MaximumBytesPerInterval == 0 || (pipe.Interval == 0))
       {
         hr = E_INVALIDARG;    
             printf("Isoch Out: MaximumBytesPerInterval or Interval value is 0.\n");
             CloseHandle(DeviceData->DeviceHandle);
             return hr;
       }
       else
       {
             DeviceData->IsochInTransferSize = 
                 ISOCH_DATA_SIZE_MS * 
                 pipe.MaximumBytesPerInterval * 
                 (8 / pipe.Interval);

             DeviceData->IsochInPacketCount = 
                  DeviceData->IsochInTransferSize / pipe.MaximumBytesPerInterval;
       }
}

...
```

In the preceding code, the app gets **Interval** and **MaximumBytesPerInterval** from [**WINUSB\_PIPE\_INFORMATION\_EX**](https://msdn.microsoft.com/library/windows/hardware/dn265570) to calculate the transfer size and number of isochronous packets required for the read transfer. For both isochronous endpoints, **Interval** is 1. That value indicates that all microframes of the frame carry data. Based on that, to send 10 milliseconds of data, you need 10 frames, total transfer size is 10\*1024\*8 bytes and 80 isochronous packets, each 1024 bytes long.

## Step 3: Send a write transfer to send data to an isochronous OUT endpoint


This procedure summarizes the steps for writing data to an isochronous endpoint.

1.  Allocate a buffer that contains the data to send.
2.  If you are sending the data asynchronously, allocate and initialize an [**OVERLAPPED**](https://msdn.microsoft.com/library/windows/desktop/bb773368) structure that contains a handle to a caller-allocated event object. The structure must be initialized to zero, otherwise the call fails.
3.  Register the buffer by calling [**WinUsb\_RegisterIsochBuffer**](https://msdn.microsoft.com/library/windows/hardware/dn265566).
4.  Start the transfer by calling [**WinUsb\_WriteIsochPipeAsap**](https://msdn.microsoft.com/library/windows/hardware/dn265569). If you want to manually specify the frame in which data will be transferred, call [**WinUsb\_WriteIsochPipe**](https://msdn.microsoft.com/library/windows/hardware/dn265568) instead.
5.  Get results of the transfer by calling [**WinUsb\_GetOverlappedResult**](https://msdn.microsoft.com/library/windows/hardware/ff540263).
6.  When finished, release the buffer handle by calling [**WinUsb\_UnregisterIsochBuffer**](https://msdn.microsoft.com/library/windows/hardware/dn265567), the overlapped event handle, and the transfer buffer.

Here is an example that shows how to send a write transfer.

```ManagedCPlusPlus
#define ISOCH_TRANSFER_COUNT   3

VOID
    SendIsochOutTransfer(
    _Inout_ PDEVICE_DATA DeviceData,
    _In_ BOOL AsapTransfer
    )
{
    PUCHAR writeBuffer;
    LPOVERLAPPED overlapped;
    ULONG numBytes;
    BOOL result;
    DWORD lastError;
    WINUSB_ISOCH_BUFFER_HANDLE isochWriteBufferHandle;
    ULONG frameNumber;
    ULONG startFrame;
    LARGE_INTEGER timeStamp;
    ULONG i;
    ULONG totalTransferSize;

    isochWriteBufferHandle = INVALID_HANDLE_VALUE;
    writeBuffer = NULL;
    overlapped = NULL;

    printf(_T("\n\nWrite transfer.\n"));

    totalTransferSize = DeviceData->IsochOutTransferSize * ISOCH_TRANSFER_COUNT;

    if (totalTransferSize % DeviceData->IsochOutBytesPerFrame != 0)
    {
        printf(_T("Transfer size must end at a frame boundary.\n"));
        goto Error;
    }

    writeBuffer = new UCHAR[totalTransferSize];

    if (writeBuffer == NULL)
    {
        printf(_T("Unable to allocate memory.\n"));
        goto Error;
    }

    ZeroMemory(writeBuffer, totalTransferSize);

    overlapped = new OVERLAPPED[ISOCH_TRANSFER_COUNT];
    if (overlapped == NULL)
    {
        printf("Unable to allocate memory.\n");
        goto Error;

    }

    ZeroMemory(overlapped, (sizeof(OVERLAPPED) * ISOCH_TRANSFER_COUNT));

    for (i = 0; i < ISOCH_TRANSFER_COUNT; i++)
    {
        overlapped[i].hEvent = CreateEvent(NULL, TRUE, FALSE, NULL);

        if (overlapped[i].hEvent == NULL)
        {
            printf("Unable to set event for overlapped operation.\n");
            goto Error;

        }
    }

    result = WinUsb_RegisterIsochBuffer(
        DeviceData->WinusbHandle,
        DeviceData->IsochOutPipe,
        writeBuffer,
        totalTransferSize,
        &isochWriteBufferHandle);

    if (!result)
    {
        printf(_T("Isoch buffer registration failed.\n"));
        goto Error;
    }

    result = WinUsb_GetCurrentFrameNumber(
                DeviceData->WinusbHandle,
                &frameNumber,
                &timeStamp);

    if (!result)
    {
        printf(_T("WinUsb_GetCurrentFrameNumber failed.\n"));
        goto Error;
    }

    startFrame = frameNumber + 5;

    for (i = 0; i < ISOCH_TRANSFER_COUNT; i++)
    {

        if (AsapTransfer)
        {
            result = WinUsb_WriteIsochPipeAsap(
                isochWriteBufferHandle,
                DeviceData->IsochOutTransferSize * i,
                DeviceData->IsochOutTransferSize,
                (i == 0) ? FALSE : TRUE,
                &overlapped[i]);

            printf(_T("Write transfer sent by using ASAP flag.\n"));
        }
        else
        {

            printf("Transfer starting at frame %d.\n", startFrame);

            result = WinUsb_WriteIsochPipe(
                isochWriteBufferHandle,
                i * DeviceData->IsochOutTransferSize,
                DeviceData->IsochOutTransferSize,
                &startFrame,
                &overlapped[i]);

            printf("Next transfer frame %d.\n", startFrame);

        }

        if (!result)
        {
            lastError = GetLastError();

            if (lastError != ERROR_IO_PENDING)
            {
                printf("Failed to send write transfer with error %x\n", lastError);
            }
        }
    }

    for (i = 0; i < ISOCH_TRANSFER_COUNT; i++)
    {
        result = WinUsb_GetOverlappedResult(
            DeviceData->WinusbHandle,
            &overlapped[i],
            &numBytes,
            TRUE);

        if (!result)
        {
            lastError = GetLastError();

            printf("Write transfer %d with error %x\n", i, lastError);
        }
        else
        {
            printf("Write transfer %d completed. \n", i);

        }
    }




Error:
    if (isochWriteBufferHandle != INVALID_HANDLE_VALUE)
    {
        result = WinUsb_UnregisterIsochBuffer(isochWriteBufferHandle);
        if (!result)
        {
            printf(_T("Failed to unregister isoch write buffer. \n"));
        }
    }

    if (writeBuffer != NULL)
    {
        delete [] writeBuffer;
    }

    for (i = 0; i < ISOCH_TRANSFER_COUNT; i++)
    {
        if (overlapped[i].hEvent != NULL)
        {
            CloseHandle(overlapped[i].hEvent);
        }

    }

    if (overlapped != NULL)
    {
        delete [] overlapped;
    }


    return;
}
```

## Step 4: Send a read transfer to receive data from an isochronous IN endpoint


This procedure summarizes the steps for reading data from an isochronous endpoint.

1.  Allocate a transfer buffer that will receive data at the end of the transfer. The size of the buffer must be based on the transfer size calculate in step 2. The transfer buffer must end at a frame boundary.
2.  If you are sending the data asynchronously, allocate an [**OVERLAPPED**](https://msdn.microsoft.com/library/windows/desktop/bb773368) structure that contains a handle to a caller-allocated event object. The structure must be initialized to zero, otherwise the call fails.
3.  Register the buffer by calling [**WinUsb\_RegisterIsochBuffer**](https://msdn.microsoft.com/library/windows/hardware/dn265566).
4.  Based on the number isochronous packets calculated in step 2, allocate an array of isochronous packets ([**USBD\_ISO\_PACKET\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff539084)).
5.  Start the transfer by calling [**WinUsb\_ReadIsochPipeAsap**](https://msdn.microsoft.com/library/windows/hardware/dn265565). If you want to manually specify the start frame in which data will be transferred, call [**WinUsb\_ReadIsochPipe**](https://msdn.microsoft.com/library/windows/hardware/dn265564) instead.
6.  Get results of the transfer by calling [**WinUsb\_GetOverlappedResult**](https://msdn.microsoft.com/library/windows/hardware/ff540263).
7.  When finished, release the buffer handle by calling [**WinUsb\_UnregisterIsochBuffer**](https://msdn.microsoft.com/library/windows/hardware/dn265567), the overlapped event handle, the array of isochronous packets, and the transfer buffer.

Here is an example that shows how to send a read transfer by calling WinUsb\_ReadIsochPipeAsap and WinUsb\_ReadIsochPipe.

```ManagedCPlusPlus
#define ISOCH_TRANSFER_COUNT   3

VOID
    SendIsochInTransfer(
    _Inout_ PDEVICE_DATA DeviceData,
    _In_ BOOL AsapTransfer
    )
{
    PUCHAR readBuffer;
    LPOVERLAPPED overlapped;
    ULONG numBytes;
    BOOL result;
    DWORD lastError;
    WINUSB_ISOCH_BUFFER_HANDLE isochReadBufferHandle;
    PUSBD_ISO_PACKET_DESCRIPTOR isochPackets;
    ULONG i;
    ULONG j;

    ULONG frameNumber;
    ULONG startFrame;
    LARGE_INTEGER timeStamp;

    ULONG totalTransferSize;

    readBuffer = NULL;
    isochPackets = NULL;
    overlapped = NULL;
    isochReadBufferHandle = INVALID_HANDLE_VALUE;

    printf(_T("\n\nRead transfer.\n"));

    totalTransferSize = DeviceData->IsochOutTransferSize * ISOCH_TRANSFER_COUNT;

    if (totalTransferSize % DeviceData->IsochOutBytesPerFrame != 0)
    {
        printf(_T("Transfer size must end at a frame boundary.\n"));
        goto Error;
    }

    readBuffer = new UCHAR[totalTransferSize];

    if (readBuffer == NULL)
    {
        printf(_T("Unable to allocate memory.\n"));
        goto Error;
    }

    ZeroMemory(readBuffer, totalTransferSize);

    overlapped = new OVERLAPPED[ISOCH_TRANSFER_COUNT];
    ZeroMemory(overlapped, (sizeof(OVERLAPPED) * ISOCH_TRANSFER_COUNT));

    for (i = 0; i < ISOCH_TRANSFER_COUNT; i++)
    {
        overlapped[i].hEvent = CreateEvent(NULL, TRUE, FALSE, NULL);

        if (overlapped[i].hEvent == NULL)
        {
            printf("Unable to set event for overlapped operation.\n");
            goto Error;
        }
    }

    isochPackets = new USBD_ISO_PACKET_DESCRIPTOR[DeviceData->IsochInPacketCount * ISOCH_TRANSFER_COUNT];
    ZeroMemory(isochPackets, DeviceData->IsochInPacketCount * ISOCH_TRANSFER_COUNT);

    result = WinUsb_RegisterIsochBuffer(
        DeviceData->WinusbHandle,
        DeviceData->IsochInPipe,
        readBuffer,
        DeviceData->IsochInTransferSize * ISOCH_TRANSFER_COUNT,
        &isochReadBufferHandle);

    if (!result)
    {
        printf(_T("Isoch buffer registration failed.\n"));
        goto Error;
    }

    result = WinUsb_GetCurrentFrameNumber(
                DeviceData->WinusbHandle,
                &frameNumber,
                &timeStamp);

    if (!result)
    {
        printf(_T("WinUsb_GetCurrentFrameNumber failed.\n"));
        goto Error;
    }

    startFrame = frameNumber + 5;

    for (i = 0; i < ISOCH_TRANSFER_COUNT; i++)
    {
        if (AsapTransfer)
        {
            result = WinUsb_ReadIsochPipeAsap(
                isochReadBufferHandle,
                DeviceData->IsochInTransferSize * i,
                DeviceData->IsochInTransferSize,
                (i == 0) ? FALSE : TRUE,
                DeviceData->IsochInPacketCount,
                &isochPackets[i * DeviceData->IsochInPacketCount],
                &overlapped[i]);

            printf(_T("Read transfer sent by using ASAP flag.\n"));

        }
        else
        {

            printf("Transfer starting at frame %d.\n", startFrame);

            result = WinUsb_ReadIsochPipe(
                isochReadBufferHandle,
                DeviceData->IsochInTransferSize * i,
                DeviceData->IsochInTransferSize,
                &startFrame,
                DeviceData->IsochInPacketCount,
                &isochPackets[i * DeviceData->IsochInPacketCount],
                &overlapped[i]);

            printf("Next transfer frame %d.\n", startFrame);

        }

        if (!result)
        {
            lastError = GetLastError();

            if (lastError != ERROR_IO_PENDING)
            {
                printf("Failed to start a read operation with error %x\n", lastError);
            }
        }
    }

    for (i = 0; i < ISOCH_TRANSFER_COUNT; i++)
    {
        result = WinUsb_GetOverlappedResult(
            DeviceData->WinusbHandle,
            &overlapped[i],
            &numBytes,
            TRUE);

        if (!result)
        {
            lastError = GetLastError();

            printf("Failed to read with error %x\n", lastError);
        }
        else
        {
            numBytes = 0;
            for (j = 0; j < DeviceData->IsochInPacketCount; j++)
            {
                numBytes += isochPackets[j].Length;
            }

            printf("Requested %d bytes in %d packets per transfer.\n", DeviceData->IsochInTransferSize, DeviceData->IsochInPacketCount);
        }

        printf("Transfer %d completed. Read %d bytes. \n\n", i+1, numBytes);
    }



Error:
    if (isochReadBufferHandle != INVALID_HANDLE_VALUE)
    {
        result = WinUsb_UnregisterIsochBuffer(isochReadBufferHandle);
        if (!result)
        {
            printf(_T("Failed to unregister isoch read buffer. \n"));
        }
    }    

    if (readBuffer != NULL)
    {
        delete [] readBuffer;
    }

    if (isochPackets != NULL)
    {
        delete [] isochPackets;
    }

    for (i = 0; i < ISOCH_TRANSFER_COUNT; i++)

    {
        if (overlapped[i].hEvent != NULL)
        {
            CloseHandle(overlapped[i].hEvent);
        }

    }

    if (overlapped != NULL)
    {
        delete [] overlapped;
    }
    return;
}
```

## Related topics
[How to Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md)  
[WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md)  



