---
Description: Learn about a USB bulk transfer and how to initiate a transfer request from your UWP app that communicates with a USB device.
title: How to send a USB bulk transfer request (UWP app)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to send a USB bulk transfer request (UWP app)


**Summary**

-   Reading from bulk IN pipes
-   Writing to bulk OUT pipes
-   Modifying the bulk pipe policy

**Important APIs**

-   **UsbBulkInPipe, UsbBulkOutPipe**
-   **DataReader, DataWriter**
-   **UsbReadOptions, UsbWriteOptions**

In this topic, you'll learn about a USB bulk transfer and how to initiate a transfer request from your UWP app that communicates with a USB device.

USB full speed, high speed, and SuperSpeed devices can support bulk endpoints. Those endpoints are used for transferring transfer large amounts of data, such as transferring data to or from a USB flash drive. Bulk transfers are reliable because they allow error detection and involves limited number of retries to make sure the data is received by the host or the device. Bulk transfers are used for data that is not time critical. Data is transferred only when there is unused bandwidth available on the bus. Therefore, when the bus is busy with other transfers, bulk data can wait indefinitely.

Bulk endpoints are unidirectional and in one transfer, data can be transferred either in an IN or OUT direction. To support reading and writing of bulk data, the device must support bulk IN and bulk OUT endpoints. Bulk IN endpoint is used to read data from the device to the host and bulk OUT endpoint is used to send data from the host to the device.

