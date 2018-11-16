---
Description: This topic describes the USB client driver verifier feature of the USB 3.0 driver stack that enables the client driver to test certain failure cases.
title: USB client driver verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB client driver verifier


This topic describes the USB client driver verifier feature of the USB 3.0 driver stack that enables the client driver to test certain failure cases.

-   [What is the USB client driver verifier](#what-is--the-usb-client-driver-verifier)
-   [How to enable the USB client driver verifier](#how-to-enable-the-usb-client-driver-verifier)
-   [Configuration settings for the USB client driver verifier](#configuration--settings-for-the-usb-client-driver-verifier)

## What is the USB client driver verifier


The *USB client driver verifier* is a feature of the USB 3.0 driver stack, included in Windows 8. When the verifier is enabled, the USB driver stack fails or modifies certain operations performed by a client driver. Those failures simulate error conditions that might be otherwise difficult to find and can lead to undesirable results later. The simulated failures give you the opportunity to make sure that your driver is able to deal with failures gracefully. The client can deal with errors through error handling code or exercise a different code path.

For example, a client driver supports I/O operations through static streams of a bulk endpoint. By using the verifier, you can make sure that driver's streams logic works regardless of the number of streams supported by various host controllers. To simulate that scenario, you can use the **UsbVerifierStaticStreamCountOverride** setting (discussed later). Each time the driver calls [**USBD\_QueryUsbCapability**](https://msdn.microsoft.com/library/windows/hardware/hh406230) to determine the maximum number of static streams that the host controller supports, the routine returns a different value.

**Important**  The USB client driver verifier only tests your driver against various xHCI controllers. It simulates some of the inherent 2.0 controller behaviors such as lack of chained MDL support. However, we recommend that you must test your client drivers with the USB 2.0 controllers and not use this tool as a replacement for the same.

 

The Windows Hardware Certification Kit includes an automated test that runs the simulated test cases. For more information, see [USB (USBDEX) Verifier Test](https://msdn.microsoft.com/library/windows/hardware/hh998558.aspx).

## How to enable the USB client driver verifier


In order to use the USB client driver verifier, enable it on your target computer on which running Windows 8. The target computer must have an xHCI controller to which the USB device is connected.

The USB client driver verifier is automatically enabled when you enable the [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) for the client driver. Alternatively, you can enable the verifier by setting this registry entry.

**Note**  Enabling [The Windows Driver Foundation (WDF) Verifier control application (WdfVerifier.exe)](https://msdn.microsoft.com/library/windows/hardware/ff556129) does not enable the USB client driver verifier automatically.

 

```cpp
HKEY_LOCAL_MACHINE
   SYSTEM
      CurrentControlSet
         services
            <Client Driver>
               Parameters
                  UsbVerifierEnabled (DWORD)
```

The **UsbVerifierEnabled** registry entry takes a DWORD value. When **UsbVerifierEnabled** is 1, the USB client driver verifier is enabled; 0 disables it. If the [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) is enabled for the client driver and **UsbVerifierEnabled** is 0, the USB client driver verifier is disabled.

## Configuration settings for the USB client driver verifier


When the verifier is enabled, the USB driver stack keeps track of URBs that the client driver allocates by calling **USBD\_xxxUrbAllocate** routines (see [USB Routines](https://msdn.microsoft.com/library/windows/hardware/ff540134#client)). If the client driver leaks any URB, the USB driver stack uses that information to cause a bugcheck through the [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448). In that case, use the **!usbanalyze -v** command to determine the cause of the leak.

Additionally and optionally, you can configure the USB client driver verifier to modify or fail specific routines and specify how often the routine must fail. To configure the verifier, set the registry entries as shown here:

```cpp
HKEY_LOCAL_MACHINE
   SYSTEM
      CurrentControlSet
         services
            <Client driver>
               Parameters
                  <USB client driver verifier setting> (DWORD)
```

The *&lt;USB client driver verifier setting&gt;* registry entry takes a DWORD value.
If you add, modify, or remove any setting, you must re-enumerate the device with the system to apply the setting.

This table shows the possible values for *&lt;USB client driver verifier setting&gt;*. The settings apply to the client driver specified under the **services** key.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>USB client driver verifier setting</th>
<th>Choose one of these possible values:</th>
<th>Use to simulate...</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>UsbVerifierFailRegistration</strong></p>
<p>Fails the client driver&#39;s calls to these routines:</p>
<ul>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh439428" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceCreateWithParameters&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439428)"><strong>WdfUsbTargetDeviceCreateWithParameters</strong></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh406241" data-raw-source="[&lt;strong&gt;USBD_CreateHandle&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406241)"><strong>USBD_CreateHandle</strong></a></li>
</ul></td>
<td><ul>
<li>0: Setting is disabled.</li>
<li>1: The call always fails.</li>
<li><em>N</em>: The call fails with a probability of 1/<em>N</em>, where <em>N</em> is a hex value between 1 to 0x7FF. For example, if <em>N</em> is 10. The call fails once every 10 calls.</li>
</ul></td>
<td><p><strong>Client driver registration failure.</strong></p>
<p>One of the initialization tasks of a client driver is to register itself with the underlying driver stack. The registration is required in several subsequent calls.</p>
<p>For example, the client driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh406241" data-raw-source="[&lt;strong&gt;USBD_CreateHandle&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406241)"><strong>USBD_CreateHandle</strong></a> for registration. Let&#39;s say the driver assumes that the routine always returns STATUS_SUCCESS, and does not implement code to handle failure. If the routine returns an error NTSTATUS code, the driver can inadvertently ignore the error and proceed with the subsequent calls by using an invalid USBD handle.</p>
<p>The setting allows you to fail the call so that can you can test the failure code path.</p>
<p>Expected client driver behavior when registration fails:</p>
<ul>
<li><p>The driver is not expected continue to function as normal.</p></li>
<li><p>The driver must not cause a system crash or become unresponsive by choosing to ignore this failure.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p><strong>UsbVerifierFailChainedMdlSupport</strong></p>
<p>Fails the client driver&#39;s calls to these routines when the caller passes GUID_USB_CAPABILITY_CHAINED_MDLS in the <em>CapabilityType</em> parameter.</p>
<ul>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh406230" data-raw-source="[&lt;strong&gt;USBD_QueryUsbCapability&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406230)"><strong>USBD_QueryUsbCapability</strong></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh439434" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceQueryUsbCapability&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439434)"><strong>WdfUsbTargetDeviceQueryUsbCapability</strong></a></li>
</ul></td>
<td><ul>
<li>0: Setting is disabled.</li>
<li>1: The call always fails.</li>
<li><em>N</em>: The call fails with a probability of 1/<em>N</em>, where <em>N</em> is a hex value between 1 to 0x7FF. For example, if <em>N</em> is 10. The call fails once every 10 calls.</li>
</ul></td>
<td><p><strong>Communication with a host controller that does not support chained MDLs.</strong></p>
<p>In order for the client driver to send chained MDLs (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565421" data-raw-source="[MDL](https://msdn.microsoft.com/library/windows/hardware/ff565421)">MDL</a>), the USB driver stack and the host controller must support them.</p>
<p>This setting allows you to test the code that is executed when the client driver sends chained MDL requests to the device that is connected to a host controller that does not support them. The call fails regardless of whether the host controller supports chained MDLs.</p>
<p>For more information about chained MDLs support in the USB driver stack, see <a href="how-to-send-chained-mdls.md" data-raw-source="[How to Send Chained MDLs](how-to-send-chained-mdls.md)">How to Send Chained MDLs</a>.</p>
<p>Expected client driver behavior when the host controller does not support chained MDLs:</p>
<ul>
<li><p>The driver is expected continue to perform I/O transfers without using chained MDLs. By doing so, you will also make sure that your driver works with USB 2.0 host controllers because those controllers do not support chained MDLs.</p></li>
<li><p>The driver must not cause a system crash or become unresponsive by choosing to ignore this failure.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p><strong>UsbVerifierFailStaticStreamsSupport</strong></p>
<p>Fails the client driver&#39;s calls to these routines when the caller passes GUID_USB_CAPABILITY_STATIC_STREAMS in the <em>CapabilityType</em> parameter.</p>
<ul>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh406230" data-raw-source="[&lt;strong&gt;USBD_QueryUsbCapability&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406230)"><strong>USBD_QueryUsbCapability</strong></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh439434" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceQueryUsbCapability&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439434)"><strong>WdfUsbTargetDeviceQueryUsbCapability</strong></a></li>
</ul></td>
<td><ul>
<li>0: Setting is disabled.</li>
<li>1: The call always fails.</li>
<li><em>N</em>: The call fails with a probability of 1/<em>N</em>, where <em>N</em> is a hex value between 1 to 0x7FF. For example, if <em>N</em> is 10. The call will fail once every 10 calls.</li>
</ul></td>
<td><p><strong>Communication with a host controller that does not support static streams.</strong></p>
<p>In order for a client driver to send I/O transfers through static streams of a bulk endpoint, the host controller must support streams.</p>
<p>If the device is connected to a host controller that does not support streams, and the driver attempts to perform stream I/O transfers, those transfers will fail. This setting allows you to test the code in case of such a failure.</p>
<p>Expected client driver behavior when the host controller does not support static streams:</p>
<ul>
<li><p>If the client driver wants to work with an xHCI controller that does not support streams, your device must be able to work without using stream-enabled bulk endpoints.</p></li>
<li><p>The driver must not cause a system crash or become unresponsive by choosing to ignore this failure.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p><strong>UsbVerifierStaticStreamCountOverride</strong></p>
Changes the value received in the <em>OutputBuffer</em> parameter when the client calls to these routines with GUID_USB_CAPABILITY_STATIC_STREAMS.
<ul>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh406230" data-raw-source="[&lt;strong&gt;USBD_QueryUsbCapability&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406230)"><strong>USBD_QueryUsbCapability</strong></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh439434" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceQueryUsbCapability&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439434)"><strong>WdfUsbTargetDeviceQueryUsbCapability</strong></a></li>
</ul>
<p>The <em>OutputBuffer</em> value indicates the maximum number of static streams that the host controller supports.</p></td>
<td><ul>
<li>0: Setting is disabled.</li>
<li>1: The verifier chooses the <em>OutputBuffer</em> value randomly. This value is useful for stress testing because the <em>OutputBuffer</em> value is not repeated and the call is tested with more variations.</li>
<li><p><em>N</em>: Specifies the <em>OutputBuffer</em> value.</p>
<p>When the flag is enabled with <em>N</em> value, <em>N</em> must be less than the maximum number of streams that the USB driver stack supports. Therefore, before setting this flag, you must have retrieved the actual value through a successful call.</p>
<p>If <em>N</em> is greater than the maximum number of streams, the setting is ignored.</p></li>
</ul></td>
<td><p><strong>Communication with various host controllers, each supporting a different value of maximum number of streams.</strong></p>
<p>By using this setting, you can make sure that driver&#39;s streams logic works regardless of the number of streams supported by various host controllers.</p>
<p>The number of streams that you can use for I/O transfer will be limited by the number of streams that the host controller supports.</p>
<p>For information about how to support static streams in your client driver, see <a href="how-to-open-streams-in-a-usb-endpoint.md" data-raw-source="[How to Open and Close Static Streams in a USB Bulk Endpoint](how-to-open-streams-in-a-usb-endpoint.md)">How to Open and Close Static Streams in a USB Bulk Endpoint</a>.</p>
<p>Expected client driver behavior when the host controller supports fewer streams than the endpoint:</p>
<ul>
<li><p>The client driver can choose to perform data transfers with fewer numbers of streams.</p></li>
<li><p>The driver must not cause a system crash or become unresponsive by choosing to ignore this failure.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p><strong>UsbVerifierFailEnableStaticStreams</strong></p>
<p>Fails the client driver&#39;s open static-streams request (URB_FUNCTION_OPEN_STATIC_STREAMS).</p></td>
<td><ul>
<li>0: Setting is disabled.</li>
<li>1: The request always fails.</li>
<li><em>N</em>: The request fails with a probability of 1/<em>N</em>, where <em>N</em> is a hex value between 1 to 0x7FF. For example, if <em>N</em> is 10. The request fails once every 10 calls.</li>
</ul>
<div class="alert">
<strong>Note</strong>  The open static-streams request fails if the previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh406230" data-raw-source="[&lt;strong&gt;USBD_QueryUsbCapability&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406230)"><strong>USBD_QueryUsbCapability</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/hh439434" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceQueryUsbCapability&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439434)"><strong>WdfUsbTargetDeviceQueryUsbCapability</strong></a> failed.
</div>
<div>
 
</div></td>
<td><p><strong>Communication with a host controller that supports static streams but the request fails due to other reasons.</strong></p>
<p>For instance, your device is connected to a host controller that supports streams. The client driver sends an open streams request with a number (of streams to open) that exceeds the maximum number of streams supported by the host controller. The USB driver stack will fail such a request.</p>
<p>By using this setting, you can test the error handling code for open streams request failure.</p>
<p>Expected client driver behavior when an open-streams request fails:</p>
<ul>
<li><p>The driver is not expected continue to function as normal.</p></li>
<li><p>The driver must not cause a system crash or become unresponsive by choosing to ignore this failure.</p></li>
</ul></td>
</tr>
</tbody>
</table>

 

## Related topics
[**USBD\_CreateHandle**](https://msdn.microsoft.com/library/windows/hardware/hh406241)  
[**USBD\_QueryUsbCapability**](https://msdn.microsoft.com/library/windows/hardware/hh406230)  
[How to Open and Close Static Streams in a USB Bulk Endpoint](how-to-open-streams-in-a-usb-endpoint.md)  
[How to Send Chained MDLs](how-to-send-chained-mdls.md)  
[USB Diagnostics and Test Guide](usb-driver-testing-guide.md)  



