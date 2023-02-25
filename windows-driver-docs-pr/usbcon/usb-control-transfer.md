---
title: How to send a USB control transfer
description: This article explains the structure of a control transfer and how a client driver should send a control request to the device.
ms.date: 02/24/2023
---

# How to send a USB control transfer

This article explains the structure of a control transfer and how a client driver should send a control request to the device.

## About the default endpoint

All USB devices must support at least one endpoint called the *default endpoint*. Any transfer that targets the default endpoint is called a *control transfer*. The purpose of a control transfer is to enable the host to obtain device information, configure the device, or perform control operations that are unique to the device.

Let's begin by studying these characteristics of the default endpoint.

- The address of the default endpoint is 0.
- The default endpoint is bidirectional, that is, the host can send data to the endpoint and receive data from it within one transfer.
- The default endpoint is available at the device level and is not defined in any interface of the device.
- The default endpoint is active as soon as a connection is established between the host and the device. It is active even before a configuration is selected.
- The maximum packet size of the default endpoint depends on the bus speed of the device. Low speed, 8 bytes; full and high speed, 64 bytes; SuperSpeed, 512 bytes.

## Layout of a control transfer

Because control transfers are high priority transfers, certain amount of bandwidth is reserved on the bus by the host. For low and full speed devices, 10% of the bandwidth; 20% for high and SuperSpeed transfers devices. Now, let's look at the layout of a control transfer.

:::image type="content" source="images/control-transfer.png" alt-text="Diagram of a USB control transfer.":::

A control transfer is divided into three transactions: *setup transaction*, *data transaction*, and *status transaction*. Each transaction contains three types of packets: *token packet*, *data packet*, and *handshake packet*.

Certain fields are common to all packets. These fields are:

- Sync field that indicates the start of packet.
- Packet identifier (PID) that indicates the type of packet, the direction of the transaction, and in the case of a handshake packet, it indicates success or failure of the transaction.
- EOP field indicates the end of packet.

Other fields depend on the type of packet.

### Token packet

Every setup transaction starts with a token packet. Here is the structure of the packet. The host always sends the token packet.

:::image type="content" source="images/token.png" alt-text="Diagram of a token packet layout.":::

The PID value indicates the type of the token packet. Here are the possible values:

- SETUP: Indicates the start of a setup transaction in a control transfer.
- IN: Indicates that the host is requesting data from the device (read case).
- OUT: Indicates that the host is sending data to the device (write case).
- SOF: Indicates the start of frame. This type of token packet contains an 11-bit frame number. The host sends the SOF packet. The frequency at which this packet is sent depends on the bus speed. For full speed, the host sends the packet every 1millisecond; every 125 microsecond on a high-speed bus.

### Data packet

Immediately following the token packet is the data packet that contains the payload. The number of bytes that each data packet can contain depends on the maximum packet size of the default endpoint. The data packet can be sent by either the host or the device, depending on the direction of the transfer.

:::image type="content" source="images/data.png" alt-text="Diagram of a data packet layout.":::

### Handshake packet

Immediately following the data packet is the handshake packet. The PID of the packet indicates whether or not the packet was received by the host or the device. The handshake packet can be sent by either the host or the device, depending on the direction of the transfer.

:::image type="content" source="images/handshake.png" alt-text="Diagram of a handshake packet layout.":::

You can see the structure of transactions and packets by using any USB analyzer, such as Beagle, Ellisys, LeCroy USB protocol analyzers. An analyzer device shows how data is sent to or received from a USB device over the wire. In this example, let's examine some traces captured by a LeCroy USB analyzer. This example is for information only. This is not an endorsement by Microsoft.

### Setup transaction

The host always initiates a control transfer. It does so by sending a setup transaction. This transaction contains a token packet called *setup token* followed by an 8-byte data packet. This screen shot shows an example setup transaction.

:::image type="content" source="images/setup-trans.png" alt-text="Screenshot of a trace of a setup transaction.":::

In the preceding trace, the host initiates (indicated by **H↓**) the control transfer by sending the setup token packet \#434. Notice that the PID specifies SETUP indicating a setup token. The PID is followed by the device address and the address of the endpoint. For control transfers, that endpoint address is always 0.

Next, the host sends the data packet \#435. The PID is DATA0 and that value is used for packet sequencing (to be discussed). The PID is followed by 8 bytes that contains the main information about this request. Those 8 bytes indicate the type of request and the size of the buffer in which the device will write its response.

All bytes are received in reverse order. As described in section 9.3, we see these fields and values:

|Field|Size|Value|Description|
|---- |--- |---- |---------- |
|**bmRequestType** (See 9.3.1 bmRequestType)|1|0x80|The data transfer direction is from device to host (D7 is 1)<br><br>The request is a standard request (D6…D5 is 0)<br><br>The recipient of the request is the DEVICE (D4 is 0)|
|**bRequest** (See section See 9.3.2 and Table 9-4)|1|0x06|The request type is GET_DESCRIPTOR.|
|**wValue** (See Table 9-5)|2|0x0100|The request value indicates that the descriptor type is DEVICE.|
|**wIndex** (See section 9.3.4)|2|0x0000|The direction is from the host to device (D7 is 1)<br><br>The endpoint number is 0.|
|**wLength** (See section 9.3.5)|2|0x0012|The request is to retrieve 18 bytes.|

Thus, we can conclude that in this control (read) transfer, the host sends a request to retrieve the device descriptor and specifies 18 bytes as the transfer length to hold that descriptor. The way the device sends those 18 bytes depends on how much data the default endpoint can send in one transaction. That information is included in the device descriptor returned by the device in the data transaction.

