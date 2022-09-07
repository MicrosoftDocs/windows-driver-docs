---
description: Learn about a USB bulk transfer and how to initiate a transfer request from your UWP app that communicates with a USB device.
title: How to send a USB bulk transfer request (UWP app)
ms.date: 04/22/2021
---

# How to send a USB bulk transfer request (UWP app)

In this topic, you'll learn about a USB bulk transfer and how to initiate a transfer request from your UWP app that communicates with a USB device.

USB full speed, high speed, and SuperSpeed devices can support bulk endpoints. Those endpoints are used for transferring transfer large amounts of data, such as transferring data to or from a USB flash drive. Bulk transfers are reliable because they allow error detection and involves limited number of retries to make sure the data is received by the host or the device. Bulk transfers are used for data that is not time critical. Data is transferred only when there is unused bandwidth available on the bus. Therefore, when the bus is busy with other transfers, bulk data can wait indefinitely.

Bulk endpoints are unidirectional and in one transfer, data can be transferred either in an IN or OUT direction. To support reading and writing of bulk data, the device must support bulk IN and bulk OUT endpoints. Bulk IN endpoint is used to read data from the device to the host and bulk OUT endpoint is used to send data from the host to the device.

In order to initiate a bulk transfer request, your app must have a reference to the *pipe* that represents an endpoint. A pipe is a communication channel opened by the device driver when the device is configured. For the app, a pipe is a logical representation of an endpoint. To read data from the endpoint, the app gets data from the associated bulk IN pipe. To write data to the endpoint, the app sends data to the bulk OUT pipe. For bulk read and write pipes, use [**UsbBulkInPipe**](/uwp/api/Windows.Devices.Usb.UsbBulkInPipe) and [**UsbBulkOutPipe**](/uwp/api/Windows.Devices.Usb.UsbBulkOutPipe) classes.

Your app can also modify the behavior of the pipe by setting certain policy flags. For example for a read request, you can set a flag that automatically clears a stall condition on the pipe. For information about those flags, see [**UsbReadOptions**](/uwp/api/Windows.Devices.Usb.UsbReadOptions) and [**UsbWriteOptions**](/uwp/api/Windows.Devices.Usb.UsbWriteOptions).

## Before you start

* You have must opened the device and obtained the [**UsbDevice**](/uwp/api/Windows.Devices.Usb.UsbDevice) object. Read [How to connect to a USB device (UWP app)](how-to-connect-to-a-usb-device--uwp-app-.md).
* You can see the complete code shown in this topic in the [CustomUsbDeviceAccess sample](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/CustomUsbDeviceAccess), Scenario4\_BulkPipes files.

## Step 1: Get the bulk pipe object

To initiate a transfer request, you must obtain a reference to the bulk pipe object ([**UsbBulkOutPipe**](/uwp/api/Windows.Devices.Usb.UsbBulkOutPipe) or [**UsbBulkInPipe**](/uwp/api/Windows.Devices.Usb.UsbBulkInPipe)). You can get pipes by enumerating all settings of all interfaces. However, for data transfers you must only use pipes of an active setting. If the pipe object is null if the associated endpoint is not in the active setting.

