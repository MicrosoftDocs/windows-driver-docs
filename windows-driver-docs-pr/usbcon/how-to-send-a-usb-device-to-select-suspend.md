---
title: USB Client Driver Verifier
description: This article describes the USB client driver verifier feature of the USB 3.0 driver stack that enables the client driver to test certain failure cases.
ms.date: 01/16/2024
---

# USB client driver verifier

This article describes the USB client driver verifier feature of the USB 3.0 driver stack that enables the client driver to test certain failure cases.

## What is the USB client driver verifier

The *USB client driver verifier* is a feature of the USB 3.0 driver stack, included in Windows 8. When the verifier is enabled, the USB driver stack fails or modifies certain operations performed by a client driver. Those failures simulate error conditions that might be otherwise difficult to find and can lead to undesirable results later. The simulated failures give you the opportunity to make sure that your driver is able to deal with failures gracefully. The client can deal with errors through error handling code or exercise a different code path.

For example, a client driver supports I/O operations through static streams of a bulk endpoint. By using the verifier, you can make sure that driver's streams logic works regardless of the number of streams supported by various host controllers. To simulate that scenario, you can use the **UsbVerifierStaticStreamCountOverride** setting (discussed later). Each time the driver calls **[USBD_QueryUsbCapability](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_queryusbcapability)** to determine the maximum number of static streams that the host controller supports, the routine returns a different value.

> [!IMPORTANT]
> The USB client driver verifier only tests your driver against various xHCI controllers. It simulates some of the inherent 2.0 controller behaviors such as lack of chained MDL support. However, we recommend that you must test your client drivers with the USB 2.0 controllers and not use this tool as a replacement for the same.

The Windows Hardware Lab Kit (HLK) tests can be used for additional testing of Systems, USB host controllers, hubs, and devices. These tests cover basic device functionality, reliability, and compatibility with Windows. For more information, see [Windows Hardware Lab Kit (HLK) Tests for USB](windows-hardware-certification-kit-tests-for-usb.md).

## How to enable the USB client driver verifier

In order to use the USB client driver verifier, enable it on your target computer on which running Windows 8. The target computer must have an xHCI controller to which the USB device is connected.

The USB client driver verifier is automatically enabled when you enable the [Driver Verifier](../devtest/driver-verifier.md) for the client driver. Alternatively, you can enable the verifier by setting this registry entry.

> [!NOTE]
> Enabling [The Windows Driver Foundation (WDF) Verifier control application (WdfVerifier.exe)](../devtest/wdf-verifier-control-application.md) does not enable the USB client driver verifier automatically.

```cpp
HKEY_LOCAL_MACHINE
   SYSTEM
      CurrentControlSet
         services
            <Client Driver>
               Parameters
                  UsbVerifierEnabled (DWORD)
```

The **UsbVerifierEnabled** registry entry takes a DWORD value. When **UsbVerifierEnabled** is 1, the USB client driver verifier is enabled; 0 disables it. If the [Driver Verifier](../devtest/driver-verifier.md) is enabled for the client driver and **UsbVerifierEnabled** is 0, the USB client driver verifier is disabled.

## Configuration settings for the USB client driver verifier

