---
Description: Create a user-mode service that communicates with GenericUSBFn.sys by sending I/O control code (IOCTL) requests.
title: Communicating with GenericUSBFn.sys from a user-mode service
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Communicating with GenericUSBFn.sys from a user-mode service 


All user-mode requests are sent to the Microsoft-provided kernel-mode driver GenericUSBFn.sys. You can create a user-mode service that communicates with GenericUSBFn.sys by sending these I/O control code (IOCTL), and GenericUSBFn.sys handles kernel-mode communication with the USB function drivers.

The IOCTLs declared in [Genericusbfnioctl.h](https://docs.microsoft.com/windows/desktop/api/genericusbfnioctl/) are used for communicating with GenericUSBFn.sys from a user-mode service.


The following steps describe how you can define a USB interface service that interacts with GenericUSBFn.sys to communicate with the USB function drivers:

1. On startup, the service listens for the device interface arrival of the interface. The device interface GUID is the InterfaceGUID value that is declared in the registry under the OEM-defined subkey of HKEY_LOCAL_MACHINE\CurrentControlSet\Control\USBFN\Interfaces. There are two common methods for listening to device arrival:
    - Trigger start the service. For more information, see Service Trigger Events. 
    - Register for device interface arrival. For more information, see the CM_Register_Notification function. 
2. After the interface arrives, the service opens a handle to the device: 
    - Get the symbolic name for the device by calling the CM_Get_Device_Interface_List function. Specify the device interface GUID that is declared in the InterfaceGUID value in the registry.
    - After you have the symbolic name for the device, open a handle to the device by using CreateFile. 
3. The service issues IOCTL_GENERICUSBFN_GET_CLASS_INFO to retrieve information about the available pipes, as configured in the registry. 
4. After the service is ready to communicate, it issues IOCTL_GENERICUSBFN_ACTIVATE_USB_BUS. After all class drivers are activated, the USB function class extension can connect to the host. 
5. To receive USB notifications, the service issues IOCTL_GENERICUSBFN_BUS_EVENT_NOTIFICATION. This IOCTL completes when a new USB event has occurred. Events (USBFN_EVENT) of particular interest include:
6. UsbfnEventReset: This is used to determine the speed of the connected USB device. 
7. UsbfnEventConfigured: The service can now issue transfer requests. 
8. UsbfnEventSetupPacket: The USB function class extension has received an interface-specific setup packet (bmRequestType.Type == BMREQUEST_CLASS). The service should reply to the setup packet by issuing a transfer request in pipe 0, followed by a handshake request (IOCTL_GENERICUSBFN_CONTROL_STATUS_HANDSHAKE_OUT) in the opposite direction on pipe 0. 
9. After the UsbfnEventConfigured event is received, the service can begin issuing transfer requests using IOCTL_GENERICUSBFN_TRANSFER_IN, IOCTL_GENERICUSBFN_TRANSFER_IN_APPEND_ZERO_PKT, and IOCTL_GENERICUSBFN_TRANSFER_OUT. 