<table>
  <thead>
    <tr>
      <th>If you want to...</th>
      <th>Use this property value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <tr>
      <td rowspan="5">Send data to a bulk pipe, obtain a reference to <a href="/uwp/api/Windows.Devices.Usb.UsbBulkOutPipe"><strong>UsbBulkOutPipe</strong></a>.</td>
      </tr>
      <tr>
      <td><a href="/uwp/api/Windows.Devices.Usb.UsbInterface#Windows_Devices_Usb_UsbInterface_BulkOutPipes"><strong>UsbDevice.DefaultInterface.BulkOutPipes[n]</strong></a> if your device configuration exposes one USB interface.</td>
      </tr>
      <tr>
      <td><a href="/uwp/api/Windows.Devices.Usb.UsbInterface#Windows_Devices_Usb_UsbInterface_BulkOutPipes"><strong>UsbDevice.Configuration.UsbInterfaces[m].BulkOutPipes[n]</strong></a>) for enumerating bulk OUT pipes in multiple interfaces supported by the device.</td>
      </tr>
       <td><a href="/uwp/api/Windows.Devices.Usb.UsbInterruptOutEndpointDescriptor#Windows_Devices_Usb_UsbInterruptOutEndpointDescriptor_Pipe"><strong>UsbInterface.InterfaceSettings\[m\].BulkOutEndpoints [n].Pipe</strong></a> for enumerating bulk OUT pipes defined by settings in an interface.</td>
      </tr>
      <tr>
      <td><a href="/uwp/api/Windows.Devices.Usb.UsbInterruptOutEndpointDescriptor#Windows_Devices_Usb_UsbInterruptOutEndpointDescriptor_Pipe"><strong>UsbEndpointDescriptor.AsBulkOutEndpointDescriptor.Pipe</strong></a> for getting the pipe object from the endpoint descriptor for the bulk OUT endpoint.
      </td>
      </tr>
    </tr>
    <tr>
      <tr>
        <td rowspan="5">Receive data from a bulk pipe, you can obtain the <a href="/uwp/api/Windows.Devices.Usb.UsbBulkInPipe"><strong>UsbBulkInPipe</strong></a> object</td>
      </tr>
       <tr>
        <td><a href="/uwp/api/Windows.Devices.Usb.UsbInterface#Windows_Devices_Usb_UsbInterface_BulkInPipes"><strong>UsbDevice.DefaultInterface.BulkInPipes[n]</strong></a> if your device configuration exposes one USB interface.</td>
       </tr>
       <tr>
       <td><a href="/uwp/api/Windows.Devices.Usb.UsbInterface#Windows_Devices_Usb_UsbInterface_BulkInPipes"><strong>UsbDevice.Configuration.UsbInterfaces[m].BulkInPipes[n]</strong></a> for enumerating bulk IN pipes in multiple interfaces supported by the device.</td>
       </tr>
       <tr>
       <td><a href="/uwp/api/Windows.Devices.Usb.UsbBulkInEndpointDescriptor#Windows_Devices_Usb_UsbBulkInEndpointDescriptor_Pipe"><strong>UsbInterface.InterfaceSettings[m].BulkInEndpoints [n].Pipe</strong></a> for enumerating bulk IN pipes defined by settings in an interface.</td>
       </tr>
       <tr>
        <td><a href="/uwp/api/Windows.Devices.Usb.UsbBulkInEndpointDescriptor#Windows_Devices_Usb_UsbBulkInEndpointDescriptor_Pipe"><strong>UsbEndpointDescriptor.AsBulkInEndpointDescriptor.Pipe</strong></a> for getting the pipe object from the endpoint descriptor for the bulk IN endpoint.</td>
      </tr>
    </tr>
  </tbody>
</table>

Note: should be in the active setting or requires a null check.

## Step 2: Configure the bulk pipe (Optional)

You can modify the behavior of the read or write operation by setting certain flags on the retrieved bulk pipe.