When the verifier is enabled, the USB driver stack keeps track of URBs that the client driver allocates by calling **USBD_xxxUrbAllocate** routines (see [USB Routines](/windows-hardware/drivers/ddi/_usbref/#client)). If the client driver leaks any URB, the USB driver stack uses that information to cause a bugcheck through the [Driver Verifier](../devtest/driver-verifier.md). In that case, use the **!usbanalyze -v** command to determine the cause of the leak.

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

The *\<USB client driver verifier setting>* registry entry takes a DWORD value.
If you add, modify, or remove any setting, you must re-enumerate the device with the system to apply the setting.

This table shows the possible values for *\<USB client driver verifier setting>*. The settings apply to the client driver specified under the **services** key.

| USB client driver verifier setting | Choose one of these possible values: | Use to simulate... |
|---|---|---|
| **UsbVerifierFailRegistration**<br/><br/>Fails the client driver's calls to these routines:<br/><br/><ul><li>**[WdfUsbTargetDeviceCreateWithParameters](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters)**</li><li>**[USBD_CreateHandle](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_createhandle)**</li></ul> | <ul><li>0: Setting is disabled.</li><li>1: The call always fails.</li><li>*N*: The call fails with a probability of 1/*N*, where *N* is a hex value between 1 to 0x7FF. For example, if *N* is 10. The call fails once every 10 calls.</li></ul> | **Client driver registration failure.**<br/><br/>One of the initialization tasks of a client driver is to register itself with the underlying driver stack. The registration is required in several subsequent calls.<br/><br/>For example, the client driver calls **[USBD_CreateHandle](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_createhandle)** for registration. Let's say the driver assumes that the routine always returns STATUS_SUCCESS, and does not implement code to handle failure. If the routine returns an error NTSTATUS code, the driver can inadvertently ignore the error and proceed with the subsequent calls by using an invalid USBD handle.<br/><br/>The setting allows you to fail the call so that can you can test the failure code path.<br/><br/>Expected client driver behavior when registration fails:<br/><br/><ul><li>The driver is not expected continue to function as normal.</li><li>The driver must not cause a system crash or become unresponsive by choosing to ignore this failure.</li></ul> |
| **UsbVerifierFailChainedMdlSupport**<br/><br/>Fails the client driver's calls to these routines when the caller passes GUID_USB_CAPABILITY_CHAINED_MDLS in the *CapabilityType* parameter.<br/><br/><ul><li>**[USBD_QueryUsbCapability](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_queryusbcapability)**</li><li>**[WdfUsbTargetDeviceQueryUsbCapability](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicequeryusbcapability)**</li></ul> | <ul><li>0: Setting is disabled.</li><li>1: The call always fails.</li><li>*N*: The call fails with a probability of 1/*N*, where *N* is a hex value between 1 to 0x7FF. For example, if *N* is 10. The call fails once every 10 calls.</li></ul> | **Communication with a host controller that does not support chained MDLs.**<br/><br/>In order for the client driver to send chained MDLs (see [MDL](../kernel/using-mdls.md)), the USB driver stack and the host controller must support them.<br/><br/>This setting allows you to test the code that is executed when the client driver sends chained MDL requests to the device that is connected to a host controller that does not support them. The call fails regardless of whether the host controller supports chained MDLs.<br/><br/>For more information about chained MDLs support in the USB driver stack, see [How to Send Chained MDLs](how-to-send-chained-mdls.md).<br/><br/>Expected client driver behavior when the host controller does not support chained MDLs:<br/><br/><ul><li>The driver is expected continue to perform I/O transfers without using chained MDLs. By doing so, you will also make sure that your driver works with USB 2.0 host controllers because those controllers do not support chained MDLs.</li><li>The driver must not cause a system crash or become unresponsive by choosing to ignore this failure.</li></ul> |
| **UsbVerifierFailStaticStreamsSupport**<br/><br/>Fails the client driver's calls to these routines when the caller passes GUID_USB_CAPABILITY_STATIC_STREAMS in the *CapabilityType* parameter.<br/><br/><ul><li>**[USBD_QueryUsbCapability](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_queryusbcapability)**</li><li>**[WdfUsbTargetDeviceQueryUsbCapability](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicequeryusbcapability)**</li></ul> | <ul><li>0: Setting is disabled.</li><li>1: The call always fails.</li><li>*N*: The call fails with a probability of 1/*N*, where *N* is a hex value between 1 to 0x7FF. For example, if *N* is 10. The call will fail once every 10 calls.</li></ul> | **Communication with a host controller that does not support static streams.**<br/><br/>In order for a client driver to send I/O transfers through static streams of a bulk endpoint, the host controller must support streams.<br/><br/>If the device is connected to a host controller that does not support streams, and the driver attempts to perform stream I/O transfers, those transfers will fail. This setting allows you to test the code in case of such a failure.<br/><br/>Expected client driver behavior when the host controller does not support static streams:<br/><br/><ul><li>If the client driver wants to work with an xHCI controller that does not support streams, your device must be able to work without using stream-enabled bulk endpoints.</li><li>The driver must not cause a system crash or become unresponsive by choosing to ignore this failure.</li></ul> |
| **UsbVerifierStaticStreamCountOverride**<br/><br/>Changes the value received in the *OutputBuffer* parameter when the client calls to these routines with GUID_USB_CAPABILITY_STATIC_STREAMS.<ul><li>**[USBD_QueryUsbCapability](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_queryusbcapability)**</li><li>**[WdfUsbTargetDeviceQueryUsbCapability](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicequeryusbcapability)**</li></ul><br/><br/>The *OutputBuffer* value indicates the maximum number of static streams that the host controller supports. | <ul><li>0: Setting is disabled.</li><li>1: The verifier chooses the *OutputBuffer* value randomly. This value is useful for stress testing because the *OutputBuffer* value is not repeated and the call is tested with more variations.</li><li>*N*: Specifies the *OutputBuffer* value.<br/><br/>When the flag is enabled with *N* value, *N* must be less than the maximum number of streams that the USB driver stack supports. Therefore, before setting this flag, you must have retrieved the actual value through a successful call.<br/><br/>If *N* is greater than the maximum number of streams, the setting is ignored.</li></ul> | **Communication with various host controllers, each supporting a different value of maximum number of streams.**<br/><br/>By using this setting, you can make sure that driver's streams logic works regardless of the number of streams supported by various host controllers.<br/><br/>The number of streams that you can use for I/O transfer will be limited by the number of streams that the host controller supports.<br/><br/>For information about how to support static streams in your client driver, see [How to Open and Close Static Streams in a USB Bulk Endpoint](how-to-open-streams-in-a-usb-endpoint.md).<br/><br/>Expected client driver behavior when the host controller supports fewer streams than the endpoint:<br/><br/><ul><li>The client driver can choose to perform data transfers with fewer numbers of streams.</li><li>The driver must not cause a system crash or become unresponsive by choosing to ignore this failure.</li></ul> |
| **UsbVerifierFailEnableStaticStreams**<br/><br/>Fails the client driver's open static-streams request (URB_FUNCTION_OPEN_STATIC_STREAMS). | <ul><li>0: Setting is disabled.</li><li>1: The request always fails.</li><li>*N*: The request fails with a probability of 1/*N*, where *N* is a hex value between 1 to 0x7FF. For example, if *N* is 10. The request fails once every 10 calls.</li></ul><br/><br/>**NOTE:** The open static-streams request fails if the previous call to **[USBD_QueryUsbCapability](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_queryusbcapability)** or **[WdfUsbTargetDeviceQueryUsbCapability](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicequeryusbcapability)** failed. | **Communication with a host controller that supports static streams but the request fails due to other reasons.**<br/><br/>For instance, your device is connected to a host controller that supports streams. The client driver sends an open streams request with a number (of streams to open) that exceeds the maximum number of streams supported by the host controller. The USB driver stack will fail such a request.<br/><br/>By using this setting, you can test the error handling code for open streams request failure.<br/><br/>Expected client driver behavior when an open-streams request fails:<br/><br/><ul><li>The driver is not expected continue to function as normal.</li><li>The driver must not cause a system crash or become unresponsive by choosing to ignore this failure.</li></ul> |

## Related topics

- **[USBD_CreateHandle](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_createhandle)**
- **[USBD_QueryUsbCapability](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_queryusbcapability)**
- [How to Open and Close Static Streams in a USB Bulk Endpoint](how-to-open-streams-in-a-usb-endpoint.md)
- [How to Send Chained MDLs](how-to-send-chained-mdls.md)
- [Overview of Microsoft USB Test Tool (MUTT) devices](./microsoft-usb-test-tool--mutt--devices.md)
