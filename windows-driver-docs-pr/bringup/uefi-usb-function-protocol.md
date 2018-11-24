---
title: UEFI USB function protocol
description: UEFI USB function protocol
ms.assetid: eac35cf4-82b4-4d7e-ae69-8f506f12ae5d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UEFI USB function protocol


**Note**   Some information in this section may apply only to Windows 10 Mobile and certain processor architectures.

 

The USB function protocol defines a generic and lightweight USB transport in the UEFI environment. This protocol is used by flashing tools, USB mass storage mode, and other tools that require bidirectional communication between a device that is booted into the UEFI environment and a host computer.

## EFI\_USBFN\_IO\_PROTOCOL


Like other UEFI device drivers, the entry point for a USB function driver attaches **EFI\_DRIVER\_BINDING\_PROTOCOL** to image handle of **EFI\_USBFN\_IO\_PROTOCOL** driver

The driver binding protocol contains three services, **Supported**, **Start**, and **Stop**. The **Supported** function must test to see if this driver supports a given controller. The **Start** function must supply power to the USB controller if needed, initialize hardware and internal data structures, and then return. The port must not be activated by this function. The **Stop** function must disable the device by resetting the run/stop bit and power off the USB controller if needed.

**GUID**

```cpp
// {32D2963A-FE5D-4f30-B633-6E5DC55803CC}
#define EFI_USBFN_IO_PROTOCOL_GUID \
  {0x32d2963a, 0xfe5d, 0x4f30, 0xb6, 0x33, 0x6e, 0x5d, 0xc5, \
   0x58, 0x3, 0xcc };
```

**Revision number**

```cpp
#define EFI_USBFN_IO_PROTOCOL_REVISION   0x00010002
```

**Protocol interface structure**

```cpp
typedef struct _EFI_USBFN_IO_PROTOCOL 
{
  UINT32                                      Revision;
  EFI_USBFN_IO_DETECT_PORT                    DetectPort;
  EFI_USBFN_IO_CONFIGURE_ENABLE_ENDPOINTS     ConfigureEnableEndpoints;
  EFI_USBFN_IO_GET_ENDPOINT_MAXPACKET_SIZE    GetEndpointMaxPacketSize;
  EFI_USBFN_IO_GET_DEVICE_INFO                GetDeviceInfo;
  EFI_USBFN_IO_GET_VENDOR_ID_PRODUCT_ID       GetVendorIdProductId;
  EFI_USBFN_IO_ABORT_TRANSFER                 AbortTransfer;
  EFI_USBFN_IO_GET_ENDPOINT_STALL_STATE       GetEndpointStallState; 
  EFI_USBFN_IO_SET_ENDPOINT_STALL_STATE       SetEndpointStallState;
  EFI_USBFN_IO_EVENTHANDLER                   EventHandler;
  EFI_USBFN_IO_TRANSFER                       Transfer;
  EFI_USBFN_IO_GET_MAXTRANSFER_SIZE           GetMaxTransferSize;
  EFI_USBFN_IO_ALLOCATE_TRANSFER_BUFFER       AllocateTransferBuffer;
  EFI_USBFN_IO_FREE_TRANSFER_BUFFER           FreeTransferBuffer;
  EFI_USBFN_IO_START_CONTROLLER               StartController;
  EFI_USBFN_IO_STOP_CONTROLLER                StopController;
  EFI_USBFN_IO_SET_ENDPOINT_POLICY            SetEndpointPolicy;
  EFI_USBFN_IO_GET_ENDPOINT_POLICY            GetEndpointPolicy;
  EFI_USBFN_IO_CONFIGURE_ENABLE_ENDPOINTS_EX  ConfigureEnableEndpointsEx;
} EFI_USBFN_IO_PROTOCOL;
```

### Members

<a href="" id="revision"></a>**Revision**  
The revision to which the **EFI\_USBFN\_IO\_PROTOCOL** adheres. All future revisions must be backward compatible. If a future version is not backward compatible, a different GUID must be used.

<a href="" id="detectport"></a>**DetectPort**  
Returns information about USB port type. See [EFI\_USBFN\_IO\_PROTOCOL.DetectPort](efi-usbfn-io-protocoldetectport.md).

<a href="" id="configureenableendpoints"></a>**ConfigureEnableEndpoints**  
Initialize all endpoints based on supplied device and configuration descriptors. Enable the device by setting the run/stop bit. See [EFI\_USBFN\_IO\_PROTOCOL.ConfigureEnableEndpoints](efi-usbfn-io-protocolconfigureenableendpoints.md).

<a href="" id="getendpointmaxpacketsize"></a>**GetEndpointMaxPacketSize**  
Returns the maximum packet size of the specified endpoint. See [EFI\_USBFN\_IO\_PROTOCOL.GetEndpointMaxPacketSize](efi-usbfn-io-protocolgetendpointmaxpacketsize.md).

<a href="" id="getdeviceinfo"></a>**GetDeviceInfo**  
Returns device specific information based on the supplied identifier as a Unicode string. See [EFI\_USBFN\_IO\_PROTOCOL.GetDeviceInfo](efi-usbfn-io-protocolgetdeviceinfo.md).

<a href="" id="getvendoridproductid"></a>**GetVendorIdProductId**  
Returns vendor-id and product-id of the device. See [EFI\_USBFN\_IO\_PROTOCOL.GetVendorIdProductId](efi-usbfn-io-protocolgetvendoridproductid.md).

<a href="" id="aborttransfer"></a>**AbortTransfer**  
Aborts transfer on the specified endpoint. See [EFI\_USBFN\_IO\_PROTOCOL.AbortTransfer](efi-usbfn-io-protocolaborttransfer.md).