In order to initiate a bulk transfer request, your app must have a reference to the *pipe* that represents an endpoint. A pipe is a communication channel opened by the device driver when the device is configured. For the app, a pipe is a logical representation of an endpoint. To read data from the endpoint, the app gets data from the associated bulk IN pipe. To write data to the endpoint, the app sends data to the bulk OUT pipe. For bulk read and write pipes, use [**UsbBulkInPipe**](https://msdn.microsoft.com/library/windows/apps/dn297573) and [**UsbBulkOutPipe**](https://msdn.microsoft.com/library/windows/apps/dn297647) classes.

Your app can also modify the behavior of the pipe by setting certain policy flags. For example for a read request, you can set a flag that automatically clears a stall condition on the pipe. For information about those flags, see [**UsbReadOptions**](https://msdn.microsoft.com/library/windows/apps/dn278430) and [**UsbWriteOptions**](https://msdn.microsoft.com/library/windows/apps/dn278464).

## Before you start...


-   You have must opened the device and obtained the [**UsbDevice**](https://msdn.microsoft.com/library/windows/apps/dn263883) object. Read [How to connect to a USB device (UWP app)](how-to-connect-to-a-usb-device--uwp-app-.md).
-   You can see the complete code shown in this topic in the CustomUsbDeviceAccess sample, Scenario4\_BulkPipes files.

## Step 1: Get the bulk pipe object


To initiate a transfer request, you must obtain a reference to the bulk pipe object ([**UsbBulkOutPipe**](https://msdn.microsoft.com/library/windows/apps/dn297647) or [**UsbBulkInPipe**](https://msdn.microsoft.com/library/windows/apps/dn297573)). You can get pipes by enumerating all settings of all interfaces. However, for data transfers you must only use pipes of an active setting. If the pipe object is null if the associated endpoint is not in the active setting.

If you want to...
Use this property value
Send data to a bulk pipe, obtain a reference to [**UsbBulkOutPipe**](https://msdn.microsoft.com/library/windows/apps/dn297647).
[**UsbDevice.DefaultInterface.BulkOutPipes\[n\]**](https://msdn.microsoft.com/library/windows/apps/dn264288) if your device configuration exposes one USB interface.
[**UsbDevice.Configuration.UsbInterfaces\[m\].BulkOutPipes\[n\]**](https://msdn.microsoft.com/library/windows/apps/dn264288) for enumerating bulk OUT pipes in multiple interfaces supported by the device.
[**UsbInterface.InterfaceSettings\[m\].BulkOutEndpoints \[n\].Pipe**](https://msdn.microsoft.com/library/windows/apps/dn278424) for enumerating bulk OUT pipes defined by settings in an interface.
[**UsbEndpointDescriptor.AsBulkOutEndpointDescriptor.Pipe**](https://msdn.microsoft.com/library/windows/apps/dn278424) for getting the pipe object from the endpoint descriptor for the bulk OUT endpoint.
Receive data from a bulk pipe, you can obtain the [**UsbBulkInPipe**](https://msdn.microsoft.com/library/windows/apps/dn297573) object
[**UsbDevice.DefaultInterface.BulkInPipes\[n\]**](https://msdn.microsoft.com/library/windows/apps/dn264287) if your device configuration exposes one USB interface.
[**UsbDevice.Configuration.UsbInterfaces\[m\].BulkInPipes\[n\]**](https://msdn.microsoft.com/library/windows/apps/dn264287) for enumerating bulk IN pipes in multiple interfaces supported by the device.
[**UsbInterface.InterfaceSettings\[m\].BulkInEndpoints \[n\].Pipe**](https://msdn.microsoft.com/library/windows/apps/dn297567) for enumerating bulk IN pipes defined by settings in an interface.
[**UsbEndpointDescriptor.AsBulkInEndpointDescriptor.Pipe**](https://msdn.microsoft.com/library/windows/apps/dn297567) for getting the pipe object from the endpoint descriptor for the bulk IN endpoint.


Note: should be in the active setting or requires a null check.

## Step 2: Configure the bulk pipe (Optional)


You can modify the behavior of the read or write operation by setting certain flags on the retrieved bulk pipe.

For reading from the device, set the [**UsbBulkInPipe.ReadOptions**](https://msdn.microsoft.com/library/windows/apps/dn297615) property to one of values defined in [**UsbReadOptions**](https://msdn.microsoft.com/library/windows/apps/dn278430). In the case of writing, set the [**UsbBulkOutPipe.WriteOptions**](https://msdn.microsoft.com/library/windows/apps/dn297671) property to one of values defined in **UsbWriteOptions**.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>If you want to...</th>
<th>Set this flag</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Automatically clear any error condition on the endpoint without stopping data flow</p></td>
<td><strong>AutoClearStall</strong>
<p>For more information, see <a href="#stall" data-raw-source="[Clearing stall conditions](#stall)">Clearing stall conditions</a>. This flag applies to both read and write transfers.</p></td>
</tr>
<tr class="even">
<td><p>Send multiple read requests with maximum efficiency. Boost performance by bypassing error checking.</p></td>
<td><strong>OverrideAutomaticBufferManagement</strong>
<p>A data request can be divided into one or more transfers, where each transfer contains a certain number of bytes called the <em>maximum transfer size</em>. For multiple transfers, there might be delay in queuing two transfers due to error checking performed by the driver. This flag bypasses that error checking. To get the maximum transfer size, use the <a href="https://msdn.microsoft.com/library/windows/apps/dn297606" data-raw-source="[&lt;strong&gt;UsbBulkInPipe.MaxTransferSizeBytes&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn297606)"><strong>UsbBulkInPipe.MaxTransferSizeBytes</strong></a> property. If your request size is <strong>UsbBulkInPipe.MaxTransferSizeBytes</strong>, you must set this flag. Note:</p>
<p></p>
<div class="alert">
<strong>Important</strong><br/><p>If you set this flag, then you must request data in multiples of the pipe&#39;s maximum packet size. That information is stored in the endpoint descriptor. The size depends on the bus speed of the device. For full speed, high speed, and SuperSpeed; the maximum packet sizes are 64, 512, and 1024 bytes respectively. To obtain that value, use the <a href="https://msdn.microsoft.com/library/windows/apps/dn297563" data-raw-source="[&lt;strong&gt;UsbBulkInPipe.EndpointDescriptor.MaxPacketSize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn297563)"><strong>UsbBulkInPipe.EndpointDescriptor.MaxPacketSize</strong></a> property.</p>
</div>
<div>

</div>
This flag only applies to read transfers.</td>
</tr>
<tr class="odd">
<td><p>Terminate a write request with a zero-length packet</p></td>
<td><strong>ShortPacketTerminate</strong>
<p>Sends a zero length packet to indicate the end of an OUT transfer.This flag only applies to write transfers.</p></td>
</tr>
<tr class="even">
<td><p>Disable reading short packets (less than maximum packet size supported by the endpoint)</p></td>
<td><strong>IgnoreShortPacket</strong>
<p>By default, if the device sends bytes less than the maximum packet size, the app receives them. If you do not want to receive short packets, set this flag.</p>
<p>This flag only applies to read transfers.</p></td>
</tr>
</tbody>
</table>



## Step 3: Set up the data stream


When bulk data is sent by the device, the data is received as in input stream on the bulk pipe. Here are the steps for getting the input stream:

1.  Obtain a reference to the input stream by getting the [**UsbBulkInPipe.InputStream**](https://msdn.microsoft.com/library/windows/apps/dn297601) property.
2.  Create a [**DataReader**](https://msdn.microsoft.com/library/windows/apps/br208119) object by specifying the input stream in the [**DataReader constructor**](https://msdn.microsoft.com/library/windows/apps/br208130).

To write data to the device, the app must write to an output stream on the bulk pipe. Here are the steps for preparing the output stream:

1.  Obtain a reference to the output stream by getting the [**UsbBulkOutPipe.OutputStream**](https://msdn.microsoft.com/library/windows/apps/dn297669) property.
2.  Create a [**DataWriter**](https://msdn.microsoft.com/library/windows/apps/br208154) object by specifying the output stream in the [**DataWriter**](https://msdn.microsoft.com/library/windows/apps/br208167) constructor.
3.  Populate the data buffer associated with the output stream.
4.  Depending on the datatype, write transfer data to the output stream by calling [**DataWriter methods**](https://msdn.microsoft.com/library/windows/apps/br208167), such as [**WriteBytes**](https://msdn.microsoft.com/library/windows/apps/br208179).

## Step 4: Start an asynchronous transfer operation


Bulk transfers are initiated through asynchronous operations.

To read bulk data, start an asynchronous read operation by calling [**DataReader.LoadAsync**](https://msdn.microsoft.com/library/windows/apps/br208135).

To write bulk data, start an asynchronous write operation by calling [**DataWriter.StoreAsync**](https://msdn.microsoft.com/library/windows/apps/br208171).

## Step 5: Get results of the read transfer operation


After the asynchronous data operation is complete, you can get the number of bytes read or written from the task object. For a read operation, call [**DataReader methods**](https://msdn.microsoft.com/library/windows/apps/br208119), such as [**ReadBytes**](https://msdn.microsoft.com/library/windows/apps/br208139), to read data from the input stream.

## Clearing stall conditions


At times, the app might experience failed data transfers. A failed transfer can be due to a stall condition on the endpoint. As long as the endpoint is stalled, data cannot be written to or read from it. In order to proceed with data transfers, the app must clear the stall condition on the associated pipe.

Your app can configure the pipe to automatically clear stall conditions, when they occur. To do so, set the [**UsbBulkInPipe.ReadOptions**](https://msdn.microsoft.com/library/windows/apps/dn297615) property to **UsbReadOptions.AutoClearStall** or [**UsbBulkOutPipe.WriteOptions**](https://msdn.microsoft.com/library/windows/apps/dn297671) property to **UsbWriteOptions.AutoClearStall**. With that automatic configuration, the app does not experience failed transfers and the data transfer experience is seamless.

To clear a stall condition manually, call [**UsbBulkInPipe.ClearStallAsync**](https://msdn.microsoft.com/library/windows/apps/dn278417) for a bulk IN pipe; call [**UsbBulkOutPipe.ClearStallAsync**](https://msdn.microsoft.com/library/windows/apps/dn297654) for a bulk OUT pipe.

**Note**  A stall condition does not indicate an empty endpoint. If there is no data in the endpoint, the transfer completes but length is zero bytes.



For read operations, you might need to clear pending data in the pipe before starting a new transfer request. To do so, call [**UsbBulkInPipe.FlushBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff551975) method.

## USB bulk transfer code example


This code example shows how to write to a bulk pipe. The example sends data to the first bulk OUT pipe on the default interface. It configures the pipe to send a zero-length packet at the end of the transfer. When the transfer is complete, number of bytes are shown.

```CSharp
    private async void BulkWrite()
    {
        String dataBuffer = "Hello World!";
        UInt32 bytesWritten = 0;

        UsbBulkOutPipe writePipe = usbDevice.DefaultInterface.BulkOutPipes[0];
        writePipe.WriteOptions |= UsbWriteOptions.ShortPacketTerminate;

        var stream = writePipe.OutputStream;

        DataWriter writer = new DataWriter(stream);

        writer.WriteString(dataBuffer);

        try
        {
            bytesWritten = await writer.StoreAsync();
        }
        catch (Exception exception)
        {
            ShowStatus(exception.Message.ToString());
        }
        finally
        {
            ShowStatus("Data written: " + bytesWritten + " bytes.");
        }
    }
```

This code example shows how to read from a bulk pipe. The example retrieves data from the first bulk IN pipe on the default interface. It configures the pipe to for maximum efficiency and receives data in chunks of maximum packet size. When the transfer is complete, number of bytes are shown.

```CSharp
    private async void BulkRead()
    {
        UInt32 bytesRead = 0;

        UsbBulkInPipe readPipe = usbDevice.DefaultInterface.BulkInPipes[0];
        readPipe.ReadOptions |= UsbReadOptions.IgnoreShortPacket;

        var stream = readPipe.InputStream;
        DataReader reader = new DataReader(stream);

        try
        {
            bytesRead = await reader.LoadAsync(readPipe.EndpointDescriptor.MaxPacketSize);
        }
        catch (Exception exception)
        {
            ShowStatus(exception.Message.ToString());
        }
        finally
        {
            ShowStatus("Number of bytes: " + bytesRead);

            IBuffer buffer = reader.ReadBuffer(bytesRead);

            ShowData (buffer.ToString());

        }
    }
```