In response, the device sends a handshake packet (\#436 indicated by **D↓**). Notice that the PID value is ACK (ACK packet). This indicates that the device acknowledged the transaction.

### Data transaction

Now, let's see what the device returns in response to the request. The actual data is transferred in a data transaction.

Here is the trace for the data transaction.

:::image type="content" source="images/datra-trans.png" alt-text="Screenshot that shows a trace of an example data transaction.":::

Upon receiving the ACK packet, the host initiates the data transaction. To initiate the transaction, it sends a token packet (\#450) with direction as IN (called IN token).

In response, the device sends a data packet (\#451) that follows the IN token. This data packet contains the actual device descriptor. The first byte indicates the length of the device descriptor, 18 bytes (0x12). The last byte in this data packet indicates the maximum packet size supported by the default endpoint. In this case, we see that the device can send 8 bytes at a time through its default endpoint.

 > [!NOTE]
> The maximum packet size of the default endpoint depends on the speed of the device. The default endpoint of a high-speed device is 64 bytes; low-speed device is 8 bytes.

The host acknowledges the data transaction by sending an ACK packet (\#452) to the device.

Let's calculate the amount of data returned. In the **wLength** field of the data packet (\#435) in the setup transaction, the host requested 18 bytes. In the data transaction, we see that only first 8 bytes of the device descriptor were received from the device. So, how does the host receive information stored in the remaining 10 bytes? The device does so in two transactions: 8 bytes and then last 2 bytes.

Now that the host knows the maximum packet size of the default endpoint, the host initiates a new data transaction and requests the next portion based on the packet size.

Here is the next data transaction:

:::image type="content" source="images/datra-trans2.png" alt-text="Screenshot that shows a trace of the new data transaction.":::

The host initiates the preceding data transaction by sending an IN token (\#463) and requesting the next 8 bytes from the device. The device responds with a data packet (\#464) that contains the next 8 bytes of the device descriptor.

Upon receiving the 8 bytes, the host sends an ACK packet (\#465) to the device.

Next, the host requests the last 2 bytes in another data transaction as follows:

:::image type="content" source="images/datra-trans3.png" alt-text="Screenshot that shows a trace of the new example data transaction in which the host requests the last 2 bytes.":::

Therefore, we see that to transfer 18 bytes from the device to the host, the host keeps track of the number of bytes transferred and initiated three data transactions (8+8+2).

> [!NOTE]
> Notice the PID of the data packets in data transactions 19, 23, 26. The PID alternates between DATA0 and DATA1. This sequence is called data toggling. In cases where there are multiple data transactions, data toggling is used to verify the packet sequence. This method makes sure that the data packets are not duplicated or lost.

By mapping the consolidated data packets to the structure of the device descriptor (See Table 9-8), we see these fields and values:

| Field | Size | Value | Description |
|---|---|---|---|
| **bLength** | 1 | 0x12 | Length of the device descriptor, which is 18 bytes. |
| **bDescriptorType** | 1 | 0x01 | The descriptor type is device. |
| **bcdUSB** | 2 | 0x0100 | The specification version number is 1.00. |
| **bDeviceClass** | 1 | 0x00 | Device class is 0. Each interface in the configuration has the class information. |
| **bDeviceSubClass** | 1 | 0x00 | Subclass is 0 because device class is 0. |
| **bProtocol** | 1 | 0x00 | Protocol is 0. This device does not use any class-specific protocols. |
| **bMaxPacketSize0** | 1 | 0x08 | The maximum packet size of the endpoint is 8 bytes. |
| **idVendor** | 2 | 0x0562 | Telex Communications. |
| **idProduct** | 2 | 0x0002 | USB microphone. |
| **bcdDevice** | 2 | 0x0100 | Indicates the device release number. |
| **iManufacturer** | 1 | 0x01 | Manufacturer string. |
| **iProduct** | 1 | 0x02 | Product string. |
| **iSerialNumber** | 1 | 0x03 | Serial number. |
| **bNumConfigurations** | 1 | 0x01 | Number of configurations. |

By examining those values we have some preliminary information about the device. The device is a low-speed USB microphone. The maximum packet size of the default endpoint is 8 bytes. The device supports one configuration.

### Status transaction

Finally, the host completes the control transfer by initiating the last transaction: status transaction.

:::image type="content" source="images/status-trans.png" alt-text="Screenshot of a trace of an example data transaction.":::

The host starts the transaction with an OUT token packet (\#481). The purpose of this packet is to verify that the device sent all of the requested data. There is no data packet sent in this status transaction. The device responds with an ACK packet. If an error occurred, the PID could have been either NAK or STALL.

## Driver models

- [Kernel-Mode Driver Framework](../wdf/index.md)
- [User- Mode Driver Framework](../wdf/index.md)
- [WinUSB](winusb.md)

## Prerequisites

Before the client driver can enumerate pipes, make sure that these requirements are met:

- The client driver must have created the framework USB target device object.

  If you are using the USB templates that are provided with Microsoft Visual Studio Professional 2012, the template code performs those tasks. The template code obtains the handle to the target device object and stores in the device context.

### KMDF client driver

A KMDF client driver must obtain a WDFUSBDEVICE handle by calling the [WdfUsbTargetDeviceCreateWithParameters](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters) method. For more information, see "Device source code" in [Understanding the USB client driver code structure (KMDF)](understanding-the-kmdf-template-code-for-usb.md).

### UMDF client driver

A UMDF client driver must obtain an [IWDFUsbTargetDevice](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbtargetdevice) pointer by querying the framework target device object. For more information, see "[IPnpCallbackHardware](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallbackhardware) implementation and USB-specific tasks" in [Understanding the USB client driver code structure (UMDF)](understanding-the-umdf-template-code-for-usb.md).

The most important aspect for a control transfer is to format the setup token appropriately. Before sending the request, gather this set of information:

- Direction of the request: host to device or device to host.
- Recipient of the request: device, interface, endpoint, or other.
- Category of request: standard, class, or vendor.
- Type of request, such as a GET_DESCRIPTPOR request. For more information, see section 9.5 in the USB specification.
- **wValue** and **wIndex** values. Those values depend on the type of request.

You can obtain all that information from the official USB specification.

If you are writing a UMDF driver, get the header file, Usb_hw.h from the UMDF Sample Driver for OSR USB Fx2 Learning Kit. This header file contains useful macros and structure for formatting the setup packet for the control transfer.

All UMDF drivers must communicate with a kernel-mode driver in order to send and receive data from devices. For a USB UMDF driver, the kernel-mode driver is always the Microsoft-provided driver [WinUSB](winusb.md) (Winusb.sys).

Whenever a UMDF driver makes a request for the USB driver stack, the Windows I/O manager sends the request to WinUSB. After receiving the request, WinUSB either processes the request or forwards it to the USB driver stack.

## Microsoft-defined methods for sending control transfer requests

A USB client driver on the host initiates most control requests to get information about the device, configure the device, or send vendor control commands. All of those requests can be categorized into:

- **Standard requests** are defined in the USB specification. The purpose of sending standard requests is to obtain information about the device, its configurations, interfaces, and endpoints. The recipient of each request depends on the type of request. The recipient can be the device, an interface, or an endpoint.

  > [!NOTE]
  > The target of any control transfer is always the default endpoint. The recipient is the device's entity whose information (descriptor, status, and so on) the host is interested in.

  Requests can be further classified into: configuration requests, feature requests, and status requests.

  - **Configuration requests** are sent to get information from the device so that the host can configure it, such as a GET_DESCRIPTOR request. These requests can also be write requests that are sent by the host to set a particular configuration or alternate setting in the device.
  - **Feature requests** are sent by the client driver to enable or disable certain Boolean device settings supported by the device, interface, or an endpoint.
  - **Status requests** enable the host get or set the USB-defined status bits of a device, endpoint, or interface.

  For more information, see Section 9.4 in USB specification, version 2.0. The standard request types are defined the header file, Usbspec.h.

- **Class requests** are defined by a specific device class specification.

- **Vendor requests** are provided by the vendor and depend on the requests supported by the device.

The Microsoft-provided USB stack handles all the protocol communication with the device as shown in the preceding traces. The driver exposes device driver interfaces (DDIs) that enable a client driver to send control transfers in many ways. If your client driver is a Windows Driver Foundation (WDF) driver, it can call routines directly to send the common types of control requests. WDF supports control transfers intrinsically for both KMDF and UMDF.

Certain types of control requests are not exposed through WDF. For those requests, the client driver can use the WDF-hybrid model. This model allows the client driver to build and format WDM URB-style requests and then send those requests by using WDF framework objects. The hybrid model only applies to kernel-mode drivers.

**For UMDF drivers:**

Use the helper macros and structure defined in usb_hw.h. This header is included with the UMDF Sample Driver for OSR USB Fx2 Learning Kit.

Use this table to determine the best way to send control requests to the USB driver stack. If you are unable to view this table, see the table in [this article](/windows-hardware/drivers/ddi/index).

| If you want to send a control request to... | For a KMDF driver... | For a UMDF driver... | For a WDM driver, build a URB structure (Helper routine) |
|---|---|---|---|
| CLEAR_FEATURE: Disable certain feature settings in device, its configurations, interfaces and endpoints. See section 9.4.1 in the USB specification. | <ol><li>Declare a setup packet. See the **[WDF_USB_CONTROL_SETUP_PACKET](/windows-hardware/drivers/ddi/wdfusb/ns-wdfusb-_wdf_usb_control_setup_packet)** structure.</li><li>Initialize the setup packet by calling **[WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdf_usb_control_setup_packet_init_feature)**.</li><li>Specify a recipient value defined in **[WDF_USB_BMREQUEST_RECIPIENT](/windows-hardware/drivers/ddi/wdfusb/ne-wdfusb-_wdf_usb_bmrequest_recipient)**.</li><li>Specify the feature selector (**wValue**). See USB_FEATURE_XXX constants in Usbspec.h. Also see Table 9-6 in the USB specification.</li><li>Set *SetFeature* to **FALSE**.</li><li>Send the request by calling **[WdfUsbTargetDeviceSendControlTransferSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendcontroltransfersynchronously)** or **[WdfUsbTargetDeviceFormatRequestForControlTransfer](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforcontroltransfer)**.</li></ol> | <ol><li>Declare a setup packet. See the **WINUSB_CONTROL_SETUP_PACKET** structure declared in usb_hw.h.</li><li>Initialize the setup packet by calling the helper macro, **WINUSB_CONTROL_SETUP_PACKET_INIT_FEATURE**, defined in usb_hw.h.</li><li>Specify a recipient value defined in **WINUSB_BMREQUEST_RECIPIENT**.</li><li>Specify the feature selector (**wValue**). See **USB_FEATURE_XXX** constants in Usbspec.h. Also see Table 9-6 in the USB specification.</li><li>Set *SetFeature* to **FALSE**.</li><li>Build the request by associating the initialized setup packet with the framework request object and the transfer buffer by calling **[IWDFUsbTargetDevice::FormatRequestForControlTransfer](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-formatrequestforcontroltransfer)** method.</li><li>Send the request by calling the **[IWDFIoRequest::Send](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-send)** method.</li></ol> | **[_URB_CONTROL_FEATURE_REQUEST](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_control_feature_request)**<br><br>(**[UsbBuildFeatureRequest](/previous-versions/ff538932(v=vs.85))**)<br><br>URB_FUNCTION_CLEAR_FEATURE_TO_DEVICE<br><br>URB_FUNCTION_CLEAR_FEATURE_TO_INTERFACE<br><br>URB_FUNCTION_CLEAR_FEATURE_TO_ENDPOINT<br><br>URB_FUNCTION_CLEAR_FEATURE_TO_OTHER |
| GET_CONFIGURATION: Get the current USB configuration. See section 9.4.2 in the USB specification. | KMDF selects the first configuration by default. To retrieve the device-defined configuration number:<br><br><ol><li>Format a **[WDF_USB_CONTROL_SETUP_PACKET](/windows-hardware/drivers/ddi/wdfusb/ns-wdfusb-_wdf_usb_control_setup_packet)** and set its **bRequest** member to **USB_REQUEST_GET_CONFIGURATION**.</li><li>Send the request by calling **[WdfUsbTargetDeviceSendControlTransferSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendcontroltransfersynchronously)** or **[WdfUsbTargetDeviceFormatRequestForControlTransfer](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforcontroltransfer)**.</li></ol> | UMDF selects the first configuration by default. To retrieve the device-defined configuration number:<br><br><ol><li>Declare a setup packet. See the **WINUSB_CONTROL_SETUP_PACKET** structure declared in usb_hw.h.</li><li>Initialize the setup packet by calling the helper macro, **WINUSB_CONTROL_SETUP_PACKET_INIT**, defined in usb_hw.h.</li><li>Specify **BmRequestToDevice** as the direction, **BmRequestToDevice** as the recipient, and **USB_REQUEST_GET_CONFIGURATION** as the request.</li><li>Build the request by associating the initialized setup packet with the framework request object and the transfer buffer by calling **[IWDFUsbTargetDevice::FormatRequestForControlTransfer](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-formatrequestforcontroltransfer)** method.</li><li>Send the request by calling the **[IWDFIoRequest::Send](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-send)** method.</li><li>Receive the configuration number in the transfer buffer. Access that buffer by calling **[IWDFMemory](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfmemory)** methods.</li></ol> | **[_URB_CONTROL_GET_CONFIGURATION_REQUEST](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_control_get_configuration_request)**<br><br>URB_FUNCTION_GET_CONFIGURATION |
| GET_DESCRIPTOR: Get device, configuration, interface, and endpoint descriptors. See section 9.4.3 in the USB specification.<br><br>For more information, see [USB Descriptors](usb-descriptors.md). | Call these methods:<br><br><ul><li>**[WdfUsbTargetDeviceGetDeviceDescriptor](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicegetdevicedescriptor)**</li><li>**[WdfUsbInterfaceGetDescriptor](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfacegetdescriptor)**</li><li>**[WdfUsbInterfaceGetEndpointInformation](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfacegetendpointinformation)** or **[WdfUsbTargetPipeGetInformation](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipegetinformation)**. This method returns endpoint descriptor fields in a **[WDF_USB_PIPE_INFORMATION](/windows-hardware/drivers/ddi/wdfusb/ns-wdfusb-_wdf_usb_pipe_information)** structure.</li></ul> | Call these methods:<br><br><ul><li>**[IWDFUsbTargetDevice::RetrieveDescriptor](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-retrievedescriptor)**</li><li>**[IWDFUsbInterface::GetInterfaceDescriptor](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbinterface-getinterfacedescriptor)**</li><li>**[IWDFUsbTargetPipe::GetInformation](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetpipe-getinformation)**. This method returns endpoint descriptor fields in a **[WINUSB_PIPE_INFORMATION](/windows/win32/api/winusbio/ns-winusbio-_winusb_pipe_information)** structure.</li></ul> | **[_URB_CONTROL_DESCRIPTOR_REQUEST](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_control_descriptor_request)**<br><br>(**[UsbBuildGetDescriptorRequest](/previous-versions/ff538943(v=vs.85))**)<br><br>URB_FUNCTION_GET_DESCRIPTOR_FROM_DEVICE<br><br>URB_FUNCTION_GET_DESCRIPTOR_FROM_ENDPOINT<br><br>URB_FUNCTION_GET_DESCRIPTOR_FROM_INTERFACE |
| GET_INTERFACE: Get the current alternate setting for an interface. See section 9.4.4 in the USB specification. | <br><br><ol><li>Get a WDFUSBINTERFACE handle to the target interface object by calling the **[WdfUsbTargetDeviceGetInterface](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicegetinterface)** method.</li><li>Call the **[WdfUsbInterfaceGetConfiguredSettingIndex](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfacegetconfiguredsettingindex)** method.</li></ol> | <ol><li>Get a **[IWDFUsbInterface](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbinterface)** pointer to the target interface object.</li><li>Call the **[IWDFUsbInterface::GetConfiguredSettingIndex](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbinterface-getconfiguredsettingindex)** method.</li></ol> | **[_URB_CONTROL_GET_INTERFACE_REQUEST](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_control_get_interface_request)**<br><br>URB_FUNCTION_GET_INTERFACE |
| GET_STATUS: Get status bits from a device, endpoint, or interface. See section 9.4.5. in the USB specification. | <ol><li>Declare a setup packet. See the **[WDF_USB_CONTROL_SETUP_PACKET](/windows-hardware/drivers/ddi/wdfusb/ns-wdfusb-_wdf_usb_control_setup_packet)** structure.</li><li>Initialize the setup packet by calling **[WDF_USB_CONTROL_SETUP_PACKET_INIT_GET_STATUS](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdf_usb_control_setup_packet_init_get_status)**.</li><li>Specify the recipient value defined in **[WDF_USB_BMREQUEST_RECIPIENT](/windows-hardware/drivers/ddi/wdfusb/ne-wdfusb-_wdf_usb_bmrequest_recipient)**.</li><li>Specify which status you want to get: device, interface, or endpoint (**wIndex**).</li><li>Send the request by calling **[WdfUsbTargetDeviceSendControlTransferSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendcontroltransfersynchronously)** or **[WdfUsbTargetDeviceFormatRequestForControlTransfer](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforcontroltransfer)**.</li></ol> | <ol><li>Declare a setup packet. See the **WINUSB_CONTROL_SETUP_PACKET** structure declared in usb_hw.h.</li><li>Initialize the setup packet by calling the helper macro, **WINUSB_CONTROL_SETUP_PACKET_INIT_GET_STATUS**, defined in usb_hw.h.</li><li>Specify a recipient value defined in **WINUSB_BMREQUEST_RECIPIENT**.</li><li>Specify which status you want to get: device, interface, or endpoint (**wIndex**).</li><li>Build the request by associating the initialized setup packet with the framework request object and the transfer buffer by calling **[IWDFUsbTargetDevice::FormatRequestForControlTransfer](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-formatrequestforcontroltransfer)** method.</li><li>Send the request by calling the **[IWDFIoRequest::Send](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-send)** method.</li><li>Receive the status value in the transfer buffer. Access that buffer by calling **[IWDFMemory](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfmemory)** methods.</li><li>To determine if the status indicates self-powered, remote wake-up, use thee values defined in the **WINUSB_DEVICE_TRAITS** enumeration:</li></ol> | **[_URB_CONTROL_GET_STATUS_REQUEST](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_control_get_status_request)**<br><br>(**[UsbBuildGetStatusRequest](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbbuildgetstatusrequest)**)<br><br>URB_FUNCTION_GET_STATUS_FROM_DEVICE<br><br>URB_FUNCTION_GET_STATUS_FROM_INTERFACE<br><br>URB_FUNCTION_GET_STATUS_FROM_ENDPOINT<br><br>URB_FUNCTION_GET_STATUS_FROM_OTHER. |
| SET_ADDRESS: See section 9.4.6 in USB specification. | This request is handled by the USB driver stack; the client driver cannot perform this operation. | This request is handled by the USB driver stack; the client driver cannot perform this operation. | This request is handled by the USB driver stack; the client driver cannot perform this operation. |
| SET_CONFIGURATION: Set a configuration. See section 9.4.7 in USB specification.<br><br>For more information, see [How to select a configuration for a USB device](how-to-select-a-configuration-for-a-usb-device.md). | By default KMDF selects the default configuration and first alternate setting in each interface. The client driver can change the default configuration by calling **[WdfUsbTargetDeviceSelectConfigType](/windows-hardware/drivers/ddi/wdfusb/ne-wdfusb-_wdfusbtargetdeviceselectconfigtype)** method and specifying **WdfUsbTargetDeviceSelectConfigTypeUrb** as the request option. You must then format an URB for this request and submit it to the USB driver stack. | By default UMDF selects the default configuration and first alternate setting in each interface. The client driver cannot change the configuration. | **[_URB_SELECT_CONFIGURATION](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_select_configuration)**<br><br>(**[USBD_SelectConfigUrbAllocateAndBuild](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_selectconfigurballocateandbuild)**)<br><br>URB_FUNCTION_SELECT_CONFIGURATION |
| SET_DESCRIPTOR: Update an existing device, configuration, or string descriptor. See section 9.4.8 in USB specification.<br><br>This request is not commonly used. However, the USB driver stack accepts such a request from the client driver. | <ol><li>Allocate and build an **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** for the request.</li><li>Specify the transfer information in a **[_URB_CONTROL_DESCRIPTOR_REQUEST](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_control_descriptor_request)** structure.</li><li>Send the request by calling **[WdfUsbTargetDeviceFormatRequestForUrb](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforurb)** or **[WdfUsbTargetDeviceSendUrbSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendurbsynchronously)** .</li></ol> | <ol><li>Declare a setup packet. See the **WINUSB_CONTROL_SETUP_PACKET** structure declared in usb_hw.h.</li><li>Specify the transfer information as per the USB specification.</li><li>Build the request by associating the initialized setup packet with the framework request object and the transfer buffer by calling **[IWDFUsbTargetDevice::FormatRequestForControlTransfer](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-formatrequestforcontroltransfer)** method.</li><li>Send the request by calling the **[IWDFIoRequest::Send](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-send)** method.</li></ol> | **[_URB_CONTROL_DESCRIPTOR_REQUEST](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_control_descriptor_request)**<br><br>URB_FUNCTION_SET_DESCRIPTOR_TO_DEVICE<br><br>URB_FUNCTION_SET_DESCRIPTOR_TO_ENDPOINT<br><br>URB_FUNCTION_SET_DESCRIPTOR_TO_INTERFACE |
| SET_FEATURE: Enable certain feature settings in device, its configurations, interfaces and endpoints. See section 9.4.9 in the USB specification. | <ol><li>Declare a setup packet. See the **[WDF_USB_CONTROL_SETUP_PACKET](/windows-hardware/drivers/ddi/wdfusb/ns-wdfusb-_wdf_usb_control_setup_packet)** structure.</li><li>Initialize the setup packet by calling **[WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdf_usb_control_setup_packet_init_feature)**.</li><li>Specify the recipient value (device, interface, endpoint) defined in **[WDF_USB_BMREQUEST_RECIPIENT](/windows-hardware/drivers/ddi/wdfusb/ne-wdfusb-_wdf_usb_bmrequest_recipient)**.</li><li>Specify the feature selector (**wValue**). See USB_FEATURE_XXX constants in Usbspec.h. Also see Table 9-6 in the USB specification.</li><li>Set *SetFeature* to **TRUE**</li><li>Send the request by calling **[WdfUsbTargetDeviceSendControlTransferSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendcontroltransfersynchronously)** or **[WdfUsbTargetDeviceFormatRequestForControlTransfer](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforcontroltransfer)**.</li></ol> | <ol><li>Declare a setup packet. See the **WINUSB_CONTROL_SETUP_PACKET** structure declared in usb_hw.h.</li><li>Initialize the setup packet by calling the helper macro, **WINUSB_CONTROL_SETUP_PACKET_INIT_FEATURE**, defined in usb_hw.h.</li><li>Specify a recipient value defined in **WINUSB_BMREQUEST_RECIPIENT**.</li><li>Specify the feature selector (**wValue**). See **USB_FEATURE_XXX** constants in Usbspec.h. Also see Table 9-6 in the USB specification.</li><li>Set *SetFeature* to **TRUE**.</li><li>Build the request by associating the initialized setup packet with the framework request object and the transfer buffer by calling **[IWDFUsbTargetDevice::FormatRequestForControlTransfer](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-formatrequestforcontroltransfer)** method.</li><li>Send the request by calling the **[IWDFIoRequest::Send](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-send)** method.</li></ol> | **[_URB_CONTROL_FEATURE_REQUEST](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_control_feature_request)**<br><br>(**[UsbBuildFeatureRequest](/previous-versions/ff538932(v=vs.85))**)<br><br>URB_FUNCTION_SET_FEATURE_TO_DEVICE<br><br>URB_FUNCTION_SET_FEATURE_TO_INTERFACE<br><br>URB_FUNCTION_SET_FEATURE_TO_ENDPOINT<br><br>URB_FUNCTION_SET_FEATURE_TO_OTHER |
| SET_INTERFACE: Changes the alternate setting in an interface. See section 9.4.9 in the USB specification.<br><br>For more information, see [How to select an alternate setting in a USB interface](select-a-usb-alternate-setting.md). | **[WdfUsbTargetDeviceSelectConfig](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceselectconfig)**<ol><li>Get a WDFUSBINTERFACE handle to the target interface object.</li><li>Call the **[WdfUsbInterfaceSelectSetting](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfaceselectsetting)** method.</li></ol> | <ol><li>Get a **[IWDFUsbInterface](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbinterface)** pointer to the target interface object.</li><li>Call the **[IWDFUsbInterface::SelectSetting](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbinterface-selectsetting)** method.</li></ol> | **[_URB_SELECT_INTERFACE](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_select_interface)**<br><br>(**[USBD_SelectInterfaceUrbAllocateAndBuild](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_selectinterfaceurballocateandbuild)**)<br><br>URB_FUNCTION_SELECT_INTERFACE |
| SYNC_FRAME: Set and get and endpoint's synchronization frame number. See section 9.4.10 in the USB specification. | This request is handled by the USB driver stack; the client driver cannot perform this operation. | This request is handled by the USB driver stack; the client driver cannot perform this operation. | This request is handled by the USB driver stack; the client driver cannot perform this operation. |
| For device class-specific requests and vendor commands. | <ol><li>Declare a setup packet. See the **[WDF_USB_CONTROL_SETUP_PACKET](/windows-hardware/drivers/ddi/wdfusb/ns-wdfusb-_wdf_usb_control_setup_packet)** structure.</li><li>Initialize the setup packet by calling **[WDF_USB_CONTROL_SETUP_PACKET_INIT_CLASS](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdf_usb_control_setup_packet_init_class)**-specific requests or **[WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdf_usb_control_setup_packet_init_vendor)** for vendor commands.</li><li>Specify the recipient value (device, interface, endpoint) defined in **[WDF_USB_BMREQUEST_RECIPIENT](/windows-hardware/drivers/ddi/wdfusb/ne-wdfusb-_wdf_usb_bmrequest_recipient)**.</li><li>Send the request by calling **[WdfUsbTargetDeviceSendControlTransferSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendcontroltransfersynchronously)** or **[WdfUsbTargetDeviceFormatRequestForControlTransfer](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforcontroltransfer)**.</li></ol> | <ol><li>Declare a setup packet. See the **WINUSB_CONTROL_SETUP_PACKET** structure declared in usb_hw.h.</li><li>Initialize the setup packet by calling the helper macro, **WINUSB_CONTROL_SETUP_PACKET_INIT_CLASS** or **WINUSB_CONTROL_SETUP_PACKET_INIT_VENDOR**, defined in usb_hw.h.</li><li>Specify the direction (see the **WINUSB_BMREQUEST_DIRECTION** enumeration), the recipient ( see the **WINUSB_BMREQUEST_RECIPIENT** enumeration), and the request, as described in the class or the hardware specification.</li><li>Build the request by associating the initialized setup packet with the framework request object and the transfer buffer by calling **[IWDFUsbTargetDevice::FormatRequestForControlTransfer](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-formatrequestforcontroltransfer)** method.</li><li>Send the request by calling the **[IWDFIoRequest::Send](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-send)** method.</li><li>Receive the information from the device in the transfer buffer. Access that buffer by calling **[IWDFMemory](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfmemory)** methods.</li></ol> | **[_URB_CONTROL_VENDOR_OR_CLASS_REQUEST](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_control_vendor_or_class_request)**<br><br>(**[UsbBuildVendorRequest](/previous-versions/ff538986(v=vs.85))**)<br><br>URB_FUNCTION_VENDOR_DEVICE<br><br>URB_FUNCTION_VENDOR_INTERFACE<br><br>URB_FUNCTION_VENDOR_ENDPOINT<br><br>URB_FUNCTION_VENDOR_OTHER<br><br>URB_FUNCTION_CLASS_DEVICE<br><br>URB_FUNCTION_CLASS_INTERFACE<br><br>URB_FUNCTION_CLASS_ENDPOINT<br><br>URB_FUNCTION_CLASS_OTHER |

## How to send a control transfer for vendor commands - KMDF

This procedure shows how a client driver can send a control transfer. In this example, the client driver sends a vendor command that retrieves the firmware version from the device.

1. Declare a constant for the vendor command. Study the hardware specification and determine the vendor command that you want to use.
1. Declare a [WDF_MEMORY_DESCRIPTOR](/windows-hardware/drivers/ddi/wdfmemory/ns-wdfmemory-_wdf_memory_descriptor) structure and initialize it by calling the [WDF_MEMORY_DESCRIPTOR_INIT_BUFFER](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdf_memory_descriptor_init_buffer) macro. This structure will receive the response from the device after the USB driver completes the request.
1. Depending on whether you send the request synchronously or asynchronously, specify your send options:
    - If you send the request synchronously by calling [WdfUsbTargetDeviceSendControlTransferSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendcontroltransfersynchronously), specify a timeout value. That value is important because without a timeout, you can block the thread indefinitely.

        For this, declare a [WDF_REQUEST_SEND_OPTIONS](/windows-hardware/drivers/ddi/wdfrequest/ns-wdfrequest-_wdf_request_send_options) structure and initialize it by calling the [WDF_REQUEST_SEND_OPTIONS_INIT](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdf_request_send_options_init) macro. Specify the option as **WDF_REQUEST_SEND_OPTION_TIMEOUT**.

        Next, set the timeout value by calling the [WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdf_request_send_options_set_timeout) macro.

    - If you are sending the request asynchronously, implement a completion routine. Free all allocated resources in the completion routine.

1. Declare a [WDF_USB_CONTROL_SETUP_PACKET](/windows-hardware/drivers/ddi/wdfusb/ns-wdfusb-_wdf_usb_control_setup_packet) structure to contain the setup token and format the structure. To do so, call the [WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdf_usb_control_setup_packet_init_vendor) macro to format the setup packet. In the call specify, the direction of the request, the recipient, the sent-request options (initialized in step3), and the constant for the vendor command.
1. Send the request by calling [WdfUsbTargetDeviceSendControlTransferSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendcontroltransfersynchronously) or [WdfUsbTargetDeviceFormatRequestForControlTransfer](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforcontroltransfer).
1. Check the NTSTATUS value returned by the framework and inspect the received value.

This code example sends a control transfer request to a USB device to retrieve its firmware version. The request is sent synchronously and the client driver specifies a relative timeout value of 5 seconds (in 100-nanosecond units). The driver stores the received response in the driver-defined device context.

```cpp
enum {
    USBFX2_GET_FIRMWARE_VERSION = 0x1,
....

} USBFX2_VENDOR_COMMANDS; 

#define WDF_TIMEOUT_TO_SEC              ((LONGLONG) 1 * 10 * 1000 * 1000)  // defined in wdfcore.h

const __declspec(selectany) LONGLONG
            DEFAULT_CONTROL_TRANSFER_TIMEOUT = 5 * -1 * WDF_TIMEOUT_TO_SEC; 


typedef struct _DEVICE_CONTEXT
{

    ...
       union {
        USHORT      VersionAsUshort;
        struct {
            BYTE Minor;
            BYTE Major;
        } Version;
    } Firmware; // Firmware version.

} DEVICE_CONTEXT, *PDEVICE_CONTEXT;


__drv_requiresIRQL(PASSIVE_LEVEL)
VOID  GetFirmwareVersion(
    __in PDEVICE_CONTEXT DeviceContext
)
{
    NTSTATUS                        status;
    WDF_USB_CONTROL_SETUP_PACKET    controlSetupPacket;
    WDF_REQUEST_SEND_OPTIONS        sendOptions;
    USHORT                          firmwareVersion;
    WDF_MEMORY_DESCRIPTOR           memoryDescriptor;

    PAGED_CODE();

    firmwareVersion = 0;

    WDF_MEMORY_DESCRIPTOR_INIT_BUFFER(&memoryDescriptor, (PVOID) &firmwareVersion, sizeof(firmwareVersion));

    WDF_REQUEST_SEND_OPTIONS_INIT(
                                  &sendOptions,
                                  WDF_REQUEST_SEND_OPTION_TIMEOUT
                                  );

    WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT(
                                         &sendOptions,
                                         DEFAULT_CONTROL_TRANSFER_TIMEOUT
                                         );

    WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR(&controlSetupPacket,
                                        BmRequestDeviceToHost,       // Direction of the request
                                        BmRequestToDevice,           // Recipient
                                        USBFX2_GET_FIRMWARE_VERSION, // Vendor command
                                        0,                           // Value
                                        0);                          // Index 

    status = WdfUsbTargetDeviceSendControlTransferSynchronously(
                                        DeviceContext->UsbDevice,
                                        WDF_NO_HANDLE,               // Optional WDFREQUEST
                                        &sendOptions,
                                        &controlSetupPacket,
                                        &memoryDescriptor,           // MemoryDescriptor
                                        NULL);                       // BytesTransferred 

    if (!NT_SUCCESS(status)) 
    {
        KdPrint(("Device %d: Failed to get device firmware version 0x%x\n", DeviceContext->DeviceNumber, status));
        TraceEvents(DeviceContext->DebugLog,
                    TRACE_LEVEL_ERROR,
                    DBG_RUN,
                    "Device %d: Failed to get device firmware version 0x%x\n",
                    DeviceContext->DeviceNumber,
                    status);
    }
    else 
    {
        DeviceContext->Firmware.VersionAsUshort = firmwareVersion;
        TraceEvents(DeviceContext->DebugLog,
                    TRACE_LEVEL_INFORMATION,
                    DBG_RUN,
                    "Device %d: Get device firmware version : 0x%x\n",
                    DeviceContext->DeviceNumber,
                    firmwareVersion);
    }

    return;
}
```

## How to send a control transfer for GET_STATUS - UMDF

This procedure shows how a client driver can send a control transfer for a GET_STATUS command. The recipient of the request is the device and the request obtains information in bits D1-D0. For more information, see Figure 9-4 in the USB specification.

1. Include the header file Usb_hw.h available with the UMDF Sample Driver for OSR USB Fx2 Learning Kit.
1. Declare a **WINUSB_CONTROL_SETUP_PACKET** structure.
1. Initialize the setup packet by calling the helper macro, **WINUSB_CONTROL_SETUP_PACKET_INIT_GET_STATUS**.
1. Specify **BmRequestToDevice** as the recipient.
1. Specify 0 in the *Index* value.
1. Call the helper method SendControlTransferSynchronously to send the request synchronously.

    The helper method builds the request by associating the initialized setup packet with the framework request object and the transfer buffer by calling [IWDFUsbTargetDevice::FormatRequestForControlTransfer](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-formatrequestforcontroltransfer) method. The helper method then sends the request by calling the [IWDFIoRequest::Send](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-send) method. After the method returns, inspect the value returned.

1. To determine if the status indicates self-powered, remote wake-up, use these values defined in the **WINUSB_DEVICE_TRAITS** enumeration:

This code example sends a control transfer request to a get the status of the device. The example sends the request synchronously by calling a helper method named SendControlTransferSynchronously.

```cpp
HRESULT
CDevice::GetDeviceStatus ()
{

    HRESULT hr = S_OK;

    USHORT deviceStatus;
    ULONG bytesTransferred;

    TraceEvents(TRACE_LEVEL_INFORMATION,
                DRIVER_ALL_INFO,
                "%!FUNC!: entry");

    // Setup the control packet.

    WINUSB_CONTROL_SETUP_PACKET setupPacket;

    WINUSB_CONTROL_SETUP_PACKET_INIT_GET_STATUS(
                                      &setupPacket,
                                      BmRequestToDevice,
                                      0);

    hr = SendControlTransferSynchronously(
                 &(setupPacket.WinUsb),
                 & deviceStatus,
                 sizeof(USHORT),
                 &bytesReturned
                );

     if (SUCCEEDED(hr))
    {
        if (deviceStatus & USB_GETSTATUS_SELF_POWERED)
        {
             m_Self_Powered = true;
        } 
        if (deviceStatus & USB_GETSTATUS_REMOTE_WAKEUP_ENABLED)
        {
             m_remote_wake-enabled = true;
        }
    }

    return hr;
 }
```

The following code example shows the implementation of the helper method named SendControlTransferSynchronously. This method sends a request synchronously.

```cpp
HRESULT
CDevice::SendControlTransferSynchronously(
    _In_ PWINUSB_SETUP_PACKET SetupPacket,
    _Inout_ PBYTE Buffer,
    _In_ ULONG BufferLength,
    _Out_ PULONG LengthTransferred
    )
{
    HRESULT hr = S_OK;
    IWDFIoRequest *pWdfRequest = NULL;
    IWDFDriver * FxDriver = NULL;
    IWDFMemory * FxMemory = NULL;
    IWDFRequestCompletionParams * FxComplParams = NULL;
    IWDFUsbRequestCompletionParams * FxUsbComplParams = NULL;

    *LengthTransferred = 0;

    hr = m_FxDevice->CreateRequest( NULL, //pCallbackInterface
                                    NULL, //pParentObject
                                    &pWdfRequest);

    if (SUCCEEDED(hr))
    {
        m_FxDevice->GetDriver(&FxDriver);

        hr = FxDriver->CreatePreallocatedWdfMemory( Buffer,
                                                    BufferLength,
                                                    NULL,        //pCallbackInterface
                                                    pWdfRequest, //pParetObject
                                                    &FxMemory );
    }

    if (SUCCEEDED(hr))
    {
        hr = m_pIUsbTargetDevice->FormatRequestForControlTransfer( pWdfRequest,
                                                                   SetupPacket,
                                                                   FxMemory,
                                                                   NULL); //TransferOffset
    }

    if (SUCCEEDED(hr))
    {
        hr = pWdfRequest->Send( m_pIUsbTargetDevice,
                                WDF_REQUEST_SEND_OPTION_SYNCHRONOUS,
                                0); //Timeout
    }

    if (SUCCEEDED(hr))
    {
        pWdfRequest->GetCompletionParams(&FxComplParams);

        hr = FxComplParams->GetCompletionStatus();
    }

    if (SUCCEEDED(hr))
    {
        HRESULT hrQI = FxComplParams->QueryInterface(IID_PPV_ARGS(&FxUsbComplParams));
        WUDF_TEST_DRIVER_ASSERT(SUCCEEDED(hrQI));

        WUDF_TEST_DRIVER_ASSERT( WdfUsbRequestTypeDeviceControlTransfer ==
                            FxUsbComplParams->GetCompletedUsbRequestType() );

        FxUsbComplParams->GetDeviceControlTransferParameters( NULL,
                                                             LengthTransferred,
                                                             NULL,
                                                             NULL );
    }

    SAFE_RELEASE(FxUsbComplParams);
    SAFE_RELEASE(FxComplParams);
    SAFE_RELEASE(FxMemory);

    pWdfRequest->DeleteWdfObject(); 
    SAFE_RELEASE(pWdfRequest);

    SAFE_RELEASE(FxDriver);

    return hr;
}
```

If you are using Winusb.sys as the function driver for your device, you can send control transfers from an application. To format the setup packet in WinUSB, use the UMDF helper macros and structures, described in the table in this article. To send the request, call [WinUsb_ControlTransfer](/windows/win32/api/winusb/nf-winusb-winusb_controltransfer) function.