<a href="" id="getendpointstallstate"></a>**GetEndpointStallState**  
Returns the stall state on the specified endpoint. See [EFI\_USBFN\_IO\_PROTOCOL.GetEndpointStallState](efi-usbfn-io-protocolgetendpointstallstate.md).

<a href="" id="setendpointstalls"></a>**SetEndpointStallS**  
Sets or clears the stall state on the specified endpoint. See [EFI\_USBFN\_IO\_PROTOCOL.SetEndpointStallState](efi-usbfn-io-protocolsetendpointstallstate.md).

<a href="" id="eventhandler"></a>**EventHandler**  
This function is called repeatedly to receive updates on USB bus states, receive, transmit complete events on endpoints and setup packet on endpoint 0. See [EFI\_USBFN\_IO\_PROTOCOL.EventHandler](efi-usbfn-io-protocoleventhandler.md).

<a href="" id="transfer"></a>**Transfer**  
This function handles transferring data to or from the host on the specified endpoint, depending on the direction specified. See [EFI\_USBFN\_IO\_PROTOCOL.Transfer](efi-usbfn-io-protocoltransfer.md).

<a href="" id="getmaxtransfersize"></a>**GetMaxTransferSize**  
The maximum supported transfer size in bytes. See [EFI\_USBFN\_IO\_PROTOCOL.GetMaxTransferSize](efi-usbfn-io-protocolgetmaxtransfersize.md).

<a href="" id="allocatetransferbuffer"></a>**AllocateTransferBuffer**  
Allocates a transfer buffer of the specified size that satisfies controller requirements. See [EFI\_USBFN\_IO\_PROTOCOL.AllocateTransferBuffer](efi-usbfn-io-protocolallocatetransferbuffer.md).

<a href="" id="freetransferbuffer"></a>**FreeTransferBuffer**  
De-allocates the memory allocated for the transfer buffer by the **AllocateTransferBuffer** function. See [EFI\_USBFN\_IO\_PROTOCOL.FreeTransferBuffer](efi-usbfn-io-protocolfreetransferbuffer.md).

<a href="" id="startcontroller"></a>**StartController**  
Supplies power to the USB controller if needed and initializes hardware and internal data structures. See [EFI\_USBFN\_IO\_PROTOCOL.StartController](efi-usbfn-io-protocolstartcontroller.md). This function is available starting in revision 0x00010001 of the protocol.

<a href="" id="stopcontroller"></a>**StopController**  
Disables the device by resetting the run/stop bit and powers off the USB controller if needed. See [EFI\_USBFN\_IO\_PROTOCOL.StopController](efi-usbfn-io-protocolstopcontroller.md). This function is available starting in revision 0x00010001 of the protocol.

<a href="" id="setendpointpolicy"></a>**SetEndpointPolicy**  
Sets the configuration policy for the specified non-control endpoint. See [EFI\_USBFN\_IO\_PROTOCOL.SetEndpointPolicy](efi-usbfn-io-protocolsetendpointpolicy.md). This function is available starting in revision 0x00010001 of the protocol.

<a href="" id="getendpointpolicy"></a>**GetEndpointPolicy**  
Retrieves the configuration policy for the specified non-control endpoint. See [EFI\_USBFN\_IO\_PROTOCOL.GetEndpointPolicy](efi-usbfn-io-protocolgetendpointpolicy.md). This function is available starting in revision 0x00010001 of the protocol.

<a href="" id="configureenableendpointsex"></a>**ConfigureEnableEndpointsEx**  
Intializes all endpoints by selecting the device and configuration descriptor with the highest speed (up to SuperSpeed) supported by the hardware. Enables the device by setting the run/stop bit. See [EFI\_USBFN\_IO\_PROTOCOL.ConfigureEnableEndpointsEx](efi-usbfn-io-protocol-configureenableendpointsex.md). This function is available starting in revision 0x00010002 of the protocol.

### Remarks

The following table lists the functions that are supported in each version of the **EFI\_USBFN\_IO\_PROTOCOL** protocol.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Revision 0x00010002</th>
<th>Revision 0x00010001</th>
<th>Revision 0x00010000</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>ConfigureEnableEndpointsEx</strong></p></td>
<td><p><strong>DetectPort</strong></p>
<p><strong>ConfigureEnableEndpoints</strong></p>
<p><strong>GetEndpointMaxPacketSize</strong></p>
<p><strong>GetDeviceInfo</strong></p>
<p><strong>GetVendorIdProductId</strong></p>
<p><strong>AbortTransfer</strong></p>
<p><strong>GetEndpointStallState</strong></p>
<p><strong>SetEndpointStallState</strong></p>
<p><strong>EventHandler</strong></p>
<p><strong>Transfer</strong></p>
<p><strong>GetMaxTransferSize</strong></p>
<p><strong>AllocateTransferBuffer</strong></p>
<p><strong>FreeTransferBuffer</strong></p>
<p><strong>StartController</strong></p>
<p><strong>StopController</strong></p>
<p><strong>SetEndpointPolicy</strong></p>
<p><strong>GetEndpointPolicy</strong></p></td>
<td><p><strong>DetectPort</strong></p>
<p><strong>ConfigureEnableEndpoints</strong></p>
<p><strong>GetEndpointMaxPacketSize</strong></p>
<p><strong>GetDeviceInfo</strong></p>
<p><strong>GetVendorIdProductId</strong></p>
<p><strong>AbortTransfer</strong></p>
<p><strong>GetEndpointStallState</strong></p>
<p><strong>SetEndpointStallState</strong></p>
<p><strong>EventHandler</strong></p>
<p><strong>Transfer</strong></p>
<p><strong>GetMaxTransferSize</strong></p>
<p><strong>AllocateTransferBuffer</strong></p>
<p><strong>FreeTransferBuffer</strong></p></td>
</tr>
</tbody>
</table>