For reading from the device, set the [**UsbBulkInPipe.ReadOptions**](/uwp/api/Windows.Devices.Usb.UsbBulkInPipe#Windows_Devices_Usb_UsbBulkInPipe_ReadOptions) property to one of values defined in [**UsbReadOptions**](/uwp/api/Windows.Devices.Usb.UsbReadOptions). In the case of writing, set the [**UsbBulkOutPipe.WriteOptions**](/uwp/api/Windows.Devices.Usb.UsbBulkOutPipe#Windows_Devices_Usb_UsbBulkOutPipe_WriteOptions) property to one of values defined in **UsbWriteOptions**.

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
<p>For more information, see <a href="#clearing-stall-conditions">Clearing stall conditions</a>. This flag applies to both read and write transfers.</p></td>
</tr>
<tr class="even">
<td><p>Send multiple read requests with maximum efficiency. Boost performance by bypassing error checking.</p></td>
<td><strong>OverrideAutomaticBufferManagement</strong>
<p>A data request can be divided into one or more transfers, where each transfer contains a certain number of bytes called the <em>maximum transfer size</em>. For multiple transfers, there might be delay in queuing two transfers due to error checking performed by the driver. This flag bypasses that error checking. To get the maximum transfer size, use the <a href="/uwp/api/Windows.Devices.Usb.UsbBulkInPipe#Windows_Devices_Usb_UsbBulkInPipe_MaxTransferSizeBytes" data-raw-source="[&lt;strong&gt;UsbBulkInPipe.MaxTransferSizeBytes&lt;/strong&gt;](/uwp/api/Windows.Devices.Usb.UsbBulkInPipe#Windows_Devices_Usb_UsbBulkInPipe_MaxTransferSizeBytes)"><strong>UsbBulkInPipe.MaxTransferSizeBytes</strong></a> property. If your request size is <strong>UsbBulkInPipe.MaxTransferSizeBytes</strong>, you must set this flag. Note:</p>
<p></p>
<div class="alert">
<strong>Important</strong><br/><p>If you set this flag, then you must request data in multiples of the pipe's maximum packet size. That information is stored in the endpoint descriptor. The size depends on the bus speed of the device. For full speed, high speed, and SuperSpeed; the maximum packet sizes are 64, 512, and 1024 bytes respectively. To obtain that value, use the <a href="/uwp/api/Windows.Devices.Usb.UsbBulkInEndpointDescriptor#Windows_Devices_Usb_UsbBulkInEndpointDescriptor_MaxPacketSize" data-raw-source="[&lt;strong&gt;UsbBulkInPipe.EndpointDescriptor.MaxPacketSize&lt;/strong&gt;](/uwp/api/Windows.Devices.Usb.UsbBulkInEndpointDescriptor#Windows_Devices_Usb_UsbBulkInEndpointDescriptor_MaxPacketSize)"><strong>UsbBulkInPipe.EndpointDescriptor.MaxPacketSize</strong></a> property.</p>
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

1. Obtain a reference to the input stream by getting the [**UsbBulkInPipe.InputStream**](/uwp/api/Windows.Devices.Usb.UsbBulkInPipe#Windows_Devices_Usb_UsbBulkInPipe_InputStream) property.
2. Create a [**DataReader**](/uwp/api/Windows.Storage.Streams.DataReader) object by specifying the input stream in the [**DataReader constructor**](/uwp/api/Windows.Storage.Streams.DataReader#Windows_Storage_Streams_DataReader__ctor_Windows_Storage_Streams_IInputStream_).

To write data to the device, the app must write to an output stream on the bulk pipe. Here are the steps for preparing the output stream:

1. Obtain a reference to the output stream by getting the [**UsbBulkOutPipe.OutputStream**](/uwp/api/Windows.Devices.Usb.UsbBulkOutPipe#Windows_Devices_Usb_UsbBulkOutPipe_OutputStream) property.
2. Create a [**DataWriter**](/uwp/api/Windows.Storage.Streams.DataWriter) object by specifying the output stream in the [**DataWriter**](/uwp/api/Windows.Storage.Streams.DataWriter#Windows_Storage_Streams_DataWriter__ctor_Windows_Storage_Streams_IOutputStream_) constructor.
3. Populate the data buffer associated with the output stream.
4. Depending on the datatype, write transfer data to the output stream by calling [**DataWriter methods**](/uwp/api/Windows.Storage.Streams.DataWriter#Windows_Storage_Streams_DataWriter__ctor_Windows_Storage_Streams_IOutputStream_), such as [**WriteBytes**](/uwp/api/Windows.Storage.Streams.DataWriter#Windows_Storage_Streams_DataWriter_WriteBytes_System_Byte___).

## Step 4: Start an asynchronous transfer operation

Bulk transfers are initiated through asynchronous operations.

To read bulk data, start an asynchronous read operation by calling [**DataReader.LoadAsync**](/uwp/api/Windows.Storage.Streams.DataReader#Windows_Storage_Streams_DataReader_LoadAsync_System_UInt32_).

To write bulk data, start an asynchronous write operation by calling [**DataWriter.StoreAsync**](/uwp/api/Windows.Storage.Streams.DataWriter#Windows_Storage_Streams_DataWriter_StoreAsync).

## Step 5: Get results of the read transfer operation

After the asynchronous data operation is complete, you can get the number of bytes read or written from the task object. For a read operation, call [**DataReader methods**](/uwp/api/Windows.Storage.Streams.DataReader), such as [**ReadBytes**](/uwp/api/Windows.Storage.Streams.DataReader#Windows_Storage_Streams_DataReader_ReadBytes_System_Byte___), to read data from the input stream.

## Clearing stall conditions

At times, the app might experience failed data transfers. A failed transfer can be due to a stall condition on the endpoint. As long as the endpoint is stalled, data cannot be written to or read from it. In order to proceed with data transfers, the app must clear the stall condition on the associated pipe.

Your app can configure the pipe to automatically clear stall conditions, when they occur. To do so, set the [**UsbBulkInPipe.ReadOptions**](/uwp/api/Windows.Devices.Usb.UsbBulkInPipe#Windows_Devices_Usb_UsbBulkInPipe_ReadOptions) property to **UsbReadOptions.AutoClearStall** or [**UsbBulkOutPipe.WriteOptions**](/uwp/api/Windows.Devices.Usb.UsbBulkOutPipe#Windows_Devices_Usb_UsbBulkOutPipe_WriteOptions) property to **UsbWriteOptions.AutoClearStall**. With that automatic configuration, the app does not experience failed transfers and the data transfer experience is seamless.

To clear a stall condition manually, call [**UsbBulkInPipe.ClearStallAsync**](/uwp/api/Windows.Devices.Usb.UsbInterruptInPipe#Windows_Devices_Usb_UsbInterruptInPipe_ClearStallAsync) for a bulk IN pipe; call [**UsbBulkOutPipe.ClearStallAsync**](/uwp/api/Windows.Devices.Usb.UsbBulkOutPipe#Windows_Devices_Usb_UsbBulkOutPipe_ClearStallAsync) for a bulk OUT pipe.

**Note**  A stall condition does not indicate an empty endpoint. If there is no data in the endpoint, the transfer completes but length is zero bytes.

For read operations, you might need to clear pending data in the pipe before starting a new transfer request. To do so, call [**UsbBulkInPipe.FlushBuffer**](/previous-versions/windows/hardware/network/ff551975(v=vs.85)) method.

## USB bulk transfer code example

This code example shows how to write to a bulk pipe. The example sends data to the first bulk OUT pipe on the default interface. It configures the pipe to send a zero-length packet at the end of the transfer. When the transfer is complete, number of bytes are shown.

```csharp
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

```csharp
    private async void BulkRead()
    {
        UInt32 bytesRead = 0;

        UsbBulkInPipe readPipe = usbDevice.DefaultInterface.BulkInPipes[0];

        // Warning: Setting IgnoreShortPacket causes LoadAsync to block until you receive a number of packets >= readPipe.EndpointDescriptor.MaxPacketSize.
        // Remove the following line if you want to see messages that are less than the max transfer size, for example if you are communicating with a USBTMC device. 
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

            using (var dataReader = Windows.Storage.Streams.DataReader.FromBuffer(buffer))
            {
                dataReader.UnicodeEncoding = Windows.Storage.Streams.UnicodeEncoding.Utf8;
                ShowData(dataReader.ReadString(buffer.Length));
            }
        }
    }
```
